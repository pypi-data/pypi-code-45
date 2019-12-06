"Main interface for elastictranscoder service type defs"
from __future__ import annotations

import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateJobInputDetectedPropertiesTypeDef = TypedDict(
    "ClientCreateJobInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ClientCreateJobInputEncryptionTypeDef = TypedDict(
    "ClientCreateJobInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientCreateJobInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientCreateJobInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobInputInputCaptionsTypeDef = TypedDict(
    "ClientCreateJobInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobInputInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)

ClientCreateJobInputTimeSpanTypeDef = TypedDict(
    "ClientCreateJobInputTimeSpanTypeDef", {"StartTime": str, "Duration": str}, total=False
)

ClientCreateJobInputTypeDef = TypedDict(
    "ClientCreateJobInputTypeDef",
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

ClientCreateJobInputsDetectedPropertiesTypeDef = TypedDict(
    "ClientCreateJobInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ClientCreateJobInputsEncryptionTypeDef = TypedDict(
    "ClientCreateJobInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientCreateJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientCreateJobInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobInputsInputCaptionsTypeDef = TypedDict(
    "ClientCreateJobInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobInputsInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)

ClientCreateJobInputsTimeSpanTypeDef = TypedDict(
    "ClientCreateJobInputsTimeSpanTypeDef", {"StartTime": str, "Duration": str}, total=False
)

ClientCreateJobInputsTypeDef = TypedDict(
    "ClientCreateJobInputsTypeDef",
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

ClientCreateJobOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputAlbumArtArtworkTypeDef = TypedDict(
    "ClientCreateJobOutputAlbumArtArtworkTypeDef",
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

ClientCreateJobOutputAlbumArtTypeDef = TypedDict(
    "ClientCreateJobOutputAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientCreateJobOutputAlbumArtArtworkTypeDef]},
    total=False,
)

ClientCreateJobOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "ClientCreateJobOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientCreateJobOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientCreateJobOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobOutputCaptionsTypeDef = TypedDict(
    "ClientCreateJobOutputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobOutputCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientCreateJobOutputCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)

ClientCreateJobOutputCompositionTimeSpanTypeDef = TypedDict(
    "ClientCreateJobOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientCreateJobOutputCompositionTypeDef = TypedDict(
    "ClientCreateJobOutputCompositionTypeDef",
    {"TimeSpan": ClientCreateJobOutputCompositionTimeSpanTypeDef},
    total=False,
)

ClientCreateJobOutputEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputThumbnailEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputWatermarksEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputWatermarksTypeDef = TypedDict(
    "ClientCreateJobOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientCreateJobOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobOutputTypeDef = TypedDict(
    "ClientCreateJobOutputTypeDef",
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

ClientCreateJobOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputsAlbumArtArtworkTypeDef = TypedDict(
    "ClientCreateJobOutputsAlbumArtArtworkTypeDef",
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

ClientCreateJobOutputsAlbumArtTypeDef = TypedDict(
    "ClientCreateJobOutputsAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientCreateJobOutputsAlbumArtArtworkTypeDef]},
    total=False,
)

ClientCreateJobOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "ClientCreateJobOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientCreateJobOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientCreateJobOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobOutputsCaptionsTypeDef = TypedDict(
    "ClientCreateJobOutputsCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobOutputsCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientCreateJobOutputsCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)

ClientCreateJobOutputsCompositionTimeSpanTypeDef = TypedDict(
    "ClientCreateJobOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientCreateJobOutputsCompositionTypeDef = TypedDict(
    "ClientCreateJobOutputsCompositionTypeDef",
    {"TimeSpan": ClientCreateJobOutputsCompositionTimeSpanTypeDef},
    total=False,
)

ClientCreateJobOutputsEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputsThumbnailEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputsWatermarksEncryptionTypeDef = TypedDict(
    "ClientCreateJobOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobOutputsWatermarksTypeDef = TypedDict(
    "ClientCreateJobOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientCreateJobOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobOutputsTypeDef = TypedDict(
    "ClientCreateJobOutputsTypeDef",
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

ClientCreateJobPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "ClientCreateJobPlaylistsHlsContentProtectionTypeDef",
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

ClientCreateJobPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "ClientCreateJobPlaylistsPlayReadyDrmTypeDef",
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

ClientCreateJobPlaylistsTypeDef = TypedDict(
    "ClientCreateJobPlaylistsTypeDef",
    {
        "Name": str,
        "Format": str,
        "OutputKeys": List[str],
        "HlsContentProtection": ClientCreateJobPlaylistsHlsContentProtectionTypeDef,
        "PlayReadyDrm": ClientCreateJobPlaylistsPlayReadyDrmTypeDef,
    },
    total=False,
)

ClientCreateJobResponseJobInputDetectedPropertiesTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ClientCreateJobResponseJobInputEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobResponseJobInputInputCaptionsTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobResponseJobInputInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)

ClientCreateJobResponseJobInputTimeSpanTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientCreateJobResponseJobInputTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputTypeDef",
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

ClientCreateJobResponseJobInputsDetectedPropertiesTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ClientCreateJobResponseJobInputsEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobResponseJobInputsInputCaptionsTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)

ClientCreateJobResponseJobInputsTimeSpanTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientCreateJobResponseJobInputsTypeDef = TypedDict(
    "ClientCreateJobResponseJobInputsTypeDef",
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

ClientCreateJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputAlbumArtArtworkTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputAlbumArtArtworkTypeDef",
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

ClientCreateJobResponseJobOutputAlbumArtTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientCreateJobResponseJobOutputAlbumArtArtworkTypeDef]},
    total=False,
)

ClientCreateJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientCreateJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobResponseJobOutputCaptionsTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobResponseJobOutputCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientCreateJobResponseJobOutputCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)

ClientCreateJobResponseJobOutputCompositionTimeSpanTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientCreateJobResponseJobOutputCompositionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputCompositionTypeDef",
    {"TimeSpan": ClientCreateJobResponseJobOutputCompositionTimeSpanTypeDef},
    total=False,
)

ClientCreateJobResponseJobOutputEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputThumbnailEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputWatermarksEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputWatermarksTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientCreateJobResponseJobOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobResponseJobOutputTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputTypeDef",
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

ClientCreateJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputsAlbumArtArtworkTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsAlbumArtArtworkTypeDef",
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

ClientCreateJobResponseJobOutputsAlbumArtTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientCreateJobResponseJobOutputsAlbumArtArtworkTypeDef]},
    total=False,
)

ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobResponseJobOutputsCaptionsTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientCreateJobResponseJobOutputsCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientCreateJobResponseJobOutputsCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)

ClientCreateJobResponseJobOutputsCompositionTimeSpanTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientCreateJobResponseJobOutputsCompositionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsCompositionTypeDef",
    {"TimeSpan": ClientCreateJobResponseJobOutputsCompositionTimeSpanTypeDef},
    total=False,
)

ClientCreateJobResponseJobOutputsEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputsThumbnailEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputsWatermarksEncryptionTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientCreateJobResponseJobOutputsWatermarksTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientCreateJobResponseJobOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)

ClientCreateJobResponseJobOutputsTypeDef = TypedDict(
    "ClientCreateJobResponseJobOutputsTypeDef",
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

ClientCreateJobResponseJobPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "ClientCreateJobResponseJobPlaylistsHlsContentProtectionTypeDef",
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

ClientCreateJobResponseJobPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "ClientCreateJobResponseJobPlaylistsPlayReadyDrmTypeDef",
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

ClientCreateJobResponseJobPlaylistsTypeDef = TypedDict(
    "ClientCreateJobResponseJobPlaylistsTypeDef",
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

ClientCreateJobResponseJobTimingTypeDef = TypedDict(
    "ClientCreateJobResponseJobTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)

ClientCreateJobResponseJobTypeDef = TypedDict(
    "ClientCreateJobResponseJobTypeDef",
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

ClientCreateJobResponseTypeDef = TypedDict(
    "ClientCreateJobResponseTypeDef", {"Job": ClientCreateJobResponseJobTypeDef}, total=False
)

ClientCreatePipelineContentConfigPermissionsTypeDef = TypedDict(
    "ClientCreatePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientCreatePipelineContentConfigTypeDef = TypedDict(
    "ClientCreatePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientCreatePipelineContentConfigPermissionsTypeDef],
    },
    total=False,
)

ClientCreatePipelineNotificationsTypeDef = TypedDict(
    "ClientCreatePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)

ClientCreatePipelineResponsePipelineContentConfigPermissionsTypeDef = TypedDict(
    "ClientCreatePipelineResponsePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientCreatePipelineResponsePipelineContentConfigTypeDef = TypedDict(
    "ClientCreatePipelineResponsePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientCreatePipelineResponsePipelineContentConfigPermissionsTypeDef],
    },
    total=False,
)

ClientCreatePipelineResponsePipelineNotificationsTypeDef = TypedDict(
    "ClientCreatePipelineResponsePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)

ClientCreatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "ClientCreatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientCreatePipelineResponsePipelineThumbnailConfigTypeDef = TypedDict(
    "ClientCreatePipelineResponsePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientCreatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)

ClientCreatePipelineResponsePipelineTypeDef = TypedDict(
    "ClientCreatePipelineResponsePipelineTypeDef",
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

ClientCreatePipelineResponseWarningsTypeDef = TypedDict(
    "ClientCreatePipelineResponseWarningsTypeDef", {"Code": str, "Message": str}, total=False
)

ClientCreatePipelineResponseTypeDef = TypedDict(
    "ClientCreatePipelineResponseTypeDef",
    {
        "Pipeline": ClientCreatePipelineResponsePipelineTypeDef,
        "Warnings": List[ClientCreatePipelineResponseWarningsTypeDef],
    },
    total=False,
)

ClientCreatePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "ClientCreatePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientCreatePipelineThumbnailConfigTypeDef = TypedDict(
    "ClientCreatePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientCreatePipelineThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)

ClientCreatePresetAudioCodecOptionsTypeDef = TypedDict(
    "ClientCreatePresetAudioCodecOptionsTypeDef",
    {"Profile": str, "BitDepth": str, "BitOrder": str, "Signed": str},
    total=False,
)

ClientCreatePresetAudioTypeDef = TypedDict(
    "ClientCreatePresetAudioTypeDef",
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

ClientCreatePresetResponsePresetAudioCodecOptionsTypeDef = TypedDict(
    "ClientCreatePresetResponsePresetAudioCodecOptionsTypeDef",
    {"Profile": str, "BitDepth": str, "BitOrder": str, "Signed": str},
    total=False,
)

ClientCreatePresetResponsePresetAudioTypeDef = TypedDict(
    "ClientCreatePresetResponsePresetAudioTypeDef",
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

ClientCreatePresetResponsePresetThumbnailsTypeDef = TypedDict(
    "ClientCreatePresetResponsePresetThumbnailsTypeDef",
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

ClientCreatePresetResponsePresetVideoWatermarksTypeDef = TypedDict(
    "ClientCreatePresetResponsePresetVideoWatermarksTypeDef",
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

ClientCreatePresetResponsePresetVideoTypeDef = TypedDict(
    "ClientCreatePresetResponsePresetVideoTypeDef",
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

ClientCreatePresetResponsePresetTypeDef = TypedDict(
    "ClientCreatePresetResponsePresetTypeDef",
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

ClientCreatePresetResponseTypeDef = TypedDict(
    "ClientCreatePresetResponseTypeDef",
    {"Preset": ClientCreatePresetResponsePresetTypeDef, "Warning": str},
    total=False,
)

ClientCreatePresetThumbnailsTypeDef = TypedDict(
    "ClientCreatePresetThumbnailsTypeDef",
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

ClientCreatePresetVideoWatermarksTypeDef = TypedDict(
    "ClientCreatePresetVideoWatermarksTypeDef",
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

ClientCreatePresetVideoTypeDef = TypedDict(
    "ClientCreatePresetVideoTypeDef",
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

ClientListJobsByPipelineResponseJobsInputDetectedPropertiesTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ClientListJobsByPipelineResponseJobsInputEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsInputInputCaptionsTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByPipelineResponseJobsInputInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsInputTimeSpanTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsInputTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputTypeDef",
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

ClientListJobsByPipelineResponseJobsInputsDetectedPropertiesTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ClientListJobsByPipelineResponseJobsInputsEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsInputsInputCaptionsTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByPipelineResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsInputsTimeSpanTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsInputsTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsInputsTypeDef",
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

ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkTypeDef",
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

ClientListJobsByPipelineResponseJobsOutputAlbumArtTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ClientListJobsByPipelineResponseJobsOutputAlbumArtArtworkTypeDef],
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputCaptionsTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputCaptionsTypeDef",
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

ClientListJobsByPipelineResponseJobsOutputCompositionTimeSpanTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputCompositionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputCompositionTypeDef",
    {"TimeSpan": ClientListJobsByPipelineResponseJobsOutputCompositionTimeSpanTypeDef},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputThumbnailEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputWatermarksEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputWatermarksTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputTypeDef",
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

ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkTypeDef",
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

ClientListJobsByPipelineResponseJobsOutputsAlbumArtTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ClientListJobsByPipelineResponseJobsOutputsAlbumArtArtworkTypeDef],
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsCaptionsTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsCaptionsTypeDef",
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

ClientListJobsByPipelineResponseJobsOutputsCompositionTimeSpanTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsCompositionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsCompositionTypeDef",
    {"TimeSpan": ClientListJobsByPipelineResponseJobsOutputsCompositionTimeSpanTypeDef},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsThumbnailEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsWatermarksEncryptionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsWatermarksTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientListJobsByPipelineResponseJobsOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByPipelineResponseJobsOutputsTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsOutputsTypeDef",
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

ClientListJobsByPipelineResponseJobsPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsPlaylistsHlsContentProtectionTypeDef",
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

ClientListJobsByPipelineResponseJobsPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsPlaylistsPlayReadyDrmTypeDef",
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

ClientListJobsByPipelineResponseJobsPlaylistsTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsPlaylistsTypeDef",
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

ClientListJobsByPipelineResponseJobsTimingTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)

ClientListJobsByPipelineResponseJobsTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseJobsTypeDef",
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

ClientListJobsByPipelineResponseTypeDef = TypedDict(
    "ClientListJobsByPipelineResponseTypeDef",
    {"Jobs": List[ClientListJobsByPipelineResponseJobsTypeDef], "NextPageToken": str},
    total=False,
)

ClientListJobsByStatusResponseJobsInputDetectedPropertiesTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ClientListJobsByStatusResponseJobsInputEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByStatusResponseJobsInputInputCaptionsTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByStatusResponseJobsInputInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)

ClientListJobsByStatusResponseJobsInputTimeSpanTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientListJobsByStatusResponseJobsInputTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputTypeDef",
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

ClientListJobsByStatusResponseJobsInputsDetectedPropertiesTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ClientListJobsByStatusResponseJobsInputsEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByStatusResponseJobsInputsInputCaptionsTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ClientListJobsByStatusResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)

ClientListJobsByStatusResponseJobsInputsTimeSpanTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientListJobsByStatusResponseJobsInputsTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsInputsTypeDef",
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

ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkTypeDef",
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

ClientListJobsByStatusResponseJobsOutputAlbumArtTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ClientListJobsByStatusResponseJobsOutputAlbumArtArtworkTypeDef],
    },
    total=False,
)

ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByStatusResponseJobsOutputCaptionsTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputCaptionsTypeDef",
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

ClientListJobsByStatusResponseJobsOutputCompositionTimeSpanTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputCompositionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputCompositionTypeDef",
    {"TimeSpan": ClientListJobsByStatusResponseJobsOutputCompositionTimeSpanTypeDef},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputThumbnailEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputWatermarksEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputWatermarksTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByStatusResponseJobsOutputTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputTypeDef",
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

ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkTypeDef",
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

ClientListJobsByStatusResponseJobsOutputsAlbumArtTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ClientListJobsByStatusResponseJobsOutputsAlbumArtArtworkTypeDef],
    },
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsCaptionsTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsCaptionsTypeDef",
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

ClientListJobsByStatusResponseJobsOutputsCompositionTimeSpanTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsCompositionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsCompositionTypeDef",
    {"TimeSpan": ClientListJobsByStatusResponseJobsOutputsCompositionTimeSpanTypeDef},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsThumbnailEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsWatermarksEncryptionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsWatermarksTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientListJobsByStatusResponseJobsOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)

ClientListJobsByStatusResponseJobsOutputsTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsOutputsTypeDef",
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

ClientListJobsByStatusResponseJobsPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsPlaylistsHlsContentProtectionTypeDef",
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

ClientListJobsByStatusResponseJobsPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsPlaylistsPlayReadyDrmTypeDef",
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

ClientListJobsByStatusResponseJobsPlaylistsTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsPlaylistsTypeDef",
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

ClientListJobsByStatusResponseJobsTimingTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)

ClientListJobsByStatusResponseJobsTypeDef = TypedDict(
    "ClientListJobsByStatusResponseJobsTypeDef",
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

ClientListJobsByStatusResponseTypeDef = TypedDict(
    "ClientListJobsByStatusResponseTypeDef",
    {"Jobs": List[ClientListJobsByStatusResponseJobsTypeDef], "NextPageToken": str},
    total=False,
)

ClientListPipelinesResponsePipelinesContentConfigPermissionsTypeDef = TypedDict(
    "ClientListPipelinesResponsePipelinesContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientListPipelinesResponsePipelinesContentConfigTypeDef = TypedDict(
    "ClientListPipelinesResponsePipelinesContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientListPipelinesResponsePipelinesContentConfigPermissionsTypeDef],
    },
    total=False,
)

ClientListPipelinesResponsePipelinesNotificationsTypeDef = TypedDict(
    "ClientListPipelinesResponsePipelinesNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)

ClientListPipelinesResponsePipelinesThumbnailConfigPermissionsTypeDef = TypedDict(
    "ClientListPipelinesResponsePipelinesThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientListPipelinesResponsePipelinesThumbnailConfigTypeDef = TypedDict(
    "ClientListPipelinesResponsePipelinesThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientListPipelinesResponsePipelinesThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)

ClientListPipelinesResponsePipelinesTypeDef = TypedDict(
    "ClientListPipelinesResponsePipelinesTypeDef",
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

ClientListPipelinesResponseTypeDef = TypedDict(
    "ClientListPipelinesResponseTypeDef",
    {"Pipelines": List[ClientListPipelinesResponsePipelinesTypeDef], "NextPageToken": str},
    total=False,
)

ClientListPresetsResponsePresetsAudioCodecOptionsTypeDef = TypedDict(
    "ClientListPresetsResponsePresetsAudioCodecOptionsTypeDef",
    {"Profile": str, "BitDepth": str, "BitOrder": str, "Signed": str},
    total=False,
)

ClientListPresetsResponsePresetsAudioTypeDef = TypedDict(
    "ClientListPresetsResponsePresetsAudioTypeDef",
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

ClientListPresetsResponsePresetsThumbnailsTypeDef = TypedDict(
    "ClientListPresetsResponsePresetsThumbnailsTypeDef",
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

ClientListPresetsResponsePresetsVideoWatermarksTypeDef = TypedDict(
    "ClientListPresetsResponsePresetsVideoWatermarksTypeDef",
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

ClientListPresetsResponsePresetsVideoTypeDef = TypedDict(
    "ClientListPresetsResponsePresetsVideoTypeDef",
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

ClientListPresetsResponsePresetsTypeDef = TypedDict(
    "ClientListPresetsResponsePresetsTypeDef",
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

ClientListPresetsResponseTypeDef = TypedDict(
    "ClientListPresetsResponseTypeDef",
    {"Presets": List[ClientListPresetsResponsePresetsTypeDef], "NextPageToken": str},
    total=False,
)

ClientReadJobResponseJobInputDetectedPropertiesTypeDef = TypedDict(
    "ClientReadJobResponseJobInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ClientReadJobResponseJobInputEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientReadJobResponseJobInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientReadJobResponseJobInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientReadJobResponseJobInputInputCaptionsTypeDef = TypedDict(
    "ClientReadJobResponseJobInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientReadJobResponseJobInputInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)

ClientReadJobResponseJobInputTimeSpanTypeDef = TypedDict(
    "ClientReadJobResponseJobInputTimeSpanTypeDef", {"StartTime": str, "Duration": str}, total=False
)

ClientReadJobResponseJobInputTypeDef = TypedDict(
    "ClientReadJobResponseJobInputTypeDef",
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

ClientReadJobResponseJobInputsDetectedPropertiesTypeDef = TypedDict(
    "ClientReadJobResponseJobInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ClientReadJobResponseJobInputsEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientReadJobResponseJobInputsInputCaptionsTypeDef = TypedDict(
    "ClientReadJobResponseJobInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientReadJobResponseJobInputsInputCaptionsCaptionSourcesTypeDef],
    },
    total=False,
)

ClientReadJobResponseJobInputsTimeSpanTypeDef = TypedDict(
    "ClientReadJobResponseJobInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientReadJobResponseJobInputsTypeDef = TypedDict(
    "ClientReadJobResponseJobInputsTypeDef",
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

ClientReadJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputAlbumArtArtworkTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputAlbumArtArtworkTypeDef",
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

ClientReadJobResponseJobOutputAlbumArtTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientReadJobResponseJobOutputAlbumArtArtworkTypeDef]},
    total=False,
)

ClientReadJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientReadJobResponseJobOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ClientReadJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientReadJobResponseJobOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientReadJobResponseJobOutputCaptionsTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientReadJobResponseJobOutputCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientReadJobResponseJobOutputCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)

ClientReadJobResponseJobOutputCompositionTimeSpanTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientReadJobResponseJobOutputCompositionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputCompositionTypeDef",
    {"TimeSpan": ClientReadJobResponseJobOutputCompositionTimeSpanTypeDef},
    total=False,
)

ClientReadJobResponseJobOutputEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputThumbnailEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputWatermarksEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputWatermarksTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientReadJobResponseJobOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)

ClientReadJobResponseJobOutputTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputTypeDef",
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

ClientReadJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputsAlbumArtArtworkTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsAlbumArtArtworkTypeDef",
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

ClientReadJobResponseJobOutputsAlbumArtTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsAlbumArtTypeDef",
    {"MergePolicy": str, "Artwork": List[ClientReadJobResponseJobOutputsAlbumArtArtworkTypeDef]},
    total=False,
)

ClientReadJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ClientReadJobResponseJobOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ClientReadJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ClientReadJobResponseJobOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ClientReadJobResponseJobOutputsCaptionsTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[ClientReadJobResponseJobOutputsCaptionsCaptionSourcesTypeDef],
        "CaptionFormats": List[ClientReadJobResponseJobOutputsCaptionsCaptionFormatsTypeDef],
    },
    total=False,
)

ClientReadJobResponseJobOutputsCompositionTimeSpanTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ClientReadJobResponseJobOutputsCompositionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsCompositionTypeDef",
    {"TimeSpan": ClientReadJobResponseJobOutputsCompositionTimeSpanTypeDef},
    total=False,
)

ClientReadJobResponseJobOutputsEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputsThumbnailEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputsWatermarksEncryptionTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ClientReadJobResponseJobOutputsWatermarksTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ClientReadJobResponseJobOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)

ClientReadJobResponseJobOutputsTypeDef = TypedDict(
    "ClientReadJobResponseJobOutputsTypeDef",
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

ClientReadJobResponseJobPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "ClientReadJobResponseJobPlaylistsHlsContentProtectionTypeDef",
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

ClientReadJobResponseJobPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "ClientReadJobResponseJobPlaylistsPlayReadyDrmTypeDef",
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

ClientReadJobResponseJobPlaylistsTypeDef = TypedDict(
    "ClientReadJobResponseJobPlaylistsTypeDef",
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

ClientReadJobResponseJobTimingTypeDef = TypedDict(
    "ClientReadJobResponseJobTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)

ClientReadJobResponseJobTypeDef = TypedDict(
    "ClientReadJobResponseJobTypeDef",
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

ClientReadJobResponseTypeDef = TypedDict(
    "ClientReadJobResponseTypeDef", {"Job": ClientReadJobResponseJobTypeDef}, total=False
)

ClientReadPipelineResponsePipelineContentConfigPermissionsTypeDef = TypedDict(
    "ClientReadPipelineResponsePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientReadPipelineResponsePipelineContentConfigTypeDef = TypedDict(
    "ClientReadPipelineResponsePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientReadPipelineResponsePipelineContentConfigPermissionsTypeDef],
    },
    total=False,
)

ClientReadPipelineResponsePipelineNotificationsTypeDef = TypedDict(
    "ClientReadPipelineResponsePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)

ClientReadPipelineResponsePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "ClientReadPipelineResponsePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientReadPipelineResponsePipelineThumbnailConfigTypeDef = TypedDict(
    "ClientReadPipelineResponsePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientReadPipelineResponsePipelineThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)

ClientReadPipelineResponsePipelineTypeDef = TypedDict(
    "ClientReadPipelineResponsePipelineTypeDef",
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

ClientReadPipelineResponseWarningsTypeDef = TypedDict(
    "ClientReadPipelineResponseWarningsTypeDef", {"Code": str, "Message": str}, total=False
)

ClientReadPipelineResponseTypeDef = TypedDict(
    "ClientReadPipelineResponseTypeDef",
    {
        "Pipeline": ClientReadPipelineResponsePipelineTypeDef,
        "Warnings": List[ClientReadPipelineResponseWarningsTypeDef],
    },
    total=False,
)

ClientReadPresetResponsePresetAudioCodecOptionsTypeDef = TypedDict(
    "ClientReadPresetResponsePresetAudioCodecOptionsTypeDef",
    {"Profile": str, "BitDepth": str, "BitOrder": str, "Signed": str},
    total=False,
)

ClientReadPresetResponsePresetAudioTypeDef = TypedDict(
    "ClientReadPresetResponsePresetAudioTypeDef",
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

ClientReadPresetResponsePresetThumbnailsTypeDef = TypedDict(
    "ClientReadPresetResponsePresetThumbnailsTypeDef",
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

ClientReadPresetResponsePresetVideoWatermarksTypeDef = TypedDict(
    "ClientReadPresetResponsePresetVideoWatermarksTypeDef",
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

ClientReadPresetResponsePresetVideoTypeDef = TypedDict(
    "ClientReadPresetResponsePresetVideoTypeDef",
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

ClientReadPresetResponsePresetTypeDef = TypedDict(
    "ClientReadPresetResponsePresetTypeDef",
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

ClientReadPresetResponseTypeDef = TypedDict(
    "ClientReadPresetResponseTypeDef",
    {"Preset": ClientReadPresetResponsePresetTypeDef},
    total=False,
)

ClientTestRoleResponseTypeDef = TypedDict(
    "ClientTestRoleResponseTypeDef", {"Success": str, "Messages": List[str]}, total=False
)

ClientUpdatePipelineContentConfigPermissionsTypeDef = TypedDict(
    "ClientUpdatePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientUpdatePipelineContentConfigTypeDef = TypedDict(
    "ClientUpdatePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientUpdatePipelineContentConfigPermissionsTypeDef],
    },
    total=False,
)

ClientUpdatePipelineNotificationsNotificationsTypeDef = TypedDict(
    "ClientUpdatePipelineNotificationsNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)

ClientUpdatePipelineNotificationsResponsePipelineContentConfigPermissionsTypeDef = TypedDict(
    "ClientUpdatePipelineNotificationsResponsePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientUpdatePipelineNotificationsResponsePipelineContentConfigTypeDef = TypedDict(
    "ClientUpdatePipelineNotificationsResponsePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[
            ClientUpdatePipelineNotificationsResponsePipelineContentConfigPermissionsTypeDef
        ],
    },
    total=False,
)

ClientUpdatePipelineNotificationsResponsePipelineNotificationsTypeDef = TypedDict(
    "ClientUpdatePipelineNotificationsResponsePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)

ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigTypeDef = TypedDict(
    "ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[
            ClientUpdatePipelineNotificationsResponsePipelineThumbnailConfigPermissionsTypeDef
        ],
    },
    total=False,
)

ClientUpdatePipelineNotificationsResponsePipelineTypeDef = TypedDict(
    "ClientUpdatePipelineNotificationsResponsePipelineTypeDef",
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

ClientUpdatePipelineNotificationsResponseTypeDef = TypedDict(
    "ClientUpdatePipelineNotificationsResponseTypeDef",
    {"Pipeline": ClientUpdatePipelineNotificationsResponsePipelineTypeDef},
    total=False,
)

ClientUpdatePipelineNotificationsTypeDef = TypedDict(
    "ClientUpdatePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)

ClientUpdatePipelineResponsePipelineContentConfigPermissionsTypeDef = TypedDict(
    "ClientUpdatePipelineResponsePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientUpdatePipelineResponsePipelineContentConfigTypeDef = TypedDict(
    "ClientUpdatePipelineResponsePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientUpdatePipelineResponsePipelineContentConfigPermissionsTypeDef],
    },
    total=False,
)

ClientUpdatePipelineResponsePipelineNotificationsTypeDef = TypedDict(
    "ClientUpdatePipelineResponsePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)

ClientUpdatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "ClientUpdatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientUpdatePipelineResponsePipelineThumbnailConfigTypeDef = TypedDict(
    "ClientUpdatePipelineResponsePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientUpdatePipelineResponsePipelineThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)

ClientUpdatePipelineResponsePipelineTypeDef = TypedDict(
    "ClientUpdatePipelineResponsePipelineTypeDef",
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

ClientUpdatePipelineResponseWarningsTypeDef = TypedDict(
    "ClientUpdatePipelineResponseWarningsTypeDef", {"Code": str, "Message": str}, total=False
)

ClientUpdatePipelineResponseTypeDef = TypedDict(
    "ClientUpdatePipelineResponseTypeDef",
    {
        "Pipeline": ClientUpdatePipelineResponsePipelineTypeDef,
        "Warnings": List[ClientUpdatePipelineResponseWarningsTypeDef],
    },
    total=False,
)

ClientUpdatePipelineStatusResponsePipelineContentConfigPermissionsTypeDef = TypedDict(
    "ClientUpdatePipelineStatusResponsePipelineContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientUpdatePipelineStatusResponsePipelineContentConfigTypeDef = TypedDict(
    "ClientUpdatePipelineStatusResponsePipelineContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[
            ClientUpdatePipelineStatusResponsePipelineContentConfigPermissionsTypeDef
        ],
    },
    total=False,
)

ClientUpdatePipelineStatusResponsePipelineNotificationsTypeDef = TypedDict(
    "ClientUpdatePipelineStatusResponsePipelineNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)

ClientUpdatePipelineStatusResponsePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "ClientUpdatePipelineStatusResponsePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientUpdatePipelineStatusResponsePipelineThumbnailConfigTypeDef = TypedDict(
    "ClientUpdatePipelineStatusResponsePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[
            ClientUpdatePipelineStatusResponsePipelineThumbnailConfigPermissionsTypeDef
        ],
    },
    total=False,
)

ClientUpdatePipelineStatusResponsePipelineTypeDef = TypedDict(
    "ClientUpdatePipelineStatusResponsePipelineTypeDef",
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

ClientUpdatePipelineStatusResponseTypeDef = TypedDict(
    "ClientUpdatePipelineStatusResponseTypeDef",
    {"Pipeline": ClientUpdatePipelineStatusResponsePipelineTypeDef},
    total=False,
)

ClientUpdatePipelineThumbnailConfigPermissionsTypeDef = TypedDict(
    "ClientUpdatePipelineThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ClientUpdatePipelineThumbnailConfigTypeDef = TypedDict(
    "ClientUpdatePipelineThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ClientUpdatePipelineThumbnailConfigPermissionsTypeDef],
    },
    total=False,
)

JobCompleteWaitWaiterConfigTypeDef = TypedDict(
    "JobCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

ListJobsByPipelinePaginatePaginationConfigTypeDef = TypedDict(
    "ListJobsByPipelinePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputDetectedPropertiesTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputInputCaptionsTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByPipelinePaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputTimeSpanTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputTypeDef",
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

ListJobsByPipelinePaginateResponseJobsInputsDetectedPropertiesTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputsEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByPipelinePaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputsTimeSpanTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsInputsTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsInputsTypeDef",
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

ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkTypeDef",
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

ListJobsByPipelinePaginateResponseJobsOutputAlbumArtTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ListJobsByPipelinePaginateResponseJobsOutputAlbumArtArtworkTypeDef],
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputCaptionsTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputCaptionsTypeDef",
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

ListJobsByPipelinePaginateResponseJobsOutputCompositionTimeSpanTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputCompositionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputCompositionTypeDef",
    {"TimeSpan": ListJobsByPipelinePaginateResponseJobsOutputCompositionTimeSpanTypeDef},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputThumbnailEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputWatermarksEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputWatermarksTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputTypeDef",
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

ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkTypeDef",
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

ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ListJobsByPipelinePaginateResponseJobsOutputsAlbumArtArtworkTypeDef],
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsCaptionsTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsCaptionsTypeDef",
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

ListJobsByPipelinePaginateResponseJobsOutputsCompositionTimeSpanTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsCompositionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsCompositionTypeDef",
    {"TimeSpan": ListJobsByPipelinePaginateResponseJobsOutputsCompositionTimeSpanTypeDef},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsThumbnailEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsWatermarksEncryptionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsWatermarksTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ListJobsByPipelinePaginateResponseJobsOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)

ListJobsByPipelinePaginateResponseJobsOutputsTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsOutputsTypeDef",
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

ListJobsByPipelinePaginateResponseJobsPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsPlaylistsHlsContentProtectionTypeDef",
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

ListJobsByPipelinePaginateResponseJobsPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsPlaylistsPlayReadyDrmTypeDef",
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

ListJobsByPipelinePaginateResponseJobsPlaylistsTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsPlaylistsTypeDef",
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

ListJobsByPipelinePaginateResponseJobsTimingTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)

ListJobsByPipelinePaginateResponseJobsTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseJobsTypeDef",
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

ListJobsByPipelinePaginateResponseTypeDef = TypedDict(
    "ListJobsByPipelinePaginateResponseTypeDef",
    {"Jobs": List[ListJobsByPipelinePaginateResponseJobsTypeDef], "NextToken": str},
    total=False,
)

ListJobsByStatusPaginatePaginationConfigTypeDef = TypedDict(
    "ListJobsByStatusPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputDetectedPropertiesTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputInputCaptionsTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByStatusPaginateResponseJobsInputInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputTimeSpanTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputTypeDef",
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

ListJobsByStatusPaginateResponseJobsInputsDetectedPropertiesTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputsDetectedPropertiesTypeDef",
    {"Width": int, "Height": int, "FrameRate": str, "FileSize": int, "DurationMillis": int},
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputsEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputsInputCaptionsTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputsInputCaptionsTypeDef",
    {
        "MergePolicy": str,
        "CaptionSources": List[
            ListJobsByStatusPaginateResponseJobsInputsInputCaptionsCaptionSourcesTypeDef
        ],
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputsTimeSpanTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputsTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsInputsTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsInputsTypeDef",
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

ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkTypeDef",
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

ListJobsByStatusPaginateResponseJobsOutputAlbumArtTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ListJobsByStatusPaginateResponseJobsOutputAlbumArtArtworkTypeDef],
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputCaptionsTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputCaptionsTypeDef",
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

ListJobsByStatusPaginateResponseJobsOutputCompositionTimeSpanTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputCompositionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputCompositionTypeDef",
    {"TimeSpan": ListJobsByStatusPaginateResponseJobsOutputCompositionTimeSpanTypeDef},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputThumbnailEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputWatermarksEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputWatermarksTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputWatermarksEncryptionTypeDef,
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputTypeDef",
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

ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkTypeDef",
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

ListJobsByStatusPaginateResponseJobsOutputsAlbumArtTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsAlbumArtTypeDef",
    {
        "MergePolicy": str,
        "Artwork": List[ListJobsByStatusPaginateResponseJobsOutputsAlbumArtArtworkTypeDef],
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsTypeDef",
    {
        "Format": str,
        "Pattern": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionFormatsEncryptionTypeDef,
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesTypeDef",
    {
        "Key": str,
        "Language": str,
        "TimeOffset": str,
        "Label": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputsCaptionsCaptionSourcesEncryptionTypeDef,
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsCaptionsTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsCaptionsTypeDef",
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

ListJobsByStatusPaginateResponseJobsOutputsCompositionTimeSpanTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsCompositionTimeSpanTypeDef",
    {"StartTime": str, "Duration": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsCompositionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsCompositionTypeDef",
    {"TimeSpan": ListJobsByStatusPaginateResponseJobsOutputsCompositionTimeSpanTypeDef},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsThumbnailEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsThumbnailEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsWatermarksEncryptionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsWatermarksEncryptionTypeDef",
    {"Mode": str, "Key": str, "KeyMd5": str, "InitializationVector": str},
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsWatermarksTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsWatermarksTypeDef",
    {
        "PresetWatermarkId": str,
        "InputKey": str,
        "Encryption": ListJobsByStatusPaginateResponseJobsOutputsWatermarksEncryptionTypeDef,
    },
    total=False,
)

ListJobsByStatusPaginateResponseJobsOutputsTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsOutputsTypeDef",
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

ListJobsByStatusPaginateResponseJobsPlaylistsHlsContentProtectionTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsPlaylistsHlsContentProtectionTypeDef",
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

ListJobsByStatusPaginateResponseJobsPlaylistsPlayReadyDrmTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsPlaylistsPlayReadyDrmTypeDef",
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

ListJobsByStatusPaginateResponseJobsPlaylistsTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsPlaylistsTypeDef",
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

ListJobsByStatusPaginateResponseJobsTimingTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsTimingTypeDef",
    {"SubmitTimeMillis": int, "StartTimeMillis": int, "FinishTimeMillis": int},
    total=False,
)

ListJobsByStatusPaginateResponseJobsTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseJobsTypeDef",
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

ListJobsByStatusPaginateResponseTypeDef = TypedDict(
    "ListJobsByStatusPaginateResponseTypeDef",
    {"Jobs": List[ListJobsByStatusPaginateResponseJobsTypeDef], "NextToken": str},
    total=False,
)

ListPipelinesPaginatePaginationConfigTypeDef = TypedDict(
    "ListPipelinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListPipelinesPaginateResponsePipelinesContentConfigPermissionsTypeDef = TypedDict(
    "ListPipelinesPaginateResponsePipelinesContentConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ListPipelinesPaginateResponsePipelinesContentConfigTypeDef = TypedDict(
    "ListPipelinesPaginateResponsePipelinesContentConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[ListPipelinesPaginateResponsePipelinesContentConfigPermissionsTypeDef],
    },
    total=False,
)

ListPipelinesPaginateResponsePipelinesNotificationsTypeDef = TypedDict(
    "ListPipelinesPaginateResponsePipelinesNotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)

ListPipelinesPaginateResponsePipelinesThumbnailConfigPermissionsTypeDef = TypedDict(
    "ListPipelinesPaginateResponsePipelinesThumbnailConfigPermissionsTypeDef",
    {"GranteeType": str, "Grantee": str, "Access": List[str]},
    total=False,
)

ListPipelinesPaginateResponsePipelinesThumbnailConfigTypeDef = TypedDict(
    "ListPipelinesPaginateResponsePipelinesThumbnailConfigTypeDef",
    {
        "Bucket": str,
        "StorageClass": str,
        "Permissions": List[
            ListPipelinesPaginateResponsePipelinesThumbnailConfigPermissionsTypeDef
        ],
    },
    total=False,
)

ListPipelinesPaginateResponsePipelinesTypeDef = TypedDict(
    "ListPipelinesPaginateResponsePipelinesTypeDef",
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

ListPipelinesPaginateResponseTypeDef = TypedDict(
    "ListPipelinesPaginateResponseTypeDef",
    {"Pipelines": List[ListPipelinesPaginateResponsePipelinesTypeDef], "NextToken": str},
    total=False,
)

ListPresetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPresetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

ListPresetsPaginateResponsePresetsAudioCodecOptionsTypeDef = TypedDict(
    "ListPresetsPaginateResponsePresetsAudioCodecOptionsTypeDef",
    {"Profile": str, "BitDepth": str, "BitOrder": str, "Signed": str},
    total=False,
)

ListPresetsPaginateResponsePresetsAudioTypeDef = TypedDict(
    "ListPresetsPaginateResponsePresetsAudioTypeDef",
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

ListPresetsPaginateResponsePresetsThumbnailsTypeDef = TypedDict(
    "ListPresetsPaginateResponsePresetsThumbnailsTypeDef",
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

ListPresetsPaginateResponsePresetsVideoWatermarksTypeDef = TypedDict(
    "ListPresetsPaginateResponsePresetsVideoWatermarksTypeDef",
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

ListPresetsPaginateResponsePresetsVideoTypeDef = TypedDict(
    "ListPresetsPaginateResponsePresetsVideoTypeDef",
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

ListPresetsPaginateResponsePresetsTypeDef = TypedDict(
    "ListPresetsPaginateResponsePresetsTypeDef",
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

ListPresetsPaginateResponseTypeDef = TypedDict(
    "ListPresetsPaginateResponseTypeDef",
    {"Presets": List[ListPresetsPaginateResponsePresetsTypeDef], "NextToken": str},
    total=False,
)
