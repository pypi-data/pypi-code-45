"Main interface for mobile service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, IO

# pylint: disable=import-self
import mypy_boto3_mobile.client as client_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
from typing import Union, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_mobile.paginator as paginator_scope
from mypy_boto3_mobile.type_defs import (
    ClientCreateProjectResponseTypeDef,
    ClientDeleteProjectResponseTypeDef,
    ClientDescribeBundleResponseTypeDef,
    ClientDescribeProjectResponseTypeDef,
    ClientExportBundleResponseTypeDef,
    ClientExportProjectResponseTypeDef,
    ClientListBundlesResponseTypeDef,
    ClientListProjectsResponseTypeDef,
    ClientUpdateProjectResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    """
    [Mobile.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_project(
        self,
        name: str = None,
        region: str = None,
        contents: Union[bytes, IO] = None,
        snapshotId: str = None,
    ) -> ClientCreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.create_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_project(self, projectId: str) -> ClientDeleteProjectResponseTypeDef:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.delete_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_bundle(self, bundleId: str) -> ClientDescribeBundleResponseTypeDef:
        """
        [Client.describe_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.describe_bundle)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_project(
        self, projectId: str, syncFromResources: bool = None
    ) -> ClientDescribeProjectResponseTypeDef:
        """
        [Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.describe_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_bundle(
        self,
        bundleId: str,
        projectId: str = None,
        platform: Literal[
            "OSX", "WINDOWS", "LINUX", "OBJC", "SWIFT", "ANDROID", "JAVASCRIPT"
        ] = None,
    ) -> ClientExportBundleResponseTypeDef:
        """
        [Client.export_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.export_bundle)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_project(self, projectId: str) -> ClientExportProjectResponseTypeDef:
        """
        [Client.export_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.export_project)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bundles(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListBundlesResponseTypeDef:
        """
        [Client.list_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.list_bundles)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_projects(
        self, maxResults: int = None, nextToken: str = None
    ) -> ClientListProjectsResponseTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.list_projects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_project(
        self, projectId: str, contents: Union[bytes, IO] = None
    ) -> ClientUpdateProjectResponseTypeDef:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Client.update_project)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_bundles"]
    ) -> paginator_scope.ListBundlesPaginator:
        """
        [Paginator.ListBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Paginator.ListBundles)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> paginator_scope.ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mobile.html#Mobile.Paginator.ListProjects)
        """


class Exceptions:
    AccountActionRequiredException: Boto3ClientError
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnauthorizedException: Boto3ClientError
