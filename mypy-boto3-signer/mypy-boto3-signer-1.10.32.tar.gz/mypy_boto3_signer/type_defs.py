"Main interface for signer service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef",
    "ClientDescribeSigningJobResponseoverridesTypeDef",
    "ClientDescribeSigningJobResponsesignedObjects3TypeDef",
    "ClientDescribeSigningJobResponsesignedObjectTypeDef",
    "ClientDescribeSigningJobResponsesigningMaterialTypeDef",
    "ClientDescribeSigningJobResponsesources3TypeDef",
    "ClientDescribeSigningJobResponsesourceTypeDef",
    "ClientDescribeSigningJobResponseTypeDef",
    "ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef",
    "ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef",
    "ClientGetSigningPlatformResponsesigningConfigurationTypeDef",
    "ClientGetSigningPlatformResponsesigningImageFormatTypeDef",
    "ClientGetSigningPlatformResponseTypeDef",
    "ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef",
    "ClientGetSigningProfileResponseoverridesTypeDef",
    "ClientGetSigningProfileResponsesigningMaterialTypeDef",
    "ClientGetSigningProfileResponseTypeDef",
    "ClientListSigningJobsResponsejobssignedObjects3TypeDef",
    "ClientListSigningJobsResponsejobssignedObjectTypeDef",
    "ClientListSigningJobsResponsejobssigningMaterialTypeDef",
    "ClientListSigningJobsResponsejobssources3TypeDef",
    "ClientListSigningJobsResponsejobssourceTypeDef",
    "ClientListSigningJobsResponsejobsTypeDef",
    "ClientListSigningJobsResponseTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef",
    "ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef",
    "ClientListSigningPlatformsResponseplatformsTypeDef",
    "ClientListSigningPlatformsResponseTypeDef",
    "ClientListSigningProfilesResponseprofilessigningMaterialTypeDef",
    "ClientListSigningProfilesResponseprofilesTypeDef",
    "ClientListSigningProfilesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutSigningProfileOverridessigningConfigurationTypeDef",
    "ClientPutSigningProfileOverridesTypeDef",
    "ClientPutSigningProfileResponseTypeDef",
    "ClientPutSigningProfileSigningMaterialTypeDef",
    "ClientStartSigningJobDestinations3TypeDef",
    "ClientStartSigningJobDestinationTypeDef",
    "ClientStartSigningJobResponseTypeDef",
    "ClientStartSigningJobSources3TypeDef",
    "ClientStartSigningJobSourceTypeDef",
    "ListSigningJobsPaginatePaginationConfigTypeDef",
    "ListSigningJobsPaginateResponsejobssignedObjects3TypeDef",
    "ListSigningJobsPaginateResponsejobssignedObjectTypeDef",
    "ListSigningJobsPaginateResponsejobssigningMaterialTypeDef",
    "ListSigningJobsPaginateResponsejobssources3TypeDef",
    "ListSigningJobsPaginateResponsejobssourceTypeDef",
    "ListSigningJobsPaginateResponsejobsTypeDef",
    "ListSigningJobsPaginateResponseTypeDef",
    "ListSigningPlatformsPaginatePaginationConfigTypeDef",
    "ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    "ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    "ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef",
    "ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef",
    "ListSigningPlatformsPaginateResponseplatformsTypeDef",
    "ListSigningPlatformsPaginateResponseTypeDef",
    "ListSigningProfilesPaginatePaginationConfigTypeDef",
    "ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef",
    "ListSigningProfilesPaginateResponseprofilesTypeDef",
    "ListSigningProfilesPaginateResponseTypeDef",
    "SuccessfulSigningJobWaitWaiterConfigTypeDef",
)


_ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": Literal["RSA", "ECDSA"], "hashAlgorithm": Literal["SHA1", "SHA256"]},
    total=False,
)


class ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef(
    _ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef
):
    pass


_ClientDescribeSigningJobResponseoverridesTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponseoverridesTypeDef",
    {"signingConfiguration": ClientDescribeSigningJobResponseoverridessigningConfigurationTypeDef},
    total=False,
)


class ClientDescribeSigningJobResponseoverridesTypeDef(
    _ClientDescribeSigningJobResponseoverridesTypeDef
):
    pass


_ClientDescribeSigningJobResponsesignedObjects3TypeDef = TypedDict(
    "_ClientDescribeSigningJobResponsesignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)


class ClientDescribeSigningJobResponsesignedObjects3TypeDef(
    _ClientDescribeSigningJobResponsesignedObjects3TypeDef
):
    pass


_ClientDescribeSigningJobResponsesignedObjectTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponsesignedObjectTypeDef",
    {"s3": ClientDescribeSigningJobResponsesignedObjects3TypeDef},
    total=False,
)


class ClientDescribeSigningJobResponsesignedObjectTypeDef(
    _ClientDescribeSigningJobResponsesignedObjectTypeDef
):
    pass


_ClientDescribeSigningJobResponsesigningMaterialTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponsesigningMaterialTypeDef", {"certificateArn": str}, total=False
)


class ClientDescribeSigningJobResponsesigningMaterialTypeDef(
    _ClientDescribeSigningJobResponsesigningMaterialTypeDef
):
    pass


_ClientDescribeSigningJobResponsesources3TypeDef = TypedDict(
    "_ClientDescribeSigningJobResponsesources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)


class ClientDescribeSigningJobResponsesources3TypeDef(
    _ClientDescribeSigningJobResponsesources3TypeDef
):
    pass


_ClientDescribeSigningJobResponsesourceTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponsesourceTypeDef",
    {"s3": ClientDescribeSigningJobResponsesources3TypeDef},
    total=False,
)


class ClientDescribeSigningJobResponsesourceTypeDef(_ClientDescribeSigningJobResponsesourceTypeDef):
    pass


_ClientDescribeSigningJobResponseTypeDef = TypedDict(
    "_ClientDescribeSigningJobResponseTypeDef",
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


class ClientDescribeSigningJobResponseTypeDef(_ClientDescribeSigningJobResponseTypeDef):
    """
    - *(dict) --*

      - **jobId** *(string) --*

        The ID of the signing job on output.
    """


_ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "_ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["RSA", "ECDSA"]], "defaultValue": Literal["RSA", "ECDSA"]},
    total=False,
)


class ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef(
    _ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef
):
    pass


_ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "_ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["SHA1", "SHA256"]], "defaultValue": Literal["SHA1", "SHA256"]},
    total=False,
)


class ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef(
    _ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef
):
    pass


_ClientGetSigningPlatformResponsesigningConfigurationTypeDef = TypedDict(
    "_ClientGetSigningPlatformResponsesigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ClientGetSigningPlatformResponsesigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ClientGetSigningPlatformResponsesigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)


class ClientGetSigningPlatformResponsesigningConfigurationTypeDef(
    _ClientGetSigningPlatformResponsesigningConfigurationTypeDef
):
    pass


_ClientGetSigningPlatformResponsesigningImageFormatTypeDef = TypedDict(
    "_ClientGetSigningPlatformResponsesigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)


class ClientGetSigningPlatformResponsesigningImageFormatTypeDef(
    _ClientGetSigningPlatformResponsesigningImageFormatTypeDef
):
    pass


_ClientGetSigningPlatformResponseTypeDef = TypedDict(
    "_ClientGetSigningPlatformResponseTypeDef",
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


class ClientGetSigningPlatformResponseTypeDef(_ClientGetSigningPlatformResponseTypeDef):
    """
    - *(dict) --*

      - **platformId** *(string) --*

        The ID of the target signing platform.
    """


_ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef = TypedDict(
    "_ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": Literal["RSA", "ECDSA"], "hashAlgorithm": Literal["SHA1", "SHA256"]},
    total=False,
)


class ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef(
    _ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef
):
    pass


_ClientGetSigningProfileResponseoverridesTypeDef = TypedDict(
    "_ClientGetSigningProfileResponseoverridesTypeDef",
    {"signingConfiguration": ClientGetSigningProfileResponseoverridessigningConfigurationTypeDef},
    total=False,
)


class ClientGetSigningProfileResponseoverridesTypeDef(
    _ClientGetSigningProfileResponseoverridesTypeDef
):
    pass


_ClientGetSigningProfileResponsesigningMaterialTypeDef = TypedDict(
    "_ClientGetSigningProfileResponsesigningMaterialTypeDef", {"certificateArn": str}, total=False
)


class ClientGetSigningProfileResponsesigningMaterialTypeDef(
    _ClientGetSigningProfileResponsesigningMaterialTypeDef
):
    pass


_ClientGetSigningProfileResponseTypeDef = TypedDict(
    "_ClientGetSigningProfileResponseTypeDef",
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


class ClientGetSigningProfileResponseTypeDef(_ClientGetSigningProfileResponseTypeDef):
    """
    - *(dict) --*

      - **profileName** *(string) --*

        The name of the target signing profile.
    """


_ClientListSigningJobsResponsejobssignedObjects3TypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobssignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)


class ClientListSigningJobsResponsejobssignedObjects3TypeDef(
    _ClientListSigningJobsResponsejobssignedObjects3TypeDef
):
    pass


_ClientListSigningJobsResponsejobssignedObjectTypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobssignedObjectTypeDef",
    {"s3": ClientListSigningJobsResponsejobssignedObjects3TypeDef},
    total=False,
)


class ClientListSigningJobsResponsejobssignedObjectTypeDef(
    _ClientListSigningJobsResponsejobssignedObjectTypeDef
):
    pass


_ClientListSigningJobsResponsejobssigningMaterialTypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobssigningMaterialTypeDef", {"certificateArn": str}, total=False
)


class ClientListSigningJobsResponsejobssigningMaterialTypeDef(
    _ClientListSigningJobsResponsejobssigningMaterialTypeDef
):
    pass


_ClientListSigningJobsResponsejobssources3TypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobssources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)


class ClientListSigningJobsResponsejobssources3TypeDef(
    _ClientListSigningJobsResponsejobssources3TypeDef
):
    pass


_ClientListSigningJobsResponsejobssourceTypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobssourceTypeDef",
    {"s3": ClientListSigningJobsResponsejobssources3TypeDef},
    total=False,
)


class ClientListSigningJobsResponsejobssourceTypeDef(
    _ClientListSigningJobsResponsejobssourceTypeDef
):
    pass


_ClientListSigningJobsResponsejobsTypeDef = TypedDict(
    "_ClientListSigningJobsResponsejobsTypeDef",
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


class ClientListSigningJobsResponsejobsTypeDef(_ClientListSigningJobsResponsejobsTypeDef):
    """
    - *(dict) --*

      Contains information about a signing job.
      - **jobId** *(string) --*

        The ID of the signing job.
    """


_ClientListSigningJobsResponseTypeDef = TypedDict(
    "_ClientListSigningJobsResponseTypeDef",
    {"jobs": List[ClientListSigningJobsResponsejobsTypeDef], "nextToken": str},
    total=False,
)


class ClientListSigningJobsResponseTypeDef(_ClientListSigningJobsResponseTypeDef):
    """
    - *(dict) --*

      - **jobs** *(list) --*

        A list of your signing jobs.
        - *(dict) --*

          Contains information about a signing job.
          - **jobId** *(string) --*

            The ID of the signing job.
    """


_ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["RSA", "ECDSA"]], "defaultValue": Literal["RSA", "ECDSA"]},
    total=False,
)


class ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef(
    _ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef
):
    pass


_ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["SHA1", "SHA256"]], "defaultValue": Literal["SHA1", "SHA256"]},
    total=False,
)


class ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef(
    _ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef
):
    pass


_ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ClientListSigningPlatformsResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ClientListSigningPlatformsResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)


class ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef(
    _ClientListSigningPlatformsResponseplatformssigningConfigurationTypeDef
):
    pass


_ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)


class ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef(
    _ClientListSigningPlatformsResponseplatformssigningImageFormatTypeDef
):
    pass


_ClientListSigningPlatformsResponseplatformsTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseplatformsTypeDef",
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


class ClientListSigningPlatformsResponseplatformsTypeDef(
    _ClientListSigningPlatformsResponseplatformsTypeDef
):
    """
    - *(dict) --*

      Contains information about the signing configurations and parameters that is used to perform a
      code signing job.
      - **platformId** *(string) --*

        The ID of a code signing; platform.
    """


_ClientListSigningPlatformsResponseTypeDef = TypedDict(
    "_ClientListSigningPlatformsResponseTypeDef",
    {"platforms": List[ClientListSigningPlatformsResponseplatformsTypeDef], "nextToken": str},
    total=False,
)


class ClientListSigningPlatformsResponseTypeDef(_ClientListSigningPlatformsResponseTypeDef):
    """
    - *(dict) --*

      - **platforms** *(list) --*

        A list of all platforms that match the request parameters.
        - *(dict) --*

          Contains information about the signing configurations and parameters that is used to
          perform a code signing job.
          - **platformId** *(string) --*

            The ID of a code signing; platform.
    """


_ClientListSigningProfilesResponseprofilessigningMaterialTypeDef = TypedDict(
    "_ClientListSigningProfilesResponseprofilessigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)


class ClientListSigningProfilesResponseprofilessigningMaterialTypeDef(
    _ClientListSigningProfilesResponseprofilessigningMaterialTypeDef
):
    pass


_ClientListSigningProfilesResponseprofilesTypeDef = TypedDict(
    "_ClientListSigningProfilesResponseprofilesTypeDef",
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


class ClientListSigningProfilesResponseprofilesTypeDef(
    _ClientListSigningProfilesResponseprofilesTypeDef
):
    """
    - *(dict) --*

      Contains information about the ACM certificates and code signing configuration parameters that
      can be used by a given code signing user.
      - **profileName** *(string) --*

        The name of the signing profile.
    """


_ClientListSigningProfilesResponseTypeDef = TypedDict(
    "_ClientListSigningProfilesResponseTypeDef",
    {"profiles": List[ClientListSigningProfilesResponseprofilesTypeDef], "nextToken": str},
    total=False,
)


class ClientListSigningProfilesResponseTypeDef(_ClientListSigningProfilesResponseTypeDef):
    """
    - *(dict) --*

      - **profiles** *(list) --*

        A list of profiles that are available in the AWS account. This includes profiles with the
        status of ``CANCELED`` if the ``includeCanceled`` parameter is set to ``true`` .
        - *(dict) --*

          Contains information about the ACM certificates and code signing configuration parameters
          that can be used by a given code signing user.
          - **profileName** *(string) --*

            The name of the signing profile.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        A list of tags associated with the signing profile.
        - *(string) --*

          - *(string) --*
    """


_ClientPutSigningProfileOverridessigningConfigurationTypeDef = TypedDict(
    "_ClientPutSigningProfileOverridessigningConfigurationTypeDef",
    {"encryptionAlgorithm": Literal["RSA", "ECDSA"], "hashAlgorithm": Literal["SHA1", "SHA256"]},
    total=False,
)


class ClientPutSigningProfileOverridessigningConfigurationTypeDef(
    _ClientPutSigningProfileOverridessigningConfigurationTypeDef
):
    """
    - **signingConfiguration** *(dict) --*

      A signing configuration that overrides the default encryption or hash algorithm of a signing
      job.
      - **encryptionAlgorithm** *(string) --*

        A specified override of the default encryption algorithm that is used in a code signing job.
    """


_ClientPutSigningProfileOverridesTypeDef = TypedDict(
    "_ClientPutSigningProfileOverridesTypeDef",
    {"signingConfiguration": ClientPutSigningProfileOverridessigningConfigurationTypeDef},
    total=False,
)


class ClientPutSigningProfileOverridesTypeDef(_ClientPutSigningProfileOverridesTypeDef):
    """
    A subfield of ``platform`` . This specifies any different configuration options that you want to
    apply to the chosen platform (such as a different ``hash-algorithm`` or ``signing-algorithm`` ).
    - **signingConfiguration** *(dict) --*

      A signing configuration that overrides the default encryption or hash algorithm of a signing
      job.
      - **encryptionAlgorithm** *(string) --*

        A specified override of the default encryption algorithm that is used in a code signing job.
    """


_ClientPutSigningProfileResponseTypeDef = TypedDict(
    "_ClientPutSigningProfileResponseTypeDef", {"arn": str}, total=False
)


class ClientPutSigningProfileResponseTypeDef(_ClientPutSigningProfileResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the signing profile created.
    """


_ClientPutSigningProfileSigningMaterialTypeDef = TypedDict(
    "_ClientPutSigningProfileSigningMaterialTypeDef", {"certificateArn": str}
)


class ClientPutSigningProfileSigningMaterialTypeDef(_ClientPutSigningProfileSigningMaterialTypeDef):
    """
    The AWS Certificate Manager certificate that will be used to sign code with the new signing
    profile.
    - **certificateArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) of the certificates that is used to sign your code.
    """


_ClientStartSigningJobDestinations3TypeDef = TypedDict(
    "_ClientStartSigningJobDestinations3TypeDef", {"bucketName": str, "prefix": str}, total=False
)


class ClientStartSigningJobDestinations3TypeDef(_ClientStartSigningJobDestinations3TypeDef):
    """
    - **s3** *(dict) --*

      The ``S3Destination`` object.
      - **bucketName** *(string) --*

        Name of the S3 bucket.
    """


_ClientStartSigningJobDestinationTypeDef = TypedDict(
    "_ClientStartSigningJobDestinationTypeDef",
    {"s3": ClientStartSigningJobDestinations3TypeDef},
    total=False,
)


class ClientStartSigningJobDestinationTypeDef(_ClientStartSigningJobDestinationTypeDef):
    """
    The S3 bucket in which to save your signed object. The destination contains the name of your
    bucket and an optional prefix.
    - **s3** *(dict) --*

      The ``S3Destination`` object.
      - **bucketName** *(string) --*

        Name of the S3 bucket.
    """


_ClientStartSigningJobResponseTypeDef = TypedDict(
    "_ClientStartSigningJobResponseTypeDef", {"jobId": str}, total=False
)


class ClientStartSigningJobResponseTypeDef(_ClientStartSigningJobResponseTypeDef):
    """
    - *(dict) --*

      - **jobId** *(string) --*

        The ID of your signing job.
    """


_RequiredClientStartSigningJobSources3TypeDef = TypedDict(
    "_RequiredClientStartSigningJobSources3TypeDef", {"bucketName": str}
)
_OptionalClientStartSigningJobSources3TypeDef = TypedDict(
    "_OptionalClientStartSigningJobSources3TypeDef", {"key": str, "version": str}, total=False
)


class ClientStartSigningJobSources3TypeDef(
    _RequiredClientStartSigningJobSources3TypeDef, _OptionalClientStartSigningJobSources3TypeDef
):
    """
    - **s3** *(dict) --*

      The ``S3Source`` object.
      - **bucketName** *(string) --***[REQUIRED]**

        Name of the S3 bucket.
    """


_ClientStartSigningJobSourceTypeDef = TypedDict(
    "_ClientStartSigningJobSourceTypeDef", {"s3": ClientStartSigningJobSources3TypeDef}, total=False
)


class ClientStartSigningJobSourceTypeDef(_ClientStartSigningJobSourceTypeDef):
    """
    The S3 bucket that contains the object to sign or a BLOB that contains your raw code.
    - **s3** *(dict) --*

      The ``S3Source`` object.
      - **bucketName** *(string) --***[REQUIRED]**

        Name of the S3 bucket.
    """


_ListSigningJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSigningJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSigningJobsPaginatePaginationConfigTypeDef(
    _ListSigningJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSigningJobsPaginateResponsejobssignedObjects3TypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobssignedObjects3TypeDef",
    {"bucketName": str, "key": str},
    total=False,
)


class ListSigningJobsPaginateResponsejobssignedObjects3TypeDef(
    _ListSigningJobsPaginateResponsejobssignedObjects3TypeDef
):
    pass


_ListSigningJobsPaginateResponsejobssignedObjectTypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobssignedObjectTypeDef",
    {"s3": ListSigningJobsPaginateResponsejobssignedObjects3TypeDef},
    total=False,
)


class ListSigningJobsPaginateResponsejobssignedObjectTypeDef(
    _ListSigningJobsPaginateResponsejobssignedObjectTypeDef
):
    pass


_ListSigningJobsPaginateResponsejobssigningMaterialTypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobssigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)


class ListSigningJobsPaginateResponsejobssigningMaterialTypeDef(
    _ListSigningJobsPaginateResponsejobssigningMaterialTypeDef
):
    pass


_ListSigningJobsPaginateResponsejobssources3TypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobssources3TypeDef",
    {"bucketName": str, "key": str, "version": str},
    total=False,
)


class ListSigningJobsPaginateResponsejobssources3TypeDef(
    _ListSigningJobsPaginateResponsejobssources3TypeDef
):
    pass


_ListSigningJobsPaginateResponsejobssourceTypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobssourceTypeDef",
    {"s3": ListSigningJobsPaginateResponsejobssources3TypeDef},
    total=False,
)


class ListSigningJobsPaginateResponsejobssourceTypeDef(
    _ListSigningJobsPaginateResponsejobssourceTypeDef
):
    pass


_ListSigningJobsPaginateResponsejobsTypeDef = TypedDict(
    "_ListSigningJobsPaginateResponsejobsTypeDef",
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


class ListSigningJobsPaginateResponsejobsTypeDef(_ListSigningJobsPaginateResponsejobsTypeDef):
    """
    - *(dict) --*

      Contains information about a signing job.
      - **jobId** *(string) --*

        The ID of the signing job.
    """


_ListSigningJobsPaginateResponseTypeDef = TypedDict(
    "_ListSigningJobsPaginateResponseTypeDef",
    {"jobs": List[ListSigningJobsPaginateResponsejobsTypeDef], "NextToken": str},
    total=False,
)


class ListSigningJobsPaginateResponseTypeDef(_ListSigningJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **jobs** *(list) --*

        A list of your signing jobs.
        - *(dict) --*

          Contains information about a signing job.
          - **jobId** *(string) --*

            The ID of the signing job.
    """


_ListSigningPlatformsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSigningPlatformsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSigningPlatformsPaginatePaginationConfigTypeDef(
    _ListSigningPlatformsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["RSA", "ECDSA"]], "defaultValue": Literal["RSA", "ECDSA"]},
    total=False,
)


class ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef(
    _ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef
):
    pass


_ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef",
    {"allowedValues": List[Literal["SHA1", "SHA256"]], "defaultValue": Literal["SHA1", "SHA256"]},
    total=False,
)


class ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef(
    _ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef
):
    pass


_ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": ListSigningPlatformsPaginateResponseplatformssigningConfigurationencryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": ListSigningPlatformsPaginateResponseplatformssigningConfigurationhashAlgorithmOptionsTypeDef,
    },
    total=False,
)


class ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef(
    _ListSigningPlatformsPaginateResponseplatformssigningConfigurationTypeDef
):
    pass


_ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef",
    {"supportedFormats": List[str], "defaultFormat": str},
    total=False,
)


class ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef(
    _ListSigningPlatformsPaginateResponseplatformssigningImageFormatTypeDef
):
    pass


_ListSigningPlatformsPaginateResponseplatformsTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseplatformsTypeDef",
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


class ListSigningPlatformsPaginateResponseplatformsTypeDef(
    _ListSigningPlatformsPaginateResponseplatformsTypeDef
):
    """
    - *(dict) --*

      Contains information about the signing configurations and parameters that is used to perform a
      code signing job.
      - **platformId** *(string) --*

        The ID of a code signing; platform.
    """


_ListSigningPlatformsPaginateResponseTypeDef = TypedDict(
    "_ListSigningPlatformsPaginateResponseTypeDef",
    {"platforms": List[ListSigningPlatformsPaginateResponseplatformsTypeDef], "NextToken": str},
    total=False,
)


class ListSigningPlatformsPaginateResponseTypeDef(_ListSigningPlatformsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **platforms** *(list) --*

        A list of all platforms that match the request parameters.
        - *(dict) --*

          Contains information about the signing configurations and parameters that is used to
          perform a code signing job.
          - **platformId** *(string) --*

            The ID of a code signing; platform.
    """


_ListSigningProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSigningProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSigningProfilesPaginatePaginationConfigTypeDef(
    _ListSigningProfilesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef = TypedDict(
    "_ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef",
    {"certificateArn": str},
    total=False,
)


class ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef(
    _ListSigningProfilesPaginateResponseprofilessigningMaterialTypeDef
):
    pass


_ListSigningProfilesPaginateResponseprofilesTypeDef = TypedDict(
    "_ListSigningProfilesPaginateResponseprofilesTypeDef",
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


class ListSigningProfilesPaginateResponseprofilesTypeDef(
    _ListSigningProfilesPaginateResponseprofilesTypeDef
):
    """
    - *(dict) --*

      Contains information about the ACM certificates and code signing configuration parameters that
      can be used by a given code signing user.
      - **profileName** *(string) --*

        The name of the signing profile.
    """


_ListSigningProfilesPaginateResponseTypeDef = TypedDict(
    "_ListSigningProfilesPaginateResponseTypeDef",
    {"profiles": List[ListSigningProfilesPaginateResponseprofilesTypeDef], "NextToken": str},
    total=False,
)


class ListSigningProfilesPaginateResponseTypeDef(_ListSigningProfilesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **profiles** *(list) --*

        A list of profiles that are available in the AWS account. This includes profiles with the
        status of ``CANCELED`` if the ``includeCanceled`` parameter is set to ``true`` .
        - *(dict) --*

          Contains information about the ACM certificates and code signing configuration parameters
          that can be used by a given code signing user.
          - **profileName** *(string) --*

            The name of the signing profile.
    """


_SuccessfulSigningJobWaitWaiterConfigTypeDef = TypedDict(
    "_SuccessfulSigningJobWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class SuccessfulSigningJobWaitWaiterConfigTypeDef(_SuccessfulSigningJobWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 20
    """
