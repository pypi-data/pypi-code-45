"Main interface for codebuild service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_codebuild.client as client_scope

# pylint: disable=import-self
import mypy_boto3_codebuild.paginator as paginator_scope
from mypy_boto3_codebuild.type_defs import (
    ClientBatchDeleteBuildsResponseTypeDef,
    ClientBatchGetBuildsResponseTypeDef,
    ClientBatchGetProjectsResponseTypeDef,
    ClientBatchGetReportGroupsResponseTypeDef,
    ClientBatchGetReportsResponseTypeDef,
    ClientCreateProjectArtifactsTypeDef,
    ClientCreateProjectCacheTypeDef,
    ClientCreateProjectEnvironmentTypeDef,
    ClientCreateProjectLogsConfigTypeDef,
    ClientCreateProjectResponseTypeDef,
    ClientCreateProjectSecondaryArtifactsTypeDef,
    ClientCreateProjectSecondarySourceVersionsTypeDef,
    ClientCreateProjectSecondarySourcesTypeDef,
    ClientCreateProjectSourceTypeDef,
    ClientCreateProjectTagsTypeDef,
    ClientCreateProjectVpcConfigTypeDef,
    ClientCreateReportGroupExportConfigTypeDef,
    ClientCreateReportGroupResponseTypeDef,
    ClientCreateWebhookFilterGroupsTypeDef,
    ClientCreateWebhookResponseTypeDef,
    ClientDeleteSourceCredentialsResponseTypeDef,
    ClientDescribeTestCasesFilterTypeDef,
    ClientDescribeTestCasesResponseTypeDef,
    ClientImportSourceCredentialsResponseTypeDef,
    ClientListBuildsForProjectResponseTypeDef,
    ClientListBuildsResponseTypeDef,
    ClientListCuratedEnvironmentImagesResponseTypeDef,
    ClientListProjectsResponseTypeDef,
    ClientListReportGroupsResponseTypeDef,
    ClientListReportsFilterTypeDef,
    ClientListReportsForReportGroupFilterTypeDef,
    ClientListReportsForReportGroupResponseTypeDef,
    ClientListReportsResponseTypeDef,
    ClientListSourceCredentialsResponseTypeDef,
    ClientStartBuildArtifactsOverrideTypeDef,
    ClientStartBuildCacheOverrideTypeDef,
    ClientStartBuildEnvironmentVariablesOverrideTypeDef,
    ClientStartBuildGitSubmodulesConfigOverrideTypeDef,
    ClientStartBuildLogsConfigOverrideTypeDef,
    ClientStartBuildRegistryCredentialOverrideTypeDef,
    ClientStartBuildResponseTypeDef,
    ClientStartBuildSecondaryArtifactsOverrideTypeDef,
    ClientStartBuildSecondarySourcesOverrideTypeDef,
    ClientStartBuildSecondarySourcesVersionOverrideTypeDef,
    ClientStartBuildSourceAuthOverrideTypeDef,
    ClientStopBuildResponseTypeDef,
    ClientUpdateProjectArtifactsTypeDef,
    ClientUpdateProjectCacheTypeDef,
    ClientUpdateProjectEnvironmentTypeDef,
    ClientUpdateProjectLogsConfigTypeDef,
    ClientUpdateProjectResponseTypeDef,
    ClientUpdateProjectSecondaryArtifactsTypeDef,
    ClientUpdateProjectSecondarySourceVersionsTypeDef,
    ClientUpdateProjectSecondarySourcesTypeDef,
    ClientUpdateProjectSourceTypeDef,
    ClientUpdateProjectTagsTypeDef,
    ClientUpdateProjectVpcConfigTypeDef,
    ClientUpdateReportGroupExportConfigTypeDef,
    ClientUpdateReportGroupResponseTypeDef,
    ClientUpdateWebhookFilterGroupsTypeDef,
    ClientUpdateWebhookResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [CodeBuild.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_delete_builds(self, ids: List[str]) -> ClientBatchDeleteBuildsResponseTypeDef:
        """
        [Client.batch_delete_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.batch_delete_builds)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_builds(self, ids: List[str]) -> ClientBatchGetBuildsResponseTypeDef:
        """
        [Client.batch_get_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.batch_get_builds)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_projects(self, names: List[str]) -> ClientBatchGetProjectsResponseTypeDef:
        """
        [Client.batch_get_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.batch_get_projects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_report_groups(
        self, reportGroupArns: List[str]
    ) -> ClientBatchGetReportGroupsResponseTypeDef:
        """
        [Client.batch_get_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.batch_get_report_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_reports(self, reportArns: List[str]) -> ClientBatchGetReportsResponseTypeDef:
        """
        [Client.batch_get_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.batch_get_reports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_project(
        self,
        name: str,
        source: ClientCreateProjectSourceTypeDef,
        artifacts: ClientCreateProjectArtifactsTypeDef,
        environment: ClientCreateProjectEnvironmentTypeDef,
        serviceRole: str,
        description: str = None,
        secondarySources: List[ClientCreateProjectSecondarySourcesTypeDef] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List[ClientCreateProjectSecondarySourceVersionsTypeDef] = None,
        secondaryArtifacts: List[ClientCreateProjectSecondaryArtifactsTypeDef] = None,
        cache: ClientCreateProjectCacheTypeDef = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List[ClientCreateProjectTagsTypeDef] = None,
        vpcConfig: ClientCreateProjectVpcConfigTypeDef = None,
        badgeEnabled: bool = None,
        logsConfig: ClientCreateProjectLogsConfigTypeDef = None,
    ) -> ClientCreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.create_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_report_group(
        self, name: str, type: str, exportConfig: ClientCreateReportGroupExportConfigTypeDef
    ) -> ClientCreateReportGroupResponseTypeDef:
        """
        [Client.create_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.create_report_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        filterGroups: List[List[ClientCreateWebhookFilterGroupsTypeDef]] = None,
    ) -> ClientCreateWebhookResponseTypeDef:
        """
        [Client.create_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.create_webhook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_project(self, name: str) -> Dict[str, Any]:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.delete_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_report(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.delete_report)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_report_group(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.delete_report_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_source_credentials(self, arn: str) -> ClientDeleteSourceCredentialsResponseTypeDef:
        """
        [Client.delete_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.delete_source_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_webhook(self, projectName: str) -> Dict[str, Any]:
        """
        [Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.delete_webhook)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_test_cases(
        self,
        reportArn: str,
        nextToken: str = None,
        maxResults: int = None,
        filter: ClientDescribeTestCasesFilterTypeDef = None,
    ) -> ClientDescribeTestCasesResponseTypeDef:
        """
        [Client.describe_test_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.describe_test_cases)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_source_credentials(
        self,
        token: str,
        serverType: Literal["GITHUB", "BITBUCKET", "GITHUB_ENTERPRISE"],
        authType: Literal["OAUTH", "BASIC_AUTH", "PERSONAL_ACCESS_TOKEN"],
        username: str = None,
        shouldOverwrite: bool = None,
    ) -> ClientImportSourceCredentialsResponseTypeDef:
        """
        [Client.import_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.import_source_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invalidate_project_cache(self, projectName: str) -> Dict[str, Any]:
        """
        [Client.invalidate_project_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.invalidate_project_cache)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_builds(
        self, sortOrder: Literal["ASCENDING", "DESCENDING"] = None, nextToken: str = None
    ) -> ClientListBuildsResponseTypeDef:
        """
        [Client.list_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.list_builds)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_builds_for_project(
        self,
        projectName: str,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ClientListBuildsForProjectResponseTypeDef:
        """
        [Client.list_builds_for_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.list_builds_for_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_curated_environment_images(
        self, *args: Any, **kwargs: Any
    ) -> ClientListCuratedEnvironmentImagesResponseTypeDef:
        """
        [Client.list_curated_environment_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.list_curated_environment_images)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_projects(
        self,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
    ) -> ClientListProjectsResponseTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.list_projects)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_report_groups(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        sortBy: Literal["NAME", "CREATED_TIME", "LAST_MODIFIED_TIME"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListReportGroupsResponseTypeDef:
        """
        [Client.list_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.list_report_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_reports(
        self,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ClientListReportsFilterTypeDef = None,
    ) -> ClientListReportsResponseTypeDef:
        """
        [Client.list_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.list_reports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_reports_for_report_group(
        self,
        reportGroupArn: str,
        nextToken: str = None,
        sortOrder: Literal["ASCENDING", "DESCENDING"] = None,
        maxResults: int = None,
        filter: ClientListReportsForReportGroupFilterTypeDef = None,
    ) -> ClientListReportsForReportGroupResponseTypeDef:
        """
        [Client.list_reports_for_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.list_reports_for_report_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_source_credentials(
        self, *args: Any, **kwargs: Any
    ) -> ClientListSourceCredentialsResponseTypeDef:
        """
        [Client.list_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.list_source_credentials)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_build(
        self,
        projectName: str,
        secondarySourcesOverride: List[ClientStartBuildSecondarySourcesOverrideTypeDef] = None,
        secondarySourcesVersionOverride: List[
            ClientStartBuildSecondarySourcesVersionOverrideTypeDef
        ] = None,
        sourceVersion: str = None,
        artifactsOverride: ClientStartBuildArtifactsOverrideTypeDef = None,
        secondaryArtifactsOverride: List[ClientStartBuildSecondaryArtifactsOverrideTypeDef] = None,
        environmentVariablesOverride: List[
            ClientStartBuildEnvironmentVariablesOverrideTypeDef
        ] = None,
        sourceTypeOverride: Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ] = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: ClientStartBuildSourceAuthOverrideTypeDef = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: ClientStartBuildGitSubmodulesConfigOverrideTypeDef = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildStatusOverride: bool = None,
        environmentTypeOverride: Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ] = None,
        imageOverride: str = None,
        computeTypeOverride: Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ] = None,
        certificateOverride: str = None,
        cacheOverride: ClientStartBuildCacheOverrideTypeDef = None,
        serviceRoleOverride: str = None,
        privilegedModeOverride: bool = None,
        timeoutInMinutesOverride: int = None,
        queuedTimeoutInMinutesOverride: int = None,
        idempotencyToken: str = None,
        logsConfigOverride: ClientStartBuildLogsConfigOverrideTypeDef = None,
        registryCredentialOverride: ClientStartBuildRegistryCredentialOverrideTypeDef = None,
        imagePullCredentialsTypeOverride: Literal["CODEBUILD", "SERVICE_ROLE"] = None,
    ) -> ClientStartBuildResponseTypeDef:
        """
        [Client.start_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.start_build)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_build(self, id: str) -> ClientStopBuildResponseTypeDef:
        """
        [Client.stop_build documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.stop_build)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_project(
        self,
        name: str,
        description: str = None,
        source: ClientUpdateProjectSourceTypeDef = None,
        secondarySources: List[ClientUpdateProjectSecondarySourcesTypeDef] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List[ClientUpdateProjectSecondarySourceVersionsTypeDef] = None,
        artifacts: ClientUpdateProjectArtifactsTypeDef = None,
        secondaryArtifacts: List[ClientUpdateProjectSecondaryArtifactsTypeDef] = None,
        cache: ClientUpdateProjectCacheTypeDef = None,
        environment: ClientUpdateProjectEnvironmentTypeDef = None,
        serviceRole: str = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List[ClientUpdateProjectTagsTypeDef] = None,
        vpcConfig: ClientUpdateProjectVpcConfigTypeDef = None,
        badgeEnabled: bool = None,
        logsConfig: ClientUpdateProjectLogsConfigTypeDef = None,
    ) -> ClientUpdateProjectResponseTypeDef:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.update_project)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_report_group(
        self, arn: str, exportConfig: ClientUpdateReportGroupExportConfigTypeDef = None
    ) -> ClientUpdateReportGroupResponseTypeDef:
        """
        [Client.update_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.update_report_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        rotateSecret: bool = None,
        filterGroups: List[List[ClientUpdateWebhookFilterGroupsTypeDef]] = None,
    ) -> ClientUpdateWebhookResponseTypeDef:
        """
        [Client.update_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Client.update_webhook)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_builds"]
    ) -> paginator_scope.ListBuildsPaginator:
        """
        [Paginator.ListBuilds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_builds_for_project"]
    ) -> paginator_scope.ListBuildsForProjectPaginator:
        """
        [Paginator.ListBuildsForProject documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_projects"]
    ) -> paginator_scope.ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects)
        """


class Exceptions:
    AccountLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidInputException: Boto3ClientError
    OAuthProviderException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
