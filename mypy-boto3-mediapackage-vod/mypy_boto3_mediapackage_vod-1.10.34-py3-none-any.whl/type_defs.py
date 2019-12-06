"Main interface for mediapackage-vod service type defs"
from __future__ import annotations

import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateAssetResponseEgressEndpointsTypeDef = TypedDict(
    "ClientCreateAssetResponseEgressEndpointsTypeDef",
    {"PackagingConfigurationId": str, "Url": str},
    total=False,
)

ClientCreateAssetResponseTypeDef = TypedDict(
    "ClientCreateAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List[ClientCreateAssetResponseEgressEndpointsTypeDef],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)

_RequiredClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef,
):
    pass


ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
)

ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationCmafPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationCmafPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

_RequiredClientCreatePackagingConfigurationDashPackageTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationDashPackageTypeDef",
    {"DashManifests": List[ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef]},
)
_OptionalClientCreatePackagingConfigurationDashPackageTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationDashPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationDashPackageTypeDef(
    _RequiredClientCreatePackagingConfigurationDashPackageTypeDef,
    _OptionalClientCreatePackagingConfigurationDashPackageTypeDef,
):
    pass


_RequiredClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef,
):
    pass


_RequiredClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef
    },
)
_OptionalClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef",
    {"ConstantInitializationVector": str, "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"]},
    total=False,
)


class ClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef(
    _RequiredClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef,
    _OptionalClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef,
):
    pass


ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationHlsPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationHlsPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef,
        "HlsManifests": List[ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

_RequiredClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef,
):
    pass


ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef
    },
)

ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationMssPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationMssPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef,
        "MssManifests": List[ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseCmafPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseCmafPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseDashPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseDashPackageTypeDef",
    {
        "DashManifests": List[
            ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef
        ],
        "Encryption": ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseHlsPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseHlsPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseMssPackageTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseMssPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientCreatePackagingConfigurationResponseTypeDef = TypedDict(
    "ClientCreatePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": ClientCreatePackagingConfigurationResponseCmafPackageTypeDef,
        "DashPackage": ClientCreatePackagingConfigurationResponseDashPackageTypeDef,
        "HlsPackage": ClientCreatePackagingConfigurationResponseHlsPackageTypeDef,
        "Id": str,
        "MssPackage": ClientCreatePackagingConfigurationResponseMssPackageTypeDef,
        "PackagingGroupId": str,
    },
    total=False,
)

ClientCreatePackagingGroupResponseTypeDef = TypedDict(
    "ClientCreatePackagingGroupResponseTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)

ClientDescribeAssetResponseEgressEndpointsTypeDef = TypedDict(
    "ClientDescribeAssetResponseEgressEndpointsTypeDef",
    {"PackagingConfigurationId": str, "Url": str},
    total=False,
)

ClientDescribeAssetResponseTypeDef = TypedDict(
    "ClientDescribeAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List[ClientDescribeAssetResponseEgressEndpointsTypeDef],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseCmafPackageTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseCmafPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseDashPackageTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseDashPackageTypeDef",
    {
        "DashManifests": List[
            ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef
        ],
        "Encryption": ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseHlsPackageTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseHlsPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseMssPackageTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseMssPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientDescribePackagingConfigurationResponseTypeDef = TypedDict(
    "ClientDescribePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": ClientDescribePackagingConfigurationResponseCmafPackageTypeDef,
        "DashPackage": ClientDescribePackagingConfigurationResponseDashPackageTypeDef,
        "HlsPackage": ClientDescribePackagingConfigurationResponseHlsPackageTypeDef,
        "Id": str,
        "MssPackage": ClientDescribePackagingConfigurationResponseMssPackageTypeDef,
        "PackagingGroupId": str,
    },
    total=False,
)

ClientDescribePackagingGroupResponseTypeDef = TypedDict(
    "ClientDescribePackagingGroupResponseTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)

ClientListAssetsResponseAssetsTypeDef = TypedDict(
    "ClientListAssetsResponseAssetsTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)

ClientListAssetsResponseTypeDef = TypedDict(
    "ClientListAssetsResponseTypeDef",
    {"Assets": List[ClientListAssetsResponseAssetsTypeDef], "NextToken": str},
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef",
    {
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef",
    {
        "DashManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef
        ],
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef",
    {
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef",
    {
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef",
    {
        "Arn": str,
        "CmafPackage": ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef,
        "DashPackage": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef,
        "HlsPackage": ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef,
        "Id": str,
        "MssPackage": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef,
        "PackagingGroupId": str,
    },
    total=False,
)

ClientListPackagingConfigurationsResponseTypeDef = TypedDict(
    "ClientListPackagingConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingConfigurations": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef
        ],
    },
    total=False,
)

ClientListPackagingGroupsResponsePackagingGroupsTypeDef = TypedDict(
    "ClientListPackagingGroupsResponsePackagingGroupsTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)

ClientListPackagingGroupsResponseTypeDef = TypedDict(
    "ClientListPackagingGroupsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingGroups": List[ClientListPackagingGroupsResponsePackagingGroupsTypeDef],
    },
    total=False,
)

ListAssetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAssetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAssetsPaginateResponseAssetsTypeDef = TypedDict(
    "ListAssetsPaginateResponseAssetsTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
    total=False,
)

ListAssetsPaginateResponseTypeDef = TypedDict(
    "ListAssetsPaginateResponseTypeDef",
    {"Assets": List[ListAssetsPaginateResponseAssetsTypeDef]},
    total=False,
)

ListPackagingConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageTypeDef",
    {
        "Encryption": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageTypeDef",
    {
        "DashManifests": List[
            ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsTypeDef
        ],
        "Encryption": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageTypeDef",
    {
        "Encryption": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionTypeDef,
        "HlsManifests": List[
            ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageTypeDef",
    {
        "Encryption": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponsePackagingConfigurationsTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsTypeDef",
    {
        "Arn": str,
        "CmafPackage": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageTypeDef,
        "DashPackage": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageTypeDef,
        "HlsPackage": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageTypeDef,
        "Id": str,
        "MssPackage": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageTypeDef,
        "PackagingGroupId": str,
    },
    total=False,
)

ListPackagingConfigurationsPaginateResponseTypeDef = TypedDict(
    "ListPackagingConfigurationsPaginateResponseTypeDef",
    {
        "PackagingConfigurations": List[
            ListPackagingConfigurationsPaginateResponsePackagingConfigurationsTypeDef
        ]
    },
    total=False,
)

ListPackagingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPackagingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef = TypedDict(
    "ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)

ListPackagingGroupsPaginateResponseTypeDef = TypedDict(
    "ListPackagingGroupsPaginateResponseTypeDef",
    {"PackagingGroups": List[ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef]},
    total=False,
)
