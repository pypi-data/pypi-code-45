"Main interface for mediapackage service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List
from mypy_boto3_mediapackage.type_defs import ClientCreateChannelResponseTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
from typing import overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_mediapackage.client as client_scope

# pylint: disable=import-self
import mypy_boto3_mediapackage.paginator as paginator_scope
from mypy_boto3_mediapackage.type_defs import (
    ClientCreateHarvestJobResponseTypeDef,
    ClientCreateHarvestJobS3DestinationTypeDef,
    ClientCreateOriginEndpointCmafPackageTypeDef,
    ClientCreateOriginEndpointDashPackageTypeDef,
    ClientCreateOriginEndpointHlsPackageTypeDef,
    ClientCreateOriginEndpointMssPackageTypeDef,
    ClientCreateOriginEndpointResponseTypeDef,
    ClientDescribeChannelResponseTypeDef,
    ClientDescribeHarvestJobResponseTypeDef,
    ClientDescribeOriginEndpointResponseTypeDef,
    ClientListChannelsResponseTypeDef,
    ClientListHarvestJobsResponseTypeDef,
    ClientListOriginEndpointsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientRotateChannelCredentialsResponseTypeDef,
    ClientRotateIngestEndpointCredentialsResponseTypeDef,
    ClientUpdateChannelResponseTypeDef,
    ClientUpdateOriginEndpointCmafPackageTypeDef,
    ClientUpdateOriginEndpointDashPackageTypeDef,
    ClientUpdateOriginEndpointHlsPackageTypeDef,
    ClientUpdateOriginEndpointMssPackageTypeDef,
    ClientUpdateOriginEndpointResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    """
    [MediaPackage.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_channel(
        self, Id: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> ClientCreateChannelResponseTypeDef:
        """
        [Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.create_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_harvest_job(
        self,
        EndTime: str,
        Id: str,
        OriginEndpointId: str,
        S3Destination: ClientCreateHarvestJobS3DestinationTypeDef,
        StartTime: str,
    ) -> ClientCreateHarvestJobResponseTypeDef:
        """
        [Client.create_harvest_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.create_harvest_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_origin_endpoint(
        self,
        ChannelId: str,
        Id: str,
        CmafPackage: ClientCreateOriginEndpointCmafPackageTypeDef = None,
        DashPackage: ClientCreateOriginEndpointDashPackageTypeDef = None,
        Description: str = None,
        HlsPackage: ClientCreateOriginEndpointHlsPackageTypeDef = None,
        ManifestName: str = None,
        MssPackage: ClientCreateOriginEndpointMssPackageTypeDef = None,
        Origination: Literal["ALLOW", "DENY"] = None,
        StartoverWindowSeconds: int = None,
        Tags: Dict[str, str] = None,
        TimeDelaySeconds: int = None,
        Whitelist: List[str] = None,
    ) -> ClientCreateOriginEndpointResponseTypeDef:
        """
        [Client.create_origin_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.create_origin_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_channel(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.delete_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_origin_endpoint(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_origin_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.delete_origin_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_channel(self, Id: str) -> ClientDescribeChannelResponseTypeDef:
        """
        [Client.describe_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.describe_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_harvest_job(self, Id: str) -> ClientDescribeHarvestJobResponseTypeDef:
        """
        [Client.describe_harvest_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.describe_harvest_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_origin_endpoint(self, Id: str) -> ClientDescribeOriginEndpointResponseTypeDef:
        """
        [Client.describe_origin_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.describe_origin_endpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_channels(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListChannelsResponseTypeDef:
        """
        [Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.list_channels)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_harvest_jobs(
        self,
        IncludeChannelId: str = None,
        IncludeStatus: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListHarvestJobsResponseTypeDef:
        """
        [Client.list_harvest_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.list_harvest_jobs)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_origin_endpoints(
        self, ChannelId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ClientListOriginEndpointsResponseTypeDef:
        """
        [Client.list_origin_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.list_origin_endpoints)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def rotate_channel_credentials(self, Id: str) -> ClientRotateChannelCredentialsResponseTypeDef:
        """
        [Client.rotate_channel_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.rotate_channel_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def rotate_ingest_endpoint_credentials(
        self, Id: str, IngestEndpointId: str
    ) -> ClientRotateIngestEndpointCredentialsResponseTypeDef:
        """
        [Client.rotate_ingest_endpoint_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.rotate_ingest_endpoint_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_channel(
        self, Id: str, Description: str = None
    ) -> ClientUpdateChannelResponseTypeDef:
        """
        [Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.update_channel)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_origin_endpoint(
        self,
        Id: str,
        CmafPackage: ClientUpdateOriginEndpointCmafPackageTypeDef = None,
        DashPackage: ClientUpdateOriginEndpointDashPackageTypeDef = None,
        Description: str = None,
        HlsPackage: ClientUpdateOriginEndpointHlsPackageTypeDef = None,
        ManifestName: str = None,
        MssPackage: ClientUpdateOriginEndpointMssPackageTypeDef = None,
        Origination: Literal["ALLOW", "DENY"] = None,
        StartoverWindowSeconds: int = None,
        TimeDelaySeconds: int = None,
        Whitelist: List[str] = None,
    ) -> ClientUpdateOriginEndpointResponseTypeDef:
        """
        [Client.update_origin_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Client.update_origin_endpoint)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_channels"]
    ) -> paginator_scope.ListChannelsPaginator:
        """
        [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Paginator.ListChannels)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_harvest_jobs"]
    ) -> paginator_scope.ListHarvestJobsPaginator:
        """
        [Paginator.ListHarvestJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Paginator.ListHarvestJobs)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_origin_endpoints"]
    ) -> paginator_scope.ListOriginEndpointsPaginator:
        """
        [Paginator.ListOriginEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediapackage.html#MediaPackage.Paginator.ListOriginEndpoints)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnprocessableEntityException: Boto3ClientError
