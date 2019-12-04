"Main interface for ecr service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef",
    "ClientBatchCheckLayerAvailabilityResponselayersTypeDef",
    "ClientBatchCheckLayerAvailabilityResponseTypeDef",
    "ClientBatchDeleteImageImageIdsTypeDef",
    "ClientBatchDeleteImageResponsefailuresimageIdTypeDef",
    "ClientBatchDeleteImageResponsefailuresTypeDef",
    "ClientBatchDeleteImageResponseimageIdsTypeDef",
    "ClientBatchDeleteImageResponseTypeDef",
    "ClientBatchGetImageImageIdsTypeDef",
    "ClientBatchGetImageResponsefailuresimageIdTypeDef",
    "ClientBatchGetImageResponsefailuresTypeDef",
    "ClientBatchGetImageResponseimagesimageIdTypeDef",
    "ClientBatchGetImageResponseimagesTypeDef",
    "ClientBatchGetImageResponseTypeDef",
    "ClientCompleteLayerUploadResponseTypeDef",
    "ClientCreateRepositoryImageScanningConfigurationTypeDef",
    "ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    "ClientCreateRepositoryResponserepositoryTypeDef",
    "ClientCreateRepositoryResponseTypeDef",
    "ClientCreateRepositoryTagsTypeDef",
    "ClientDeleteLifecyclePolicyResponseTypeDef",
    "ClientDeleteRepositoryPolicyResponseTypeDef",
    "ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    "ClientDeleteRepositoryResponserepositoryTypeDef",
    "ClientDeleteRepositoryResponseTypeDef",
    "ClientDescribeImageScanFindingsImageIdTypeDef",
    "ClientDescribeImageScanFindingsResponseimageIdTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef",
    "ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef",
    "ClientDescribeImageScanFindingsResponseTypeDef",
    "ClientDescribeImagesFilterTypeDef",
    "ClientDescribeImagesImageIdsTypeDef",
    "ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef",
    "ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef",
    "ClientDescribeImagesResponseimageDetailsTypeDef",
    "ClientDescribeImagesResponseTypeDef",
    "ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef",
    "ClientDescribeRepositoriesResponserepositoriesTypeDef",
    "ClientDescribeRepositoriesResponseTypeDef",
    "ClientGetAuthorizationTokenResponseauthorizationDataTypeDef",
    "ClientGetAuthorizationTokenResponseTypeDef",
    "ClientGetDownloadUrlForLayerResponseTypeDef",
    "ClientGetLifecyclePolicyPreviewFilterTypeDef",
    "ClientGetLifecyclePolicyPreviewImageIdsTypeDef",
    "ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef",
    "ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef",
    "ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef",
    "ClientGetLifecyclePolicyPreviewResponseTypeDef",
    "ClientGetLifecyclePolicyResponseTypeDef",
    "ClientGetRepositoryPolicyResponseTypeDef",
    "ClientInitiateLayerUploadResponseTypeDef",
    "ClientListImagesFilterTypeDef",
    "ClientListImagesResponseimageIdsTypeDef",
    "ClientListImagesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutImageResponseimageimageIdTypeDef",
    "ClientPutImageResponseimageTypeDef",
    "ClientPutImageResponseTypeDef",
    "ClientPutImageScanningConfigurationImageScanningConfigurationTypeDef",
    "ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef",
    "ClientPutImageScanningConfigurationResponseTypeDef",
    "ClientPutImageTagMutabilityResponseTypeDef",
    "ClientPutLifecyclePolicyResponseTypeDef",
    "ClientSetRepositoryPolicyResponseTypeDef",
    "ClientStartImageScanImageIdTypeDef",
    "ClientStartImageScanResponseimageIdTypeDef",
    "ClientStartImageScanResponseimageScanStatusTypeDef",
    "ClientStartImageScanResponseTypeDef",
    "ClientStartLifecyclePolicyPreviewResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUploadLayerPartResponseTypeDef",
    "DescribeImageScanFindingsPaginateImageIdTypeDef",
    "DescribeImageScanFindingsPaginatePaginationConfigTypeDef",
    "DescribeImageScanFindingsPaginateResponseimageIdTypeDef",
    "DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef",
    "DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef",
    "DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef",
    "DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef",
    "DescribeImageScanFindingsPaginateResponseTypeDef",
    "DescribeImagesPaginateFilterTypeDef",
    "DescribeImagesPaginateImageIdsTypeDef",
    "DescribeImagesPaginatePaginationConfigTypeDef",
    "DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef",
    "DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef",
    "DescribeImagesPaginateResponseimageDetailsTypeDef",
    "DescribeImagesPaginateResponseTypeDef",
    "DescribeRepositoriesPaginatePaginationConfigTypeDef",
    "DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef",
    "DescribeRepositoriesPaginateResponserepositoriesTypeDef",
    "DescribeRepositoriesPaginateResponseTypeDef",
    "GetLifecyclePolicyPreviewPaginateFilterTypeDef",
    "GetLifecyclePolicyPreviewPaginateImageIdsTypeDef",
    "GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef",
    "GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef",
    "GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef",
    "GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef",
    "GetLifecyclePolicyPreviewPaginateResponseTypeDef",
    "ListImagesPaginateFilterTypeDef",
    "ListImagesPaginatePaginationConfigTypeDef",
    "ListImagesPaginateResponseimageIdsTypeDef",
    "ListImagesPaginateResponseTypeDef",
)


_ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef = TypedDict(
    "_ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef",
    {
        "layerDigest": str,
        "failureCode": Literal["InvalidLayerDigest", "MissingLayerDigest"],
        "failureReason": str,
    },
    total=False,
)


class ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef(
    _ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef
):
    pass


_ClientBatchCheckLayerAvailabilityResponselayersTypeDef = TypedDict(
    "_ClientBatchCheckLayerAvailabilityResponselayersTypeDef",
    {
        "layerDigest": str,
        "layerAvailability": Literal["AVAILABLE", "UNAVAILABLE"],
        "layerSize": int,
        "mediaType": str,
    },
    total=False,
)


class ClientBatchCheckLayerAvailabilityResponselayersTypeDef(
    _ClientBatchCheckLayerAvailabilityResponselayersTypeDef
):
    """
    - *(dict) --*

      An object representing an Amazon ECR image layer.
      - **layerDigest** *(string) --*

        The ``sha256`` digest of the image layer.
    """


_ClientBatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "_ClientBatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List[ClientBatchCheckLayerAvailabilityResponselayersTypeDef],
        "failures": List[ClientBatchCheckLayerAvailabilityResponsefailuresTypeDef],
    },
    total=False,
)


class ClientBatchCheckLayerAvailabilityResponseTypeDef(
    _ClientBatchCheckLayerAvailabilityResponseTypeDef
):
    """
    - *(dict) --*

      - **layers** *(list) --*

        A list of image layer objects corresponding to the image layer references in the request.
        - *(dict) --*

          An object representing an Amazon ECR image layer.
          - **layerDigest** *(string) --*

            The ``sha256`` digest of the image layer.
    """


_ClientBatchDeleteImageImageIdsTypeDef = TypedDict(
    "_ClientBatchDeleteImageImageIdsTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)


class ClientBatchDeleteImageImageIdsTypeDef(_ClientBatchDeleteImageImageIdsTypeDef):
    """
    - *(dict) --*

      An object with identifying information for an Amazon ECR image.
      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.
    """


_ClientBatchDeleteImageResponsefailuresimageIdTypeDef = TypedDict(
    "_ClientBatchDeleteImageResponsefailuresimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientBatchDeleteImageResponsefailuresimageIdTypeDef(
    _ClientBatchDeleteImageResponsefailuresimageIdTypeDef
):
    pass


_ClientBatchDeleteImageResponsefailuresTypeDef = TypedDict(
    "_ClientBatchDeleteImageResponsefailuresTypeDef",
    {
        "imageId": ClientBatchDeleteImageResponsefailuresimageIdTypeDef,
        "failureCode": Literal[
            "InvalidImageDigest",
            "InvalidImageTag",
            "ImageTagDoesNotMatchDigest",
            "ImageNotFound",
            "MissingDigestAndTag",
        ],
        "failureReason": str,
    },
    total=False,
)


class ClientBatchDeleteImageResponsefailuresTypeDef(_ClientBatchDeleteImageResponsefailuresTypeDef):
    pass


_ClientBatchDeleteImageResponseimageIdsTypeDef = TypedDict(
    "_ClientBatchDeleteImageResponseimageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientBatchDeleteImageResponseimageIdsTypeDef(_ClientBatchDeleteImageResponseimageIdsTypeDef):
    """
    - *(dict) --*

      An object with identifying information for an Amazon ECR image.
      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.
    """


_ClientBatchDeleteImageResponseTypeDef = TypedDict(
    "_ClientBatchDeleteImageResponseTypeDef",
    {
        "imageIds": List[ClientBatchDeleteImageResponseimageIdsTypeDef],
        "failures": List[ClientBatchDeleteImageResponsefailuresTypeDef],
    },
    total=False,
)


class ClientBatchDeleteImageResponseTypeDef(_ClientBatchDeleteImageResponseTypeDef):
    """
    - *(dict) --*

      - **imageIds** *(list) --*

        The image IDs of the deleted images.
        - *(dict) --*

          An object with identifying information for an Amazon ECR image.
          - **imageDigest** *(string) --*

            The ``sha256`` digest of the image manifest.
    """


_ClientBatchGetImageImageIdsTypeDef = TypedDict(
    "_ClientBatchGetImageImageIdsTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)


class ClientBatchGetImageImageIdsTypeDef(_ClientBatchGetImageImageIdsTypeDef):
    """
    - *(dict) --*

      An object with identifying information for an Amazon ECR image.
      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.
    """


_ClientBatchGetImageResponsefailuresimageIdTypeDef = TypedDict(
    "_ClientBatchGetImageResponsefailuresimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientBatchGetImageResponsefailuresimageIdTypeDef(
    _ClientBatchGetImageResponsefailuresimageIdTypeDef
):
    pass


_ClientBatchGetImageResponsefailuresTypeDef = TypedDict(
    "_ClientBatchGetImageResponsefailuresTypeDef",
    {
        "imageId": ClientBatchGetImageResponsefailuresimageIdTypeDef,
        "failureCode": Literal[
            "InvalidImageDigest",
            "InvalidImageTag",
            "ImageTagDoesNotMatchDigest",
            "ImageNotFound",
            "MissingDigestAndTag",
        ],
        "failureReason": str,
    },
    total=False,
)


class ClientBatchGetImageResponsefailuresTypeDef(_ClientBatchGetImageResponsefailuresTypeDef):
    pass


_ClientBatchGetImageResponseimagesimageIdTypeDef = TypedDict(
    "_ClientBatchGetImageResponseimagesimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientBatchGetImageResponseimagesimageIdTypeDef(
    _ClientBatchGetImageResponseimagesimageIdTypeDef
):
    pass


_ClientBatchGetImageResponseimagesTypeDef = TypedDict(
    "_ClientBatchGetImageResponseimagesTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientBatchGetImageResponseimagesimageIdTypeDef,
        "imageManifest": str,
    },
    total=False,
)


class ClientBatchGetImageResponseimagesTypeDef(_ClientBatchGetImageResponseimagesTypeDef):
    """
    - *(dict) --*

      An object representing an Amazon ECR image.
      - **registryId** *(string) --*

        The AWS account ID associated with the registry containing the image.
    """


_ClientBatchGetImageResponseTypeDef = TypedDict(
    "_ClientBatchGetImageResponseTypeDef",
    {
        "images": List[ClientBatchGetImageResponseimagesTypeDef],
        "failures": List[ClientBatchGetImageResponsefailuresTypeDef],
    },
    total=False,
)


class ClientBatchGetImageResponseTypeDef(_ClientBatchGetImageResponseTypeDef):
    """
    - *(dict) --*

      - **images** *(list) --*

        A list of image objects corresponding to the image references in the request.
        - *(dict) --*

          An object representing an Amazon ECR image.
          - **registryId** *(string) --*

            The AWS account ID associated with the registry containing the image.
    """


_ClientCompleteLayerUploadResponseTypeDef = TypedDict(
    "_ClientCompleteLayerUploadResponseTypeDef",
    {"registryId": str, "repositoryName": str, "uploadId": str, "layerDigest": str},
    total=False,
)


class ClientCompleteLayerUploadResponseTypeDef(_ClientCompleteLayerUploadResponseTypeDef):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientCreateRepositoryImageScanningConfigurationTypeDef = TypedDict(
    "_ClientCreateRepositoryImageScanningConfigurationTypeDef", {"scanOnPush": bool}, total=False
)


class ClientCreateRepositoryImageScanningConfigurationTypeDef(
    _ClientCreateRepositoryImageScanningConfigurationTypeDef
):
    """
    The image scanning configuration for the repository. This setting determines whether images are
    scanned for known vulnerabilities after being pushed to the repository.
    - **scanOnPush** *(boolean) --*

      The setting that determines whether images are scanned after being pushed to a repository. If
      set to ``true`` , images will be scanned after being pushed. If this parameter is not
      specified, it will default to ``false`` and images will not be scanned unless a scan is
      manually started with the  StartImageScan API.
    """


_ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef = TypedDict(
    "_ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef(
    _ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef
):
    pass


_ClientCreateRepositoryResponserepositoryTypeDef = TypedDict(
    "_ClientCreateRepositoryResponserepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
        "imageScanningConfiguration": ClientCreateRepositoryResponserepositoryimageScanningConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateRepositoryResponserepositoryTypeDef(
    _ClientCreateRepositoryResponserepositoryTypeDef
):
    """
    - **repository** *(dict) --*

      The repository that was created.
      - **repositoryArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
        ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the
        repository owner, repository namespace, and repository name. For example,
        ``arn:aws:ecr:region:012345678910:repository/test`` .
    """


_ClientCreateRepositoryResponseTypeDef = TypedDict(
    "_ClientCreateRepositoryResponseTypeDef",
    {"repository": ClientCreateRepositoryResponserepositoryTypeDef},
    total=False,
)


class ClientCreateRepositoryResponseTypeDef(_ClientCreateRepositoryResponseTypeDef):
    """
    - *(dict) --*

      - **repository** *(dict) --*

        The repository that was created.
        - **repositoryArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
          ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the
          repository owner, repository namespace, and repository name. For example,
          ``arn:aws:ecr:region:012345678910:repository/test`` .
    """


_ClientCreateRepositoryTagsTypeDef = TypedDict(
    "_ClientCreateRepositoryTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRepositoryTagsTypeDef(_ClientCreateRepositoryTagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define. Tag keys can have a maximum
      character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **Key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientDeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientDeleteLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
    },
    total=False,
)


class ClientDeleteLifecyclePolicyResponseTypeDef(_ClientDeleteLifecyclePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientDeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "_ClientDeleteRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)


class ClientDeleteRepositoryPolicyResponseTypeDef(_ClientDeleteRepositoryPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef = TypedDict(
    "_ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef(
    _ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef
):
    pass


_ClientDeleteRepositoryResponserepositoryTypeDef = TypedDict(
    "_ClientDeleteRepositoryResponserepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
        "imageScanningConfiguration": ClientDeleteRepositoryResponserepositoryimageScanningConfigurationTypeDef,
    },
    total=False,
)


class ClientDeleteRepositoryResponserepositoryTypeDef(
    _ClientDeleteRepositoryResponserepositoryTypeDef
):
    """
    - **repository** *(dict) --*

      The repository that was deleted.
      - **repositoryArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
        ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the
        repository owner, repository namespace, and repository name. For example,
        ``arn:aws:ecr:region:012345678910:repository/test`` .
    """


_ClientDeleteRepositoryResponseTypeDef = TypedDict(
    "_ClientDeleteRepositoryResponseTypeDef",
    {"repository": ClientDeleteRepositoryResponserepositoryTypeDef},
    total=False,
)


class ClientDeleteRepositoryResponseTypeDef(_ClientDeleteRepositoryResponseTypeDef):
    """
    - *(dict) --*

      - **repository** *(dict) --*

        The repository that was deleted.
        - **repositoryArn** *(string) --*

          The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
          ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the
          repository owner, repository namespace, and repository name. For example,
          ``arn:aws:ecr:region:012345678910:repository/test`` .
    """


_ClientDescribeImageScanFindingsImageIdTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsImageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientDescribeImageScanFindingsImageIdTypeDef(_ClientDescribeImageScanFindingsImageIdTypeDef):
    """
    An object with identifying information for an Amazon ECR image.
    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.
    """


_ClientDescribeImageScanFindingsResponseimageIdTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientDescribeImageScanFindingsResponseimageIdTypeDef(
    _ClientDescribeImageScanFindingsResponseimageIdTypeDef
):
    pass


_ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef(
    _ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef
):
    pass


_ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef",
    {
        "name": str,
        "description": str,
        "uri": str,
        "severity": Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNDEFINED"],
        "attributes": List[
            ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsattributesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef(
    _ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef
):
    pass


_ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findings": List[ClientDescribeImageScanFindingsResponseimageScanFindingsfindingsTypeDef],
        "findingSeverityCounts": Dict[str, int],
    },
    total=False,
)


class ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef(
    _ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef
):
    pass


_ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef",
    {"status": Literal["IN_PROGRESS", "COMPLETE", "FAILED"], "description": str},
    total=False,
)


class ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef(
    _ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef
):
    pass


_ClientDescribeImageScanFindingsResponseTypeDef = TypedDict(
    "_ClientDescribeImageScanFindingsResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientDescribeImageScanFindingsResponseimageIdTypeDef,
        "imageScanStatus": ClientDescribeImageScanFindingsResponseimageScanStatusTypeDef,
        "imageScanFindings": ClientDescribeImageScanFindingsResponseimageScanFindingsTypeDef,
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeImageScanFindingsResponseTypeDef(
    _ClientDescribeImageScanFindingsResponseTypeDef
):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientDescribeImagesFilterTypeDef = TypedDict(
    "_ClientDescribeImagesFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)


class ClientDescribeImagesFilterTypeDef(_ClientDescribeImagesFilterTypeDef):
    """
    The filter key and value with which to filter your ``DescribeImages`` results.
    - **tagStatus** *(string) --*

      The tag status with which to filter your  DescribeImages results. You can filter results based
      on whether they are ``TAGGED`` or ``UNTAGGED`` .
    """


_ClientDescribeImagesImageIdsTypeDef = TypedDict(
    "_ClientDescribeImagesImageIdsTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)


class ClientDescribeImagesImageIdsTypeDef(_ClientDescribeImagesImageIdsTypeDef):
    """
    - *(dict) --*

      An object with identifying information for an Amazon ECR image.
      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.
    """


_ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef = TypedDict(
    "_ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[str, int],
    },
    total=False,
)


class ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef(
    _ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef
):
    pass


_ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef = TypedDict(
    "_ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef",
    {"status": Literal["IN_PROGRESS", "COMPLETE", "FAILED"], "description": str},
    total=False,
)


class ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef(
    _ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef
):
    pass


_ClientDescribeImagesResponseimageDetailsTypeDef = TypedDict(
    "_ClientDescribeImagesResponseimageDetailsTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageDigest": str,
        "imageTags": List[str],
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageScanStatus": ClientDescribeImagesResponseimageDetailsimageScanStatusTypeDef,
        "imageScanFindingsSummary": ClientDescribeImagesResponseimageDetailsimageScanFindingsSummaryTypeDef,
    },
    total=False,
)


class ClientDescribeImagesResponseimageDetailsTypeDef(
    _ClientDescribeImagesResponseimageDetailsTypeDef
):
    """
    - *(dict) --*

      An object that describes an image returned by a  DescribeImages operation.
      - **registryId** *(string) --*

        The AWS account ID associated with the registry to which this image belongs.
    """


_ClientDescribeImagesResponseTypeDef = TypedDict(
    "_ClientDescribeImagesResponseTypeDef",
    {"imageDetails": List[ClientDescribeImagesResponseimageDetailsTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeImagesResponseTypeDef(_ClientDescribeImagesResponseTypeDef):
    """
    - *(dict) --*

      - **imageDetails** *(list) --*

        A list of  ImageDetail objects that contain data about the image.
        - *(dict) --*

          An object that describes an image returned by a  DescribeImages operation.
          - **registryId** *(string) --*

            The AWS account ID associated with the registry to which this image belongs.
    """


_ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef = TypedDict(
    "_ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef(
    _ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef
):
    pass


_ClientDescribeRepositoriesResponserepositoriesTypeDef = TypedDict(
    "_ClientDescribeRepositoriesResponserepositoriesTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
        "imageScanningConfiguration": ClientDescribeRepositoriesResponserepositoriesimageScanningConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeRepositoriesResponserepositoriesTypeDef(
    _ClientDescribeRepositoriesResponserepositoriesTypeDef
):
    """
    - *(dict) --*

      An object representing a repository.
      - **repositoryArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
        ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the
        repository owner, repository namespace, and repository name. For example,
        ``arn:aws:ecr:region:012345678910:repository/test`` .
    """


_ClientDescribeRepositoriesResponseTypeDef = TypedDict(
    "_ClientDescribeRepositoriesResponseTypeDef",
    {"repositories": List[ClientDescribeRepositoriesResponserepositoriesTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeRepositoriesResponseTypeDef(_ClientDescribeRepositoriesResponseTypeDef):
    """
    - *(dict) --*

      - **repositories** *(list) --*

        A list of repository objects corresponding to valid repositories.
        - *(dict) --*

          An object representing a repository.
          - **repositoryArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
            ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of
            the repository owner, repository namespace, and repository name. For example,
            ``arn:aws:ecr:region:012345678910:repository/test`` .
    """


_ClientGetAuthorizationTokenResponseauthorizationDataTypeDef = TypedDict(
    "_ClientGetAuthorizationTokenResponseauthorizationDataTypeDef",
    {"authorizationToken": str, "expiresAt": datetime, "proxyEndpoint": str},
    total=False,
)


class ClientGetAuthorizationTokenResponseauthorizationDataTypeDef(
    _ClientGetAuthorizationTokenResponseauthorizationDataTypeDef
):
    """
    - *(dict) --*

      An object representing authorization data for an Amazon ECR registry.
      - **authorizationToken** *(string) --*

        A base64-encoded string that contains authorization data for the specified Amazon ECR
        registry. When the string is decoded, it is presented in the format ``user:password`` for
        private registry authentication using ``docker login`` .
    """


_ClientGetAuthorizationTokenResponseTypeDef = TypedDict(
    "_ClientGetAuthorizationTokenResponseTypeDef",
    {"authorizationData": List[ClientGetAuthorizationTokenResponseauthorizationDataTypeDef]},
    total=False,
)


class ClientGetAuthorizationTokenResponseTypeDef(_ClientGetAuthorizationTokenResponseTypeDef):
    """
    - *(dict) --*

      - **authorizationData** *(list) --*

        A list of authorization token data objects that correspond to the ``registryIds`` values in
        the request.
        - *(dict) --*

          An object representing authorization data for an Amazon ECR registry.
          - **authorizationToken** *(string) --*

            A base64-encoded string that contains authorization data for the specified Amazon ECR
            registry. When the string is decoded, it is presented in the format ``user:password``
            for private registry authentication using ``docker login`` .
    """


_ClientGetDownloadUrlForLayerResponseTypeDef = TypedDict(
    "_ClientGetDownloadUrlForLayerResponseTypeDef",
    {"downloadUrl": str, "layerDigest": str},
    total=False,
)


class ClientGetDownloadUrlForLayerResponseTypeDef(_ClientGetDownloadUrlForLayerResponseTypeDef):
    """
    - *(dict) --*

      - **downloadUrl** *(string) --*

        The pre-signed Amazon S3 download URL for the requested layer.
    """


_ClientGetLifecyclePolicyPreviewFilterTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)


class ClientGetLifecyclePolicyPreviewFilterTypeDef(_ClientGetLifecyclePolicyPreviewFilterTypeDef):
    """
    An optional parameter that filters results based on image tag status and all tags, if tagged.
    - **tagStatus** *(string) --*

      The tag status of the image.
    """


_ClientGetLifecyclePolicyPreviewImageIdsTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewImageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientGetLifecyclePolicyPreviewImageIdsTypeDef(
    _ClientGetLifecyclePolicyPreviewImageIdsTypeDef
):
    """
    - *(dict) --*

      An object with identifying information for an Amazon ECR image.
      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.
    """


_ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef",
    {"type": str},
    total=False,
)


class ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef(
    _ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef
):
    pass


_ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef",
    {
        "imageTags": List[str],
        "imageDigest": str,
        "imagePushedAt": datetime,
        "action": ClientGetLifecyclePolicyPreviewResponsepreviewResultsactionTypeDef,
        "appliedRulePriority": int,
    },
    total=False,
)


class ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef(
    _ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef
):
    pass


_ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef",
    {"expiringImageTotalCount": int},
    total=False,
)


class ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef(
    _ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef
):
    pass


_ClientGetLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": Literal["IN_PROGRESS", "COMPLETE", "EXPIRED", "FAILED"],
        "nextToken": str,
        "previewResults": List[ClientGetLifecyclePolicyPreviewResponsepreviewResultsTypeDef],
        "summary": ClientGetLifecyclePolicyPreviewResponsesummaryTypeDef,
    },
    total=False,
)


class ClientGetLifecyclePolicyPreviewResponseTypeDef(
    _ClientGetLifecyclePolicyPreviewResponseTypeDef
):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientGetLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
    },
    total=False,
)


class ClientGetLifecyclePolicyResponseTypeDef(_ClientGetLifecyclePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientGetRepositoryPolicyResponseTypeDef = TypedDict(
    "_ClientGetRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)


class ClientGetRepositoryPolicyResponseTypeDef(_ClientGetRepositoryPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientInitiateLayerUploadResponseTypeDef = TypedDict(
    "_ClientInitiateLayerUploadResponseTypeDef", {"uploadId": str, "partSize": int}, total=False
)


class ClientInitiateLayerUploadResponseTypeDef(_ClientInitiateLayerUploadResponseTypeDef):
    """
    - *(dict) --*

      - **uploadId** *(string) --*

        The upload ID for the layer upload. This parameter is passed to further  UploadLayerPart and
        CompleteLayerUpload operations.
    """


_ClientListImagesFilterTypeDef = TypedDict(
    "_ClientListImagesFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)


class ClientListImagesFilterTypeDef(_ClientListImagesFilterTypeDef):
    """
    The filter key and value with which to filter your ``ListImages`` results.
    - **tagStatus** *(string) --*

      The tag status with which to filter your  ListImages results. You can filter results based on
      whether they are ``TAGGED`` or ``UNTAGGED`` .
    """


_ClientListImagesResponseimageIdsTypeDef = TypedDict(
    "_ClientListImagesResponseimageIdsTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)


class ClientListImagesResponseimageIdsTypeDef(_ClientListImagesResponseimageIdsTypeDef):
    """
    - *(dict) --*

      An object with identifying information for an Amazon ECR image.
      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.
    """


_ClientListImagesResponseTypeDef = TypedDict(
    "_ClientListImagesResponseTypeDef",
    {"imageIds": List[ClientListImagesResponseimageIdsTypeDef], "nextToken": str},
    total=False,
)


class ClientListImagesResponseTypeDef(_ClientListImagesResponseTypeDef):
    """
    - *(dict) --*

      - **imageIds** *(list) --*

        The list of image IDs for the requested repository.
        - *(dict) --*

          An object with identifying information for an Amazon ECR image.
          - **imageDigest** *(string) --*

            The ``sha256`` digest of the image manifest.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponsetagsTypeDef(_ClientListTagsForResourceResponsetagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define. Tag keys can have a maximum
      character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **Key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        The tags for the resource.
        - *(dict) --*

          The metadata that you apply to a resource to help you categorize and organize them. Each
          tag consists of a key and an optional value, both of which you define. Tag keys can have a
          maximum character length of 128 characters, and tag values can have a maximum length of
          256 characters.
          - **Key** *(string) --*

            One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
            like a category for more specific tag values.
    """


_ClientPutImageResponseimageimageIdTypeDef = TypedDict(
    "_ClientPutImageResponseimageimageIdTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)


class ClientPutImageResponseimageimageIdTypeDef(_ClientPutImageResponseimageimageIdTypeDef):
    pass


_ClientPutImageResponseimageTypeDef = TypedDict(
    "_ClientPutImageResponseimageTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientPutImageResponseimageimageIdTypeDef,
        "imageManifest": str,
    },
    total=False,
)


class ClientPutImageResponseimageTypeDef(_ClientPutImageResponseimageTypeDef):
    """
    - **image** *(dict) --*

      Details of the image uploaded.
      - **registryId** *(string) --*

        The AWS account ID associated with the registry containing the image.
    """


_ClientPutImageResponseTypeDef = TypedDict(
    "_ClientPutImageResponseTypeDef", {"image": ClientPutImageResponseimageTypeDef}, total=False
)


class ClientPutImageResponseTypeDef(_ClientPutImageResponseTypeDef):
    """
    - *(dict) --*

      - **image** *(dict) --*

        Details of the image uploaded.
        - **registryId** *(string) --*

          The AWS account ID associated with the registry containing the image.
    """


_ClientPutImageScanningConfigurationImageScanningConfigurationTypeDef = TypedDict(
    "_ClientPutImageScanningConfigurationImageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientPutImageScanningConfigurationImageScanningConfigurationTypeDef(
    _ClientPutImageScanningConfigurationImageScanningConfigurationTypeDef
):
    """
    The image scanning configuration for the repository. This setting determines whether images are
    scanned for known vulnerabilities after being pushed to the repository.
    - **scanOnPush** *(boolean) --*

      The setting that determines whether images are scanned after being pushed to a repository. If
      set to ``true`` , images will be scanned after being pushed. If this parameter is not
      specified, it will default to ``false`` and images will not be scanned unless a scan is
      manually started with the  StartImageScan API.
    """


_ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef = TypedDict(
    "_ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef(
    _ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef
):
    pass


_ClientPutImageScanningConfigurationResponseTypeDef = TypedDict(
    "_ClientPutImageScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageScanningConfiguration": ClientPutImageScanningConfigurationResponseimageScanningConfigurationTypeDef,
    },
    total=False,
)


class ClientPutImageScanningConfigurationResponseTypeDef(
    _ClientPutImageScanningConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientPutImageTagMutabilityResponseTypeDef = TypedDict(
    "_ClientPutImageTagMutabilityResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
    },
    total=False,
)


class ClientPutImageTagMutabilityResponseTypeDef(_ClientPutImageTagMutabilityResponseTypeDef):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientPutLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientPutLifecyclePolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "lifecyclePolicyText": str},
    total=False,
)


class ClientPutLifecyclePolicyResponseTypeDef(_ClientPutLifecyclePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientSetRepositoryPolicyResponseTypeDef = TypedDict(
    "_ClientSetRepositoryPolicyResponseTypeDef",
    {"registryId": str, "repositoryName": str, "policyText": str},
    total=False,
)


class ClientSetRepositoryPolicyResponseTypeDef(_ClientSetRepositoryPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientStartImageScanImageIdTypeDef = TypedDict(
    "_ClientStartImageScanImageIdTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)


class ClientStartImageScanImageIdTypeDef(_ClientStartImageScanImageIdTypeDef):
    """
    An object with identifying information for an Amazon ECR image.
    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.
    """


_ClientStartImageScanResponseimageIdTypeDef = TypedDict(
    "_ClientStartImageScanResponseimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class ClientStartImageScanResponseimageIdTypeDef(_ClientStartImageScanResponseimageIdTypeDef):
    pass


_ClientStartImageScanResponseimageScanStatusTypeDef = TypedDict(
    "_ClientStartImageScanResponseimageScanStatusTypeDef",
    {"status": Literal["IN_PROGRESS", "COMPLETE", "FAILED"], "description": str},
    total=False,
)


class ClientStartImageScanResponseimageScanStatusTypeDef(
    _ClientStartImageScanResponseimageScanStatusTypeDef
):
    pass


_ClientStartImageScanResponseTypeDef = TypedDict(
    "_ClientStartImageScanResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": ClientStartImageScanResponseimageIdTypeDef,
        "imageScanStatus": ClientStartImageScanResponseimageScanStatusTypeDef,
    },
    total=False,
)


class ClientStartImageScanResponseTypeDef(_ClientStartImageScanResponseTypeDef):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientStartLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "_ClientStartLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": Literal["IN_PROGRESS", "COMPLETE", "EXPIRED", "FAILED"],
    },
    total=False,
)


class ClientStartLifecyclePolicyPreviewResponseTypeDef(
    _ClientStartLifecyclePolicyPreviewResponseTypeDef
):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      The metadata that you apply to a resource to help you categorize and organize them. Each tag
      consists of a key and an optional value, both of which you define. Tag keys can have a maximum
      character length of 128 characters, and tag values can have a maximum length of 256
      characters.
      - **Key** *(string) --*

        One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
        a category for more specific tag values.
    """


_ClientUploadLayerPartResponseTypeDef = TypedDict(
    "_ClientUploadLayerPartResponseTypeDef",
    {"registryId": str, "repositoryName": str, "uploadId": str, "lastByteReceived": int},
    total=False,
)


class ClientUploadLayerPartResponseTypeDef(_ClientUploadLayerPartResponseTypeDef):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_DescribeImageScanFindingsPaginateImageIdTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateImageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class DescribeImageScanFindingsPaginateImageIdTypeDef(
    _DescribeImageScanFindingsPaginateImageIdTypeDef
):
    """
    An object with identifying information for an Amazon ECR image.
    - **imageDigest** *(string) --*

      The ``sha256`` digest of the image manifest.
    """


_DescribeImageScanFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeImageScanFindingsPaginatePaginationConfigTypeDef(
    _DescribeImageScanFindingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeImageScanFindingsPaginateResponseimageIdTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseimageIdTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class DescribeImageScanFindingsPaginateResponseimageIdTypeDef(
    _DescribeImageScanFindingsPaginateResponseimageIdTypeDef
):
    pass


_DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)


class DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef(
    _DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef
):
    pass


_DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef",
    {
        "name": str,
        "description": str,
        "uri": str,
        "severity": Literal["INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNDEFINED"],
        "attributes": List[
            DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsattributesTypeDef
        ],
    },
    total=False,
)


class DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef(
    _DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef
):
    pass


_DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findings": List[DescribeImageScanFindingsPaginateResponseimageScanFindingsfindingsTypeDef],
        "findingSeverityCounts": Dict[str, int],
    },
    total=False,
)


class DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef(
    _DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef
):
    pass


_DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef",
    {"status": Literal["IN_PROGRESS", "COMPLETE", "FAILED"], "description": str},
    total=False,
)


class DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef(
    _DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef
):
    pass


_DescribeImageScanFindingsPaginateResponseTypeDef = TypedDict(
    "_DescribeImageScanFindingsPaginateResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": DescribeImageScanFindingsPaginateResponseimageIdTypeDef,
        "imageScanStatus": DescribeImageScanFindingsPaginateResponseimageScanStatusTypeDef,
        "imageScanFindings": DescribeImageScanFindingsPaginateResponseimageScanFindingsTypeDef,
        "NextToken": str,
    },
    total=False,
)


class DescribeImageScanFindingsPaginateResponseTypeDef(
    _DescribeImageScanFindingsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_DescribeImagesPaginateFilterTypeDef = TypedDict(
    "_DescribeImagesPaginateFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)


class DescribeImagesPaginateFilterTypeDef(_DescribeImagesPaginateFilterTypeDef):
    """
    The filter key and value with which to filter your ``DescribeImages`` results.
    - **tagStatus** *(string) --*

      The tag status with which to filter your  DescribeImages results. You can filter results based
      on whether they are ``TAGGED`` or ``UNTAGGED`` .
    """


_DescribeImagesPaginateImageIdsTypeDef = TypedDict(
    "_DescribeImagesPaginateImageIdsTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)


class DescribeImagesPaginateImageIdsTypeDef(_DescribeImagesPaginateImageIdsTypeDef):
    """
    - *(dict) --*

      An object with identifying information for an Amazon ECR image.
      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.
    """


_DescribeImagesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeImagesPaginatePaginationConfigTypeDef(_DescribeImagesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[str, int],
    },
    total=False,
)


class DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef(
    _DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef
):
    pass


_DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef",
    {"status": Literal["IN_PROGRESS", "COMPLETE", "FAILED"], "description": str},
    total=False,
)


class DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef(
    _DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef
):
    pass


_DescribeImagesPaginateResponseimageDetailsTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseimageDetailsTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageDigest": str,
        "imageTags": List[str],
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageScanStatus": DescribeImagesPaginateResponseimageDetailsimageScanStatusTypeDef,
        "imageScanFindingsSummary": DescribeImagesPaginateResponseimageDetailsimageScanFindingsSummaryTypeDef,
    },
    total=False,
)


class DescribeImagesPaginateResponseimageDetailsTypeDef(
    _DescribeImagesPaginateResponseimageDetailsTypeDef
):
    """
    - *(dict) --*

      An object that describes an image returned by a  DescribeImages operation.
      - **registryId** *(string) --*

        The AWS account ID associated with the registry to which this image belongs.
    """


_DescribeImagesPaginateResponseTypeDef = TypedDict(
    "_DescribeImagesPaginateResponseTypeDef",
    {"imageDetails": List[DescribeImagesPaginateResponseimageDetailsTypeDef], "NextToken": str},
    total=False,
)


class DescribeImagesPaginateResponseTypeDef(_DescribeImagesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **imageDetails** *(list) --*

        A list of  ImageDetail objects that contain data about the image.
        - *(dict) --*

          An object that describes an image returned by a  DescribeImages operation.
          - **registryId** *(string) --*

            The AWS account ID associated with the registry to which this image belongs.
    """


_DescribeRepositoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeRepositoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeRepositoriesPaginatePaginationConfigTypeDef(
    _DescribeRepositoriesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef = TypedDict(
    "_DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef",
    {"scanOnPush": bool},
    total=False,
)


class DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef(
    _DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef
):
    pass


_DescribeRepositoriesPaginateResponserepositoriesTypeDef = TypedDict(
    "_DescribeRepositoriesPaginateResponserepositoriesTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": Literal["MUTABLE", "IMMUTABLE"],
        "imageScanningConfiguration": DescribeRepositoriesPaginateResponserepositoriesimageScanningConfigurationTypeDef,
    },
    total=False,
)


class DescribeRepositoriesPaginateResponserepositoriesTypeDef(
    _DescribeRepositoriesPaginateResponserepositoriesTypeDef
):
    """
    - *(dict) --*

      An object representing a repository.
      - **repositoryArn** *(string) --*

        The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
        ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of the
        repository owner, repository namespace, and repository name. For example,
        ``arn:aws:ecr:region:012345678910:repository/test`` .
    """


_DescribeRepositoriesPaginateResponseTypeDef = TypedDict(
    "_DescribeRepositoriesPaginateResponseTypeDef",
    {
        "repositories": List[DescribeRepositoriesPaginateResponserepositoriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeRepositoriesPaginateResponseTypeDef(_DescribeRepositoriesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **repositories** *(list) --*

        A list of repository objects corresponding to valid repositories.
        - *(dict) --*

          An object representing a repository.
          - **repositoryArn** *(string) --*

            The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the
            ``arn:aws:ecr`` namespace, followed by the region of the repository, AWS account ID of
            the repository owner, repository namespace, and repository name. For example,
            ``arn:aws:ecr:region:012345678910:repository/test`` .
    """


_GetLifecyclePolicyPreviewPaginateFilterTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)


class GetLifecyclePolicyPreviewPaginateFilterTypeDef(
    _GetLifecyclePolicyPreviewPaginateFilterTypeDef
):
    """
    An optional parameter that filters results based on image tag status and all tags, if tagged.
    - **tagStatus** *(string) --*

      The tag status of the image.
    """


_GetLifecyclePolicyPreviewPaginateImageIdsTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateImageIdsTypeDef",
    {"imageDigest": str, "imageTag": str},
    total=False,
)


class GetLifecyclePolicyPreviewPaginateImageIdsTypeDef(
    _GetLifecyclePolicyPreviewPaginateImageIdsTypeDef
):
    """
    - *(dict) --*

      An object with identifying information for an Amazon ECR image.
      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.
    """


_GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef(
    _GetLifecyclePolicyPreviewPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef",
    {"type": str},
    total=False,
)


class GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef(
    _GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef
):
    pass


_GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef",
    {
        "imageTags": List[str],
        "imageDigest": str,
        "imagePushedAt": datetime,
        "action": GetLifecyclePolicyPreviewPaginateResponsepreviewResultsactionTypeDef,
        "appliedRulePriority": int,
    },
    total=False,
)


class GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef(
    _GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef
):
    pass


_GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef",
    {"expiringImageTotalCount": int},
    total=False,
)


class GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef(
    _GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef
):
    pass


_GetLifecyclePolicyPreviewPaginateResponseTypeDef = TypedDict(
    "_GetLifecyclePolicyPreviewPaginateResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": Literal["IN_PROGRESS", "COMPLETE", "EXPIRED", "FAILED"],
        "previewResults": List[GetLifecyclePolicyPreviewPaginateResponsepreviewResultsTypeDef],
        "summary": GetLifecyclePolicyPreviewPaginateResponsesummaryTypeDef,
        "NextToken": str,
    },
    total=False,
)


class GetLifecyclePolicyPreviewPaginateResponseTypeDef(
    _GetLifecyclePolicyPreviewPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **registryId** *(string) --*

        The registry ID associated with the request.
    """


_ListImagesPaginateFilterTypeDef = TypedDict(
    "_ListImagesPaginateFilterTypeDef",
    {"tagStatus": Literal["TAGGED", "UNTAGGED", "ANY"]},
    total=False,
)


class ListImagesPaginateFilterTypeDef(_ListImagesPaginateFilterTypeDef):
    """
    The filter key and value with which to filter your ``ListImages`` results.
    - **tagStatus** *(string) --*

      The tag status with which to filter your  ListImages results. You can filter results based on
      whether they are ``TAGGED`` or ``UNTAGGED`` .
    """


_ListImagesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListImagesPaginatePaginationConfigTypeDef(_ListImagesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListImagesPaginateResponseimageIdsTypeDef = TypedDict(
    "_ListImagesPaginateResponseimageIdsTypeDef", {"imageDigest": str, "imageTag": str}, total=False
)


class ListImagesPaginateResponseimageIdsTypeDef(_ListImagesPaginateResponseimageIdsTypeDef):
    """
    - *(dict) --*

      An object with identifying information for an Amazon ECR image.
      - **imageDigest** *(string) --*

        The ``sha256`` digest of the image manifest.
    """


_ListImagesPaginateResponseTypeDef = TypedDict(
    "_ListImagesPaginateResponseTypeDef",
    {"imageIds": List[ListImagesPaginateResponseimageIdsTypeDef], "NextToken": str},
    total=False,
)


class ListImagesPaginateResponseTypeDef(_ListImagesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **imageIds** *(list) --*

        The list of image IDs for the requested repository.
        - *(dict) --*

          An object with identifying information for an Amazon ECR image.
          - **imageDigest** *(string) --*

            The ``sha256`` digest of the image manifest.
    """
