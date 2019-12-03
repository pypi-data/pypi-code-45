"Main interface for mediapackage-vod service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateAssetResponseEgressEndpointsTypeDef",
    "ClientCreateAssetResponseTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationCmafPackageTypeDef",
    "ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef",
    "ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationDashPackageTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationHlsPackageTypeDef",
    "ClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef",
    "ClientCreatePackagingConfigurationMssPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseCmafPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseDashPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseHlsPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    "ClientCreatePackagingConfigurationResponseMssPackageTypeDef",
    "ClientCreatePackagingConfigurationResponseTypeDef",
    "ClientCreatePackagingGroupResponseTypeDef",
    "ClientDescribeAssetResponseEgressEndpointsTypeDef",
    "ClientDescribeAssetResponseTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseCmafPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseDashPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseHlsPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    "ClientDescribePackagingConfigurationResponseMssPackageTypeDef",
    "ClientDescribePackagingConfigurationResponseTypeDef",
    "ClientDescribePackagingGroupResponseTypeDef",
    "ClientListAssetsResponseAssetsTypeDef",
    "ClientListAssetsResponseTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef",
    "ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef",
    "ClientListPackagingConfigurationsResponseTypeDef",
    "ClientListPackagingGroupsResponsePackagingGroupsTypeDef",
    "ClientListPackagingGroupsResponseTypeDef",
    "ListAssetsPaginatePaginationConfigTypeDef",
    "ListAssetsPaginateResponseAssetsTypeDef",
    "ListAssetsPaginateResponseTypeDef",
    "ListPackagingConfigurationsPaginatePaginationConfigTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageTypeDef",
    "ListPackagingConfigurationsPaginateResponsePackagingConfigurationsTypeDef",
    "ListPackagingConfigurationsPaginateResponseTypeDef",
    "ListPackagingGroupsPaginatePaginationConfigTypeDef",
    "ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef",
    "ListPackagingGroupsPaginateResponseTypeDef",
)


_ClientCreateAssetResponseEgressEndpointsTypeDef = TypedDict(
    "_ClientCreateAssetResponseEgressEndpointsTypeDef",
    {"PackagingConfigurationId": str, "Url": str},
    total=False,
)


class ClientCreateAssetResponseEgressEndpointsTypeDef(
    _ClientCreateAssetResponseEgressEndpointsTypeDef
):
    """
    - *(dict) --*The endpoint URL used to access an Asset using one PackagingConfiguration.

      - **PackagingConfigurationId** *(string) --*The ID of the PackagingConfiguration being applied
      to the Asset.
      - **Url** *(string) --*The URL of the parent manifest for the repackaged Asset.
    """


_ClientCreateAssetResponseTypeDef = TypedDict(
    "_ClientCreateAssetResponseTypeDef",
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


class ClientCreateAssetResponseTypeDef(_ClientCreateAssetResponseTypeDef):
    """
    - *(dict) --*The new MediaPackage VOD Asset resource.

      - **Arn** *(string) --*The ARN of the Asset.
      - **CreatedAt** *(string) --*The time the Asset was initially submitted for Ingest.
      - **EgressEndpoints** *(list) --*The list of egress endpoints available for the Asset.

        - *(dict) --*The endpoint URL used to access an Asset using one PackagingConfiguration.

          - **PackagingConfigurationId** *(string) --*The ID of the PackagingConfiguration being
          applied to the Asset.
          - **Url** *(string) --*The URL of the parent manifest for the repackaged Asset.
    """


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
    """
    - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
    Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
      AWS Elemental MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

        - *(string) --*
    """


_ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
)


class ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A CMAF encryption configuration.

      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationCmafPackageHlsManifestsStreamSelectionTypeDef
):
    pass


_ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef",
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


class ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef(
    _ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef
):
    pass


_ClientCreatePackagingConfigurationCmafPackageTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationCmafPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientCreatePackagingConfigurationCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationCmafPackageTypeDef(
    _ClientCreatePackagingConfigurationCmafPackageTypeDef
):
    """
    - **Encryption** *(dict) --*A CMAF encryption configuration.

      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef
):
    """
    - **StreamSelection** *(dict) --*A StreamSelection configuration.

      - **MaxVideoBitsPerSecond** *(integer) --*The maximum video bitrate (bps) to include in
      output.
      - **MinVideoBitsPerSecond** *(integer) --*The minimum video bitrate (bps) to include in
      output.
      - **StreamOrder** *(string) --*A directive that determines the order of streams in the output.
    """


_ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientCreatePackagingConfigurationDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef(
    _ClientCreatePackagingConfigurationDashPackageDashManifestsTypeDef
):
    """
    - *(dict) --*A DASH manifest configuration.

      - **ManifestName** *(string) --*An optional string to include in the name of the manifest.
      - **MinBufferTimeSeconds** *(integer) --*Minimum duration (in seconds) that a player will
      buffer media before starting the presentation.
      - **Profile** *(string) --*The Dynamic Adaptive Streaming over HTTP (DASH) profile type. When
      set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
      - **StreamSelection** *(dict) --*A StreamSelection configuration.

        - **MaxVideoBitsPerSecond** *(integer) --*The maximum video bitrate (bps) to include in
        output.
        - **MinVideoBitsPerSecond** *(integer) --*The minimum video bitrate (bps) to include in
        output.
        - **StreamOrder** *(string) --*A directive that determines the order of streams in the
        output.
    """


_ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationDashPackageEncryptionTypeDef
):
    pass


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
    """
    - **DashManifests** *(list) --***[REQUIRED]** A list of DASH manifest configurations.

      - *(dict) --*A DASH manifest configuration.

        - **ManifestName** *(string) --*An optional string to include in the name of the manifest.
        - **MinBufferTimeSeconds** *(integer) --*Minimum duration (in seconds) that a player will
        buffer media before starting the presentation.
        - **Profile** *(string) --*The Dynamic Adaptive Streaming over HTTP (DASH) profile type.
        When set to "HBBTV_1_5", HbbTV 1.5 compliant output is enabled.
        - **StreamSelection** *(dict) --*A StreamSelection configuration.

          - **MaxVideoBitsPerSecond** *(integer) --*The maximum video bitrate (bps) to include in
          output.
          - **MinVideoBitsPerSecond** *(integer) --*The minimum video bitrate (bps) to include in
          output.
          - **StreamOrder** *(string) --*A directive that determines the order of streams in the
          output.
    """


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
    """
    - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
    Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
      AWS Elemental MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

        - *(string) --*
    """


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
    """
    - **Encryption** *(dict) --*An HTTP Live Streaming (HLS) encryption configuration.

      - **ConstantInitializationVector** *(string) --*A constant initialization vector for
      encryption (optional). When not specified the initialization vector will be periodically
      rotated.
      - **EncryptionMethod** *(string) --*The encryption method to use.
      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationHlsPackageHlsManifestsStreamSelectionTypeDef
):
    pass


_ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef",
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


class ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef(
    _ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef
):
    pass


_ClientCreatePackagingConfigurationHlsPackageTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationHlsPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationHlsPackageEncryptionTypeDef,
        "HlsManifests": List[ClientCreatePackagingConfigurationHlsPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ClientCreatePackagingConfigurationHlsPackageTypeDef(
    _ClientCreatePackagingConfigurationHlsPackageTypeDef
):
    """
    - **Encryption** *(dict) --*An HTTP Live Streaming (HLS) encryption configuration.

      - **ConstantInitializationVector** *(string) --*A constant initialization vector for
      encryption (optional). When not specified the initialization vector will be periodically
      rotated.
      - **EncryptionMethod** *(string) --*The encryption method to use.
      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


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
    """
    - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
    Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
      AWS Elemental MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

        - *(string) --*
    """


_ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationMssPackageEncryptionSpekeKeyProviderTypeDef
    },
)


class ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A Microsoft Smooth Streaming (MSS) encryption configuration.

      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef
):
    pass


_ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientCreatePackagingConfigurationMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef(
    _ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef
):
    pass


_ClientCreatePackagingConfigurationMssPackageTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationMssPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationMssPackageEncryptionTypeDef,
        "MssManifests": List[ClientCreatePackagingConfigurationMssPackageMssManifestsTypeDef],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationMssPackageTypeDef(
    _ClientCreatePackagingConfigurationMssPackageTypeDef
):
    """
    - **Encryption** *(dict) --*A Microsoft Smooth Streaming (MSS) encryption configuration.

      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
):
    """
    - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager and
    Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
      MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --*The system IDs to include in key requests.

        - *(string) --*
    """


_ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A CMAF encryption configuration.

      - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
      and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
        MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --*The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
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


class ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef(
    _ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseCmafPackageTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseCmafPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientCreatePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseCmafPackageTypeDef(
    _ClientCreatePackagingConfigurationResponseCmafPackageTypeDef
):
    """
    - **CmafPackage** *(dict) --*A CMAF packaging configuration.

      - **Encryption** *(dict) --*A CMAF encryption configuration.

        - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
        and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

          - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
          MediaPackage will assume when accessing the key provider service.
          - **SystemIds** *(list) --*The system IDs to include in key requests.

            - *(string) --*
    """


_ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientCreatePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef(
    _ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseDashPackageTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseDashPackageTypeDef",
    {
        "DashManifests": List[
            ClientCreatePackagingConfigurationResponseDashPackageDashManifestsTypeDef
        ],
        "Encryption": ClientCreatePackagingConfigurationResponseDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseDashPackageTypeDef(
    _ClientCreatePackagingConfigurationResponseDashPackageTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationResponseHlsPackageEncryptionTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
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


class ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef(
    _ClientCreatePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseHlsPackageTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseHlsPackageTypeDef",
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


class ClientCreatePackagingConfigurationResponseHlsPackageTypeDef(
    _ClientCreatePackagingConfigurationResponseHlsPackageTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreatePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef(
    _ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef(
    _ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientCreatePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef(
    _ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseMssPackageTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseMssPackageTypeDef",
    {
        "Encryption": ClientCreatePackagingConfigurationResponseMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientCreatePackagingConfigurationResponseMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientCreatePackagingConfigurationResponseMssPackageTypeDef(
    _ClientCreatePackagingConfigurationResponseMssPackageTypeDef
):
    pass


_ClientCreatePackagingConfigurationResponseTypeDef = TypedDict(
    "_ClientCreatePackagingConfigurationResponseTypeDef",
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


class ClientCreatePackagingConfigurationResponseTypeDef(
    _ClientCreatePackagingConfigurationResponseTypeDef
):
    """
    - *(dict) --*The new MediaPackage VOD PackagingConfiguration resource.

      - **Arn** *(string) --*The ARN of the PackagingConfiguration.
      - **CmafPackage** *(dict) --*A CMAF packaging configuration.

        - **Encryption** *(dict) --*A CMAF encryption configuration.

          - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
          Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

            - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
            Elemental MediaPackage will assume when accessing the key provider service.
            - **SystemIds** *(list) --*The system IDs to include in key requests.

              - *(string) --*
    """


_ClientCreatePackagingGroupResponseTypeDef = TypedDict(
    "_ClientCreatePackagingGroupResponseTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)


class ClientCreatePackagingGroupResponseTypeDef(_ClientCreatePackagingGroupResponseTypeDef):
    """
    - *(dict) --*The new MediaPackage VOD PackagingGroup resource.

      - **Arn** *(string) --*The ARN of the PackagingGroup.
      - **DomainName** *(string) --*The fully qualified domain name for Assets in the
      PackagingGroup.
      - **Id** *(string) --*The ID of the PackagingGroup.
    """


_ClientDescribeAssetResponseEgressEndpointsTypeDef = TypedDict(
    "_ClientDescribeAssetResponseEgressEndpointsTypeDef",
    {"PackagingConfigurationId": str, "Url": str},
    total=False,
)


class ClientDescribeAssetResponseEgressEndpointsTypeDef(
    _ClientDescribeAssetResponseEgressEndpointsTypeDef
):
    """
    - *(dict) --*The endpoint URL used to access an Asset using one PackagingConfiguration.

      - **PackagingConfigurationId** *(string) --*The ID of the PackagingConfiguration being applied
      to the Asset.
      - **Url** *(string) --*The URL of the parent manifest for the repackaged Asset.
    """


_ClientDescribeAssetResponseTypeDef = TypedDict(
    "_ClientDescribeAssetResponseTypeDef",
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


class ClientDescribeAssetResponseTypeDef(_ClientDescribeAssetResponseTypeDef):
    """
    - *(dict) --*A MediaPackage VOD Asset resource.

      - **Arn** *(string) --*The ARN of the Asset.
      - **CreatedAt** *(string) --*The time the Asset was initially submitted for Ingest.
      - **EgressEndpoints** *(list) --*The list of egress endpoints available for the Asset.

        - *(dict) --*The endpoint URL used to access an Asset using one PackagingConfiguration.

          - **PackagingConfigurationId** *(string) --*The ID of the PackagingConfiguration being
          applied to the Asset.
          - **Url** *(string) --*The URL of the parent manifest for the repackaged Asset.
    """


_ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
):
    """
    - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager and
    Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
      MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --*The system IDs to include in key requests.

        - *(string) --*
    """


_ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef(
    _ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A CMAF encryption configuration.

      - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
      and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
        MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --*The system IDs to include in key requests.

          - *(string) --*
    """


_ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef(
    _ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsStreamSelectionTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef",
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


class ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef(
    _ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseCmafPackageTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseCmafPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientDescribePackagingConfigurationResponseCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseCmafPackageTypeDef(
    _ClientDescribePackagingConfigurationResponseCmafPackageTypeDef
):
    """
    - **CmafPackage** *(dict) --*A CMAF packaging configuration.

      - **Encryption** *(dict) --*A CMAF encryption configuration.

        - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
        and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

          - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
          MediaPackage will assume when accessing the key provider service.
          - **SystemIds** *(list) --*The system IDs to include in key requests.

            - *(string) --*
    """


_ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef(
    _ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientDescribePackagingConfigurationResponseDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef(
    _ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef(
    _ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseDashPackageTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseDashPackageTypeDef",
    {
        "DashManifests": List[
            ClientDescribePackagingConfigurationResponseDashPackageDashManifestsTypeDef
        ],
        "Encryption": ClientDescribePackagingConfigurationResponseDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseDashPackageTypeDef(
    _ClientDescribePackagingConfigurationResponseDashPackageTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef(
    _ClientDescribePackagingConfigurationResponseHlsPackageEncryptionTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef(
    _ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsStreamSelectionTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef",
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


class ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef(
    _ClientDescribePackagingConfigurationResponseHlsPackageHlsManifestsTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseHlsPackageTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseHlsPackageTypeDef",
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


class ClientDescribePackagingConfigurationResponseHlsPackageTypeDef(
    _ClientDescribePackagingConfigurationResponseHlsPackageTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribePackagingConfigurationResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef(
    _ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef(
    _ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientDescribePackagingConfigurationResponseMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef(
    _ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseMssPackageTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseMssPackageTypeDef",
    {
        "Encryption": ClientDescribePackagingConfigurationResponseMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientDescribePackagingConfigurationResponseMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientDescribePackagingConfigurationResponseMssPackageTypeDef(
    _ClientDescribePackagingConfigurationResponseMssPackageTypeDef
):
    pass


_ClientDescribePackagingConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribePackagingConfigurationResponseTypeDef",
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


class ClientDescribePackagingConfigurationResponseTypeDef(
    _ClientDescribePackagingConfigurationResponseTypeDef
):
    """
    - *(dict) --*A MediaPackage VOD PackagingConfiguration resource.

      - **Arn** *(string) --*The ARN of the PackagingConfiguration.
      - **CmafPackage** *(dict) --*A CMAF packaging configuration.

        - **Encryption** *(dict) --*A CMAF encryption configuration.

          - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
          Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

            - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
            Elemental MediaPackage will assume when accessing the key provider service.
            - **SystemIds** *(list) --*The system IDs to include in key requests.

              - *(string) --*
    """


_ClientDescribePackagingGroupResponseTypeDef = TypedDict(
    "_ClientDescribePackagingGroupResponseTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)


class ClientDescribePackagingGroupResponseTypeDef(_ClientDescribePackagingGroupResponseTypeDef):
    """
    - *(dict) --*A MediaPackage VOD PackagingGroup resource.

      - **Arn** *(string) --*The ARN of the PackagingGroup.
      - **DomainName** *(string) --*The fully qualified domain name for Assets in the
      PackagingGroup.
      - **Id** *(string) --*The ID of the PackagingGroup.
    """


_ClientListAssetsResponseAssetsTypeDef = TypedDict(
    "_ClientListAssetsResponseAssetsTypeDef",
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


class ClientListAssetsResponseAssetsTypeDef(_ClientListAssetsResponseAssetsTypeDef):
    """
    - *(dict) --*A MediaPackage VOD Asset resource.

      - **Arn** *(string) --*The ARN of the Asset.
      - **CreatedAt** *(string) --*The time the Asset was initially submitted for Ingest.
      - **Id** *(string) --*The unique identifier for the Asset.
      - **PackagingGroupId** *(string) --*The ID of the PackagingGroup for the Asset.
      - **ResourceId** *(string) --*The resource ID to include in SPEKE key requests.
      - **SourceArn** *(string) --*ARN of the source object in S3.
      - **SourceRoleArn** *(string) --*The IAM role ARN used to access the source S3 bucket.
    """


_ClientListAssetsResponseTypeDef = TypedDict(
    "_ClientListAssetsResponseTypeDef",
    {"Assets": List[ClientListAssetsResponseAssetsTypeDef], "NextToken": str},
    total=False,
)


class ClientListAssetsResponseTypeDef(_ClientListAssetsResponseTypeDef):
    """
    - *(dict) --*A collection of MediaPackage VOD Asset resources.

      - **Assets** *(list) --*A list of MediaPackage VOD Asset resources.

        - *(dict) --*A MediaPackage VOD Asset resource.

          - **Arn** *(string) --*The ARN of the Asset.
          - **CreatedAt** *(string) --*The time the Asset was initially submitted for Ingest.
          - **Id** *(string) --*The unique identifier for the Asset.
          - **PackagingGroupId** *(string) --*The ID of the PackagingGroup for the Asset.
          - **ResourceId** *(string) --*The resource ID to include in SPEKE key requests.
          - **SourceArn** *(string) --*ARN of the source object in S3.
          - **SourceRoleArn** *(string) --*The IAM role ARN used to access the source S3 bucket.
    """


_ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef
):
    """
    - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager and
    Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
      MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --*The system IDs to include in key requests.

        - *(string) --*
    """


_ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A CMAF encryption configuration.

      - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
      and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
        MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --*The system IDs to include in key requests.

          - *(string) --*
    """


_ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef",
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


class ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef",
    {
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsCmafPackageTypeDef
):
    """
    - **CmafPackage** *(dict) --*A CMAF packaging configuration.

      - **Encryption** *(dict) --*A CMAF encryption configuration.

        - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
        and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

          - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
          MediaPackage will assume when accessing the key provider service.
          - **SystemIds** *(list) --*The system IDs to include in key requests.

            - *(string) --*
    """


_ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef",
    {
        "DashManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageDashManifestsTypeDef
        ],
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsDashPackageTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageEncryptionTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef",
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


class ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef",
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


class ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsHlsPackageTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef",
    {
        "Encryption": ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsMssPackageTypeDef
):
    pass


_ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef",
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


class ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef(
    _ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef
):
    """
    - *(dict) --*A MediaPackage VOD PackagingConfiguration resource.

      - **Arn** *(string) --*The ARN of the PackagingConfiguration.
      - **CmafPackage** *(dict) --*A CMAF packaging configuration.

        - **Encryption** *(dict) --*A CMAF encryption configuration.

          - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
          Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

            - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
            Elemental MediaPackage will assume when accessing the key provider service.
            - **SystemIds** *(list) --*The system IDs to include in key requests.

              - *(string) --*
    """


_ClientListPackagingConfigurationsResponseTypeDef = TypedDict(
    "_ClientListPackagingConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingConfigurations": List[
            ClientListPackagingConfigurationsResponsePackagingConfigurationsTypeDef
        ],
    },
    total=False,
)


class ClientListPackagingConfigurationsResponseTypeDef(
    _ClientListPackagingConfigurationsResponseTypeDef
):
    """
    - *(dict) --*A collection of MediaPackage VOD PackagingConfiguration resources.

      - **NextToken** *(string) --*A token that can be used to resume pagination from the end of the
      collection.
      - **PackagingConfigurations** *(list) --*A list of MediaPackage VOD PackagingConfiguration
      resources.

        - *(dict) --*A MediaPackage VOD PackagingConfiguration resource.

          - **Arn** *(string) --*The ARN of the PackagingConfiguration.
          - **CmafPackage** *(dict) --*A CMAF packaging configuration.

            - **Encryption** *(dict) --*A CMAF encryption configuration.

              - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
              Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

                - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
                Elemental MediaPackage will assume when accessing the key provider service.
                - **SystemIds** *(list) --*The system IDs to include in key requests.

                  - *(string) --*
    """


_ClientListPackagingGroupsResponsePackagingGroupsTypeDef = TypedDict(
    "_ClientListPackagingGroupsResponsePackagingGroupsTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)


class ClientListPackagingGroupsResponsePackagingGroupsTypeDef(
    _ClientListPackagingGroupsResponsePackagingGroupsTypeDef
):
    """
    - *(dict) --*A MediaPackage VOD PackagingGroup resource.

      - **Arn** *(string) --*The ARN of the PackagingGroup.
      - **DomainName** *(string) --*The fully qualified domain name for Assets in the
      PackagingGroup.
      - **Id** *(string) --*The ID of the PackagingGroup.
    """


_ClientListPackagingGroupsResponseTypeDef = TypedDict(
    "_ClientListPackagingGroupsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingGroups": List[ClientListPackagingGroupsResponsePackagingGroupsTypeDef],
    },
    total=False,
)


class ClientListPackagingGroupsResponseTypeDef(_ClientListPackagingGroupsResponseTypeDef):
    """
    - *(dict) --*A collection of MediaPackage VOD PackagingGroup resources.

      - **NextToken** *(string) --*A token that can be used to resume pagination from the end of the
      collection.
      - **PackagingGroups** *(list) --*A list of MediaPackage VOD PackagingGroup resources.

        - *(dict) --*A MediaPackage VOD PackagingGroup resource.

          - **Arn** *(string) --*The ARN of the PackagingGroup.
          - **DomainName** *(string) --*The fully qualified domain name for Assets in the
          PackagingGroup.
          - **Id** *(string) --*The ID of the PackagingGroup.
    """


_ListAssetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAssetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAssetsPaginatePaginationConfigTypeDef(_ListAssetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAssetsPaginateResponseAssetsTypeDef = TypedDict(
    "_ListAssetsPaginateResponseAssetsTypeDef",
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


class ListAssetsPaginateResponseAssetsTypeDef(_ListAssetsPaginateResponseAssetsTypeDef):
    """
    - *(dict) --*A MediaPackage VOD Asset resource.

      - **Arn** *(string) --*The ARN of the Asset.
      - **CreatedAt** *(string) --*The time the Asset was initially submitted for Ingest.
      - **Id** *(string) --*The unique identifier for the Asset.
      - **PackagingGroupId** *(string) --*The ID of the PackagingGroup for the Asset.
      - **ResourceId** *(string) --*The resource ID to include in SPEKE key requests.
      - **SourceArn** *(string) --*ARN of the source object in S3.
      - **SourceRoleArn** *(string) --*The IAM role ARN used to access the source S3 bucket.
    """


_ListAssetsPaginateResponseTypeDef = TypedDict(
    "_ListAssetsPaginateResponseTypeDef",
    {"Assets": List[ListAssetsPaginateResponseAssetsTypeDef]},
    total=False,
)


class ListAssetsPaginateResponseTypeDef(_ListAssetsPaginateResponseTypeDef):
    """
    - *(dict) --*A collection of MediaPackage VOD Asset resources.

      - **Assets** *(list) --*A list of MediaPackage VOD Asset resources.

        - *(dict) --*A MediaPackage VOD Asset resource.

          - **Arn** *(string) --*The ARN of the Asset.
          - **CreatedAt** *(string) --*The time the Asset was initially submitted for Ingest.
          - **Id** *(string) --*The unique identifier for the Asset.
          - **PackagingGroupId** *(string) --*The ID of the PackagingGroup for the Asset.
          - **ResourceId** *(string) --*The resource ID to include in SPEKE key requests.
          - **SourceArn** *(string) --*ARN of the source object in S3.
          - **SourceRoleArn** *(string) --*The IAM role ARN used to access the source S3 bucket.
    """


_ListPackagingConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPackagingConfigurationsPaginatePaginationConfigTypeDef(
    _ListPackagingConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef
):
    """
    - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager and
    Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
      MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --*The system IDs to include in key requests.

        - *(string) --*
    """


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A CMAF encryption configuration.

      - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
      and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
        MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --*The system IDs to include in key requests.

          - *(string) --*
    """


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsStreamSelectionTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef",
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


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageTypeDef",
    {
        "Encryption": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsCmafPackageTypeDef
):
    """
    - **CmafPackage** *(dict) --*A CMAF packaging configuration.

      - **Encryption** *(dict) --*A CMAF encryption configuration.

        - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
        and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

          - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
          MediaPackage will assume when accessing the key provider service.
          - **SystemIds** *(list) --*The system IDs to include in key requests.

            - *(string) --*
    """


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsTypeDef",
    {
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "StreamSelection": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageTypeDef",
    {
        "DashManifests": List[
            ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageDashManifestsTypeDef
        ],
        "Encryption": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageEncryptionTypeDef,
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsDashPackageTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "SpekeKeyProvider": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageEncryptionTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsStreamSelectionTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef",
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


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageHlsManifestsTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageTypeDef",
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


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsHlsPackageTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsStreamSelectionTypeDef,
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageTypeDef",
    {
        "Encryption": ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageEncryptionTypeDef,
        "MssManifests": List[
            ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageMssManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsMssPackageTypeDef
):
    pass


_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponsePackagingConfigurationsTypeDef",
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


class ListPackagingConfigurationsPaginateResponsePackagingConfigurationsTypeDef(
    _ListPackagingConfigurationsPaginateResponsePackagingConfigurationsTypeDef
):
    """
    - *(dict) --*A MediaPackage VOD PackagingConfiguration resource.

      - **Arn** *(string) --*The ARN of the PackagingConfiguration.
      - **CmafPackage** *(dict) --*A CMAF packaging configuration.

        - **Encryption** *(dict) --*A CMAF encryption configuration.

          - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
          Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

            - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
            Elemental MediaPackage will assume when accessing the key provider service.
            - **SystemIds** *(list) --*The system IDs to include in key requests.

              - *(string) --*
    """


_ListPackagingConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListPackagingConfigurationsPaginateResponseTypeDef",
    {
        "PackagingConfigurations": List[
            ListPackagingConfigurationsPaginateResponsePackagingConfigurationsTypeDef
        ]
    },
    total=False,
)


class ListPackagingConfigurationsPaginateResponseTypeDef(
    _ListPackagingConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*A collection of MediaPackage VOD PackagingConfiguration resources.

      - **PackagingConfigurations** *(list) --*A list of MediaPackage VOD PackagingConfiguration
      resources.

        - *(dict) --*A MediaPackage VOD PackagingConfiguration resource.

          - **Arn** *(string) --*The ARN of the PackagingConfiguration.
          - **CmafPackage** *(dict) --*A CMAF packaging configuration.

            - **Encryption** *(dict) --*A CMAF encryption configuration.

              - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
              Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

                - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
                Elemental MediaPackage will assume when accessing the key provider service.
                - **SystemIds** *(list) --*The system IDs to include in key requests.

                  - *(string) --*
    """


_ListPackagingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPackagingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPackagingGroupsPaginatePaginationConfigTypeDef(
    _ListPackagingGroupsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef = TypedDict(
    "_ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef",
    {"Arn": str, "DomainName": str, "Id": str},
    total=False,
)


class ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef(
    _ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef
):
    """
    - *(dict) --*A MediaPackage VOD PackagingGroup resource.

      - **Arn** *(string) --*The ARN of the PackagingGroup.
      - **DomainName** *(string) --*The fully qualified domain name for Assets in the
      PackagingGroup.
      - **Id** *(string) --*The ID of the PackagingGroup.
    """


_ListPackagingGroupsPaginateResponseTypeDef = TypedDict(
    "_ListPackagingGroupsPaginateResponseTypeDef",
    {"PackagingGroups": List[ListPackagingGroupsPaginateResponsePackagingGroupsTypeDef]},
    total=False,
)


class ListPackagingGroupsPaginateResponseTypeDef(_ListPackagingGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*A collection of MediaPackage VOD PackagingGroup resources.

      - **PackagingGroups** *(list) --*A list of MediaPackage VOD PackagingGroup resources.

        - *(dict) --*A MediaPackage VOD PackagingGroup resource.

          - **Arn** *(string) --*The ARN of the PackagingGroup.
          - **DomainName** *(string) --*The fully qualified domain name for Assets in the
          PackagingGroup.
          - **Id** *(string) --*The ID of the PackagingGroup.
    """
