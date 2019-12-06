"Main interface for signer service type defs"
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


ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef = TypedDict(
    "ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": Literal["RSA", "ECDSA"], "hashAlgorithm": Literal["SHA1", "SHA256"]},
    total=False,
)

ClientDescribeSigningJobResponseoverridesTypeDef = TypedDict(
    "ClientDescribeSigningJobResponseoverridesTypeDef",
    {"signingConfiguration": ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef},
    total=False,
)

ClientDescribeSigningJobResponsesignedObjects3TypeDef = TypedDict(
    "ClientDescribeSigningJobResponsesignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)

ClientDescribeSigningJobResponsesignedObjectTypeDef = TypedDict(
    "ClientDescribeSigningJobResponsesignedObjectTypeDef",
    {"s3": ClientDescribeSigningJobResponsesignedObjects3TypeDef},
    total=False,
)

ClientDescribeSigningJobResponsesigningMaterialTypeDef = TypedDict(
    "ClientDescribeSigningJobResponsesigningMaterialTypeDef", {"certificateArn": str}, total=False
)

ClientDescribeSigningJobResponsesources3TypeDef = TypedDict(
    "ClientDescribeSigningJobResponsesources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)

ClientDescribeSigningJobResponsesourceTypeDef = TypedDict(
    "ClientDescribeSigningJobResponsesourceTypeDef",
    {"s3": ClientDescribeSigningJobResponsesources3TypeDef},
    total=False,
)

ClientDescribeSigningJobResponseTypeDef = TypedDict(
    "ClientDescribeSigningJobResponseTypeDef",
    {
        "jobId": str,
        "source": ClientDescribeSigningJobResponsesourceTypeDef,
        "signingMaterial": ClientDescribeSigningJobResponsesigningMaterialTypeDef,
        "platformId": str,
        "profileName": str,
        "overrides": ClientDescribeSigningJobResponseoverridesTypeDef,
        "signingParameters": Dict[str, str],
        "createdAt": datetime,
        "completedAt": datetime,
        "requestedBy": str,
        "status": Literal["InProgress", "Failed", "Succeeded"],
        "statusReason": str,
        "signedObject": ClientDescribeSigningJobResponsesignedObjectTypeDef,
    },
    total=False,
)

ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["RSA", "ECDSA"]], "defaultValue": Literal["RSA", "ECDSA"]},
    total=False,
)

ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["SHA1", "SHA256"]], "defaultValue": Literal["SHA1", "SHA256"]},
    total=False,
)

ClientGetSigningPlatformResponsesigningConfigurationTypeDef = TypedDict(
    "ClientGetSigningPlatformResponsesigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)

ClientGetSigningPlatformResponsesigningImageFormatTypeDef = TypedDict(
    "ClientGetSigningPlatformResponsesigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)

ClientGetSigningPlatformResponseTypeDef = TypedDict(
    "ClientGetSigningPlatformResponseTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": str,
        "signingConfiguration": ClientGetSigningPlatformResponsesigningConfigurationTypeDef,
        "signingImageFormat": ClientGetSigningPlatformResponsesigningImageFormatTypeDef,
        "maxSizeInMB": int,
    },
    total=False,
)

ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef = TypedDict(
    "ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": Literal["RSA", "ECDSA"], "hashAlgorithm": Literal["SHA1", "SHA256"]},
    total=False,
)

ClientGetSigningProfileResponseoverridesTypeDef = TypedDict(
    "ClientGetSigningProfileResponseoverridesTypeDef",
    {"signingConfiguration": ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef},
    total=False,
)

ClientGetSigningProfileResponsesigningMaterialTypeDef = TypedDict(
    "ClientGetSigningProfileResponsesigningMaterialTypeDef", {"certificateArn": str}, total=False
)

ClientGetSigningProfileResponseTypeDef = TypedDict(
    "ClientGetSigningProfileResponseTypeDef",
    {
        "profileName": str,
        "signingMaterial": ClientGetSigningProfileResponsesigningMaterialTypeDef,
        "platformId": str,
        "overrides": ClientGetSigningProfileResponseoverridesTypeDef,
        "signingParameters": Dict[str, str],
        "status": Literal["Active", "Canceled"],
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListSigningJobsResponsejobssignedObjects3TypeDef = TypedDict(
    "ClientListSigningJobsResponsejobssignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)

ClientListSigningJobsResponsejobssignedObjectTypeDef = TypedDict(
    "ClientListSigningJobsResponsejobssignedObjectTypeDef",
    {"s3": ClientListSigningJobsResponsejobssignedObjects3TypeDef},
    total=False,
)

ClientListSigningJobsResponsejobssigningMaterialTypeDef = TypedDict(
    "ClientListSigningJobsResponsejobssigningMaterialTypeDef", {"certificateArn": str}, total=False
)

ClientListSigningJobsResponsejobssources3TypeDef = TypedDict(
    "ClientListSigningJobsResponsejobssources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)

ClientListSigningJobsResponsejobssourceTypeDef = TypedDict(
    "ClientListSigningJobsResponsejobssourceTypeDef",
    {"s3": ClientListSigningJobsResponsejobssources3TypeDef},
    total=False,
)

ClientListSigningJobsResponsejobsTypeDef = TypedDict(
    "ClientListSigningJobsResponsejobsTypeDef",
    {
        "jobId": str,
        "source": ClientListSigningJobsResponsejobssourceTypeDef,
        "signedObject": ClientListSigningJobsResponsejobssignedObjectTypeDef,
        "signingMaterial": ClientListSigningJobsResponsejobssigningMaterialTypeDef,
        "createdAt": datetime,
        "status": Literal["InProgress", "Failed", "Succeeded"],
    },
    total=False,
)

ClientListSigningJobsResponseTypeDef = TypedDict(
    "ClientListSigningJobsResponseTypeDef",
    {"jobs": List[ClientListSigningJobsResponsejobsTypeDef], "nextToken": str},
    total=False,
)

ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["RSA", "ECDSA"]], "defaultValue": Literal["RSA", "ECDSA"]},
    total=False,
)

ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["SHA1", "SHA256"]], "defaultValue": Literal["SHA1", "SHA256"]},
    total=False,
)

ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)

ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)

ClientListSigningPlatformsResponseplatformsTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseplatformsTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": str,
        "signingConfiguration": ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef,
        "signingImageFormat": ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef,
        "maxSizeInMB": int,
    },
    total=False,
)

ClientListSigningPlatformsResponseTypeDef = TypedDict(
    "ClientListSigningPlatformsResponseTypeDef",
    {"platforms": List[ClientListSigningPlatformsResponseplatformsTypeDef], "nextToken": str},
    total=False,
)

ClientListSigningProfilesResponseprofilessigningMaterialTypeDef = TypedDict(
    "ClientListSigningProfilesResponseprofilessigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)

ClientListSigningProfilesResponseprofilesTypeDef = TypedDict(
    "ClientListSigningProfilesResponseprofilesTypeDef",
    {
        "profileName": str,
        "signingMaterial": ClientListSigningProfilesResponseprofilessigningMaterialTypeDef,
        "platformId": str,
        "signingParameters": Dict[str, str],
        "status": Literal["Active", "Canceled"],
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListSigningProfilesResponseTypeDef = TypedDict(
    "ClientListSigningProfilesResponseTypeDef",
    {"profiles": List[ClientListSigningProfilesResponseprofilesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientPutSigningProfileOverridessigningConfigurationTypeDef = TypedDict(
    "ClientPutSigningProfileOverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": Literal["RSA", "ECDSA"], "hashAlgorithm": Literal["SHA1", "SHA256"]},
    total=False,
)

ClientPutSigningProfileOverridesTypeDef = TypedDict(
    "ClientPutSigningProfileOverridesTypeDef",
    {"signingConfiguration": ClientPutSigningProfileOverridessigningConfigurationTypeDef},
    total=False,
)

ClientPutSigningProfileResponseTypeDef = TypedDict(
    "ClientPutSigningProfileResponseTypeDef", {"arn": str}, total=False
)

ClientPutSigningProfileSigningMaterialTypeDef = TypedDict(
    "ClientPutSigningProfileSigningMaterialTypeDef", {"certificateArn": str}
)

ClientStartSigningJobDestinations3TypeDef = TypedDict(
    "ClientStartSigningJobDestinations3TypeDef", {"bucketName": str, "prefix": str}, total=False
)

ClientStartSigningJobDestinationTypeDef = TypedDict(
    "ClientStartSigningJobDestinationTypeDef",
    {"s3": ClientStartSigningJobDestinations3TypeDef},
    total=False,
)

ClientStartSigningJobResponseTypeDef = TypedDict(
    "ClientStartSigningJobResponseTypeDef", {"jobId": str}, total=False
)

_RequiredClientStartSigningJobSources3TypeDef = TypedDict(
    "_RequiredClientStartSigningJobSources3TypeDef", {"bucketName": str}
)
_OptionalClientStartSigningJobSources3TypeDef = TypedDict(
    "_OptionalClientStartSigningJobSources3TypeDef", {"key": str, "version": str}, total=False
)


class ClientStartSigningJobSources3TypeDef(
    _RequiredClientStartSigningJobSources3TypeDef, _OptionalClientStartSigningJobSources3TypeDef
):
    pass


ClientStartSigningJobSourceTypeDef = TypedDict(
    "ClientStartSigningJobSourceTypeDef", {"s3": ClientStartSigningJobSources3TypeDef}, total=False
)

ListSigningJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListSigningJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSigningJobsPaginateResponsejobssignedObjects3TypeDef = TypedDict(
    "ListSigningJobsPaginateResponsejobssignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)

ListSigningJobsPaginateResponsejobssignedObjectTypeDef = TypedDict(
    "ListSigningJobsPaginateResponsejobssignedObjectTypeDef",
    {"s3": ListSigningJobsPaginateResponsejobssignedObjects3TypeDef},
    total=False,
)

ListSigningJobsPaginateResponsejobssigningMaterialTypeDef = TypedDict(
    "ListSigningJobsPaginateResponsejobssigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)

ListSigningJobsPaginateResponsejobssources3TypeDef = TypedDict(
    "ListSigningJobsPaginateResponsejobssources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)

ListSigningJobsPaginateResponsejobssourceTypeDef = TypedDict(
    "ListSigningJobsPaginateResponsejobssourceTypeDef",
    {"s3": ListSigningJobsPaginateResponsejobssources3TypeDef},
    total=False,
)

ListSigningJobsPaginateResponsejobsTypeDef = TypedDict(
    "ListSigningJobsPaginateResponsejobsTypeDef",
    {
        "jobId": str,
        "source": ListSigningJobsPaginateResponsejobssourceTypeDef,
        "signedObject": ListSigningJobsPaginateResponsejobssignedObjectTypeDef,
        "signingMaterial": ListSigningJobsPaginateResponsejobssigningMaterialTypeDef,
        "createdAt": datetime,
        "status": Literal["InProgress", "Failed", "Succeeded"],
    },
    total=False,
)

ListSigningJobsPaginateResponseTypeDef = TypedDict(
    "ListSigningJobsPaginateResponseTypeDef",
    {"jobs": List[ListSigningJobsPaginateResponsejobsTypeDef], "NextToken": str},
    total=False,
)

ListSigningPlatformsPaginatePaginationConfigTypeDef = TypedDict(
    "ListSigningPlatformsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["RSA", "ECDSA"]], "defaultValue": Literal["RSA", "ECDSA"]},
    total=False,
)

ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["SHA1", "SHA256"]], "defaultValue": Literal["SHA1", "SHA256"]},
    total=False,
)

ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef = TypedDict(
    "ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)

ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef = TypedDict(
    "ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)

ListSigningPlatformsPaginateResponseplatformsTypeDef = TypedDict(
    "ListSigningPlatformsPaginateResponseplatformsTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": str,
        "signingConfiguration": ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef,
        "signingImageFormat": ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef,
        "maxSizeInMB": int,
    },
    total=False,
)

ListSigningPlatformsPaginateResponseTypeDef = TypedDict(
    "ListSigningPlatformsPaginateResponseTypeDef",
    {"platforms": List[ListSigningPlatformsPaginateResponseplatformsTypeDef], "NextToken": str},
    total=False,
)

ListSigningProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "ListSigningProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef = TypedDict(
    "ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)

ListSigningProfilesPaginateResponseprofilesTypeDef = TypedDict(
    "ListSigningProfilesPaginateResponseprofilesTypeDef",
    {
        "profileName": str,
        "signingMaterial": ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef,
        "platformId": str,
        "signingParameters": Dict[str, str],
        "status": Literal["Active", "Canceled"],
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ListSigningProfilesPaginateResponseTypeDef = TypedDict(
    "ListSigningProfilesPaginateResponseTypeDef",
    {"profiles": List[ListSigningProfilesPaginateResponseprofilesTypeDef], "NextToken": str},
    total=False,
)

SuccessfulSigningJobWaitWaiterConfigTypeDef = TypedDict(
    "SuccessfulSigningJobWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
