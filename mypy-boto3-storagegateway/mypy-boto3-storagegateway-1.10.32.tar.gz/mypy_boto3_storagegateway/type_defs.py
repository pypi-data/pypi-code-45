"Main interface for storagegateway service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientActivateGatewayResponseTypeDef",
    "ClientActivateGatewayTagsTypeDef",
    "ClientAddCacheResponseTypeDef",
    "ClientAddTagsToResourceResponseTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientAddUploadBufferResponseTypeDef",
    "ClientAddWorkingStorageResponseTypeDef",
    "ClientAssignTapePoolResponseTypeDef",
    "ClientAttachVolumeResponseTypeDef",
    "ClientCancelArchivalResponseTypeDef",
    "ClientCancelRetrievalResponseTypeDef",
    "ClientCreateCachedIscsiVolumeResponseTypeDef",
    "ClientCreateCachedIscsiVolumeTagsTypeDef",
    "ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef",
    "ClientCreateNfsFileShareResponseTypeDef",
    "ClientCreateNfsFileShareTagsTypeDef",
    "ClientCreateSmbFileShareResponseTypeDef",
    "ClientCreateSmbFileShareTagsTypeDef",
    "ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef",
    "ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef",
    "ClientCreateSnapshotResponseTypeDef",
    "ClientCreateSnapshotTagsTypeDef",
    "ClientCreateStoredIscsiVolumeResponseTypeDef",
    "ClientCreateStoredIscsiVolumeTagsTypeDef",
    "ClientCreateTapeWithBarcodeResponseTypeDef",
    "ClientCreateTapeWithBarcodeTagsTypeDef",
    "ClientCreateTapesResponseTypeDef",
    "ClientCreateTapesTagsTypeDef",
    "ClientDeleteBandwidthRateLimitResponseTypeDef",
    "ClientDeleteChapCredentialsResponseTypeDef",
    "ClientDeleteFileShareResponseTypeDef",
    "ClientDeleteGatewayResponseTypeDef",
    "ClientDeleteSnapshotScheduleResponseTypeDef",
    "ClientDeleteTapeArchiveResponseTypeDef",
    "ClientDeleteTapeResponseTypeDef",
    "ClientDeleteVolumeResponseTypeDef",
    "ClientDescribeAvailabilityMonitorTestResponseTypeDef",
    "ClientDescribeBandwidthRateLimitResponseTypeDef",
    "ClientDescribeCacheResponseTypeDef",
    "ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    "ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef",
    "ClientDescribeCachedIscsiVolumesResponseTypeDef",
    "ClientDescribeChapCredentialsResponseChapCredentialsTypeDef",
    "ClientDescribeChapCredentialsResponseTypeDef",
    "ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef",
    "ClientDescribeGatewayInformationResponseTagsTypeDef",
    "ClientDescribeGatewayInformationResponseTypeDef",
    "ClientDescribeMaintenanceStartTimeResponseTypeDef",
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef",
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef",
    "ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef",
    "ClientDescribeNfsFileSharesResponseTypeDef",
    "ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef",
    "ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef",
    "ClientDescribeSmbFileSharesResponseTypeDef",
    "ClientDescribeSmbSettingsResponseTypeDef",
    "ClientDescribeSnapshotScheduleResponseTagsTypeDef",
    "ClientDescribeSnapshotScheduleResponseTypeDef",
    "ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    "ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef",
    "ClientDescribeStoredIscsiVolumesResponseTypeDef",
    "ClientDescribeTapeArchivesResponseTapeArchivesTypeDef",
    "ClientDescribeTapeArchivesResponseTypeDef",
    "ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef",
    "ClientDescribeTapeRecoveryPointsResponseTypeDef",
    "ClientDescribeTapesResponseTapesTypeDef",
    "ClientDescribeTapesResponseTypeDef",
    "ClientDescribeUploadBufferResponseTypeDef",
    "ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef",
    "ClientDescribeVtlDevicesResponseVTLDevicesTypeDef",
    "ClientDescribeVtlDevicesResponseTypeDef",
    "ClientDescribeWorkingStorageResponseTypeDef",
    "ClientDetachVolumeResponseTypeDef",
    "ClientDisableGatewayResponseTypeDef",
    "ClientJoinDomainResponseTypeDef",
    "ClientListFileSharesResponseFileShareInfoListTypeDef",
    "ClientListFileSharesResponseTypeDef",
    "ClientListGatewaysResponseGatewaysTypeDef",
    "ClientListGatewaysResponseTypeDef",
    "ClientListLocalDisksResponseDisksTypeDef",
    "ClientListLocalDisksResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTapesResponseTapeInfosTypeDef",
    "ClientListTapesResponseTypeDef",
    "ClientListVolumeInitiatorsResponseTypeDef",
    "ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef",
    "ClientListVolumeRecoveryPointsResponseTypeDef",
    "ClientListVolumesResponseVolumeInfosTypeDef",
    "ClientListVolumesResponseTypeDef",
    "ClientNotifyWhenUploadedResponseTypeDef",
    "ClientRefreshCacheResponseTypeDef",
    "ClientRemoveTagsFromResourceResponseTypeDef",
    "ClientResetCacheResponseTypeDef",
    "ClientRetrieveTapeArchiveResponseTypeDef",
    "ClientRetrieveTapeRecoveryPointResponseTypeDef",
    "ClientSetLocalConsolePasswordResponseTypeDef",
    "ClientSetSmbGuestPasswordResponseTypeDef",
    "ClientShutdownGatewayResponseTypeDef",
    "ClientStartAvailabilityMonitorTestResponseTypeDef",
    "ClientStartGatewayResponseTypeDef",
    "ClientUpdateBandwidthRateLimitResponseTypeDef",
    "ClientUpdateChapCredentialsResponseTypeDef",
    "ClientUpdateGatewayInformationResponseTypeDef",
    "ClientUpdateGatewaySoftwareNowResponseTypeDef",
    "ClientUpdateMaintenanceStartTimeResponseTypeDef",
    "ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef",
    "ClientUpdateNfsFileShareResponseTypeDef",
    "ClientUpdateSmbFileShareResponseTypeDef",
    "ClientUpdateSmbSecurityStrategyResponseTypeDef",
    "ClientUpdateSnapshotScheduleResponseTypeDef",
    "ClientUpdateSnapshotScheduleTagsTypeDef",
    "ClientUpdateVtlDeviceTypeResponseTypeDef",
    "DescribeTapeArchivesPaginatePaginationConfigTypeDef",
    "DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef",
    "DescribeTapeArchivesPaginateResponseTypeDef",
    "DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef",
    "DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef",
    "DescribeTapeRecoveryPointsPaginateResponseTypeDef",
    "DescribeTapesPaginatePaginationConfigTypeDef",
    "DescribeTapesPaginateResponseTapesTypeDef",
    "DescribeTapesPaginateResponseTypeDef",
    "DescribeVTLDevicesPaginatePaginationConfigTypeDef",
    "DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef",
    "DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef",
    "DescribeVTLDevicesPaginateResponseTypeDef",
    "ListFileSharesPaginatePaginationConfigTypeDef",
    "ListFileSharesPaginateResponseFileShareInfoListTypeDef",
    "ListFileSharesPaginateResponseTypeDef",
    "ListGatewaysPaginatePaginationConfigTypeDef",
    "ListGatewaysPaginateResponseGatewaysTypeDef",
    "ListGatewaysPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListTapesPaginatePaginationConfigTypeDef",
    "ListTapesPaginateResponseTapeInfosTypeDef",
    "ListTapesPaginateResponseTypeDef",
    "ListVolumesPaginatePaginationConfigTypeDef",
    "ListVolumesPaginateResponseVolumeInfosTypeDef",
    "ListVolumesPaginateResponseTypeDef",
)


_ClientActivateGatewayResponseTypeDef = TypedDict(
    "_ClientActivateGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientActivateGatewayResponseTypeDef(_ClientActivateGatewayResponseTypeDef):
    """
    - *(dict) --*

      AWS Storage Gateway returns the Amazon Resource Name (ARN) of the activated gateway. It is a
      string made of information such as your account, gateway name, and AWS Region. This ARN is
      used to reference the gateway in other API operations as well as resource-based authorization.
      .. note::

        For gateways activated prior to September 02, 2015, the gateway ARN contains the gateway
        name rather than the gateway ID. Changing the name of the gateway has no effect on the
        gateway ARN.
    """


_ClientActivateGatewayTagsTypeDef = TypedDict(
    "_ClientActivateGatewayTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientActivateGatewayTagsTypeDef(_ClientActivateGatewayTagsTypeDef):
    pass


_ClientAddCacheResponseTypeDef = TypedDict(
    "_ClientAddCacheResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientAddCacheResponseTypeDef(_ClientAddCacheResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientAddTagsToResourceResponseTypeDef = TypedDict(
    "_ClientAddTagsToResourceResponseTypeDef", {"ResourceARN": str}, total=False
)


class ClientAddTagsToResourceResponseTypeDef(_ClientAddTagsToResourceResponseTypeDef):
    """
    - *(dict) --*

      AddTagsToResourceOutput
      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the resource you want to add tags to.
    """


_ClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_ClientAddTagsToResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(_ClientAddTagsToResourceTagsTypeDef):
    pass


_ClientAddUploadBufferResponseTypeDef = TypedDict(
    "_ClientAddUploadBufferResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientAddUploadBufferResponseTypeDef(_ClientAddUploadBufferResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientAddWorkingStorageResponseTypeDef = TypedDict(
    "_ClientAddWorkingStorageResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientAddWorkingStorageResponseTypeDef(_ClientAddWorkingStorageResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the of the gateway for which working storage was configured.
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientAssignTapePoolResponseTypeDef = TypedDict(
    "_ClientAssignTapePoolResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientAssignTapePoolResponseTypeDef(_ClientAssignTapePoolResponseTypeDef):
    """
    - *(dict) --*

      - **TapeARN** *(string) --*

        The unique Amazon Resource Names (ARN) of the virtual tape that was added to the tape pool.
    """


_ClientAttachVolumeResponseTypeDef = TypedDict(
    "_ClientAttachVolumeResponseTypeDef", {"VolumeARN": str, "TargetARN": str}, total=False
)


class ClientAttachVolumeResponseTypeDef(_ClientAttachVolumeResponseTypeDef):
    """
    - *(dict) --*

      AttachVolumeOutput
      - **VolumeARN** *(string) --*

        The Amazon Resource Name (ARN) of the volume that was attached to the gateway.
    """


_ClientCancelArchivalResponseTypeDef = TypedDict(
    "_ClientCancelArchivalResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientCancelArchivalResponseTypeDef(_ClientCancelArchivalResponseTypeDef):
    """
    - *(dict) --*

      CancelArchivalOutput
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of the virtual tape for which archiving was canceled.
    """


_ClientCancelRetrievalResponseTypeDef = TypedDict(
    "_ClientCancelRetrievalResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientCancelRetrievalResponseTypeDef(_ClientCancelRetrievalResponseTypeDef):
    """
    - *(dict) --*

      CancelRetrievalOutput
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of the virtual tape for which retrieval was canceled.
    """


_ClientCreateCachedIscsiVolumeResponseTypeDef = TypedDict(
    "_ClientCreateCachedIscsiVolumeResponseTypeDef",
    {"VolumeARN": str, "TargetARN": str},
    total=False,
)


class ClientCreateCachedIscsiVolumeResponseTypeDef(_ClientCreateCachedIscsiVolumeResponseTypeDef):
    """
    - *(dict) --*

      - **VolumeARN** *(string) --*

        The Amazon Resource Name (ARN) of the configured volume.
    """


_ClientCreateCachedIscsiVolumeTagsTypeDef = TypedDict(
    "_ClientCreateCachedIscsiVolumeTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateCachedIscsiVolumeTagsTypeDef(_ClientCreateCachedIscsiVolumeTagsTypeDef):
    pass


_ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef = TypedDict(
    "_ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef",
    {"FileMode": str, "DirectoryMode": str, "GroupId": int, "OwnerId": int},
    total=False,
)


class ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef(
    _ClientCreateNfsFileShareNFSFileShareDefaultsTypeDef
):
    """
    File share default values. Optional.
    - **FileMode** *(string) --*

      The Unix file mode in the form "nnnn". For example, "0666" represents the default file mode
      inside the file share. The default value is 0666.
    """


_ClientCreateNfsFileShareResponseTypeDef = TypedDict(
    "_ClientCreateNfsFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)


class ClientCreateNfsFileShareResponseTypeDef(_ClientCreateNfsFileShareResponseTypeDef):
    """
    - *(dict) --*

      CreateNFSFileShareOutput
      - **FileShareARN** *(string) --*

        The Amazon Resource Name (ARN) of the newly created file share.
    """


_ClientCreateNfsFileShareTagsTypeDef = TypedDict(
    "_ClientCreateNfsFileShareTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateNfsFileShareTagsTypeDef(_ClientCreateNfsFileShareTagsTypeDef):
    pass


_ClientCreateSmbFileShareResponseTypeDef = TypedDict(
    "_ClientCreateSmbFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)


class ClientCreateSmbFileShareResponseTypeDef(_ClientCreateSmbFileShareResponseTypeDef):
    """
    - *(dict) --*

      CreateSMBFileShareOutput
      - **FileShareARN** *(string) --*

        The Amazon Resource Name (ARN) of the newly created file share.
    """


_ClientCreateSmbFileShareTagsTypeDef = TypedDict(
    "_ClientCreateSmbFileShareTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateSmbFileShareTagsTypeDef(_ClientCreateSmbFileShareTagsTypeDef):
    pass


_ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef = TypedDict(
    "_ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef",
    {"SnapshotId": str, "VolumeARN": str, "VolumeRecoveryPointTime": str},
    total=False,
)


class ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef(
    _ClientCreateSnapshotFromVolumeRecoveryPointResponseTypeDef
):
    """
    - *(dict) --*

      - **SnapshotId** *(string) --*

        The ID of the snapshot.
    """


_ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef = TypedDict(
    "_ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef(
    _ClientCreateSnapshotFromVolumeRecoveryPointTagsTypeDef
):
    pass


_ClientCreateSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseTypeDef", {"VolumeARN": str, "SnapshotId": str}, total=False
)


class ClientCreateSnapshotResponseTypeDef(_ClientCreateSnapshotResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      - **VolumeARN** *(string) --*

        The Amazon Resource Name (ARN) of the volume of which the snapshot was taken.
    """


_ClientCreateSnapshotTagsTypeDef = TypedDict(
    "_ClientCreateSnapshotTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateSnapshotTagsTypeDef(_ClientCreateSnapshotTagsTypeDef):
    pass


_ClientCreateStoredIscsiVolumeResponseTypeDef = TypedDict(
    "_ClientCreateStoredIscsiVolumeResponseTypeDef",
    {"VolumeARN": str, "VolumeSizeInBytes": int, "TargetARN": str},
    total=False,
)


class ClientCreateStoredIscsiVolumeResponseTypeDef(_ClientCreateStoredIscsiVolumeResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      - **VolumeARN** *(string) --*

        The Amazon Resource Name (ARN) of the configured volume.
    """


_ClientCreateStoredIscsiVolumeTagsTypeDef = TypedDict(
    "_ClientCreateStoredIscsiVolumeTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateStoredIscsiVolumeTagsTypeDef(_ClientCreateStoredIscsiVolumeTagsTypeDef):
    pass


_ClientCreateTapeWithBarcodeResponseTypeDef = TypedDict(
    "_ClientCreateTapeWithBarcodeResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientCreateTapeWithBarcodeResponseTypeDef(_ClientCreateTapeWithBarcodeResponseTypeDef):
    """
    - *(dict) --*

      CreateTapeOutput
      - **TapeARN** *(string) --*

        A unique Amazon Resource Name (ARN) that represents the virtual tape that was created.
    """


_ClientCreateTapeWithBarcodeTagsTypeDef = TypedDict(
    "_ClientCreateTapeWithBarcodeTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateTapeWithBarcodeTagsTypeDef(_ClientCreateTapeWithBarcodeTagsTypeDef):
    pass


_ClientCreateTapesResponseTypeDef = TypedDict(
    "_ClientCreateTapesResponseTypeDef", {"TapeARNs": List[str]}, total=False
)


class ClientCreateTapesResponseTypeDef(_ClientCreateTapesResponseTypeDef):
    """
    - *(dict) --*

      CreateTapeOutput
      - **TapeARNs** *(list) --*

        A list of unique Amazon Resource Names (ARNs) that represents the virtual tapes that were
        created.
        - *(string) --*
    """


_ClientCreateTapesTagsTypeDef = TypedDict(
    "_ClientCreateTapesTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateTapesTagsTypeDef(_ClientCreateTapesTagsTypeDef):
    pass


_ClientDeleteBandwidthRateLimitResponseTypeDef = TypedDict(
    "_ClientDeleteBandwidthRateLimitResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientDeleteBandwidthRateLimitResponseTypeDef(_ClientDeleteBandwidthRateLimitResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the of the gateway whose bandwidth rate information was deleted.
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDeleteChapCredentialsResponseTypeDef = TypedDict(
    "_ClientDeleteChapCredentialsResponseTypeDef",
    {"TargetARN": str, "InitiatorName": str},
    total=False,
)


class ClientDeleteChapCredentialsResponseTypeDef(_ClientDeleteChapCredentialsResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      - **TargetARN** *(string) --*

        The Amazon Resource Name (ARN) of the target.
    """


_ClientDeleteFileShareResponseTypeDef = TypedDict(
    "_ClientDeleteFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)


class ClientDeleteFileShareResponseTypeDef(_ClientDeleteFileShareResponseTypeDef):
    """
    - *(dict) --*

      DeleteFileShareOutput
      - **FileShareARN** *(string) --*

        The Amazon Resource Name (ARN) of the deleted file share.
    """


_ClientDeleteGatewayResponseTypeDef = TypedDict(
    "_ClientDeleteGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientDeleteGatewayResponseTypeDef(_ClientDeleteGatewayResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the ID of the deleted gateway.
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDeleteSnapshotScheduleResponseTypeDef = TypedDict(
    "_ClientDeleteSnapshotScheduleResponseTypeDef", {"VolumeARN": str}, total=False
)


class ClientDeleteSnapshotScheduleResponseTypeDef(_ClientDeleteSnapshotScheduleResponseTypeDef):
    """
    - *(dict) --*

      - **VolumeARN** *(string) --*

        The volume which snapshot schedule was deleted.
    """


_ClientDeleteTapeArchiveResponseTypeDef = TypedDict(
    "_ClientDeleteTapeArchiveResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientDeleteTapeArchiveResponseTypeDef(_ClientDeleteTapeArchiveResponseTypeDef):
    """
    - *(dict) --*

      DeleteTapeArchiveOutput
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of the virtual tape that was deleted from the virtual tape
        shelf (VTS).
    """


_ClientDeleteTapeResponseTypeDef = TypedDict(
    "_ClientDeleteTapeResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientDeleteTapeResponseTypeDef(_ClientDeleteTapeResponseTypeDef):
    """
    - *(dict) --*

      DeleteTapeOutput
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of the deleted virtual tape.
    """


_ClientDeleteVolumeResponseTypeDef = TypedDict(
    "_ClientDeleteVolumeResponseTypeDef", {"VolumeARN": str}, total=False
)


class ClientDeleteVolumeResponseTypeDef(_ClientDeleteVolumeResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the of the storage volume that was deleted
      - **VolumeARN** *(string) --*

        The Amazon Resource Name (ARN) of the storage volume that was deleted. It is the same ARN
        you provided in the request.
    """


_ClientDescribeAvailabilityMonitorTestResponseTypeDef = TypedDict(
    "_ClientDescribeAvailabilityMonitorTestResponseTypeDef",
    {"GatewayARN": str, "Status": Literal["COMPLETE", "FAILED", "PENDING"], "StartTime": datetime},
    total=False,
)


class ClientDescribeAvailabilityMonitorTestResponseTypeDef(
    _ClientDescribeAvailabilityMonitorTestResponseTypeDef
):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDescribeBandwidthRateLimitResponseTypeDef = TypedDict(
    "_ClientDescribeBandwidthRateLimitResponseTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
    },
    total=False,
)


class ClientDescribeBandwidthRateLimitResponseTypeDef(
    _ClientDescribeBandwidthRateLimitResponseTypeDef
):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDescribeCacheResponseTypeDef = TypedDict(
    "_ClientDescribeCacheResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "CacheAllocatedInBytes": int,
        "CacheUsedPercentage": float,
        "CacheDirtyPercentage": float,
        "CacheHitPercentage": float,
        "CacheMissPercentage": float,
    },
    total=False,
)


class ClientDescribeCacheResponseTypeDef(_ClientDescribeCacheResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef = TypedDict(
    "_ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "LunNumber": int,
        "ChapEnabled": bool,
    },
    total=False,
)


class ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef(
    _ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef
):
    pass


_ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef = TypedDict(
    "_ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "SourceSnapshotId": str,
        "VolumeiSCSIAttributes": ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesVolumeiSCSIAttributesTypeDef,
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)


class ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef(
    _ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef
):
    """
    - *(dict) --*

      Describes an iSCSI cached volume.
      - **VolumeARN** *(string) --*

        The Amazon Resource Name (ARN) of the storage volume.
    """


_ClientDescribeCachedIscsiVolumesResponseTypeDef = TypedDict(
    "_ClientDescribeCachedIscsiVolumesResponseTypeDef",
    {"CachediSCSIVolumes": List[ClientDescribeCachedIscsiVolumesResponseCachediSCSIVolumesTypeDef]},
    total=False,
)


class ClientDescribeCachedIscsiVolumesResponseTypeDef(
    _ClientDescribeCachedIscsiVolumesResponseTypeDef
):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      - **CachediSCSIVolumes** *(list) --*

        An array of objects where each object contains metadata about one cached volume.
        - *(dict) --*

          Describes an iSCSI cached volume.
          - **VolumeARN** *(string) --*

            The Amazon Resource Name (ARN) of the storage volume.
    """


_ClientDescribeChapCredentialsResponseChapCredentialsTypeDef = TypedDict(
    "_ClientDescribeChapCredentialsResponseChapCredentialsTypeDef",
    {
        "TargetARN": str,
        "SecretToAuthenticateInitiator": str,
        "InitiatorName": str,
        "SecretToAuthenticateTarget": str,
    },
    total=False,
)


class ClientDescribeChapCredentialsResponseChapCredentialsTypeDef(
    _ClientDescribeChapCredentialsResponseChapCredentialsTypeDef
):
    """
    - *(dict) --*

      Describes Challenge-Handshake Authentication Protocol (CHAP) information that supports
      authentication between your gateway and iSCSI initiators.
      - **TargetARN** *(string) --*

        The Amazon Resource Name (ARN) of the volume.
        Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).
    """


_ClientDescribeChapCredentialsResponseTypeDef = TypedDict(
    "_ClientDescribeChapCredentialsResponseTypeDef",
    {"ChapCredentials": List[ClientDescribeChapCredentialsResponseChapCredentialsTypeDef]},
    total=False,
)


class ClientDescribeChapCredentialsResponseTypeDef(_ClientDescribeChapCredentialsResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing a .
      - **ChapCredentials** *(list) --*

        An array of  ChapInfo objects that represent CHAP credentials. Each object in the array
        contains CHAP credential information for one target-initiator pair. If no CHAP credentials
        are set, an empty array is returned. CHAP credential information is provided in a JSON
        object with the following fields:
        * **InitiatorName** : The iSCSI initiator that connects to the target.
        * **SecretToAuthenticateInitiator** : The secret key that the initiator (for example, the
        Windows client) must provide to participate in mutual CHAP with the target.
        * **SecretToAuthenticateTarget** : The secret key that the target must provide to
        participate in mutual CHAP with the initiator (e.g. Windows client).
        * **TargetARN** : The Amazon Resource Name (ARN) of the storage volume.
        - *(dict) --*

          Describes Challenge-Handshake Authentication Protocol (CHAP) information that supports
          authentication between your gateway and iSCSI initiators.
          - **TargetARN** *(string) --*

            The Amazon Resource Name (ARN) of the volume.
            Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).
    """


_ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef = TypedDict(
    "_ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef",
    {"Ipv4Address": str, "MacAddress": str, "Ipv6Address": str},
    total=False,
)


class ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef(
    _ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef
):
    pass


_ClientDescribeGatewayInformationResponseTagsTypeDef = TypedDict(
    "_ClientDescribeGatewayInformationResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeGatewayInformationResponseTagsTypeDef(
    _ClientDescribeGatewayInformationResponseTagsTypeDef
):
    pass


_ClientDescribeGatewayInformationResponseTypeDef = TypedDict(
    "_ClientDescribeGatewayInformationResponseTypeDef",
    {
        "GatewayARN": str,
        "GatewayId": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayState": str,
        "GatewayNetworkInterfaces": List[
            ClientDescribeGatewayInformationResponseGatewayNetworkInterfacesTypeDef
        ],
        "GatewayType": str,
        "NextUpdateAvailabilityDate": str,
        "LastSoftwareUpdate": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
        "Tags": List[ClientDescribeGatewayInformationResponseTagsTypeDef],
        "VPCEndpoint": str,
        "CloudWatchLogGroupARN": str,
        "HostEnvironment": Literal["VMWARE", "HYPER-V", "EC2", "OTHER"],
    },
    total=False,
)


class ClientDescribeGatewayInformationResponseTypeDef(
    _ClientDescribeGatewayInformationResponseTypeDef
):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDescribeMaintenanceStartTimeResponseTypeDef = TypedDict(
    "_ClientDescribeMaintenanceStartTimeResponseTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfWeek": int,
        "DayOfMonth": int,
        "Timezone": str,
    },
    total=False,
)


class ClientDescribeMaintenanceStartTimeResponseTypeDef(
    _ClientDescribeMaintenanceStartTimeResponseTypeDef
):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      *  DescribeMaintenanceStartTimeOutput$DayOfMonth
      *  DescribeMaintenanceStartTimeOutput$DayOfWeek
      *  DescribeMaintenanceStartTimeOutput$HourOfDay
      *  DescribeMaintenanceStartTimeOutput$MinuteOfHour
      *  DescribeMaintenanceStartTimeOutput$Timezone
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef = TypedDict(
    "_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef",
    {"FileMode": str, "DirectoryMode": str, "GroupId": int, "OwnerId": int},
    total=False,
)


class ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef(
    _ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef
):
    """
    - **NFSFileShareDefaults** *(dict) --*

      Describes Network File System (NFS) file share default values. Files and folders stored as
      Amazon S3 objects in S3 buckets don't, by default, have Unix file permissions assigned to
      them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent files
      and folders are assigned these default Unix permissions. This operation is only supported for
      file gateways.
      - **FileMode** *(string) --*

        The Unix file mode in the form "nnnn". For example, "0666" represents the default file mode
        inside the file share. The default value is 0666.
    """


_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef = TypedDict(
    "_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef(
    _ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef
):
    pass


_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef = TypedDict(
    "_ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef",
    {
        "NFSFileShareDefaults": ClientDescribeNfsFileSharesResponseNFSFileShareInfoListNFSFileShareDefaultsTypeDef,
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ],
        "ClientList": List[str],
        "Squash": str,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "Tags": List[ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTagsTypeDef],
    },
    total=False,
)


class ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef(
    _ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef
):
    """
    - *(dict) --*

      The Unix file permissions and ownership information assigned, by default, to native S3 objects
      when file gateway discovers them in S3 buckets. This operation is only supported in file
      gateways.
      - **NFSFileShareDefaults** *(dict) --*

        Describes Network File System (NFS) file share default values. Files and folders stored as
        Amazon S3 objects in S3 buckets don't, by default, have Unix file permissions assigned to
        them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent files
        and folders are assigned these default Unix permissions. This operation is only supported
        for file gateways.
        - **FileMode** *(string) --*

          The Unix file mode in the form "nnnn". For example, "0666" represents the default file
          mode inside the file share. The default value is 0666.
    """


_ClientDescribeNfsFileSharesResponseTypeDef = TypedDict(
    "_ClientDescribeNfsFileSharesResponseTypeDef",
    {"NFSFileShareInfoList": List[ClientDescribeNfsFileSharesResponseNFSFileShareInfoListTypeDef]},
    total=False,
)


class ClientDescribeNfsFileSharesResponseTypeDef(_ClientDescribeNfsFileSharesResponseTypeDef):
    """
    - *(dict) --*

      DescribeNFSFileSharesOutput
      - **NFSFileShareInfoList** *(list) --*

        An array containing a description for each requested file share.
        - *(dict) --*

          The Unix file permissions and ownership information assigned, by default, to native S3
          objects when file gateway discovers them in S3 buckets. This operation is only supported
          in file gateways.
          - **NFSFileShareDefaults** *(dict) --*

            Describes Network File System (NFS) file share default values. Files and folders stored
            as Amazon S3 objects in S3 buckets don't, by default, have Unix file permissions
            assigned to them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that
            represent files and folders are assigned these default Unix permissions. This operation
            is only supported for file gateways.
            - **FileMode** *(string) --*

              The Unix file mode in the form "nnnn". For example, "0666" represents the default file
              mode inside the file share. The default value is 0666.
    """


_ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef = TypedDict(
    "_ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef(
    _ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef
):
    pass


_ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef = TypedDict(
    "_ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef",
    {
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
            "aws-exec-read",
        ],
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "SMBACLEnabled": bool,
        "AdminUserList": List[str],
        "ValidUserList": List[str],
        "InvalidUserList": List[str],
        "Authentication": str,
        "Tags": List[ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTagsTypeDef],
    },
    total=False,
)


class ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef(
    _ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef
):
    """
    - *(dict) --*

      The Windows file permissions and ownership information assigned, by default, to native S3
      objects when file gateway discovers them in S3 buckets. This operation is only supported for
      file gateways.
      - **FileShareARN** *(string) --*

        The Amazon Resource Name (ARN) of the file share.
    """


_ClientDescribeSmbFileSharesResponseTypeDef = TypedDict(
    "_ClientDescribeSmbFileSharesResponseTypeDef",
    {"SMBFileShareInfoList": List[ClientDescribeSmbFileSharesResponseSMBFileShareInfoListTypeDef]},
    total=False,
)


class ClientDescribeSmbFileSharesResponseTypeDef(_ClientDescribeSmbFileSharesResponseTypeDef):
    """
    - *(dict) --*

      DescribeSMBFileSharesOutput
      - **SMBFileShareInfoList** *(list) --*

        An array containing a description for each requested file share.
        - *(dict) --*

          The Windows file permissions and ownership information assigned, by default, to native S3
          objects when file gateway discovers them in S3 buckets. This operation is only supported
          for file gateways.
          - **FileShareARN** *(string) --*

            The Amazon Resource Name (ARN) of the file share.
    """


_ClientDescribeSmbSettingsResponseTypeDef = TypedDict(
    "_ClientDescribeSmbSettingsResponseTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "ActiveDirectoryStatus": Literal[
            "ACCESS_DENIED",
            "DETACHED",
            "JOINED",
            "JOINING",
            "NETWORK_ERROR",
            "TIMEOUT",
            "UNKNOWN_ERROR",
        ],
        "SMBGuestPasswordSet": bool,
        "SMBSecurityStrategy": Literal[
            "ClientSpecified", "MandatorySigning", "MandatoryEncryption"
        ],
    },
    total=False,
)


class ClientDescribeSmbSettingsResponseTypeDef(_ClientDescribeSmbSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDescribeSnapshotScheduleResponseTagsTypeDef = TypedDict(
    "_ClientDescribeSnapshotScheduleResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeSnapshotScheduleResponseTagsTypeDef(
    _ClientDescribeSnapshotScheduleResponseTagsTypeDef
):
    pass


_ClientDescribeSnapshotScheduleResponseTypeDef = TypedDict(
    "_ClientDescribeSnapshotScheduleResponseTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
        "Description": str,
        "Timezone": str,
        "Tags": List[ClientDescribeSnapshotScheduleResponseTagsTypeDef],
    },
    total=False,
)


class ClientDescribeSnapshotScheduleResponseTypeDef(_ClientDescribeSnapshotScheduleResponseTypeDef):
    """
    - *(dict) --*

      - **VolumeARN** *(string) --*

        The Amazon Resource Name (ARN) of the volume that was specified in the request.
    """


_ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef = TypedDict(
    "_ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "LunNumber": int,
        "ChapEnabled": bool,
    },
    total=False,
)


class ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef(
    _ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef
):
    pass


_ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef = TypedDict(
    "_ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "VolumeDiskId": str,
        "SourceSnapshotId": str,
        "PreservedExistingData": bool,
        "VolumeiSCSIAttributes": ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesVolumeiSCSIAttributesTypeDef,
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)


class ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef(
    _ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef
):
    """
    - *(dict) --*

      Describes an iSCSI stored volume.
      - **VolumeARN** *(string) --*

        The Amazon Resource Name (ARN) of the storage volume.
    """


_ClientDescribeStoredIscsiVolumesResponseTypeDef = TypedDict(
    "_ClientDescribeStoredIscsiVolumesResponseTypeDef",
    {"StorediSCSIVolumes": List[ClientDescribeStoredIscsiVolumesResponseStorediSCSIVolumesTypeDef]},
    total=False,
)


class ClientDescribeStoredIscsiVolumesResponseTypeDef(
    _ClientDescribeStoredIscsiVolumesResponseTypeDef
):
    """
    - *(dict) --*

      - **StorediSCSIVolumes** *(list) --*

        Describes a single unit of output from  DescribeStorediSCSIVolumes . The following fields
        are returned:
        * **ChapEnabled** : Indicates whether mutual CHAP is enabled for the iSCSI target.
        * **LunNumber** : The logical disk number.
        * **NetworkInterfaceId** : The network interface ID of the stored volume that initiator use
        to map the stored volume as an iSCSI target.
        * **NetworkInterfacePort** : The port used to communicate with iSCSI targets.
        * **PreservedExistingData** : Indicates if when the stored volume was created, existing data
        on the underlying local disk was preserved.
        * **SourceSnapshotId** : If the stored volume was created from a snapshot, this field
        contains the snapshot ID used, e.g. snap-1122aabb. Otherwise, this field is not included.
        * **StorediSCSIVolumes** : An array of StorediSCSIVolume objects where each object contains
        metadata about one stored volume.
        * **TargetARN** : The Amazon Resource Name (ARN) of the volume target.
        * **VolumeARN** : The Amazon Resource Name (ARN) of the stored volume.
        * **VolumeDiskId** : The disk ID of the local disk that was specified in the
        CreateStorediSCSIVolume operation.
        * **VolumeId** : The unique identifier of the storage volume, e.g. vol-1122AABB.
        * **VolumeiSCSIAttributes** : An  VolumeiSCSIAttributes object that represents a collection
        of iSCSI attributes for one stored volume.
        * **VolumeProgress** : Represents the percentage complete if the volume is restoring or
        bootstrapping that represents the percent of data transferred. This field does not appear in
        the response if the stored volume is not restoring or bootstrapping.
        * **VolumeSizeInBytes** : The size of the volume in bytes.
        * **VolumeStatus** : One of the ``VolumeStatus`` values that indicates the state of the
        volume.
        * **VolumeType** : One of the enumeration values describing the type of the volume.
        Currently, on STORED volumes are supported.
        - *(dict) --*

          Describes an iSCSI stored volume.
          - **VolumeARN** *(string) --*

            The Amazon Resource Name (ARN) of the storage volume.
    """


_ClientDescribeTapeArchivesResponseTapeArchivesTypeDef = TypedDict(
    "_ClientDescribeTapeArchivesResponseTapeArchivesTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "CompletionTime": datetime,
        "RetrievedTo": str,
        "TapeStatus": str,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)


class ClientDescribeTapeArchivesResponseTapeArchivesTypeDef(
    _ClientDescribeTapeArchivesResponseTapeArchivesTypeDef
):
    """
    - *(dict) --*

      Represents a virtual tape that is archived in the virtual tape shelf (VTS).
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of an archived virtual tape.
    """


_ClientDescribeTapeArchivesResponseTypeDef = TypedDict(
    "_ClientDescribeTapeArchivesResponseTypeDef",
    {"TapeArchives": List[ClientDescribeTapeArchivesResponseTapeArchivesTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeTapeArchivesResponseTypeDef(_ClientDescribeTapeArchivesResponseTypeDef):
    """
    - *(dict) --*

      DescribeTapeArchivesOutput
      - **TapeArchives** *(list) --*

        An array of virtual tape objects in the virtual tape shelf (VTS). The description includes
        of the Amazon Resource Name (ARN) of the virtual tapes. The information returned includes
        the Amazon Resource Names (ARNs) of the tapes, size of the tapes, status of the tapes,
        progress of the description and tape barcode.
        - *(dict) --*

          Represents a virtual tape that is archived in the virtual tape shelf (VTS).
          - **TapeARN** *(string) --*

            The Amazon Resource Name (ARN) of an archived virtual tape.
    """


_ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef = TypedDict(
    "_ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef",
    {"TapeARN": str, "TapeRecoveryPointTime": datetime, "TapeSizeInBytes": int, "TapeStatus": str},
    total=False,
)


class ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef(
    _ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef
):
    pass


_ClientDescribeTapeRecoveryPointsResponseTypeDef = TypedDict(
    "_ClientDescribeTapeRecoveryPointsResponseTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List[
            ClientDescribeTapeRecoveryPointsResponseTapeRecoveryPointInfosTypeDef
        ],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeTapeRecoveryPointsResponseTypeDef(
    _ClientDescribeTapeRecoveryPointsResponseTypeDef
):
    """
    - *(dict) --*

      DescribeTapeRecoveryPointsOutput
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDescribeTapesResponseTapesTypeDef = TypedDict(
    "_ClientDescribeTapesResponseTapesTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "VTLDevice": str,
        "Progress": float,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)


class ClientDescribeTapesResponseTapesTypeDef(_ClientDescribeTapesResponseTapesTypeDef):
    """
    - *(dict) --*

      Describes a virtual tape object.
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of the virtual tape.
    """


_ClientDescribeTapesResponseTypeDef = TypedDict(
    "_ClientDescribeTapesResponseTypeDef",
    {"Tapes": List[ClientDescribeTapesResponseTapesTypeDef], "Marker": str},
    total=False,
)


class ClientDescribeTapesResponseTypeDef(_ClientDescribeTapesResponseTypeDef):
    """
    - *(dict) --*

      DescribeTapesOutput
      - **Tapes** *(list) --*

        An array of virtual tape descriptions.
        - *(dict) --*

          Describes a virtual tape object.
          - **TapeARN** *(string) --*

            The Amazon Resource Name (ARN) of the virtual tape.
    """


_ClientDescribeUploadBufferResponseTypeDef = TypedDict(
    "_ClientDescribeUploadBufferResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "UploadBufferUsedInBytes": int,
        "UploadBufferAllocatedInBytes": int,
    },
    total=False,
)


class ClientDescribeUploadBufferResponseTypeDef(_ClientDescribeUploadBufferResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef = TypedDict(
    "_ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef",
    {"TargetARN": str, "NetworkInterfaceId": str, "NetworkInterfacePort": int, "ChapEnabled": bool},
    total=False,
)


class ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef(
    _ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef
):
    pass


_ClientDescribeVtlDevicesResponseVTLDevicesTypeDef = TypedDict(
    "_ClientDescribeVtlDevicesResponseVTLDevicesTypeDef",
    {
        "VTLDeviceARN": str,
        "VTLDeviceType": str,
        "VTLDeviceVendor": str,
        "VTLDeviceProductIdentifier": str,
        "DeviceiSCSIAttributes": ClientDescribeVtlDevicesResponseVTLDevicesDeviceiSCSIAttributesTypeDef,
    },
    total=False,
)


class ClientDescribeVtlDevicesResponseVTLDevicesTypeDef(
    _ClientDescribeVtlDevicesResponseVTLDevicesTypeDef
):
    pass


_ClientDescribeVtlDevicesResponseTypeDef = TypedDict(
    "_ClientDescribeVtlDevicesResponseTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List[ClientDescribeVtlDevicesResponseVTLDevicesTypeDef],
        "Marker": str,
    },
    total=False,
)


class ClientDescribeVtlDevicesResponseTypeDef(_ClientDescribeVtlDevicesResponseTypeDef):
    """
    - *(dict) --*

      DescribeVTLDevicesOutput
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDescribeWorkingStorageResponseTypeDef = TypedDict(
    "_ClientDescribeWorkingStorageResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "WorkingStorageUsedInBytes": int,
        "WorkingStorageAllocatedInBytes": int,
    },
    total=False,
)


class ClientDescribeWorkingStorageResponseTypeDef(_ClientDescribeWorkingStorageResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientDetachVolumeResponseTypeDef = TypedDict(
    "_ClientDetachVolumeResponseTypeDef", {"VolumeARN": str}, total=False
)


class ClientDetachVolumeResponseTypeDef(_ClientDetachVolumeResponseTypeDef):
    """
    - *(dict) --*

      AttachVolumeOutput
      - **VolumeARN** *(string) --*

        The Amazon Resource Name (ARN) of the volume that was detached.
    """


_ClientDisableGatewayResponseTypeDef = TypedDict(
    "_ClientDisableGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientDisableGatewayResponseTypeDef(_ClientDisableGatewayResponseTypeDef):
    """
    - *(dict) --*

      DisableGatewayOutput
      - **GatewayARN** *(string) --*

        The unique Amazon Resource Name (ARN) of the disabled gateway.
    """


_ClientJoinDomainResponseTypeDef = TypedDict(
    "_ClientJoinDomainResponseTypeDef",
    {
        "GatewayARN": str,
        "ActiveDirectoryStatus": Literal[
            "ACCESS_DENIED",
            "DETACHED",
            "JOINED",
            "JOINING",
            "NETWORK_ERROR",
            "TIMEOUT",
            "UNKNOWN_ERROR",
        ],
    },
    total=False,
)


class ClientJoinDomainResponseTypeDef(_ClientJoinDomainResponseTypeDef):
    """
    - *(dict) --*

      JoinDomainOutput
      - **GatewayARN** *(string) --*

        The unique Amazon Resource Name (ARN) of the gateway that joined the domain.
    """


_ClientListFileSharesResponseFileShareInfoListTypeDef = TypedDict(
    "_ClientListFileSharesResponseFileShareInfoListTypeDef",
    {
        "FileShareType": Literal["NFS", "SMB"],
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
    },
    total=False,
)


class ClientListFileSharesResponseFileShareInfoListTypeDef(
    _ClientListFileSharesResponseFileShareInfoListTypeDef
):
    pass


_ClientListFileSharesResponseTypeDef = TypedDict(
    "_ClientListFileSharesResponseTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileShareInfoList": List[ClientListFileSharesResponseFileShareInfoListTypeDef],
    },
    total=False,
)


class ClientListFileSharesResponseTypeDef(_ClientListFileSharesResponseTypeDef):
    """
    - *(dict) --*

      ListFileShareOutput
      - **Marker** *(string) --*

        If the request includes ``Marker`` , the response returns that value in this field.
    """


_ClientListGatewaysResponseGatewaysTypeDef = TypedDict(
    "_ClientListGatewaysResponseGatewaysTypeDef",
    {
        "GatewayId": str,
        "GatewayARN": str,
        "GatewayType": str,
        "GatewayOperationalState": str,
        "GatewayName": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
    },
    total=False,
)


class ClientListGatewaysResponseGatewaysTypeDef(_ClientListGatewaysResponseGatewaysTypeDef):
    """
    - *(dict) --*

      Describes a gateway object.
      - **GatewayId** *(string) --*

        The unique identifier assigned to your gateway during activation. This ID becomes part of
        the gateway Amazon Resource Name (ARN), which you use as input for other operations.
    """


_ClientListGatewaysResponseTypeDef = TypedDict(
    "_ClientListGatewaysResponseTypeDef",
    {"Gateways": List[ClientListGatewaysResponseGatewaysTypeDef], "Marker": str},
    total=False,
)


class ClientListGatewaysResponseTypeDef(_ClientListGatewaysResponseTypeDef):
    """
    - *(dict) --*

      - **Gateways** *(list) --*

        An array of  GatewayInfo objects.
        - *(dict) --*

          Describes a gateway object.
          - **GatewayId** *(string) --*

            The unique identifier assigned to your gateway during activation. This ID becomes part
            of the gateway Amazon Resource Name (ARN), which you use as input for other operations.
    """


_ClientListLocalDisksResponseDisksTypeDef = TypedDict(
    "_ClientListLocalDisksResponseDisksTypeDef",
    {
        "DiskId": str,
        "DiskPath": str,
        "DiskNode": str,
        "DiskStatus": str,
        "DiskSizeInBytes": int,
        "DiskAllocationType": str,
        "DiskAllocationResource": str,
        "DiskAttributeList": List[str],
    },
    total=False,
)


class ClientListLocalDisksResponseDisksTypeDef(_ClientListLocalDisksResponseDisksTypeDef):
    pass


_ClientListLocalDisksResponseTypeDef = TypedDict(
    "_ClientListLocalDisksResponseTypeDef",
    {"GatewayARN": str, "Disks": List[ClientListLocalDisksResponseDisksTypeDef]},
    total=False,
)


class ClientListLocalDisksResponseTypeDef(_ClientListLocalDisksResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    pass


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"ResourceARN": str, "Marker": str, "Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      ListTagsForResourceOutput
      - **ResourceARN** *(string) --*

        he Amazon Resource Name (ARN) of the resource for which you want to list tags.
    """


_ClientListTapesResponseTapeInfosTypeDef = TypedDict(
    "_ClientListTapesResponseTapeInfosTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "GatewayARN": str,
        "PoolId": str,
    },
    total=False,
)


class ClientListTapesResponseTapeInfosTypeDef(_ClientListTapesResponseTapeInfosTypeDef):
    """
    - *(dict) --*

      Describes a virtual tape.
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of a virtual tape.
    """


_ClientListTapesResponseTypeDef = TypedDict(
    "_ClientListTapesResponseTypeDef",
    {"TapeInfos": List[ClientListTapesResponseTapeInfosTypeDef], "Marker": str},
    total=False,
)


class ClientListTapesResponseTypeDef(_ClientListTapesResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      *  ListTapesOutput$Marker
      *  ListTapesOutput$VolumeInfos
      - **TapeInfos** *(list) --*

        An array of  TapeInfo objects, where each object describes an a single tape. If there not
        tapes in the tape library or VTS, then the ``TapeInfos`` is an empty array.
        - *(dict) --*

          Describes a virtual tape.
          - **TapeARN** *(string) --*

            The Amazon Resource Name (ARN) of a virtual tape.
    """


_ClientListVolumeInitiatorsResponseTypeDef = TypedDict(
    "_ClientListVolumeInitiatorsResponseTypeDef", {"Initiators": List[str]}, total=False
)


class ClientListVolumeInitiatorsResponseTypeDef(_ClientListVolumeInitiatorsResponseTypeDef):
    """
    - *(dict) --*

      ListVolumeInitiatorsOutput
      - **Initiators** *(list) --*

        The host names and port numbers of all iSCSI initiators that are connected to the gateway.
        - *(string) --*
    """


_ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef = TypedDict(
    "_ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "VolumeUsageInBytes": int,
        "VolumeRecoveryPointTime": str,
    },
    total=False,
)


class ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef(
    _ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef
):
    pass


_ClientListVolumeRecoveryPointsResponseTypeDef = TypedDict(
    "_ClientListVolumeRecoveryPointsResponseTypeDef",
    {
        "GatewayARN": str,
        "VolumeRecoveryPointInfos": List[
            ClientListVolumeRecoveryPointsResponseVolumeRecoveryPointInfosTypeDef
        ],
    },
    total=False,
)


class ClientListVolumeRecoveryPointsResponseTypeDef(_ClientListVolumeRecoveryPointsResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientListVolumesResponseVolumeInfosTypeDef = TypedDict(
    "_ClientListVolumesResponseVolumeInfosTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "GatewayARN": str,
        "GatewayId": str,
        "VolumeType": str,
        "VolumeSizeInBytes": int,
        "VolumeAttachmentStatus": str,
    },
    total=False,
)


class ClientListVolumesResponseVolumeInfosTypeDef(_ClientListVolumesResponseVolumeInfosTypeDef):
    pass


_ClientListVolumesResponseTypeDef = TypedDict(
    "_ClientListVolumesResponseTypeDef",
    {
        "GatewayARN": str,
        "Marker": str,
        "VolumeInfos": List[ClientListVolumesResponseVolumeInfosTypeDef],
    },
    total=False,
)


class ClientListVolumesResponseTypeDef(_ClientListVolumesResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      *  ListVolumesOutput$Marker
      *  ListVolumesOutput$VolumeInfos
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientNotifyWhenUploadedResponseTypeDef = TypedDict(
    "_ClientNotifyWhenUploadedResponseTypeDef",
    {"FileShareARN": str, "NotificationId": str},
    total=False,
)


class ClientNotifyWhenUploadedResponseTypeDef(_ClientNotifyWhenUploadedResponseTypeDef):
    """
    - *(dict) --*

      - **FileShareARN** *(string) --*

        The Amazon Resource Name (ARN) of the file share.
    """


_ClientRefreshCacheResponseTypeDef = TypedDict(
    "_ClientRefreshCacheResponseTypeDef", {"FileShareARN": str, "NotificationId": str}, total=False
)


class ClientRefreshCacheResponseTypeDef(_ClientRefreshCacheResponseTypeDef):
    """
    - *(dict) --*

      RefreshCacheOutput
      - **FileShareARN** *(string) --*

        The Amazon Resource Name (ARN) of the file share.
    """


_ClientRemoveTagsFromResourceResponseTypeDef = TypedDict(
    "_ClientRemoveTagsFromResourceResponseTypeDef", {"ResourceARN": str}, total=False
)


class ClientRemoveTagsFromResourceResponseTypeDef(_ClientRemoveTagsFromResourceResponseTypeDef):
    """
    - *(dict) --*

      RemoveTagsFromResourceOutput
      - **ResourceARN** *(string) --*

        The Amazon Resource Name (ARN) of the resource that the tags were removed from.
    """


_ClientResetCacheResponseTypeDef = TypedDict(
    "_ClientResetCacheResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientResetCacheResponseTypeDef(_ClientResetCacheResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientRetrieveTapeArchiveResponseTypeDef = TypedDict(
    "_ClientRetrieveTapeArchiveResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientRetrieveTapeArchiveResponseTypeDef(_ClientRetrieveTapeArchiveResponseTypeDef):
    """
    - *(dict) --*

      RetrieveTapeArchiveOutput
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of the retrieved virtual tape.
    """


_ClientRetrieveTapeRecoveryPointResponseTypeDef = TypedDict(
    "_ClientRetrieveTapeRecoveryPointResponseTypeDef", {"TapeARN": str}, total=False
)


class ClientRetrieveTapeRecoveryPointResponseTypeDef(
    _ClientRetrieveTapeRecoveryPointResponseTypeDef
):
    """
    - *(dict) --*

      RetrieveTapeRecoveryPointOutput
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of the virtual tape for which the recovery point was
        retrieved.
    """


_ClientSetLocalConsolePasswordResponseTypeDef = TypedDict(
    "_ClientSetLocalConsolePasswordResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientSetLocalConsolePasswordResponseTypeDef(_ClientSetLocalConsolePasswordResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientSetSmbGuestPasswordResponseTypeDef = TypedDict(
    "_ClientSetSmbGuestPasswordResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientSetSmbGuestPasswordResponseTypeDef(_ClientSetSmbGuestPasswordResponseTypeDef):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientShutdownGatewayResponseTypeDef = TypedDict(
    "_ClientShutdownGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientShutdownGatewayResponseTypeDef(_ClientShutdownGatewayResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the of the gateway that was shut down.
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientStartAvailabilityMonitorTestResponseTypeDef = TypedDict(
    "_ClientStartAvailabilityMonitorTestResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientStartAvailabilityMonitorTestResponseTypeDef(
    _ClientStartAvailabilityMonitorTestResponseTypeDef
):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientStartGatewayResponseTypeDef = TypedDict(
    "_ClientStartGatewayResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientStartGatewayResponseTypeDef(_ClientStartGatewayResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the of the gateway that was restarted.
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientUpdateBandwidthRateLimitResponseTypeDef = TypedDict(
    "_ClientUpdateBandwidthRateLimitResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientUpdateBandwidthRateLimitResponseTypeDef(_ClientUpdateBandwidthRateLimitResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the of the gateway whose throttle information was updated.
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientUpdateChapCredentialsResponseTypeDef = TypedDict(
    "_ClientUpdateChapCredentialsResponseTypeDef",
    {"TargetARN": str, "InitiatorName": str},
    total=False,
)


class ClientUpdateChapCredentialsResponseTypeDef(_ClientUpdateChapCredentialsResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      - **TargetARN** *(string) --*

        The Amazon Resource Name (ARN) of the target. This is the same target specified in the
        request.
    """


_ClientUpdateGatewayInformationResponseTypeDef = TypedDict(
    "_ClientUpdateGatewayInformationResponseTypeDef",
    {"GatewayARN": str, "GatewayName": str},
    total=False,
)


class ClientUpdateGatewayInformationResponseTypeDef(_ClientUpdateGatewayInformationResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the ARN of the gateway that was updated.
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientUpdateGatewaySoftwareNowResponseTypeDef = TypedDict(
    "_ClientUpdateGatewaySoftwareNowResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientUpdateGatewaySoftwareNowResponseTypeDef(_ClientUpdateGatewaySoftwareNowResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the of the gateway that was updated.
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientUpdateMaintenanceStartTimeResponseTypeDef = TypedDict(
    "_ClientUpdateMaintenanceStartTimeResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientUpdateMaintenanceStartTimeResponseTypeDef(
    _ClientUpdateMaintenanceStartTimeResponseTypeDef
):
    """
    - *(dict) --*

      A JSON object containing the of the gateway whose maintenance start time is updated.
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef = TypedDict(
    "_ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef",
    {"FileMode": str, "DirectoryMode": str, "GroupId": int, "OwnerId": int},
    total=False,
)


class ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef(
    _ClientUpdateNfsFileShareNFSFileShareDefaultsTypeDef
):
    """
    The default values for the file share. Optional.
    - **FileMode** *(string) --*

      The Unix file mode in the form "nnnn". For example, "0666" represents the default file mode
      inside the file share. The default value is 0666.
    """


_ClientUpdateNfsFileShareResponseTypeDef = TypedDict(
    "_ClientUpdateNfsFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)


class ClientUpdateNfsFileShareResponseTypeDef(_ClientUpdateNfsFileShareResponseTypeDef):
    """
    - *(dict) --*

      UpdateNFSFileShareOutput
      - **FileShareARN** *(string) --*

        The Amazon Resource Name (ARN) of the updated file share.
    """


_ClientUpdateSmbFileShareResponseTypeDef = TypedDict(
    "_ClientUpdateSmbFileShareResponseTypeDef", {"FileShareARN": str}, total=False
)


class ClientUpdateSmbFileShareResponseTypeDef(_ClientUpdateSmbFileShareResponseTypeDef):
    """
    - *(dict) --*

      UpdateSMBFileShareOutput
      - **FileShareARN** *(string) --*

        The Amazon Resource Name (ARN) of the updated SMB file share.
    """


_ClientUpdateSmbSecurityStrategyResponseTypeDef = TypedDict(
    "_ClientUpdateSmbSecurityStrategyResponseTypeDef", {"GatewayARN": str}, total=False
)


class ClientUpdateSmbSecurityStrategyResponseTypeDef(
    _ClientUpdateSmbSecurityStrategyResponseTypeDef
):
    """
    - *(dict) --*

      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ClientUpdateSnapshotScheduleResponseTypeDef = TypedDict(
    "_ClientUpdateSnapshotScheduleResponseTypeDef", {"VolumeARN": str}, total=False
)


class ClientUpdateSnapshotScheduleResponseTypeDef(_ClientUpdateSnapshotScheduleResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the of the updated storage volume.
      - **VolumeARN** *(string) --*

        The Amazon Resource Name (ARN) of the volume. Use the  ListVolumes operation to return a
        list of gateway volumes.
    """


_ClientUpdateSnapshotScheduleTagsTypeDef = TypedDict(
    "_ClientUpdateSnapshotScheduleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUpdateSnapshotScheduleTagsTypeDef(_ClientUpdateSnapshotScheduleTagsTypeDef):
    pass


_ClientUpdateVtlDeviceTypeResponseTypeDef = TypedDict(
    "_ClientUpdateVtlDeviceTypeResponseTypeDef", {"VTLDeviceARN": str}, total=False
)


class ClientUpdateVtlDeviceTypeResponseTypeDef(_ClientUpdateVtlDeviceTypeResponseTypeDef):
    """
    - *(dict) --*

      UpdateVTLDeviceTypeOutput
      - **VTLDeviceARN** *(string) --*

        The Amazon Resource Name (ARN) of the medium changer you have selected.
    """


_DescribeTapeArchivesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTapeArchivesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTapeArchivesPaginatePaginationConfigTypeDef(
    _DescribeTapeArchivesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef = TypedDict(
    "_DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "CompletionTime": datetime,
        "RetrievedTo": str,
        "TapeStatus": str,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)


class DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef(
    _DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef
):
    """
    - *(dict) --*

      Represents a virtual tape that is archived in the virtual tape shelf (VTS).
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of an archived virtual tape.
    """


_DescribeTapeArchivesPaginateResponseTypeDef = TypedDict(
    "_DescribeTapeArchivesPaginateResponseTypeDef",
    {
        "TapeArchives": List[DescribeTapeArchivesPaginateResponseTapeArchivesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeTapeArchivesPaginateResponseTypeDef(_DescribeTapeArchivesPaginateResponseTypeDef):
    """
    - *(dict) --*

      DescribeTapeArchivesOutput
      - **TapeArchives** *(list) --*

        An array of virtual tape objects in the virtual tape shelf (VTS). The description includes
        of the Amazon Resource Name (ARN) of the virtual tapes. The information returned includes
        the Amazon Resource Names (ARNs) of the tapes, size of the tapes, status of the tapes,
        progress of the description and tape barcode.
        - *(dict) --*

          Represents a virtual tape that is archived in the virtual tape shelf (VTS).
          - **TapeARN** *(string) --*

            The Amazon Resource Name (ARN) of an archived virtual tape.
    """


_DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef(
    _DescribeTapeRecoveryPointsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef = TypedDict(
    "_DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef",
    {"TapeARN": str, "TapeRecoveryPointTime": datetime, "TapeSizeInBytes": int, "TapeStatus": str},
    total=False,
)


class DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef(
    _DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef
):
    pass


_DescribeTapeRecoveryPointsPaginateResponseTypeDef = TypedDict(
    "_DescribeTapeRecoveryPointsPaginateResponseTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List[
            DescribeTapeRecoveryPointsPaginateResponseTapeRecoveryPointInfosTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeTapeRecoveryPointsPaginateResponseTypeDef(
    _DescribeTapeRecoveryPointsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      DescribeTapeRecoveryPointsOutput
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_DescribeTapesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTapesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTapesPaginatePaginationConfigTypeDef(_DescribeTapesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeTapesPaginateResponseTapesTypeDef = TypedDict(
    "_DescribeTapesPaginateResponseTapesTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "VTLDevice": str,
        "Progress": float,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
    },
    total=False,
)


class DescribeTapesPaginateResponseTapesTypeDef(_DescribeTapesPaginateResponseTapesTypeDef):
    """
    - *(dict) --*

      Describes a virtual tape object.
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of the virtual tape.
    """


_DescribeTapesPaginateResponseTypeDef = TypedDict(
    "_DescribeTapesPaginateResponseTypeDef",
    {"Tapes": List[DescribeTapesPaginateResponseTapesTypeDef], "NextToken": str},
    total=False,
)


class DescribeTapesPaginateResponseTypeDef(_DescribeTapesPaginateResponseTypeDef):
    """
    - *(dict) --*

      DescribeTapesOutput
      - **Tapes** *(list) --*

        An array of virtual tape descriptions.
        - *(dict) --*

          Describes a virtual tape object.
          - **TapeARN** *(string) --*

            The Amazon Resource Name (ARN) of the virtual tape.
    """


_DescribeVTLDevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeVTLDevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeVTLDevicesPaginatePaginationConfigTypeDef(
    _DescribeVTLDevicesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef = TypedDict(
    "_DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef",
    {"TargetARN": str, "NetworkInterfaceId": str, "NetworkInterfacePort": int, "ChapEnabled": bool},
    total=False,
)


class DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef(
    _DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef
):
    pass


_DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef = TypedDict(
    "_DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef",
    {
        "VTLDeviceARN": str,
        "VTLDeviceType": str,
        "VTLDeviceVendor": str,
        "VTLDeviceProductIdentifier": str,
        "DeviceiSCSIAttributes": DescribeVTLDevicesPaginateResponseVTLDevicesDeviceiSCSIAttributesTypeDef,
    },
    total=False,
)


class DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef(
    _DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef
):
    pass


_DescribeVTLDevicesPaginateResponseTypeDef = TypedDict(
    "_DescribeVTLDevicesPaginateResponseTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List[DescribeVTLDevicesPaginateResponseVTLDevicesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeVTLDevicesPaginateResponseTypeDef(_DescribeVTLDevicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      DescribeVTLDevicesOutput
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """


_ListFileSharesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFileSharesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFileSharesPaginatePaginationConfigTypeDef(_ListFileSharesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFileSharesPaginateResponseFileShareInfoListTypeDef = TypedDict(
    "_ListFileSharesPaginateResponseFileShareInfoListTypeDef",
    {
        "FileShareType": Literal["NFS", "SMB"],
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
    },
    total=False,
)


class ListFileSharesPaginateResponseFileShareInfoListTypeDef(
    _ListFileSharesPaginateResponseFileShareInfoListTypeDef
):
    pass


_ListFileSharesPaginateResponseTypeDef = TypedDict(
    "_ListFileSharesPaginateResponseTypeDef",
    {
        "Marker": str,
        "FileShareInfoList": List[ListFileSharesPaginateResponseFileShareInfoListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListFileSharesPaginateResponseTypeDef(_ListFileSharesPaginateResponseTypeDef):
    """
    - *(dict) --*

      ListFileShareOutput
      - **Marker** *(string) --*

        If the request includes ``Marker`` , the response returns that value in this field.
    """


_ListGatewaysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGatewaysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGatewaysPaginatePaginationConfigTypeDef(_ListGatewaysPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGatewaysPaginateResponseGatewaysTypeDef = TypedDict(
    "_ListGatewaysPaginateResponseGatewaysTypeDef",
    {
        "GatewayId": str,
        "GatewayARN": str,
        "GatewayType": str,
        "GatewayOperationalState": str,
        "GatewayName": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
    },
    total=False,
)


class ListGatewaysPaginateResponseGatewaysTypeDef(_ListGatewaysPaginateResponseGatewaysTypeDef):
    """
    - *(dict) --*

      Describes a gateway object.
      - **GatewayId** *(string) --*

        The unique identifier assigned to your gateway during activation. This ID becomes part of
        the gateway Amazon Resource Name (ARN), which you use as input for other operations.
    """


_ListGatewaysPaginateResponseTypeDef = TypedDict(
    "_ListGatewaysPaginateResponseTypeDef",
    {"Gateways": List[ListGatewaysPaginateResponseGatewaysTypeDef], "NextToken": str},
    total=False,
)


class ListGatewaysPaginateResponseTypeDef(_ListGatewaysPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Gateways** *(list) --*

        An array of  GatewayInfo objects.
        - *(dict) --*

          Describes a gateway object.
          - **GatewayId** *(string) --*

            The unique identifier assigned to your gateway during activation. This ID becomes part
            of the gateway Amazon Resource Name (ARN), which you use as input for other operations.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    pass


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {
        "ResourceARN": str,
        "Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(_ListTagsForResourcePaginateResponseTypeDef):
    """
    - *(dict) --*

      ListTagsForResourceOutput
      - **ResourceARN** *(string) --*

        he Amazon Resource Name (ARN) of the resource for which you want to list tags.
    """


_ListTapesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTapesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTapesPaginatePaginationConfigTypeDef(_ListTapesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTapesPaginateResponseTapeInfosTypeDef = TypedDict(
    "_ListTapesPaginateResponseTapeInfosTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "GatewayARN": str,
        "PoolId": str,
    },
    total=False,
)


class ListTapesPaginateResponseTapeInfosTypeDef(_ListTapesPaginateResponseTapeInfosTypeDef):
    """
    - *(dict) --*

      Describes a virtual tape.
      - **TapeARN** *(string) --*

        The Amazon Resource Name (ARN) of a virtual tape.
    """


_ListTapesPaginateResponseTypeDef = TypedDict(
    "_ListTapesPaginateResponseTypeDef",
    {"TapeInfos": List[ListTapesPaginateResponseTapeInfosTypeDef], "NextToken": str},
    total=False,
)


class ListTapesPaginateResponseTypeDef(_ListTapesPaginateResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      *  ListTapesOutput$Marker
      *  ListTapesOutput$VolumeInfos
      - **TapeInfos** *(list) --*

        An array of  TapeInfo objects, where each object describes an a single tape. If there not
        tapes in the tape library or VTS, then the ``TapeInfos`` is an empty array.
        - *(dict) --*

          Describes a virtual tape.
          - **TapeARN** *(string) --*

            The Amazon Resource Name (ARN) of a virtual tape.
    """


_ListVolumesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVolumesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVolumesPaginatePaginationConfigTypeDef(_ListVolumesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListVolumesPaginateResponseVolumeInfosTypeDef = TypedDict(
    "_ListVolumesPaginateResponseVolumeInfosTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "GatewayARN": str,
        "GatewayId": str,
        "VolumeType": str,
        "VolumeSizeInBytes": int,
        "VolumeAttachmentStatus": str,
    },
    total=False,
)


class ListVolumesPaginateResponseVolumeInfosTypeDef(_ListVolumesPaginateResponseVolumeInfosTypeDef):
    pass


_ListVolumesPaginateResponseTypeDef = TypedDict(
    "_ListVolumesPaginateResponseTypeDef",
    {
        "GatewayARN": str,
        "VolumeInfos": List[ListVolumesPaginateResponseVolumeInfosTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListVolumesPaginateResponseTypeDef(_ListVolumesPaginateResponseTypeDef):
    """
    - *(dict) --*

      A JSON object containing the following fields:
      *  ListVolumesOutput$Marker
      *  ListVolumesOutput$VolumeInfos
      - **GatewayARN** *(string) --*

        The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a
        list of gateways for your account and AWS Region.
    """
