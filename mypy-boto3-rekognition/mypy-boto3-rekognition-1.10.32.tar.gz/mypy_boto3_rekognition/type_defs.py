"Main interface for rekognition service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    "ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef",
    "ClientCompareFacesResponseFaceMatchesFacePoseTypeDef",
    "ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef",
    "ClientCompareFacesResponseFaceMatchesFaceTypeDef",
    "ClientCompareFacesResponseFaceMatchesTypeDef",
    "ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef",
    "ClientCompareFacesResponseSourceImageFaceTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesPoseTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesQualityTypeDef",
    "ClientCompareFacesResponseUnmatchedFacesTypeDef",
    "ClientCompareFacesResponseTypeDef",
    "ClientCompareFacesSourceImageS3ObjectTypeDef",
    "ClientCompareFacesSourceImageTypeDef",
    "ClientCompareFacesTargetImageS3ObjectTypeDef",
    "ClientCompareFacesTargetImageTypeDef",
    "ClientCreateCollectionResponseTypeDef",
    "ClientCreateProjectResponseTypeDef",
    "ClientCreateProjectVersionOutputConfigTypeDef",
    "ClientCreateProjectVersionResponseTypeDef",
    "ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestTypeDef",
    "ClientCreateProjectVersionTestingDataAssetsTypeDef",
    "ClientCreateProjectVersionTestingDataTypeDef",
    "ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestTypeDef",
    "ClientCreateProjectVersionTrainingDataAssetsTypeDef",
    "ClientCreateProjectVersionTrainingDataTypeDef",
    "ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef",
    "ClientCreateStreamProcessorInputTypeDef",
    "ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef",
    "ClientCreateStreamProcessorOutputTypeDef",
    "ClientCreateStreamProcessorResponseTypeDef",
    "ClientCreateStreamProcessorSettingsFaceSearchTypeDef",
    "ClientCreateStreamProcessorSettingsTypeDef",
    "ClientDeleteCollectionResponseTypeDef",
    "ClientDeleteFacesResponseTypeDef",
    "ClientDescribeCollectionResponseTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsOutputConfigTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultTypeDef",
    "ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTypeDef",
    "ClientDescribeProjectVersionsResponseTypeDef",
    "ClientDescribeProjectsResponseProjectDescriptionsTypeDef",
    "ClientDescribeProjectsResponseTypeDef",
    "ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef",
    "ClientDescribeStreamProcessorResponseInputTypeDef",
    "ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef",
    "ClientDescribeStreamProcessorResponseOutputTypeDef",
    "ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef",
    "ClientDescribeStreamProcessorResponseSettingsTypeDef",
    "ClientDescribeStreamProcessorResponseTypeDef",
    "ClientDetectCustomLabelsImageS3ObjectTypeDef",
    "ClientDetectCustomLabelsImageTypeDef",
    "ClientDetectCustomLabelsResponseCustomLabelsGeometryBoundingBoxTypeDef",
    "ClientDetectCustomLabelsResponseCustomLabelsGeometryPolygonTypeDef",
    "ClientDetectCustomLabelsResponseCustomLabelsGeometryTypeDef",
    "ClientDetectCustomLabelsResponseCustomLabelsTypeDef",
    "ClientDetectCustomLabelsResponseTypeDef",
    "ClientDetectFacesImageS3ObjectTypeDef",
    "ClientDetectFacesImageTypeDef",
    "ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef",
    "ClientDetectFacesResponseFaceDetailsBeardTypeDef",
    "ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef",
    "ClientDetectFacesResponseFaceDetailsEmotionsTypeDef",
    "ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef",
    "ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef",
    "ClientDetectFacesResponseFaceDetailsGenderTypeDef",
    "ClientDetectFacesResponseFaceDetailsLandmarksTypeDef",
    "ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef",
    "ClientDetectFacesResponseFaceDetailsMustacheTypeDef",
    "ClientDetectFacesResponseFaceDetailsPoseTypeDef",
    "ClientDetectFacesResponseFaceDetailsQualityTypeDef",
    "ClientDetectFacesResponseFaceDetailsSmileTypeDef",
    "ClientDetectFacesResponseFaceDetailsSunglassesTypeDef",
    "ClientDetectFacesResponseFaceDetailsTypeDef",
    "ClientDetectFacesResponseTypeDef",
    "ClientDetectLabelsImageS3ObjectTypeDef",
    "ClientDetectLabelsImageTypeDef",
    "ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef",
    "ClientDetectLabelsResponseLabelsInstancesTypeDef",
    "ClientDetectLabelsResponseLabelsParentsTypeDef",
    "ClientDetectLabelsResponseLabelsTypeDef",
    "ClientDetectLabelsResponseTypeDef",
    "ClientDetectModerationLabelsHumanLoopConfigDataAttributesTypeDef",
    "ClientDetectModerationLabelsHumanLoopConfigTypeDef",
    "ClientDetectModerationLabelsImageS3ObjectTypeDef",
    "ClientDetectModerationLabelsImageTypeDef",
    "ClientDetectModerationLabelsResponseHumanLoopActivationOutputTypeDef",
    "ClientDetectModerationLabelsResponseModerationLabelsTypeDef",
    "ClientDetectModerationLabelsResponseTypeDef",
    "ClientDetectTextImageS3ObjectTypeDef",
    "ClientDetectTextImageTypeDef",
    "ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef",
    "ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef",
    "ClientDetectTextResponseTextDetectionsGeometryTypeDef",
    "ClientDetectTextResponseTextDetectionsTypeDef",
    "ClientDetectTextResponseTypeDef",
    "ClientGetCelebrityInfoResponseTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef",
    "ClientGetCelebrityRecognitionResponseCelebritiesTypeDef",
    "ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef",
    "ClientGetCelebrityRecognitionResponseTypeDef",
    "ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef",
    "ClientGetContentModerationResponseModerationLabelsTypeDef",
    "ClientGetContentModerationResponseVideoMetadataTypeDef",
    "ClientGetContentModerationResponseTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceBeardTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceGenderTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef",
    "ClientGetFaceDetectionResponseFacesFacePoseTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceQualityTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceSmileTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef",
    "ClientGetFaceDetectionResponseFacesFaceTypeDef",
    "ClientGetFaceDetectionResponseFacesTypeDef",
    "ClientGetFaceDetectionResponseVideoMetadataTypeDef",
    "ClientGetFaceDetectionResponseTypeDef",
    "ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef",
    "ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef",
    "ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonFaceTypeDef",
    "ClientGetFaceSearchResponsePersonsPersonTypeDef",
    "ClientGetFaceSearchResponsePersonsTypeDef",
    "ClientGetFaceSearchResponseVideoMetadataTypeDef",
    "ClientGetFaceSearchResponseTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef",
    "ClientGetLabelDetectionResponseLabelsLabelTypeDef",
    "ClientGetLabelDetectionResponseLabelsTypeDef",
    "ClientGetLabelDetectionResponseVideoMetadataTypeDef",
    "ClientGetLabelDetectionResponseTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef",
    "ClientGetPersonTrackingResponsePersonsPersonTypeDef",
    "ClientGetPersonTrackingResponsePersonsTypeDef",
    "ClientGetPersonTrackingResponseVideoMetadataTypeDef",
    "ClientGetPersonTrackingResponseTypeDef",
    "ClientIndexFacesImageS3ObjectTypeDef",
    "ClientIndexFacesImageTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef",
    "ClientIndexFacesResponseFaceRecordsFaceTypeDef",
    "ClientIndexFacesResponseFaceRecordsTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef",
    "ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef",
    "ClientIndexFacesResponseUnindexedFacesTypeDef",
    "ClientIndexFacesResponseTypeDef",
    "ClientListCollectionsResponseTypeDef",
    "ClientListFacesResponseFacesBoundingBoxTypeDef",
    "ClientListFacesResponseFacesTypeDef",
    "ClientListFacesResponseTypeDef",
    "ClientListStreamProcessorsResponseStreamProcessorsTypeDef",
    "ClientListStreamProcessorsResponseTypeDef",
    "ClientRecognizeCelebritiesImageS3ObjectTypeDef",
    "ClientRecognizeCelebritiesImageTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef",
    "ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef",
    "ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef",
    "ClientRecognizeCelebritiesResponseTypeDef",
    "ClientSearchFacesByImageImageS3ObjectTypeDef",
    "ClientSearchFacesByImageImageTypeDef",
    "ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef",
    "ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef",
    "ClientSearchFacesByImageResponseFaceMatchesTypeDef",
    "ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef",
    "ClientSearchFacesByImageResponseTypeDef",
    "ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    "ClientSearchFacesResponseFaceMatchesFaceTypeDef",
    "ClientSearchFacesResponseFaceMatchesTypeDef",
    "ClientSearchFacesResponseTypeDef",
    "ClientStartCelebrityRecognitionNotificationChannelTypeDef",
    "ClientStartCelebrityRecognitionResponseTypeDef",
    "ClientStartCelebrityRecognitionVideoS3ObjectTypeDef",
    "ClientStartCelebrityRecognitionVideoTypeDef",
    "ClientStartContentModerationNotificationChannelTypeDef",
    "ClientStartContentModerationResponseTypeDef",
    "ClientStartContentModerationVideoS3ObjectTypeDef",
    "ClientStartContentModerationVideoTypeDef",
    "ClientStartFaceDetectionNotificationChannelTypeDef",
    "ClientStartFaceDetectionResponseTypeDef",
    "ClientStartFaceDetectionVideoS3ObjectTypeDef",
    "ClientStartFaceDetectionVideoTypeDef",
    "ClientStartFaceSearchNotificationChannelTypeDef",
    "ClientStartFaceSearchResponseTypeDef",
    "ClientStartFaceSearchVideoS3ObjectTypeDef",
    "ClientStartFaceSearchVideoTypeDef",
    "ClientStartLabelDetectionNotificationChannelTypeDef",
    "ClientStartLabelDetectionResponseTypeDef",
    "ClientStartLabelDetectionVideoS3ObjectTypeDef",
    "ClientStartLabelDetectionVideoTypeDef",
    "ClientStartPersonTrackingNotificationChannelTypeDef",
    "ClientStartPersonTrackingResponseTypeDef",
    "ClientStartPersonTrackingVideoS3ObjectTypeDef",
    "ClientStartPersonTrackingVideoTypeDef",
    "ClientStartProjectVersionResponseTypeDef",
    "ClientStopProjectVersionResponseTypeDef",
    "DescribeProjectVersionsPaginatePaginationConfigTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsOutputConfigTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultTypeDef",
    "DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTypeDef",
    "DescribeProjectVersionsPaginateResponseTypeDef",
    "DescribeProjectsPaginatePaginationConfigTypeDef",
    "DescribeProjectsPaginateResponseProjectDescriptionsTypeDef",
    "DescribeProjectsPaginateResponseTypeDef",
    "ListCollectionsPaginatePaginationConfigTypeDef",
    "ListCollectionsPaginateResponseTypeDef",
    "ListFacesPaginatePaginationConfigTypeDef",
    "ListFacesPaginateResponseFacesBoundingBoxTypeDef",
    "ListFacesPaginateResponseFacesTypeDef",
    "ListFacesPaginateResponseTypeDef",
    "ListStreamProcessorsPaginatePaginationConfigTypeDef",
    "ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef",
    "ListStreamProcessorsPaginateResponseTypeDef",
    "ProjectVersionRunningWaitWaiterConfigTypeDef",
    "ProjectVersionTrainingCompletedWaitWaiterConfigTypeDef",
)


_ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef(
    _ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef
):
    pass


_ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef(
    _ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef
):
    pass


_ClientCompareFacesResponseFaceMatchesFacePoseTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientCompareFacesResponseFaceMatchesFacePoseTypeDef(
    _ClientCompareFacesResponseFaceMatchesFacePoseTypeDef
):
    pass


_ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef(
    _ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef
):
    pass


_ClientCompareFacesResponseFaceMatchesFaceTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesFaceTypeDef",
    {
        "BoundingBox": ClientCompareFacesResponseFaceMatchesFaceBoundingBoxTypeDef,
        "Confidence": Any,
        "Landmarks": List[ClientCompareFacesResponseFaceMatchesFaceLandmarksTypeDef],
        "Pose": ClientCompareFacesResponseFaceMatchesFacePoseTypeDef,
        "Quality": ClientCompareFacesResponseFaceMatchesFaceQualityTypeDef,
    },
    total=False,
)


class ClientCompareFacesResponseFaceMatchesFaceTypeDef(
    _ClientCompareFacesResponseFaceMatchesFaceTypeDef
):
    pass


_ClientCompareFacesResponseFaceMatchesTypeDef = TypedDict(
    "_ClientCompareFacesResponseFaceMatchesTypeDef",
    {"Similarity": Any, "Face": ClientCompareFacesResponseFaceMatchesFaceTypeDef},
    total=False,
)


class ClientCompareFacesResponseFaceMatchesTypeDef(_ClientCompareFacesResponseFaceMatchesTypeDef):
    pass


_ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef = TypedDict(
    "_ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef",
    {"Width": float, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef(
    _ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef
):
    """
    - **BoundingBox** *(dict) --*

      Bounding box of the face.
      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.
    """


_ClientCompareFacesResponseSourceImageFaceTypeDef = TypedDict(
    "_ClientCompareFacesResponseSourceImageFaceTypeDef",
    {"BoundingBox": ClientCompareFacesResponseSourceImageFaceBoundingBoxTypeDef, "Confidence": Any},
    total=False,
)


class ClientCompareFacesResponseSourceImageFaceTypeDef(
    _ClientCompareFacesResponseSourceImageFaceTypeDef
):
    """
    - **SourceImageFace** *(dict) --*

      The face in the source image that was used for comparison.
      - **BoundingBox** *(dict) --*

        Bounding box of the face.
        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.
    """


_ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef = TypedDict(
    "_ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef(
    _ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef
):
    pass


_ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef = TypedDict(
    "_ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef(
    _ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef
):
    pass


_ClientCompareFacesResponseUnmatchedFacesPoseTypeDef = TypedDict(
    "_ClientCompareFacesResponseUnmatchedFacesPoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientCompareFacesResponseUnmatchedFacesPoseTypeDef(
    _ClientCompareFacesResponseUnmatchedFacesPoseTypeDef
):
    pass


_ClientCompareFacesResponseUnmatchedFacesQualityTypeDef = TypedDict(
    "_ClientCompareFacesResponseUnmatchedFacesQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientCompareFacesResponseUnmatchedFacesQualityTypeDef(
    _ClientCompareFacesResponseUnmatchedFacesQualityTypeDef
):
    pass


_ClientCompareFacesResponseUnmatchedFacesTypeDef = TypedDict(
    "_ClientCompareFacesResponseUnmatchedFacesTypeDef",
    {
        "BoundingBox": ClientCompareFacesResponseUnmatchedFacesBoundingBoxTypeDef,
        "Confidence": Any,
        "Landmarks": List[ClientCompareFacesResponseUnmatchedFacesLandmarksTypeDef],
        "Pose": ClientCompareFacesResponseUnmatchedFacesPoseTypeDef,
        "Quality": ClientCompareFacesResponseUnmatchedFacesQualityTypeDef,
    },
    total=False,
)


class ClientCompareFacesResponseUnmatchedFacesTypeDef(
    _ClientCompareFacesResponseUnmatchedFacesTypeDef
):
    pass


_ClientCompareFacesResponseTypeDef = TypedDict(
    "_ClientCompareFacesResponseTypeDef",
    {
        "SourceImageFace": ClientCompareFacesResponseSourceImageFaceTypeDef,
        "FaceMatches": List[ClientCompareFacesResponseFaceMatchesTypeDef],
        "UnmatchedFaces": List[ClientCompareFacesResponseUnmatchedFacesTypeDef],
        "SourceImageOrientationCorrection": Literal[
            "ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"
        ],
        "TargetImageOrientationCorrection": Literal[
            "ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"
        ],
    },
    total=False,
)


class ClientCompareFacesResponseTypeDef(_ClientCompareFacesResponseTypeDef):
    """
    - *(dict) --*

      - **SourceImageFace** *(dict) --*

        The face in the source image that was used for comparison.
        - **BoundingBox** *(dict) --*

          Bounding box of the face.
          - **Width** *(float) --*

            Width of the bounding box as a ratio of the overall image width.
    """


_ClientCompareFacesSourceImageS3ObjectTypeDef = TypedDict(
    "_ClientCompareFacesSourceImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientCompareFacesSourceImageS3ObjectTypeDef(_ClientCompareFacesSourceImageS3ObjectTypeDef):
    pass


_ClientCompareFacesSourceImageTypeDef = TypedDict(
    "_ClientCompareFacesSourceImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientCompareFacesSourceImageS3ObjectTypeDef},
    total=False,
)


class ClientCompareFacesSourceImageTypeDef(_ClientCompareFacesSourceImageTypeDef):
    """
    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.
    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode
    image bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.
    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.
    """


_ClientCompareFacesTargetImageS3ObjectTypeDef = TypedDict(
    "_ClientCompareFacesTargetImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientCompareFacesTargetImageS3ObjectTypeDef(_ClientCompareFacesTargetImageS3ObjectTypeDef):
    pass


_ClientCompareFacesTargetImageTypeDef = TypedDict(
    "_ClientCompareFacesTargetImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientCompareFacesTargetImageS3ObjectTypeDef},
    total=False,
)


class ClientCompareFacesTargetImageTypeDef(_ClientCompareFacesTargetImageTypeDef):
    """
    The target image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.
    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode
    image bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.
    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.
    """


_ClientCreateCollectionResponseTypeDef = TypedDict(
    "_ClientCreateCollectionResponseTypeDef",
    {"StatusCode": int, "CollectionArn": str, "FaceModelVersion": str},
    total=False,
)


class ClientCreateCollectionResponseTypeDef(_ClientCreateCollectionResponseTypeDef):
    """
    - *(dict) --*

      - **StatusCode** *(integer) --*

        HTTP status code indicating the result of the operation.
    """


_ClientCreateProjectResponseTypeDef = TypedDict(
    "_ClientCreateProjectResponseTypeDef", {"ProjectArn": str}, total=False
)


class ClientCreateProjectResponseTypeDef(_ClientCreateProjectResponseTypeDef):
    """
    - *(dict) --*

      - **ProjectArn** *(string) --*

        The Amazon Resource Name (ARN) of the new project. You can use the ARN to configure IAM
        access to the project.
    """


_ClientCreateProjectVersionOutputConfigTypeDef = TypedDict(
    "_ClientCreateProjectVersionOutputConfigTypeDef",
    {"S3Bucket": str, "S3KeyPrefix": str},
    total=False,
)


class ClientCreateProjectVersionOutputConfigTypeDef(_ClientCreateProjectVersionOutputConfigTypeDef):
    """
    The Amazon S3 location to store the results of training.
    - **S3Bucket** *(string) --*

      The S3 bucket where training output is placed.
    """


_ClientCreateProjectVersionResponseTypeDef = TypedDict(
    "_ClientCreateProjectVersionResponseTypeDef", {"ProjectVersionArn": str}, total=False
)


class ClientCreateProjectVersionResponseTypeDef(_ClientCreateProjectVersionResponseTypeDef):
    """
    - *(dict) --*

      - **ProjectVersionArn** *(string) --*

        The ARN of the model version that was created. Use ``DescribeProjectVersion`` to get the
        current status of the training operation.
    """


_ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "_ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestS3ObjectTypeDef(
    _ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestS3ObjectTypeDef
):
    """
    - **S3Object** *(dict) --*

      Provides the S3 bucket name and object name.
      The region for the S3 bucket containing the S3 object must match the region you use for Amazon
      Rekognition operations.
      For Amazon Rekognition to process an S3 object, the user must have permission to access the S3
      object. For more information, see Resource-Based Policies in the Amazon Rekognition Developer
      Guide.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestTypeDef = TypedDict(
    "_ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestTypeDef",
    {"S3Object": ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestS3ObjectTypeDef},
    total=False,
)


class ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestTypeDef(
    _ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestTypeDef
):
    """
    - **GroundTruthManifest** *(dict) --*

      The S3 bucket that contains the Ground Truth manifest file.
      - **S3Object** *(dict) --*

        Provides the S3 bucket name and object name.
        The region for the S3 bucket containing the S3 object must match the region you use for
        Amazon Rekognition operations.
        For Amazon Rekognition to process an S3 object, the user must have permission to access the
        S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition
        Developer Guide.
        - **Bucket** *(string) --*

          Name of the S3 bucket.
    """


_ClientCreateProjectVersionTestingDataAssetsTypeDef = TypedDict(
    "_ClientCreateProjectVersionTestingDataAssetsTypeDef",
    {"GroundTruthManifest": ClientCreateProjectVersionTestingDataAssetsGroundTruthManifestTypeDef},
    total=False,
)


class ClientCreateProjectVersionTestingDataAssetsTypeDef(
    _ClientCreateProjectVersionTestingDataAssetsTypeDef
):
    """
    - *(dict) --*

      Assets are the images that you use to train and evaluate a model version. Assets are
      referenced by Sagemaker GroundTruth manifest files.
      - **GroundTruthManifest** *(dict) --*

        The S3 bucket that contains the Ground Truth manifest file.
        - **S3Object** *(dict) --*

          Provides the S3 bucket name and object name.
          The region for the S3 bucket containing the S3 object must match the region you use for
          Amazon Rekognition operations.
          For Amazon Rekognition to process an S3 object, the user must have permission to access
          the S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition
          Developer Guide.
          - **Bucket** *(string) --*

            Name of the S3 bucket.
    """


_ClientCreateProjectVersionTestingDataTypeDef = TypedDict(
    "_ClientCreateProjectVersionTestingDataTypeDef",
    {"Assets": List[ClientCreateProjectVersionTestingDataAssetsTypeDef], "AutoCreate": bool},
    total=False,
)


class ClientCreateProjectVersionTestingDataTypeDef(_ClientCreateProjectVersionTestingDataTypeDef):
    """
    The dataset to use for testing.
    - **Assets** *(list) --*

      The assets used for testing.
      - *(dict) --*

        Assets are the images that you use to train and evaluate a model version. Assets are
        referenced by Sagemaker GroundTruth manifest files.
        - **GroundTruthManifest** *(dict) --*

          The S3 bucket that contains the Ground Truth manifest file.
          - **S3Object** *(dict) --*

            Provides the S3 bucket name and object name.
            The region for the S3 bucket containing the S3 object must match the region you use for
            Amazon Rekognition operations.
            For Amazon Rekognition to process an S3 object, the user must have permission to access
            the S3 object. For more information, see Resource-Based Policies in the Amazon
            Rekognition Developer Guide.
            - **Bucket** *(string) --*

              Name of the S3 bucket.
    """


_ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "_ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestS3ObjectTypeDef(
    _ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestS3ObjectTypeDef
):
    """
    - **S3Object** *(dict) --*

      Provides the S3 bucket name and object name.
      The region for the S3 bucket containing the S3 object must match the region you use for Amazon
      Rekognition operations.
      For Amazon Rekognition to process an S3 object, the user must have permission to access the S3
      object. For more information, see Resource-Based Policies in the Amazon Rekognition Developer
      Guide.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestTypeDef = TypedDict(
    "_ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestTypeDef",
    {"S3Object": ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestS3ObjectTypeDef},
    total=False,
)


class ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestTypeDef(
    _ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestTypeDef
):
    """
    - **GroundTruthManifest** *(dict) --*

      The S3 bucket that contains the Ground Truth manifest file.
      - **S3Object** *(dict) --*

        Provides the S3 bucket name and object name.
        The region for the S3 bucket containing the S3 object must match the region you use for
        Amazon Rekognition operations.
        For Amazon Rekognition to process an S3 object, the user must have permission to access the
        S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition
        Developer Guide.
        - **Bucket** *(string) --*

          Name of the S3 bucket.
    """


_ClientCreateProjectVersionTrainingDataAssetsTypeDef = TypedDict(
    "_ClientCreateProjectVersionTrainingDataAssetsTypeDef",
    {"GroundTruthManifest": ClientCreateProjectVersionTrainingDataAssetsGroundTruthManifestTypeDef},
    total=False,
)


class ClientCreateProjectVersionTrainingDataAssetsTypeDef(
    _ClientCreateProjectVersionTrainingDataAssetsTypeDef
):
    """
    - *(dict) --*

      Assets are the images that you use to train and evaluate a model version. Assets are
      referenced by Sagemaker GroundTruth manifest files.
      - **GroundTruthManifest** *(dict) --*

        The S3 bucket that contains the Ground Truth manifest file.
        - **S3Object** *(dict) --*

          Provides the S3 bucket name and object name.
          The region for the S3 bucket containing the S3 object must match the region you use for
          Amazon Rekognition operations.
          For Amazon Rekognition to process an S3 object, the user must have permission to access
          the S3 object. For more information, see Resource-Based Policies in the Amazon Rekognition
          Developer Guide.
          - **Bucket** *(string) --*

            Name of the S3 bucket.
    """


_ClientCreateProjectVersionTrainingDataTypeDef = TypedDict(
    "_ClientCreateProjectVersionTrainingDataTypeDef",
    {"Assets": List[ClientCreateProjectVersionTrainingDataAssetsTypeDef]},
    total=False,
)


class ClientCreateProjectVersionTrainingDataTypeDef(_ClientCreateProjectVersionTrainingDataTypeDef):
    """
    The dataset to use for training.
    - **Assets** *(list) --*

      A Sagemaker GroundTruth manifest file that contains the training images (assets).
      - *(dict) --*

        Assets are the images that you use to train and evaluate a model version. Assets are
        referenced by Sagemaker GroundTruth manifest files.
        - **GroundTruthManifest** *(dict) --*

          The S3 bucket that contains the Ground Truth manifest file.
          - **S3Object** *(dict) --*

            Provides the S3 bucket name and object name.
            The region for the S3 bucket containing the S3 object must match the region you use for
            Amazon Rekognition operations.
            For Amazon Rekognition to process an S3 object, the user must have permission to access
            the S3 object. For more information, see Resource-Based Policies in the Amazon
            Rekognition Developer Guide.
            - **Bucket** *(string) --*

              Name of the S3 bucket.
    """


_ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef = TypedDict(
    "_ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef", {"Arn": str}, total=False
)


class ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef(
    _ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef
):
    """
    - **KinesisVideoStream** *(dict) --*

      The Kinesis video stream input stream for the source streaming video.
      - **Arn** *(string) --*

        ARN of the Kinesis video stream stream that streams the source video.
    """


_ClientCreateStreamProcessorInputTypeDef = TypedDict(
    "_ClientCreateStreamProcessorInputTypeDef",
    {"KinesisVideoStream": ClientCreateStreamProcessorInputKinesisVideoStreamTypeDef},
    total=False,
)


class ClientCreateStreamProcessorInputTypeDef(_ClientCreateStreamProcessorInputTypeDef):
    """
    Kinesis video stream stream that provides the source streaming video. If you are using the AWS
    CLI, the parameter name is ``StreamProcessorInput`` .
    - **KinesisVideoStream** *(dict) --*

      The Kinesis video stream input stream for the source streaming video.
      - **Arn** *(string) --*

        ARN of the Kinesis video stream stream that streams the source video.
    """


_ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef = TypedDict(
    "_ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef", {"Arn": str}, total=False
)


class ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef(
    _ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef
):
    """
    - **KinesisDataStream** *(dict) --*

      The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor
      streams the analysis results.
      - **Arn** *(string) --*

        ARN of the output Amazon Kinesis Data Streams stream.
    """


_ClientCreateStreamProcessorOutputTypeDef = TypedDict(
    "_ClientCreateStreamProcessorOutputTypeDef",
    {"KinesisDataStream": ClientCreateStreamProcessorOutputKinesisDataStreamTypeDef},
    total=False,
)


class ClientCreateStreamProcessorOutputTypeDef(_ClientCreateStreamProcessorOutputTypeDef):
    """
    Kinesis data stream stream to which Amazon Rekognition Video puts the analysis results. If you
    are using the AWS CLI, the parameter name is ``StreamProcessorOutput`` .
    - **KinesisDataStream** *(dict) --*

      The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor
      streams the analysis results.
      - **Arn** *(string) --*

        ARN of the output Amazon Kinesis Data Streams stream.
    """


_ClientCreateStreamProcessorResponseTypeDef = TypedDict(
    "_ClientCreateStreamProcessorResponseTypeDef", {"StreamProcessorArn": str}, total=False
)


class ClientCreateStreamProcessorResponseTypeDef(_ClientCreateStreamProcessorResponseTypeDef):
    """
    - *(dict) --*

      - **StreamProcessorArn** *(string) --*

        ARN for the newly create stream processor.
    """


_ClientCreateStreamProcessorSettingsFaceSearchTypeDef = TypedDict(
    "_ClientCreateStreamProcessorSettingsFaceSearchTypeDef",
    {"CollectionId": str, "FaceMatchThreshold": Any},
    total=False,
)


class ClientCreateStreamProcessorSettingsFaceSearchTypeDef(
    _ClientCreateStreamProcessorSettingsFaceSearchTypeDef
):
    """
    - **FaceSearch** *(dict) --*

      Face search settings to use on a streaming video.
      - **CollectionId** *(string) --*

        The ID of a collection that contains faces that you want to search for.
    """


_ClientCreateStreamProcessorSettingsTypeDef = TypedDict(
    "_ClientCreateStreamProcessorSettingsTypeDef",
    {"FaceSearch": ClientCreateStreamProcessorSettingsFaceSearchTypeDef},
    total=False,
)


class ClientCreateStreamProcessorSettingsTypeDef(_ClientCreateStreamProcessorSettingsTypeDef):
    """
    Face recognition input parameters to be used by the stream processor. Includes the collection to
    use for face recognition and the face attributes to detect.
    - **FaceSearch** *(dict) --*

      Face search settings to use on a streaming video.
      - **CollectionId** *(string) --*

        The ID of a collection that contains faces that you want to search for.
    """


_ClientDeleteCollectionResponseTypeDef = TypedDict(
    "_ClientDeleteCollectionResponseTypeDef", {"StatusCode": int}, total=False
)


class ClientDeleteCollectionResponseTypeDef(_ClientDeleteCollectionResponseTypeDef):
    """
    - *(dict) --*

      - **StatusCode** *(integer) --*

        HTTP status code that indicates the result of the operation.
    """


_ClientDeleteFacesResponseTypeDef = TypedDict(
    "_ClientDeleteFacesResponseTypeDef", {"DeletedFaces": List[str]}, total=False
)


class ClientDeleteFacesResponseTypeDef(_ClientDeleteFacesResponseTypeDef):
    """
    - *(dict) --*

      - **DeletedFaces** *(list) --*

        An array of strings (face IDs) of the faces that were deleted.
        - *(string) --*
    """


_ClientDescribeCollectionResponseTypeDef = TypedDict(
    "_ClientDescribeCollectionResponseTypeDef",
    {
        "FaceCount": int,
        "FaceModelVersion": str,
        "CollectionARN": str,
        "CreationTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeCollectionResponseTypeDef(_ClientDescribeCollectionResponseTypeDef):
    """
    - *(dict) --*

      - **FaceCount** *(integer) --*

        The number of faces that are indexed into the collection. To index faces into a collection,
        use  IndexFaces .
    """


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef",
    {
        "S3Object": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultTypeDef",
    {
        "F1Score": Any,
        "Summary": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef,
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsOutputConfigTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsOutputConfigTypeDef",
    {"S3Bucket": str, "S3KeyPrefix": str},
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsOutputConfigTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsOutputConfigTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef",
    {
        "GroundTruthManifest": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputTypeDef",
    {
        "Assets": List[
            ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef
        ],
        "AutoCreate": bool,
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef",
    {
        "GroundTruthManifest": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef",
    {
        "Assets": List[
            ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef
        ],
        "AutoCreate": bool,
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultTypeDef",
    {
        "Input": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultInputTypeDef,
        "Output": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef,
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef",
    {
        "GroundTruthManifest": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef",
    {
        "Assets": List[
            ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef",
    {
        "GroundTruthManifest": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef",
    {
        "Assets": List[
            ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultTypeDef",
    {
        "Input": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef,
        "Output": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef,
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultTypeDef
):
    pass


_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTypeDef",
    {
        "ProjectVersionArn": str,
        "CreationTimestamp": datetime,
        "MinInferenceUnits": int,
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ],
        "StatusMessage": str,
        "BillableTrainingTimeInSeconds": int,
        "TrainingEndTimestamp": datetime,
        "OutputConfig": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsOutputConfigTypeDef,
        "TrainingDataResult": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTrainingDataResultTypeDef,
        "TestingDataResult": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTestingDataResultTypeDef,
        "EvaluationResult": ClientDescribeProjectVersionsResponseProjectVersionDescriptionsEvaluationResultTypeDef,
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTypeDef(
    _ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTypeDef
):
    """
    - *(dict) --*

      The description of a version of a model.
      - **ProjectVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the model version.
    """


_ClientDescribeProjectVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeProjectVersionsResponseTypeDef",
    {
        "ProjectVersionDescriptions": List[
            ClientDescribeProjectVersionsResponseProjectVersionDescriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeProjectVersionsResponseTypeDef(_ClientDescribeProjectVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **ProjectVersionDescriptions** *(list) --*

        A list of model descriptions. The list is sorted by the creation date and time of the model
        versions, latest to earliest.
        - *(dict) --*

          The description of a version of a model.
          - **ProjectVersionArn** *(string) --*

            The Amazon Resource Name (ARN) of the model version.
    """


_ClientDescribeProjectsResponseProjectDescriptionsTypeDef = TypedDict(
    "_ClientDescribeProjectsResponseProjectDescriptionsTypeDef",
    {
        "ProjectArn": str,
        "CreationTimestamp": datetime,
        "Status": Literal["CREATING", "CREATED", "DELETING"],
    },
    total=False,
)


class ClientDescribeProjectsResponseProjectDescriptionsTypeDef(
    _ClientDescribeProjectsResponseProjectDescriptionsTypeDef
):
    """
    - *(dict) --*

      A description of a Amazon Rekognition Custom Labels project.
      - **ProjectArn** *(string) --*

        The Amazon Resource Name (ARN) of the project.
    """


_ClientDescribeProjectsResponseTypeDef = TypedDict(
    "_ClientDescribeProjectsResponseTypeDef",
    {
        "ProjectDescriptions": List[ClientDescribeProjectsResponseProjectDescriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeProjectsResponseTypeDef(_ClientDescribeProjectsResponseTypeDef):
    """
    - *(dict) --*

      - **ProjectDescriptions** *(list) --*

        A list of project descriptions. The list is sorted by the date and time the projects are
        created.
        - *(dict) --*

          A description of a Amazon Rekognition Custom Labels project.
          - **ProjectArn** *(string) --*

            The Amazon Resource Name (ARN) of the project.
    """


_ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef",
    {"Arn": str},
    total=False,
)


class ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef(
    _ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef
):
    pass


_ClientDescribeStreamProcessorResponseInputTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseInputTypeDef",
    {"KinesisVideoStream": ClientDescribeStreamProcessorResponseInputKinesisVideoStreamTypeDef},
    total=False,
)


class ClientDescribeStreamProcessorResponseInputTypeDef(
    _ClientDescribeStreamProcessorResponseInputTypeDef
):
    pass


_ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef",
    {"Arn": str},
    total=False,
)


class ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef(
    _ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef
):
    pass


_ClientDescribeStreamProcessorResponseOutputTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseOutputTypeDef",
    {"KinesisDataStream": ClientDescribeStreamProcessorResponseOutputKinesisDataStreamTypeDef},
    total=False,
)


class ClientDescribeStreamProcessorResponseOutputTypeDef(
    _ClientDescribeStreamProcessorResponseOutputTypeDef
):
    pass


_ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef",
    {"CollectionId": str, "FaceMatchThreshold": Any},
    total=False,
)


class ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef(
    _ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef
):
    pass


_ClientDescribeStreamProcessorResponseSettingsTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseSettingsTypeDef",
    {"FaceSearch": ClientDescribeStreamProcessorResponseSettingsFaceSearchTypeDef},
    total=False,
)


class ClientDescribeStreamProcessorResponseSettingsTypeDef(
    _ClientDescribeStreamProcessorResponseSettingsTypeDef
):
    pass


_ClientDescribeStreamProcessorResponseTypeDef = TypedDict(
    "_ClientDescribeStreamProcessorResponseTypeDef",
    {
        "Name": str,
        "StreamProcessorArn": str,
        "Status": Literal["STOPPED", "STARTING", "RUNNING", "FAILED", "STOPPING"],
        "StatusMessage": str,
        "CreationTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Input": ClientDescribeStreamProcessorResponseInputTypeDef,
        "Output": ClientDescribeStreamProcessorResponseOutputTypeDef,
        "RoleArn": str,
        "Settings": ClientDescribeStreamProcessorResponseSettingsTypeDef,
    },
    total=False,
)


class ClientDescribeStreamProcessorResponseTypeDef(_ClientDescribeStreamProcessorResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        Name of the stream processor.
    """


_ClientDetectCustomLabelsImageS3ObjectTypeDef = TypedDict(
    "_ClientDetectCustomLabelsImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectCustomLabelsImageS3ObjectTypeDef(_ClientDetectCustomLabelsImageS3ObjectTypeDef):
    pass


_ClientDetectCustomLabelsImageTypeDef = TypedDict(
    "_ClientDetectCustomLabelsImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectCustomLabelsImageS3ObjectTypeDef},
    total=False,
)


class ClientDetectCustomLabelsImageTypeDef(_ClientDetectCustomLabelsImageTypeDef):
    """
    Provides the input image either as bytes or an S3 object.
    You pass image bytes to an Amazon Rekognition API operation by using the ``Bytes`` property. For
    example, you would use the ``Bytes`` property to pass an image loaded from a local file system.
    Image bytes passed by using the ``Bytes`` property must be base64-encoded. Your code may not
    need to encode image bytes if you are using an AWS SDK to call Amazon Rekognition API
    operations.
    For more information, see Analyzing an Image Loaded from a Local File System in the Amazon
    Rekognition Developer Guide.
    You pass images stored in an S3 bucket to an Amazon Rekognition API operation by using the
    ``S3Object`` property. Images stored in an S3 bucket do not need to be base64-encoded.
    The region for the S3 bucket containing the S3 object must match the region you use for Amazon
    Rekognition operations.
    If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes using the
    Bytes property is not supported. You must first upload the image to an Amazon S3 bucket and then
    call the operation using the S3Object property.
    For Amazon Rekognition to process an S3 object, the user must have permission to access the S3
    object. For more information, see Resource Based Policies in the Amazon Rekognition Developer
    Guide.
    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.
    """


_ClientDetectCustomLabelsResponseCustomLabelsGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientDetectCustomLabelsResponseCustomLabelsGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientDetectCustomLabelsResponseCustomLabelsGeometryBoundingBoxTypeDef(
    _ClientDetectCustomLabelsResponseCustomLabelsGeometryBoundingBoxTypeDef
):
    pass


_ClientDetectCustomLabelsResponseCustomLabelsGeometryPolygonTypeDef = TypedDict(
    "_ClientDetectCustomLabelsResponseCustomLabelsGeometryPolygonTypeDef",
    {"X": Any, "Y": Any},
    total=False,
)


class ClientDetectCustomLabelsResponseCustomLabelsGeometryPolygonTypeDef(
    _ClientDetectCustomLabelsResponseCustomLabelsGeometryPolygonTypeDef
):
    pass


_ClientDetectCustomLabelsResponseCustomLabelsGeometryTypeDef = TypedDict(
    "_ClientDetectCustomLabelsResponseCustomLabelsGeometryTypeDef",
    {
        "BoundingBox": ClientDetectCustomLabelsResponseCustomLabelsGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientDetectCustomLabelsResponseCustomLabelsGeometryPolygonTypeDef],
    },
    total=False,
)


class ClientDetectCustomLabelsResponseCustomLabelsGeometryTypeDef(
    _ClientDetectCustomLabelsResponseCustomLabelsGeometryTypeDef
):
    pass


_ClientDetectCustomLabelsResponseCustomLabelsTypeDef = TypedDict(
    "_ClientDetectCustomLabelsResponseCustomLabelsTypeDef",
    {
        "Name": str,
        "Confidence": Any,
        "Geometry": ClientDetectCustomLabelsResponseCustomLabelsGeometryTypeDef,
    },
    total=False,
)


class ClientDetectCustomLabelsResponseCustomLabelsTypeDef(
    _ClientDetectCustomLabelsResponseCustomLabelsTypeDef
):
    """
    - *(dict) --*

      A custom label detected in an image by a call to  DetectCustomLabels .
      - **Name** *(string) --*

        The name of the custom label.
    """


_ClientDetectCustomLabelsResponseTypeDef = TypedDict(
    "_ClientDetectCustomLabelsResponseTypeDef",
    {"CustomLabels": List[ClientDetectCustomLabelsResponseCustomLabelsTypeDef]},
    total=False,
)


class ClientDetectCustomLabelsResponseTypeDef(_ClientDetectCustomLabelsResponseTypeDef):
    """
    - *(dict) --*

      - **CustomLabels** *(list) --*

        An array of custom labels detected in the input image.
        - *(dict) --*

          A custom label detected in an image by a call to  DetectCustomLabels .
          - **Name** *(string) --*

            The name of the custom label.
    """


_ClientDetectFacesImageS3ObjectTypeDef = TypedDict(
    "_ClientDetectFacesImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectFacesImageS3ObjectTypeDef(_ClientDetectFacesImageS3ObjectTypeDef):
    pass


_ClientDetectFacesImageTypeDef = TypedDict(
    "_ClientDetectFacesImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectFacesImageS3ObjectTypeDef},
    total=False,
)


class ClientDetectFacesImageTypeDef(_ClientDetectFacesImageTypeDef):
    """
    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.
    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode
    image bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.
    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.
    """


_ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef", {"Low": int, "High": int}, total=False
)


class ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef(
    _ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsBeardTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsBeardTypeDef(
    _ClientDetectFacesResponseFaceDetailsBeardTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef(
    _ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsEmotionsTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)


class ClientDetectFacesResponseFaceDetailsEmotionsTypeDef(
    _ClientDetectFacesResponseFaceDetailsEmotionsTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef(
    _ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef(
    _ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsGenderTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsGenderTypeDef(
    _ClientDetectFacesResponseFaceDetailsGenderTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsLandmarksTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientDetectFacesResponseFaceDetailsLandmarksTypeDef(
    _ClientDetectFacesResponseFaceDetailsLandmarksTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef(
    _ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsMustacheTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsMustacheTypeDef(
    _ClientDetectFacesResponseFaceDetailsMustacheTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsPoseTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsPoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsPoseTypeDef(
    _ClientDetectFacesResponseFaceDetailsPoseTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsQualityTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsQualityTypeDef(
    _ClientDetectFacesResponseFaceDetailsQualityTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsSmileTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsSmileTypeDef(
    _ClientDetectFacesResponseFaceDetailsSmileTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsSunglassesTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientDetectFacesResponseFaceDetailsSunglassesTypeDef(
    _ClientDetectFacesResponseFaceDetailsSunglassesTypeDef
):
    pass


_ClientDetectFacesResponseFaceDetailsTypeDef = TypedDict(
    "_ClientDetectFacesResponseFaceDetailsTypeDef",
    {
        "BoundingBox": ClientDetectFacesResponseFaceDetailsBoundingBoxTypeDef,
        "AgeRange": ClientDetectFacesResponseFaceDetailsAgeRangeTypeDef,
        "Smile": ClientDetectFacesResponseFaceDetailsSmileTypeDef,
        "Eyeglasses": ClientDetectFacesResponseFaceDetailsEyeglassesTypeDef,
        "Sunglasses": ClientDetectFacesResponseFaceDetailsSunglassesTypeDef,
        "Gender": ClientDetectFacesResponseFaceDetailsGenderTypeDef,
        "Beard": ClientDetectFacesResponseFaceDetailsBeardTypeDef,
        "Mustache": ClientDetectFacesResponseFaceDetailsMustacheTypeDef,
        "EyesOpen": ClientDetectFacesResponseFaceDetailsEyesOpenTypeDef,
        "MouthOpen": ClientDetectFacesResponseFaceDetailsMouthOpenTypeDef,
        "Emotions": List[ClientDetectFacesResponseFaceDetailsEmotionsTypeDef],
        "Landmarks": List[ClientDetectFacesResponseFaceDetailsLandmarksTypeDef],
        "Pose": ClientDetectFacesResponseFaceDetailsPoseTypeDef,
        "Quality": ClientDetectFacesResponseFaceDetailsQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)


class ClientDetectFacesResponseFaceDetailsTypeDef(_ClientDetectFacesResponseFaceDetailsTypeDef):
    """
    - *(dict) --*

      Structure containing attributes of the face that the algorithm detected.
      A ``FaceDetail`` object contains either the default facial attributes or all facial
      attributes. The default attributes are ``BoundingBox`` , ``Confidence`` , ``Landmarks`` ,
      ``Pose`` , and ``Quality`` .

        GetFaceDetection is the only Amazon Rekognition Video stored video operation that can return
        a ``FaceDetail`` object with all attributes. To specify which attributes to return, use the
        ``FaceAttributes`` input parameter for  StartFaceDetection . The following Amazon
        Rekognition Video operations return only the default attributes. The corresponding Start
        operations don't have a ``FaceAttributes`` input parameter.
    """


_ClientDetectFacesResponseTypeDef = TypedDict(
    "_ClientDetectFacesResponseTypeDef",
    {
        "FaceDetails": List[ClientDetectFacesResponseFaceDetailsTypeDef],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
    },
    total=False,
)


class ClientDetectFacesResponseTypeDef(_ClientDetectFacesResponseTypeDef):
    """
    - *(dict) --*

      - **FaceDetails** *(list) --*

        Details of each face found in the image.
        - *(dict) --*

          Structure containing attributes of the face that the algorithm detected.
          A ``FaceDetail`` object contains either the default facial attributes or all facial
          attributes. The default attributes are ``BoundingBox`` , ``Confidence`` , ``Landmarks`` ,
          ``Pose`` , and ``Quality`` .

            GetFaceDetection is the only Amazon Rekognition Video stored video operation that can
            return a ``FaceDetail`` object with all attributes. To specify which attributes to
            return, use the ``FaceAttributes`` input parameter for  StartFaceDetection . The
            following Amazon Rekognition Video operations return only the default attributes. The
            corresponding Start operations don't have a ``FaceAttributes`` input parameter.
    """


_ClientDetectLabelsImageS3ObjectTypeDef = TypedDict(
    "_ClientDetectLabelsImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectLabelsImageS3ObjectTypeDef(_ClientDetectLabelsImageS3ObjectTypeDef):
    pass


_ClientDetectLabelsImageTypeDef = TypedDict(
    "_ClientDetectLabelsImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectLabelsImageS3ObjectTypeDef},
    total=False,
)


class ClientDetectLabelsImageTypeDef(_ClientDetectLabelsImageTypeDef):
    """
    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing image bytes is not supported. Images stored in an S3 Bucket do
    not need to be base64-encoded.
    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode
    image bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.
    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.
    """


_ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef = TypedDict(
    "_ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef(
    _ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef
):
    pass


_ClientDetectLabelsResponseLabelsInstancesTypeDef = TypedDict(
    "_ClientDetectLabelsResponseLabelsInstancesTypeDef",
    {"BoundingBox": ClientDetectLabelsResponseLabelsInstancesBoundingBoxTypeDef, "Confidence": Any},
    total=False,
)


class ClientDetectLabelsResponseLabelsInstancesTypeDef(
    _ClientDetectLabelsResponseLabelsInstancesTypeDef
):
    pass


_ClientDetectLabelsResponseLabelsParentsTypeDef = TypedDict(
    "_ClientDetectLabelsResponseLabelsParentsTypeDef", {"Name": str}, total=False
)


class ClientDetectLabelsResponseLabelsParentsTypeDef(
    _ClientDetectLabelsResponseLabelsParentsTypeDef
):
    pass


_ClientDetectLabelsResponseLabelsTypeDef = TypedDict(
    "_ClientDetectLabelsResponseLabelsTypeDef",
    {
        "Name": str,
        "Confidence": Any,
        "Instances": List[ClientDetectLabelsResponseLabelsInstancesTypeDef],
        "Parents": List[ClientDetectLabelsResponseLabelsParentsTypeDef],
    },
    total=False,
)


class ClientDetectLabelsResponseLabelsTypeDef(_ClientDetectLabelsResponseLabelsTypeDef):
    """
    - *(dict) --*

      Structure containing details about the detected label, including the name, detected instances,
      parent labels, and level of confidence.
      - **Name** *(string) --*

        The name (label) of the object or scene.
    """


_ClientDetectLabelsResponseTypeDef = TypedDict(
    "_ClientDetectLabelsResponseTypeDef",
    {
        "Labels": List[ClientDetectLabelsResponseLabelsTypeDef],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
        "LabelModelVersion": str,
    },
    total=False,
)


class ClientDetectLabelsResponseTypeDef(_ClientDetectLabelsResponseTypeDef):
    """
    - *(dict) --*

      - **Labels** *(list) --*

        An array of labels for the real-world objects detected.
        - *(dict) --*

          Structure containing details about the detected label, including the name, detected
          instances, parent labels, and level of confidence.
          - **Name** *(string) --*

            The name (label) of the object or scene.
    """


_ClientDetectModerationLabelsHumanLoopConfigDataAttributesTypeDef = TypedDict(
    "_ClientDetectModerationLabelsHumanLoopConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)


class ClientDetectModerationLabelsHumanLoopConfigDataAttributesTypeDef(
    _ClientDetectModerationLabelsHumanLoopConfigDataAttributesTypeDef
):
    pass


_RequiredClientDetectModerationLabelsHumanLoopConfigTypeDef = TypedDict(
    "_RequiredClientDetectModerationLabelsHumanLoopConfigTypeDef", {"HumanLoopName": str}
)
_OptionalClientDetectModerationLabelsHumanLoopConfigTypeDef = TypedDict(
    "_OptionalClientDetectModerationLabelsHumanLoopConfigTypeDef",
    {
        "FlowDefinitionArn": str,
        "DataAttributes": ClientDetectModerationLabelsHumanLoopConfigDataAttributesTypeDef,
    },
    total=False,
)


class ClientDetectModerationLabelsHumanLoopConfigTypeDef(
    _RequiredClientDetectModerationLabelsHumanLoopConfigTypeDef,
    _OptionalClientDetectModerationLabelsHumanLoopConfigTypeDef,
):
    """
    Sets up the configuration for human evaluation, including the FlowDefinition the image will be
    sent to.
    - **HumanLoopName** *(string) --***[REQUIRED]**

      The name of the human review used for this image. This should be kept unique within a region.
    """


_ClientDetectModerationLabelsImageS3ObjectTypeDef = TypedDict(
    "_ClientDetectModerationLabelsImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectModerationLabelsImageS3ObjectTypeDef(
    _ClientDetectModerationLabelsImageS3ObjectTypeDef
):
    pass


_ClientDetectModerationLabelsImageTypeDef = TypedDict(
    "_ClientDetectModerationLabelsImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectModerationLabelsImageS3ObjectTypeDef},
    total=False,
)


class ClientDetectModerationLabelsImageTypeDef(_ClientDetectModerationLabelsImageTypeDef):
    """
    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.
    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode
    image bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.
    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.
    """


_ClientDetectModerationLabelsResponseHumanLoopActivationOutputTypeDef = TypedDict(
    "_ClientDetectModerationLabelsResponseHumanLoopActivationOutputTypeDef",
    {
        "HumanLoopArn": str,
        "HumanLoopActivationReasons": List[str],
        "HumanLoopActivationConditionsEvaluationResults": str,
    },
    total=False,
)


class ClientDetectModerationLabelsResponseHumanLoopActivationOutputTypeDef(
    _ClientDetectModerationLabelsResponseHumanLoopActivationOutputTypeDef
):
    pass


_ClientDetectModerationLabelsResponseModerationLabelsTypeDef = TypedDict(
    "_ClientDetectModerationLabelsResponseModerationLabelsTypeDef",
    {"Confidence": float, "Name": str, "ParentName": str},
    total=False,
)


class ClientDetectModerationLabelsResponseModerationLabelsTypeDef(
    _ClientDetectModerationLabelsResponseModerationLabelsTypeDef
):
    """
    - *(dict) --*

      Provides information about a single type of unsafe content found in an image or video. Each
      type of moderated content has a label within a hierarchical taxonomy. For more information,
      see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.
      - **Confidence** *(float) --*

        Specifies the confidence that Amazon Rekognition has that the label has been correctly
        identified.
        If you don't specify the ``MinConfidence`` parameter in the call to
        ``DetectModerationLabels`` , the operation returns labels with a confidence value greater
        than or equal to 50 percent.
    """


_ClientDetectModerationLabelsResponseTypeDef = TypedDict(
    "_ClientDetectModerationLabelsResponseTypeDef",
    {
        "ModerationLabels": List[ClientDetectModerationLabelsResponseModerationLabelsTypeDef],
        "ModerationModelVersion": str,
        "HumanLoopActivationOutput": ClientDetectModerationLabelsResponseHumanLoopActivationOutputTypeDef,
    },
    total=False,
)


class ClientDetectModerationLabelsResponseTypeDef(_ClientDetectModerationLabelsResponseTypeDef):
    """
    - *(dict) --*

      - **ModerationLabels** *(list) --*

        Array of detected Moderation labels and the time, in milliseconds from the start of the
        video, they were detected.
        - *(dict) --*

          Provides information about a single type of unsafe content found in an image or video.
          Each type of moderated content has a label within a hierarchical taxonomy. For more
          information, see Detecting Unsafe Content in the Amazon Rekognition Developer Guide.
          - **Confidence** *(float) --*

            Specifies the confidence that Amazon Rekognition has that the label has been correctly
            identified.
            If you don't specify the ``MinConfidence`` parameter in the call to
            ``DetectModerationLabels`` , the operation returns labels with a confidence value
            greater than or equal to 50 percent.
    """


_ClientDetectTextImageS3ObjectTypeDef = TypedDict(
    "_ClientDetectTextImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectTextImageS3ObjectTypeDef(_ClientDetectTextImageS3ObjectTypeDef):
    pass


_ClientDetectTextImageTypeDef = TypedDict(
    "_ClientDetectTextImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectTextImageS3ObjectTypeDef},
    total=False,
)


class ClientDetectTextImageTypeDef(_ClientDetectTextImageTypeDef):
    """
    The input image as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call
    Amazon Rekognition operations, you can't pass image bytes.
    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode
    image bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.
    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.
    """


_ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef(
    _ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef
):
    pass


_ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef = TypedDict(
    "_ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef",
    {"X": Any, "Y": Any},
    total=False,
)


class ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef(
    _ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef
):
    pass


_ClientDetectTextResponseTextDetectionsGeometryTypeDef = TypedDict(
    "_ClientDetectTextResponseTextDetectionsGeometryTypeDef",
    {
        "BoundingBox": ClientDetectTextResponseTextDetectionsGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientDetectTextResponseTextDetectionsGeometryPolygonTypeDef],
    },
    total=False,
)


class ClientDetectTextResponseTextDetectionsGeometryTypeDef(
    _ClientDetectTextResponseTextDetectionsGeometryTypeDef
):
    pass


_ClientDetectTextResponseTextDetectionsTypeDef = TypedDict(
    "_ClientDetectTextResponseTextDetectionsTypeDef",
    {
        "DetectedText": str,
        "Type": Literal["LINE", "WORD"],
        "Id": int,
        "ParentId": int,
        "Confidence": Any,
        "Geometry": ClientDetectTextResponseTextDetectionsGeometryTypeDef,
    },
    total=False,
)


class ClientDetectTextResponseTextDetectionsTypeDef(_ClientDetectTextResponseTextDetectionsTypeDef):
    """
    - *(dict) --*

      Information about a word or line of text detected by  DetectText .
      The ``DetectedText`` field contains the text that Amazon Rekognition detected in the image.
      Every word and line has an identifier (``Id`` ). Each word belongs to a line and has a parent
      identifier (``ParentId`` ) that identifies the line of text in which the word appears. The
      word ``Id`` is also an index for the word within a line of words.
      For more information, see Detecting Text in the Amazon Rekognition Developer Guide.
      - **DetectedText** *(string) --*

        The word or line of text recognized by Amazon Rekognition.
    """


_ClientDetectTextResponseTypeDef = TypedDict(
    "_ClientDetectTextResponseTypeDef",
    {"TextDetections": List[ClientDetectTextResponseTextDetectionsTypeDef]},
    total=False,
)


class ClientDetectTextResponseTypeDef(_ClientDetectTextResponseTypeDef):
    """
    - *(dict) --*

      - **TextDetections** *(list) --*

        An array of text that was detected in the input image.
        - *(dict) --*

          Information about a word or line of text detected by  DetectText .
          The ``DetectedText`` field contains the text that Amazon Rekognition detected in the
          image.
          Every word and line has an identifier (``Id`` ). Each word belongs to a line and has a
          parent identifier (``ParentId`` ) that identifies the line of text in which the word
          appears. The word ``Id`` is also an index for the word within a line of words.
          For more information, see Detecting Text in the Amazon Rekognition Developer Guide.
          - **DetectedText** *(string) --*

            The word or line of text recognized by Amazon Rekognition.
    """


_ClientGetCelebrityInfoResponseTypeDef = TypedDict(
    "_ClientGetCelebrityInfoResponseTypeDef", {"Urls": List[str], "Name": str}, total=False
)


class ClientGetCelebrityInfoResponseTypeDef(_ClientGetCelebrityInfoResponseTypeDef):
    """
    - *(dict) --*

      - **Urls** *(list) --*

        An array of URLs pointing to additional celebrity information.
        - *(string) --*
    """


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef",
    {
        "BoundingBox": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceAgeRangeTypeDef,
        "Smile": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSmileTypeDef,
        "Eyeglasses": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceSunglassesTypeDef,
        "Gender": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceGenderTypeDef,
        "Beard": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceBeardTypeDef,
        "Mustache": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMustacheTypeDef,
        "EyesOpen": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceMouthOpenTypeDef,
        "Emotions": List[
            ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceEmotionsTypeDef
        ],
        "Landmarks": List[
            ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceLandmarksTypeDef
        ],
        "Pose": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFacePoseTypeDef,
        "Quality": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "Id": str,
        "Confidence": Any,
        "BoundingBox": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityBoundingBoxTypeDef,
        "Face": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityFaceTypeDef,
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseCelebritiesTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseCelebritiesTypeDef",
    {
        "Timestamp": int,
        "Celebrity": ClientGetCelebrityRecognitionResponseCelebritiesCelebrityTypeDef,
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseCelebritiesTypeDef(
    _ClientGetCelebrityRecognitionResponseCelebritiesTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef(
    _ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef
):
    pass


_ClientGetCelebrityRecognitionResponseTypeDef = TypedDict(
    "_ClientGetCelebrityRecognitionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": ClientGetCelebrityRecognitionResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Celebrities": List[ClientGetCelebrityRecognitionResponseCelebritiesTypeDef],
    },
    total=False,
)


class ClientGetCelebrityRecognitionResponseTypeDef(_ClientGetCelebrityRecognitionResponseTypeDef):
    """
    - *(dict) --*

      - **JobStatus** *(string) --*

        The current status of the celebrity recognition job.
    """


_ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef = TypedDict(
    "_ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef",
    {"Confidence": Any, "Name": str, "ParentName": str},
    total=False,
)


class ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef(
    _ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef
):
    pass


_ClientGetContentModerationResponseModerationLabelsTypeDef = TypedDict(
    "_ClientGetContentModerationResponseModerationLabelsTypeDef",
    {
        "Timestamp": int,
        "ModerationLabel": ClientGetContentModerationResponseModerationLabelsModerationLabelTypeDef,
    },
    total=False,
)


class ClientGetContentModerationResponseModerationLabelsTypeDef(
    _ClientGetContentModerationResponseModerationLabelsTypeDef
):
    pass


_ClientGetContentModerationResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetContentModerationResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetContentModerationResponseVideoMetadataTypeDef(
    _ClientGetContentModerationResponseVideoMetadataTypeDef
):
    pass


_ClientGetContentModerationResponseTypeDef = TypedDict(
    "_ClientGetContentModerationResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": ClientGetContentModerationResponseVideoMetadataTypeDef,
        "ModerationLabels": List[ClientGetContentModerationResponseModerationLabelsTypeDef],
        "NextToken": str,
        "ModerationModelVersion": str,
    },
    total=False,
)


class ClientGetContentModerationResponseTypeDef(_ClientGetContentModerationResponseTypeDef):
    """
    - *(dict) --*

      - **JobStatus** *(string) --*

        The current status of the unsafe content analysis job.
    """


_ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceBeardTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceBeardTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceBeardTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceGenderTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceGenderTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceGenderTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFacePoseTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFacePoseTypeDef(
    _ClientGetFaceDetectionResponseFacesFacePoseTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceQualityTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceQualityTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceQualityTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceSmileTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceSmileTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceSmileTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesFaceTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesFaceTypeDef",
    {
        "BoundingBox": ClientGetFaceDetectionResponseFacesFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetFaceDetectionResponseFacesFaceAgeRangeTypeDef,
        "Smile": ClientGetFaceDetectionResponseFacesFaceSmileTypeDef,
        "Eyeglasses": ClientGetFaceDetectionResponseFacesFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetFaceDetectionResponseFacesFaceSunglassesTypeDef,
        "Gender": ClientGetFaceDetectionResponseFacesFaceGenderTypeDef,
        "Beard": ClientGetFaceDetectionResponseFacesFaceBeardTypeDef,
        "Mustache": ClientGetFaceDetectionResponseFacesFaceMustacheTypeDef,
        "EyesOpen": ClientGetFaceDetectionResponseFacesFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetFaceDetectionResponseFacesFaceMouthOpenTypeDef,
        "Emotions": List[ClientGetFaceDetectionResponseFacesFaceEmotionsTypeDef],
        "Landmarks": List[ClientGetFaceDetectionResponseFacesFaceLandmarksTypeDef],
        "Pose": ClientGetFaceDetectionResponseFacesFacePoseTypeDef,
        "Quality": ClientGetFaceDetectionResponseFacesFaceQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)


class ClientGetFaceDetectionResponseFacesFaceTypeDef(
    _ClientGetFaceDetectionResponseFacesFaceTypeDef
):
    pass


_ClientGetFaceDetectionResponseFacesTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseFacesTypeDef",
    {"Timestamp": int, "Face": ClientGetFaceDetectionResponseFacesFaceTypeDef},
    total=False,
)


class ClientGetFaceDetectionResponseFacesTypeDef(_ClientGetFaceDetectionResponseFacesTypeDef):
    pass


_ClientGetFaceDetectionResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetFaceDetectionResponseVideoMetadataTypeDef(
    _ClientGetFaceDetectionResponseVideoMetadataTypeDef
):
    pass


_ClientGetFaceDetectionResponseTypeDef = TypedDict(
    "_ClientGetFaceDetectionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": ClientGetFaceDetectionResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Faces": List[ClientGetFaceDetectionResponseFacesTypeDef],
    },
    total=False,
)


class ClientGetFaceDetectionResponseTypeDef(_ClientGetFaceDetectionResponseTypeDef):
    """
    - *(dict) --*

      - **JobStatus** *(string) --*

        The current status of the face detection job.
    """


_ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef(
    _ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientGetFaceSearchResponsePersonsFaceMatchesFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef(
    _ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef",
    {"Similarity": Any, "Face": ClientGetFaceSearchResponsePersonsFaceMatchesFaceTypeDef},
    total=False,
)


class ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef(
    _ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonFaceTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonFaceTypeDef",
    {
        "BoundingBox": ClientGetFaceSearchResponsePersonsPersonFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetFaceSearchResponsePersonsPersonFaceAgeRangeTypeDef,
        "Smile": ClientGetFaceSearchResponsePersonsPersonFaceSmileTypeDef,
        "Eyeglasses": ClientGetFaceSearchResponsePersonsPersonFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetFaceSearchResponsePersonsPersonFaceSunglassesTypeDef,
        "Gender": ClientGetFaceSearchResponsePersonsPersonFaceGenderTypeDef,
        "Beard": ClientGetFaceSearchResponsePersonsPersonFaceBeardTypeDef,
        "Mustache": ClientGetFaceSearchResponsePersonsPersonFaceMustacheTypeDef,
        "EyesOpen": ClientGetFaceSearchResponsePersonsPersonFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetFaceSearchResponsePersonsPersonFaceMouthOpenTypeDef,
        "Emotions": List[ClientGetFaceSearchResponsePersonsPersonFaceEmotionsTypeDef],
        "Landmarks": List[ClientGetFaceSearchResponsePersonsPersonFaceLandmarksTypeDef],
        "Pose": ClientGetFaceSearchResponsePersonsPersonFacePoseTypeDef,
        "Quality": ClientGetFaceSearchResponsePersonsPersonFaceQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonFaceTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonFaceTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsPersonTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsPersonTypeDef",
    {
        "Index": int,
        "BoundingBox": ClientGetFaceSearchResponsePersonsPersonBoundingBoxTypeDef,
        "Face": ClientGetFaceSearchResponsePersonsPersonFaceTypeDef,
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsPersonTypeDef(
    _ClientGetFaceSearchResponsePersonsPersonTypeDef
):
    pass


_ClientGetFaceSearchResponsePersonsTypeDef = TypedDict(
    "_ClientGetFaceSearchResponsePersonsTypeDef",
    {
        "Timestamp": int,
        "Person": ClientGetFaceSearchResponsePersonsPersonTypeDef,
        "FaceMatches": List[ClientGetFaceSearchResponsePersonsFaceMatchesTypeDef],
    },
    total=False,
)


class ClientGetFaceSearchResponsePersonsTypeDef(_ClientGetFaceSearchResponsePersonsTypeDef):
    pass


_ClientGetFaceSearchResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetFaceSearchResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetFaceSearchResponseVideoMetadataTypeDef(
    _ClientGetFaceSearchResponseVideoMetadataTypeDef
):
    pass


_ClientGetFaceSearchResponseTypeDef = TypedDict(
    "_ClientGetFaceSearchResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "NextToken": str,
        "VideoMetadata": ClientGetFaceSearchResponseVideoMetadataTypeDef,
        "Persons": List[ClientGetFaceSearchResponsePersonsTypeDef],
    },
    total=False,
)


class ClientGetFaceSearchResponseTypeDef(_ClientGetFaceSearchResponseTypeDef):
    """
    - *(dict) --*

      - **JobStatus** *(string) --*

        The current status of the face search job.
    """


_ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef(
    _ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef
):
    pass


_ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef",
    {
        "BoundingBox": ClientGetLabelDetectionResponseLabelsLabelInstancesBoundingBoxTypeDef,
        "Confidence": Any,
    },
    total=False,
)


class ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef(
    _ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef
):
    pass


_ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef", {"Name": str}, total=False
)


class ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef(
    _ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef
):
    pass


_ClientGetLabelDetectionResponseLabelsLabelTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseLabelsLabelTypeDef",
    {
        "Name": str,
        "Confidence": Any,
        "Instances": List[ClientGetLabelDetectionResponseLabelsLabelInstancesTypeDef],
        "Parents": List[ClientGetLabelDetectionResponseLabelsLabelParentsTypeDef],
    },
    total=False,
)


class ClientGetLabelDetectionResponseLabelsLabelTypeDef(
    _ClientGetLabelDetectionResponseLabelsLabelTypeDef
):
    pass


_ClientGetLabelDetectionResponseLabelsTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseLabelsTypeDef",
    {"Timestamp": int, "Label": ClientGetLabelDetectionResponseLabelsLabelTypeDef},
    total=False,
)


class ClientGetLabelDetectionResponseLabelsTypeDef(_ClientGetLabelDetectionResponseLabelsTypeDef):
    pass


_ClientGetLabelDetectionResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetLabelDetectionResponseVideoMetadataTypeDef(
    _ClientGetLabelDetectionResponseVideoMetadataTypeDef
):
    pass


_ClientGetLabelDetectionResponseTypeDef = TypedDict(
    "_ClientGetLabelDetectionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": ClientGetLabelDetectionResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Labels": List[ClientGetLabelDetectionResponseLabelsTypeDef],
        "LabelModelVersion": str,
    },
    total=False,
)


class ClientGetLabelDetectionResponseTypeDef(_ClientGetLabelDetectionResponseTypeDef):
    """
    - *(dict) --*

      - **JobStatus** *(string) --*

        The current status of the label detection job.
    """


_ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef",
    {
        "BoundingBox": ClientGetPersonTrackingResponsePersonsPersonFaceBoundingBoxTypeDef,
        "AgeRange": ClientGetPersonTrackingResponsePersonsPersonFaceAgeRangeTypeDef,
        "Smile": ClientGetPersonTrackingResponsePersonsPersonFaceSmileTypeDef,
        "Eyeglasses": ClientGetPersonTrackingResponsePersonsPersonFaceEyeglassesTypeDef,
        "Sunglasses": ClientGetPersonTrackingResponsePersonsPersonFaceSunglassesTypeDef,
        "Gender": ClientGetPersonTrackingResponsePersonsPersonFaceGenderTypeDef,
        "Beard": ClientGetPersonTrackingResponsePersonsPersonFaceBeardTypeDef,
        "Mustache": ClientGetPersonTrackingResponsePersonsPersonFaceMustacheTypeDef,
        "EyesOpen": ClientGetPersonTrackingResponsePersonsPersonFaceEyesOpenTypeDef,
        "MouthOpen": ClientGetPersonTrackingResponsePersonsPersonFaceMouthOpenTypeDef,
        "Emotions": List[ClientGetPersonTrackingResponsePersonsPersonFaceEmotionsTypeDef],
        "Landmarks": List[ClientGetPersonTrackingResponsePersonsPersonFaceLandmarksTypeDef],
        "Pose": ClientGetPersonTrackingResponsePersonsPersonFacePoseTypeDef,
        "Quality": ClientGetPersonTrackingResponsePersonsPersonFaceQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsPersonTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsPersonTypeDef",
    {
        "Index": int,
        "BoundingBox": ClientGetPersonTrackingResponsePersonsPersonBoundingBoxTypeDef,
        "Face": ClientGetPersonTrackingResponsePersonsPersonFaceTypeDef,
    },
    total=False,
)


class ClientGetPersonTrackingResponsePersonsPersonTypeDef(
    _ClientGetPersonTrackingResponsePersonsPersonTypeDef
):
    pass


_ClientGetPersonTrackingResponsePersonsTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponsePersonsTypeDef",
    {"Timestamp": int, "Person": ClientGetPersonTrackingResponsePersonsPersonTypeDef},
    total=False,
)


class ClientGetPersonTrackingResponsePersonsTypeDef(_ClientGetPersonTrackingResponsePersonsTypeDef):
    pass


_ClientGetPersonTrackingResponseVideoMetadataTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponseVideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": Any,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)


class ClientGetPersonTrackingResponseVideoMetadataTypeDef(
    _ClientGetPersonTrackingResponseVideoMetadataTypeDef
):
    pass


_ClientGetPersonTrackingResponseTypeDef = TypedDict(
    "_ClientGetPersonTrackingResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": ClientGetPersonTrackingResponseVideoMetadataTypeDef,
        "NextToken": str,
        "Persons": List[ClientGetPersonTrackingResponsePersonsTypeDef],
    },
    total=False,
)


class ClientGetPersonTrackingResponseTypeDef(_ClientGetPersonTrackingResponseTypeDef):
    """
    - *(dict) --*

      - **JobStatus** *(string) --*

        The current status of the person tracking job.
    """


_ClientIndexFacesImageS3ObjectTypeDef = TypedDict(
    "_ClientIndexFacesImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientIndexFacesImageS3ObjectTypeDef(_ClientIndexFacesImageS3ObjectTypeDef):
    pass


_ClientIndexFacesImageTypeDef = TypedDict(
    "_ClientIndexFacesImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientIndexFacesImageS3ObjectTypeDef},
    total=False,
)


class ClientIndexFacesImageTypeDef(_ClientIndexFacesImageTypeDef):
    """
    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes isn't supported.
    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode
    image bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.
    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.
    """


_ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef",
    {
        "BoundingBox": ClientIndexFacesResponseFaceRecordsFaceDetailBoundingBoxTypeDef,
        "AgeRange": ClientIndexFacesResponseFaceRecordsFaceDetailAgeRangeTypeDef,
        "Smile": ClientIndexFacesResponseFaceRecordsFaceDetailSmileTypeDef,
        "Eyeglasses": ClientIndexFacesResponseFaceRecordsFaceDetailEyeglassesTypeDef,
        "Sunglasses": ClientIndexFacesResponseFaceRecordsFaceDetailSunglassesTypeDef,
        "Gender": ClientIndexFacesResponseFaceRecordsFaceDetailGenderTypeDef,
        "Beard": ClientIndexFacesResponseFaceRecordsFaceDetailBeardTypeDef,
        "Mustache": ClientIndexFacesResponseFaceRecordsFaceDetailMustacheTypeDef,
        "EyesOpen": ClientIndexFacesResponseFaceRecordsFaceDetailEyesOpenTypeDef,
        "MouthOpen": ClientIndexFacesResponseFaceRecordsFaceDetailMouthOpenTypeDef,
        "Emotions": List[ClientIndexFacesResponseFaceRecordsFaceDetailEmotionsTypeDef],
        "Landmarks": List[ClientIndexFacesResponseFaceRecordsFaceDetailLandmarksTypeDef],
        "Pose": ClientIndexFacesResponseFaceRecordsFaceDetailPoseTypeDef,
        "Quality": ClientIndexFacesResponseFaceRecordsFaceDetailQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef
):
    pass


_ClientIndexFacesResponseFaceRecordsFaceTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientIndexFacesResponseFaceRecordsFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)


class ClientIndexFacesResponseFaceRecordsFaceTypeDef(
    _ClientIndexFacesResponseFaceRecordsFaceTypeDef
):
    """
    - **Face** *(dict) --*

      Describes the face properties such as the bounding box, face ID, image ID of the input image,
      and external image ID that you assigned.
      - **FaceId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the face.
    """


_ClientIndexFacesResponseFaceRecordsTypeDef = TypedDict(
    "_ClientIndexFacesResponseFaceRecordsTypeDef",
    {
        "Face": ClientIndexFacesResponseFaceRecordsFaceTypeDef,
        "FaceDetail": ClientIndexFacesResponseFaceRecordsFaceDetailTypeDef,
    },
    total=False,
)


class ClientIndexFacesResponseFaceRecordsTypeDef(_ClientIndexFacesResponseFaceRecordsTypeDef):
    """
    - *(dict) --*

      Object containing both the face metadata (stored in the backend database), and facial
      attributes that are detected but aren't stored in the database.
      - **Face** *(dict) --*

        Describes the face properties such as the bounding box, face ID, image ID of the input
        image, and external image ID that you assigned.
        - **FaceId** *(string) --*

          Unique identifier that Amazon Rekognition assigns to the face.
    """


_ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef",
    {"Low": int, "High": int},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": Any,
    },
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef",
    {"Value": Literal["Male", "Female"], "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef",
    {"Value": bool, "Confidence": Any},
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef",
    {
        "BoundingBox": ClientIndexFacesResponseUnindexedFacesFaceDetailBoundingBoxTypeDef,
        "AgeRange": ClientIndexFacesResponseUnindexedFacesFaceDetailAgeRangeTypeDef,
        "Smile": ClientIndexFacesResponseUnindexedFacesFaceDetailSmileTypeDef,
        "Eyeglasses": ClientIndexFacesResponseUnindexedFacesFaceDetailEyeglassesTypeDef,
        "Sunglasses": ClientIndexFacesResponseUnindexedFacesFaceDetailSunglassesTypeDef,
        "Gender": ClientIndexFacesResponseUnindexedFacesFaceDetailGenderTypeDef,
        "Beard": ClientIndexFacesResponseUnindexedFacesFaceDetailBeardTypeDef,
        "Mustache": ClientIndexFacesResponseUnindexedFacesFaceDetailMustacheTypeDef,
        "EyesOpen": ClientIndexFacesResponseUnindexedFacesFaceDetailEyesOpenTypeDef,
        "MouthOpen": ClientIndexFacesResponseUnindexedFacesFaceDetailMouthOpenTypeDef,
        "Emotions": List[ClientIndexFacesResponseUnindexedFacesFaceDetailEmotionsTypeDef],
        "Landmarks": List[ClientIndexFacesResponseUnindexedFacesFaceDetailLandmarksTypeDef],
        "Pose": ClientIndexFacesResponseUnindexedFacesFaceDetailPoseTypeDef,
        "Quality": ClientIndexFacesResponseUnindexedFacesFaceDetailQualityTypeDef,
        "Confidence": Any,
    },
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef(
    _ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef
):
    pass


_ClientIndexFacesResponseUnindexedFacesTypeDef = TypedDict(
    "_ClientIndexFacesResponseUnindexedFacesTypeDef",
    {
        "Reasons": List[
            Literal[
                "EXCEEDS_MAX_FACES",
                "EXTREME_POSE",
                "LOW_BRIGHTNESS",
                "LOW_SHARPNESS",
                "LOW_CONFIDENCE",
                "SMALL_BOUNDING_BOX",
                "LOW_FACE_QUALITY",
            ]
        ],
        "FaceDetail": ClientIndexFacesResponseUnindexedFacesFaceDetailTypeDef,
    },
    total=False,
)


class ClientIndexFacesResponseUnindexedFacesTypeDef(_ClientIndexFacesResponseUnindexedFacesTypeDef):
    pass


_ClientIndexFacesResponseTypeDef = TypedDict(
    "_ClientIndexFacesResponseTypeDef",
    {
        "FaceRecords": List[ClientIndexFacesResponseFaceRecordsTypeDef],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
        "FaceModelVersion": str,
        "UnindexedFaces": List[ClientIndexFacesResponseUnindexedFacesTypeDef],
    },
    total=False,
)


class ClientIndexFacesResponseTypeDef(_ClientIndexFacesResponseTypeDef):
    """
    - *(dict) --*

      - **FaceRecords** *(list) --*

        An array of faces detected and added to the collection. For more information, see Searching
        Faces in a Collection in the Amazon Rekognition Developer Guide.
        - *(dict) --*

          Object containing both the face metadata (stored in the backend database), and facial
          attributes that are detected but aren't stored in the database.
          - **Face** *(dict) --*

            Describes the face properties such as the bounding box, face ID, image ID of the input
            image, and external image ID that you assigned.
            - **FaceId** *(string) --*

              Unique identifier that Amazon Rekognition assigns to the face.
    """


_ClientListCollectionsResponseTypeDef = TypedDict(
    "_ClientListCollectionsResponseTypeDef",
    {"CollectionIds": List[str], "NextToken": str, "FaceModelVersions": List[str]},
    total=False,
)


class ClientListCollectionsResponseTypeDef(_ClientListCollectionsResponseTypeDef):
    """
    - *(dict) --*

      - **CollectionIds** *(list) --*

        An array of collection IDs.
        - *(string) --*
    """


_ClientListFacesResponseFacesBoundingBoxTypeDef = TypedDict(
    "_ClientListFacesResponseFacesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientListFacesResponseFacesBoundingBoxTypeDef(
    _ClientListFacesResponseFacesBoundingBoxTypeDef
):
    pass


_ClientListFacesResponseFacesTypeDef = TypedDict(
    "_ClientListFacesResponseFacesTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientListFacesResponseFacesBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)


class ClientListFacesResponseFacesTypeDef(_ClientListFacesResponseFacesTypeDef):
    """
    - *(dict) --*

      Describes the face properties such as the bounding box, face ID, image ID of the input image,
      and external image ID that you assigned.
      - **FaceId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the face.
    """


_ClientListFacesResponseTypeDef = TypedDict(
    "_ClientListFacesResponseTypeDef",
    {"Faces": List[ClientListFacesResponseFacesTypeDef], "NextToken": str, "FaceModelVersion": str},
    total=False,
)


class ClientListFacesResponseTypeDef(_ClientListFacesResponseTypeDef):
    """
    - *(dict) --*

      - **Faces** *(list) --*

        An array of ``Face`` objects.
        - *(dict) --*

          Describes the face properties such as the bounding box, face ID, image ID of the input
          image, and external image ID that you assigned.
          - **FaceId** *(string) --*

            Unique identifier that Amazon Rekognition assigns to the face.
    """


_ClientListStreamProcessorsResponseStreamProcessorsTypeDef = TypedDict(
    "_ClientListStreamProcessorsResponseStreamProcessorsTypeDef",
    {"Name": str, "Status": Literal["STOPPED", "STARTING", "RUNNING", "FAILED", "STOPPING"]},
    total=False,
)


class ClientListStreamProcessorsResponseStreamProcessorsTypeDef(
    _ClientListStreamProcessorsResponseStreamProcessorsTypeDef
):
    pass


_ClientListStreamProcessorsResponseTypeDef = TypedDict(
    "_ClientListStreamProcessorsResponseTypeDef",
    {
        "NextToken": str,
        "StreamProcessors": List[ClientListStreamProcessorsResponseStreamProcessorsTypeDef],
    },
    total=False,
)


class ClientListStreamProcessorsResponseTypeDef(_ClientListStreamProcessorsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the response is truncated, Amazon Rekognition Video returns this token that you can use
        in the subsequent request to retrieve the next set of stream processors.
    """


_ClientRecognizeCelebritiesImageS3ObjectTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientRecognizeCelebritiesImageS3ObjectTypeDef(
    _ClientRecognizeCelebritiesImageS3ObjectTypeDef
):
    pass


_ClientRecognizeCelebritiesImageTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientRecognizeCelebritiesImageS3ObjectTypeDef},
    total=False,
)


class ClientRecognizeCelebritiesImageTypeDef(_ClientRecognizeCelebritiesImageTypeDef):
    """
    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.
    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode
    image bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.
    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.
    """


_ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef
):
    pass


_ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef
):
    pass


_ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef
):
    pass


_ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef
):
    pass


_ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef",
    {
        "BoundingBox": ClientRecognizeCelebritiesResponseCelebrityFacesFaceBoundingBoxTypeDef,
        "Confidence": Any,
        "Landmarks": List[ClientRecognizeCelebritiesResponseCelebrityFacesFaceLandmarksTypeDef],
        "Pose": ClientRecognizeCelebritiesResponseCelebrityFacesFacePoseTypeDef,
        "Quality": ClientRecognizeCelebritiesResponseCelebrityFacesFaceQualityTypeDef,
    },
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef
):
    pass


_ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "Id": str,
        "Face": ClientRecognizeCelebritiesResponseCelebrityFacesFaceTypeDef,
        "MatchConfidence": Any,
    },
    total=False,
)


class ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef(
    _ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef
):
    """
    - *(dict) --*

      Provides information about a celebrity recognized by the  RecognizeCelebrities operation.
      - **Urls** *(list) --*

        An array of URLs pointing to additional information about the celebrity. If there is no
        additional information about the celebrity, this list is empty.
        - *(string) --*
    """


_ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef(
    _ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef
):
    pass


_ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": Any,
        "Y": Any,
    },
    total=False,
)


class ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef(
    _ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef
):
    pass


_ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef",
    {"Roll": Any, "Yaw": Any, "Pitch": Any},
    total=False,
)


class ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef(
    _ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef
):
    pass


_ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef",
    {"Brightness": Any, "Sharpness": Any},
    total=False,
)


class ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef(
    _ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef
):
    pass


_ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef",
    {
        "BoundingBox": ClientRecognizeCelebritiesResponseUnrecognizedFacesBoundingBoxTypeDef,
        "Confidence": Any,
        "Landmarks": List[ClientRecognizeCelebritiesResponseUnrecognizedFacesLandmarksTypeDef],
        "Pose": ClientRecognizeCelebritiesResponseUnrecognizedFacesPoseTypeDef,
        "Quality": ClientRecognizeCelebritiesResponseUnrecognizedFacesQualityTypeDef,
    },
    total=False,
)


class ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef(
    _ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef
):
    pass


_ClientRecognizeCelebritiesResponseTypeDef = TypedDict(
    "_ClientRecognizeCelebritiesResponseTypeDef",
    {
        "CelebrityFaces": List[ClientRecognizeCelebritiesResponseCelebrityFacesTypeDef],
        "UnrecognizedFaces": List[ClientRecognizeCelebritiesResponseUnrecognizedFacesTypeDef],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
    },
    total=False,
)


class ClientRecognizeCelebritiesResponseTypeDef(_ClientRecognizeCelebritiesResponseTypeDef):
    """
    - *(dict) --*

      - **CelebrityFaces** *(list) --*

        Details about each celebrity found in the image. Amazon Rekognition can detect a maximum of
        15 celebrities in an image.
        - *(dict) --*

          Provides information about a celebrity recognized by the  RecognizeCelebrities operation.
          - **Urls** *(list) --*

            An array of URLs pointing to additional information about the celebrity. If there is no
            additional information about the celebrity, this list is empty.
            - *(string) --*
    """


_ClientSearchFacesByImageImageS3ObjectTypeDef = TypedDict(
    "_ClientSearchFacesByImageImageS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientSearchFacesByImageImageS3ObjectTypeDef(_ClientSearchFacesByImageImageS3ObjectTypeDef):
    pass


_ClientSearchFacesByImageImageTypeDef = TypedDict(
    "_ClientSearchFacesByImageImageTypeDef",
    {"Bytes": bytes, "S3Object": ClientSearchFacesByImageImageS3ObjectTypeDef},
    total=False,
)


class ClientSearchFacesByImageImageTypeDef(_ClientSearchFacesByImageImageTypeDef):
    """
    The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon
    Rekognition operations, passing base64-encoded image bytes is not supported.
    If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode
    image bytes passed using the ``Bytes`` field. For more information, see Images in the Amazon
    Rekognition developer guide.
    - **Bytes** *(bytes) --*

      Blob of image bytes up to 5 MBs.
    """


_ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef(
    _ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef
):
    pass


_ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef = TypedDict(
    "_ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientSearchFacesByImageResponseFaceMatchesFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)


class ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef(
    _ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef
):
    pass


_ClientSearchFacesByImageResponseFaceMatchesTypeDef = TypedDict(
    "_ClientSearchFacesByImageResponseFaceMatchesTypeDef",
    {"Similarity": Any, "Face": ClientSearchFacesByImageResponseFaceMatchesFaceTypeDef},
    total=False,
)


class ClientSearchFacesByImageResponseFaceMatchesTypeDef(
    _ClientSearchFacesByImageResponseFaceMatchesTypeDef
):
    pass


_ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef = TypedDict(
    "_ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef",
    {"Width": float, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef(
    _ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef
):
    """
    - **SearchedFaceBoundingBox** *(dict) --*

      The bounding box around the face in the input image that Amazon Rekognition used for the
      search.
      - **Width** *(float) --*

        Width of the bounding box as a ratio of the overall image width.
    """


_ClientSearchFacesByImageResponseTypeDef = TypedDict(
    "_ClientSearchFacesByImageResponseTypeDef",
    {
        "SearchedFaceBoundingBox": ClientSearchFacesByImageResponseSearchedFaceBoundingBoxTypeDef,
        "SearchedFaceConfidence": Any,
        "FaceMatches": List[ClientSearchFacesByImageResponseFaceMatchesTypeDef],
        "FaceModelVersion": str,
    },
    total=False,
)


class ClientSearchFacesByImageResponseTypeDef(_ClientSearchFacesByImageResponseTypeDef):
    """
    - *(dict) --*

      - **SearchedFaceBoundingBox** *(dict) --*

        The bounding box around the face in the input image that Amazon Rekognition used for the
        search.
        - **Width** *(float) --*

          Width of the bounding box as a ratio of the overall image width.
    """


_ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef = TypedDict(
    "_ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef(
    _ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef
):
    pass


_ClientSearchFacesResponseFaceMatchesFaceTypeDef = TypedDict(
    "_ClientSearchFacesResponseFaceMatchesFaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ClientSearchFacesResponseFaceMatchesFaceBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)


class ClientSearchFacesResponseFaceMatchesFaceTypeDef(
    _ClientSearchFacesResponseFaceMatchesFaceTypeDef
):
    pass


_ClientSearchFacesResponseFaceMatchesTypeDef = TypedDict(
    "_ClientSearchFacesResponseFaceMatchesTypeDef",
    {"Similarity": Any, "Face": ClientSearchFacesResponseFaceMatchesFaceTypeDef},
    total=False,
)


class ClientSearchFacesResponseFaceMatchesTypeDef(_ClientSearchFacesResponseFaceMatchesTypeDef):
    pass


_ClientSearchFacesResponseTypeDef = TypedDict(
    "_ClientSearchFacesResponseTypeDef",
    {
        "SearchedFaceId": str,
        "FaceMatches": List[ClientSearchFacesResponseFaceMatchesTypeDef],
        "FaceModelVersion": str,
    },
    total=False,
)


class ClientSearchFacesResponseTypeDef(_ClientSearchFacesResponseTypeDef):
    """
    - *(dict) --*

      - **SearchedFaceId** *(string) --*

        ID of the face that was searched for matches in a collection.
    """


_RequiredClientStartCelebrityRecognitionNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartCelebrityRecognitionNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartCelebrityRecognitionNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartCelebrityRecognitionNotificationChannelTypeDef",
    {"RoleArn": str},
    total=False,
)


class ClientStartCelebrityRecognitionNotificationChannelTypeDef(
    _RequiredClientStartCelebrityRecognitionNotificationChannelTypeDef,
    _OptionalClientStartCelebrityRecognitionNotificationChannelTypeDef,
):
    """
    The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status
    of the celebrity recognition analysis to.
    - **SNSTopicArn** *(string) --***[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
    """


_ClientStartCelebrityRecognitionResponseTypeDef = TypedDict(
    "_ClientStartCelebrityRecognitionResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartCelebrityRecognitionResponseTypeDef(
    _ClientStartCelebrityRecognitionResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier for the celebrity recognition analysis job. Use ``JobId`` to identify the job
        in a subsequent call to ``GetCelebrityRecognition`` .
    """


_ClientStartCelebrityRecognitionVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartCelebrityRecognitionVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartCelebrityRecognitionVideoS3ObjectTypeDef(
    _ClientStartCelebrityRecognitionVideoS3ObjectTypeDef
):
    """
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_ClientStartCelebrityRecognitionVideoTypeDef = TypedDict(
    "_ClientStartCelebrityRecognitionVideoTypeDef",
    {"S3Object": ClientStartCelebrityRecognitionVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartCelebrityRecognitionVideoTypeDef(_ClientStartCelebrityRecognitionVideoTypeDef):
    """
    The video in which you want to recognize celebrities. The video must be stored in an Amazon S3
    bucket.
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_RequiredClientStartContentModerationNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartContentModerationNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartContentModerationNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartContentModerationNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartContentModerationNotificationChannelTypeDef(
    _RequiredClientStartContentModerationNotificationChannelTypeDef,
    _OptionalClientStartContentModerationNotificationChannelTypeDef,
):
    """
    The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion status
    of the unsafe content analysis to.
    - **SNSTopicArn** *(string) --***[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
    """


_ClientStartContentModerationResponseTypeDef = TypedDict(
    "_ClientStartContentModerationResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartContentModerationResponseTypeDef(_ClientStartContentModerationResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier for the unsafe content analysis job. Use ``JobId`` to identify the job in a
        subsequent call to ``GetContentModeration`` .
    """


_ClientStartContentModerationVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartContentModerationVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartContentModerationVideoS3ObjectTypeDef(
    _ClientStartContentModerationVideoS3ObjectTypeDef
):
    """
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_ClientStartContentModerationVideoTypeDef = TypedDict(
    "_ClientStartContentModerationVideoTypeDef",
    {"S3Object": ClientStartContentModerationVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartContentModerationVideoTypeDef(_ClientStartContentModerationVideoTypeDef):
    """
    The video in which you want to detect unsafe content. The video must be stored in an Amazon S3
    bucket.
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_RequiredClientStartFaceDetectionNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartFaceDetectionNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartFaceDetectionNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartFaceDetectionNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartFaceDetectionNotificationChannelTypeDef(
    _RequiredClientStartFaceDetectionNotificationChannelTypeDef,
    _OptionalClientStartFaceDetectionNotificationChannelTypeDef,
):
    """
    The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the
    completion status of the face detection operation.
    - **SNSTopicArn** *(string) --***[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
    """


_ClientStartFaceDetectionResponseTypeDef = TypedDict(
    "_ClientStartFaceDetectionResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartFaceDetectionResponseTypeDef(_ClientStartFaceDetectionResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier for the face detection job. Use ``JobId`` to identify the job in a subsequent
        call to ``GetFaceDetection`` .
    """


_ClientStartFaceDetectionVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartFaceDetectionVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartFaceDetectionVideoS3ObjectTypeDef(_ClientStartFaceDetectionVideoS3ObjectTypeDef):
    """
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_ClientStartFaceDetectionVideoTypeDef = TypedDict(
    "_ClientStartFaceDetectionVideoTypeDef",
    {"S3Object": ClientStartFaceDetectionVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartFaceDetectionVideoTypeDef(_ClientStartFaceDetectionVideoTypeDef):
    """
    The video in which you want to detect faces. The video must be stored in an Amazon S3 bucket.
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_RequiredClientStartFaceSearchNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartFaceSearchNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartFaceSearchNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartFaceSearchNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartFaceSearchNotificationChannelTypeDef(
    _RequiredClientStartFaceSearchNotificationChannelTypeDef,
    _OptionalClientStartFaceSearchNotificationChannelTypeDef,
):
    """
    The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the
    completion status of the search.
    - **SNSTopicArn** *(string) --***[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
    """


_ClientStartFaceSearchResponseTypeDef = TypedDict(
    "_ClientStartFaceSearchResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartFaceSearchResponseTypeDef(_ClientStartFaceSearchResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier for the search job. Use ``JobId`` to identify the job in a subsequent call to
        ``GetFaceSearch`` .
    """


_ClientStartFaceSearchVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartFaceSearchVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartFaceSearchVideoS3ObjectTypeDef(_ClientStartFaceSearchVideoS3ObjectTypeDef):
    """
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_ClientStartFaceSearchVideoTypeDef = TypedDict(
    "_ClientStartFaceSearchVideoTypeDef",
    {"S3Object": ClientStartFaceSearchVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartFaceSearchVideoTypeDef(_ClientStartFaceSearchVideoTypeDef):
    """
    The video you want to search. The video must be stored in an Amazon S3 bucket.
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_RequiredClientStartLabelDetectionNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartLabelDetectionNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartLabelDetectionNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartLabelDetectionNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartLabelDetectionNotificationChannelTypeDef(
    _RequiredClientStartLabelDetectionNotificationChannelTypeDef,
    _OptionalClientStartLabelDetectionNotificationChannelTypeDef,
):
    """
    The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion status of
    the label detection operation to.
    - **SNSTopicArn** *(string) --***[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
    """


_ClientStartLabelDetectionResponseTypeDef = TypedDict(
    "_ClientStartLabelDetectionResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartLabelDetectionResponseTypeDef(_ClientStartLabelDetectionResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier for the label detection job. Use ``JobId`` to identify the job in a
        subsequent call to ``GetLabelDetection`` .
    """


_ClientStartLabelDetectionVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartLabelDetectionVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartLabelDetectionVideoS3ObjectTypeDef(_ClientStartLabelDetectionVideoS3ObjectTypeDef):
    """
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_ClientStartLabelDetectionVideoTypeDef = TypedDict(
    "_ClientStartLabelDetectionVideoTypeDef",
    {"S3Object": ClientStartLabelDetectionVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartLabelDetectionVideoTypeDef(_ClientStartLabelDetectionVideoTypeDef):
    """
    The video in which you want to detect labels. The video must be stored in an Amazon S3 bucket.
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_RequiredClientStartPersonTrackingNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartPersonTrackingNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartPersonTrackingNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartPersonTrackingNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartPersonTrackingNotificationChannelTypeDef(
    _RequiredClientStartPersonTrackingNotificationChannelTypeDef,
    _OptionalClientStartPersonTrackingNotificationChannelTypeDef,
):
    """
    The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion status of
    the people detection operation to.
    - **SNSTopicArn** *(string) --***[REQUIRED]**

      The Amazon SNS topic to which Amazon Rekognition to posts the completion status.
    """


_ClientStartPersonTrackingResponseTypeDef = TypedDict(
    "_ClientStartPersonTrackingResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartPersonTrackingResponseTypeDef(_ClientStartPersonTrackingResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier for the person detection job. Use ``JobId`` to identify the job in a
        subsequent call to ``GetPersonTracking`` .
    """


_ClientStartPersonTrackingVideoS3ObjectTypeDef = TypedDict(
    "_ClientStartPersonTrackingVideoS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartPersonTrackingVideoS3ObjectTypeDef(_ClientStartPersonTrackingVideoS3ObjectTypeDef):
    """
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_ClientStartPersonTrackingVideoTypeDef = TypedDict(
    "_ClientStartPersonTrackingVideoTypeDef",
    {"S3Object": ClientStartPersonTrackingVideoS3ObjectTypeDef},
    total=False,
)


class ClientStartPersonTrackingVideoTypeDef(_ClientStartPersonTrackingVideoTypeDef):
    """
    The video in which you want to detect people. The video must be stored in an Amazon S3 bucket.
    - **S3Object** *(dict) --*

      The Amazon S3 bucket name and file name for the video.
      - **Bucket** *(string) --*

        Name of the S3 bucket.
    """


_ClientStartProjectVersionResponseTypeDef = TypedDict(
    "_ClientStartProjectVersionResponseTypeDef",
    {
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ]
    },
    total=False,
)


class ClientStartProjectVersionResponseTypeDef(_ClientStartProjectVersionResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The current running status of the model.
    """


_ClientStopProjectVersionResponseTypeDef = TypedDict(
    "_ClientStopProjectVersionResponseTypeDef",
    {
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ]
    },
    total=False,
)


class ClientStopProjectVersionResponseTypeDef(_ClientStopProjectVersionResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The current status of the stop operation.
    """


_DescribeProjectVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeProjectVersionsPaginatePaginationConfigTypeDef(
    _DescribeProjectVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef",
    {
        "S3Object": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryS3ObjectTypeDef
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultTypeDef",
    {
        "F1Score": Any,
        "Summary": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultSummaryTypeDef,
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsOutputConfigTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsOutputConfigTypeDef",
    {"S3Bucket": str, "S3KeyPrefix": str},
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsOutputConfigTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsOutputConfigTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef",
    {
        "GroundTruthManifest": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputTypeDef",
    {
        "Assets": List[
            DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputAssetsTypeDef
        ],
        "AutoCreate": bool,
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef",
    {
        "GroundTruthManifest": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef",
    {
        "Assets": List[
            DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputAssetsTypeDef
        ],
        "AutoCreate": bool,
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultTypeDef",
    {
        "Input": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultInputTypeDef,
        "Output": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultOutputTypeDef,
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef",
    {
        "GroundTruthManifest": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef",
    {
        "Assets": List[
            DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputAssetsTypeDef
        ]
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef",
    {
        "S3Object": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestS3ObjectTypeDef
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef",
    {
        "GroundTruthManifest": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsGroundTruthManifestTypeDef
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef",
    {
        "Assets": List[
            DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputAssetsTypeDef
        ]
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultTypeDef",
    {
        "Input": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultInputTypeDef,
        "Output": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultOutputTypeDef,
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultTypeDef
):
    pass


_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTypeDef",
    {
        "ProjectVersionArn": str,
        "CreationTimestamp": datetime,
        "MinInferenceUnits": int,
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ],
        "StatusMessage": str,
        "BillableTrainingTimeInSeconds": int,
        "TrainingEndTimestamp": datetime,
        "OutputConfig": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsOutputConfigTypeDef,
        "TrainingDataResult": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTrainingDataResultTypeDef,
        "TestingDataResult": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTestingDataResultTypeDef,
        "EvaluationResult": DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsEvaluationResultTypeDef,
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTypeDef(
    _DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTypeDef
):
    """
    - *(dict) --*

      The description of a version of a model.
      - **ProjectVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the model version.
    """


_DescribeProjectVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeProjectVersionsPaginateResponseTypeDef",
    {
        "ProjectVersionDescriptions": List[
            DescribeProjectVersionsPaginateResponseProjectVersionDescriptionsTypeDef
        ]
    },
    total=False,
)


class DescribeProjectVersionsPaginateResponseTypeDef(
    _DescribeProjectVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ProjectVersionDescriptions** *(list) --*

        A list of model descriptions. The list is sorted by the creation date and time of the model
        versions, latest to earliest.
        - *(dict) --*

          The description of a version of a model.
          - **ProjectVersionArn** *(string) --*

            The Amazon Resource Name (ARN) of the model version.
    """


_DescribeProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeProjectsPaginatePaginationConfigTypeDef(
    _DescribeProjectsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeProjectsPaginateResponseProjectDescriptionsTypeDef = TypedDict(
    "_DescribeProjectsPaginateResponseProjectDescriptionsTypeDef",
    {
        "ProjectArn": str,
        "CreationTimestamp": datetime,
        "Status": Literal["CREATING", "CREATED", "DELETING"],
    },
    total=False,
)


class DescribeProjectsPaginateResponseProjectDescriptionsTypeDef(
    _DescribeProjectsPaginateResponseProjectDescriptionsTypeDef
):
    """
    - *(dict) --*

      A description of a Amazon Rekognition Custom Labels project.
      - **ProjectArn** *(string) --*

        The Amazon Resource Name (ARN) of the project.
    """


_DescribeProjectsPaginateResponseTypeDef = TypedDict(
    "_DescribeProjectsPaginateResponseTypeDef",
    {"ProjectDescriptions": List[DescribeProjectsPaginateResponseProjectDescriptionsTypeDef]},
    total=False,
)


class DescribeProjectsPaginateResponseTypeDef(_DescribeProjectsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ProjectDescriptions** *(list) --*

        A list of project descriptions. The list is sorted by the date and time the projects are
        created.
        - *(dict) --*

          A description of a Amazon Rekognition Custom Labels project.
          - **ProjectArn** *(string) --*

            The Amazon Resource Name (ARN) of the project.
    """


_ListCollectionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCollectionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCollectionsPaginatePaginationConfigTypeDef(
    _ListCollectionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCollectionsPaginateResponseTypeDef = TypedDict(
    "_ListCollectionsPaginateResponseTypeDef",
    {"CollectionIds": List[str], "FaceModelVersions": List[str]},
    total=False,
)


class ListCollectionsPaginateResponseTypeDef(_ListCollectionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **CollectionIds** *(list) --*

        An array of collection IDs.
        - *(string) --*
    """


_ListFacesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFacesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFacesPaginatePaginationConfigTypeDef(_ListFacesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFacesPaginateResponseFacesBoundingBoxTypeDef = TypedDict(
    "_ListFacesPaginateResponseFacesBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ListFacesPaginateResponseFacesBoundingBoxTypeDef(
    _ListFacesPaginateResponseFacesBoundingBoxTypeDef
):
    pass


_ListFacesPaginateResponseFacesTypeDef = TypedDict(
    "_ListFacesPaginateResponseFacesTypeDef",
    {
        "FaceId": str,
        "BoundingBox": ListFacesPaginateResponseFacesBoundingBoxTypeDef,
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": Any,
    },
    total=False,
)


class ListFacesPaginateResponseFacesTypeDef(_ListFacesPaginateResponseFacesTypeDef):
    """
    - *(dict) --*

      Describes the face properties such as the bounding box, face ID, image ID of the input image,
      and external image ID that you assigned.
      - **FaceId** *(string) --*

        Unique identifier that Amazon Rekognition assigns to the face.
    """


_ListFacesPaginateResponseTypeDef = TypedDict(
    "_ListFacesPaginateResponseTypeDef",
    {"Faces": List[ListFacesPaginateResponseFacesTypeDef], "FaceModelVersion": str},
    total=False,
)


class ListFacesPaginateResponseTypeDef(_ListFacesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Faces** *(list) --*

        An array of ``Face`` objects.
        - *(dict) --*

          Describes the face properties such as the bounding box, face ID, image ID of the input
          image, and external image ID that you assigned.
          - **FaceId** *(string) --*

            Unique identifier that Amazon Rekognition assigns to the face.
    """


_ListStreamProcessorsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStreamProcessorsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStreamProcessorsPaginatePaginationConfigTypeDef(
    _ListStreamProcessorsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef = TypedDict(
    "_ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef",
    {"Name": str, "Status": Literal["STOPPED", "STARTING", "RUNNING", "FAILED", "STOPPING"]},
    total=False,
)


class ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef(
    _ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef
):
    """
    - *(dict) --*

      An object that recognizes faces in a streaming video. An Amazon Rekognition stream processor
      is created by a call to  CreateStreamProcessor . The request parameters for
      ``CreateStreamProcessor`` describe the Kinesis video stream source for the streaming video,
      face recognition parameters, and where to stream the analysis resullts.
      - **Name** *(string) --*

        Name of the Amazon Rekognition stream processor.
    """


_ListStreamProcessorsPaginateResponseTypeDef = TypedDict(
    "_ListStreamProcessorsPaginateResponseTypeDef",
    {"StreamProcessors": List[ListStreamProcessorsPaginateResponseStreamProcessorsTypeDef]},
    total=False,
)


class ListStreamProcessorsPaginateResponseTypeDef(_ListStreamProcessorsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **StreamProcessors** *(list) --*

        List of stream processors that you have created.
        - *(dict) --*

          An object that recognizes faces in a streaming video. An Amazon Rekognition stream
          processor is created by a call to  CreateStreamProcessor . The request parameters for
          ``CreateStreamProcessor`` describe the Kinesis video stream source for the streaming
          video, face recognition parameters, and where to stream the analysis resullts.
          - **Name** *(string) --*

            Name of the Amazon Rekognition stream processor.
    """


_ProjectVersionRunningWaitWaiterConfigTypeDef = TypedDict(
    "_ProjectVersionRunningWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class ProjectVersionRunningWaitWaiterConfigTypeDef(_ProjectVersionRunningWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_ProjectVersionTrainingCompletedWaitWaiterConfigTypeDef = TypedDict(
    "_ProjectVersionTrainingCompletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ProjectVersionTrainingCompletedWaitWaiterConfigTypeDef(
    _ProjectVersionTrainingCompletedWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 120
    """
