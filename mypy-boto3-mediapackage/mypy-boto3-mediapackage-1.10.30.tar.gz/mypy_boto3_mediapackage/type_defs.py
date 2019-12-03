"Main interface for mediapackage service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef",
    "ClientCreateChannelResponseHlsIngestTypeDef",
    "ClientCreateChannelResponseTypeDef",
    "ClientCreateHarvestJobResponseS3DestinationTypeDef",
    "ClientCreateHarvestJobResponseTypeDef",
    "ClientCreateHarvestJobS3DestinationTypeDef",
    "ClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointCmafPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointCmafPackageHlsManifestsTypeDef",
    "ClientCreateOriginEndpointCmafPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointCmafPackageTypeDef",
    "ClientCreateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointDashPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointDashPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointDashPackageTypeDef",
    "ClientCreateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointHlsPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointHlsPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointHlsPackageTypeDef",
    "ClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointMssPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointMssPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointMssPackageTypeDef",
    "ClientCreateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointResponseCmafPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    "ClientCreateOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointResponseCmafPackageTypeDef",
    "ClientCreateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointResponseDashPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointResponseDashPackageTypeDef",
    "ClientCreateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointResponseHlsPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointResponseHlsPackageTypeDef",
    "ClientCreateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientCreateOriginEndpointResponseMssPackageEncryptionTypeDef",
    "ClientCreateOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    "ClientCreateOriginEndpointResponseMssPackageTypeDef",
    "ClientCreateOriginEndpointResponseTypeDef",
    "ClientDescribeChannelResponseHlsIngestIngestEndpointsTypeDef",
    "ClientDescribeChannelResponseHlsIngestTypeDef",
    "ClientDescribeChannelResponseTypeDef",
    "ClientDescribeHarvestJobResponseS3DestinationTypeDef",
    "ClientDescribeHarvestJobResponseTypeDef",
    "ClientDescribeOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribeOriginEndpointResponseCmafPackageEncryptionTypeDef",
    "ClientDescribeOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    "ClientDescribeOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    "ClientDescribeOriginEndpointResponseCmafPackageTypeDef",
    "ClientDescribeOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribeOriginEndpointResponseDashPackageEncryptionTypeDef",
    "ClientDescribeOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    "ClientDescribeOriginEndpointResponseDashPackageTypeDef",
    "ClientDescribeOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribeOriginEndpointResponseHlsPackageEncryptionTypeDef",
    "ClientDescribeOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    "ClientDescribeOriginEndpointResponseHlsPackageTypeDef",
    "ClientDescribeOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientDescribeOriginEndpointResponseMssPackageEncryptionTypeDef",
    "ClientDescribeOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    "ClientDescribeOriginEndpointResponseMssPackageTypeDef",
    "ClientDescribeOriginEndpointResponseTypeDef",
    "ClientListChannelsResponseChannelsHlsIngestIngestEndpointsTypeDef",
    "ClientListChannelsResponseChannelsHlsIngestTypeDef",
    "ClientListChannelsResponseChannelsTypeDef",
    "ClientListChannelsResponseTypeDef",
    "ClientListHarvestJobsResponseHarvestJobsS3DestinationTypeDef",
    "ClientListHarvestJobsResponseHarvestJobsTypeDef",
    "ClientListHarvestJobsResponseTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageHlsManifestsTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageStreamSelectionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsCmafPackageTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageStreamSelectionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsDashPackageTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageStreamSelectionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsHlsPackageTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageStreamSelectionTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsMssPackageTypeDef",
    "ClientListOriginEndpointsResponseOriginEndpointsTypeDef",
    "ClientListOriginEndpointsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRotateChannelCredentialsResponseHlsIngestIngestEndpointsTypeDef",
    "ClientRotateChannelCredentialsResponseHlsIngestTypeDef",
    "ClientRotateChannelCredentialsResponseTypeDef",
    "ClientRotateIngestEndpointCredentialsResponseHlsIngestIngestEndpointsTypeDef",
    "ClientRotateIngestEndpointCredentialsResponseHlsIngestTypeDef",
    "ClientRotateIngestEndpointCredentialsResponseTypeDef",
    "ClientUpdateChannelResponseHlsIngestIngestEndpointsTypeDef",
    "ClientUpdateChannelResponseHlsIngestTypeDef",
    "ClientUpdateChannelResponseTypeDef",
    "ClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointCmafPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointCmafPackageHlsManifestsTypeDef",
    "ClientUpdateOriginEndpointCmafPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointCmafPackageTypeDef",
    "ClientUpdateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointDashPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointDashPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointDashPackageTypeDef",
    "ClientUpdateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointHlsPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointHlsPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointHlsPackageTypeDef",
    "ClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointMssPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointMssPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointMssPackageTypeDef",
    "ClientUpdateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointResponseCmafPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    "ClientUpdateOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointResponseCmafPackageTypeDef",
    "ClientUpdateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointResponseDashPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointResponseDashPackageTypeDef",
    "ClientUpdateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointResponseHlsPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointResponseHlsPackageTypeDef",
    "ClientUpdateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ClientUpdateOriginEndpointResponseMssPackageEncryptionTypeDef",
    "ClientUpdateOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    "ClientUpdateOriginEndpointResponseMssPackageTypeDef",
    "ClientUpdateOriginEndpointResponseTypeDef",
    "ListChannelsPaginatePaginationConfigTypeDef",
    "ListChannelsPaginateResponseChannelsHlsIngestIngestEndpointsTypeDef",
    "ListChannelsPaginateResponseChannelsHlsIngestTypeDef",
    "ListChannelsPaginateResponseChannelsTypeDef",
    "ListChannelsPaginateResponseTypeDef",
    "ListHarvestJobsPaginatePaginationConfigTypeDef",
    "ListHarvestJobsPaginateResponseHarvestJobsS3DestinationTypeDef",
    "ListHarvestJobsPaginateResponseHarvestJobsTypeDef",
    "ListHarvestJobsPaginateResponseTypeDef",
    "ListOriginEndpointsPaginatePaginationConfigTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageHlsManifestsTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageStreamSelectionTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageStreamSelectionTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageStreamSelectionTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageStreamSelectionTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageTypeDef",
    "ListOriginEndpointsPaginateResponseOriginEndpointsTypeDef",
    "ListOriginEndpointsPaginateResponseTypeDef",
)


_ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef = TypedDict(
    "_ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)


class ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef(
    _ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef
):
    """
    - *(dict) --*An endpoint for ingesting source content for a Channel.

      - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
      - **Password** *(string) --*The system generated password for ingest authentication.
      - **Url** *(string) --*The ingest URL to which the source stream should be sent.
      - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientCreateChannelResponseHlsIngestTypeDef = TypedDict(
    "_ClientCreateChannelResponseHlsIngestTypeDef",
    {"IngestEndpoints": List[ClientCreateChannelResponseHlsIngestIngestEndpointsTypeDef]},
    total=False,
)


class ClientCreateChannelResponseHlsIngestTypeDef(_ClientCreateChannelResponseHlsIngestTypeDef):
    """
    - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

      - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
      sent.

        - *(dict) --*An endpoint for ingesting source content for a Channel.

          - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
          - **Password** *(string) --*The system generated password for ingest authentication.
          - **Url** *(string) --*The ingest URL to which the source stream should be sent.
          - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientCreateChannelResponseTypeDef = TypedDict(
    "_ClientCreateChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientCreateChannelResponseHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateChannelResponseTypeDef(_ClientCreateChannelResponseTypeDef):
    """
    - *(dict) --*The new Channel record.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the Channel.
      - **Description** *(string) --*A short text description of the Channel.
      - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

        - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
        sent.

          - *(dict) --*An endpoint for ingesting source content for a Channel.

            - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
            - **Password** *(string) --*The system generated password for ingest authentication.
            - **Url** *(string) --*The ingest URL to which the source stream should be sent.
            - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientCreateHarvestJobResponseS3DestinationTypeDef = TypedDict(
    "_ClientCreateHarvestJobResponseS3DestinationTypeDef",
    {"BucketName": str, "ManifestKey": str, "RoleArn": str},
    total=False,
)


class ClientCreateHarvestJobResponseS3DestinationTypeDef(
    _ClientCreateHarvestJobResponseS3DestinationTypeDef
):
    """
    - **S3Destination** *(dict) --*Configuration parameters for where in an S3 bucket to place the
    harvested content

      - **BucketName** *(string) --*The name of an S3 bucket within which harvested content will be
      exported
      - **ManifestKey** *(string) --*The key in the specified S3 bucket where the harvested
      top-level manifest will be placed.
      - **RoleArn** *(string) --*The IAM role used to write to the specified S3 bucket
    """


_ClientCreateHarvestJobResponseTypeDef = TypedDict(
    "_ClientCreateHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": ClientCreateHarvestJobResponseS3DestinationTypeDef,
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)


class ClientCreateHarvestJobResponseTypeDef(_ClientCreateHarvestJobResponseTypeDef):
    """
    - *(dict) --*A new HarvestJob record.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the HarvestJob.
      - **ChannelId** *(string) --*The ID of the Channel that the HarvestJob will harvest from.
      - **CreatedAt** *(string) --*The time the HarvestJob was submitted
      - **EndTime** *(string) --*The end of the time-window which will be harvested.
      - **Id** *(string) --*The ID of the HarvestJob. The ID must be unique within the region and it
      cannot be changed after the HarvestJob is submitted.
      - **OriginEndpointId** *(string) --*The ID of the OriginEndpoint that the HarvestJob will
      harvest from. This cannot be changed after the HarvestJob is submitted.
      - **S3Destination** *(dict) --*Configuration parameters for where in an S3 bucket to place the
      harvested content

        - **BucketName** *(string) --*The name of an S3 bucket within which harvested content will
        be exported
        - **ManifestKey** *(string) --*The key in the specified S3 bucket where the harvested
        top-level manifest will be placed.
        - **RoleArn** *(string) --*The IAM role used to write to the specified S3 bucket
    """


_ClientCreateHarvestJobS3DestinationTypeDef = TypedDict(
    "_ClientCreateHarvestJobS3DestinationTypeDef",
    {"BucketName": str, "ManifestKey": str, "RoleArn": str},
)


class ClientCreateHarvestJobS3DestinationTypeDef(_ClientCreateHarvestJobS3DestinationTypeDef):
    """
    - **BucketName** *(string) --***[REQUIRED]** The name of an S3 bucket within which harvested
    content will be exported
    - **ManifestKey** *(string) --***[REQUIRED]** The key in the specified S3 bucket where the
    harvested top-level manifest will be placed.
    - **RoleArn** *(string) --***[REQUIRED]** The IAM role used to write to the specified S3 bucket
    """


_RequiredClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"ResourceId": str, "RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "Url": str},
    total=False,
)


class ClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef,
):
    """
    - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
    Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
      certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the
      key provider service.
      - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
      - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
      AWS Elemental MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

        - *(string) --*
    """


_RequiredClientCreateOriginEndpointCmafPackageEncryptionTypeDef = TypedDict(
    "_RequiredClientCreateOriginEndpointCmafPackageEncryptionTypeDef",
    {"SpekeKeyProvider": ClientCreateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef},
)
_OptionalClientCreateOriginEndpointCmafPackageEncryptionTypeDef = TypedDict(
    "_OptionalClientCreateOriginEndpointCmafPackageEncryptionTypeDef",
    {"KeyRotationIntervalSeconds": int},
    total=False,
)


class ClientCreateOriginEndpointCmafPackageEncryptionTypeDef(
    _RequiredClientCreateOriginEndpointCmafPackageEncryptionTypeDef,
    _OptionalClientCreateOriginEndpointCmafPackageEncryptionTypeDef,
):
    """
    - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

      - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
      rotation.
      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreateOriginEndpointCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientCreateOriginEndpointCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
    },
    total=False,
)


class ClientCreateOriginEndpointCmafPackageHlsManifestsTypeDef(
    _ClientCreateOriginEndpointCmafPackageHlsManifestsTypeDef
):
    pass


_ClientCreateOriginEndpointCmafPackageStreamSelectionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreateOriginEndpointCmafPackageStreamSelectionTypeDef(
    _ClientCreateOriginEndpointCmafPackageStreamSelectionTypeDef
):
    pass


_ClientCreateOriginEndpointCmafPackageTypeDef = TypedDict(
    "_ClientCreateOriginEndpointCmafPackageTypeDef",
    {
        "Encryption": ClientCreateOriginEndpointCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientCreateOriginEndpointCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientCreateOriginEndpointCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreateOriginEndpointCmafPackageTypeDef(_ClientCreateOriginEndpointCmafPackageTypeDef):
    """
    - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

      - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
      rotation.
      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientCreateOriginEndpointDashPackageEncryptionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientCreateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientCreateOriginEndpointDashPackageEncryptionTypeDef(
    _ClientCreateOriginEndpointDashPackageEncryptionTypeDef
):
    pass


_ClientCreateOriginEndpointDashPackageStreamSelectionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreateOriginEndpointDashPackageStreamSelectionTypeDef(
    _ClientCreateOriginEndpointDashPackageStreamSelectionTypeDef
):
    pass


_ClientCreateOriginEndpointDashPackageTypeDef = TypedDict(
    "_ClientCreateOriginEndpointDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientCreateOriginEndpointDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientCreateOriginEndpointDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)


class ClientCreateOriginEndpointDashPackageTypeDef(_ClientCreateOriginEndpointDashPackageTypeDef):
    """
    - **AdTriggers** *(list) --*A list of SCTE-35 message types that are treated as ad markers in
    the output. If empty, no ad markers are output. Specify multiple items to create ad markers for
    all of the included message types.

      - *(string) --*
    """


_ClientCreateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientCreateOriginEndpointHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientCreateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientCreateOriginEndpointHlsPackageEncryptionTypeDef(
    _ClientCreateOriginEndpointHlsPackageEncryptionTypeDef
):
    pass


_ClientCreateOriginEndpointHlsPackageStreamSelectionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreateOriginEndpointHlsPackageStreamSelectionTypeDef(
    _ClientCreateOriginEndpointHlsPackageStreamSelectionTypeDef
):
    pass


_ClientCreateOriginEndpointHlsPackageTypeDef = TypedDict(
    "_ClientCreateOriginEndpointHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientCreateOriginEndpointHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientCreateOriginEndpointHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ClientCreateOriginEndpointHlsPackageTypeDef(_ClientCreateOriginEndpointHlsPackageTypeDef):
    """
    - **AdMarkers** *(string) --*This setting controls how ad markers are included in the packaged
    OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes
    the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the
    input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout
    tags based on SCTE-35 messages in the input source.
    - **AdTriggers** *(list) --*A list of SCTE-35 message types that are treated as ad markers in
    the output. If empty, no ad markers are output. Specify multiple items to create ad markers for
    all of the included message types.

      - *(string) --*
    """


_RequiredClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"ResourceId": str, "RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "Url": str},
    total=False,
)


class ClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef,
):
    """
    - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
    Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
      certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the
      key provider service.
      - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
      - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
      AWS Elemental MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

        - *(string) --*
    """


_ClientCreateOriginEndpointMssPackageEncryptionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointMssPackageEncryptionTypeDef",
    {"SpekeKeyProvider": ClientCreateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef},
)


class ClientCreateOriginEndpointMssPackageEncryptionTypeDef(
    _ClientCreateOriginEndpointMssPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A Microsoft Smooth Streaming (MSS) encryption configuration.

      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreateOriginEndpointMssPackageStreamSelectionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreateOriginEndpointMssPackageStreamSelectionTypeDef(
    _ClientCreateOriginEndpointMssPackageStreamSelectionTypeDef
):
    pass


_ClientCreateOriginEndpointMssPackageTypeDef = TypedDict(
    "_ClientCreateOriginEndpointMssPackageTypeDef",
    {
        "Encryption": ClientCreateOriginEndpointMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientCreateOriginEndpointMssPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreateOriginEndpointMssPackageTypeDef(_ClientCreateOriginEndpointMssPackageTypeDef):
    """
    - **Encryption** *(dict) --*A Microsoft Smooth Streaming (MSS) encryption configuration.

      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
):
    """
    - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager and
    Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
      certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the
      key provider service.
      - **ResourceId** *(string) --*The resource ID to include in key requests.
      - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
      MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --*The system IDs to include in key requests.

        - *(string) --*
    """


_ClientCreateOriginEndpointResponseCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseCmafPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientCreateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientCreateOriginEndpointResponseCmafPackageEncryptionTypeDef(
    _ClientCreateOriginEndpointResponseCmafPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

      - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
      rotation.
      - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
      and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --*The resource ID to include in key requests.
        - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
        MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --*The system IDs to include in key requests.

          - *(string) --*
    """


_ClientCreateOriginEndpointResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)


class ClientCreateOriginEndpointResponseCmafPackageHlsManifestsTypeDef(
    _ClientCreateOriginEndpointResponseCmafPackageHlsManifestsTypeDef
):
    pass


_ClientCreateOriginEndpointResponseCmafPackageStreamSelectionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreateOriginEndpointResponseCmafPackageStreamSelectionTypeDef(
    _ClientCreateOriginEndpointResponseCmafPackageStreamSelectionTypeDef
):
    pass


_ClientCreateOriginEndpointResponseCmafPackageTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseCmafPackageTypeDef",
    {
        "Encryption": ClientCreateOriginEndpointResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientCreateOriginEndpointResponseCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientCreateOriginEndpointResponseCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreateOriginEndpointResponseCmafPackageTypeDef(
    _ClientCreateOriginEndpointResponseCmafPackageTypeDef
):
    """
    - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging configuration.

      - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

        - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
        rotation.
        - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
        and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

          - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
          certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
          the key provider service.
          - **ResourceId** *(string) --*The resource ID to include in key requests.
          - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
          MediaPackage will assume when accessing the key provider service.
          - **SystemIds** *(list) --*The system IDs to include in key requests.

            - *(string) --*
    """


_ClientCreateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientCreateOriginEndpointResponseDashPackageEncryptionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientCreateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientCreateOriginEndpointResponseDashPackageEncryptionTypeDef(
    _ClientCreateOriginEndpointResponseDashPackageEncryptionTypeDef
):
    pass


_ClientCreateOriginEndpointResponseDashPackageStreamSelectionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreateOriginEndpointResponseDashPackageStreamSelectionTypeDef(
    _ClientCreateOriginEndpointResponseDashPackageStreamSelectionTypeDef
):
    pass


_ClientCreateOriginEndpointResponseDashPackageTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientCreateOriginEndpointResponseDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientCreateOriginEndpointResponseDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)


class ClientCreateOriginEndpointResponseDashPackageTypeDef(
    _ClientCreateOriginEndpointResponseDashPackageTypeDef
):
    pass


_ClientCreateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientCreateOriginEndpointResponseHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientCreateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientCreateOriginEndpointResponseHlsPackageEncryptionTypeDef(
    _ClientCreateOriginEndpointResponseHlsPackageEncryptionTypeDef
):
    pass


_ClientCreateOriginEndpointResponseHlsPackageStreamSelectionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreateOriginEndpointResponseHlsPackageStreamSelectionTypeDef(
    _ClientCreateOriginEndpointResponseHlsPackageStreamSelectionTypeDef
):
    pass


_ClientCreateOriginEndpointResponseHlsPackageTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientCreateOriginEndpointResponseHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientCreateOriginEndpointResponseHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ClientCreateOriginEndpointResponseHlsPackageTypeDef(
    _ClientCreateOriginEndpointResponseHlsPackageTypeDef
):
    pass


_ClientCreateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientCreateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientCreateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientCreateOriginEndpointResponseMssPackageEncryptionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientCreateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientCreateOriginEndpointResponseMssPackageEncryptionTypeDef(
    _ClientCreateOriginEndpointResponseMssPackageEncryptionTypeDef
):
    pass


_ClientCreateOriginEndpointResponseMssPackageStreamSelectionTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientCreateOriginEndpointResponseMssPackageStreamSelectionTypeDef(
    _ClientCreateOriginEndpointResponseMssPackageStreamSelectionTypeDef
):
    pass


_ClientCreateOriginEndpointResponseMssPackageTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseMssPackageTypeDef",
    {
        "Encryption": ClientCreateOriginEndpointResponseMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientCreateOriginEndpointResponseMssPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientCreateOriginEndpointResponseMssPackageTypeDef(
    _ClientCreateOriginEndpointResponseMssPackageTypeDef
):
    pass


_ClientCreateOriginEndpointResponseTypeDef = TypedDict(
    "_ClientCreateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CmafPackage": ClientCreateOriginEndpointResponseCmafPackageTypeDef,
        "DashPackage": ClientCreateOriginEndpointResponseDashPackageTypeDef,
        "Description": str,
        "HlsPackage": ClientCreateOriginEndpointResponseHlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": ClientCreateOriginEndpointResponseMssPackageTypeDef,
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)


class ClientCreateOriginEndpointResponseTypeDef(_ClientCreateOriginEndpointResponseTypeDef):
    """
    - *(dict) --*A new OriginEndpoint record.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
      - **ChannelId** *(string) --*The ID of the Channel the OriginEndpoint is associated with.
      - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging configuration.

        - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption
        configuration.

          - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption
          key rotation.
          - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
          Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

            - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
            certificate that MediaPackage will use for enforcing secure end-to-end data transfer
            with the key provider service.
            - **ResourceId** *(string) --*The resource ID to include in key requests.
            - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
            Elemental MediaPackage will assume when accessing the key provider service.
            - **SystemIds** *(list) --*The system IDs to include in key requests.

              - *(string) --*
    """


_ClientDescribeChannelResponseHlsIngestIngestEndpointsTypeDef = TypedDict(
    "_ClientDescribeChannelResponseHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)


class ClientDescribeChannelResponseHlsIngestIngestEndpointsTypeDef(
    _ClientDescribeChannelResponseHlsIngestIngestEndpointsTypeDef
):
    """
    - *(dict) --*An endpoint for ingesting source content for a Channel.

      - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
      - **Password** *(string) --*The system generated password for ingest authentication.
      - **Url** *(string) --*The ingest URL to which the source stream should be sent.
      - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientDescribeChannelResponseHlsIngestTypeDef = TypedDict(
    "_ClientDescribeChannelResponseHlsIngestTypeDef",
    {"IngestEndpoints": List[ClientDescribeChannelResponseHlsIngestIngestEndpointsTypeDef]},
    total=False,
)


class ClientDescribeChannelResponseHlsIngestTypeDef(_ClientDescribeChannelResponseHlsIngestTypeDef):
    """
    - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

      - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
      sent.

        - *(dict) --*An endpoint for ingesting source content for a Channel.

          - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
          - **Password** *(string) --*The system generated password for ingest authentication.
          - **Url** *(string) --*The ingest URL to which the source stream should be sent.
          - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientDescribeChannelResponseTypeDef = TypedDict(
    "_ClientDescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientDescribeChannelResponseHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeChannelResponseTypeDef(_ClientDescribeChannelResponseTypeDef):
    """
    - *(dict) --*A Channel record.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the Channel.
      - **Description** *(string) --*A short text description of the Channel.
      - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

        - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
        sent.

          - *(dict) --*An endpoint for ingesting source content for a Channel.

            - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
            - **Password** *(string) --*The system generated password for ingest authentication.
            - **Url** *(string) --*The ingest URL to which the source stream should be sent.
            - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientDescribeHarvestJobResponseS3DestinationTypeDef = TypedDict(
    "_ClientDescribeHarvestJobResponseS3DestinationTypeDef",
    {"BucketName": str, "ManifestKey": str, "RoleArn": str},
    total=False,
)


class ClientDescribeHarvestJobResponseS3DestinationTypeDef(
    _ClientDescribeHarvestJobResponseS3DestinationTypeDef
):
    """
    - **S3Destination** *(dict) --*Configuration parameters for where in an S3 bucket to place the
    harvested content

      - **BucketName** *(string) --*The name of an S3 bucket within which harvested content will be
      exported
      - **ManifestKey** *(string) --*The key in the specified S3 bucket where the harvested
      top-level manifest will be placed.
      - **RoleArn** *(string) --*The IAM role used to write to the specified S3 bucket
    """


_ClientDescribeHarvestJobResponseTypeDef = TypedDict(
    "_ClientDescribeHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": ClientDescribeHarvestJobResponseS3DestinationTypeDef,
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)


class ClientDescribeHarvestJobResponseTypeDef(_ClientDescribeHarvestJobResponseTypeDef):
    """
    - *(dict) --*An HarvestJob record.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the HarvestJob.
      - **ChannelId** *(string) --*The ID of the Channel that the HarvestJob will harvest from.
      - **CreatedAt** *(string) --*The time the HarvestJob was submitted
      - **EndTime** *(string) --*The end of the time-window which will be harvested.
      - **Id** *(string) --*The ID of the HarvestJob. The ID must be unique within the region and it
      cannot be changed after the HarvestJob is submitted.
      - **OriginEndpointId** *(string) --*The ID of the OriginEndpoint that the HarvestJob will
      harvest from. This cannot be changed after the HarvestJob is submitted.
      - **S3Destination** *(dict) --*Configuration parameters for where in an S3 bucket to place the
      harvested content

        - **BucketName** *(string) --*The name of an S3 bucket within which harvested content will
        be exported
        - **ManifestKey** *(string) --*The key in the specified S3 bucket where the harvested
        top-level manifest will be placed.
        - **RoleArn** *(string) --*The IAM role used to write to the specified S3 bucket
    """


_ClientDescribeOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientDescribeOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientDescribeOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
):
    """
    - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager and
    Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
      certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the
      key provider service.
      - **ResourceId** *(string) --*The resource ID to include in key requests.
      - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
      MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --*The system IDs to include in key requests.

        - *(string) --*
    """


_ClientDescribeOriginEndpointResponseCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseCmafPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientDescribeOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseCmafPackageEncryptionTypeDef(
    _ClientDescribeOriginEndpointResponseCmafPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

      - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
      rotation.
      - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
      and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --*The resource ID to include in key requests.
        - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
        MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --*The system IDs to include in key requests.

          - *(string) --*
    """


_ClientDescribeOriginEndpointResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseCmafPackageHlsManifestsTypeDef(
    _ClientDescribeOriginEndpointResponseCmafPackageHlsManifestsTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseCmafPackageStreamSelectionTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseCmafPackageStreamSelectionTypeDef(
    _ClientDescribeOriginEndpointResponseCmafPackageStreamSelectionTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseCmafPackageTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseCmafPackageTypeDef",
    {
        "Encryption": ClientDescribeOriginEndpointResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientDescribeOriginEndpointResponseCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientDescribeOriginEndpointResponseCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseCmafPackageTypeDef(
    _ClientDescribeOriginEndpointResponseCmafPackageTypeDef
):
    """
    - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging configuration.

      - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

        - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
        rotation.
        - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
        and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

          - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
          certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
          the key provider service.
          - **ResourceId** *(string) --*The resource ID to include in key requests.
          - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
          MediaPackage will assume when accessing the key provider service.
          - **SystemIds** *(list) --*The system IDs to include in key requests.

            - *(string) --*
    """


_ClientDescribeOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientDescribeOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientDescribeOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseDashPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientDescribeOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseDashPackageEncryptionTypeDef(
    _ClientDescribeOriginEndpointResponseDashPackageEncryptionTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseDashPackageStreamSelectionTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseDashPackageStreamSelectionTypeDef(
    _ClientDescribeOriginEndpointResponseDashPackageStreamSelectionTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseDashPackageTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientDescribeOriginEndpointResponseDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientDescribeOriginEndpointResponseDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseDashPackageTypeDef(
    _ClientDescribeOriginEndpointResponseDashPackageTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientDescribeOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientDescribeOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientDescribeOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseHlsPackageEncryptionTypeDef(
    _ClientDescribeOriginEndpointResponseHlsPackageEncryptionTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseHlsPackageStreamSelectionTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseHlsPackageStreamSelectionTypeDef(
    _ClientDescribeOriginEndpointResponseHlsPackageStreamSelectionTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseHlsPackageTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientDescribeOriginEndpointResponseHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientDescribeOriginEndpointResponseHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseHlsPackageTypeDef(
    _ClientDescribeOriginEndpointResponseHlsPackageTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientDescribeOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientDescribeOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseMssPackageEncryptionTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientDescribeOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseMssPackageEncryptionTypeDef(
    _ClientDescribeOriginEndpointResponseMssPackageEncryptionTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseMssPackageStreamSelectionTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseMssPackageStreamSelectionTypeDef(
    _ClientDescribeOriginEndpointResponseMssPackageStreamSelectionTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseMssPackageTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseMssPackageTypeDef",
    {
        "Encryption": ClientDescribeOriginEndpointResponseMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientDescribeOriginEndpointResponseMssPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseMssPackageTypeDef(
    _ClientDescribeOriginEndpointResponseMssPackageTypeDef
):
    pass


_ClientDescribeOriginEndpointResponseTypeDef = TypedDict(
    "_ClientDescribeOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CmafPackage": ClientDescribeOriginEndpointResponseCmafPackageTypeDef,
        "DashPackage": ClientDescribeOriginEndpointResponseDashPackageTypeDef,
        "Description": str,
        "HlsPackage": ClientDescribeOriginEndpointResponseHlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": ClientDescribeOriginEndpointResponseMssPackageTypeDef,
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)


class ClientDescribeOriginEndpointResponseTypeDef(_ClientDescribeOriginEndpointResponseTypeDef):
    """
    - *(dict) --*An OriginEndpoint record.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
      - **ChannelId** *(string) --*The ID of the Channel the OriginEndpoint is associated with.
      - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging configuration.

        - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption
        configuration.

          - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption
          key rotation.
          - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
          Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

            - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
            certificate that MediaPackage will use for enforcing secure end-to-end data transfer
            with the key provider service.
            - **ResourceId** *(string) --*The resource ID to include in key requests.
            - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
            Elemental MediaPackage will assume when accessing the key provider service.
            - **SystemIds** *(list) --*The system IDs to include in key requests.

              - *(string) --*
    """


_ClientListChannelsResponseChannelsHlsIngestIngestEndpointsTypeDef = TypedDict(
    "_ClientListChannelsResponseChannelsHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)


class ClientListChannelsResponseChannelsHlsIngestIngestEndpointsTypeDef(
    _ClientListChannelsResponseChannelsHlsIngestIngestEndpointsTypeDef
):
    """
    - *(dict) --*An endpoint for ingesting source content for a Channel.

      - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
      - **Password** *(string) --*The system generated password for ingest authentication.
      - **Url** *(string) --*The ingest URL to which the source stream should be sent.
      - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientListChannelsResponseChannelsHlsIngestTypeDef = TypedDict(
    "_ClientListChannelsResponseChannelsHlsIngestTypeDef",
    {"IngestEndpoints": List[ClientListChannelsResponseChannelsHlsIngestIngestEndpointsTypeDef]},
    total=False,
)


class ClientListChannelsResponseChannelsHlsIngestTypeDef(
    _ClientListChannelsResponseChannelsHlsIngestTypeDef
):
    """
    - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

      - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
      sent.

        - *(dict) --*An endpoint for ingesting source content for a Channel.

          - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
          - **Password** *(string) --*The system generated password for ingest authentication.
          - **Url** *(string) --*The ingest URL to which the source stream should be sent.
          - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientListChannelsResponseChannelsTypeDef = TypedDict(
    "_ClientListChannelsResponseChannelsTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientListChannelsResponseChannelsHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListChannelsResponseChannelsTypeDef(_ClientListChannelsResponseChannelsTypeDef):
    """
    - *(dict) --*A Channel resource configuration.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the Channel.
      - **Description** *(string) --*A short text description of the Channel.
      - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

        - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
        sent.

          - *(dict) --*An endpoint for ingesting source content for a Channel.

            - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
            - **Password** *(string) --*The system generated password for ingest authentication.
            - **Url** *(string) --*The ingest URL to which the source stream should be sent.
            - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientListChannelsResponseTypeDef = TypedDict(
    "_ClientListChannelsResponseTypeDef",
    {"Channels": List[ClientListChannelsResponseChannelsTypeDef], "NextToken": str},
    total=False,
)


class ClientListChannelsResponseTypeDef(_ClientListChannelsResponseTypeDef):
    """
    - *(dict) --*A collection of Channel records.

      - **Channels** *(list) --*A list of Channel records.

        - *(dict) --*A Channel resource configuration.

          - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the Channel.
          - **Description** *(string) --*A short text description of the Channel.
          - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

            - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should
            be sent.

              - *(dict) --*An endpoint for ingesting source content for a Channel.

                - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
                - **Password** *(string) --*The system generated password for ingest authentication.
                - **Url** *(string) --*The ingest URL to which the source stream should be sent.
                - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientListHarvestJobsResponseHarvestJobsS3DestinationTypeDef = TypedDict(
    "_ClientListHarvestJobsResponseHarvestJobsS3DestinationTypeDef",
    {"BucketName": str, "ManifestKey": str, "RoleArn": str},
    total=False,
)


class ClientListHarvestJobsResponseHarvestJobsS3DestinationTypeDef(
    _ClientListHarvestJobsResponseHarvestJobsS3DestinationTypeDef
):
    """
    - **S3Destination** *(dict) --*Configuration parameters for where in an S3 bucket to place the
    harvested content

      - **BucketName** *(string) --*The name of an S3 bucket within which harvested content will be
      exported
      - **ManifestKey** *(string) --*The key in the specified S3 bucket where the harvested
      top-level manifest will be placed.
      - **RoleArn** *(string) --*The IAM role used to write to the specified S3 bucket
    """


_ClientListHarvestJobsResponseHarvestJobsTypeDef = TypedDict(
    "_ClientListHarvestJobsResponseHarvestJobsTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": ClientListHarvestJobsResponseHarvestJobsS3DestinationTypeDef,
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)


class ClientListHarvestJobsResponseHarvestJobsTypeDef(
    _ClientListHarvestJobsResponseHarvestJobsTypeDef
):
    """
    - *(dict) --*A HarvestJob resource configuration

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the HarvestJob.
      - **ChannelId** *(string) --*The ID of the Channel that the HarvestJob will harvest from.
      - **CreatedAt** *(string) --*The time the HarvestJob was submitted
      - **EndTime** *(string) --*The end of the time-window which will be harvested.
      - **Id** *(string) --*The ID of the HarvestJob. The ID must be unique within the region and it
      cannot be changed after the HarvestJob is submitted.
      - **OriginEndpointId** *(string) --*The ID of the OriginEndpoint that the HarvestJob will
      harvest from. This cannot be changed after the HarvestJob is submitted.
      - **S3Destination** *(dict) --*Configuration parameters for where in an S3 bucket to place the
      harvested content

        - **BucketName** *(string) --*The name of an S3 bucket within which harvested content will
        be exported
        - **ManifestKey** *(string) --*The key in the specified S3 bucket where the harvested
        top-level manifest will be placed.
        - **RoleArn** *(string) --*The IAM role used to write to the specified S3 bucket
    """


_ClientListHarvestJobsResponseTypeDef = TypedDict(
    "_ClientListHarvestJobsResponseTypeDef",
    {"HarvestJobs": List[ClientListHarvestJobsResponseHarvestJobsTypeDef], "NextToken": str},
    total=False,
)


class ClientListHarvestJobsResponseTypeDef(_ClientListHarvestJobsResponseTypeDef):
    """
    - *(dict) --*A collection of HarvestJob records.

      - **HarvestJobs** *(list) --*A list of HarvestJob records.

        - *(dict) --*A HarvestJob resource configuration

          - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the HarvestJob.
          - **ChannelId** *(string) --*The ID of the Channel that the HarvestJob will harvest from.
          - **CreatedAt** *(string) --*The time the HarvestJob was submitted
          - **EndTime** *(string) --*The end of the time-window which will be harvested.
          - **Id** *(string) --*The ID of the HarvestJob. The ID must be unique within the region
          and it cannot be changed after the HarvestJob is submitted.
          - **OriginEndpointId** *(string) --*The ID of the OriginEndpoint that the HarvestJob will
          harvest from. This cannot be changed after the HarvestJob is submitted.
          - **S3Destination** *(dict) --*Configuration parameters for where in an S3 bucket to place
          the harvested content

            - **BucketName** *(string) --*The name of an S3 bucket within which harvested content
            will be exported
            - **ManifestKey** *(string) --*The key in the specified S3 bucket where the harvested
            top-level manifest will be placed.
            - **RoleArn** *(string) --*The IAM role used to write to the specified S3 bucket
    """


_ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef
):
    """
    - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager and
    Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
      certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the
      key provider service.
      - **ResourceId** *(string) --*The resource ID to include in key requests.
      - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
      MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --*The system IDs to include in key requests.

        - *(string) --*
    """


_ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

      - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
      rotation.
      - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
      and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --*The resource ID to include in key requests.
        - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
        MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --*The system IDs to include in key requests.

          - *(string) --*
    """


_ClientListOriginEndpointsResponseOriginEndpointsCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsCmafPackageHlsManifestsTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsCmafPackageHlsManifestsTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsCmafPackageStreamSelectionTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsCmafPackageStreamSelectionTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsCmafPackageStreamSelectionTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsCmafPackageTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsCmafPackageTypeDef",
    {
        "Encryption": ClientListOriginEndpointsResponseOriginEndpointsCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ClientListOriginEndpointsResponseOriginEndpointsCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientListOriginEndpointsResponseOriginEndpointsCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsCmafPackageTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsCmafPackageTypeDef
):
    """
    - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging configuration.

      - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

        - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
        rotation.
        - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
        and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

          - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
          certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
          the key provider service.
          - **ResourceId** *(string) --*The resource ID to include in key requests.
          - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
          MediaPackage will assume when accessing the key provider service.
          - **SystemIds** *(list) --*The system IDs to include in key requests.

            - *(string) --*
    """


_ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsDashPackageStreamSelectionTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsDashPackageStreamSelectionTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsDashPackageStreamSelectionTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsDashPackageTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientListOriginEndpointsResponseOriginEndpointsDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientListOriginEndpointsResponseOriginEndpointsDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsDashPackageTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsDashPackageTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsHlsPackageStreamSelectionTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsHlsPackageStreamSelectionTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsHlsPackageStreamSelectionTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsHlsPackageTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientListOriginEndpointsResponseOriginEndpointsHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientListOriginEndpointsResponseOriginEndpointsHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsHlsPackageTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsHlsPackageTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsMssPackageStreamSelectionTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsMssPackageStreamSelectionTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsMssPackageStreamSelectionTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsMssPackageTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsMssPackageTypeDef",
    {
        "Encryption": ClientListOriginEndpointsResponseOriginEndpointsMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientListOriginEndpointsResponseOriginEndpointsMssPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsMssPackageTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsMssPackageTypeDef
):
    pass


_ClientListOriginEndpointsResponseOriginEndpointsTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseOriginEndpointsTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CmafPackage": ClientListOriginEndpointsResponseOriginEndpointsCmafPackageTypeDef,
        "DashPackage": ClientListOriginEndpointsResponseOriginEndpointsDashPackageTypeDef,
        "Description": str,
        "HlsPackage": ClientListOriginEndpointsResponseOriginEndpointsHlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": ClientListOriginEndpointsResponseOriginEndpointsMssPackageTypeDef,
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)


class ClientListOriginEndpointsResponseOriginEndpointsTypeDef(
    _ClientListOriginEndpointsResponseOriginEndpointsTypeDef
):
    """
    - *(dict) --*An OriginEndpoint resource configuration.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
      - **ChannelId** *(string) --*The ID of the Channel the OriginEndpoint is associated with.
      - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging configuration.

        - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption
        configuration.

          - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption
          key rotation.
          - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
          Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

            - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
            certificate that MediaPackage will use for enforcing secure end-to-end data transfer
            with the key provider service.
            - **ResourceId** *(string) --*The resource ID to include in key requests.
            - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
            Elemental MediaPackage will assume when accessing the key provider service.
            - **SystemIds** *(list) --*The system IDs to include in key requests.

              - *(string) --*
    """


_ClientListOriginEndpointsResponseTypeDef = TypedDict(
    "_ClientListOriginEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "OriginEndpoints": List[ClientListOriginEndpointsResponseOriginEndpointsTypeDef],
    },
    total=False,
)


class ClientListOriginEndpointsResponseTypeDef(_ClientListOriginEndpointsResponseTypeDef):
    """
    - *(dict) --*A collection of OriginEndpoint records.

      - **NextToken** *(string) --*A token that can be used to resume pagination from the end of the
      collection.
      - **OriginEndpoints** *(list) --*A list of OriginEndpoint records.

        - *(dict) --*An OriginEndpoint resource configuration.

          - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
          - **ChannelId** *(string) --*The ID of the Channel the OriginEndpoint is associated with.
          - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging
          configuration.

            - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption
            configuration.

              - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each
              encryption key rotation.
              - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
              Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

                - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate
                Manager certificate that MediaPackage will use for enforcing secure end-to-end data
                transfer with the key provider service.
                - **ResourceId** *(string) --*The resource ID to include in key requests.
                - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
                Elemental MediaPackage will assume when accessing the key provider service.
                - **SystemIds** *(list) --*The system IDs to include in key requests.

                  - *(string) --*
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*200 response

      - **Tags** *(dict) --*

        - *(string) --*

          - *(string) --*
    """


_ClientRotateChannelCredentialsResponseHlsIngestIngestEndpointsTypeDef = TypedDict(
    "_ClientRotateChannelCredentialsResponseHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)


class ClientRotateChannelCredentialsResponseHlsIngestIngestEndpointsTypeDef(
    _ClientRotateChannelCredentialsResponseHlsIngestIngestEndpointsTypeDef
):
    """
    - *(dict) --*An endpoint for ingesting source content for a Channel.

      - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
      - **Password** *(string) --*The system generated password for ingest authentication.
      - **Url** *(string) --*The ingest URL to which the source stream should be sent.
      - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientRotateChannelCredentialsResponseHlsIngestTypeDef = TypedDict(
    "_ClientRotateChannelCredentialsResponseHlsIngestTypeDef",
    {
        "IngestEndpoints": List[
            ClientRotateChannelCredentialsResponseHlsIngestIngestEndpointsTypeDef
        ]
    },
    total=False,
)


class ClientRotateChannelCredentialsResponseHlsIngestTypeDef(
    _ClientRotateChannelCredentialsResponseHlsIngestTypeDef
):
    """
    - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

      - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
      sent.

        - *(dict) --*An endpoint for ingesting source content for a Channel.

          - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
          - **Password** *(string) --*The system generated password for ingest authentication.
          - **Url** *(string) --*The ingest URL to which the source stream should be sent.
          - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientRotateChannelCredentialsResponseTypeDef = TypedDict(
    "_ClientRotateChannelCredentialsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientRotateChannelCredentialsResponseHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientRotateChannelCredentialsResponseTypeDef(_ClientRotateChannelCredentialsResponseTypeDef):
    """
    - *(dict) --*The updated Channel record.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the Channel.
      - **Description** *(string) --*A short text description of the Channel.
      - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

        - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
        sent.

          - *(dict) --*An endpoint for ingesting source content for a Channel.

            - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
            - **Password** *(string) --*The system generated password for ingest authentication.
            - **Url** *(string) --*The ingest URL to which the source stream should be sent.
            - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientRotateIngestEndpointCredentialsResponseHlsIngestIngestEndpointsTypeDef = TypedDict(
    "_ClientRotateIngestEndpointCredentialsResponseHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)


class ClientRotateIngestEndpointCredentialsResponseHlsIngestIngestEndpointsTypeDef(
    _ClientRotateIngestEndpointCredentialsResponseHlsIngestIngestEndpointsTypeDef
):
    """
    - *(dict) --*An endpoint for ingesting source content for a Channel.

      - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
      - **Password** *(string) --*The system generated password for ingest authentication.
      - **Url** *(string) --*The ingest URL to which the source stream should be sent.
      - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientRotateIngestEndpointCredentialsResponseHlsIngestTypeDef = TypedDict(
    "_ClientRotateIngestEndpointCredentialsResponseHlsIngestTypeDef",
    {
        "IngestEndpoints": List[
            ClientRotateIngestEndpointCredentialsResponseHlsIngestIngestEndpointsTypeDef
        ]
    },
    total=False,
)


class ClientRotateIngestEndpointCredentialsResponseHlsIngestTypeDef(
    _ClientRotateIngestEndpointCredentialsResponseHlsIngestTypeDef
):
    """
    - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

      - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
      sent.

        - *(dict) --*An endpoint for ingesting source content for a Channel.

          - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
          - **Password** *(string) --*The system generated password for ingest authentication.
          - **Url** *(string) --*The ingest URL to which the source stream should be sent.
          - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientRotateIngestEndpointCredentialsResponseTypeDef = TypedDict(
    "_ClientRotateIngestEndpointCredentialsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientRotateIngestEndpointCredentialsResponseHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientRotateIngestEndpointCredentialsResponseTypeDef(
    _ClientRotateIngestEndpointCredentialsResponseTypeDef
):
    """
    - *(dict) --*The updated Channel record.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the Channel.
      - **Description** *(string) --*A short text description of the Channel.
      - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

        - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
        sent.

          - *(dict) --*An endpoint for ingesting source content for a Channel.

            - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
            - **Password** *(string) --*The system generated password for ingest authentication.
            - **Url** *(string) --*The ingest URL to which the source stream should be sent.
            - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientUpdateChannelResponseHlsIngestIngestEndpointsTypeDef = TypedDict(
    "_ClientUpdateChannelResponseHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)


class ClientUpdateChannelResponseHlsIngestIngestEndpointsTypeDef(
    _ClientUpdateChannelResponseHlsIngestIngestEndpointsTypeDef
):
    """
    - *(dict) --*An endpoint for ingesting source content for a Channel.

      - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
      - **Password** *(string) --*The system generated password for ingest authentication.
      - **Url** *(string) --*The ingest URL to which the source stream should be sent.
      - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientUpdateChannelResponseHlsIngestTypeDef = TypedDict(
    "_ClientUpdateChannelResponseHlsIngestTypeDef",
    {"IngestEndpoints": List[ClientUpdateChannelResponseHlsIngestIngestEndpointsTypeDef]},
    total=False,
)


class ClientUpdateChannelResponseHlsIngestTypeDef(_ClientUpdateChannelResponseHlsIngestTypeDef):
    """
    - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

      - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
      sent.

        - *(dict) --*An endpoint for ingesting source content for a Channel.

          - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
          - **Password** *(string) --*The system generated password for ingest authentication.
          - **Url** *(string) --*The ingest URL to which the source stream should be sent.
          - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ClientUpdateChannelResponseTypeDef = TypedDict(
    "_ClientUpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ClientUpdateChannelResponseHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientUpdateChannelResponseTypeDef(_ClientUpdateChannelResponseTypeDef):
    """
    - *(dict) --*The updated Channel record.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the Channel.
      - **Description** *(string) --*A short text description of the Channel.
      - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

        - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
        sent.

          - *(dict) --*An endpoint for ingesting source content for a Channel.

            - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
            - **Password** *(string) --*The system generated password for ingest authentication.
            - **Url** *(string) --*The ingest URL to which the source stream should be sent.
            - **Username** *(string) --*The system generated username for ingest authentication.
    """


_RequiredClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"ResourceId": str, "RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "Url": str},
    total=False,
)


class ClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef,
):
    """
    - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
    Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
      certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the
      key provider service.
      - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
      - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
      AWS Elemental MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

        - *(string) --*
    """


_RequiredClientUpdateOriginEndpointCmafPackageEncryptionTypeDef = TypedDict(
    "_RequiredClientUpdateOriginEndpointCmafPackageEncryptionTypeDef",
    {"SpekeKeyProvider": ClientUpdateOriginEndpointCmafPackageEncryptionSpekeKeyProviderTypeDef},
)
_OptionalClientUpdateOriginEndpointCmafPackageEncryptionTypeDef = TypedDict(
    "_OptionalClientUpdateOriginEndpointCmafPackageEncryptionTypeDef",
    {"KeyRotationIntervalSeconds": int},
    total=False,
)


class ClientUpdateOriginEndpointCmafPackageEncryptionTypeDef(
    _RequiredClientUpdateOriginEndpointCmafPackageEncryptionTypeDef,
    _OptionalClientUpdateOriginEndpointCmafPackageEncryptionTypeDef,
):
    """
    - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

      - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
      rotation.
      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientUpdateOriginEndpointCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
    },
    total=False,
)


class ClientUpdateOriginEndpointCmafPackageHlsManifestsTypeDef(
    _ClientUpdateOriginEndpointCmafPackageHlsManifestsTypeDef
):
    pass


_ClientUpdateOriginEndpointCmafPackageStreamSelectionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientUpdateOriginEndpointCmafPackageStreamSelectionTypeDef(
    _ClientUpdateOriginEndpointCmafPackageStreamSelectionTypeDef
):
    pass


_ClientUpdateOriginEndpointCmafPackageTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointCmafPackageTypeDef",
    {
        "Encryption": ClientUpdateOriginEndpointCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientUpdateOriginEndpointCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientUpdateOriginEndpointCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientUpdateOriginEndpointCmafPackageTypeDef(_ClientUpdateOriginEndpointCmafPackageTypeDef):
    """
    - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

      - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
      rotation.
      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientUpdateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientUpdateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientUpdateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientUpdateOriginEndpointDashPackageEncryptionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientUpdateOriginEndpointDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientUpdateOriginEndpointDashPackageEncryptionTypeDef(
    _ClientUpdateOriginEndpointDashPackageEncryptionTypeDef
):
    pass


_ClientUpdateOriginEndpointDashPackageStreamSelectionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientUpdateOriginEndpointDashPackageStreamSelectionTypeDef(
    _ClientUpdateOriginEndpointDashPackageStreamSelectionTypeDef
):
    pass


_ClientUpdateOriginEndpointDashPackageTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientUpdateOriginEndpointDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientUpdateOriginEndpointDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)


class ClientUpdateOriginEndpointDashPackageTypeDef(_ClientUpdateOriginEndpointDashPackageTypeDef):
    """
    - **AdTriggers** *(list) --*A list of SCTE-35 message types that are treated as ad markers in
    the output. If empty, no ad markers are output. Specify multiple items to create ad markers for
    all of the included message types.

      - *(string) --*
    """


_ClientUpdateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientUpdateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientUpdateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientUpdateOriginEndpointHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientUpdateOriginEndpointHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientUpdateOriginEndpointHlsPackageEncryptionTypeDef(
    _ClientUpdateOriginEndpointHlsPackageEncryptionTypeDef
):
    pass


_ClientUpdateOriginEndpointHlsPackageStreamSelectionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientUpdateOriginEndpointHlsPackageStreamSelectionTypeDef(
    _ClientUpdateOriginEndpointHlsPackageStreamSelectionTypeDef
):
    pass


_ClientUpdateOriginEndpointHlsPackageTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientUpdateOriginEndpointHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientUpdateOriginEndpointHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ClientUpdateOriginEndpointHlsPackageTypeDef(_ClientUpdateOriginEndpointHlsPackageTypeDef):
    """
    - **AdMarkers** *(string) --*This setting controls how ad markers are included in the packaged
    OriginEndpoint. "NONE" will omit all SCTE-35 ad markers from the output. "PASSTHROUGH" causes
    the manifest to contain a copy of the SCTE-35 ad markers (comments) taken directly from the
    input HTTP Live Streaming (HLS) manifest. "SCTE35_ENHANCED" generates ad markers and blackout
    tags based on SCTE-35 messages in the input source.
    - **AdTriggers** *(list) --*A list of SCTE-35 message types that are treated as ad markers in
    the output. If empty, no ad markers are output. Specify multiple items to create ad markers for
    all of the included message types.

      - *(string) --*
    """


_RequiredClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"ResourceId": str, "RoleArn": str, "SystemIds": List[str]},
)
_OptionalClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "Url": str},
    total=False,
)


class ClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef(
    _RequiredClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef,
    _OptionalClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef,
):
    """
    - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
    Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
      certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the
      key provider service.
      - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
      - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
      AWS Elemental MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

        - *(string) --*
    """


_ClientUpdateOriginEndpointMssPackageEncryptionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointMssPackageEncryptionTypeDef",
    {"SpekeKeyProvider": ClientUpdateOriginEndpointMssPackageEncryptionSpekeKeyProviderTypeDef},
)


class ClientUpdateOriginEndpointMssPackageEncryptionTypeDef(
    _ClientUpdateOriginEndpointMssPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A Microsoft Smooth Streaming (MSS) encryption configuration.

      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientUpdateOriginEndpointMssPackageStreamSelectionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientUpdateOriginEndpointMssPackageStreamSelectionTypeDef(
    _ClientUpdateOriginEndpointMssPackageStreamSelectionTypeDef
):
    pass


_ClientUpdateOriginEndpointMssPackageTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointMssPackageTypeDef",
    {
        "Encryption": ClientUpdateOriginEndpointMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientUpdateOriginEndpointMssPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientUpdateOriginEndpointMssPackageTypeDef(_ClientUpdateOriginEndpointMssPackageTypeDef):
    """
    - **Encryption** *(dict) --*A Microsoft Smooth Streaming (MSS) encryption configuration.

      - **SpekeKeyProvider** *(dict) --***[REQUIRED]** A configuration for accessing an external
      Secure Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --***[REQUIRED]** The resource ID to include in key requests.
        - **RoleArn** *(string) --***[REQUIRED]** An Amazon Resource Name (ARN) of an IAM role that
        AWS Elemental MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --***[REQUIRED]** The system IDs to include in key requests.

          - *(string) --*
    """


_ClientUpdateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientUpdateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientUpdateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef
):
    """
    - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager and
    Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
      certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the
      key provider service.
      - **ResourceId** *(string) --*The resource ID to include in key requests.
      - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
      MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --*The system IDs to include in key requests.

        - *(string) --*
    """


_ClientUpdateOriginEndpointResponseCmafPackageEncryptionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseCmafPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientUpdateOriginEndpointResponseCmafPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseCmafPackageEncryptionTypeDef(
    _ClientUpdateOriginEndpointResponseCmafPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

      - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
      rotation.
      - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
      and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --*The resource ID to include in key requests.
        - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
        MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --*The system IDs to include in key requests.

          - *(string) --*
    """


_ClientUpdateOriginEndpointResponseCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseCmafPackageHlsManifestsTypeDef(
    _ClientUpdateOriginEndpointResponseCmafPackageHlsManifestsTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseCmafPackageStreamSelectionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseCmafPackageStreamSelectionTypeDef(
    _ClientUpdateOriginEndpointResponseCmafPackageStreamSelectionTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseCmafPackageTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseCmafPackageTypeDef",
    {
        "Encryption": ClientUpdateOriginEndpointResponseCmafPackageEncryptionTypeDef,
        "HlsManifests": List[ClientUpdateOriginEndpointResponseCmafPackageHlsManifestsTypeDef],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ClientUpdateOriginEndpointResponseCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseCmafPackageTypeDef(
    _ClientUpdateOriginEndpointResponseCmafPackageTypeDef
):
    """
    - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging configuration.

      - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

        - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
        rotation.
        - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
        and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

          - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
          certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
          the key provider service.
          - **ResourceId** *(string) --*The resource ID to include in key requests.
          - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
          MediaPackage will assume when accessing the key provider service.
          - **SystemIds** *(list) --*The system IDs to include in key requests.

            - *(string) --*
    """


_ClientUpdateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientUpdateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientUpdateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseDashPackageEncryptionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ClientUpdateOriginEndpointResponseDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseDashPackageEncryptionTypeDef(
    _ClientUpdateOriginEndpointResponseDashPackageEncryptionTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseDashPackageStreamSelectionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseDashPackageStreamSelectionTypeDef(
    _ClientUpdateOriginEndpointResponseDashPackageStreamSelectionTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseDashPackageTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientUpdateOriginEndpointResponseDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ClientUpdateOriginEndpointResponseDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseDashPackageTypeDef(
    _ClientUpdateOriginEndpointResponseDashPackageTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientUpdateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientUpdateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseHlsPackageEncryptionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ClientUpdateOriginEndpointResponseHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseHlsPackageEncryptionTypeDef(
    _ClientUpdateOriginEndpointResponseHlsPackageEncryptionTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseHlsPackageStreamSelectionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseHlsPackageStreamSelectionTypeDef(
    _ClientUpdateOriginEndpointResponseHlsPackageStreamSelectionTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseHlsPackageTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ClientUpdateOriginEndpointResponseHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientUpdateOriginEndpointResponseHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseHlsPackageTypeDef(
    _ClientUpdateOriginEndpointResponseHlsPackageTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ClientUpdateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef(
    _ClientUpdateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseMssPackageEncryptionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ClientUpdateOriginEndpointResponseMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseMssPackageEncryptionTypeDef(
    _ClientUpdateOriginEndpointResponseMssPackageEncryptionTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseMssPackageStreamSelectionTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseMssPackageStreamSelectionTypeDef(
    _ClientUpdateOriginEndpointResponseMssPackageStreamSelectionTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseMssPackageTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseMssPackageTypeDef",
    {
        "Encryption": ClientUpdateOriginEndpointResponseMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ClientUpdateOriginEndpointResponseMssPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseMssPackageTypeDef(
    _ClientUpdateOriginEndpointResponseMssPackageTypeDef
):
    pass


_ClientUpdateOriginEndpointResponseTypeDef = TypedDict(
    "_ClientUpdateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CmafPackage": ClientUpdateOriginEndpointResponseCmafPackageTypeDef,
        "DashPackage": ClientUpdateOriginEndpointResponseDashPackageTypeDef,
        "Description": str,
        "HlsPackage": ClientUpdateOriginEndpointResponseHlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": ClientUpdateOriginEndpointResponseMssPackageTypeDef,
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)


class ClientUpdateOriginEndpointResponseTypeDef(_ClientUpdateOriginEndpointResponseTypeDef):
    """
    - *(dict) --*An updated OriginEndpoint record.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
      - **ChannelId** *(string) --*The ID of the Channel the OriginEndpoint is associated with.
      - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging configuration.

        - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption
        configuration.

          - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption
          key rotation.
          - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
          Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

            - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
            certificate that MediaPackage will use for enforcing secure end-to-end data transfer
            with the key provider service.
            - **ResourceId** *(string) --*The resource ID to include in key requests.
            - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
            Elemental MediaPackage will assume when accessing the key provider service.
            - **SystemIds** *(list) --*The system IDs to include in key requests.

              - *(string) --*
    """


_ListChannelsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListChannelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListChannelsPaginatePaginationConfigTypeDef(_ListChannelsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListChannelsPaginateResponseChannelsHlsIngestIngestEndpointsTypeDef = TypedDict(
    "_ListChannelsPaginateResponseChannelsHlsIngestIngestEndpointsTypeDef",
    {"Id": str, "Password": str, "Url": str, "Username": str},
    total=False,
)


class ListChannelsPaginateResponseChannelsHlsIngestIngestEndpointsTypeDef(
    _ListChannelsPaginateResponseChannelsHlsIngestIngestEndpointsTypeDef
):
    """
    - *(dict) --*An endpoint for ingesting source content for a Channel.

      - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
      - **Password** *(string) --*The system generated password for ingest authentication.
      - **Url** *(string) --*The ingest URL to which the source stream should be sent.
      - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ListChannelsPaginateResponseChannelsHlsIngestTypeDef = TypedDict(
    "_ListChannelsPaginateResponseChannelsHlsIngestTypeDef",
    {"IngestEndpoints": List[ListChannelsPaginateResponseChannelsHlsIngestIngestEndpointsTypeDef]},
    total=False,
)


class ListChannelsPaginateResponseChannelsHlsIngestTypeDef(
    _ListChannelsPaginateResponseChannelsHlsIngestTypeDef
):
    """
    - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

      - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
      sent.

        - *(dict) --*An endpoint for ingesting source content for a Channel.

          - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
          - **Password** *(string) --*The system generated password for ingest authentication.
          - **Url** *(string) --*The ingest URL to which the source stream should be sent.
          - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ListChannelsPaginateResponseChannelsTypeDef = TypedDict(
    "_ListChannelsPaginateResponseChannelsTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": ListChannelsPaginateResponseChannelsHlsIngestTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListChannelsPaginateResponseChannelsTypeDef(_ListChannelsPaginateResponseChannelsTypeDef):
    """
    - *(dict) --*A Channel resource configuration.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the Channel.
      - **Description** *(string) --*A short text description of the Channel.
      - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

        - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should be
        sent.

          - *(dict) --*An endpoint for ingesting source content for a Channel.

            - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
            - **Password** *(string) --*The system generated password for ingest authentication.
            - **Url** *(string) --*The ingest URL to which the source stream should be sent.
            - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ListChannelsPaginateResponseTypeDef = TypedDict(
    "_ListChannelsPaginateResponseTypeDef",
    {"Channels": List[ListChannelsPaginateResponseChannelsTypeDef]},
    total=False,
)


class ListChannelsPaginateResponseTypeDef(_ListChannelsPaginateResponseTypeDef):
    """
    - *(dict) --*A collection of Channel records.

      - **Channels** *(list) --*A list of Channel records.

        - *(dict) --*A Channel resource configuration.

          - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the Channel.
          - **Description** *(string) --*A short text description of the Channel.
          - **HlsIngest** *(dict) --*An HTTP Live Streaming (HLS) ingest resource configuration.

            - **IngestEndpoints** *(list) --*A list of endpoints to which the source stream should
            be sent.

              - *(dict) --*An endpoint for ingesting source content for a Channel.

                - **Id** *(string) --*The system generated unique identifier for the IngestEndpoint
                - **Password** *(string) --*The system generated password for ingest authentication.
                - **Url** *(string) --*The ingest URL to which the source stream should be sent.
                - **Username** *(string) --*The system generated username for ingest authentication.
    """


_ListHarvestJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHarvestJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHarvestJobsPaginatePaginationConfigTypeDef(
    _ListHarvestJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListHarvestJobsPaginateResponseHarvestJobsS3DestinationTypeDef = TypedDict(
    "_ListHarvestJobsPaginateResponseHarvestJobsS3DestinationTypeDef",
    {"BucketName": str, "ManifestKey": str, "RoleArn": str},
    total=False,
)


class ListHarvestJobsPaginateResponseHarvestJobsS3DestinationTypeDef(
    _ListHarvestJobsPaginateResponseHarvestJobsS3DestinationTypeDef
):
    """
    - **S3Destination** *(dict) --*Configuration parameters for where in an S3 bucket to place the
    harvested content

      - **BucketName** *(string) --*The name of an S3 bucket within which harvested content will be
      exported
      - **ManifestKey** *(string) --*The key in the specified S3 bucket where the harvested
      top-level manifest will be placed.
      - **RoleArn** *(string) --*The IAM role used to write to the specified S3 bucket
    """


_ListHarvestJobsPaginateResponseHarvestJobsTypeDef = TypedDict(
    "_ListHarvestJobsPaginateResponseHarvestJobsTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": ListHarvestJobsPaginateResponseHarvestJobsS3DestinationTypeDef,
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)


class ListHarvestJobsPaginateResponseHarvestJobsTypeDef(
    _ListHarvestJobsPaginateResponseHarvestJobsTypeDef
):
    """
    - *(dict) --*A HarvestJob resource configuration

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the HarvestJob.
      - **ChannelId** *(string) --*The ID of the Channel that the HarvestJob will harvest from.
      - **CreatedAt** *(string) --*The time the HarvestJob was submitted
      - **EndTime** *(string) --*The end of the time-window which will be harvested.
      - **Id** *(string) --*The ID of the HarvestJob. The ID must be unique within the region and it
      cannot be changed after the HarvestJob is submitted.
      - **OriginEndpointId** *(string) --*The ID of the OriginEndpoint that the HarvestJob will
      harvest from. This cannot be changed after the HarvestJob is submitted.
      - **S3Destination** *(dict) --*Configuration parameters for where in an S3 bucket to place the
      harvested content

        - **BucketName** *(string) --*The name of an S3 bucket within which harvested content will
        be exported
        - **ManifestKey** *(string) --*The key in the specified S3 bucket where the harvested
        top-level manifest will be placed.
        - **RoleArn** *(string) --*The IAM role used to write to the specified S3 bucket
    """


_ListHarvestJobsPaginateResponseTypeDef = TypedDict(
    "_ListHarvestJobsPaginateResponseTypeDef",
    {"HarvestJobs": List[ListHarvestJobsPaginateResponseHarvestJobsTypeDef]},
    total=False,
)


class ListHarvestJobsPaginateResponseTypeDef(_ListHarvestJobsPaginateResponseTypeDef):
    """
    - *(dict) --*A collection of HarvestJob records.

      - **HarvestJobs** *(list) --*A list of HarvestJob records.

        - *(dict) --*A HarvestJob resource configuration

          - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the HarvestJob.
          - **ChannelId** *(string) --*The ID of the Channel that the HarvestJob will harvest from.
          - **CreatedAt** *(string) --*The time the HarvestJob was submitted
          - **EndTime** *(string) --*The end of the time-window which will be harvested.
          - **Id** *(string) --*The ID of the HarvestJob. The ID must be unique within the region
          and it cannot be changed after the HarvestJob is submitted.
          - **OriginEndpointId** *(string) --*The ID of the OriginEndpoint that the HarvestJob will
          harvest from. This cannot be changed after the HarvestJob is submitted.
          - **S3Destination** *(dict) --*Configuration parameters for where in an S3 bucket to place
          the harvested content

            - **BucketName** *(string) --*The name of an S3 bucket within which harvested content
            will be exported
            - **ManifestKey** *(string) --*The key in the specified S3 bucket where the harvested
            top-level manifest will be placed.
            - **RoleArn** *(string) --*The IAM role used to write to the specified S3 bucket
    """


_ListOriginEndpointsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOriginEndpointsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOriginEndpointsPaginatePaginationConfigTypeDef(
    _ListOriginEndpointsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef
):
    """
    - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager and
    Encoder Key Exchange (SPEKE) service that will provide encryption keys.

      - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
      certificate that MediaPackage will use for enforcing secure end-to-end data transfer with the
      key provider service.
      - **ResourceId** *(string) --*The resource ID to include in key requests.
      - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
      MediaPackage will assume when accessing the key provider service.
      - **SystemIds** *(list) --*The system IDs to include in key requests.

        - *(string) --*
    """


_ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionTypeDef
):
    """
    - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

      - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
      rotation.
      - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
      and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

        - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
        certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
        the key provider service.
        - **ResourceId** *(string) --*The resource ID to include in key requests.
        - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
        MediaPackage will assume when accessing the key provider service.
        - **SystemIds** *(list) --*The system IDs to include in key requests.

          - *(string) --*
    """


_ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageHlsManifestsTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageHlsManifestsTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "Id": str,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageHlsManifestsTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageHlsManifestsTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageStreamSelectionTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageStreamSelectionTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageStreamSelectionTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageTypeDef",
    {
        "Encryption": ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageEncryptionTypeDef,
        "HlsManifests": List[
            ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageHlsManifestsTypeDef
        ],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageTypeDef
):
    """
    - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging configuration.

      - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption configuration.

        - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption key
        rotation.
        - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure Packager
        and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

          - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
          certificate that MediaPackage will use for enforcing secure end-to-end data transfer with
          the key provider service.
          - **ResourceId** *(string) --*The resource ID to include in key requests.
          - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS Elemental
          MediaPackage will assume when accessing the key provider service.
          - **SystemIds** *(list) --*The system IDs to include in key requests.

            - *(string) --*
    """


_ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
        "SpekeKeyProvider": ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageStreamSelectionTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageStreamSelectionTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageStreamSelectionTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageEncryptionTypeDef,
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[str],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageStreamSelectionTypeDef,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "SpekeKeyProvider": ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionSpekeKeyProviderTypeDef,
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageStreamSelectionTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageStreamSelectionTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageStreamSelectionTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageEncryptionTypeDef,
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageStreamSelectionTypeDef,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionTypeDef",
    {
        "SpekeKeyProvider": ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionSpekeKeyProviderTypeDef
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageStreamSelectionTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageStreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageStreamSelectionTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageStreamSelectionTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageTypeDef",
    {
        "Encryption": ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageEncryptionTypeDef,
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageStreamSelectionTypeDef,
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageTypeDef
):
    pass


_ListOriginEndpointsPaginateResponseOriginEndpointsTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseOriginEndpointsTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CmafPackage": ListOriginEndpointsPaginateResponseOriginEndpointsCmafPackageTypeDef,
        "DashPackage": ListOriginEndpointsPaginateResponseOriginEndpointsDashPackageTypeDef,
        "Description": str,
        "HlsPackage": ListOriginEndpointsPaginateResponseOriginEndpointsHlsPackageTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": ListOriginEndpointsPaginateResponseOriginEndpointsMssPackageTypeDef,
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)


class ListOriginEndpointsPaginateResponseOriginEndpointsTypeDef(
    _ListOriginEndpointsPaginateResponseOriginEndpointsTypeDef
):
    """
    - *(dict) --*An OriginEndpoint resource configuration.

      - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
      - **ChannelId** *(string) --*The ID of the Channel the OriginEndpoint is associated with.
      - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging configuration.

        - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption
        configuration.

          - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each encryption
          key rotation.
          - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
          Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

            - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate Manager
            certificate that MediaPackage will use for enforcing secure end-to-end data transfer
            with the key provider service.
            - **ResourceId** *(string) --*The resource ID to include in key requests.
            - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
            Elemental MediaPackage will assume when accessing the key provider service.
            - **SystemIds** *(list) --*The system IDs to include in key requests.

              - *(string) --*
    """


_ListOriginEndpointsPaginateResponseTypeDef = TypedDict(
    "_ListOriginEndpointsPaginateResponseTypeDef",
    {"OriginEndpoints": List[ListOriginEndpointsPaginateResponseOriginEndpointsTypeDef]},
    total=False,
)


class ListOriginEndpointsPaginateResponseTypeDef(_ListOriginEndpointsPaginateResponseTypeDef):
    """
    - *(dict) --*A collection of OriginEndpoint records.

      - **OriginEndpoints** *(list) --*A list of OriginEndpoint records.

        - *(dict) --*An OriginEndpoint resource configuration.

          - **Arn** *(string) --*The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
          - **ChannelId** *(string) --*The ID of the Channel the OriginEndpoint is associated with.
          - **CmafPackage** *(dict) --*A Common Media Application Format (CMAF) packaging
          configuration.

            - **Encryption** *(dict) --*A Common Media Application Format (CMAF) encryption
            configuration.

              - **KeyRotationIntervalSeconds** *(integer) --*Time (in seconds) between each
              encryption key rotation.
              - **SpekeKeyProvider** *(dict) --*A configuration for accessing an external Secure
              Packager and Encoder Key Exchange (SPEKE) service that will provide encryption keys.

                - **CertificateArn** *(string) --*An Amazon Resource Name (ARN) of a Certificate
                Manager certificate that MediaPackage will use for enforcing secure end-to-end data
                transfer with the key provider service.
                - **ResourceId** *(string) --*The resource ID to include in key requests.
                - **RoleArn** *(string) --*An Amazon Resource Name (ARN) of an IAM role that AWS
                Elemental MediaPackage will assume when accessing the key provider service.
                - **SystemIds** *(list) --*The system IDs to include in key requests.

                  - *(string) --*
    """
