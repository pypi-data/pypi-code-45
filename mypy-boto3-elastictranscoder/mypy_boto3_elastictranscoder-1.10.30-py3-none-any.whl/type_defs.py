"Main interface for elastictranscoder service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientCreateJobInputDetectedPropertiesTypeDef",
    "ClientCreateJobInputEncryptionTypeDef",
    "ClientCreateJobInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientCreateJobInputInputCaptionsCaptionSourcesTypeDef",
    "ClientCreateJobInputInputCaptionsTypeDef",
    "ClientCreateJobInputTimeSpanTypeDef",
    "ClientCreateJobInputTypeDef",
    "ClientCreateJobInputsDetectedPropertiesTypeDef",
    "ClientCreateJobInputsEncryptionTypeDef",
    "ClientCreateJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientCreateJobInputsInputCaptionsCaptionSourcesTypeDef",
    "ClientCreateJobInputsInputCaptionsTypeDef",
    "ClientCreateJobInputsTimeSpanTypeDef",
    "ClientCreateJobInputsTypeDef",
    "ClientCreateJobOutputAlbumArtArtworkEncryptionTypeDef",
    "ClientCreateJobOutputAlbumArtArtworkTypeDef",
    "ClientCreateJobOutputAlbumArtTypeDef",
    "ClientCreateJobOutputCaptionsCaptionFormatsEncryptionTypeDef",
    "ClientCreateJobOutputCaptionsCaptionFormatsTypeDef",
    "ClientCreateJobOutputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientCreateJobOutputCaptionsCaptionSourcesTypeDef",
    "ClientCreateJobOutputCaptionsTypeDef",
    "ClientCreateJobOutputCompositionTimeSpanTypeDef",
    "ClientCreateJobOutputCompositionTypeDef",
    "ClientCreateJobOutputEncryptionTypeDef",
    "ClientCreateJobOutputThumbnailEncryptionTypeDef",
    "ClientCreateJobOutputWatermarksEncryptionTypeDef",
    "ClientCreateJobOutputWatermarksTypeDef",
    "ClientCreateJobOutputTypeDef",
    "ClientCreateJobOutputsAlbumArtArtworkEncryptionTypeDef",
    "ClientCreateJobOutputsAlbumArtArtworkTypeDef",
    "ClientCreateJobOutputsAlbumArtTypeDef",
    "ClientCreateJobOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    "ClientCreateJobOutputsCaptionsCaptionFormatsTypeDef",
    "ClientCreateJobOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientCreateJobOutputsCaptionsCaptionSourcesTypeDef",
    "ClientCreateJobOutputsCaptionsTypeDef",
    "ClientCreateJobOutputsCompositionTimeSpanTypeDef",
    "ClientCreateJobOutputsCompositionTypeDef",
    "ClientCreateJobOutputsEncryptionTypeDef",
    "ClientCreateJobOutputsThumbnailEncryptionTypeDef",
    "ClientCreateJobOutputsWatermarksEncryptionTypeDef",
    "ClientCreateJobOutputsWatermarksTypeDef",
    "ClientCreateJobOutputsTypeDef",
    "ClientCreateJobPlaylistsHlsContentProtectionTypeDef",
    "ClientCreateJobPlaylistsPlayReadyDrmTypeDef",
    "ClientCreateJobPlaylistsTypeDef",
    "ClientCreateJobResponseJobInputDetectedPropertiesTypeDef",
    "ClientCreateJobResponseJobInputEncryptionTypeDef",
    "ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesTypeDef",
    "ClientCreateJobResponseJobInputInputCaptionsTypeDef",
    "ClientCreateJobResponseJobInputTimeSpanTypeDef",
    "ClientCreateJobResponseJobInputTypeDef",
    "ClientCreateJobResponseJobInputsDetectedPropertiesTypeDef",
    "ClientCreateJobResponseJobInputsEncryptionTypeDef",
    "ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef",
    "ClientCreateJobResponseJobInputsInputCaptionsTypeDef",
    "ClientCreateJobResponseJobInputsTimeSpanTypeDef",
    "ClientCreateJobResponseJobInputsTypeDef",
    "ClientCreateJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputAlbumArtArtworkTypeDef",
    "ClientCreateJobResponseJobOutputAlbumArtTypeDef",
    "ClientCreateJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputCaptionsCaptionFormatsTypeDef",
    "ClientCreateJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputCaptionsCaptionSourcesTypeDef",
    "ClientCreateJobResponseJobOutputCaptionsTypeDef",
    "ClientCreateJobResponseJobOutputCompositionTimeSpanTypeDef",
    "ClientCreateJobResponseJobOutputCompositionTypeDef",
    "ClientCreateJobResponseJobOutputEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputThumbnailEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputWatermarksEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputWatermarksTypeDef",
    "ClientCreateJobResponseJobOutputTypeDef",
    "ClientCreateJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputsAlbumArtArtworkTypeDef",
    "ClientCreateJobResponseJobOutputsAlbumArtTypeDef",
    "ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsTypeDef",
    "ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesTypeDef",
    "ClientCreateJobResponseJobOutputsCaptionsTypeDef",
    "ClientCreateJobResponseJobOutputsCompositionTimeSpanTypeDef",
    "ClientCreateJobResponseJobOutputsCompositionTypeDef",
    "ClientCreateJobResponseJobOutputsEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputsThumbnailEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputsWatermarksEncryptionTypeDef",
    "ClientCreateJobResponseJobOutputsWatermarksTypeDef",
    "ClientCreateJobResponseJobOutputsTypeDef",
    "ClientCreateJobResponseJobPlaylistsHlsContentProtectionTypeDef",
    "ClientCreateJobResponseJobPlaylistsPlayReadyDrmTypeDef",
    "ClientCreateJobResponseJobPlaylistsTypeDef",
    "ClientCreateJobResponseJobTimingTypeDef",
    "ClientCreateJobResponseJobTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientCreatePipelineContentConfigPermissionsTypeDef",
    "ClientCreatePipelineContentConfigTypeDef",
    "ClientCreatePipelineNotificationsTypeDef",
    "ClientCreatePipelineResponsePipelineContentConfigPermissionsTypeDef",
    "ClientCreatePipelineResponsePipelineContentConfigTypeDef",
    "ClientCreatePipelineResponsePipelineNotificationsTypeDef",
    "ClientCreatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef",
    "ClientCreatePipelineResponsePipelineThumbnailConfigTypeDef",
    "ClientCreatePipelineResponsePipelineTypeDef",
    "ClientCreatePipelineResponseWarningsTypeDef",
    "ClientCreatePipelineResponseTypeDef",
    "ClientCreatePipelineThumbnailConfigPermissionsTypeDef",
    "ClientCreatePipelineThumbnailConfigTypeDef",
    "ClientCreatePresetAudioCodecOptionsTypeDef",
    "ClientCreatePresetAudioTypeDef",
    "ClientCreatePresetResponsePresetAudioCodecOptionsTypeDef",
    "ClientCreatePresetResponsePresetAudioTypeDef",
    "ClientCreatePresetResponsePresetThumbnailsTypeDef",
    "ClientCreatePresetResponsePresetVideoWatermarksTypeDef",
    "ClientCreatePresetResponsePresetVideoTypeDef",
    "ClientCreatePresetResponsePresetTypeDef",
    "ClientCreatePresetResponseTypeDef",
    "ClientCreatePresetThumbnailsTypeDef",
    "ClientCreatePresetVideoWatermarksTypeDef",
    "ClientCreatePresetVideoTypeDef",
    "ClientListJobsByPipelineResponseJobsInputDetectedPropertiesTypeDef",
    "ClientListJobsByPipelineResponseJobsInputEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    "ClientListJobsByPipelineResponseJobsInputInputCaptionsTypeDef",
    "ClientListJobsByPipelineResponseJobsInputTimeSpanTypeDef",
    "ClientListJobsByPipelineResponseJobsInputTypeDef",
    "ClientListJobsByPipelineResponseJobsInputsDetectedPropertiesTypeDef",
    "ClientListJobsByPipelineResponseJobsInputsEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    "ClientListJobsByPipelineResponseJobsInputsInputCaptionsTypeDef",
    "ClientListJobsByPipelineResponseJobsInputsTimeSpanTypeDef",
    "ClientListJobsByPipelineResponseJobsInputsTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputAlbumArtTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputCaptionsTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputCompositionTimeSpanTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputCompositionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputThumbnailEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputWatermarksEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputWatermarksTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsAlbumArtTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsCaptionsTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsCompositionTimeSpanTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsCompositionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsThumbnailEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsWatermarksEncryptionTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsWatermarksTypeDef",
    "ClientListJobsByPipelineResponseJobsOutputsTypeDef",
    "ClientListJobsByPipelineResponseJobsPlaylistsHlsContentProtectionTypeDef",
    "ClientListJobsByPipelineResponseJobsPlaylistsPlayReadyDrmTypeDef",
    "ClientListJobsByPipelineResponseJobsPlaylistsTypeDef",
    "ClientListJobsByPipelineResponseJobsTimingTypeDef",
    "ClientListJobsByPipelineResponseJobsTypeDef",
    "ClientListJobsByPipelineResponseTypeDef",
    "ClientListJobsByStatusResponseJobsInputDetectedPropertiesTypeDef",
    "ClientListJobsByStatusResponseJobsInputEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    "ClientListJobsByStatusResponseJobsInputInputCaptionsTypeDef",
    "ClientListJobsByStatusResponseJobsInputTimeSpanTypeDef",
    "ClientListJobsByStatusResponseJobsInputTypeDef",
    "ClientListJobsByStatusResponseJobsInputsDetectedPropertiesTypeDef",
    "ClientListJobsByStatusResponseJobsInputsEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    "ClientListJobsByStatusResponseJobsInputsInputCaptionsTypeDef",
    "ClientListJobsByStatusResponseJobsInputsTimeSpanTypeDef",
    "ClientListJobsByStatusResponseJobsInputsTypeDef",
    "ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkTypeDef",
    "ClientListJobsByStatusResponseJobsOutputAlbumArtTypeDef",
    "ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    "ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    "ClientListJobsByStatusResponseJobsOutputCaptionsTypeDef",
    "ClientListJobsByStatusResponseJobsOutputCompositionTimeSpanTypeDef",
    "ClientListJobsByStatusResponseJobsOutputCompositionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputThumbnailEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputWatermarksEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputWatermarksTypeDef",
    "ClientListJobsByStatusResponseJobsOutputTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsAlbumArtTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsCaptionsTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsCompositionTimeSpanTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsCompositionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsThumbnailEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsWatermarksEncryptionTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsWatermarksTypeDef",
    "ClientListJobsByStatusResponseJobsOutputsTypeDef",
    "ClientListJobsByStatusResponseJobsPlaylistsHlsContentProtectionTypeDef",
    "ClientListJobsByStatusResponseJobsPlaylistsPlayReadyDrmTypeDef",
    "ClientListJobsByStatusResponseJobsPlaylistsTypeDef",
    "ClientListJobsByStatusResponseJobsTimingTypeDef",
    "ClientListJobsByStatusResponseJobsTypeDef",
    "ClientListJobsByStatusResponseTypeDef",
    "ClientListPipelinesResponsePipelinesContentConfigPermissionsTypeDef",
    "ClientListPipelinesResponsePipelinesContentConfigTypeDef",
    "ClientListPipelinesResponsePipelinesNotificationsTypeDef",
    "ClientListPipelinesResponsePipelinesThumbnailConfigPermissionsTypeDef",
    "ClientListPipelinesResponsePipelinesThumbnailConfigTypeDef",
    "ClientListPipelinesResponsePipelinesTypeDef",
    "ClientListPipelinesResponseTypeDef",
    "ClientListPresetsResponsePresetsAudioCodecOptionsTypeDef",
    "ClientListPresetsResponsePresetsAudioTypeDef",
    "ClientListPresetsResponsePresetsThumbnailsTypeDef",
    "ClientListPresetsResponsePresetsVideoWatermarksTypeDef",
    "ClientListPresetsResponsePresetsVideoTypeDef",
    "ClientListPresetsResponsePresetsTypeDef",
    "ClientListPresetsResponseTypeDef",
    "ClientReadJobResponseJobInputDetectedPropertiesTypeDef",
    "ClientReadJobResponseJobInputEncryptionTypeDef",
    "ClientReadJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientReadJobResponseJobInputInputCaptionsCaptionSourcesTypeDef",
    "ClientReadJobResponseJobInputInputCaptionsTypeDef",
    "ClientReadJobResponseJobInputTimeSpanTypeDef",
    "ClientReadJobResponseJobInputTypeDef",
    "ClientReadJobResponseJobInputsDetectedPropertiesTypeDef",
    "ClientReadJobResponseJobInputsEncryptionTypeDef",
    "ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef",
    "ClientReadJobResponseJobInputsInputCaptionsTypeDef",
    "ClientReadJobResponseJobInputsTimeSpanTypeDef",
    "ClientReadJobResponseJobInputsTypeDef",
    "ClientReadJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef",
    "ClientReadJobResponseJobOutputAlbumArtArtworkTypeDef",
    "ClientReadJobResponseJobOutputAlbumArtTypeDef",
    "ClientReadJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef",
    "ClientReadJobResponseJobOutputCaptionsCaptionFormatsTypeDef",
    "ClientReadJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientReadJobResponseJobOutputCaptionsCaptionSourcesTypeDef",
    "ClientReadJobResponseJobOutputCaptionsTypeDef",
    "ClientReadJobResponseJobOutputCompositionTimeSpanTypeDef",
    "ClientReadJobResponseJobOutputCompositionTypeDef",
    "ClientReadJobResponseJobOutputEncryptionTypeDef",
    "ClientReadJobResponseJobOutputThumbnailEncryptionTypeDef",
    "ClientReadJobResponseJobOutputWatermarksEncryptionTypeDef",
    "ClientReadJobResponseJobOutputWatermarksTypeDef",
    "ClientReadJobResponseJobOutputTypeDef",
    "ClientReadJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef",
    "ClientReadJobResponseJobOutputsAlbumArtArtworkTypeDef",
    "ClientReadJobResponseJobOutputsAlbumArtTypeDef",
    "ClientReadJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    "ClientReadJobResponseJobOutputsCaptionsCaptionFormatsTypeDef",
    "ClientReadJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    "ClientReadJobResponseJobOutputsCaptionsCaptionSourcesTypeDef",
    "ClientReadJobResponseJobOutputsCaptionsTypeDef",
    "ClientReadJobResponseJobOutputsCompositionTimeSpanTypeDef",
    "ClientReadJobResponseJobOutputsCompositionTypeDef",
    "ClientReadJobResponseJobOutputsEncryptionTypeDef",
    "ClientReadJobResponseJobOutputsThumbnailEncryptionTypeDef",
    "ClientReadJobResponseJobOutputsWatermarksEncryptionTypeDef",
    "ClientReadJobResponseJobOutputsWatermarksTypeDef",
    "ClientReadJobResponseJobOutputsTypeDef",
    "ClientReadJobResponseJobPlaylistsHlsContentProtectionTypeDef",
    "ClientReadJobResponseJobPlaylistsPlayReadyDrmTypeDef",
    "ClientReadJobResponseJobPlaylistsTypeDef",
    "ClientReadJobResponseJobTimingTypeDef",
    "ClientReadJobResponseJobTypeDef",
    "ClientReadJobResponseTypeDef",
    "ClientReadPipelineResponsePipelineContentConfigPermissionsTypeDef",
    "ClientReadPipelineResponsePipelineContentConfigTypeDef",
    "ClientReadPipelineResponsePipelineNotificationsTypeDef",
    "ClientReadPipelineResponsePipelineThumbnailConfigPermissionsTypeDef",
    "ClientReadPipelineResponsePipelineThumbnailConfigTypeDef",
    "ClientReadPipelineResponsePipelineTypeDef",
    "ClientReadPipelineResponseWarningsTypeDef",
    "ClientReadPipelineResponseTypeDef",
    "ClientReadPresetResponsePresetAudioCodecOptionsTypeDef",
    "ClientReadPresetResponsePresetAudioTypeDef",
    "ClientReadPresetResponsePresetThumbnailsTypeDef",
    "ClientReadPresetResponsePresetVideoWatermarksTypeDef",
    "ClientReadPresetResponsePresetVideoTypeDef",
    "ClientReadPresetResponsePresetTypeDef",
    "ClientReadPresetResponseTypeDef",
    "ClientTestRoleResponseTypeDef",
    "ClientUpdatePipelineContentConfigPermissionsTypeDef",
    "ClientUpdatePipelineContentConfigTypeDef",
    "ClientUpdatePipelineNotificationsNotificationsTypeDef",
    "ClientUpdatePipelineNotificationsResponsePipelineContentConfigPermissionsTypeDef",
    "ClientUpdatePipelineNotificationsResponsePipelineContentConfigTypeDef",
    "ClientUpdatePipelineNotificationsResponsePipelineNotificationsTypeDef",
    "ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigPermissionsTypeDef",
    "ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigTypeDef",
    "ClientUpdatePipelineNotificationsResponsePipelineTypeDef",
    "ClientUpdatePipelineNotificationsResponseTypeDef",
    "ClientUpdatePipelineNotificationsTypeDef",
    "ClientUpdatePipelineResponsePipelineContentConfigPermissionsTypeDef",
    "ClientUpdatePipelineResponsePipelineContentConfigTypeDef",
    "ClientUpdatePipelineResponsePipelineNotificationsTypeDef",
    "ClientUpdatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef",
    "ClientUpdatePipelineResponsePipelineThumbnailConfigTypeDef",
    "ClientUpdatePipelineResponsePipelineTypeDef",
    "ClientUpdatePipelineResponseWarningsTypeDef",
    "ClientUpdatePipelineResponseTypeDef",
    "ClientUpdatePipelineStatusResponsePipelineContentConfigPermissionsTypeDef",
    "ClientUpdatePipelineStatusResponsePipelineContentConfigTypeDef",
    "ClientUpdatePipelineStatusResponsePipelineNotificationsTypeDef",
    "ClientUpdatePipelineStatusResponsePipelineThumbnailConfigPermissionsTypeDef",
    "ClientUpdatePipelineStatusResponsePipelineThumbnailConfigTypeDef",
    "ClientUpdatePipelineStatusResponsePipelineTypeDef",
    "ClientUpdatePipelineStatusResponseTypeDef",
    "ClientUpdatePipelineThumbnailConfigPermissionsTypeDef",
    "ClientUpdatePipelineThumbnailConfigTypeDef",
    "JobCompleteWaitWaiterConfigTypeDef",
    "ListJobsByPipelinePaginatePaginationConfigTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputDetectedPropertiesTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputInputCaptionsTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputTimeSpanTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputsDetectedPropertiesTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputsEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputsTimeSpanTypeDef",
    "ListJobsByPipelinePaginateResponseJobsInputsTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputAlbumArtTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputCaptionsTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputCompositionTimeSpanTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputCompositionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputThumbnailEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputWatermarksEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputWatermarksTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsCaptionsTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsCompositionTimeSpanTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsCompositionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsThumbnailEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsWatermarksEncryptionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsWatermarksTypeDef",
    "ListJobsByPipelinePaginateResponseJobsOutputsTypeDef",
    "ListJobsByPipelinePaginateResponseJobsPlaylistsHlsContentProtectionTypeDef",
    "ListJobsByPipelinePaginateResponseJobsPlaylistsPlayReadyDrmTypeDef",
    "ListJobsByPipelinePaginateResponseJobsPlaylistsTypeDef",
    "ListJobsByPipelinePaginateResponseJobsTimingTypeDef",
    "ListJobsByPipelinePaginateResponseJobsTypeDef",
    "ListJobsByPipelinePaginateResponseTypeDef",
    "ListJobsByStatusPaginatePaginationConfigTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputDetectedPropertiesTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputInputCaptionsTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputTimeSpanTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputsDetectedPropertiesTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputsEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputsInputCaptionsTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputsTimeSpanTypeDef",
    "ListJobsByStatusPaginateResponseJobsInputsTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputAlbumArtTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputCaptionsTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputCompositionTimeSpanTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputCompositionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputThumbnailEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputWatermarksEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputWatermarksTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsAlbumArtTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsCaptionsTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsCompositionTimeSpanTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsCompositionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsThumbnailEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsWatermarksEncryptionTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsWatermarksTypeDef",
    "ListJobsByStatusPaginateResponseJobsOutputsTypeDef",
    "ListJobsByStatusPaginateResponseJobsPlaylistsHlsContentProtectionTypeDef",
    "ListJobsByStatusPaginateResponseJobsPlaylistsPlayReadyDrmTypeDef",
    "ListJobsByStatusPaginateResponseJobsPlaylistsTypeDef",
    "ListJobsByStatusPaginateResponseJobsTimingTypeDef",
    "ListJobsByStatusPaginateResponseJobsTypeDef",
    "ListJobsByStatusPaginateResponseTypeDef",
    "ListPipelinesPaginatePaginationConfigTypeDef",
    "ListPipelinesPaginateResponsePipelinesContentConfigPermissionsTypeDef",
    "ListPipelinesPaginateResponsePipelinesContentConfigTypeDef",
    "ListPipelinesPaginateResponsePipelinesNotificationsTypeDef",
    "ListPipelinesPaginateResponsePipelinesThumbnailConfigPermissionsTypeDef",
    "ListPipelinesPaginateResponsePipelinesThumbnailConfigTypeDef",
    "ListPipelinesPaginateResponsePipelinesTypeDef",
    "ListPipelinesPaginateResponseTypeDef",
    "ListPresetsPaginatePaginationConfigTypeDef",
    "ListPresetsPaginateResponsePresetsAudioCodecOptionsTypeDef",
    "ListPresetsPaginateResponsePresetsAudioTypeDef",
    "ListPresetsPaginateResponsePresetsThumbnailsTypeDef",
    "ListPresetsPaginateResponsePresetsVideoWatermarksTypeDef",
    "ListPresetsPaginateResponsePresetsVideoTypeDef",
    "ListPresetsPaginateResponsePresetsTypeDef",
    "ListPresetsPaginateResponseTypeDef",
)


_ClientCreateJobInputDetectedPropertiesTypeDef = TypedDict(
    "_ClientCreateJobInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ClientCreateJobInputDetectedPropertiesTypeDef(_ClientCreateJobInputDetectedPropertiesTypeDef):
    pass


_ClientCreateJobInputEncryptionTypeDef = TypedDict(
    "_ClientCreateJobInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobInputEncryptionTypeDef(_ClientCreateJobInputEncryptionTypeDef):
    pass


_ClientCreateJobInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientCreateJobInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobInputInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientCreateJobInputInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientCreateJobInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientCreateJobInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobInputInputCaptionsCaptionSourcesTypeDef(
    _ClientCreateJobInputInputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientCreateJobInputInputCaptionsTypeDef = TypedDict(
    "_ClientCreateJobInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobInputInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)


class ClientCreateJobInputInputCaptionsTypeDef(_ClientCreateJobInputInputCaptionsTypeDef):
    pass


_ClientCreateJobInputTimeSpanTypeDef = TypedDict(
    "_ClientCreateJobInputTimeSpanTypeDef", {"StartTime": str, "Duration": str}, total=False
)


class ClientCreateJobInputTimeSpanTypeDef(_ClientCreateJobInputTimeSpanTypeDef):
    pass


_ClientCreateJobInputTypeDef = TypedDict(
    "_ClientCreateJobInputTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ClientCreateJobInputEncryptionTypeDef,
        "TimeSpan": ClientCreateJobInputTimeSpanTypeDef,
        "InputCaptions": ClientCreateJobInputInputCaptionsTypeDef,
        "DetectedProperties": ClientCreateJobInputDetectedPropertiesTypeDef,
    },
    total=False,
)


class ClientCreateJobInputTypeDef(_ClientCreateJobInputTypeDef):
    """
    A section of the request body that provides information about the file that is being transcoded.
    - **Key** *(string) --*

      The name of the file to transcode. Elsewhere in the body of the JSON block is the the ID of
      the pipeline to use for processing the job. The ``InputBucket`` object in that pipeline tells
      Elastic Transcoder which Amazon S3 bucket to get the file from.
      If the file name includes a prefix, such as ``cooking/lasagna.mpg`` , include the prefix in
      the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error.
    """


_ClientCreateJobInputsDetectedPropertiesTypeDef = TypedDict(
    "_ClientCreateJobInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ClientCreateJobInputsDetectedPropertiesTypeDef(
    _ClientCreateJobInputsDetectedPropertiesTypeDef
):
    pass


_ClientCreateJobInputsEncryptionTypeDef = TypedDict(
    "_ClientCreateJobInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobInputsEncryptionTypeDef(_ClientCreateJobInputsEncryptionTypeDef):
    pass


_ClientCreateJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientCreateJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientCreateJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientCreateJobInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientCreateJobInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobInputsInputCaptionsCaptionSourcesTypeDef(
    _ClientCreateJobInputsInputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientCreateJobInputsInputCaptionsTypeDef = TypedDict(
    "_ClientCreateJobInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobInputsInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)


class ClientCreateJobInputsInputCaptionsTypeDef(_ClientCreateJobInputsInputCaptionsTypeDef):
    pass


_ClientCreateJobInputsTimeSpanTypeDef = TypedDict(
    "_ClientCreateJobInputsTimeSpanTypeDef", {"StartTime": str, "Duration": str}, total=False
)


class ClientCreateJobInputsTimeSpanTypeDef(_ClientCreateJobInputsTimeSpanTypeDef):
    pass


_ClientCreateJobInputsTypeDef = TypedDict(
    "_ClientCreateJobInputsTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ClientCreateJobInputsEncryptionTypeDef,
        "TimeSpan": ClientCreateJobInputsTimeSpanTypeDef,
        "InputCaptions": ClientCreateJobInputsInputCaptionsTypeDef,
        "DetectedProperties": ClientCreateJobInputsDetectedPropertiesTypeDef,
    },
    total=False,
)


class ClientCreateJobInputsTypeDef(_ClientCreateJobInputsTypeDef):
    """
    - *(dict) --*

      Information about the file that you're transcoding.
      - **Key** *(string) --*

        The name of the file to transcode. Elsewhere in the body of the JSON block is the the ID of
        the pipeline to use for processing the job. The ``InputBucket`` object in that pipeline
        tells Elastic Transcoder which Amazon S3 bucket to get the file from.
        If the file name includes a prefix, such as ``cooking/lasagna.mpg`` , include the prefix in
        the key. If the file isn't in the specified bucket, Elastic Transcoder returns an error.
    """


_ClientCreateJobOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputAlbumArtArtworkEncryptionTypeDef(
    _ClientCreateJobOutputAlbumArtArtworkEncryptionTypeDef
):
    pass


_ClientCreateJobOutputAlbumArtArtworkTypeDef = TypedDict(
    "_ClientCreateJobOutputAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ClientCreateJobOutputAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobOutputAlbumArtArtworkTypeDef(_ClientCreateJobOutputAlbumArtArtworkTypeDef):
    pass


_ClientCreateJobOutputAlbumArtTypeDef = TypedDict(
    "_ClientCreateJobOutputAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientCreateJobOutputAlbumArtArtworkTypeDef]},
    total=False,
)


class ClientCreateJobOutputAlbumArtTypeDef(_ClientCreateJobOutputAlbumArtTypeDef):
    pass


_ClientCreateJobOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputCaptionsCaptionFormatsEncryptionTypeDef(
    _ClientCreateJobOutputCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ClientCreateJobOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ClientCreateJobOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientCreateJobOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobOutputCaptionsCaptionFormatsTypeDef(
    _ClientCreateJobOutputCaptionsCaptionFormatsTypeDef
):
    pass


_ClientCreateJobOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientCreateJobOutputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientCreateJobOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientCreateJobOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobOutputCaptionsCaptionSourcesTypeDef(
    _ClientCreateJobOutputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientCreateJobOutputCaptionsTypeDef = TypedDict(
    "_ClientCreateJobOutputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobOutputCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientCreateJobOutputCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)


class ClientCreateJobOutputCaptionsTypeDef(_ClientCreateJobOutputCaptionsTypeDef):
    pass


_ClientCreateJobOutputCompositionTimeSpanTypeDef = TypedDict(
    "_ClientCreateJobOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientCreateJobOutputCompositionTimeSpanTypeDef(
    _ClientCreateJobOutputCompositionTimeSpanTypeDef
):
    pass


_ClientCreateJobOutputCompositionTypeDef = TypedDict(
    "_ClientCreateJobOutputCompositionTypeDef",
    {"TimeSpan": ClientCreateJobOutputCompositionTimeSpanTypeDef},
    total=False,
)


class ClientCreateJobOutputCompositionTypeDef(_ClientCreateJobOutputCompositionTypeDef):
    pass


_ClientCreateJobOutputEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputEncryptionTypeDef(_ClientCreateJobOutputEncryptionTypeDef):
    pass


_ClientCreateJobOutputThumbnailEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputThumbnailEncryptionTypeDef(
    _ClientCreateJobOutputThumbnailEncryptionTypeDef
):
    pass


_ClientCreateJobOutputWatermarksEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputWatermarksEncryptionTypeDef(
    _ClientCreateJobOutputWatermarksEncryptionTypeDef
):
    pass


_ClientCreateJobOutputWatermarksTypeDef = TypedDict(
    "_ClientCreateJobOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientCreateJobOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobOutputWatermarksTypeDef(_ClientCreateJobOutputWatermarksTypeDef):
    pass


_ClientCreateJobOutputTypeDef = TypedDict(
    "_ClientCreateJobOutputTypeDef",
    {
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ClientCreateJobOutputThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Watermarks": List[ClientCreateJobOutputWatermarksTypeDef],
        "AlbumArt": ClientCreateJobOutputAlbumArtTypeDef,
        "Composition": List[ClientCreateJobOutputCompositionTypeDef],
        "Captions": ClientCreateJobOutputCaptionsTypeDef,
        "Encryption": ClientCreateJobOutputEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobOutputTypeDef(_ClientCreateJobOutputTypeDef):
    """
    A section of the request body that provides information about the transcoded (target) file. We
    strongly recommend that you use the ``Outputs`` syntax instead of the ``Output`` syntax.
    - **Key** *(string) --*

      The name to assign to the transcoded file. Elastic Transcoder saves the file in the Amazon S3
      bucket specified by the ``OutputBucket`` object in the pipeline that is specified by the
      pipeline ID. If a file with the specified name already exists in the output bucket, the job
      fails.
    """


_ClientCreateJobOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputsAlbumArtArtworkEncryptionTypeDef(
    _ClientCreateJobOutputsAlbumArtArtworkEncryptionTypeDef
):
    pass


_ClientCreateJobOutputsAlbumArtArtworkTypeDef = TypedDict(
    "_ClientCreateJobOutputsAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ClientCreateJobOutputsAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobOutputsAlbumArtArtworkTypeDef(_ClientCreateJobOutputsAlbumArtArtworkTypeDef):
    pass


_ClientCreateJobOutputsAlbumArtTypeDef = TypedDict(
    "_ClientCreateJobOutputsAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientCreateJobOutputsAlbumArtArtworkTypeDef]},
    total=False,
)


class ClientCreateJobOutputsAlbumArtTypeDef(_ClientCreateJobOutputsAlbumArtTypeDef):
    pass


_ClientCreateJobOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputsCaptionsCaptionFormatsEncryptionTypeDef(
    _ClientCreateJobOutputsCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ClientCreateJobOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ClientCreateJobOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientCreateJobOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobOutputsCaptionsCaptionFormatsTypeDef(
    _ClientCreateJobOutputsCaptionsCaptionFormatsTypeDef
):
    pass


_ClientCreateJobOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputsCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientCreateJobOutputsCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientCreateJobOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientCreateJobOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobOutputsCaptionsCaptionSourcesTypeDef(
    _ClientCreateJobOutputsCaptionsCaptionSourcesTypeDef
):
    pass


_ClientCreateJobOutputsCaptionsTypeDef = TypedDict(
    "_ClientCreateJobOutputsCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobOutputsCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientCreateJobOutputsCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)


class ClientCreateJobOutputsCaptionsTypeDef(_ClientCreateJobOutputsCaptionsTypeDef):
    pass


_ClientCreateJobOutputsCompositionTimeSpanTypeDef = TypedDict(
    "_ClientCreateJobOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientCreateJobOutputsCompositionTimeSpanTypeDef(
    _ClientCreateJobOutputsCompositionTimeSpanTypeDef
):
    pass


_ClientCreateJobOutputsCompositionTypeDef = TypedDict(
    "_ClientCreateJobOutputsCompositionTypeDef",
    {"TimeSpan": ClientCreateJobOutputsCompositionTimeSpanTypeDef},
    total=False,
)


class ClientCreateJobOutputsCompositionTypeDef(_ClientCreateJobOutputsCompositionTypeDef):
    pass


_ClientCreateJobOutputsEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputsEncryptionTypeDef(_ClientCreateJobOutputsEncryptionTypeDef):
    pass


_ClientCreateJobOutputsThumbnailEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputsThumbnailEncryptionTypeDef(
    _ClientCreateJobOutputsThumbnailEncryptionTypeDef
):
    pass


_ClientCreateJobOutputsWatermarksEncryptionTypeDef = TypedDict(
    "_ClientCreateJobOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobOutputsWatermarksEncryptionTypeDef(
    _ClientCreateJobOutputsWatermarksEncryptionTypeDef
):
    pass


_ClientCreateJobOutputsWatermarksTypeDef = TypedDict(
    "_ClientCreateJobOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientCreateJobOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobOutputsWatermarksTypeDef(_ClientCreateJobOutputsWatermarksTypeDef):
    pass


_ClientCreateJobOutputsTypeDef = TypedDict(
    "_ClientCreateJobOutputsTypeDef",
    {
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ClientCreateJobOutputsThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Watermarks": List[ClientCreateJobOutputsWatermarksTypeDef],
        "AlbumArt": ClientCreateJobOutputsAlbumArtTypeDef,
        "Composition": List[ClientCreateJobOutputsCompositionTypeDef],
        "Captions": ClientCreateJobOutputsCaptionsTypeDef,
        "Encryption": ClientCreateJobOutputsEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobOutputsTypeDef(_ClientCreateJobOutputsTypeDef):
    """
    - *(dict) --*

      The ``CreateJobOutput`` structure.
      - **Key** *(string) --*

        The name to assign to the transcoded file. Elastic Transcoder saves the file in the Amazon
        S3 bucket specified by the ``OutputBucket`` object in the pipeline that is specified by the
        pipeline ID. If a file with the specified name already exists in the output bucket, the job
        fails.
    """


_ClientCreateJobPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "_ClientCreateJobPlaylistsHlsContentProtectionTypeDef",
    {
        "Method": str,
        "Key": str,
        "KeyMd5": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
        "KeyStoragePolicy": str,
    },
    total=False,
)


class ClientCreateJobPlaylistsHlsContentProtectionTypeDef(
    _ClientCreateJobPlaylistsHlsContentProtectionTypeDef
):
    pass


_ClientCreateJobPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "_ClientCreateJobPlaylistsPlayReadyDrmTypeDef",
    {
        "Format": str,
        "Key": str,
        "KeyMd5": str,
        "KeyId": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
    },
    total=False,
)


class ClientCreateJobPlaylistsPlayReadyDrmTypeDef(_ClientCreateJobPlaylistsPlayReadyDrmTypeDef):
    pass


_ClientCreateJobPlaylistsTypeDef = TypedDict(
    "_ClientCreateJobPlaylistsTypeDef",
    {
        "Name": str,
        "Format": str,
        "OutputKeys": List[str],
        "HlsContentProtection": ClientCreateJobPlaylistsHlsContentProtectionTypeDef,
        "PlayReadyDrm": ClientCreateJobPlaylistsPlayReadyDrmTypeDef,
    },
    total=False,
)


class ClientCreateJobPlaylistsTypeDef(_ClientCreateJobPlaylistsTypeDef):
    """
    - *(dict) --*

      Information about the master playlist.
      - **Name** *(string) --*

        The name that you want Elastic Transcoder to assign to the master playlist, for example,
        nyc-vacation.m3u8. If the name includes a ``/`` character, the section of the name before
        the last ``/`` must be identical for all ``Name`` objects. If you create more than one
        master playlist, the values of all ``Name`` objects must be unique.
        .. note::

          Elastic Transcoder automatically appends the relevant file extension to the file name
          (``.m3u8`` for ``HLSv3`` and ``HLSv4`` playlists, and ``.ism`` and ``.ismc`` for
          ``Smooth`` playlists). If you include a file extension in ``Name`` , the file name will
          have two extensions.
    """


_ClientCreateJobResponseJobInputDetectedPropertiesTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ClientCreateJobResponseJobInputDetectedPropertiesTypeDef(
    _ClientCreateJobResponseJobInputDetectedPropertiesTypeDef
):
    pass


_ClientCreateJobResponseJobInputEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobInputEncryptionTypeDef(
    _ClientCreateJobResponseJobInputEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesTypeDef(
    _ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientCreateJobResponseJobInputInputCaptionsTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)


class ClientCreateJobResponseJobInputInputCaptionsTypeDef(
    _ClientCreateJobResponseJobInputInputCaptionsTypeDef
):
    pass


_ClientCreateJobResponseJobInputTimeSpanTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientCreateJobResponseJobInputTimeSpanTypeDef(
    _ClientCreateJobResponseJobInputTimeSpanTypeDef
):
    pass


_ClientCreateJobResponseJobInputTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ClientCreateJobResponseJobInputEncryptionTypeDef,
        "TimeSpan": ClientCreateJobResponseJobInputTimeSpanTypeDef,
        "InputCaptions": ClientCreateJobResponseJobInputInputCaptionsTypeDef,
        "DetectedProperties": ClientCreateJobResponseJobInputDetectedPropertiesTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobInputTypeDef(_ClientCreateJobResponseJobInputTypeDef):
    pass


_ClientCreateJobResponseJobInputsDetectedPropertiesTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ClientCreateJobResponseJobInputsDetectedPropertiesTypeDef(
    _ClientCreateJobResponseJobInputsDetectedPropertiesTypeDef
):
    pass


_ClientCreateJobResponseJobInputsEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobInputsEncryptionTypeDef(
    _ClientCreateJobResponseJobInputsEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef(
    _ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientCreateJobResponseJobInputsInputCaptionsTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)


class ClientCreateJobResponseJobInputsInputCaptionsTypeDef(
    _ClientCreateJobResponseJobInputsInputCaptionsTypeDef
):
    pass


_ClientCreateJobResponseJobInputsTimeSpanTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientCreateJobResponseJobInputsTimeSpanTypeDef(
    _ClientCreateJobResponseJobInputsTimeSpanTypeDef
):
    pass


_ClientCreateJobResponseJobInputsTypeDef = TypedDict(
    "_ClientCreateJobResponseJobInputsTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ClientCreateJobResponseJobInputsEncryptionTypeDef,
        "TimeSpan": ClientCreateJobResponseJobInputsTimeSpanTypeDef,
        "InputCaptions": ClientCreateJobResponseJobInputsInputCaptionsTypeDef,
        "DetectedProperties": ClientCreateJobResponseJobInputsDetectedPropertiesTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobInputsTypeDef(_ClientCreateJobResponseJobInputsTypeDef):
    pass


_ClientCreateJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputAlbumArtArtworkTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ClientCreateJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobOutputAlbumArtArtworkTypeDef(
    _ClientCreateJobResponseJobOutputAlbumArtArtworkTypeDef
):
    pass


_ClientCreateJobResponseJobOutputAlbumArtTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientCreateJobResponseJobOutputAlbumArtArtworkTypeDef]},
    total=False,
)


class ClientCreateJobResponseJobOutputAlbumArtTypeDef(
    _ClientCreateJobResponseJobOutputAlbumArtTypeDef
):
    pass


_ClientCreateJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientCreateJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobOutputCaptionsCaptionFormatsTypeDef(
    _ClientCreateJobResponseJobOutputCaptionsCaptionFormatsTypeDef
):
    pass


_ClientCreateJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobOutputCaptionsCaptionSourcesTypeDef(
    _ClientCreateJobResponseJobOutputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientCreateJobResponseJobOutputCaptionsTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobResponseJobOutputCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientCreateJobResponseJobOutputCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)


class ClientCreateJobResponseJobOutputCaptionsTypeDef(
    _ClientCreateJobResponseJobOutputCaptionsTypeDef
):
    pass


_ClientCreateJobResponseJobOutputCompositionTimeSpanTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientCreateJobResponseJobOutputCompositionTimeSpanTypeDef(
    _ClientCreateJobResponseJobOutputCompositionTimeSpanTypeDef
):
    pass


_ClientCreateJobResponseJobOutputCompositionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputCompositionTypeDef",
    {"TimeSpan": ClientCreateJobResponseJobOutputCompositionTimeSpanTypeDef},
    total=False,
)


class ClientCreateJobResponseJobOutputCompositionTypeDef(
    _ClientCreateJobResponseJobOutputCompositionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputThumbnailEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputThumbnailEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputThumbnailEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputWatermarksEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputWatermarksEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputWatermarksEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputWatermarksTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientCreateJobResponseJobOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobOutputWatermarksTypeDef(
    _ClientCreateJobResponseJobOutputWatermarksTypeDef
):
    pass


_ClientCreateJobResponseJobOutputTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ClientCreateJobResponseJobOutputThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ClientCreateJobResponseJobOutputWatermarksTypeDef],
        "AlbumArt": ClientCreateJobResponseJobOutputAlbumArtTypeDef,
        "Composition": List[ClientCreateJobResponseJobOutputCompositionTypeDef],
        "Captions": ClientCreateJobResponseJobOutputCaptionsTypeDef,
        "Encryption": ClientCreateJobResponseJobOutputEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ClientCreateJobResponseJobOutputTypeDef(_ClientCreateJobResponseJobOutputTypeDef):
    pass


_ClientCreateJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsAlbumArtArtworkTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ClientCreateJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobOutputsAlbumArtArtworkTypeDef(
    _ClientCreateJobResponseJobOutputsAlbumArtArtworkTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsAlbumArtTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientCreateJobResponseJobOutputsAlbumArtArtworkTypeDef]},
    total=False,
)


class ClientCreateJobResponseJobOutputsAlbumArtTypeDef(
    _ClientCreateJobResponseJobOutputsAlbumArtTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsTypeDef(
    _ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesTypeDef(
    _ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsCaptionsTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)


class ClientCreateJobResponseJobOutputsCaptionsTypeDef(
    _ClientCreateJobResponseJobOutputsCaptionsTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsCompositionTimeSpanTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientCreateJobResponseJobOutputsCompositionTimeSpanTypeDef(
    _ClientCreateJobResponseJobOutputsCompositionTimeSpanTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsCompositionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsCompositionTypeDef",
    {"TimeSpan": ClientCreateJobResponseJobOutputsCompositionTimeSpanTypeDef},
    total=False,
)


class ClientCreateJobResponseJobOutputsCompositionTypeDef(
    _ClientCreateJobResponseJobOutputsCompositionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputsEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputsEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsThumbnailEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputsThumbnailEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputsThumbnailEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsWatermarksEncryptionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientCreateJobResponseJobOutputsWatermarksEncryptionTypeDef(
    _ClientCreateJobResponseJobOutputsWatermarksEncryptionTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsWatermarksTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientCreateJobResponseJobOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobOutputsWatermarksTypeDef(
    _ClientCreateJobResponseJobOutputsWatermarksTypeDef
):
    pass


_ClientCreateJobResponseJobOutputsTypeDef = TypedDict(
    "_ClientCreateJobResponseJobOutputsTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ClientCreateJobResponseJobOutputsThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ClientCreateJobResponseJobOutputsWatermarksTypeDef],
        "AlbumArt": ClientCreateJobResponseJobOutputsAlbumArtTypeDef,
        "Composition": List[ClientCreateJobResponseJobOutputsCompositionTypeDef],
        "Captions": ClientCreateJobResponseJobOutputsCaptionsTypeDef,
        "Encryption": ClientCreateJobResponseJobOutputsEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ClientCreateJobResponseJobOutputsTypeDef(_ClientCreateJobResponseJobOutputsTypeDef):
    pass


_ClientCreateJobResponseJobPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "_ClientCreateJobResponseJobPlaylistsHlsContentProtectionTypeDef",
    {
        "Method": str,
        "Key": str,
        "KeyMd5": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
        "KeyStoragePolicy": str,
    },
    total=False,
)


class ClientCreateJobResponseJobPlaylistsHlsContentProtectionTypeDef(
    _ClientCreateJobResponseJobPlaylistsHlsContentProtectionTypeDef
):
    pass


_ClientCreateJobResponseJobPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "_ClientCreateJobResponseJobPlaylistsPlayReadyDrmTypeDef",
    {
        "Format": str,
        "Key": str,
        "KeyMd5": str,
        "KeyId": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
    },
    total=False,
)


class ClientCreateJobResponseJobPlaylistsPlayReadyDrmTypeDef(
    _ClientCreateJobResponseJobPlaylistsPlayReadyDrmTypeDef
):
    pass


_ClientCreateJobResponseJobPlaylistsTypeDef = TypedDict(
    "_ClientCreateJobResponseJobPlaylistsTypeDef",
    {
        "Name": str,
        "Format": str,
        "OutputKeys": List[str],
        "HlsContentProtection": ClientCreateJobResponseJobPlaylistsHlsContentProtectionTypeDef,
        "PlayReadyDrm": ClientCreateJobResponseJobPlaylistsPlayReadyDrmTypeDef,
        "Status": str,
        "StatusDetail": str,
    },
    total=False,
)


class ClientCreateJobResponseJobPlaylistsTypeDef(_ClientCreateJobResponseJobPlaylistsTypeDef):
    pass


_ClientCreateJobResponseJobTimingTypeDef = TypedDict(
    "_ClientCreateJobResponseJobTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)


class ClientCreateJobResponseJobTimingTypeDef(_ClientCreateJobResponseJobTimingTypeDef):
    pass


_ClientCreateJobResponseJobTypeDef = TypedDict(
    "_ClientCreateJobResponseJobTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PipelineId": str,
        "Input": ClientCreateJobResponseJobInputTypeDef,
        "Inputs": List[ClientCreateJobResponseJobInputsTypeDef],
        "Output": ClientCreateJobResponseJobOutputTypeDef,
        "Outputs": List[ClientCreateJobResponseJobOutputsTypeDef],
        "OutputKeyPrefix": str,
        "Playlists": List[ClientCreateJobResponseJobPlaylistsTypeDef],
        "Status": str,
        "UserMetadata": Dict[str, str],
        "Timing": ClientCreateJobResponseJobTimingTypeDef,
    },
    total=False,
)


class ClientCreateJobResponseJobTypeDef(_ClientCreateJobResponseJobTypeDef):
    """
    - **Job** *(dict) --*

      A section of the response body that provides information about the job that is created.
      - **Id** *(string) --*

        The identifier that Elastic Transcoder assigned to the job. You use this value to get
        settings for the job or to delete the job.
    """


_ClientCreateJobResponseTypeDef = TypedDict(
    "_ClientCreateJobResponseTypeDef", {"Job": ClientCreateJobResponseJobTypeDef}, total=False
)


class ClientCreateJobResponseTypeDef(_ClientCreateJobResponseTypeDef):
    """
    - *(dict) --*

      The CreateJobResponse structure.
      - **Job** *(dict) --*

        A section of the response body that provides information about the job that is created.
        - **Id** *(string) --*

          The identifier that Elastic Transcoder assigned to the job. You use this value to get
          settings for the job or to delete the job.
    """


_ClientCreatePipelineContentConfigPermissionsTypeDef = TypedDict(
    "_ClientCreatePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientCreatePipelineContentConfigPermissionsTypeDef(
    _ClientCreatePipelineContentConfigPermissionsTypeDef
):
    pass


_ClientCreatePipelineContentConfigTypeDef = TypedDict(
    "_ClientCreatePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientCreatePipelineContentConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientCreatePipelineContentConfigTypeDef(_ClientCreatePipelineContentConfigTypeDef):
    """
    The optional ``ContentConfig`` object specifies information about the Amazon S3 bucket in which
    you want Elastic Transcoder to save transcoded files and playlists: which bucket to use, which
    users you want to have access to the files, the type of access you want users to have, and the
    storage class that you want to assign to the files.
    If you specify values for ``ContentConfig`` , you must also specify values for
    ``ThumbnailConfig`` .
    If you specify values for ``ContentConfig`` and ``ThumbnailConfig`` , omit the ``OutputBucket``
    object.
    * **Bucket** : The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded
    files and playlists.
    * **Permissions** (Optional): The Permissions object specifies which users you want to have
    access to transcoded files and the type of access you want them to have. You can grant
    permissions to a maximum of 30 users and/or predefined Amazon S3 groups.
    * **Grantee Type** : Specify the type of value that appears in the ``Grantee`` object:

      * **Canonical** : The value in the ``Grantee`` object is either the canonical user ID for an
      AWS account or an origin access identity for an Amazon CloudFront distribution. For more
      information about canonical user IDs, see Access Control List (ACL) Overview in the Amazon
      Simple Storage Service Developer Guide. For more information about using CloudFront origin
      access identities to require that users use CloudFront URLs instead of Amazon S3 URLs, see
      Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content.
      .. warning::

        A canonical user ID is not the same as an AWS account number.
    """


_ClientCreatePipelineNotificationsTypeDef = TypedDict(
    "_ClientCreatePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class ClientCreatePipelineNotificationsTypeDef(_ClientCreatePipelineNotificationsTypeDef):
    """
    The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job
    status.
    .. warning::

      To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.
    """


_ClientCreatePipelineResponsePipelineContentConfigPermissionsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientCreatePipelineResponsePipelineContentConfigPermissionsTypeDef(
    _ClientCreatePipelineResponsePipelineContentConfigPermissionsTypeDef
):
    pass


_ClientCreatePipelineResponsePipelineContentConfigTypeDef = TypedDict(
    "_ClientCreatePipelineResponsePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientCreatePipelineResponsePipelineContentConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientCreatePipelineResponsePipelineContentConfigTypeDef(
    _ClientCreatePipelineResponsePipelineContentConfigTypeDef
):
    pass


_ClientCreatePipelineResponsePipelineNotificationsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class ClientCreatePipelineResponsePipelineNotificationsTypeDef(
    _ClientCreatePipelineResponsePipelineNotificationsTypeDef
):
    pass


_ClientCreatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "_ClientCreatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientCreatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef(
    _ClientCreatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef
):
    pass


_ClientCreatePipelineResponsePipelineThumbnailConfigTypeDef = TypedDict(
    "_ClientCreatePipelineResponsePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientCreatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientCreatePipelineResponsePipelineThumbnailConfigTypeDef(
    _ClientCreatePipelineResponsePipelineThumbnailConfigTypeDef
):
    pass


_ClientCreatePipelineResponsePipelineTypeDef = TypedDict(
    "_ClientCreatePipelineResponsePipelineTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Status": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Role": str,
        "AwsKmsKeyArn": str,
        "Notifications": ClientCreatePipelineResponsePipelineNotificationsTypeDef,
        "ContentConfig": ClientCreatePipelineResponsePipelineContentConfigTypeDef,
        "ThumbnailConfig": ClientCreatePipelineResponsePipelineThumbnailConfigTypeDef,
    },
    total=False,
)


class ClientCreatePipelineResponsePipelineTypeDef(_ClientCreatePipelineResponsePipelineTypeDef):
    """
    - **Pipeline** *(dict) --*

      A section of the response body that provides information about the pipeline that is created.
      - **Id** *(string) --*

        The identifier for the pipeline. You use this value to identify the pipeline in which you
        want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientCreatePipelineResponseWarningsTypeDef = TypedDict(
    "_ClientCreatePipelineResponseWarningsTypeDef", {"Code": str, "Message": str}, total=False
)


class ClientCreatePipelineResponseWarningsTypeDef(_ClientCreatePipelineResponseWarningsTypeDef):
    pass


_ClientCreatePipelineResponseTypeDef = TypedDict(
    "_ClientCreatePipelineResponseTypeDef",
    {
        "Pipeline": ClientCreatePipelineResponsePipelineTypeDef,
        "Warnings": List[ClientCreatePipelineResponseWarningsTypeDef],
    },
    total=False,
)


class ClientCreatePipelineResponseTypeDef(_ClientCreatePipelineResponseTypeDef):
    """
    - *(dict) --*

      When you create a pipeline, Elastic Transcoder returns the values that you specified in the
      request.
      - **Pipeline** *(dict) --*

        A section of the response body that provides information about the pipeline that is created.
        - **Id** *(string) --*

          The identifier for the pipeline. You use this value to identify the pipeline in which you
          want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientCreatePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "_ClientCreatePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientCreatePipelineThumbnailConfigPermissionsTypeDef(
    _ClientCreatePipelineThumbnailConfigPermissionsTypeDef
):
    pass


_ClientCreatePipelineThumbnailConfigTypeDef = TypedDict(
    "_ClientCreatePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientCreatePipelineThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientCreatePipelineThumbnailConfigTypeDef(_ClientCreatePipelineThumbnailConfigTypeDef):
    """
    The ``ThumbnailConfig`` object specifies several values, including the Amazon S3 bucket in which
    you want Elastic Transcoder to save thumbnail files, which users you want to have access to the
    files, the type of access you want users to have, and the storage class that you want to assign
    to the files.
    If you specify values for ``ContentConfig`` , you must also specify values for
    ``ThumbnailConfig`` even if you don't want to create thumbnails.
    If you specify values for ``ContentConfig`` and ``ThumbnailConfig`` , omit the ``OutputBucket``
    object.
    * **Bucket** : The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail
    files.
    * **Permissions** (Optional): The ``Permissions`` object specifies which users and/or predefined
    Amazon S3 groups you want to have access to thumbnail files, and the type of access you want
    them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3
    groups.
    * **GranteeType** : Specify the type of value that appears in the Grantee object:

      * **Canonical** : The value in the ``Grantee`` object is either the canonical user ID for an
      AWS account or an origin access identity for an Amazon CloudFront distribution.
      .. warning::

        A canonical user ID is not the same as an AWS account number.
    """


_ClientCreatePresetAudioCodecOptionsTypeDef = TypedDict(
    "_ClientCreatePresetAudioCodecOptionsTypeDef",
    {"Profile": str, "BitDepth": str, "BitOrder": str, "Signed": str},
    total=False,
)


class ClientCreatePresetAudioCodecOptionsTypeDef(_ClientCreatePresetAudioCodecOptionsTypeDef):
    pass


_ClientCreatePresetAudioTypeDef = TypedDict(
    "_ClientCreatePresetAudioTypeDef",
    {
        "Codec": str,
        "SampleRate": str,
        "BitRate": str,
        "Channels": str,
        "AudioPackingMode": str,
        "CodecOptions": ClientCreatePresetAudioCodecOptionsTypeDef,
    },
    total=False,
)


class ClientCreatePresetAudioTypeDef(_ClientCreatePresetAudioTypeDef):
    """
    A section of the request body that specifies the audio parameters.
    - **Codec** *(string) --*

      The audio codec for the output file. Valid values include ``aac`` , ``flac`` , ``mp2`` ,
      ``mp3`` , ``pcm`` , and ``vorbis`` .
    """


_ClientCreatePresetResponsePresetAudioCodecOptionsTypeDef = TypedDict(
    "_ClientCreatePresetResponsePresetAudioCodecOptionsTypeDef",
    {"Profile": str, "BitDepth": str, "BitOrder": str, "Signed": str},
    total=False,
)


class ClientCreatePresetResponsePresetAudioCodecOptionsTypeDef(
    _ClientCreatePresetResponsePresetAudioCodecOptionsTypeDef
):
    pass


_ClientCreatePresetResponsePresetAudioTypeDef = TypedDict(
    "_ClientCreatePresetResponsePresetAudioTypeDef",
    {
        "Codec": str,
        "SampleRate": str,
        "BitRate": str,
        "Channels": str,
        "AudioPackingMode": str,
        "CodecOptions": ClientCreatePresetResponsePresetAudioCodecOptionsTypeDef,
    },
    total=False,
)


class ClientCreatePresetResponsePresetAudioTypeDef(_ClientCreatePresetResponsePresetAudioTypeDef):
    pass


_ClientCreatePresetResponsePresetThumbnailsTypeDef = TypedDict(
    "_ClientCreatePresetResponsePresetThumbnailsTypeDef",
    {
        "Format": str,
        "Interval": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
    },
    total=False,
)


class ClientCreatePresetResponsePresetThumbnailsTypeDef(
    _ClientCreatePresetResponsePresetThumbnailsTypeDef
):
    pass


_ClientCreatePresetResponsePresetVideoWatermarksTypeDef = TypedDict(
    "_ClientCreatePresetResponsePresetVideoWatermarksTypeDef",
    {
        "Id": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "HorizontalAlign": str,
        "HorizontalOffset": str,
        "VerticalAlign": str,
        "VerticalOffset": str,
        "Opacity": str,
        "Target": str,
    },
    total=False,
)


class ClientCreatePresetResponsePresetVideoWatermarksTypeDef(
    _ClientCreatePresetResponsePresetVideoWatermarksTypeDef
):
    pass


_ClientCreatePresetResponsePresetVideoTypeDef = TypedDict(
    "_ClientCreatePresetResponsePresetVideoTypeDef",
    {
        "Codec": str,
        "CodecOptions": Dict[str, str],
        "KeyframesMaxDist": str,
        "FixedGOP": str,
        "BitRate": str,
        "FrameRate": str,
        "MaxFrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "DisplayAspectRatio": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "Watermarks": List[ClientCreatePresetResponsePresetVideoWatermarksTypeDef],
    },
    total=False,
)


class ClientCreatePresetResponsePresetVideoTypeDef(_ClientCreatePresetResponsePresetVideoTypeDef):
    pass


_ClientCreatePresetResponsePresetTypeDef = TypedDict(
    "_ClientCreatePresetResponsePresetTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Container": str,
        "Audio": ClientCreatePresetResponsePresetAudioTypeDef,
        "Video": ClientCreatePresetResponsePresetVideoTypeDef,
        "Thumbnails": ClientCreatePresetResponsePresetThumbnailsTypeDef,
        "Type": str,
    },
    total=False,
)


class ClientCreatePresetResponsePresetTypeDef(_ClientCreatePresetResponsePresetTypeDef):
    """
    - **Preset** *(dict) --*

      A section of the response body that provides information about the preset that is created.
      - **Id** *(string) --*

        Identifier for the new preset. You use this value to get settings for the preset or to
        delete it.
    """


_ClientCreatePresetResponseTypeDef = TypedDict(
    "_ClientCreatePresetResponseTypeDef",
    {"Preset": ClientCreatePresetResponsePresetTypeDef, "Warning": str},
    total=False,
)


class ClientCreatePresetResponseTypeDef(_ClientCreatePresetResponseTypeDef):
    """
    - *(dict) --*

      The ``CreatePresetResponse`` structure.
      - **Preset** *(dict) --*

        A section of the response body that provides information about the preset that is created.
        - **Id** *(string) --*

          Identifier for the new preset. You use this value to get settings for the preset or to
          delete it.
    """


_ClientCreatePresetThumbnailsTypeDef = TypedDict(
    "_ClientCreatePresetThumbnailsTypeDef",
    {
        "Format": str,
        "Interval": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
    },
    total=False,
)


class ClientCreatePresetThumbnailsTypeDef(_ClientCreatePresetThumbnailsTypeDef):
    """
    A section of the request body that specifies the thumbnail parameters, if any.
    - **Format** *(string) --*

      The format of thumbnails, if any. Valid values are ``jpg`` and ``png`` .
      You specify whether you want Elastic Transcoder to create thumbnails when you create a job.
    """


_ClientCreatePresetVideoWatermarksTypeDef = TypedDict(
    "_ClientCreatePresetVideoWatermarksTypeDef",
    {
        "Id": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "HorizontalAlign": str,
        "HorizontalOffset": str,
        "VerticalAlign": str,
        "VerticalOffset": str,
        "Opacity": str,
        "Target": str,
    },
    total=False,
)


class ClientCreatePresetVideoWatermarksTypeDef(_ClientCreatePresetVideoWatermarksTypeDef):
    pass


_ClientCreatePresetVideoTypeDef = TypedDict(
    "_ClientCreatePresetVideoTypeDef",
    {
        "Codec": str,
        "CodecOptions": Dict[str, str],
        "KeyframesMaxDist": str,
        "FixedGOP": str,
        "BitRate": str,
        "FrameRate": str,
        "MaxFrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "DisplayAspectRatio": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "Watermarks": List[ClientCreatePresetVideoWatermarksTypeDef],
    },
    total=False,
)


class ClientCreatePresetVideoTypeDef(_ClientCreatePresetVideoTypeDef):
    """
    A section of the request body that specifies the video parameters.
    - **Codec** *(string) --*

      The video codec for the output file. Valid values include ``gif`` , ``H.264`` , ``mpeg2`` ,
      ``vp8`` , and ``vp9`` . You can only specify ``vp8`` and ``vp9`` when the container type is
      ``webm`` , ``gif`` when the container type is ``gif`` , and ``mpeg2`` when the container type
      is ``mpg`` .
    """


_ClientListJobsByPipelineResponseJobsInputDetectedPropertiesTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputDetectedPropertiesTypeDef(
    _ClientListJobsByPipelineResponseJobsInputDetectedPropertiesTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsInputEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesTypeDef(
    _ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputInputCaptionsTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputInputCaptionsTypeDef(
    _ClientListJobsByPipelineResponseJobsInputInputCaptionsTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputTimeSpanTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputTimeSpanTypeDef(
    _ClientListJobsByPipelineResponseJobsInputTimeSpanTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ClientListJobsByPipelineResponseJobsInputEncryptionTypeDef,
        "TimeSpan": ClientListJobsByPipelineResponseJobsInputTimeSpanTypeDef,
        "InputCaptions": ClientListJobsByPipelineResponseJobsInputInputCaptionsTypeDef,
        "DetectedProperties": ClientListJobsByPipelineResponseJobsInputDetectedPropertiesTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputTypeDef(
    _ClientListJobsByPipelineResponseJobsInputTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputsDetectedPropertiesTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputsDetectedPropertiesTypeDef(
    _ClientListJobsByPipelineResponseJobsInputsDetectedPropertiesTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputsEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputsEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsInputsEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesTypeDef(
    _ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputsInputCaptionsTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputsInputCaptionsTypeDef(
    _ClientListJobsByPipelineResponseJobsInputsInputCaptionsTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputsTimeSpanTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputsTimeSpanTypeDef(
    _ClientListJobsByPipelineResponseJobsInputsTimeSpanTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsInputsTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsInputsTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ClientListJobsByPipelineResponseJobsInputsEncryptionTypeDef,
        "TimeSpan": ClientListJobsByPipelineResponseJobsInputsTimeSpanTypeDef,
        "InputCaptions": ClientListJobsByPipelineResponseJobsInputsInputCaptionsTypeDef,
        "DetectedProperties": ClientListJobsByPipelineResponseJobsInputsDetectedPropertiesTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsInputsTypeDef(
    _ClientListJobsByPipelineResponseJobsInputsTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputAlbumArtTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkTypeDef],
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputAlbumArtTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputAlbumArtTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputCaptionsTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesTypeDef
        ],
        "CaptionFormats": List[
            ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsTypeDef
        ],
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputCaptionsTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputCaptionsTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputCompositionTimeSpanTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputCompositionTimeSpanTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputCompositionTimeSpanTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputCompositionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputCompositionTypeDef",
    {"TimeSpan": ClientListJobsByPipelineResponseJobsOutputCompositionTimeSpanTypeDef},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputCompositionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputCompositionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputThumbnailEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputThumbnailEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputThumbnailEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputWatermarksEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputWatermarksEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputWatermarksEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputWatermarksTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputWatermarksTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputWatermarksTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ClientListJobsByPipelineResponseJobsOutputThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ClientListJobsByPipelineResponseJobsOutputWatermarksTypeDef],
        "AlbumArt": ClientListJobsByPipelineResponseJobsOutputAlbumArtTypeDef,
        "Composition": List[ClientListJobsByPipelineResponseJobsOutputCompositionTypeDef],
        "Captions": ClientListJobsByPipelineResponseJobsOutputCaptionsTypeDef,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsAlbumArtTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkTypeDef],
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsAlbumArtTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsAlbumArtTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsCaptionsTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesTypeDef
        ],
        "CaptionFormats": List[
            ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsTypeDef
        ],
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsCaptionsTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsCaptionsTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsCompositionTimeSpanTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsCompositionTimeSpanTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsCompositionTimeSpanTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsCompositionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsCompositionTypeDef",
    {"TimeSpan": ClientListJobsByPipelineResponseJobsOutputsCompositionTimeSpanTypeDef},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsCompositionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsCompositionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsThumbnailEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsThumbnailEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsThumbnailEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsWatermarksEncryptionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsWatermarksEncryptionTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsWatermarksEncryptionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsWatermarksTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsWatermarksTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsWatermarksTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsOutputsTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsOutputsTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ClientListJobsByPipelineResponseJobsOutputsThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ClientListJobsByPipelineResponseJobsOutputsWatermarksTypeDef],
        "AlbumArt": ClientListJobsByPipelineResponseJobsOutputsAlbumArtTypeDef,
        "Composition": List[ClientListJobsByPipelineResponseJobsOutputsCompositionTypeDef],
        "Captions": ClientListJobsByPipelineResponseJobsOutputsCaptionsTypeDef,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputsEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsOutputsTypeDef(
    _ClientListJobsByPipelineResponseJobsOutputsTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsPlaylistsHlsContentProtectionTypeDef",
    {
        "Method": str,
        "Key": str,
        "KeyMd5": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
        "KeyStoragePolicy": str,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsPlaylistsHlsContentProtectionTypeDef(
    _ClientListJobsByPipelineResponseJobsPlaylistsHlsContentProtectionTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsPlaylistsPlayReadyDrmTypeDef",
    {
        "Format": str,
        "Key": str,
        "KeyMd5": str,
        "KeyId": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsPlaylistsPlayReadyDrmTypeDef(
    _ClientListJobsByPipelineResponseJobsPlaylistsPlayReadyDrmTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsPlaylistsTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsPlaylistsTypeDef",
    {
        "Name": str,
        "Format": str,
        "OutputKeys": List[str],
        "HlsContentProtection": ClientListJobsByPipelineResponseJobsPlaylistsHlsContentProtectionTypeDef,
        "PlayReadyDrm": ClientListJobsByPipelineResponseJobsPlaylistsPlayReadyDrmTypeDef,
        "Status": str,
        "StatusDetail": str,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsPlaylistsTypeDef(
    _ClientListJobsByPipelineResponseJobsPlaylistsTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsTimingTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)


class ClientListJobsByPipelineResponseJobsTimingTypeDef(
    _ClientListJobsByPipelineResponseJobsTimingTypeDef
):
    pass


_ClientListJobsByPipelineResponseJobsTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseJobsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PipelineId": str,
        "Input": ClientListJobsByPipelineResponseJobsInputTypeDef,
        "Inputs": List[ClientListJobsByPipelineResponseJobsInputsTypeDef],
        "Output": ClientListJobsByPipelineResponseJobsOutputTypeDef,
        "Outputs": List[ClientListJobsByPipelineResponseJobsOutputsTypeDef],
        "OutputKeyPrefix": str,
        "Playlists": List[ClientListJobsByPipelineResponseJobsPlaylistsTypeDef],
        "Status": str,
        "UserMetadata": Dict[str, str],
        "Timing": ClientListJobsByPipelineResponseJobsTimingTypeDef,
    },
    total=False,
)


class ClientListJobsByPipelineResponseJobsTypeDef(_ClientListJobsByPipelineResponseJobsTypeDef):
    """
    - *(dict) --*

      A section of the response body that provides information about the job that is created.
      - **Id** *(string) --*

        The identifier that Elastic Transcoder assigned to the job. You use this value to get
        settings for the job or to delete the job.
    """


_ClientListJobsByPipelineResponseTypeDef = TypedDict(
    "_ClientListJobsByPipelineResponseTypeDef",
    {"Jobs": List[ClientListJobsByPipelineResponseJobsTypeDef], "NextPageToken": str},
    total=False,
)


class ClientListJobsByPipelineResponseTypeDef(_ClientListJobsByPipelineResponseTypeDef):
    """
    - *(dict) --*

      The ``ListJobsByPipelineResponse`` structure.
      - **Jobs** *(list) --*

        An array of ``Job`` objects that are in the specified pipeline.
        - *(dict) --*

          A section of the response body that provides information about the job that is created.
          - **Id** *(string) --*

            The identifier that Elastic Transcoder assigned to the job. You use this value to get
            settings for the job or to delete the job.
    """


_ClientListJobsByStatusResponseJobsInputDetectedPropertiesTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ClientListJobsByStatusResponseJobsInputDetectedPropertiesTypeDef(
    _ClientListJobsByStatusResponseJobsInputDetectedPropertiesTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsInputEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsInputEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesTypeDef(
    _ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputInputCaptionsTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsInputInputCaptionsTypeDef(
    _ClientListJobsByStatusResponseJobsInputInputCaptionsTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputTimeSpanTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsInputTimeSpanTypeDef(
    _ClientListJobsByStatusResponseJobsInputTimeSpanTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ClientListJobsByStatusResponseJobsInputEncryptionTypeDef,
        "TimeSpan": ClientListJobsByStatusResponseJobsInputTimeSpanTypeDef,
        "InputCaptions": ClientListJobsByStatusResponseJobsInputInputCaptionsTypeDef,
        "DetectedProperties": ClientListJobsByStatusResponseJobsInputDetectedPropertiesTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsInputTypeDef(
    _ClientListJobsByStatusResponseJobsInputTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputsDetectedPropertiesTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ClientListJobsByStatusResponseJobsInputsDetectedPropertiesTypeDef(
    _ClientListJobsByStatusResponseJobsInputsDetectedPropertiesTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputsEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsInputsEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsInputsEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesTypeDef(
    _ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputsInputCaptionsTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsInputsInputCaptionsTypeDef(
    _ClientListJobsByStatusResponseJobsInputsInputCaptionsTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputsTimeSpanTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsInputsTimeSpanTypeDef(
    _ClientListJobsByStatusResponseJobsInputsTimeSpanTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsInputsTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsInputsTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ClientListJobsByStatusResponseJobsInputsEncryptionTypeDef,
        "TimeSpan": ClientListJobsByStatusResponseJobsInputsTimeSpanTypeDef,
        "InputCaptions": ClientListJobsByStatusResponseJobsInputsInputCaptionsTypeDef,
        "DetectedProperties": ClientListJobsByStatusResponseJobsInputsDetectedPropertiesTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsInputsTypeDef(
    _ClientListJobsByStatusResponseJobsInputsTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkTypeDef(
    _ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputAlbumArtTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkTypeDef],
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputAlbumArtTypeDef(
    _ClientListJobsByStatusResponseJobsOutputAlbumArtTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsTypeDef(
    _ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesTypeDef(
    _ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputCaptionsTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesTypeDef
        ],
        "CaptionFormats": List[
            ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsTypeDef
        ],
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputCaptionsTypeDef(
    _ClientListJobsByStatusResponseJobsOutputCaptionsTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputCompositionTimeSpanTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputCompositionTimeSpanTypeDef(
    _ClientListJobsByStatusResponseJobsOutputCompositionTimeSpanTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputCompositionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputCompositionTypeDef",
    {"TimeSpan": ClientListJobsByStatusResponseJobsOutputCompositionTimeSpanTypeDef},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputCompositionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputCompositionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputThumbnailEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputThumbnailEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputThumbnailEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputWatermarksEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputWatermarksEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputWatermarksEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputWatermarksTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputWatermarksTypeDef(
    _ClientListJobsByStatusResponseJobsOutputWatermarksTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ClientListJobsByStatusResponseJobsOutputThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ClientListJobsByStatusResponseJobsOutputWatermarksTypeDef],
        "AlbumArt": ClientListJobsByStatusResponseJobsOutputAlbumArtTypeDef,
        "Composition": List[ClientListJobsByStatusResponseJobsOutputCompositionTypeDef],
        "Captions": ClientListJobsByStatusResponseJobsOutputCaptionsTypeDef,
        "Encryption": ClientListJobsByStatusResponseJobsOutputEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputTypeDef(
    _ClientListJobsByStatusResponseJobsOutputTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsAlbumArtTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkTypeDef],
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsAlbumArtTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsAlbumArtTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsCaptionsTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesTypeDef
        ],
        "CaptionFormats": List[
            ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsTypeDef
        ],
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsCaptionsTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsCaptionsTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsCompositionTimeSpanTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsCompositionTimeSpanTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsCompositionTimeSpanTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsCompositionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsCompositionTypeDef",
    {"TimeSpan": ClientListJobsByStatusResponseJobsOutputsCompositionTimeSpanTypeDef},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsCompositionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsCompositionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsThumbnailEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsThumbnailEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsThumbnailEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsWatermarksEncryptionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsWatermarksEncryptionTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsWatermarksEncryptionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsWatermarksTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsWatermarksTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsWatermarksTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsOutputsTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsOutputsTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ClientListJobsByStatusResponseJobsOutputsThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ClientListJobsByStatusResponseJobsOutputsWatermarksTypeDef],
        "AlbumArt": ClientListJobsByStatusResponseJobsOutputsAlbumArtTypeDef,
        "Composition": List[ClientListJobsByStatusResponseJobsOutputsCompositionTypeDef],
        "Captions": ClientListJobsByStatusResponseJobsOutputsCaptionsTypeDef,
        "Encryption": ClientListJobsByStatusResponseJobsOutputsEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsOutputsTypeDef(
    _ClientListJobsByStatusResponseJobsOutputsTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsPlaylistsHlsContentProtectionTypeDef",
    {
        "Method": str,
        "Key": str,
        "KeyMd5": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
        "KeyStoragePolicy": str,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsPlaylistsHlsContentProtectionTypeDef(
    _ClientListJobsByStatusResponseJobsPlaylistsHlsContentProtectionTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsPlaylistsPlayReadyDrmTypeDef",
    {
        "Format": str,
        "Key": str,
        "KeyMd5": str,
        "KeyId": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsPlaylistsPlayReadyDrmTypeDef(
    _ClientListJobsByStatusResponseJobsPlaylistsPlayReadyDrmTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsPlaylistsTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsPlaylistsTypeDef",
    {
        "Name": str,
        "Format": str,
        "OutputKeys": List[str],
        "HlsContentProtection": ClientListJobsByStatusResponseJobsPlaylistsHlsContentProtectionTypeDef,
        "PlayReadyDrm": ClientListJobsByStatusResponseJobsPlaylistsPlayReadyDrmTypeDef,
        "Status": str,
        "StatusDetail": str,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsPlaylistsTypeDef(
    _ClientListJobsByStatusResponseJobsPlaylistsTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsTimingTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)


class ClientListJobsByStatusResponseJobsTimingTypeDef(
    _ClientListJobsByStatusResponseJobsTimingTypeDef
):
    pass


_ClientListJobsByStatusResponseJobsTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseJobsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PipelineId": str,
        "Input": ClientListJobsByStatusResponseJobsInputTypeDef,
        "Inputs": List[ClientListJobsByStatusResponseJobsInputsTypeDef],
        "Output": ClientListJobsByStatusResponseJobsOutputTypeDef,
        "Outputs": List[ClientListJobsByStatusResponseJobsOutputsTypeDef],
        "OutputKeyPrefix": str,
        "Playlists": List[ClientListJobsByStatusResponseJobsPlaylistsTypeDef],
        "Status": str,
        "UserMetadata": Dict[str, str],
        "Timing": ClientListJobsByStatusResponseJobsTimingTypeDef,
    },
    total=False,
)


class ClientListJobsByStatusResponseJobsTypeDef(_ClientListJobsByStatusResponseJobsTypeDef):
    """
    - *(dict) --*

      A section of the response body that provides information about the job that is created.
      - **Id** *(string) --*

        The identifier that Elastic Transcoder assigned to the job. You use this value to get
        settings for the job or to delete the job.
    """


_ClientListJobsByStatusResponseTypeDef = TypedDict(
    "_ClientListJobsByStatusResponseTypeDef",
    {"Jobs": List[ClientListJobsByStatusResponseJobsTypeDef], "NextPageToken": str},
    total=False,
)


class ClientListJobsByStatusResponseTypeDef(_ClientListJobsByStatusResponseTypeDef):
    """
    - *(dict) --*

      The ``ListJobsByStatusResponse`` structure.
      - **Jobs** *(list) --*

        An array of ``Job`` objects that have the specified status.
        - *(dict) --*

          A section of the response body that provides information about the job that is created.
          - **Id** *(string) --*

            The identifier that Elastic Transcoder assigned to the job. You use this value to get
            settings for the job or to delete the job.
    """


_ClientListPipelinesResponsePipelinesContentConfigPermissionsTypeDef = TypedDict(
    "_ClientListPipelinesResponsePipelinesContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientListPipelinesResponsePipelinesContentConfigPermissionsTypeDef(
    _ClientListPipelinesResponsePipelinesContentConfigPermissionsTypeDef
):
    pass


_ClientListPipelinesResponsePipelinesContentConfigTypeDef = TypedDict(
    "_ClientListPipelinesResponsePipelinesContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientListPipelinesResponsePipelinesContentConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientListPipelinesResponsePipelinesContentConfigTypeDef(
    _ClientListPipelinesResponsePipelinesContentConfigTypeDef
):
    pass


_ClientListPipelinesResponsePipelinesNotificationsTypeDef = TypedDict(
    "_ClientListPipelinesResponsePipelinesNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class ClientListPipelinesResponsePipelinesNotificationsTypeDef(
    _ClientListPipelinesResponsePipelinesNotificationsTypeDef
):
    pass


_ClientListPipelinesResponsePipelinesThumbnailConfigPermissionsTypeDef = TypedDict(
    "_ClientListPipelinesResponsePipelinesThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientListPipelinesResponsePipelinesThumbnailConfigPermissionsTypeDef(
    _ClientListPipelinesResponsePipelinesThumbnailConfigPermissionsTypeDef
):
    pass


_ClientListPipelinesResponsePipelinesThumbnailConfigTypeDef = TypedDict(
    "_ClientListPipelinesResponsePipelinesThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientListPipelinesResponsePipelinesThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientListPipelinesResponsePipelinesThumbnailConfigTypeDef(
    _ClientListPipelinesResponsePipelinesThumbnailConfigTypeDef
):
    pass


_ClientListPipelinesResponsePipelinesTypeDef = TypedDict(
    "_ClientListPipelinesResponsePipelinesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Status": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Role": str,
        "AwsKmsKeyArn": str,
        "Notifications": ClientListPipelinesResponsePipelinesNotificationsTypeDef,
        "ContentConfig": ClientListPipelinesResponsePipelinesContentConfigTypeDef,
        "ThumbnailConfig": ClientListPipelinesResponsePipelinesThumbnailConfigTypeDef,
    },
    total=False,
)


class ClientListPipelinesResponsePipelinesTypeDef(_ClientListPipelinesResponsePipelinesTypeDef):
    """
    - *(dict) --*

      The pipeline (queue) that is used to manage jobs.
      - **Id** *(string) --*

        The identifier for the pipeline. You use this value to identify the pipeline in which you
        want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientListPipelinesResponseTypeDef = TypedDict(
    "_ClientListPipelinesResponseTypeDef",
    {"Pipelines": List[ClientListPipelinesResponsePipelinesTypeDef], "NextPageToken": str},
    total=False,
)


class ClientListPipelinesResponseTypeDef(_ClientListPipelinesResponseTypeDef):
    """
    - *(dict) --*

      A list of the pipelines associated with the current AWS account.
      - **Pipelines** *(list) --*

        An array of ``Pipeline`` objects.
        - *(dict) --*

          The pipeline (queue) that is used to manage jobs.
          - **Id** *(string) --*

            The identifier for the pipeline. You use this value to identify the pipeline in which
            you want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientListPresetsResponsePresetsAudioCodecOptionsTypeDef = TypedDict(
    "_ClientListPresetsResponsePresetsAudioCodecOptionsTypeDef",
    {"Profile": str, "BitDepth": str, "BitOrder": str, "Signed": str},
    total=False,
)


class ClientListPresetsResponsePresetsAudioCodecOptionsTypeDef(
    _ClientListPresetsResponsePresetsAudioCodecOptionsTypeDef
):
    pass


_ClientListPresetsResponsePresetsAudioTypeDef = TypedDict(
    "_ClientListPresetsResponsePresetsAudioTypeDef",
    {
        "Codec": str,
        "SampleRate": str,
        "BitRate": str,
        "Channels": str,
        "AudioPackingMode": str,
        "CodecOptions": ClientListPresetsResponsePresetsAudioCodecOptionsTypeDef,
    },
    total=False,
)


class ClientListPresetsResponsePresetsAudioTypeDef(_ClientListPresetsResponsePresetsAudioTypeDef):
    pass


_ClientListPresetsResponsePresetsThumbnailsTypeDef = TypedDict(
    "_ClientListPresetsResponsePresetsThumbnailsTypeDef",
    {
        "Format": str,
        "Interval": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
    },
    total=False,
)


class ClientListPresetsResponsePresetsThumbnailsTypeDef(
    _ClientListPresetsResponsePresetsThumbnailsTypeDef
):
    pass


_ClientListPresetsResponsePresetsVideoWatermarksTypeDef = TypedDict(
    "_ClientListPresetsResponsePresetsVideoWatermarksTypeDef",
    {
        "Id": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "HorizontalAlign": str,
        "HorizontalOffset": str,
        "VerticalAlign": str,
        "VerticalOffset": str,
        "Opacity": str,
        "Target": str,
    },
    total=False,
)


class ClientListPresetsResponsePresetsVideoWatermarksTypeDef(
    _ClientListPresetsResponsePresetsVideoWatermarksTypeDef
):
    pass


_ClientListPresetsResponsePresetsVideoTypeDef = TypedDict(
    "_ClientListPresetsResponsePresetsVideoTypeDef",
    {
        "Codec": str,
        "CodecOptions": Dict[str, str],
        "KeyframesMaxDist": str,
        "FixedGOP": str,
        "BitRate": str,
        "FrameRate": str,
        "MaxFrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "DisplayAspectRatio": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "Watermarks": List[ClientListPresetsResponsePresetsVideoWatermarksTypeDef],
    },
    total=False,
)


class ClientListPresetsResponsePresetsVideoTypeDef(_ClientListPresetsResponsePresetsVideoTypeDef):
    pass


_ClientListPresetsResponsePresetsTypeDef = TypedDict(
    "_ClientListPresetsResponsePresetsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Container": str,
        "Audio": ClientListPresetsResponsePresetsAudioTypeDef,
        "Video": ClientListPresetsResponsePresetsVideoTypeDef,
        "Thumbnails": ClientListPresetsResponsePresetsThumbnailsTypeDef,
        "Type": str,
    },
    total=False,
)


class ClientListPresetsResponsePresetsTypeDef(_ClientListPresetsResponsePresetsTypeDef):
    """
    - *(dict) --*

      Presets are templates that contain most of the settings for transcoding media files from one
      format to another. Elastic Transcoder includes some default presets for common formats, for
      example, several iPod and iPhone versions. You can also create your own presets for formats
      that aren't included among the default presets. You specify which preset you want to use when
      you create a job.
      - **Id** *(string) --*

        Identifier for the new preset. You use this value to get settings for the preset or to
        delete it.
    """


_ClientListPresetsResponseTypeDef = TypedDict(
    "_ClientListPresetsResponseTypeDef",
    {"Presets": List[ClientListPresetsResponsePresetsTypeDef], "NextPageToken": str},
    total=False,
)


class ClientListPresetsResponseTypeDef(_ClientListPresetsResponseTypeDef):
    """
    - *(dict) --*

      The ``ListPresetsResponse`` structure.
      - **Presets** *(list) --*

        An array of ``Preset`` objects.
        - *(dict) --*

          Presets are templates that contain most of the settings for transcoding media files from
          one format to another. Elastic Transcoder includes some default presets for common
          formats, for example, several iPod and iPhone versions. You can also create your own
          presets for formats that aren't included among the default presets. You specify which
          preset you want to use when you create a job.
          - **Id** *(string) --*

            Identifier for the new preset. You use this value to get settings for the preset or to
            delete it.
    """


_ClientReadJobResponseJobInputDetectedPropertiesTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ClientReadJobResponseJobInputDetectedPropertiesTypeDef(
    _ClientReadJobResponseJobInputDetectedPropertiesTypeDef
):
    pass


_ClientReadJobResponseJobInputEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobInputEncryptionTypeDef(
    _ClientReadJobResponseJobInputEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientReadJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientReadJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobInputInputCaptionsCaptionSourcesTypeDef(
    _ClientReadJobResponseJobInputInputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientReadJobResponseJobInputInputCaptionsTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientReadJobResponseJobInputInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)


class ClientReadJobResponseJobInputInputCaptionsTypeDef(
    _ClientReadJobResponseJobInputInputCaptionsTypeDef
):
    pass


_ClientReadJobResponseJobInputTimeSpanTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientReadJobResponseJobInputTimeSpanTypeDef(_ClientReadJobResponseJobInputTimeSpanTypeDef):
    pass


_ClientReadJobResponseJobInputTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ClientReadJobResponseJobInputEncryptionTypeDef,
        "TimeSpan": ClientReadJobResponseJobInputTimeSpanTypeDef,
        "InputCaptions": ClientReadJobResponseJobInputInputCaptionsTypeDef,
        "DetectedProperties": ClientReadJobResponseJobInputDetectedPropertiesTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobInputTypeDef(_ClientReadJobResponseJobInputTypeDef):
    pass


_ClientReadJobResponseJobInputsDetectedPropertiesTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ClientReadJobResponseJobInputsDetectedPropertiesTypeDef(
    _ClientReadJobResponseJobInputsDetectedPropertiesTypeDef
):
    pass


_ClientReadJobResponseJobInputsEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobInputsEncryptionTypeDef(
    _ClientReadJobResponseJobInputsEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef(
    _ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientReadJobResponseJobInputsInputCaptionsTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)


class ClientReadJobResponseJobInputsInputCaptionsTypeDef(
    _ClientReadJobResponseJobInputsInputCaptionsTypeDef
):
    pass


_ClientReadJobResponseJobInputsTimeSpanTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientReadJobResponseJobInputsTimeSpanTypeDef(_ClientReadJobResponseJobInputsTimeSpanTypeDef):
    pass


_ClientReadJobResponseJobInputsTypeDef = TypedDict(
    "_ClientReadJobResponseJobInputsTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ClientReadJobResponseJobInputsEncryptionTypeDef,
        "TimeSpan": ClientReadJobResponseJobInputsTimeSpanTypeDef,
        "InputCaptions": ClientReadJobResponseJobInputsInputCaptionsTypeDef,
        "DetectedProperties": ClientReadJobResponseJobInputsDetectedPropertiesTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobInputsTypeDef(_ClientReadJobResponseJobInputsTypeDef):
    pass


_ClientReadJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef(
    _ClientReadJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputAlbumArtArtworkTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ClientReadJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobOutputAlbumArtArtworkTypeDef(
    _ClientReadJobResponseJobOutputAlbumArtArtworkTypeDef
):
    pass


_ClientReadJobResponseJobOutputAlbumArtTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientReadJobResponseJobOutputAlbumArtArtworkTypeDef]},
    total=False,
)


class ClientReadJobResponseJobOutputAlbumArtTypeDef(_ClientReadJobResponseJobOutputAlbumArtTypeDef):
    pass


_ClientReadJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef(
    _ClientReadJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientReadJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobOutputCaptionsCaptionFormatsTypeDef(
    _ClientReadJobResponseJobOutputCaptionsCaptionFormatsTypeDef
):
    pass


_ClientReadJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientReadJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientReadJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobOutputCaptionsCaptionSourcesTypeDef(
    _ClientReadJobResponseJobOutputCaptionsCaptionSourcesTypeDef
):
    pass


_ClientReadJobResponseJobOutputCaptionsTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientReadJobResponseJobOutputCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientReadJobResponseJobOutputCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)


class ClientReadJobResponseJobOutputCaptionsTypeDef(_ClientReadJobResponseJobOutputCaptionsTypeDef):
    pass


_ClientReadJobResponseJobOutputCompositionTimeSpanTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientReadJobResponseJobOutputCompositionTimeSpanTypeDef(
    _ClientReadJobResponseJobOutputCompositionTimeSpanTypeDef
):
    pass


_ClientReadJobResponseJobOutputCompositionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputCompositionTypeDef",
    {"TimeSpan": ClientReadJobResponseJobOutputCompositionTimeSpanTypeDef},
    total=False,
)


class ClientReadJobResponseJobOutputCompositionTypeDef(
    _ClientReadJobResponseJobOutputCompositionTypeDef
):
    pass


_ClientReadJobResponseJobOutputEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputEncryptionTypeDef(
    _ClientReadJobResponseJobOutputEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputThumbnailEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputThumbnailEncryptionTypeDef(
    _ClientReadJobResponseJobOutputThumbnailEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputWatermarksEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputWatermarksEncryptionTypeDef(
    _ClientReadJobResponseJobOutputWatermarksEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputWatermarksTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientReadJobResponseJobOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobOutputWatermarksTypeDef(
    _ClientReadJobResponseJobOutputWatermarksTypeDef
):
    pass


_ClientReadJobResponseJobOutputTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ClientReadJobResponseJobOutputThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ClientReadJobResponseJobOutputWatermarksTypeDef],
        "AlbumArt": ClientReadJobResponseJobOutputAlbumArtTypeDef,
        "Composition": List[ClientReadJobResponseJobOutputCompositionTypeDef],
        "Captions": ClientReadJobResponseJobOutputCaptionsTypeDef,
        "Encryption": ClientReadJobResponseJobOutputEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ClientReadJobResponseJobOutputTypeDef(_ClientReadJobResponseJobOutputTypeDef):
    pass


_ClientReadJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef(
    _ClientReadJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputsAlbumArtArtworkTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ClientReadJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobOutputsAlbumArtArtworkTypeDef(
    _ClientReadJobResponseJobOutputsAlbumArtArtworkTypeDef
):
    pass


_ClientReadJobResponseJobOutputsAlbumArtTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientReadJobResponseJobOutputsAlbumArtArtworkTypeDef]},
    total=False,
)


class ClientReadJobResponseJobOutputsAlbumArtTypeDef(
    _ClientReadJobResponseJobOutputsAlbumArtTypeDef
):
    pass


_ClientReadJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef(
    _ClientReadJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientReadJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobOutputsCaptionsCaptionFormatsTypeDef(
    _ClientReadJobResponseJobOutputsCaptionsCaptionFormatsTypeDef
):
    pass


_ClientReadJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef(
    _ClientReadJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientReadJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobOutputsCaptionsCaptionSourcesTypeDef(
    _ClientReadJobResponseJobOutputsCaptionsCaptionSourcesTypeDef
):
    pass


_ClientReadJobResponseJobOutputsCaptionsTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientReadJobResponseJobOutputsCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientReadJobResponseJobOutputsCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)


class ClientReadJobResponseJobOutputsCaptionsTypeDef(
    _ClientReadJobResponseJobOutputsCaptionsTypeDef
):
    pass


_ClientReadJobResponseJobOutputsCompositionTimeSpanTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ClientReadJobResponseJobOutputsCompositionTimeSpanTypeDef(
    _ClientReadJobResponseJobOutputsCompositionTimeSpanTypeDef
):
    pass


_ClientReadJobResponseJobOutputsCompositionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsCompositionTypeDef",
    {"TimeSpan": ClientReadJobResponseJobOutputsCompositionTimeSpanTypeDef},
    total=False,
)


class ClientReadJobResponseJobOutputsCompositionTypeDef(
    _ClientReadJobResponseJobOutputsCompositionTypeDef
):
    pass


_ClientReadJobResponseJobOutputsEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputsEncryptionTypeDef(
    _ClientReadJobResponseJobOutputsEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputsThumbnailEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputsThumbnailEncryptionTypeDef(
    _ClientReadJobResponseJobOutputsThumbnailEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputsWatermarksEncryptionTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ClientReadJobResponseJobOutputsWatermarksEncryptionTypeDef(
    _ClientReadJobResponseJobOutputsWatermarksEncryptionTypeDef
):
    pass


_ClientReadJobResponseJobOutputsWatermarksTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientReadJobResponseJobOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobOutputsWatermarksTypeDef(
    _ClientReadJobResponseJobOutputsWatermarksTypeDef
):
    pass


_ClientReadJobResponseJobOutputsTypeDef = TypedDict(
    "_ClientReadJobResponseJobOutputsTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ClientReadJobResponseJobOutputsThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ClientReadJobResponseJobOutputsWatermarksTypeDef],
        "AlbumArt": ClientReadJobResponseJobOutputsAlbumArtTypeDef,
        "Composition": List[ClientReadJobResponseJobOutputsCompositionTypeDef],
        "Captions": ClientReadJobResponseJobOutputsCaptionsTypeDef,
        "Encryption": ClientReadJobResponseJobOutputsEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ClientReadJobResponseJobOutputsTypeDef(_ClientReadJobResponseJobOutputsTypeDef):
    pass


_ClientReadJobResponseJobPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "_ClientReadJobResponseJobPlaylistsHlsContentProtectionTypeDef",
    {
        "Method": str,
        "Key": str,
        "KeyMd5": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
        "KeyStoragePolicy": str,
    },
    total=False,
)


class ClientReadJobResponseJobPlaylistsHlsContentProtectionTypeDef(
    _ClientReadJobResponseJobPlaylistsHlsContentProtectionTypeDef
):
    pass


_ClientReadJobResponseJobPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "_ClientReadJobResponseJobPlaylistsPlayReadyDrmTypeDef",
    {
        "Format": str,
        "Key": str,
        "KeyMd5": str,
        "KeyId": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
    },
    total=False,
)


class ClientReadJobResponseJobPlaylistsPlayReadyDrmTypeDef(
    _ClientReadJobResponseJobPlaylistsPlayReadyDrmTypeDef
):
    pass


_ClientReadJobResponseJobPlaylistsTypeDef = TypedDict(
    "_ClientReadJobResponseJobPlaylistsTypeDef",
    {
        "Name": str,
        "Format": str,
        "OutputKeys": List[str],
        "HlsContentProtection": ClientReadJobResponseJobPlaylistsHlsContentProtectionTypeDef,
        "PlayReadyDrm": ClientReadJobResponseJobPlaylistsPlayReadyDrmTypeDef,
        "Status": str,
        "StatusDetail": str,
    },
    total=False,
)


class ClientReadJobResponseJobPlaylistsTypeDef(_ClientReadJobResponseJobPlaylistsTypeDef):
    pass


_ClientReadJobResponseJobTimingTypeDef = TypedDict(
    "_ClientReadJobResponseJobTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)


class ClientReadJobResponseJobTimingTypeDef(_ClientReadJobResponseJobTimingTypeDef):
    pass


_ClientReadJobResponseJobTypeDef = TypedDict(
    "_ClientReadJobResponseJobTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PipelineId": str,
        "Input": ClientReadJobResponseJobInputTypeDef,
        "Inputs": List[ClientReadJobResponseJobInputsTypeDef],
        "Output": ClientReadJobResponseJobOutputTypeDef,
        "Outputs": List[ClientReadJobResponseJobOutputsTypeDef],
        "OutputKeyPrefix": str,
        "Playlists": List[ClientReadJobResponseJobPlaylistsTypeDef],
        "Status": str,
        "UserMetadata": Dict[str, str],
        "Timing": ClientReadJobResponseJobTimingTypeDef,
    },
    total=False,
)


class ClientReadJobResponseJobTypeDef(_ClientReadJobResponseJobTypeDef):
    """
    - **Job** *(dict) --*

      A section of the response body that provides information about the job.
      - **Id** *(string) --*

        The identifier that Elastic Transcoder assigned to the job. You use this value to get
        settings for the job or to delete the job.
    """


_ClientReadJobResponseTypeDef = TypedDict(
    "_ClientReadJobResponseTypeDef", {"Job": ClientReadJobResponseJobTypeDef}, total=False
)


class ClientReadJobResponseTypeDef(_ClientReadJobResponseTypeDef):
    """
    - *(dict) --*

      The ``ReadJobResponse`` structure.
      - **Job** *(dict) --*

        A section of the response body that provides information about the job.
        - **Id** *(string) --*

          The identifier that Elastic Transcoder assigned to the job. You use this value to get
          settings for the job or to delete the job.
    """


_ClientReadPipelineResponsePipelineContentConfigPermissionsTypeDef = TypedDict(
    "_ClientReadPipelineResponsePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientReadPipelineResponsePipelineContentConfigPermissionsTypeDef(
    _ClientReadPipelineResponsePipelineContentConfigPermissionsTypeDef
):
    pass


_ClientReadPipelineResponsePipelineContentConfigTypeDef = TypedDict(
    "_ClientReadPipelineResponsePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientReadPipelineResponsePipelineContentConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientReadPipelineResponsePipelineContentConfigTypeDef(
    _ClientReadPipelineResponsePipelineContentConfigTypeDef
):
    pass


_ClientReadPipelineResponsePipelineNotificationsTypeDef = TypedDict(
    "_ClientReadPipelineResponsePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class ClientReadPipelineResponsePipelineNotificationsTypeDef(
    _ClientReadPipelineResponsePipelineNotificationsTypeDef
):
    pass


_ClientReadPipelineResponsePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "_ClientReadPipelineResponsePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientReadPipelineResponsePipelineThumbnailConfigPermissionsTypeDef(
    _ClientReadPipelineResponsePipelineThumbnailConfigPermissionsTypeDef
):
    pass


_ClientReadPipelineResponsePipelineThumbnailConfigTypeDef = TypedDict(
    "_ClientReadPipelineResponsePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientReadPipelineResponsePipelineThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientReadPipelineResponsePipelineThumbnailConfigTypeDef(
    _ClientReadPipelineResponsePipelineThumbnailConfigTypeDef
):
    pass


_ClientReadPipelineResponsePipelineTypeDef = TypedDict(
    "_ClientReadPipelineResponsePipelineTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Status": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Role": str,
        "AwsKmsKeyArn": str,
        "Notifications": ClientReadPipelineResponsePipelineNotificationsTypeDef,
        "ContentConfig": ClientReadPipelineResponsePipelineContentConfigTypeDef,
        "ThumbnailConfig": ClientReadPipelineResponsePipelineThumbnailConfigTypeDef,
    },
    total=False,
)


class ClientReadPipelineResponsePipelineTypeDef(_ClientReadPipelineResponsePipelineTypeDef):
    """
    - **Pipeline** *(dict) --*

      A section of the response body that provides information about the pipeline.
      - **Id** *(string) --*

        The identifier for the pipeline. You use this value to identify the pipeline in which you
        want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientReadPipelineResponseWarningsTypeDef = TypedDict(
    "_ClientReadPipelineResponseWarningsTypeDef", {"Code": str, "Message": str}, total=False
)


class ClientReadPipelineResponseWarningsTypeDef(_ClientReadPipelineResponseWarningsTypeDef):
    pass


_ClientReadPipelineResponseTypeDef = TypedDict(
    "_ClientReadPipelineResponseTypeDef",
    {
        "Pipeline": ClientReadPipelineResponsePipelineTypeDef,
        "Warnings": List[ClientReadPipelineResponseWarningsTypeDef],
    },
    total=False,
)


class ClientReadPipelineResponseTypeDef(_ClientReadPipelineResponseTypeDef):
    """
    - *(dict) --*

      The ``ReadPipelineResponse`` structure.
      - **Pipeline** *(dict) --*

        A section of the response body that provides information about the pipeline.
        - **Id** *(string) --*

          The identifier for the pipeline. You use this value to identify the pipeline in which you
          want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientReadPresetResponsePresetAudioCodecOptionsTypeDef = TypedDict(
    "_ClientReadPresetResponsePresetAudioCodecOptionsTypeDef",
    {"Profile": str, "BitDepth": str, "BitOrder": str, "Signed": str},
    total=False,
)


class ClientReadPresetResponsePresetAudioCodecOptionsTypeDef(
    _ClientReadPresetResponsePresetAudioCodecOptionsTypeDef
):
    pass


_ClientReadPresetResponsePresetAudioTypeDef = TypedDict(
    "_ClientReadPresetResponsePresetAudioTypeDef",
    {
        "Codec": str,
        "SampleRate": str,
        "BitRate": str,
        "Channels": str,
        "AudioPackingMode": str,
        "CodecOptions": ClientReadPresetResponsePresetAudioCodecOptionsTypeDef,
    },
    total=False,
)


class ClientReadPresetResponsePresetAudioTypeDef(_ClientReadPresetResponsePresetAudioTypeDef):
    pass


_ClientReadPresetResponsePresetThumbnailsTypeDef = TypedDict(
    "_ClientReadPresetResponsePresetThumbnailsTypeDef",
    {
        "Format": str,
        "Interval": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
    },
    total=False,
)


class ClientReadPresetResponsePresetThumbnailsTypeDef(
    _ClientReadPresetResponsePresetThumbnailsTypeDef
):
    pass


_ClientReadPresetResponsePresetVideoWatermarksTypeDef = TypedDict(
    "_ClientReadPresetResponsePresetVideoWatermarksTypeDef",
    {
        "Id": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "HorizontalAlign": str,
        "HorizontalOffset": str,
        "VerticalAlign": str,
        "VerticalOffset": str,
        "Opacity": str,
        "Target": str,
    },
    total=False,
)


class ClientReadPresetResponsePresetVideoWatermarksTypeDef(
    _ClientReadPresetResponsePresetVideoWatermarksTypeDef
):
    pass


_ClientReadPresetResponsePresetVideoTypeDef = TypedDict(
    "_ClientReadPresetResponsePresetVideoTypeDef",
    {
        "Codec": str,
        "CodecOptions": Dict[str, str],
        "KeyframesMaxDist": str,
        "FixedGOP": str,
        "BitRate": str,
        "FrameRate": str,
        "MaxFrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "DisplayAspectRatio": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "Watermarks": List[ClientReadPresetResponsePresetVideoWatermarksTypeDef],
    },
    total=False,
)


class ClientReadPresetResponsePresetVideoTypeDef(_ClientReadPresetResponsePresetVideoTypeDef):
    pass


_ClientReadPresetResponsePresetTypeDef = TypedDict(
    "_ClientReadPresetResponsePresetTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Container": str,
        "Audio": ClientReadPresetResponsePresetAudioTypeDef,
        "Video": ClientReadPresetResponsePresetVideoTypeDef,
        "Thumbnails": ClientReadPresetResponsePresetThumbnailsTypeDef,
        "Type": str,
    },
    total=False,
)


class ClientReadPresetResponsePresetTypeDef(_ClientReadPresetResponsePresetTypeDef):
    """
    - **Preset** *(dict) --*

      A section of the response body that provides information about the preset.
      - **Id** *(string) --*

        Identifier for the new preset. You use this value to get settings for the preset or to
        delete it.
    """


_ClientReadPresetResponseTypeDef = TypedDict(
    "_ClientReadPresetResponseTypeDef",
    {"Preset": ClientReadPresetResponsePresetTypeDef},
    total=False,
)


class ClientReadPresetResponseTypeDef(_ClientReadPresetResponseTypeDef):
    """
    - *(dict) --*

      The ``ReadPresetResponse`` structure.
      - **Preset** *(dict) --*

        A section of the response body that provides information about the preset.
        - **Id** *(string) --*

          Identifier for the new preset. You use this value to get settings for the preset or to
          delete it.
    """


_ClientTestRoleResponseTypeDef = TypedDict(
    "_ClientTestRoleResponseTypeDef", {"Success": str, "Messages": List[str]}, total=False
)


class ClientTestRoleResponseTypeDef(_ClientTestRoleResponseTypeDef):
    """
    - *(dict) --*

      The ``TestRoleResponse`` structure.
      - **Success** *(string) --*

        If the operation is successful, this value is ``true`` ; otherwise, the value is ``false`` .
    """


_ClientUpdatePipelineContentConfigPermissionsTypeDef = TypedDict(
    "_ClientUpdatePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientUpdatePipelineContentConfigPermissionsTypeDef(
    _ClientUpdatePipelineContentConfigPermissionsTypeDef
):
    pass


_ClientUpdatePipelineContentConfigTypeDef = TypedDict(
    "_ClientUpdatePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientUpdatePipelineContentConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientUpdatePipelineContentConfigTypeDef(_ClientUpdatePipelineContentConfigTypeDef):
    """
    The optional ``ContentConfig`` object specifies information about the Amazon S3 bucket in which
    you want Elastic Transcoder to save transcoded files and playlists: which bucket to use, which
    users you want to have access to the files, the type of access you want users to have, and the
    storage class that you want to assign to the files.
    If you specify values for ``ContentConfig`` , you must also specify values for
    ``ThumbnailConfig`` .
    If you specify values for ``ContentConfig`` and ``ThumbnailConfig`` , omit the ``OutputBucket``
    object.
    * **Bucket** : The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded
    files and playlists.
    * **Permissions** (Optional): The Permissions object specifies which users you want to have
    access to transcoded files and the type of access you want them to have. You can grant
    permissions to a maximum of 30 users and/or predefined Amazon S3 groups.
    * **Grantee Type** : Specify the type of value that appears in the ``Grantee`` object:

      * **Canonical** : The value in the ``Grantee`` object is either the canonical user ID for an
      AWS account or an origin access identity for an Amazon CloudFront distribution. For more
      information about canonical user IDs, see Access Control List (ACL) Overview in the Amazon
      Simple Storage Service Developer Guide. For more information about using CloudFront origin
      access identities to require that users use CloudFront URLs instead of Amazon S3 URLs, see
      Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content.
      .. warning::

        A canonical user ID is not the same as an AWS account number.
    """


_ClientUpdatePipelineNotificationsNotificationsTypeDef = TypedDict(
    "_ClientUpdatePipelineNotificationsNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class ClientUpdatePipelineNotificationsNotificationsTypeDef(
    _ClientUpdatePipelineNotificationsNotificationsTypeDef
):
    """
    The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to
    notify to report job status.
    .. warning::

      To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.
    """


_ClientUpdatePipelineNotificationsResponsePipelineContentConfigPermissionsTypeDef = TypedDict(
    "_ClientUpdatePipelineNotificationsResponsePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientUpdatePipelineNotificationsResponsePipelineContentConfigPermissionsTypeDef(
    _ClientUpdatePipelineNotificationsResponsePipelineContentConfigPermissionsTypeDef
):
    pass


_ClientUpdatePipelineNotificationsResponsePipelineContentConfigTypeDef = TypedDict(
    "_ClientUpdatePipelineNotificationsResponsePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[
            ClientUpdatePipelineNotificationsResponsePipelineContentConfigPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdatePipelineNotificationsResponsePipelineContentConfigTypeDef(
    _ClientUpdatePipelineNotificationsResponsePipelineContentConfigTypeDef
):
    pass


_ClientUpdatePipelineNotificationsResponsePipelineNotificationsTypeDef = TypedDict(
    "_ClientUpdatePipelineNotificationsResponsePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class ClientUpdatePipelineNotificationsResponsePipelineNotificationsTypeDef(
    _ClientUpdatePipelineNotificationsResponsePipelineNotificationsTypeDef
):
    pass


_ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "_ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigPermissionsTypeDef(
    _ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigPermissionsTypeDef
):
    pass


_ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigTypeDef = TypedDict(
    "_ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[
            ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigTypeDef(
    _ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigTypeDef
):
    pass


_ClientUpdatePipelineNotificationsResponsePipelineTypeDef = TypedDict(
    "_ClientUpdatePipelineNotificationsResponsePipelineTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Status": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Role": str,
        "AwsKmsKeyArn": str,
        "Notifications": ClientUpdatePipelineNotificationsResponsePipelineNotificationsTypeDef,
        "ContentConfig": ClientUpdatePipelineNotificationsResponsePipelineContentConfigTypeDef,
        "ThumbnailConfig": ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigTypeDef,
    },
    total=False,
)


class ClientUpdatePipelineNotificationsResponsePipelineTypeDef(
    _ClientUpdatePipelineNotificationsResponsePipelineTypeDef
):
    """
    - **Pipeline** *(dict) --*

      A section of the response body that provides information about the pipeline associated with
      this notification.
      - **Id** *(string) --*

        The identifier for the pipeline. You use this value to identify the pipeline in which you
        want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientUpdatePipelineNotificationsResponseTypeDef = TypedDict(
    "_ClientUpdatePipelineNotificationsResponseTypeDef",
    {"Pipeline": ClientUpdatePipelineNotificationsResponsePipelineTypeDef},
    total=False,
)


class ClientUpdatePipelineNotificationsResponseTypeDef(
    _ClientUpdatePipelineNotificationsResponseTypeDef
):
    """
    - *(dict) --*

      The ``UpdatePipelineNotificationsResponse`` structure.
      - **Pipeline** *(dict) --*

        A section of the response body that provides information about the pipeline associated with
        this notification.
        - **Id** *(string) --*

          The identifier for the pipeline. You use this value to identify the pipeline in which you
          want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientUpdatePipelineNotificationsTypeDef = TypedDict(
    "_ClientUpdatePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class ClientUpdatePipelineNotificationsTypeDef(_ClientUpdatePipelineNotificationsTypeDef):
    """
    The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to
    notify to report job status.
    .. warning::

      To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.
    """


_ClientUpdatePipelineResponsePipelineContentConfigPermissionsTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientUpdatePipelineResponsePipelineContentConfigPermissionsTypeDef(
    _ClientUpdatePipelineResponsePipelineContentConfigPermissionsTypeDef
):
    pass


_ClientUpdatePipelineResponsePipelineContentConfigTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientUpdatePipelineResponsePipelineContentConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientUpdatePipelineResponsePipelineContentConfigTypeDef(
    _ClientUpdatePipelineResponsePipelineContentConfigTypeDef
):
    pass


_ClientUpdatePipelineResponsePipelineNotificationsTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class ClientUpdatePipelineResponsePipelineNotificationsTypeDef(
    _ClientUpdatePipelineResponsePipelineNotificationsTypeDef
):
    pass


_ClientUpdatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientUpdatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef(
    _ClientUpdatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef
):
    pass


_ClientUpdatePipelineResponsePipelineThumbnailConfigTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientUpdatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientUpdatePipelineResponsePipelineThumbnailConfigTypeDef(
    _ClientUpdatePipelineResponsePipelineThumbnailConfigTypeDef
):
    pass


_ClientUpdatePipelineResponsePipelineTypeDef = TypedDict(
    "_ClientUpdatePipelineResponsePipelineTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Status": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Role": str,
        "AwsKmsKeyArn": str,
        "Notifications": ClientUpdatePipelineResponsePipelineNotificationsTypeDef,
        "ContentConfig": ClientUpdatePipelineResponsePipelineContentConfigTypeDef,
        "ThumbnailConfig": ClientUpdatePipelineResponsePipelineThumbnailConfigTypeDef,
    },
    total=False,
)


class ClientUpdatePipelineResponsePipelineTypeDef(_ClientUpdatePipelineResponsePipelineTypeDef):
    """
    - **Pipeline** *(dict) --*

      The pipeline updated by this ``UpdatePipelineResponse`` call.
      - **Id** *(string) --*

        The identifier for the pipeline. You use this value to identify the pipeline in which you
        want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientUpdatePipelineResponseWarningsTypeDef = TypedDict(
    "_ClientUpdatePipelineResponseWarningsTypeDef", {"Code": str, "Message": str}, total=False
)


class ClientUpdatePipelineResponseWarningsTypeDef(_ClientUpdatePipelineResponseWarningsTypeDef):
    pass


_ClientUpdatePipelineResponseTypeDef = TypedDict(
    "_ClientUpdatePipelineResponseTypeDef",
    {
        "Pipeline": ClientUpdatePipelineResponsePipelineTypeDef,
        "Warnings": List[ClientUpdatePipelineResponseWarningsTypeDef],
    },
    total=False,
)


class ClientUpdatePipelineResponseTypeDef(_ClientUpdatePipelineResponseTypeDef):
    """
    - *(dict) --*

      When you update a pipeline, Elastic Transcoder returns the values that you specified in the
      request.
      - **Pipeline** *(dict) --*

        The pipeline updated by this ``UpdatePipelineResponse`` call.
        - **Id** *(string) --*

          The identifier for the pipeline. You use this value to identify the pipeline in which you
          want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientUpdatePipelineStatusResponsePipelineContentConfigPermissionsTypeDef = TypedDict(
    "_ClientUpdatePipelineStatusResponsePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientUpdatePipelineStatusResponsePipelineContentConfigPermissionsTypeDef(
    _ClientUpdatePipelineStatusResponsePipelineContentConfigPermissionsTypeDef
):
    pass


_ClientUpdatePipelineStatusResponsePipelineContentConfigTypeDef = TypedDict(
    "_ClientUpdatePipelineStatusResponsePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[
            ClientUpdatePipelineStatusResponsePipelineContentConfigPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdatePipelineStatusResponsePipelineContentConfigTypeDef(
    _ClientUpdatePipelineStatusResponsePipelineContentConfigTypeDef
):
    pass


_ClientUpdatePipelineStatusResponsePipelineNotificationsTypeDef = TypedDict(
    "_ClientUpdatePipelineStatusResponsePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class ClientUpdatePipelineStatusResponsePipelineNotificationsTypeDef(
    _ClientUpdatePipelineStatusResponsePipelineNotificationsTypeDef
):
    pass


_ClientUpdatePipelineStatusResponsePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "_ClientUpdatePipelineStatusResponsePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientUpdatePipelineStatusResponsePipelineThumbnailConfigPermissionsTypeDef(
    _ClientUpdatePipelineStatusResponsePipelineThumbnailConfigPermissionsTypeDef
):
    pass


_ClientUpdatePipelineStatusResponsePipelineThumbnailConfigTypeDef = TypedDict(
    "_ClientUpdatePipelineStatusResponsePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[
            ClientUpdatePipelineStatusResponsePipelineThumbnailConfigPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientUpdatePipelineStatusResponsePipelineThumbnailConfigTypeDef(
    _ClientUpdatePipelineStatusResponsePipelineThumbnailConfigTypeDef
):
    pass


_ClientUpdatePipelineStatusResponsePipelineTypeDef = TypedDict(
    "_ClientUpdatePipelineStatusResponsePipelineTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Status": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Role": str,
        "AwsKmsKeyArn": str,
        "Notifications": ClientUpdatePipelineStatusResponsePipelineNotificationsTypeDef,
        "ContentConfig": ClientUpdatePipelineStatusResponsePipelineContentConfigTypeDef,
        "ThumbnailConfig": ClientUpdatePipelineStatusResponsePipelineThumbnailConfigTypeDef,
    },
    total=False,
)


class ClientUpdatePipelineStatusResponsePipelineTypeDef(
    _ClientUpdatePipelineStatusResponsePipelineTypeDef
):
    """
    - **Pipeline** *(dict) --*

      A section of the response body that provides information about the pipeline.
      - **Id** *(string) --*

        The identifier for the pipeline. You use this value to identify the pipeline in which you
        want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientUpdatePipelineStatusResponseTypeDef = TypedDict(
    "_ClientUpdatePipelineStatusResponseTypeDef",
    {"Pipeline": ClientUpdatePipelineStatusResponsePipelineTypeDef},
    total=False,
)


class ClientUpdatePipelineStatusResponseTypeDef(_ClientUpdatePipelineStatusResponseTypeDef):
    """
    - *(dict) --*

      When you update status for a pipeline, Elastic Transcoder returns the values that you
      specified in the request.
      - **Pipeline** *(dict) --*

        A section of the response body that provides information about the pipeline.
        - **Id** *(string) --*

          The identifier for the pipeline. You use this value to identify the pipeline in which you
          want to perform a variety of operations, such as creating a job or a preset.
    """


_ClientUpdatePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "_ClientUpdatePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ClientUpdatePipelineThumbnailConfigPermissionsTypeDef(
    _ClientUpdatePipelineThumbnailConfigPermissionsTypeDef
):
    pass


_ClientUpdatePipelineThumbnailConfigTypeDef = TypedDict(
    "_ClientUpdatePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientUpdatePipelineThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)


class ClientUpdatePipelineThumbnailConfigTypeDef(_ClientUpdatePipelineThumbnailConfigTypeDef):
    """
    The ``ThumbnailConfig`` object specifies several values, including the Amazon S3 bucket in which
    you want Elastic Transcoder to save thumbnail files, which users you want to have access to the
    files, the type of access you want users to have, and the storage class that you want to assign
    to the files.
    If you specify values for ``ContentConfig`` , you must also specify values for
    ``ThumbnailConfig`` even if you don't want to create thumbnails.
    If you specify values for ``ContentConfig`` and ``ThumbnailConfig`` , omit the ``OutputBucket``
    object.
    * **Bucket** : The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail
    files.
    * **Permissions** (Optional): The ``Permissions`` object specifies which users and/or predefined
    Amazon S3 groups you want to have access to thumbnail files, and the type of access you want
    them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3
    groups.
    * **GranteeType** : Specify the type of value that appears in the Grantee object:

      * **Canonical** : The value in the ``Grantee`` object is either the canonical user ID for an
      AWS account or an origin access identity for an Amazon CloudFront distribution.
      .. warning::

        A canonical user ID is not the same as an AWS account number.
    """


_JobCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_JobCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class JobCompleteWaitWaiterConfigTypeDef(_JobCompleteWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_ListJobsByPipelinePaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsByPipelinePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListJobsByPipelinePaginatePaginationConfigTypeDef(
    _ListJobsByPipelinePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobsByPipelinePaginateResponseJobsInputDetectedPropertiesTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputDetectedPropertiesTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputDetectedPropertiesTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputInputCaptionsTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputInputCaptionsTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputInputCaptionsTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputTimeSpanTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputTimeSpanTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputTimeSpanTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsInputEncryptionTypeDef,
        "TimeSpan": ListJobsByPipelinePaginateResponseJobsInputTimeSpanTypeDef,
        "InputCaptions": ListJobsByPipelinePaginateResponseJobsInputInputCaptionsTypeDef,
        "DetectedProperties": ListJobsByPipelinePaginateResponseJobsInputDetectedPropertiesTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputsDetectedPropertiesTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputsDetectedPropertiesTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputsDetectedPropertiesTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputsEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputsEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputsEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputsTimeSpanTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputsTimeSpanTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputsTimeSpanTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsInputsTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsInputsTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsInputsEncryptionTypeDef,
        "TimeSpan": ListJobsByPipelinePaginateResponseJobsInputsTimeSpanTypeDef,
        "InputCaptions": ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsTypeDef,
        "DetectedProperties": ListJobsByPipelinePaginateResponseJobsInputsDetectedPropertiesTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsInputsTypeDef(
    _ListJobsByPipelinePaginateResponseJobsInputsTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputAlbumArtTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkTypeDef],
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputAlbumArtTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputAlbumArtTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputCaptionsTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef
        ],
        "CaptionFormats": List[
            ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef
        ],
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputCaptionsTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputCaptionsTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputCompositionTimeSpanTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputCompositionTimeSpanTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputCompositionTimeSpanTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputCompositionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputCompositionTypeDef",
    {"TimeSpan": ListJobsByPipelinePaginateResponseJobsOutputCompositionTimeSpanTypeDef},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputCompositionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputCompositionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputThumbnailEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputThumbnailEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputThumbnailEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputWatermarksEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputWatermarksEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputWatermarksEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputWatermarksTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputWatermarksTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputWatermarksTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ListJobsByPipelinePaginateResponseJobsOutputThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ListJobsByPipelinePaginateResponseJobsOutputWatermarksTypeDef],
        "AlbumArt": ListJobsByPipelinePaginateResponseJobsOutputAlbumArtTypeDef,
        "Composition": List[ListJobsByPipelinePaginateResponseJobsOutputCompositionTypeDef],
        "Captions": ListJobsByPipelinePaginateResponseJobsOutputCaptionsTypeDef,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkTypeDef],
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsCaptionsTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef
        ],
        "CaptionFormats": List[
            ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef
        ],
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsCaptionsTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsCaptionsTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsCompositionTimeSpanTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsCompositionTimeSpanTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsCompositionTimeSpanTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsCompositionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsCompositionTypeDef",
    {"TimeSpan": ListJobsByPipelinePaginateResponseJobsOutputsCompositionTimeSpanTypeDef},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsCompositionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsCompositionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsThumbnailEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsThumbnailEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsThumbnailEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsWatermarksEncryptionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsWatermarksEncryptionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsWatermarksEncryptionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsWatermarksTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsWatermarksTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsWatermarksTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsOutputsTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsOutputsTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ListJobsByPipelinePaginateResponseJobsOutputsThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ListJobsByPipelinePaginateResponseJobsOutputsWatermarksTypeDef],
        "AlbumArt": ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtTypeDef,
        "Composition": List[ListJobsByPipelinePaginateResponseJobsOutputsCompositionTypeDef],
        "Captions": ListJobsByPipelinePaginateResponseJobsOutputsCaptionsTypeDef,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputsEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsOutputsTypeDef(
    _ListJobsByPipelinePaginateResponseJobsOutputsTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsPlaylistsHlsContentProtectionTypeDef",
    {
        "Method": str,
        "Key": str,
        "KeyMd5": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
        "KeyStoragePolicy": str,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsPlaylistsHlsContentProtectionTypeDef(
    _ListJobsByPipelinePaginateResponseJobsPlaylistsHlsContentProtectionTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsPlaylistsPlayReadyDrmTypeDef",
    {
        "Format": str,
        "Key": str,
        "KeyMd5": str,
        "KeyId": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsPlaylistsPlayReadyDrmTypeDef(
    _ListJobsByPipelinePaginateResponseJobsPlaylistsPlayReadyDrmTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsPlaylistsTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsPlaylistsTypeDef",
    {
        "Name": str,
        "Format": str,
        "OutputKeys": List[str],
        "HlsContentProtection": ListJobsByPipelinePaginateResponseJobsPlaylistsHlsContentProtectionTypeDef,
        "PlayReadyDrm": ListJobsByPipelinePaginateResponseJobsPlaylistsPlayReadyDrmTypeDef,
        "Status": str,
        "StatusDetail": str,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsPlaylistsTypeDef(
    _ListJobsByPipelinePaginateResponseJobsPlaylistsTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsTimingTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsTimingTypeDef(
    _ListJobsByPipelinePaginateResponseJobsTimingTypeDef
):
    pass


_ListJobsByPipelinePaginateResponseJobsTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseJobsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PipelineId": str,
        "Input": ListJobsByPipelinePaginateResponseJobsInputTypeDef,
        "Inputs": List[ListJobsByPipelinePaginateResponseJobsInputsTypeDef],
        "Output": ListJobsByPipelinePaginateResponseJobsOutputTypeDef,
        "Outputs": List[ListJobsByPipelinePaginateResponseJobsOutputsTypeDef],
        "OutputKeyPrefix": str,
        "Playlists": List[ListJobsByPipelinePaginateResponseJobsPlaylistsTypeDef],
        "Status": str,
        "UserMetadata": Dict[str, str],
        "Timing": ListJobsByPipelinePaginateResponseJobsTimingTypeDef,
    },
    total=False,
)


class ListJobsByPipelinePaginateResponseJobsTypeDef(_ListJobsByPipelinePaginateResponseJobsTypeDef):
    """
    - *(dict) --*

      A section of the response body that provides information about the job that is created.
      - **Id** *(string) --*

        The identifier that Elastic Transcoder assigned to the job. You use this value to get
        settings for the job or to delete the job.
    """


_ListJobsByPipelinePaginateResponseTypeDef = TypedDict(
    "_ListJobsByPipelinePaginateResponseTypeDef",
    {"Jobs": List[ListJobsByPipelinePaginateResponseJobsTypeDef], "NextToken": str},
    total=False,
)


class ListJobsByPipelinePaginateResponseTypeDef(_ListJobsByPipelinePaginateResponseTypeDef):
    """
    - *(dict) --*

      The ``ListJobsByPipelineResponse`` structure.
      - **Jobs** *(list) --*

        An array of ``Job`` objects that are in the specified pipeline.
        - *(dict) --*

          A section of the response body that provides information about the job that is created.
          - **Id** *(string) --*

            The identifier that Elastic Transcoder assigned to the job. You use this value to get
            settings for the job or to delete the job.
    """


_ListJobsByStatusPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsByStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListJobsByStatusPaginatePaginationConfigTypeDef(
    _ListJobsByStatusPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobsByStatusPaginateResponseJobsInputDetectedPropertiesTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputDetectedPropertiesTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputDetectedPropertiesTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputInputCaptionsTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputInputCaptionsTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputInputCaptionsTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputTimeSpanTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputTimeSpanTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputTimeSpanTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsInputEncryptionTypeDef,
        "TimeSpan": ListJobsByStatusPaginateResponseJobsInputTimeSpanTypeDef,
        "InputCaptions": ListJobsByStatusPaginateResponseJobsInputInputCaptionsTypeDef,
        "DetectedProperties": ListJobsByStatusPaginateResponseJobsInputDetectedPropertiesTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputsDetectedPropertiesTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputsDetectedPropertiesTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputsDetectedPropertiesTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputsEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputsEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputsEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputsInputCaptionsTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputsInputCaptionsTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputsInputCaptionsTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputsTimeSpanTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputsTimeSpanTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputsTimeSpanTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsInputsTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsInputsTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsInputsEncryptionTypeDef,
        "TimeSpan": ListJobsByStatusPaginateResponseJobsInputsTimeSpanTypeDef,
        "InputCaptions": ListJobsByStatusPaginateResponseJobsInputsInputCaptionsTypeDef,
        "DetectedProperties": ListJobsByStatusPaginateResponseJobsInputsDetectedPropertiesTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsInputsTypeDef(
    _ListJobsByStatusPaginateResponseJobsInputsTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputAlbumArtTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkTypeDef],
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputAlbumArtTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputAlbumArtTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputCaptionsTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef
        ],
        "CaptionFormats": List[
            ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef
        ],
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputCaptionsTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputCaptionsTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputCompositionTimeSpanTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputCompositionTimeSpanTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputCompositionTimeSpanTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputCompositionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputCompositionTypeDef",
    {"TimeSpan": ListJobsByStatusPaginateResponseJobsOutputCompositionTimeSpanTypeDef},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputCompositionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputCompositionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputThumbnailEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputThumbnailEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputThumbnailEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputWatermarksEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputWatermarksEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputWatermarksEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputWatermarksTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputWatermarksTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputWatermarksTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ListJobsByStatusPaginateResponseJobsOutputThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ListJobsByStatusPaginateResponseJobsOutputWatermarksTypeDef],
        "AlbumArt": ListJobsByStatusPaginateResponseJobsOutputAlbumArtTypeDef,
        "Composition": List[ListJobsByStatusPaginateResponseJobsOutputCompositionTypeDef],
        "Captions": ListJobsByStatusPaginateResponseJobsOutputCaptionsTypeDef,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkTypeDef",
    {
        "InputKey": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "AlbumArtFormat": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsAlbumArtTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkTypeDef],
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsAlbumArtTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsAlbumArtTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsCaptionsTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef
        ],
        "CaptionFormats": List[
            ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef
        ],
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsCaptionsTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsCaptionsTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsCompositionTimeSpanTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsCompositionTimeSpanTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsCompositionTimeSpanTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsCompositionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsCompositionTypeDef",
    {"TimeSpan": ListJobsByStatusPaginateResponseJobsOutputsCompositionTimeSpanTypeDef},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsCompositionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsCompositionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsThumbnailEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsThumbnailEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsThumbnailEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsWatermarksEncryptionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsWatermarksEncryptionTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsWatermarksEncryptionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsWatermarksTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsWatermarksTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsWatermarksTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsOutputsTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsOutputsTypeDef",
    {
        "Id": str,
        "Key": str,
        "ThumbnailPattern": str,
        "ThumbnailEncryption": ListJobsByStatusPaginateResponseJobsOutputsThumbnailEncryptionTypeDef,
        "Rotate": str,
        "PresetId": str,
        "SegmentDuration": str,
        "Status": str,
        "StatusDetail": str,
        "Duration": int,
        "Width": int,
        "Height": int,
        "FrameRate": str,
        "FileSize": int,
        "DurationMillis": int,
        "Watermarks": List[ListJobsByStatusPaginateResponseJobsOutputsWatermarksTypeDef],
        "AlbumArt": ListJobsByStatusPaginateResponseJobsOutputsAlbumArtTypeDef,
        "Composition": List[ListJobsByStatusPaginateResponseJobsOutputsCompositionTypeDef],
        "Captions": ListJobsByStatusPaginateResponseJobsOutputsCaptionsTypeDef,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputsEncryptionTypeDef,
        "AppliedColorSpaceConversion": str,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsOutputsTypeDef(
    _ListJobsByStatusPaginateResponseJobsOutputsTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsPlaylistsHlsContentProtectionTypeDef",
    {
        "Method": str,
        "Key": str,
        "KeyMd5": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
        "KeyStoragePolicy": str,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsPlaylistsHlsContentProtectionTypeDef(
    _ListJobsByStatusPaginateResponseJobsPlaylistsHlsContentProtectionTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsPlaylistsPlayReadyDrmTypeDef",
    {
        "Format": str,
        "Key": str,
        "KeyMd5": str,
        "KeyId": str,
        "InitializationVector": str,
        "LicenseAcquisitionUrl": str,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsPlaylistsPlayReadyDrmTypeDef(
    _ListJobsByStatusPaginateResponseJobsPlaylistsPlayReadyDrmTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsPlaylistsTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsPlaylistsTypeDef",
    {
        "Name": str,
        "Format": str,
        "OutputKeys": List[str],
        "HlsContentProtection": ListJobsByStatusPaginateResponseJobsPlaylistsHlsContentProtectionTypeDef,
        "PlayReadyDrm": ListJobsByStatusPaginateResponseJobsPlaylistsPlayReadyDrmTypeDef,
        "Status": str,
        "StatusDetail": str,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsPlaylistsTypeDef(
    _ListJobsByStatusPaginateResponseJobsPlaylistsTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsTimingTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)


class ListJobsByStatusPaginateResponseJobsTimingTypeDef(
    _ListJobsByStatusPaginateResponseJobsTimingTypeDef
):
    pass


_ListJobsByStatusPaginateResponseJobsTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseJobsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PipelineId": str,
        "Input": ListJobsByStatusPaginateResponseJobsInputTypeDef,
        "Inputs": List[ListJobsByStatusPaginateResponseJobsInputsTypeDef],
        "Output": ListJobsByStatusPaginateResponseJobsOutputTypeDef,
        "Outputs": List[ListJobsByStatusPaginateResponseJobsOutputsTypeDef],
        "OutputKeyPrefix": str,
        "Playlists": List[ListJobsByStatusPaginateResponseJobsPlaylistsTypeDef],
        "Status": str,
        "UserMetadata": Dict[str, str],
        "Timing": ListJobsByStatusPaginateResponseJobsTimingTypeDef,
    },
    total=False,
)


class ListJobsByStatusPaginateResponseJobsTypeDef(_ListJobsByStatusPaginateResponseJobsTypeDef):
    """
    - *(dict) --*

      A section of the response body that provides information about the job that is created.
      - **Id** *(string) --*

        The identifier that Elastic Transcoder assigned to the job. You use this value to get
        settings for the job or to delete the job.
    """


_ListJobsByStatusPaginateResponseTypeDef = TypedDict(
    "_ListJobsByStatusPaginateResponseTypeDef",
    {"Jobs": List[ListJobsByStatusPaginateResponseJobsTypeDef], "NextToken": str},
    total=False,
)


class ListJobsByStatusPaginateResponseTypeDef(_ListJobsByStatusPaginateResponseTypeDef):
    """
    - *(dict) --*

      The ``ListJobsByStatusResponse`` structure.
      - **Jobs** *(list) --*

        An array of ``Job`` objects that have the specified status.
        - *(dict) --*

          A section of the response body that provides information about the job that is created.
          - **Id** *(string) --*

            The identifier that Elastic Transcoder assigned to the job. You use this value to get
            settings for the job or to delete the job.
    """


_ListPipelinesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPipelinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPipelinesPaginatePaginationConfigTypeDef(_ListPipelinesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPipelinesPaginateResponsePipelinesContentConfigPermissionsTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsePipelinesContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ListPipelinesPaginateResponsePipelinesContentConfigPermissionsTypeDef(
    _ListPipelinesPaginateResponsePipelinesContentConfigPermissionsTypeDef
):
    pass


_ListPipelinesPaginateResponsePipelinesContentConfigTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsePipelinesContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ListPipelinesPaginateResponsePipelinesContentConfigPermissionsTypeDef],
    },
    total=False,
)


class ListPipelinesPaginateResponsePipelinesContentConfigTypeDef(
    _ListPipelinesPaginateResponsePipelinesContentConfigTypeDef
):
    pass


_ListPipelinesPaginateResponsePipelinesNotificationsTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsePipelinesNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class ListPipelinesPaginateResponsePipelinesNotificationsTypeDef(
    _ListPipelinesPaginateResponsePipelinesNotificationsTypeDef
):
    pass


_ListPipelinesPaginateResponsePipelinesThumbnailConfigPermissionsTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsePipelinesThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)


class ListPipelinesPaginateResponsePipelinesThumbnailConfigPermissionsTypeDef(
    _ListPipelinesPaginateResponsePipelinesThumbnailConfigPermissionsTypeDef
):
    pass


_ListPipelinesPaginateResponsePipelinesThumbnailConfigTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsePipelinesThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[
            ListPipelinesPaginateResponsePipelinesThumbnailConfigPermissionsTypeDef
        ],
    },
    total=False,
)


class ListPipelinesPaginateResponsePipelinesThumbnailConfigTypeDef(
    _ListPipelinesPaginateResponsePipelinesThumbnailConfigTypeDef
):
    pass


_ListPipelinesPaginateResponsePipelinesTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsePipelinesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Status": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Role": str,
        "AwsKmsKeyArn": str,
        "Notifications": ListPipelinesPaginateResponsePipelinesNotificationsTypeDef,
        "ContentConfig": ListPipelinesPaginateResponsePipelinesContentConfigTypeDef,
        "ThumbnailConfig": ListPipelinesPaginateResponsePipelinesThumbnailConfigTypeDef,
    },
    total=False,
)


class ListPipelinesPaginateResponsePipelinesTypeDef(_ListPipelinesPaginateResponsePipelinesTypeDef):
    """
    - *(dict) --*

      The pipeline (queue) that is used to manage jobs.
      - **Id** *(string) --*

        The identifier for the pipeline. You use this value to identify the pipeline in which you
        want to perform a variety of operations, such as creating a job or a preset.
    """


_ListPipelinesPaginateResponseTypeDef = TypedDict(
    "_ListPipelinesPaginateResponseTypeDef",
    {"Pipelines": List[ListPipelinesPaginateResponsePipelinesTypeDef], "NextToken": str},
    total=False,
)


class ListPipelinesPaginateResponseTypeDef(_ListPipelinesPaginateResponseTypeDef):
    """
    - *(dict) --*

      A list of the pipelines associated with the current AWS account.
      - **Pipelines** *(list) --*

        An array of ``Pipeline`` objects.
        - *(dict) --*

          The pipeline (queue) that is used to manage jobs.
          - **Id** *(string) --*

            The identifier for the pipeline. You use this value to identify the pipeline in which
            you want to perform a variety of operations, such as creating a job or a preset.
    """


_ListPresetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPresetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListPresetsPaginatePaginationConfigTypeDef(_ListPresetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPresetsPaginateResponsePresetsAudioCodecOptionsTypeDef = TypedDict(
    "_ListPresetsPaginateResponsePresetsAudioCodecOptionsTypeDef",
    {"Profile": str, "BitDepth": str, "BitOrder": str, "Signed": str},
    total=False,
)


class ListPresetsPaginateResponsePresetsAudioCodecOptionsTypeDef(
    _ListPresetsPaginateResponsePresetsAudioCodecOptionsTypeDef
):
    pass


_ListPresetsPaginateResponsePresetsAudioTypeDef = TypedDict(
    "_ListPresetsPaginateResponsePresetsAudioTypeDef",
    {
        "Codec": str,
        "SampleRate": str,
        "BitRate": str,
        "Channels": str,
        "AudioPackingMode": str,
        "CodecOptions": ListPresetsPaginateResponsePresetsAudioCodecOptionsTypeDef,
    },
    total=False,
)


class ListPresetsPaginateResponsePresetsAudioTypeDef(
    _ListPresetsPaginateResponsePresetsAudioTypeDef
):
    pass


_ListPresetsPaginateResponsePresetsThumbnailsTypeDef = TypedDict(
    "_ListPresetsPaginateResponsePresetsThumbnailsTypeDef",
    {
        "Format": str,
        "Interval": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
    },
    total=False,
)


class ListPresetsPaginateResponsePresetsThumbnailsTypeDef(
    _ListPresetsPaginateResponsePresetsThumbnailsTypeDef
):
    pass


_ListPresetsPaginateResponsePresetsVideoWatermarksTypeDef = TypedDict(
    "_ListPresetsPaginateResponsePresetsVideoWatermarksTypeDef",
    {
        "Id": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "SizingPolicy": str,
        "HorizontalAlign": str,
        "HorizontalOffset": str,
        "VerticalAlign": str,
        "VerticalOffset": str,
        "Opacity": str,
        "Target": str,
    },
    total=False,
)


class ListPresetsPaginateResponsePresetsVideoWatermarksTypeDef(
    _ListPresetsPaginateResponsePresetsVideoWatermarksTypeDef
):
    pass


_ListPresetsPaginateResponsePresetsVideoTypeDef = TypedDict(
    "_ListPresetsPaginateResponsePresetsVideoTypeDef",
    {
        "Codec": str,
        "CodecOptions": Dict[str, str],
        "KeyframesMaxDist": str,
        "FixedGOP": str,
        "BitRate": str,
        "FrameRate": str,
        "MaxFrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "MaxWidth": str,
        "MaxHeight": str,
        "DisplayAspectRatio": str,
        "SizingPolicy": str,
        "PaddingPolicy": str,
        "Watermarks": List[ListPresetsPaginateResponsePresetsVideoWatermarksTypeDef],
    },
    total=False,
)


class ListPresetsPaginateResponsePresetsVideoTypeDef(
    _ListPresetsPaginateResponsePresetsVideoTypeDef
):
    pass


_ListPresetsPaginateResponsePresetsTypeDef = TypedDict(
    "_ListPresetsPaginateResponsePresetsTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Container": str,
        "Audio": ListPresetsPaginateResponsePresetsAudioTypeDef,
        "Video": ListPresetsPaginateResponsePresetsVideoTypeDef,
        "Thumbnails": ListPresetsPaginateResponsePresetsThumbnailsTypeDef,
        "Type": str,
    },
    total=False,
)


class ListPresetsPaginateResponsePresetsTypeDef(_ListPresetsPaginateResponsePresetsTypeDef):
    """
    - *(dict) --*

      Presets are templates that contain most of the settings for transcoding media files from one
      format to another. Elastic Transcoder includes some default presets for common formats, for
      example, several iPod and iPhone versions. You can also create your own presets for formats
      that aren't included among the default presets. You specify which preset you want to use when
      you create a job.
      - **Id** *(string) --*

        Identifier for the new preset. You use this value to get settings for the preset or to
        delete it.
    """


_ListPresetsPaginateResponseTypeDef = TypedDict(
    "_ListPresetsPaginateResponseTypeDef",
    {"Presets": List[ListPresetsPaginateResponsePresetsTypeDef], "NextToken": str},
    total=False,
)


class ListPresetsPaginateResponseTypeDef(_ListPresetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The ``ListPresetsResponse`` structure.
      - **Presets** *(list) --*

        An array of ``Preset`` objects.
        - *(dict) --*

          Presets are templates that contain most of the settings for transcoding media files from
          one format to another. Elastic Transcoder includes some default presets for common
          formats, for example, several iPod and iPhone versions. You can also create your own
          presets for formats that aren't included among the default presets. You specify which
          preset you want to use when you create a job.
          - **Id** *(string) --*

            Identifier for the new preset. You use this value to get settings for the preset or to
            delete it.
    """
