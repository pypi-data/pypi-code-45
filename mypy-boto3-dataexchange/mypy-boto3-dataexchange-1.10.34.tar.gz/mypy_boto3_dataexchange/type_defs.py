"Main interface for dataexchange service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateDataSetResponseOriginDetailsTypeDef = TypedDict(
    "ClientCreateDataSetResponseOriginDetailsTypeDef", {"ProductId": str}, total=False
)

ClientCreateDataSetResponseTypeDef = TypedDict(
    "ClientCreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": Literal["OWNED", "ENTITLED"],
        "OriginDetails": ClientCreateDataSetResponseOriginDetailsTypeDef,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
    },
    total=False,
)

_RequiredClientCreateJobDetailsExportAssetToSignedUrlTypeDef = TypedDict(
    "_RequiredClientCreateJobDetailsExportAssetToSignedUrlTypeDef", {"AssetId": str}
)
_OptionalClientCreateJobDetailsExportAssetToSignedUrlTypeDef = TypedDict(
    "_OptionalClientCreateJobDetailsExportAssetToSignedUrlTypeDef",
    {"DataSetId": str, "RevisionId": str},
    total=False,
)


class ClientCreateJobDetailsExportAssetToSignedUrlTypeDef(
    _RequiredClientCreateJobDetailsExportAssetToSignedUrlTypeDef,
    _OptionalClientCreateJobDetailsExportAssetToSignedUrlTypeDef,
):
    pass


ClientCreateJobDetailsExportAssetsToS3AssetDestinationsTypeDef = TypedDict(
    "ClientCreateJobDetailsExportAssetsToS3AssetDestinationsTypeDef",
    {"AssetId": str, "Bucket": str, "Key": str},
    total=False,
)

ClientCreateJobDetailsExportAssetsToS3TypeDef = TypedDict(
    "ClientCreateJobDetailsExportAssetsToS3TypeDef",
    {
        "AssetDestinations": List[ClientCreateJobDetailsExportAssetsToS3AssetDestinationsTypeDef],
        "DataSetId": str,
        "RevisionId": str,
    },
    total=False,
)

ClientCreateJobDetailsImportAssetFromSignedUrlTypeDef = TypedDict(
    "ClientCreateJobDetailsImportAssetFromSignedUrlTypeDef",
    {"AssetName": str, "DataSetId": str, "Md5Hash": str, "RevisionId": str},
    total=False,
)

ClientCreateJobDetailsImportAssetsFromS3AssetSourcesTypeDef = TypedDict(
    "ClientCreateJobDetailsImportAssetsFromS3AssetSourcesTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientCreateJobDetailsImportAssetsFromS3TypeDef = TypedDict(
    "ClientCreateJobDetailsImportAssetsFromS3TypeDef",
    {
        "AssetSources": List[ClientCreateJobDetailsImportAssetsFromS3AssetSourcesTypeDef],
        "DataSetId": str,
        "RevisionId": str,
    },
    total=False,
)

ClientCreateJobDetailsTypeDef = TypedDict(
    "ClientCreateJobDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": ClientCreateJobDetailsExportAssetToSignedUrlTypeDef,
        "ExportAssetsToS3": ClientCreateJobDetailsExportAssetsToS3TypeDef,
        "ImportAssetFromSignedUrl": ClientCreateJobDetailsImportAssetFromSignedUrlTypeDef,
        "ImportAssetsFromS3": ClientCreateJobDetailsImportAssetsFromS3TypeDef,
    },
    total=False,
)

ClientCreateJobResponseDetailsExportAssetToSignedUrlTypeDef = TypedDict(
    "ClientCreateJobResponseDetailsExportAssetToSignedUrlTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
        "SignedUrl": str,
        "SignedUrlExpiresAt": datetime,
    },
    total=False,
)

ClientCreateJobResponseDetailsExportAssetsToS3AssetDestinationsTypeDef = TypedDict(
    "ClientCreateJobResponseDetailsExportAssetsToS3AssetDestinationsTypeDef",
    {"AssetId": str, "Bucket": str, "Key": str},
    total=False,
)

ClientCreateJobResponseDetailsExportAssetsToS3TypeDef = TypedDict(
    "ClientCreateJobResponseDetailsExportAssetsToS3TypeDef",
    {
        "AssetDestinations": List[
            ClientCreateJobResponseDetailsExportAssetsToS3AssetDestinationsTypeDef
        ],
        "DataSetId": str,
        "RevisionId": str,
    },
    total=False,
)

ClientCreateJobResponseDetailsImportAssetFromSignedUrlTypeDef = TypedDict(
    "ClientCreateJobResponseDetailsImportAssetFromSignedUrlTypeDef",
    {
        "AssetName": str,
        "DataSetId": str,
        "Md5Hash": str,
        "RevisionId": str,
        "SignedUrl": str,
        "SignedUrlExpiresAt": datetime,
    },
    total=False,
)

ClientCreateJobResponseDetailsImportAssetsFromS3AssetSourcesTypeDef = TypedDict(
    "ClientCreateJobResponseDetailsImportAssetsFromS3AssetSourcesTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientCreateJobResponseDetailsImportAssetsFromS3TypeDef = TypedDict(
    "ClientCreateJobResponseDetailsImportAssetsFromS3TypeDef",
    {
        "AssetSources": List[ClientCreateJobResponseDetailsImportAssetsFromS3AssetSourcesTypeDef],
        "DataSetId": str,
        "RevisionId": str,
    },
    total=False,
)

ClientCreateJobResponseDetailsTypeDef = TypedDict(
    "ClientCreateJobResponseDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": ClientCreateJobResponseDetailsExportAssetToSignedUrlTypeDef,
        "ExportAssetsToS3": ClientCreateJobResponseDetailsExportAssetsToS3TypeDef,
        "ImportAssetFromSignedUrl": ClientCreateJobResponseDetailsImportAssetFromSignedUrlTypeDef,
        "ImportAssetsFromS3": ClientCreateJobResponseDetailsImportAssetsFromS3TypeDef,
    },
    total=False,
)

ClientCreateJobResponseErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef = TypedDict(
    "ClientCreateJobResponseErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    {"AssetName": str},
    total=False,
)

ClientCreateJobResponseErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef = TypedDict(
    "ClientCreateJobResponseErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientCreateJobResponseErrorsDetailsTypeDef = TypedDict(
    "ClientCreateJobResponseErrorsDetailsTypeDef",
    {
        "ImportAssetFromSignedUrlJobErrorDetails": ClientCreateJobResponseErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef,
        "ImportAssetsFromS3JobErrorDetails": List[
            ClientCreateJobResponseErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef
        ],
    },
    total=False,
)

ClientCreateJobResponseErrorsTypeDef = TypedDict(
    "ClientCreateJobResponseErrorsTypeDef",
    {
        "Code": Literal[
            "ACCESS_DENIED_EXCEPTION",
            "INTERNAL_SERVER_EXCEPTION",
            "MALWARE_DETECTED",
            "RESOURCE_NOT_FOUND_EXCEPTION",
            "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
            "VALIDATION_EXCEPTION",
            "MALWARE_SCAN_ENCRYPTED_FILE",
        ],
        "Details": ClientCreateJobResponseErrorsDetailsTypeDef,
        "LimitName": Literal["Assets per revision", "Asset size in GB"],
        "LimitValue": float,
        "Message": str,
        "ResourceId": str,
        "ResourceType": Literal["REVISION", "ASSET"],
    },
    total=False,
)

ClientCreateJobResponseTypeDef = TypedDict(
    "ClientCreateJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": ClientCreateJobResponseDetailsTypeDef,
        "Errors": List[ClientCreateJobResponseErrorsTypeDef],
        "Id": str,
        "State": Literal["WAITING", "IN_PROGRESS", "ERROR", "COMPLETED", "CANCELLED", "TIMED_OUT"],
        "Type": Literal[
            "IMPORT_ASSETS_FROM_S3",
            "IMPORT_ASSET_FROM_SIGNED_URL",
            "EXPORT_ASSETS_TO_S3",
            "EXPORT_ASSET_TO_SIGNED_URL",
        ],
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientCreateRevisionResponseTypeDef = TypedDict(
    "ClientCreateRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientGetAssetResponseAssetDetailsS3SnapshotAssetTypeDef = TypedDict(
    "ClientGetAssetResponseAssetDetailsS3SnapshotAssetTypeDef", {"Size": float}, total=False
)

ClientGetAssetResponseAssetDetailsTypeDef = TypedDict(
    "ClientGetAssetResponseAssetDetailsTypeDef",
    {"S3SnapshotAsset": ClientGetAssetResponseAssetDetailsS3SnapshotAssetTypeDef},
    total=False,
)

ClientGetAssetResponseTypeDef = TypedDict(
    "ClientGetAssetResponseTypeDef",
    {
        "Arn": str,
        "AssetDetails": ClientGetAssetResponseAssetDetailsTypeDef,
        "AssetType": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientGetDataSetResponseOriginDetailsTypeDef = TypedDict(
    "ClientGetDataSetResponseOriginDetailsTypeDef", {"ProductId": str}, total=False
)

ClientGetDataSetResponseTypeDef = TypedDict(
    "ClientGetDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": Literal["OWNED", "ENTITLED"],
        "OriginDetails": ClientGetDataSetResponseOriginDetailsTypeDef,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientGetJobResponseDetailsExportAssetToSignedUrlTypeDef = TypedDict(
    "ClientGetJobResponseDetailsExportAssetToSignedUrlTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
        "SignedUrl": str,
        "SignedUrlExpiresAt": datetime,
    },
    total=False,
)

ClientGetJobResponseDetailsExportAssetsToS3AssetDestinationsTypeDef = TypedDict(
    "ClientGetJobResponseDetailsExportAssetsToS3AssetDestinationsTypeDef",
    {"AssetId": str, "Bucket": str, "Key": str},
    total=False,
)

ClientGetJobResponseDetailsExportAssetsToS3TypeDef = TypedDict(
    "ClientGetJobResponseDetailsExportAssetsToS3TypeDef",
    {
        "AssetDestinations": List[
            ClientGetJobResponseDetailsExportAssetsToS3AssetDestinationsTypeDef
        ],
        "DataSetId": str,
        "RevisionId": str,
    },
    total=False,
)

ClientGetJobResponseDetailsImportAssetFromSignedUrlTypeDef = TypedDict(
    "ClientGetJobResponseDetailsImportAssetFromSignedUrlTypeDef",
    {
        "AssetName": str,
        "DataSetId": str,
        "Md5Hash": str,
        "RevisionId": str,
        "SignedUrl": str,
        "SignedUrlExpiresAt": datetime,
    },
    total=False,
)

ClientGetJobResponseDetailsImportAssetsFromS3AssetSourcesTypeDef = TypedDict(
    "ClientGetJobResponseDetailsImportAssetsFromS3AssetSourcesTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientGetJobResponseDetailsImportAssetsFromS3TypeDef = TypedDict(
    "ClientGetJobResponseDetailsImportAssetsFromS3TypeDef",
    {
        "AssetSources": List[ClientGetJobResponseDetailsImportAssetsFromS3AssetSourcesTypeDef],
        "DataSetId": str,
        "RevisionId": str,
    },
    total=False,
)

ClientGetJobResponseDetailsTypeDef = TypedDict(
    "ClientGetJobResponseDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": ClientGetJobResponseDetailsExportAssetToSignedUrlTypeDef,
        "ExportAssetsToS3": ClientGetJobResponseDetailsExportAssetsToS3TypeDef,
        "ImportAssetFromSignedUrl": ClientGetJobResponseDetailsImportAssetFromSignedUrlTypeDef,
        "ImportAssetsFromS3": ClientGetJobResponseDetailsImportAssetsFromS3TypeDef,
    },
    total=False,
)

ClientGetJobResponseErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef = TypedDict(
    "ClientGetJobResponseErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    {"AssetName": str},
    total=False,
)

ClientGetJobResponseErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef = TypedDict(
    "ClientGetJobResponseErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientGetJobResponseErrorsDetailsTypeDef = TypedDict(
    "ClientGetJobResponseErrorsDetailsTypeDef",
    {
        "ImportAssetFromSignedUrlJobErrorDetails": ClientGetJobResponseErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef,
        "ImportAssetsFromS3JobErrorDetails": List[
            ClientGetJobResponseErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef
        ],
    },
    total=False,
)

ClientGetJobResponseErrorsTypeDef = TypedDict(
    "ClientGetJobResponseErrorsTypeDef",
    {
        "Code": Literal[
            "ACCESS_DENIED_EXCEPTION",
            "INTERNAL_SERVER_EXCEPTION",
            "MALWARE_DETECTED",
            "RESOURCE_NOT_FOUND_EXCEPTION",
            "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
            "VALIDATION_EXCEPTION",
            "MALWARE_SCAN_ENCRYPTED_FILE",
        ],
        "Details": ClientGetJobResponseErrorsDetailsTypeDef,
        "LimitName": Literal["Assets per revision", "Asset size in GB"],
        "LimitValue": float,
        "Message": str,
        "ResourceId": str,
        "ResourceType": Literal["REVISION", "ASSET"],
    },
    total=False,
)

ClientGetJobResponseTypeDef = TypedDict(
    "ClientGetJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": ClientGetJobResponseDetailsTypeDef,
        "Errors": List[ClientGetJobResponseErrorsTypeDef],
        "Id": str,
        "State": Literal["WAITING", "IN_PROGRESS", "ERROR", "COMPLETED", "CANCELLED", "TIMED_OUT"],
        "Type": Literal[
            "IMPORT_ASSETS_FROM_S3",
            "IMPORT_ASSET_FROM_SIGNED_URL",
            "EXPORT_ASSETS_TO_S3",
            "EXPORT_ASSET_TO_SIGNED_URL",
        ],
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientGetRevisionResponseTypeDef = TypedDict(
    "ClientGetRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "Tags": Dict[str, str],
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientListDataSetRevisionsResponseRevisionsTypeDef = TypedDict(
    "ClientListDataSetRevisionsResponseRevisionsTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientListDataSetRevisionsResponseTypeDef = TypedDict(
    "ClientListDataSetRevisionsResponseTypeDef",
    {"NextToken": str, "Revisions": List[ClientListDataSetRevisionsResponseRevisionsTypeDef]},
    total=False,
)

ClientListDataSetsResponseDataSetsOriginDetailsTypeDef = TypedDict(
    "ClientListDataSetsResponseDataSetsOriginDetailsTypeDef", {"ProductId": str}, total=False
)

ClientListDataSetsResponseDataSetsTypeDef = TypedDict(
    "ClientListDataSetsResponseDataSetsTypeDef",
    {
        "Arn": str,
        "AssetType": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": Literal["OWNED", "ENTITLED"],
        "OriginDetails": ClientListDataSetsResponseDataSetsOriginDetailsTypeDef,
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientListDataSetsResponseTypeDef = TypedDict(
    "ClientListDataSetsResponseTypeDef",
    {"DataSets": List[ClientListDataSetsResponseDataSetsTypeDef], "NextToken": str},
    total=False,
)

ClientListJobsResponseJobsDetailsExportAssetToSignedUrlTypeDef = TypedDict(
    "ClientListJobsResponseJobsDetailsExportAssetToSignedUrlTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
        "SignedUrl": str,
        "SignedUrlExpiresAt": datetime,
    },
    total=False,
)

ClientListJobsResponseJobsDetailsExportAssetsToS3AssetDestinationsTypeDef = TypedDict(
    "ClientListJobsResponseJobsDetailsExportAssetsToS3AssetDestinationsTypeDef",
    {"AssetId": str, "Bucket": str, "Key": str},
    total=False,
)

ClientListJobsResponseJobsDetailsExportAssetsToS3TypeDef = TypedDict(
    "ClientListJobsResponseJobsDetailsExportAssetsToS3TypeDef",
    {
        "AssetDestinations": List[
            ClientListJobsResponseJobsDetailsExportAssetsToS3AssetDestinationsTypeDef
        ],
        "DataSetId": str,
        "RevisionId": str,
    },
    total=False,
)

ClientListJobsResponseJobsDetailsImportAssetFromSignedUrlTypeDef = TypedDict(
    "ClientListJobsResponseJobsDetailsImportAssetFromSignedUrlTypeDef",
    {
        "AssetName": str,
        "DataSetId": str,
        "Md5Hash": str,
        "RevisionId": str,
        "SignedUrl": str,
        "SignedUrlExpiresAt": datetime,
    },
    total=False,
)

ClientListJobsResponseJobsDetailsImportAssetsFromS3AssetSourcesTypeDef = TypedDict(
    "ClientListJobsResponseJobsDetailsImportAssetsFromS3AssetSourcesTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientListJobsResponseJobsDetailsImportAssetsFromS3TypeDef = TypedDict(
    "ClientListJobsResponseJobsDetailsImportAssetsFromS3TypeDef",
    {
        "AssetSources": List[
            ClientListJobsResponseJobsDetailsImportAssetsFromS3AssetSourcesTypeDef
        ],
        "DataSetId": str,
        "RevisionId": str,
    },
    total=False,
)

ClientListJobsResponseJobsDetailsTypeDef = TypedDict(
    "ClientListJobsResponseJobsDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": ClientListJobsResponseJobsDetailsExportAssetToSignedUrlTypeDef,
        "ExportAssetsToS3": ClientListJobsResponseJobsDetailsExportAssetsToS3TypeDef,
        "ImportAssetFromSignedUrl": ClientListJobsResponseJobsDetailsImportAssetFromSignedUrlTypeDef,
        "ImportAssetsFromS3": ClientListJobsResponseJobsDetailsImportAssetsFromS3TypeDef,
    },
    total=False,
)

ClientListJobsResponseJobsErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef = TypedDict(
    "ClientListJobsResponseJobsErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    {"AssetName": str},
    total=False,
)

ClientListJobsResponseJobsErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef = TypedDict(
    "ClientListJobsResponseJobsErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ClientListJobsResponseJobsErrorsDetailsTypeDef = TypedDict(
    "ClientListJobsResponseJobsErrorsDetailsTypeDef",
    {
        "ImportAssetFromSignedUrlJobErrorDetails": ClientListJobsResponseJobsErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef,
        "ImportAssetsFromS3JobErrorDetails": List[
            ClientListJobsResponseJobsErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef
        ],
    },
    total=False,
)

ClientListJobsResponseJobsErrorsTypeDef = TypedDict(
    "ClientListJobsResponseJobsErrorsTypeDef",
    {
        "Code": Literal[
            "ACCESS_DENIED_EXCEPTION",
            "INTERNAL_SERVER_EXCEPTION",
            "MALWARE_DETECTED",
            "RESOURCE_NOT_FOUND_EXCEPTION",
            "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
            "VALIDATION_EXCEPTION",
            "MALWARE_SCAN_ENCRYPTED_FILE",
        ],
        "Details": ClientListJobsResponseJobsErrorsDetailsTypeDef,
        "LimitName": Literal["Assets per revision", "Asset size in GB"],
        "LimitValue": float,
        "Message": str,
        "ResourceId": str,
        "ResourceType": Literal["REVISION", "ASSET"],
    },
    total=False,
)

ClientListJobsResponseJobsTypeDef = TypedDict(
    "ClientListJobsResponseJobsTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": ClientListJobsResponseJobsDetailsTypeDef,
        "Errors": List[ClientListJobsResponseJobsErrorsTypeDef],
        "Id": str,
        "State": Literal["WAITING", "IN_PROGRESS", "ERROR", "COMPLETED", "CANCELLED", "TIMED_OUT"],
        "Type": Literal[
            "IMPORT_ASSETS_FROM_S3",
            "IMPORT_ASSET_FROM_SIGNED_URL",
            "EXPORT_ASSETS_TO_S3",
            "EXPORT_ASSET_TO_SIGNED_URL",
        ],
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef",
    {"Jobs": List[ClientListJobsResponseJobsTypeDef], "NextToken": str},
    total=False,
)

ClientListRevisionAssetsResponseAssetsAssetDetailsS3SnapshotAssetTypeDef = TypedDict(
    "ClientListRevisionAssetsResponseAssetsAssetDetailsS3SnapshotAssetTypeDef",
    {"Size": float},
    total=False,
)

ClientListRevisionAssetsResponseAssetsAssetDetailsTypeDef = TypedDict(
    "ClientListRevisionAssetsResponseAssetsAssetDetailsTypeDef",
    {"S3SnapshotAsset": ClientListRevisionAssetsResponseAssetsAssetDetailsS3SnapshotAssetTypeDef},
    total=False,
)

ClientListRevisionAssetsResponseAssetsTypeDef = TypedDict(
    "ClientListRevisionAssetsResponseAssetsTypeDef",
    {
        "Arn": str,
        "AssetDetails": ClientListRevisionAssetsResponseAssetsAssetDetailsTypeDef,
        "AssetType": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientListRevisionAssetsResponseTypeDef = TypedDict(
    "ClientListRevisionAssetsResponseTypeDef",
    {"Assets": List[ClientListRevisionAssetsResponseAssetsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientUpdateAssetResponseAssetDetailsS3SnapshotAssetTypeDef = TypedDict(
    "ClientUpdateAssetResponseAssetDetailsS3SnapshotAssetTypeDef", {"Size": float}, total=False
)

ClientUpdateAssetResponseAssetDetailsTypeDef = TypedDict(
    "ClientUpdateAssetResponseAssetDetailsTypeDef",
    {"S3SnapshotAsset": ClientUpdateAssetResponseAssetDetailsS3SnapshotAssetTypeDef},
    total=False,
)

ClientUpdateAssetResponseTypeDef = TypedDict(
    "ClientUpdateAssetResponseTypeDef",
    {
        "Arn": str,
        "AssetDetails": ClientUpdateAssetResponseAssetDetailsTypeDef,
        "AssetType": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientUpdateDataSetResponseOriginDetailsTypeDef = TypedDict(
    "ClientUpdateDataSetResponseOriginDetailsTypeDef", {"ProductId": str}, total=False
)

ClientUpdateDataSetResponseTypeDef = TypedDict(
    "ClientUpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "AssetType": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": Literal["OWNED", "ENTITLED"],
        "OriginDetails": ClientUpdateDataSetResponseOriginDetailsTypeDef,
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

ClientUpdateRevisionResponseTypeDef = TypedDict(
    "ClientUpdateRevisionResponseTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

ListDataSetRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDataSetRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDataSetRevisionsPaginateResponseRevisionsTypeDef = TypedDict(
    "ListDataSetRevisionsPaginateResponseRevisionsTypeDef",
    {
        "Arn": str,
        "Comment": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Finalized": bool,
        "Id": str,
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

ListDataSetRevisionsPaginateResponseTypeDef = TypedDict(
    "ListDataSetRevisionsPaginateResponseTypeDef",
    {"Revisions": List[ListDataSetRevisionsPaginateResponseRevisionsTypeDef]},
    total=False,
)

ListDataSetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDataSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDataSetsPaginateResponseDataSetsOriginDetailsTypeDef = TypedDict(
    "ListDataSetsPaginateResponseDataSetsOriginDetailsTypeDef", {"ProductId": str}, total=False
)

ListDataSetsPaginateResponseDataSetsTypeDef = TypedDict(
    "ListDataSetsPaginateResponseDataSetsTypeDef",
    {
        "Arn": str,
        "AssetType": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "Name": str,
        "Origin": Literal["OWNED", "ENTITLED"],
        "OriginDetails": ListDataSetsPaginateResponseDataSetsOriginDetailsTypeDef,
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

ListDataSetsPaginateResponseTypeDef = TypedDict(
    "ListDataSetsPaginateResponseTypeDef",
    {"DataSets": List[ListDataSetsPaginateResponseDataSetsTypeDef]},
    total=False,
)

ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListJobsPaginateResponseJobsDetailsExportAssetToSignedUrlTypeDef = TypedDict(
    "ListJobsPaginateResponseJobsDetailsExportAssetToSignedUrlTypeDef",
    {
        "AssetId": str,
        "DataSetId": str,
        "RevisionId": str,
        "SignedUrl": str,
        "SignedUrlExpiresAt": datetime,
    },
    total=False,
)

ListJobsPaginateResponseJobsDetailsExportAssetsToS3AssetDestinationsTypeDef = TypedDict(
    "ListJobsPaginateResponseJobsDetailsExportAssetsToS3AssetDestinationsTypeDef",
    {"AssetId": str, "Bucket": str, "Key": str},
    total=False,
)

ListJobsPaginateResponseJobsDetailsExportAssetsToS3TypeDef = TypedDict(
    "ListJobsPaginateResponseJobsDetailsExportAssetsToS3TypeDef",
    {
        "AssetDestinations": List[
            ListJobsPaginateResponseJobsDetailsExportAssetsToS3AssetDestinationsTypeDef
        ],
        "DataSetId": str,
        "RevisionId": str,
    },
    total=False,
)

ListJobsPaginateResponseJobsDetailsImportAssetFromSignedUrlTypeDef = TypedDict(
    "ListJobsPaginateResponseJobsDetailsImportAssetFromSignedUrlTypeDef",
    {
        "AssetName": str,
        "DataSetId": str,
        "Md5Hash": str,
        "RevisionId": str,
        "SignedUrl": str,
        "SignedUrlExpiresAt": datetime,
    },
    total=False,
)

ListJobsPaginateResponseJobsDetailsImportAssetsFromS3AssetSourcesTypeDef = TypedDict(
    "ListJobsPaginateResponseJobsDetailsImportAssetsFromS3AssetSourcesTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ListJobsPaginateResponseJobsDetailsImportAssetsFromS3TypeDef = TypedDict(
    "ListJobsPaginateResponseJobsDetailsImportAssetsFromS3TypeDef",
    {
        "AssetSources": List[
            ListJobsPaginateResponseJobsDetailsImportAssetsFromS3AssetSourcesTypeDef
        ],
        "DataSetId": str,
        "RevisionId": str,
    },
    total=False,
)

ListJobsPaginateResponseJobsDetailsTypeDef = TypedDict(
    "ListJobsPaginateResponseJobsDetailsTypeDef",
    {
        "ExportAssetToSignedUrl": ListJobsPaginateResponseJobsDetailsExportAssetToSignedUrlTypeDef,
        "ExportAssetsToS3": ListJobsPaginateResponseJobsDetailsExportAssetsToS3TypeDef,
        "ImportAssetFromSignedUrl": ListJobsPaginateResponseJobsDetailsImportAssetFromSignedUrlTypeDef,
        "ImportAssetsFromS3": ListJobsPaginateResponseJobsDetailsImportAssetsFromS3TypeDef,
    },
    total=False,
)

ListJobsPaginateResponseJobsErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef = TypedDict(
    "ListJobsPaginateResponseJobsErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    {"AssetName": str},
    total=False,
)

ListJobsPaginateResponseJobsErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef = TypedDict(
    "ListJobsPaginateResponseJobsErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef",
    {"Bucket": str, "Key": str},
    total=False,
)

ListJobsPaginateResponseJobsErrorsDetailsTypeDef = TypedDict(
    "ListJobsPaginateResponseJobsErrorsDetailsTypeDef",
    {
        "ImportAssetFromSignedUrlJobErrorDetails": ListJobsPaginateResponseJobsErrorsDetailsImportAssetFromSignedUrlJobErrorDetailsTypeDef,
        "ImportAssetsFromS3JobErrorDetails": List[
            ListJobsPaginateResponseJobsErrorsDetailsImportAssetsFromS3JobErrorDetailsTypeDef
        ],
    },
    total=False,
)

ListJobsPaginateResponseJobsErrorsTypeDef = TypedDict(
    "ListJobsPaginateResponseJobsErrorsTypeDef",
    {
        "Code": Literal[
            "ACCESS_DENIED_EXCEPTION",
            "INTERNAL_SERVER_EXCEPTION",
            "MALWARE_DETECTED",
            "RESOURCE_NOT_FOUND_EXCEPTION",
            "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
            "VALIDATION_EXCEPTION",
            "MALWARE_SCAN_ENCRYPTED_FILE",
        ],
        "Details": ListJobsPaginateResponseJobsErrorsDetailsTypeDef,
        "LimitName": Literal["Assets per revision", "Asset size in GB"],
        "LimitValue": float,
        "Message": str,
        "ResourceId": str,
        "ResourceType": Literal["REVISION", "ASSET"],
    },
    total=False,
)

ListJobsPaginateResponseJobsTypeDef = TypedDict(
    "ListJobsPaginateResponseJobsTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": ListJobsPaginateResponseJobsDetailsTypeDef,
        "Errors": List[ListJobsPaginateResponseJobsErrorsTypeDef],
        "Id": str,
        "State": Literal["WAITING", "IN_PROGRESS", "ERROR", "COMPLETED", "CANCELLED", "TIMED_OUT"],
        "Type": Literal[
            "IMPORT_ASSETS_FROM_S3",
            "IMPORT_ASSET_FROM_SIGNED_URL",
            "EXPORT_ASSETS_TO_S3",
            "EXPORT_ASSET_TO_SIGNED_URL",
        ],
        "UpdatedAt": datetime,
    },
    total=False,
)

ListJobsPaginateResponseTypeDef = TypedDict(
    "ListJobsPaginateResponseTypeDef",
    {"Jobs": List[ListJobsPaginateResponseJobsTypeDef]},
    total=False,
)

ListRevisionAssetsPaginatePaginationConfigTypeDef = TypedDict(
    "ListRevisionAssetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListRevisionAssetsPaginateResponseAssetsAssetDetailsS3SnapshotAssetTypeDef = TypedDict(
    "ListRevisionAssetsPaginateResponseAssetsAssetDetailsS3SnapshotAssetTypeDef",
    {"Size": float},
    total=False,
)

ListRevisionAssetsPaginateResponseAssetsAssetDetailsTypeDef = TypedDict(
    "ListRevisionAssetsPaginateResponseAssetsAssetDetailsTypeDef",
    {"S3SnapshotAsset": ListRevisionAssetsPaginateResponseAssetsAssetDetailsS3SnapshotAssetTypeDef},
    total=False,
)

ListRevisionAssetsPaginateResponseAssetsTypeDef = TypedDict(
    "ListRevisionAssetsPaginateResponseAssetsTypeDef",
    {
        "Arn": str,
        "AssetDetails": ListRevisionAssetsPaginateResponseAssetsAssetDetailsTypeDef,
        "AssetType": str,
        "CreatedAt": datetime,
        "DataSetId": str,
        "Id": str,
        "Name": str,
        "RevisionId": str,
        "SourceId": str,
        "UpdatedAt": datetime,
    },
    total=False,
)

ListRevisionAssetsPaginateResponseTypeDef = TypedDict(
    "ListRevisionAssetsPaginateResponseTypeDef",
    {"Assets": List[ListRevisionAssetsPaginateResponseAssetsTypeDef]},
    total=False,
)
