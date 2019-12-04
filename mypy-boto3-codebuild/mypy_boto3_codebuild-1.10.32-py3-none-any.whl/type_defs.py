"Main interface for codebuild service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef",
    "ClientBatchDeleteBuildsResponseTypeDef",
    "ClientBatchGetBuildsResponsebuildsartifactsTypeDef",
    "ClientBatchGetBuildsResponsebuildscacheTypeDef",
    "ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef",
    "ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef",
    "ClientBatchGetBuildsResponsebuildsenvironmentTypeDef",
    "ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef",
    "ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef",
    "ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef",
    "ClientBatchGetBuildsResponsebuildslogsTypeDef",
    "ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef",
    "ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef",
    "ClientBatchGetBuildsResponsebuildsphasesTypeDef",
    "ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef",
    "ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef",
    "ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef",
    "ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef",
    "ClientBatchGetBuildsResponsebuildssourceauthTypeDef",
    "ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef",
    "ClientBatchGetBuildsResponsebuildssourceTypeDef",
    "ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef",
    "ClientBatchGetBuildsResponsebuildsTypeDef",
    "ClientBatchGetBuildsResponseTypeDef",
    "ClientBatchGetProjectsResponseprojectsartifactsTypeDef",
    "ClientBatchGetProjectsResponseprojectsbadgeTypeDef",
    "ClientBatchGetProjectsResponseprojectscacheTypeDef",
    "ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef",
    "ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef",
    "ClientBatchGetProjectsResponseprojectsenvironmentTypeDef",
    "ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef",
    "ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef",
    "ClientBatchGetProjectsResponseprojectslogsConfigTypeDef",
    "ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef",
    "ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef",
    "ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef",
    "ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef",
    "ClientBatchGetProjectsResponseprojectssourceauthTypeDef",
    "ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef",
    "ClientBatchGetProjectsResponseprojectssourceTypeDef",
    "ClientBatchGetProjectsResponseprojectstagsTypeDef",
    "ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef",
    "ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef",
    "ClientBatchGetProjectsResponseprojectswebhookTypeDef",
    "ClientBatchGetProjectsResponseprojectsTypeDef",
    "ClientBatchGetProjectsResponseTypeDef",
    "ClientBatchGetReportGroupsResponsereportGroupsexportConfigs3DestinationTypeDef",
    "ClientBatchGetReportGroupsResponsereportGroupsexportConfigTypeDef",
    "ClientBatchGetReportGroupsResponsereportGroupsTypeDef",
    "ClientBatchGetReportGroupsResponseTypeDef",
    "ClientBatchGetReportsResponsereportsexportConfigs3DestinationTypeDef",
    "ClientBatchGetReportsResponsereportsexportConfigTypeDef",
    "ClientBatchGetReportsResponsereportstestSummaryTypeDef",
    "ClientBatchGetReportsResponsereportsTypeDef",
    "ClientBatchGetReportsResponseTypeDef",
    "ClientCreateProjectArtifactsTypeDef",
    "ClientCreateProjectCacheTypeDef",
    "ClientCreateProjectEnvironmentenvironmentVariablesTypeDef",
    "ClientCreateProjectEnvironmentregistryCredentialTypeDef",
    "ClientCreateProjectEnvironmentTypeDef",
    "ClientCreateProjectLogsConfigcloudWatchLogsTypeDef",
    "ClientCreateProjectLogsConfigs3LogsTypeDef",
    "ClientCreateProjectLogsConfigTypeDef",
    "ClientCreateProjectResponseprojectartifactsTypeDef",
    "ClientCreateProjectResponseprojectbadgeTypeDef",
    "ClientCreateProjectResponseprojectcacheTypeDef",
    "ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef",
    "ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef",
    "ClientCreateProjectResponseprojectenvironmentTypeDef",
    "ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef",
    "ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef",
    "ClientCreateProjectResponseprojectlogsConfigTypeDef",
    "ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef",
    "ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef",
    "ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef",
    "ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientCreateProjectResponseprojectsecondarySourcesTypeDef",
    "ClientCreateProjectResponseprojectsourceauthTypeDef",
    "ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef",
    "ClientCreateProjectResponseprojectsourceTypeDef",
    "ClientCreateProjectResponseprojecttagsTypeDef",
    "ClientCreateProjectResponseprojectvpcConfigTypeDef",
    "ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef",
    "ClientCreateProjectResponseprojectwebhookTypeDef",
    "ClientCreateProjectResponseprojectTypeDef",
    "ClientCreateProjectResponseTypeDef",
    "ClientCreateProjectSecondaryArtifactsTypeDef",
    "ClientCreateProjectSecondarySourceVersionsTypeDef",
    "ClientCreateProjectSecondarySourcesauthTypeDef",
    "ClientCreateProjectSecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientCreateProjectSecondarySourcesTypeDef",
    "ClientCreateProjectSourceauthTypeDef",
    "ClientCreateProjectSourcegitSubmodulesConfigTypeDef",
    "ClientCreateProjectSourceTypeDef",
    "ClientCreateProjectTagsTypeDef",
    "ClientCreateProjectVpcConfigTypeDef",
    "ClientCreateReportGroupExportConfigs3DestinationTypeDef",
    "ClientCreateReportGroupExportConfigTypeDef",
    "ClientCreateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef",
    "ClientCreateReportGroupResponsereportGroupexportConfigTypeDef",
    "ClientCreateReportGroupResponsereportGroupTypeDef",
    "ClientCreateReportGroupResponseTypeDef",
    "ClientCreateWebhookFilterGroupsTypeDef",
    "ClientCreateWebhookResponsewebhookfilterGroupsTypeDef",
    "ClientCreateWebhookResponsewebhookTypeDef",
    "ClientCreateWebhookResponseTypeDef",
    "ClientDeleteSourceCredentialsResponseTypeDef",
    "ClientDescribeTestCasesFilterTypeDef",
    "ClientDescribeTestCasesResponsetestCasesTypeDef",
    "ClientDescribeTestCasesResponseTypeDef",
    "ClientImportSourceCredentialsResponseTypeDef",
    "ClientListBuildsForProjectResponseTypeDef",
    "ClientListBuildsResponseTypeDef",
    "ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef",
    "ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef",
    "ClientListCuratedEnvironmentImagesResponseplatformsTypeDef",
    "ClientListCuratedEnvironmentImagesResponseTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientListReportGroupsResponseTypeDef",
    "ClientListReportsFilterTypeDef",
    "ClientListReportsForReportGroupFilterTypeDef",
    "ClientListReportsForReportGroupResponseTypeDef",
    "ClientListReportsResponseTypeDef",
    "ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef",
    "ClientListSourceCredentialsResponseTypeDef",
    "ClientStartBuildArtifactsOverrideTypeDef",
    "ClientStartBuildCacheOverrideTypeDef",
    "ClientStartBuildEnvironmentVariablesOverrideTypeDef",
    "ClientStartBuildGitSubmodulesConfigOverrideTypeDef",
    "ClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef",
    "ClientStartBuildLogsConfigOverrides3LogsTypeDef",
    "ClientStartBuildLogsConfigOverrideTypeDef",
    "ClientStartBuildRegistryCredentialOverrideTypeDef",
    "ClientStartBuildResponsebuildartifactsTypeDef",
    "ClientStartBuildResponsebuildcacheTypeDef",
    "ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef",
    "ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef",
    "ClientStartBuildResponsebuildenvironmentTypeDef",
    "ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef",
    "ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef",
    "ClientStartBuildResponsebuildlogss3LogsTypeDef",
    "ClientStartBuildResponsebuildlogsTypeDef",
    "ClientStartBuildResponsebuildnetworkInterfaceTypeDef",
    "ClientStartBuildResponsebuildphasescontextsTypeDef",
    "ClientStartBuildResponsebuildphasesTypeDef",
    "ClientStartBuildResponsebuildsecondaryArtifactsTypeDef",
    "ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef",
    "ClientStartBuildResponsebuildsecondarySourcesauthTypeDef",
    "ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientStartBuildResponsebuildsecondarySourcesTypeDef",
    "ClientStartBuildResponsebuildsourceauthTypeDef",
    "ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef",
    "ClientStartBuildResponsebuildsourceTypeDef",
    "ClientStartBuildResponsebuildvpcConfigTypeDef",
    "ClientStartBuildResponsebuildTypeDef",
    "ClientStartBuildResponseTypeDef",
    "ClientStartBuildSecondaryArtifactsOverrideTypeDef",
    "ClientStartBuildSecondarySourcesOverrideauthTypeDef",
    "ClientStartBuildSecondarySourcesOverridegitSubmodulesConfigTypeDef",
    "ClientStartBuildSecondarySourcesOverrideTypeDef",
    "ClientStartBuildSecondarySourcesVersionOverrideTypeDef",
    "ClientStartBuildSourceAuthOverrideTypeDef",
    "ClientStopBuildResponsebuildartifactsTypeDef",
    "ClientStopBuildResponsebuildcacheTypeDef",
    "ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef",
    "ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef",
    "ClientStopBuildResponsebuildenvironmentTypeDef",
    "ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef",
    "ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef",
    "ClientStopBuildResponsebuildlogss3LogsTypeDef",
    "ClientStopBuildResponsebuildlogsTypeDef",
    "ClientStopBuildResponsebuildnetworkInterfaceTypeDef",
    "ClientStopBuildResponsebuildphasescontextsTypeDef",
    "ClientStopBuildResponsebuildphasesTypeDef",
    "ClientStopBuildResponsebuildsecondaryArtifactsTypeDef",
    "ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef",
    "ClientStopBuildResponsebuildsecondarySourcesauthTypeDef",
    "ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientStopBuildResponsebuildsecondarySourcesTypeDef",
    "ClientStopBuildResponsebuildsourceauthTypeDef",
    "ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef",
    "ClientStopBuildResponsebuildsourceTypeDef",
    "ClientStopBuildResponsebuildvpcConfigTypeDef",
    "ClientStopBuildResponsebuildTypeDef",
    "ClientStopBuildResponseTypeDef",
    "ClientUpdateProjectArtifactsTypeDef",
    "ClientUpdateProjectCacheTypeDef",
    "ClientUpdateProjectEnvironmentenvironmentVariablesTypeDef",
    "ClientUpdateProjectEnvironmentregistryCredentialTypeDef",
    "ClientUpdateProjectEnvironmentTypeDef",
    "ClientUpdateProjectLogsConfigcloudWatchLogsTypeDef",
    "ClientUpdateProjectLogsConfigs3LogsTypeDef",
    "ClientUpdateProjectLogsConfigTypeDef",
    "ClientUpdateProjectResponseprojectartifactsTypeDef",
    "ClientUpdateProjectResponseprojectbadgeTypeDef",
    "ClientUpdateProjectResponseprojectcacheTypeDef",
    "ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef",
    "ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef",
    "ClientUpdateProjectResponseprojectenvironmentTypeDef",
    "ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef",
    "ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef",
    "ClientUpdateProjectResponseprojectlogsConfigTypeDef",
    "ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef",
    "ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef",
    "ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef",
    "ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientUpdateProjectResponseprojectsecondarySourcesTypeDef",
    "ClientUpdateProjectResponseprojectsourceauthTypeDef",
    "ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef",
    "ClientUpdateProjectResponseprojectsourceTypeDef",
    "ClientUpdateProjectResponseprojecttagsTypeDef",
    "ClientUpdateProjectResponseprojectvpcConfigTypeDef",
    "ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef",
    "ClientUpdateProjectResponseprojectwebhookTypeDef",
    "ClientUpdateProjectResponseprojectTypeDef",
    "ClientUpdateProjectResponseTypeDef",
    "ClientUpdateProjectSecondaryArtifactsTypeDef",
    "ClientUpdateProjectSecondarySourceVersionsTypeDef",
    "ClientUpdateProjectSecondarySourcesauthTypeDef",
    "ClientUpdateProjectSecondarySourcesgitSubmodulesConfigTypeDef",
    "ClientUpdateProjectSecondarySourcesTypeDef",
    "ClientUpdateProjectSourceauthTypeDef",
    "ClientUpdateProjectSourcegitSubmodulesConfigTypeDef",
    "ClientUpdateProjectSourceTypeDef",
    "ClientUpdateProjectTagsTypeDef",
    "ClientUpdateProjectVpcConfigTypeDef",
    "ClientUpdateReportGroupExportConfigs3DestinationTypeDef",
    "ClientUpdateReportGroupExportConfigTypeDef",
    "ClientUpdateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef",
    "ClientUpdateReportGroupResponsereportGroupexportConfigTypeDef",
    "ClientUpdateReportGroupResponsereportGroupTypeDef",
    "ClientUpdateReportGroupResponseTypeDef",
    "ClientUpdateWebhookFilterGroupsTypeDef",
    "ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef",
    "ClientUpdateWebhookResponsewebhookTypeDef",
    "ClientUpdateWebhookResponseTypeDef",
    "ListBuildsForProjectPaginatePaginationConfigTypeDef",
    "ListBuildsForProjectPaginateResponseTypeDef",
    "ListBuildsPaginatePaginationConfigTypeDef",
    "ListBuildsPaginateResponseTypeDef",
    "ListProjectsPaginatePaginationConfigTypeDef",
    "ListProjectsPaginateResponseTypeDef",
)


_ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef = TypedDict(
    "_ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef",
    {"id": str, "statusCode": str},
    total=False,
)


class ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef(
    _ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef
):
    pass


_ClientBatchDeleteBuildsResponseTypeDef = TypedDict(
    "_ClientBatchDeleteBuildsResponseTypeDef",
    {
        "buildsDeleted": List[str],
        "buildsNotDeleted": List[ClientBatchDeleteBuildsResponsebuildsNotDeletedTypeDef],
    },
    total=False,
)


class ClientBatchDeleteBuildsResponseTypeDef(_ClientBatchDeleteBuildsResponseTypeDef):
    """
    - *(dict) --*

      - **buildsDeleted** *(list) --*

        The IDs of the builds that were successfully deleted.
        - *(string) --*
    """


_ClientBatchGetBuildsResponsebuildsartifactsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsartifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildsartifactsTypeDef(
    _ClientBatchGetBuildsResponsebuildsartifactsTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildscacheTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildscacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildscacheTypeDef(
    _ClientBatchGetBuildsResponsebuildscacheTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef(
    _ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef(
    _ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildsenvironmentTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientBatchGetBuildsResponsebuildsenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientBatchGetBuildsResponsebuildsenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildsenvironmentTypeDef(
    _ClientBatchGetBuildsResponsebuildsenvironmentTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef(
    _ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef(
    _ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef(
    _ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildslogsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildslogsTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogsArn": str,
        "s3LogsArn": str,
        "cloudWatchLogs": ClientBatchGetBuildsResponsebuildslogscloudWatchLogsTypeDef,
        "s3Logs": ClientBatchGetBuildsResponsebuildslogss3LogsTypeDef,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildslogsTypeDef(_ClientBatchGetBuildsResponsebuildslogsTypeDef):
    pass


_ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef",
    {"subnetId": str, "networkInterfaceId": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef(
    _ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef",
    {"statusCode": str, "message": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef(
    _ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildsphasesTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsphasesTypeDef",
    {
        "phaseType": Literal[
            "SUBMITTED",
            "QUEUED",
            "PROVISIONING",
            "DOWNLOAD_SOURCE",
            "INSTALL",
            "PRE_BUILD",
            "BUILD",
            "POST_BUILD",
            "UPLOAD_ARTIFACTS",
            "FINALIZING",
            "COMPLETED",
        ],
        "phaseStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[ClientBatchGetBuildsResponsebuildsphasescontextsTypeDef],
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildsphasesTypeDef(
    _ClientBatchGetBuildsResponsebuildsphasesTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef(
    _ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef(
    _ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef(
    _ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetBuildsResponsebuildssecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetBuildsResponsebuildssecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef(
    _ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildssourceauthTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientBatchGetBuildsResponsebuildssourceauthTypeDef(
    _ClientBatchGetBuildsResponsebuildssourceauthTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef(
    _ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildssourceTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildssourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetBuildsResponsebuildssourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetBuildsResponsebuildssourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildssourceTypeDef(
    _ClientBatchGetBuildsResponsebuildssourceTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef(
    _ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef
):
    pass


_ClientBatchGetBuildsResponsebuildsTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponsebuildsTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[ClientBatchGetBuildsResponsebuildsphasesTypeDef],
        "source": ClientBatchGetBuildsResponsebuildssourceTypeDef,
        "secondarySources": List[ClientBatchGetBuildsResponsebuildssecondarySourcesTypeDef],
        "secondarySourceVersions": List[
            ClientBatchGetBuildsResponsebuildssecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientBatchGetBuildsResponsebuildsartifactsTypeDef,
        "secondaryArtifacts": List[ClientBatchGetBuildsResponsebuildssecondaryArtifactsTypeDef],
        "cache": ClientBatchGetBuildsResponsebuildscacheTypeDef,
        "environment": ClientBatchGetBuildsResponsebuildsenvironmentTypeDef,
        "serviceRole": str,
        "logs": ClientBatchGetBuildsResponsebuildslogsTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": ClientBatchGetBuildsResponsebuildsvpcConfigTypeDef,
        "networkInterface": ClientBatchGetBuildsResponsebuildsnetworkInterfaceTypeDef,
        "encryptionKey": str,
        "exportedEnvironmentVariables": List[
            ClientBatchGetBuildsResponsebuildsexportedEnvironmentVariablesTypeDef
        ],
        "reportArns": List[str],
    },
    total=False,
)


class ClientBatchGetBuildsResponsebuildsTypeDef(_ClientBatchGetBuildsResponsebuildsTypeDef):
    """
    - *(dict) --*

      Information about a build.
      - **id** *(string) --*

        The unique ID for the build.
    """


_ClientBatchGetBuildsResponseTypeDef = TypedDict(
    "_ClientBatchGetBuildsResponseTypeDef",
    {"builds": List[ClientBatchGetBuildsResponsebuildsTypeDef], "buildsNotFound": List[str]},
    total=False,
)


class ClientBatchGetBuildsResponseTypeDef(_ClientBatchGetBuildsResponseTypeDef):
    """
    - *(dict) --*

      - **builds** *(list) --*

        Information about the requested builds.
        - *(dict) --*

          Information about a build.
          - **id** *(string) --*

            The unique ID for the build.
    """


_ClientBatchGetProjectsResponseprojectsartifactsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsartifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectsartifactsTypeDef(
    _ClientBatchGetProjectsResponseprojectsartifactsTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectsbadgeTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsbadgeTypeDef",
    {"badgeEnabled": bool, "badgeRequestUrl": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectsbadgeTypeDef(
    _ClientBatchGetProjectsResponseprojectsbadgeTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectscacheTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectscacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectscacheTypeDef(
    _ClientBatchGetProjectsResponseprojectscacheTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef(
    _ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef(
    _ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectsenvironmentTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientBatchGetProjectsResponseprojectsenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientBatchGetProjectsResponseprojectsenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectsenvironmentTypeDef(
    _ClientBatchGetProjectsResponseprojectsenvironmentTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef(
    _ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef(
    _ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectslogsConfigTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectslogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientBatchGetProjectsResponseprojectslogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientBatchGetProjectsResponseprojectslogsConfigs3LogsTypeDef,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectslogsConfigTypeDef(
    _ClientBatchGetProjectsResponseprojectslogsConfigTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef(
    _ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef(
    _ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef(
    _ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetProjectsResponseprojectssecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetProjectsResponseprojectssecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef(
    _ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectssourceauthTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientBatchGetProjectsResponseprojectssourceauthTypeDef(
    _ClientBatchGetProjectsResponseprojectssourceauthTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef(
    _ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectssourceTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectssourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientBatchGetProjectsResponseprojectssourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientBatchGetProjectsResponseprojectssourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectssourceTypeDef(
    _ClientBatchGetProjectsResponseprojectssourceTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectstagsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientBatchGetProjectsResponseprojectstagsTypeDef(
    _ClientBatchGetProjectsResponseprojectstagsTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef(
    _ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef",
    {
        "type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"],
        "pattern": str,
        "excludeMatchedPattern": bool,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef(
    _ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectswebhookTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectswebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[
            List[ClientBatchGetProjectsResponseprojectswebhookfilterGroupsTypeDef]
        ],
        "lastModifiedSecret": datetime,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectswebhookTypeDef(
    _ClientBatchGetProjectsResponseprojectswebhookTypeDef
):
    pass


_ClientBatchGetProjectsResponseprojectsTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseprojectsTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": ClientBatchGetProjectsResponseprojectssourceTypeDef,
        "secondarySources": List[ClientBatchGetProjectsResponseprojectssecondarySourcesTypeDef],
        "sourceVersion": str,
        "secondarySourceVersions": List[
            ClientBatchGetProjectsResponseprojectssecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientBatchGetProjectsResponseprojectsartifactsTypeDef,
        "secondaryArtifacts": List[ClientBatchGetProjectsResponseprojectssecondaryArtifactsTypeDef],
        "cache": ClientBatchGetProjectsResponseprojectscacheTypeDef,
        "environment": ClientBatchGetProjectsResponseprojectsenvironmentTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List[ClientBatchGetProjectsResponseprojectstagsTypeDef],
        "created": datetime,
        "lastModified": datetime,
        "webhook": ClientBatchGetProjectsResponseprojectswebhookTypeDef,
        "vpcConfig": ClientBatchGetProjectsResponseprojectsvpcConfigTypeDef,
        "badge": ClientBatchGetProjectsResponseprojectsbadgeTypeDef,
        "logsConfig": ClientBatchGetProjectsResponseprojectslogsConfigTypeDef,
    },
    total=False,
)


class ClientBatchGetProjectsResponseprojectsTypeDef(_ClientBatchGetProjectsResponseprojectsTypeDef):
    """
    - *(dict) --*

      Information about a build project.
      - **name** *(string) --*

        The name of the build project.
    """


_ClientBatchGetProjectsResponseTypeDef = TypedDict(
    "_ClientBatchGetProjectsResponseTypeDef",
    {
        "projects": List[ClientBatchGetProjectsResponseprojectsTypeDef],
        "projectsNotFound": List[str],
    },
    total=False,
)


class ClientBatchGetProjectsResponseTypeDef(_ClientBatchGetProjectsResponseTypeDef):
    """
    - *(dict) --*

      - **projects** *(list) --*

        Information about the requested build projects.
        - *(dict) --*

          Information about a build project.
          - **name** *(string) --*

            The name of the build project.
    """


_ClientBatchGetReportGroupsResponsereportGroupsexportConfigs3DestinationTypeDef = TypedDict(
    "_ClientBatchGetReportGroupsResponsereportGroupsexportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)


class ClientBatchGetReportGroupsResponsereportGroupsexportConfigs3DestinationTypeDef(
    _ClientBatchGetReportGroupsResponsereportGroupsexportConfigs3DestinationTypeDef
):
    pass


_ClientBatchGetReportGroupsResponsereportGroupsexportConfigTypeDef = TypedDict(
    "_ClientBatchGetReportGroupsResponsereportGroupsexportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientBatchGetReportGroupsResponsereportGroupsexportConfigs3DestinationTypeDef,
    },
    total=False,
)


class ClientBatchGetReportGroupsResponsereportGroupsexportConfigTypeDef(
    _ClientBatchGetReportGroupsResponsereportGroupsexportConfigTypeDef
):
    pass


_ClientBatchGetReportGroupsResponsereportGroupsTypeDef = TypedDict(
    "_ClientBatchGetReportGroupsResponsereportGroupsTypeDef",
    {
        "arn": str,
        "name": str,
        "type": str,
        "exportConfig": ClientBatchGetReportGroupsResponsereportGroupsexportConfigTypeDef,
        "created": datetime,
        "lastModified": datetime,
    },
    total=False,
)


class ClientBatchGetReportGroupsResponsereportGroupsTypeDef(
    _ClientBatchGetReportGroupsResponsereportGroupsTypeDef
):
    """
    - *(dict) --*

      A series of reports. Each report contains information about the results from running a series
      of test cases. You specify the test cases for a report group in the buildspec for a build
      project using one or more paths to the test case files.
      - **arn** *(string) --*

        The ARN of a ``ReportGroup`` .
    """


_ClientBatchGetReportGroupsResponseTypeDef = TypedDict(
    "_ClientBatchGetReportGroupsResponseTypeDef",
    {
        "reportGroups": List[ClientBatchGetReportGroupsResponsereportGroupsTypeDef],
        "reportGroupsNotFound": List[str],
    },
    total=False,
)


class ClientBatchGetReportGroupsResponseTypeDef(_ClientBatchGetReportGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **reportGroups** *(list) --*

        The array of report groups returned by ``BatchGetReportGroups`` .
        - *(dict) --*

          A series of reports. Each report contains information about the results from running a
          series of test cases. You specify the test cases for a report group in the buildspec for a
          build project using one or more paths to the test case files.
          - **arn** *(string) --*

            The ARN of a ``ReportGroup`` .
    """


_ClientBatchGetReportsResponsereportsexportConfigs3DestinationTypeDef = TypedDict(
    "_ClientBatchGetReportsResponsereportsexportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)


class ClientBatchGetReportsResponsereportsexportConfigs3DestinationTypeDef(
    _ClientBatchGetReportsResponsereportsexportConfigs3DestinationTypeDef
):
    pass


_ClientBatchGetReportsResponsereportsexportConfigTypeDef = TypedDict(
    "_ClientBatchGetReportsResponsereportsexportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientBatchGetReportsResponsereportsexportConfigs3DestinationTypeDef,
    },
    total=False,
)


class ClientBatchGetReportsResponsereportsexportConfigTypeDef(
    _ClientBatchGetReportsResponsereportsexportConfigTypeDef
):
    pass


_ClientBatchGetReportsResponsereportstestSummaryTypeDef = TypedDict(
    "_ClientBatchGetReportsResponsereportstestSummaryTypeDef",
    {"total": int, "statusCounts": Dict[str, int], "durationInNanoSeconds": int},
    total=False,
)


class ClientBatchGetReportsResponsereportstestSummaryTypeDef(
    _ClientBatchGetReportsResponsereportstestSummaryTypeDef
):
    pass


_ClientBatchGetReportsResponsereportsTypeDef = TypedDict(
    "_ClientBatchGetReportsResponsereportsTypeDef",
    {
        "arn": str,
        "type": str,
        "name": str,
        "reportGroupArn": str,
        "executionId": str,
        "status": Literal["GENERATING", "SUCCEEDED", "FAILED", "INCOMPLETE", "DELETING"],
        "created": datetime,
        "expired": datetime,
        "exportConfig": ClientBatchGetReportsResponsereportsexportConfigTypeDef,
        "truncated": bool,
        "testSummary": ClientBatchGetReportsResponsereportstestSummaryTypeDef,
    },
    total=False,
)


class ClientBatchGetReportsResponsereportsTypeDef(_ClientBatchGetReportsResponsereportsTypeDef):
    """
    - *(dict) --*

      Information about the results from running a series of test cases during the run of a build
      project. The test cases are specified in the buildspec for the build project using one or more
      paths to the test case files. You can specify any type of tests you want, such as unit tests,
      integration tests, and functional tests.
      - **arn** *(string) --*

        The ARN of the report run.
    """


_ClientBatchGetReportsResponseTypeDef = TypedDict(
    "_ClientBatchGetReportsResponseTypeDef",
    {"reports": List[ClientBatchGetReportsResponsereportsTypeDef], "reportsNotFound": List[str]},
    total=False,
)


class ClientBatchGetReportsResponseTypeDef(_ClientBatchGetReportsResponseTypeDef):
    """
    - *(dict) --*

      - **reports** *(list) --*

        The array of ``Report`` objects returned by ``BatchGetReports`` .
        - *(dict) --*

          Information about the results from running a series of test cases during the run of a
          build project. The test cases are specified in the buildspec for the build project using
          one or more paths to the test case files. You can specify any type of tests you want, such
          as unit tests, integration tests, and functional tests.
          - **arn** *(string) --*

            The ARN of the report run.
    """


_RequiredClientCreateProjectArtifactsTypeDef = TypedDict(
    "_RequiredClientCreateProjectArtifactsTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientCreateProjectArtifactsTypeDef = TypedDict(
    "_OptionalClientCreateProjectArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectArtifactsTypeDef(
    _RequiredClientCreateProjectArtifactsTypeDef, _OptionalClientCreateProjectArtifactsTypeDef
):
    """
    Information about the build output artifacts for the build project.
    - **type** *(string) --***[REQUIRED]**

      The type of build output artifact. Valid values include:
      * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.
      .. note::

        The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .
    """


_RequiredClientCreateProjectCacheTypeDef = TypedDict(
    "_RequiredClientCreateProjectCacheTypeDef", {"type": Literal["NO_CACHE", "S3", "LOCAL"]}
)
_OptionalClientCreateProjectCacheTypeDef = TypedDict(
    "_OptionalClientCreateProjectCacheTypeDef",
    {
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientCreateProjectCacheTypeDef(
    _RequiredClientCreateProjectCacheTypeDef, _OptionalClientCreateProjectCacheTypeDef
):
    """
    Stores recently used information so that it can be quickly accessed at a later time.
    - **type** *(string) --***[REQUIRED]**

      The type of cache used by the build project. Valid values include:
      * ``NO_CACHE`` : The build project does not use any cache.
      * ``S3`` : The build project reads and writes from and to S3.
      * ``LOCAL`` : The build project stores a cache locally on a build host that is only available
      to that build host.
    """


_ClientCreateProjectEnvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientCreateProjectEnvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class ClientCreateProjectEnvironmentenvironmentVariablesTypeDef(
    _ClientCreateProjectEnvironmentenvironmentVariablesTypeDef
):
    pass


_ClientCreateProjectEnvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientCreateProjectEnvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientCreateProjectEnvironmentregistryCredentialTypeDef(
    _ClientCreateProjectEnvironmentregistryCredentialTypeDef
):
    pass


_RequiredClientCreateProjectEnvironmentTypeDef = TypedDict(
    "_RequiredClientCreateProjectEnvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ]
    },
)
_OptionalClientCreateProjectEnvironmentTypeDef = TypedDict(
    "_OptionalClientCreateProjectEnvironmentTypeDef",
    {
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[ClientCreateProjectEnvironmentenvironmentVariablesTypeDef],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientCreateProjectEnvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ClientCreateProjectEnvironmentTypeDef(
    _RequiredClientCreateProjectEnvironmentTypeDef, _OptionalClientCreateProjectEnvironmentTypeDef
):
    """
    Information about the build environment for the build project.
    - **type** *(string) --***[REQUIRED]**

      The type of build environment to use for related builds.
      * The environment type ``ARM_CONTAINER`` is available only in regions US East (N. Virginia),
      US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo),
      Asia Pacific (Sydney), and EU (Frankfurt).
      * The environment type ``LINUX_CONTAINER`` with compute type ``build.general1.2xlarge`` is
      available only in regions US East (N. Virginia), US East (N. Virginia), US West (Oregon),
      Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia
      Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China
      (Ningxia).
      * The environment type ``LINUX_GPU_CONTAINER`` is available only in regions US East (N.
      Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), EU (Ireland), EU
      (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific
      (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).
    """


_RequiredClientCreateProjectLogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientCreateProjectLogsConfigcloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"]},
)
_OptionalClientCreateProjectLogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientCreateProjectLogsConfigcloudWatchLogsTypeDef",
    {"groupName": str, "streamName": str},
    total=False,
)


class ClientCreateProjectLogsConfigcloudWatchLogsTypeDef(
    _RequiredClientCreateProjectLogsConfigcloudWatchLogsTypeDef,
    _OptionalClientCreateProjectLogsConfigcloudWatchLogsTypeDef,
):
    """
    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.
      - **status** *(string) --***[REQUIRED]**

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
        are:
        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.
        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.
    """


_ClientCreateProjectLogsConfigs3LogsTypeDef = TypedDict(
    "_ClientCreateProjectLogsConfigs3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientCreateProjectLogsConfigs3LogsTypeDef(_ClientCreateProjectLogsConfigs3LogsTypeDef):
    pass


_ClientCreateProjectLogsConfigTypeDef = TypedDict(
    "_ClientCreateProjectLogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientCreateProjectLogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientCreateProjectLogsConfigs3LogsTypeDef,
    },
    total=False,
)


class ClientCreateProjectLogsConfigTypeDef(_ClientCreateProjectLogsConfigTypeDef):
    """
    Information about logs for the build project. These can be logs in Amazon CloudWatch Logs, logs
    uploaded to a specified S3 bucket, or both.
    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.
      - **status** *(string) --***[REQUIRED]**

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
        are:
        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.
        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.
    """


_ClientCreateProjectResponseprojectartifactsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectartifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectResponseprojectartifactsTypeDef(
    _ClientCreateProjectResponseprojectartifactsTypeDef
):
    pass


_ClientCreateProjectResponseprojectbadgeTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectbadgeTypeDef",
    {"badgeEnabled": bool, "badgeRequestUrl": str},
    total=False,
)


class ClientCreateProjectResponseprojectbadgeTypeDef(
    _ClientCreateProjectResponseprojectbadgeTypeDef
):
    pass


_ClientCreateProjectResponseprojectcacheTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectcacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientCreateProjectResponseprojectcacheTypeDef(
    _ClientCreateProjectResponseprojectcacheTypeDef
):
    pass


_ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef(
    _ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef
):
    pass


_ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef(
    _ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef
):
    pass


_ClientCreateProjectResponseprojectenvironmentTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientCreateProjectResponseprojectenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientCreateProjectResponseprojectenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ClientCreateProjectResponseprojectenvironmentTypeDef(
    _ClientCreateProjectResponseprojectenvironmentTypeDef
):
    pass


_ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)


class ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef(
    _ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef
):
    pass


_ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef(
    _ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef
):
    pass


_ClientCreateProjectResponseprojectlogsConfigTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectlogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientCreateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientCreateProjectResponseprojectlogsConfigs3LogsTypeDef,
    },
    total=False,
)


class ClientCreateProjectResponseprojectlogsConfigTypeDef(
    _ClientCreateProjectResponseprojectlogsConfigTypeDef
):
    pass


_ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef(
    _ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef
):
    pass


_ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef(
    _ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef
):
    pass


_ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef(
    _ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef
):
    pass


_ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef
):
    pass


_ClientCreateProjectResponseprojectsecondarySourcesTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectResponseprojectsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectResponseprojectsecondarySourcesTypeDef(
    _ClientCreateProjectResponseprojectsecondarySourcesTypeDef
):
    pass


_ClientCreateProjectResponseprojectsourceauthTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientCreateProjectResponseprojectsourceauthTypeDef(
    _ClientCreateProjectResponseprojectsourceauthTypeDef
):
    pass


_ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef(
    _ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef
):
    pass


_ClientCreateProjectResponseprojectsourceTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectsourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectResponseprojectsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectResponseprojectsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectResponseprojectsourceTypeDef(
    _ClientCreateProjectResponseprojectsourceTypeDef
):
    pass


_ClientCreateProjectResponseprojecttagsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojecttagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateProjectResponseprojecttagsTypeDef(_ClientCreateProjectResponseprojecttagsTypeDef):
    pass


_ClientCreateProjectResponseprojectvpcConfigTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientCreateProjectResponseprojectvpcConfigTypeDef(
    _ClientCreateProjectResponseprojectvpcConfigTypeDef
):
    pass


_ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef",
    {
        "type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"],
        "pattern": str,
        "excludeMatchedPattern": bool,
    },
    total=False,
)


class ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef(
    _ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef
):
    pass


_ClientCreateProjectResponseprojectwebhookTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectwebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List[ClientCreateProjectResponseprojectwebhookfilterGroupsTypeDef]],
        "lastModifiedSecret": datetime,
    },
    total=False,
)


class ClientCreateProjectResponseprojectwebhookTypeDef(
    _ClientCreateProjectResponseprojectwebhookTypeDef
):
    pass


_ClientCreateProjectResponseprojectTypeDef = TypedDict(
    "_ClientCreateProjectResponseprojectTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": ClientCreateProjectResponseprojectsourceTypeDef,
        "secondarySources": List[ClientCreateProjectResponseprojectsecondarySourcesTypeDef],
        "sourceVersion": str,
        "secondarySourceVersions": List[
            ClientCreateProjectResponseprojectsecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientCreateProjectResponseprojectartifactsTypeDef,
        "secondaryArtifacts": List[ClientCreateProjectResponseprojectsecondaryArtifactsTypeDef],
        "cache": ClientCreateProjectResponseprojectcacheTypeDef,
        "environment": ClientCreateProjectResponseprojectenvironmentTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List[ClientCreateProjectResponseprojecttagsTypeDef],
        "created": datetime,
        "lastModified": datetime,
        "webhook": ClientCreateProjectResponseprojectwebhookTypeDef,
        "vpcConfig": ClientCreateProjectResponseprojectvpcConfigTypeDef,
        "badge": ClientCreateProjectResponseprojectbadgeTypeDef,
        "logsConfig": ClientCreateProjectResponseprojectlogsConfigTypeDef,
    },
    total=False,
)


class ClientCreateProjectResponseprojectTypeDef(_ClientCreateProjectResponseprojectTypeDef):
    """
    - **project** *(dict) --*

      Information about the build project that was created.
      - **name** *(string) --*

        The name of the build project.
    """


_ClientCreateProjectResponseTypeDef = TypedDict(
    "_ClientCreateProjectResponseTypeDef",
    {"project": ClientCreateProjectResponseprojectTypeDef},
    total=False,
)


class ClientCreateProjectResponseTypeDef(_ClientCreateProjectResponseTypeDef):
    """
    - *(dict) --*

      - **project** *(dict) --*

        Information about the build project that was created.
        - **name** *(string) --*

          The name of the build project.
    """


_RequiredClientCreateProjectSecondaryArtifactsTypeDef = TypedDict(
    "_RequiredClientCreateProjectSecondaryArtifactsTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientCreateProjectSecondaryArtifactsTypeDef = TypedDict(
    "_OptionalClientCreateProjectSecondaryArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectSecondaryArtifactsTypeDef(
    _RequiredClientCreateProjectSecondaryArtifactsTypeDef,
    _OptionalClientCreateProjectSecondaryArtifactsTypeDef,
):
    """
    - *(dict) --*

      Information about the build output artifacts for the build project.
      - **type** *(string) --***[REQUIRED]**

        The type of build output artifact. Valid values include:
        * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.
        .. note::

          The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .
    """


_RequiredClientCreateProjectSecondarySourceVersionsTypeDef = TypedDict(
    "_RequiredClientCreateProjectSecondarySourceVersionsTypeDef", {"sourceIdentifier": str}
)
_OptionalClientCreateProjectSecondarySourceVersionsTypeDef = TypedDict(
    "_OptionalClientCreateProjectSecondarySourceVersionsTypeDef",
    {"sourceVersion": str},
    total=False,
)


class ClientCreateProjectSecondarySourceVersionsTypeDef(
    _RequiredClientCreateProjectSecondarySourceVersionsTypeDef,
    _OptionalClientCreateProjectSecondarySourceVersionsTypeDef,
):
    """
    - *(dict) --*

      A source identifier and its corresponding version.
      - **sourceIdentifier** *(string) --***[REQUIRED]**

        An identifier for a source in the build project.
    """


_ClientCreateProjectSecondarySourcesauthTypeDef = TypedDict(
    "_ClientCreateProjectSecondarySourcesauthTypeDef", {"type": str, "resource": str}, total=False
)


class ClientCreateProjectSecondarySourcesauthTypeDef(
    _ClientCreateProjectSecondarySourcesauthTypeDef
):
    pass


_ClientCreateProjectSecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientCreateProjectSecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientCreateProjectSecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientCreateProjectSecondarySourcesgitSubmodulesConfigTypeDef
):
    pass


_RequiredClientCreateProjectSecondarySourcesTypeDef = TypedDict(
    "_RequiredClientCreateProjectSecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalClientCreateProjectSecondarySourcesTypeDef = TypedDict(
    "_OptionalClientCreateProjectSecondarySourcesTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectSecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectSecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectSecondarySourcesTypeDef(
    _RequiredClientCreateProjectSecondarySourcesTypeDef,
    _OptionalClientCreateProjectSecondarySourcesTypeDef,
):
    """
    - *(dict) --*

      Information about the build input source code for the build project.
      - **type** *(string) --***[REQUIRED]**

        The type of repository that contains the source code to be built. Valid values include:
        * ``BITBUCKET`` : The source code is in a Bitbucket repository.
        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.
        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
        pipeline in AWS CodePipeline.
        * ``GITHUB`` : The source code is in a GitHub repository.
        * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.
        * ``NO_SOURCE`` : The project does not have input source code.
        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    """


_ClientCreateProjectSourceauthTypeDef = TypedDict(
    "_ClientCreateProjectSourceauthTypeDef", {"type": str, "resource": str}, total=False
)


class ClientCreateProjectSourceauthTypeDef(_ClientCreateProjectSourceauthTypeDef):
    pass


_ClientCreateProjectSourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientCreateProjectSourcegitSubmodulesConfigTypeDef", {"fetchSubmodules": bool}, total=False
)


class ClientCreateProjectSourcegitSubmodulesConfigTypeDef(
    _ClientCreateProjectSourcegitSubmodulesConfigTypeDef
):
    pass


_RequiredClientCreateProjectSourceTypeDef = TypedDict(
    "_RequiredClientCreateProjectSourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalClientCreateProjectSourceTypeDef = TypedDict(
    "_OptionalClientCreateProjectSourceTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientCreateProjectSourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientCreateProjectSourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientCreateProjectSourceTypeDef(
    _RequiredClientCreateProjectSourceTypeDef, _OptionalClientCreateProjectSourceTypeDef
):
    """
    Information about the build input source code for the build project.
    - **type** *(string) --***[REQUIRED]**

      The type of repository that contains the source code to be built. Valid values include:
      * ``BITBUCKET`` : The source code is in a Bitbucket repository.
      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.
      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline
      in AWS CodePipeline.
      * ``GITHUB`` : The source code is in a GitHub repository.
      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.
      * ``NO_SOURCE`` : The project does not have input source code.
      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    """


_ClientCreateProjectTagsTypeDef = TypedDict(
    "_ClientCreateProjectTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateProjectTagsTypeDef(_ClientCreateProjectTagsTypeDef):
    """
    - *(dict) --*

      A tag, consisting of a key and a value.
      This tag is available for use by AWS services that support tags in AWS CodeBuild.
      - **key** *(string) --*

        The tag's key.
    """


_ClientCreateProjectVpcConfigTypeDef = TypedDict(
    "_ClientCreateProjectVpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientCreateProjectVpcConfigTypeDef(_ClientCreateProjectVpcConfigTypeDef):
    """
    VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.
    - **vpcId** *(string) --*

      The ID of the Amazon VPC.
    """


_ClientCreateReportGroupExportConfigs3DestinationTypeDef = TypedDict(
    "_ClientCreateReportGroupExportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)


class ClientCreateReportGroupExportConfigs3DestinationTypeDef(
    _ClientCreateReportGroupExportConfigs3DestinationTypeDef
):
    pass


_ClientCreateReportGroupExportConfigTypeDef = TypedDict(
    "_ClientCreateReportGroupExportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientCreateReportGroupExportConfigs3DestinationTypeDef,
    },
    total=False,
)


class ClientCreateReportGroupExportConfigTypeDef(_ClientCreateReportGroupExportConfigTypeDef):
    """
    A ``ReportExportConfig`` object that contains information about where the report group test
    results are exported.
    - **exportConfigType** *(string) --*

      The export configuration type. Valid values are:
      * ``S3`` : The report results are exported to an S3 bucket.
      * ``NO_EXPORT`` : The report results are not exported.
    """


_ClientCreateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef = TypedDict(
    "_ClientCreateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)


class ClientCreateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef(
    _ClientCreateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef
):
    pass


_ClientCreateReportGroupResponsereportGroupexportConfigTypeDef = TypedDict(
    "_ClientCreateReportGroupResponsereportGroupexportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientCreateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef,
    },
    total=False,
)


class ClientCreateReportGroupResponsereportGroupexportConfigTypeDef(
    _ClientCreateReportGroupResponsereportGroupexportConfigTypeDef
):
    pass


_ClientCreateReportGroupResponsereportGroupTypeDef = TypedDict(
    "_ClientCreateReportGroupResponsereportGroupTypeDef",
    {
        "arn": str,
        "name": str,
        "type": str,
        "exportConfig": ClientCreateReportGroupResponsereportGroupexportConfigTypeDef,
        "created": datetime,
        "lastModified": datetime,
    },
    total=False,
)


class ClientCreateReportGroupResponsereportGroupTypeDef(
    _ClientCreateReportGroupResponsereportGroupTypeDef
):
    """
    - **reportGroup** *(dict) --*

      Information about the report group that was created.
      - **arn** *(string) --*

        The ARN of a ``ReportGroup`` .
    """


_ClientCreateReportGroupResponseTypeDef = TypedDict(
    "_ClientCreateReportGroupResponseTypeDef",
    {"reportGroup": ClientCreateReportGroupResponsereportGroupTypeDef},
    total=False,
)


class ClientCreateReportGroupResponseTypeDef(_ClientCreateReportGroupResponseTypeDef):
    """
    - *(dict) --*

      - **reportGroup** *(dict) --*

        Information about the report group that was created.
        - **arn** *(string) --*

          The ARN of a ``ReportGroup`` .
    """


_RequiredClientCreateWebhookFilterGroupsTypeDef = TypedDict(
    "_RequiredClientCreateWebhookFilterGroupsTypeDef",
    {"type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"]},
)
_OptionalClientCreateWebhookFilterGroupsTypeDef = TypedDict(
    "_OptionalClientCreateWebhookFilterGroupsTypeDef",
    {"pattern": str, "excludeMatchedPattern": bool},
    total=False,
)


class ClientCreateWebhookFilterGroupsTypeDef(
    _RequiredClientCreateWebhookFilterGroupsTypeDef, _OptionalClientCreateWebhookFilterGroupsTypeDef
):
    """
    - *(dict) --*

      A filter used to determine which webhooks trigger a build.
      - **type** *(string) --***[REQUIRED]**

        The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
        ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

          EVENT
    """


_ClientCreateWebhookResponsewebhookfilterGroupsTypeDef = TypedDict(
    "_ClientCreateWebhookResponsewebhookfilterGroupsTypeDef",
    {
        "type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"],
        "pattern": str,
        "excludeMatchedPattern": bool,
    },
    total=False,
)


class ClientCreateWebhookResponsewebhookfilterGroupsTypeDef(
    _ClientCreateWebhookResponsewebhookfilterGroupsTypeDef
):
    pass


_ClientCreateWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientCreateWebhookResponsewebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List[ClientCreateWebhookResponsewebhookfilterGroupsTypeDef]],
        "lastModifiedSecret": datetime,
    },
    total=False,
)


class ClientCreateWebhookResponsewebhookTypeDef(_ClientCreateWebhookResponsewebhookTypeDef):
    """
    - **webhook** *(dict) --*

      Information about a webhook that connects repository events to a build project in AWS
      CodeBuild.
      - **url** *(string) --*

        The URL to the webhook.
    """


_ClientCreateWebhookResponseTypeDef = TypedDict(
    "_ClientCreateWebhookResponseTypeDef",
    {"webhook": ClientCreateWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientCreateWebhookResponseTypeDef(_ClientCreateWebhookResponseTypeDef):
    """
    - *(dict) --*

      - **webhook** *(dict) --*

        Information about a webhook that connects repository events to a build project in AWS
        CodeBuild.
        - **url** *(string) --*

          The URL to the webhook.
    """


_ClientDeleteSourceCredentialsResponseTypeDef = TypedDict(
    "_ClientDeleteSourceCredentialsResponseTypeDef", {"arn": str}, total=False
)


class ClientDeleteSourceCredentialsResponseTypeDef(_ClientDeleteSourceCredentialsResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the token.
    """


_ClientDescribeTestCasesFilterTypeDef = TypedDict(
    "_ClientDescribeTestCasesFilterTypeDef", {"status": str}, total=False
)


class ClientDescribeTestCasesFilterTypeDef(_ClientDescribeTestCasesFilterTypeDef):
    """
    A ``TestCaseFilter`` object used to filter the returned reports.
    - **status** *(string) --*

      The status used to filter test cases. Valid statuses are ``SUCCEEDED`` , ``FAILED`` ,
      ``ERROR`` , ``SKIPPED`` , and ``UNKNOWN`` . A ``TestCaseFilter`` can have one status.
    """


_ClientDescribeTestCasesResponsetestCasesTypeDef = TypedDict(
    "_ClientDescribeTestCasesResponsetestCasesTypeDef",
    {
        "reportArn": str,
        "testRawDataPath": str,
        "prefix": str,
        "name": str,
        "status": str,
        "durationInNanoSeconds": int,
        "message": str,
        "expired": datetime,
    },
    total=False,
)


class ClientDescribeTestCasesResponsetestCasesTypeDef(
    _ClientDescribeTestCasesResponsetestCasesTypeDef
):
    pass


_ClientDescribeTestCasesResponseTypeDef = TypedDict(
    "_ClientDescribeTestCasesResponseTypeDef",
    {"nextToken": str, "testCases": List[ClientDescribeTestCasesResponsetestCasesTypeDef]},
    total=False,
)


class ClientDescribeTestCasesResponseTypeDef(_ClientDescribeTestCasesResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        During a previous call, the maximum number of items that can be returned is the value
        specified in ``maxResults`` . If there more items in the list, then a unique string called a
        *nextToken* is returned. To get the next batch of items in the list, call this operation
        again, adding the next token to the call. To get all of the items in the list, keep calling
        this operation with each subsequent next token that is returned, until no more next tokens
        are returned.
    """


_ClientImportSourceCredentialsResponseTypeDef = TypedDict(
    "_ClientImportSourceCredentialsResponseTypeDef", {"arn": str}, total=False
)


class ClientImportSourceCredentialsResponseTypeDef(_ClientImportSourceCredentialsResponseTypeDef):
    """
    - *(dict) --*

      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the token.
    """


_ClientListBuildsForProjectResponseTypeDef = TypedDict(
    "_ClientListBuildsForProjectResponseTypeDef", {"ids": List[str], "nextToken": str}, total=False
)


class ClientListBuildsForProjectResponseTypeDef(_ClientListBuildsForProjectResponseTypeDef):
    """
    - *(dict) --*

      - **ids** *(list) --*

        A list of build IDs for the specified build project, with each build ID representing a
        single build.
        - *(string) --*
    """


_ClientListBuildsResponseTypeDef = TypedDict(
    "_ClientListBuildsResponseTypeDef", {"ids": List[str], "nextToken": str}, total=False
)


class ClientListBuildsResponseTypeDef(_ClientListBuildsResponseTypeDef):
    """
    - *(dict) --*

      - **ids** *(list) --*

        A list of build IDs, with each build ID representing a single build.
        - *(string) --*
    """


_ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef = TypedDict(
    "_ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef",
    {"name": str, "description": str, "versions": List[str]},
    total=False,
)


class ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef(
    _ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef
):
    pass


_ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef = TypedDict(
    "_ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef",
    {
        "language": Literal[
            "JAVA",
            "PYTHON",
            "NODE_JS",
            "RUBY",
            "GOLANG",
            "DOCKER",
            "ANDROID",
            "DOTNET",
            "BASE",
            "PHP",
        ],
        "images": List[ClientListCuratedEnvironmentImagesResponseplatformslanguagesimagesTypeDef],
    },
    total=False,
)


class ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef(
    _ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef
):
    pass


_ClientListCuratedEnvironmentImagesResponseplatformsTypeDef = TypedDict(
    "_ClientListCuratedEnvironmentImagesResponseplatformsTypeDef",
    {
        "platform": Literal["DEBIAN", "AMAZON_LINUX", "UBUNTU", "WINDOWS_SERVER"],
        "languages": List[ClientListCuratedEnvironmentImagesResponseplatformslanguagesTypeDef],
    },
    total=False,
)


class ClientListCuratedEnvironmentImagesResponseplatformsTypeDef(
    _ClientListCuratedEnvironmentImagesResponseplatformsTypeDef
):
    """
    - *(dict) --*

      A set of Docker images that are related by platform and are managed by AWS CodeBuild.
      - **platform** *(string) --*

        The platform's name.
    """


_ClientListCuratedEnvironmentImagesResponseTypeDef = TypedDict(
    "_ClientListCuratedEnvironmentImagesResponseTypeDef",
    {"platforms": List[ClientListCuratedEnvironmentImagesResponseplatformsTypeDef]},
    total=False,
)


class ClientListCuratedEnvironmentImagesResponseTypeDef(
    _ClientListCuratedEnvironmentImagesResponseTypeDef
):
    """
    - *(dict) --*

      - **platforms** *(list) --*

        Information about supported platforms for Docker images that are managed by AWS CodeBuild.
        - *(dict) --*

          A set of Docker images that are related by platform and are managed by AWS CodeBuild.
          - **platform** *(string) --*

            The platform's name.
    """


_ClientListProjectsResponseTypeDef = TypedDict(
    "_ClientListProjectsResponseTypeDef", {"nextToken": str, "projects": List[str]}, total=False
)


class ClientListProjectsResponseTypeDef(_ClientListProjectsResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        If there are more than 100 items in the list, only the first 100 items are returned, along
        with a unique string called a *nextToken* . To get the next batch of items in the list, call
        this operation again, adding the next token to the call.
    """


_ClientListReportGroupsResponseTypeDef = TypedDict(
    "_ClientListReportGroupsResponseTypeDef",
    {"nextToken": str, "reportGroups": List[str]},
    total=False,
)


class ClientListReportGroupsResponseTypeDef(_ClientListReportGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        During a previous call, the maximum number of items that can be returned is the value
        specified in ``maxResults`` . If there more items in the list, then a unique string called a
        *nextToken* is returned. To get the next batch of items in the list, call this operation
        again, adding the next token to the call. To get all of the items in the list, keep calling
        this operation with each subsequent next token that is returned, until no more next tokens
        are returned.
    """


_ClientListReportsFilterTypeDef = TypedDict(
    "_ClientListReportsFilterTypeDef",
    {"status": Literal["GENERATING", "SUCCEEDED", "FAILED", "INCOMPLETE", "DELETING"]},
    total=False,
)


class ClientListReportsFilterTypeDef(_ClientListReportsFilterTypeDef):
    """
    A ``ReportFilter`` object used to filter the returned reports.
    - **status** *(string) --*

      The status used to filter reports. You can filter using one status only.
    """


_ClientListReportsForReportGroupFilterTypeDef = TypedDict(
    "_ClientListReportsForReportGroupFilterTypeDef",
    {"status": Literal["GENERATING", "SUCCEEDED", "FAILED", "INCOMPLETE", "DELETING"]},
    total=False,
)


class ClientListReportsForReportGroupFilterTypeDef(_ClientListReportsForReportGroupFilterTypeDef):
    """
    A ``ReportFilter`` object used to filter the returned reports.
    - **status** *(string) --*

      The status used to filter reports. You can filter using one status only.
    """


_ClientListReportsForReportGroupResponseTypeDef = TypedDict(
    "_ClientListReportsForReportGroupResponseTypeDef",
    {"nextToken": str, "reports": List[str]},
    total=False,
)


class ClientListReportsForReportGroupResponseTypeDef(
    _ClientListReportsForReportGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        During a previous call, the maximum number of items that can be returned is the value
        specified in ``maxResults`` . If there more items in the list, then a unique string called a
        *nextToken* is returned. To get the next batch of items in the list, call this operation
        again, adding the next token to the call. To get all of the items in the list, keep calling
        this operation with each subsequent next token that is returned, until no more next tokens
        are returned.
    """


_ClientListReportsResponseTypeDef = TypedDict(
    "_ClientListReportsResponseTypeDef", {"nextToken": str, "reports": List[str]}, total=False
)


class ClientListReportsResponseTypeDef(_ClientListReportsResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        During a previous call, the maximum number of items that can be returned is the value
        specified in ``maxResults`` . If there more items in the list, then a unique string called a
        *nextToken* is returned. To get the next batch of items in the list, call this operation
        again, adding the next token to the call. To get all of the items in the list, keep calling
        this operation with each subsequent next token that is returned, until no more next tokens
        are returned.
    """


_ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef = TypedDict(
    "_ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef",
    {
        "arn": str,
        "serverType": Literal["GITHUB", "BITBUCKET", "GITHUB_ENTERPRISE"],
        "authType": Literal["OAUTH", "BASIC_AUTH", "PERSONAL_ACCESS_TOKEN"],
    },
    total=False,
)


class ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef(
    _ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef
):
    """
    - *(dict) --*

      Information about the credentials for a GitHub, GitHub Enterprise, or Bitbucket repository.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the token.
    """


_ClientListSourceCredentialsResponseTypeDef = TypedDict(
    "_ClientListSourceCredentialsResponseTypeDef",
    {
        "sourceCredentialsInfos": List[
            ClientListSourceCredentialsResponsesourceCredentialsInfosTypeDef
        ]
    },
    total=False,
)


class ClientListSourceCredentialsResponseTypeDef(_ClientListSourceCredentialsResponseTypeDef):
    """
    - *(dict) --*

      - **sourceCredentialsInfos** *(list) --*

        A list of ``SourceCredentialsInfo`` objects. Each ``SourceCredentialsInfo`` object includes
        the authentication type, token ARN, and type of source provider for one set of credentials.
        - *(dict) --*

          Information about the credentials for a GitHub, GitHub Enterprise, or Bitbucket
          repository.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the token.
    """


_RequiredClientStartBuildArtifactsOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildArtifactsOverrideTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientStartBuildArtifactsOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildArtifactsOverrideTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStartBuildArtifactsOverrideTypeDef(
    _RequiredClientStartBuildArtifactsOverrideTypeDef,
    _OptionalClientStartBuildArtifactsOverrideTypeDef,
):
    """
    Build output artifact settings that override, for this build only, the latest ones already
    defined in the build project.
    - **type** *(string) --***[REQUIRED]**

      The type of build output artifact. Valid values include:
      * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.
      .. note::

        The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .
    """


_RequiredClientStartBuildCacheOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildCacheOverrideTypeDef", {"type": Literal["NO_CACHE", "S3", "LOCAL"]}
)
_OptionalClientStartBuildCacheOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildCacheOverrideTypeDef",
    {
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientStartBuildCacheOverrideTypeDef(
    _RequiredClientStartBuildCacheOverrideTypeDef, _OptionalClientStartBuildCacheOverrideTypeDef
):
    """
    A ProjectCache object specified for this build that overrides the one defined in the build
    project.
    - **type** *(string) --***[REQUIRED]**

      The type of cache used by the build project. Valid values include:
      * ``NO_CACHE`` : The build project does not use any cache.
      * ``S3`` : The build project reads and writes from and to S3.
      * ``LOCAL`` : The build project stores a cache locally on a build host that is only available
      to that build host.
    """


_RequiredClientStartBuildEnvironmentVariablesOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildEnvironmentVariablesOverrideTypeDef", {"name": str}
)
_OptionalClientStartBuildEnvironmentVariablesOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildEnvironmentVariablesOverrideTypeDef",
    {"value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class ClientStartBuildEnvironmentVariablesOverrideTypeDef(
    _RequiredClientStartBuildEnvironmentVariablesOverrideTypeDef,
    _OptionalClientStartBuildEnvironmentVariablesOverrideTypeDef,
):
    """
    - *(dict) --*

      Information about an environment variable for a build project or a build.
      - **name** *(string) --***[REQUIRED]**

        The name or key of the environment variable.
    """


_ClientStartBuildGitSubmodulesConfigOverrideTypeDef = TypedDict(
    "_ClientStartBuildGitSubmodulesConfigOverrideTypeDef", {"fetchSubmodules": bool}
)


class ClientStartBuildGitSubmodulesConfigOverrideTypeDef(
    _ClientStartBuildGitSubmodulesConfigOverrideTypeDef
):
    """
    Information about the Git submodules configuration for this build of an AWS CodeBuild build
    project.
    - **fetchSubmodules** *(boolean) --***[REQUIRED]**

      Set to true to fetch Git submodules for your AWS CodeBuild build project.
    """


_RequiredClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"]},
)
_OptionalClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef",
    {"groupName": str, "streamName": str},
    total=False,
)


class ClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef(
    _RequiredClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef,
    _OptionalClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef,
):
    """
    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.
      - **status** *(string) --***[REQUIRED]**

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
        are:
        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.
        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.
    """


_ClientStartBuildLogsConfigOverrides3LogsTypeDef = TypedDict(
    "_ClientStartBuildLogsConfigOverrides3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientStartBuildLogsConfigOverrides3LogsTypeDef(
    _ClientStartBuildLogsConfigOverrides3LogsTypeDef
):
    pass


_ClientStartBuildLogsConfigOverrideTypeDef = TypedDict(
    "_ClientStartBuildLogsConfigOverrideTypeDef",
    {
        "cloudWatchLogs": ClientStartBuildLogsConfigOverridecloudWatchLogsTypeDef,
        "s3Logs": ClientStartBuildLogsConfigOverrides3LogsTypeDef,
    },
    total=False,
)


class ClientStartBuildLogsConfigOverrideTypeDef(_ClientStartBuildLogsConfigOverrideTypeDef):
    """
    Log settings for this build that override the log settings defined in the build project.
    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.
      - **status** *(string) --***[REQUIRED]**

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
        are:
        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.
        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.
    """


_RequiredClientStartBuildRegistryCredentialOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildRegistryCredentialOverrideTypeDef", {"credential": str}
)
_OptionalClientStartBuildRegistryCredentialOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildRegistryCredentialOverrideTypeDef",
    {"credentialProvider": str},
    total=False,
)


class ClientStartBuildRegistryCredentialOverrideTypeDef(
    _RequiredClientStartBuildRegistryCredentialOverrideTypeDef,
    _OptionalClientStartBuildRegistryCredentialOverrideTypeDef,
):
    """
    The credentials for access to a private registry.
    - **credential** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.
      .. note::

        The ``credential`` can use the name of the credentials only if they exist in your current
        region.
    """


_ClientStartBuildResponsebuildartifactsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildartifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStartBuildResponsebuildartifactsTypeDef(_ClientStartBuildResponsebuildartifactsTypeDef):
    pass


_ClientStartBuildResponsebuildcacheTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildcacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientStartBuildResponsebuildcacheTypeDef(_ClientStartBuildResponsebuildcacheTypeDef):
    pass


_ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef(
    _ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef
):
    pass


_ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef(
    _ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef
):
    pass


_ClientStartBuildResponsebuildenvironmentTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientStartBuildResponsebuildenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientStartBuildResponsebuildenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ClientStartBuildResponsebuildenvironmentTypeDef(
    _ClientStartBuildResponsebuildenvironmentTypeDef
):
    pass


_ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef(
    _ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef
):
    pass


_ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)


class ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef(
    _ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef
):
    pass


_ClientStartBuildResponsebuildlogss3LogsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildlogss3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientStartBuildResponsebuildlogss3LogsTypeDef(
    _ClientStartBuildResponsebuildlogss3LogsTypeDef
):
    pass


_ClientStartBuildResponsebuildlogsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildlogsTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogsArn": str,
        "s3LogsArn": str,
        "cloudWatchLogs": ClientStartBuildResponsebuildlogscloudWatchLogsTypeDef,
        "s3Logs": ClientStartBuildResponsebuildlogss3LogsTypeDef,
    },
    total=False,
)


class ClientStartBuildResponsebuildlogsTypeDef(_ClientStartBuildResponsebuildlogsTypeDef):
    pass


_ClientStartBuildResponsebuildnetworkInterfaceTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildnetworkInterfaceTypeDef",
    {"subnetId": str, "networkInterfaceId": str},
    total=False,
)


class ClientStartBuildResponsebuildnetworkInterfaceTypeDef(
    _ClientStartBuildResponsebuildnetworkInterfaceTypeDef
):
    pass


_ClientStartBuildResponsebuildphasescontextsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildphasescontextsTypeDef",
    {"statusCode": str, "message": str},
    total=False,
)


class ClientStartBuildResponsebuildphasescontextsTypeDef(
    _ClientStartBuildResponsebuildphasescontextsTypeDef
):
    pass


_ClientStartBuildResponsebuildphasesTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildphasesTypeDef",
    {
        "phaseType": Literal[
            "SUBMITTED",
            "QUEUED",
            "PROVISIONING",
            "DOWNLOAD_SOURCE",
            "INSTALL",
            "PRE_BUILD",
            "BUILD",
            "POST_BUILD",
            "UPLOAD_ARTIFACTS",
            "FINALIZING",
            "COMPLETED",
        ],
        "phaseStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[ClientStartBuildResponsebuildphasescontextsTypeDef],
    },
    total=False,
)


class ClientStartBuildResponsebuildphasesTypeDef(_ClientStartBuildResponsebuildphasesTypeDef):
    pass


_ClientStartBuildResponsebuildsecondaryArtifactsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsecondaryArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStartBuildResponsebuildsecondaryArtifactsTypeDef(
    _ClientStartBuildResponsebuildsecondaryArtifactsTypeDef
):
    pass


_ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef(
    _ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef
):
    pass


_ClientStartBuildResponsebuildsecondarySourcesauthTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientStartBuildResponsebuildsecondarySourcesauthTypeDef(
    _ClientStartBuildResponsebuildsecondarySourcesauthTypeDef
):
    pass


_ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef
):
    pass


_ClientStartBuildResponsebuildsecondarySourcesTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStartBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStartBuildResponsebuildsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStartBuildResponsebuildsecondarySourcesTypeDef(
    _ClientStartBuildResponsebuildsecondarySourcesTypeDef
):
    pass


_ClientStartBuildResponsebuildsourceauthTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsourceauthTypeDef", {"type": str, "resource": str}, total=False
)


class ClientStartBuildResponsebuildsourceauthTypeDef(
    _ClientStartBuildResponsebuildsourceauthTypeDef
):
    pass


_ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef(
    _ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef
):
    pass


_ClientStartBuildResponsebuildsourceTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildsourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStartBuildResponsebuildsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStartBuildResponsebuildsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStartBuildResponsebuildsourceTypeDef(_ClientStartBuildResponsebuildsourceTypeDef):
    pass


_ClientStartBuildResponsebuildvpcConfigTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientStartBuildResponsebuildvpcConfigTypeDef(_ClientStartBuildResponsebuildvpcConfigTypeDef):
    pass


_ClientStartBuildResponsebuildTypeDef = TypedDict(
    "_ClientStartBuildResponsebuildTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[ClientStartBuildResponsebuildphasesTypeDef],
        "source": ClientStartBuildResponsebuildsourceTypeDef,
        "secondarySources": List[ClientStartBuildResponsebuildsecondarySourcesTypeDef],
        "secondarySourceVersions": List[
            ClientStartBuildResponsebuildsecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientStartBuildResponsebuildartifactsTypeDef,
        "secondaryArtifacts": List[ClientStartBuildResponsebuildsecondaryArtifactsTypeDef],
        "cache": ClientStartBuildResponsebuildcacheTypeDef,
        "environment": ClientStartBuildResponsebuildenvironmentTypeDef,
        "serviceRole": str,
        "logs": ClientStartBuildResponsebuildlogsTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": ClientStartBuildResponsebuildvpcConfigTypeDef,
        "networkInterface": ClientStartBuildResponsebuildnetworkInterfaceTypeDef,
        "encryptionKey": str,
        "exportedEnvironmentVariables": List[
            ClientStartBuildResponsebuildexportedEnvironmentVariablesTypeDef
        ],
        "reportArns": List[str],
    },
    total=False,
)


class ClientStartBuildResponsebuildTypeDef(_ClientStartBuildResponsebuildTypeDef):
    """
    - **build** *(dict) --*

      Information about the build to be run.
      - **id** *(string) --*

        The unique ID for the build.
    """


_ClientStartBuildResponseTypeDef = TypedDict(
    "_ClientStartBuildResponseTypeDef", {"build": ClientStartBuildResponsebuildTypeDef}, total=False
)


class ClientStartBuildResponseTypeDef(_ClientStartBuildResponseTypeDef):
    """
    - *(dict) --*

      - **build** *(dict) --*

        Information about the build to be run.
        - **id** *(string) --*

          The unique ID for the build.
    """


_RequiredClientStartBuildSecondaryArtifactsOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildSecondaryArtifactsOverrideTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientStartBuildSecondaryArtifactsOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildSecondaryArtifactsOverrideTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStartBuildSecondaryArtifactsOverrideTypeDef(
    _RequiredClientStartBuildSecondaryArtifactsOverrideTypeDef,
    _OptionalClientStartBuildSecondaryArtifactsOverrideTypeDef,
):
    """
    - *(dict) --*

      Information about the build output artifacts for the build project.
      - **type** *(string) --***[REQUIRED]**

        The type of build output artifact. Valid values include:
        * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.
        .. note::

          The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .
    """


_ClientStartBuildSecondarySourcesOverrideauthTypeDef = TypedDict(
    "_ClientStartBuildSecondarySourcesOverrideauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientStartBuildSecondarySourcesOverrideauthTypeDef(
    _ClientStartBuildSecondarySourcesOverrideauthTypeDef
):
    pass


_ClientStartBuildSecondarySourcesOverridegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientStartBuildSecondarySourcesOverridegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientStartBuildSecondarySourcesOverridegitSubmodulesConfigTypeDef(
    _ClientStartBuildSecondarySourcesOverridegitSubmodulesConfigTypeDef
):
    pass


_RequiredClientStartBuildSecondarySourcesOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildSecondarySourcesOverrideTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalClientStartBuildSecondarySourcesOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildSecondarySourcesOverrideTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStartBuildSecondarySourcesOverridegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStartBuildSecondarySourcesOverrideauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStartBuildSecondarySourcesOverrideTypeDef(
    _RequiredClientStartBuildSecondarySourcesOverrideTypeDef,
    _OptionalClientStartBuildSecondarySourcesOverrideTypeDef,
):
    """
    - *(dict) --*

      Information about the build input source code for the build project.
      - **type** *(string) --***[REQUIRED]**

        The type of repository that contains the source code to be built. Valid values include:
        * ``BITBUCKET`` : The source code is in a Bitbucket repository.
        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.
        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
        pipeline in AWS CodePipeline.
        * ``GITHUB`` : The source code is in a GitHub repository.
        * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.
        * ``NO_SOURCE`` : The project does not have input source code.
        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    """


_RequiredClientStartBuildSecondarySourcesVersionOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildSecondarySourcesVersionOverrideTypeDef", {"sourceIdentifier": str}
)
_OptionalClientStartBuildSecondarySourcesVersionOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildSecondarySourcesVersionOverrideTypeDef",
    {"sourceVersion": str},
    total=False,
)


class ClientStartBuildSecondarySourcesVersionOverrideTypeDef(
    _RequiredClientStartBuildSecondarySourcesVersionOverrideTypeDef,
    _OptionalClientStartBuildSecondarySourcesVersionOverrideTypeDef,
):
    """
    - *(dict) --*

      A source identifier and its corresponding version.
      - **sourceIdentifier** *(string) --***[REQUIRED]**

        An identifier for a source in the build project.
    """


_RequiredClientStartBuildSourceAuthOverrideTypeDef = TypedDict(
    "_RequiredClientStartBuildSourceAuthOverrideTypeDef", {"type": str}
)
_OptionalClientStartBuildSourceAuthOverrideTypeDef = TypedDict(
    "_OptionalClientStartBuildSourceAuthOverrideTypeDef", {"resource": str}, total=False
)


class ClientStartBuildSourceAuthOverrideTypeDef(
    _RequiredClientStartBuildSourceAuthOverrideTypeDef,
    _OptionalClientStartBuildSourceAuthOverrideTypeDef,
):
    """
    An authorization type for this build that overrides the one defined in the build project. This
    override applies only if the build project's source is BitBucket or GitHub.
    - **type** *(string) --***[REQUIRED]**

      .. note::

        This data type is deprecated and is no longer accurate or used.
    """


_ClientStopBuildResponsebuildartifactsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildartifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStopBuildResponsebuildartifactsTypeDef(_ClientStopBuildResponsebuildartifactsTypeDef):
    pass


_ClientStopBuildResponsebuildcacheTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildcacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientStopBuildResponsebuildcacheTypeDef(_ClientStopBuildResponsebuildcacheTypeDef):
    pass


_ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef(
    _ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef
):
    pass


_ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef(
    _ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef
):
    pass


_ClientStopBuildResponsebuildenvironmentTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientStopBuildResponsebuildenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientStopBuildResponsebuildenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ClientStopBuildResponsebuildenvironmentTypeDef(
    _ClientStopBuildResponsebuildenvironmentTypeDef
):
    pass


_ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef(
    _ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef
):
    pass


_ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)


class ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef(
    _ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef
):
    pass


_ClientStopBuildResponsebuildlogss3LogsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildlogss3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientStopBuildResponsebuildlogss3LogsTypeDef(_ClientStopBuildResponsebuildlogss3LogsTypeDef):
    pass


_ClientStopBuildResponsebuildlogsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildlogsTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogsArn": str,
        "s3LogsArn": str,
        "cloudWatchLogs": ClientStopBuildResponsebuildlogscloudWatchLogsTypeDef,
        "s3Logs": ClientStopBuildResponsebuildlogss3LogsTypeDef,
    },
    total=False,
)


class ClientStopBuildResponsebuildlogsTypeDef(_ClientStopBuildResponsebuildlogsTypeDef):
    pass


_ClientStopBuildResponsebuildnetworkInterfaceTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildnetworkInterfaceTypeDef",
    {"subnetId": str, "networkInterfaceId": str},
    total=False,
)


class ClientStopBuildResponsebuildnetworkInterfaceTypeDef(
    _ClientStopBuildResponsebuildnetworkInterfaceTypeDef
):
    pass


_ClientStopBuildResponsebuildphasescontextsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildphasescontextsTypeDef",
    {"statusCode": str, "message": str},
    total=False,
)


class ClientStopBuildResponsebuildphasescontextsTypeDef(
    _ClientStopBuildResponsebuildphasescontextsTypeDef
):
    pass


_ClientStopBuildResponsebuildphasesTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildphasesTypeDef",
    {
        "phaseType": Literal[
            "SUBMITTED",
            "QUEUED",
            "PROVISIONING",
            "DOWNLOAD_SOURCE",
            "INSTALL",
            "PRE_BUILD",
            "BUILD",
            "POST_BUILD",
            "UPLOAD_ARTIFACTS",
            "FINALIZING",
            "COMPLETED",
        ],
        "phaseStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List[ClientStopBuildResponsebuildphasescontextsTypeDef],
    },
    total=False,
)


class ClientStopBuildResponsebuildphasesTypeDef(_ClientStopBuildResponsebuildphasesTypeDef):
    pass


_ClientStopBuildResponsebuildsecondaryArtifactsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsecondaryArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientStopBuildResponsebuildsecondaryArtifactsTypeDef(
    _ClientStopBuildResponsebuildsecondaryArtifactsTypeDef
):
    pass


_ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef(
    _ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef
):
    pass


_ClientStopBuildResponsebuildsecondarySourcesauthTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientStopBuildResponsebuildsecondarySourcesauthTypeDef(
    _ClientStopBuildResponsebuildsecondarySourcesauthTypeDef
):
    pass


_ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef
):
    pass


_ClientStopBuildResponsebuildsecondarySourcesTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStopBuildResponsebuildsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStopBuildResponsebuildsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStopBuildResponsebuildsecondarySourcesTypeDef(
    _ClientStopBuildResponsebuildsecondarySourcesTypeDef
):
    pass


_ClientStopBuildResponsebuildsourceauthTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsourceauthTypeDef", {"type": str, "resource": str}, total=False
)


class ClientStopBuildResponsebuildsourceauthTypeDef(_ClientStopBuildResponsebuildsourceauthTypeDef):
    pass


_ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef(
    _ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef
):
    pass


_ClientStopBuildResponsebuildsourceTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildsourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientStopBuildResponsebuildsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientStopBuildResponsebuildsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientStopBuildResponsebuildsourceTypeDef(_ClientStopBuildResponsebuildsourceTypeDef):
    pass


_ClientStopBuildResponsebuildvpcConfigTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientStopBuildResponsebuildvpcConfigTypeDef(_ClientStopBuildResponsebuildvpcConfigTypeDef):
    pass


_ClientStopBuildResponsebuildTypeDef = TypedDict(
    "_ClientStopBuildResponsebuildTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": Literal[
            "SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED"
        ],
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List[ClientStopBuildResponsebuildphasesTypeDef],
        "source": ClientStopBuildResponsebuildsourceTypeDef,
        "secondarySources": List[ClientStopBuildResponsebuildsecondarySourcesTypeDef],
        "secondarySourceVersions": List[ClientStopBuildResponsebuildsecondarySourceVersionsTypeDef],
        "artifacts": ClientStopBuildResponsebuildartifactsTypeDef,
        "secondaryArtifacts": List[ClientStopBuildResponsebuildsecondaryArtifactsTypeDef],
        "cache": ClientStopBuildResponsebuildcacheTypeDef,
        "environment": ClientStopBuildResponsebuildenvironmentTypeDef,
        "serviceRole": str,
        "logs": ClientStopBuildResponsebuildlogsTypeDef,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": ClientStopBuildResponsebuildvpcConfigTypeDef,
        "networkInterface": ClientStopBuildResponsebuildnetworkInterfaceTypeDef,
        "encryptionKey": str,
        "exportedEnvironmentVariables": List[
            ClientStopBuildResponsebuildexportedEnvironmentVariablesTypeDef
        ],
        "reportArns": List[str],
    },
    total=False,
)


class ClientStopBuildResponsebuildTypeDef(_ClientStopBuildResponsebuildTypeDef):
    """
    - **build** *(dict) --*

      Information about the build.
      - **id** *(string) --*

        The unique ID for the build.
    """


_ClientStopBuildResponseTypeDef = TypedDict(
    "_ClientStopBuildResponseTypeDef", {"build": ClientStopBuildResponsebuildTypeDef}, total=False
)


class ClientStopBuildResponseTypeDef(_ClientStopBuildResponseTypeDef):
    """
    - *(dict) --*

      - **build** *(dict) --*

        Information about the build.
        - **id** *(string) --*

          The unique ID for the build.
    """


_RequiredClientUpdateProjectArtifactsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectArtifactsTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientUpdateProjectArtifactsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectArtifactsTypeDef(
    _RequiredClientUpdateProjectArtifactsTypeDef, _OptionalClientUpdateProjectArtifactsTypeDef
):
    """
    Information to be changed about the build output artifacts for the build project.
    - **type** *(string) --***[REQUIRED]**

      The type of build output artifact. Valid values include:
      * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.
      .. note::

        The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .
    """


_RequiredClientUpdateProjectCacheTypeDef = TypedDict(
    "_RequiredClientUpdateProjectCacheTypeDef", {"type": Literal["NO_CACHE", "S3", "LOCAL"]}
)
_OptionalClientUpdateProjectCacheTypeDef = TypedDict(
    "_OptionalClientUpdateProjectCacheTypeDef",
    {
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientUpdateProjectCacheTypeDef(
    _RequiredClientUpdateProjectCacheTypeDef, _OptionalClientUpdateProjectCacheTypeDef
):
    """
    Stores recently used information so that it can be quickly accessed at a later time.
    - **type** *(string) --***[REQUIRED]**

      The type of cache used by the build project. Valid values include:
      * ``NO_CACHE`` : The build project does not use any cache.
      * ``S3`` : The build project reads and writes from and to S3.
      * ``LOCAL`` : The build project stores a cache locally on a build host that is only available
      to that build host.
    """


_ClientUpdateProjectEnvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientUpdateProjectEnvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class ClientUpdateProjectEnvironmentenvironmentVariablesTypeDef(
    _ClientUpdateProjectEnvironmentenvironmentVariablesTypeDef
):
    pass


_ClientUpdateProjectEnvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientUpdateProjectEnvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientUpdateProjectEnvironmentregistryCredentialTypeDef(
    _ClientUpdateProjectEnvironmentregistryCredentialTypeDef
):
    pass


_RequiredClientUpdateProjectEnvironmentTypeDef = TypedDict(
    "_RequiredClientUpdateProjectEnvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ]
    },
)
_OptionalClientUpdateProjectEnvironmentTypeDef = TypedDict(
    "_OptionalClientUpdateProjectEnvironmentTypeDef",
    {
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[ClientUpdateProjectEnvironmentenvironmentVariablesTypeDef],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientUpdateProjectEnvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ClientUpdateProjectEnvironmentTypeDef(
    _RequiredClientUpdateProjectEnvironmentTypeDef, _OptionalClientUpdateProjectEnvironmentTypeDef
):
    """
    Information to be changed about the build environment for the build project.
    - **type** *(string) --***[REQUIRED]**

      The type of build environment to use for related builds.
      * The environment type ``ARM_CONTAINER`` is available only in regions US East (N. Virginia),
      US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo),
      Asia Pacific (Sydney), and EU (Frankfurt).
      * The environment type ``LINUX_CONTAINER`` with compute type ``build.general1.2xlarge`` is
      available only in regions US East (N. Virginia), US East (N. Virginia), US West (Oregon),
      Canada (Central), EU (Ireland), EU (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia
      Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), China (Beijing), and China
      (Ningxia).
      * The environment type ``LINUX_GPU_CONTAINER`` is available only in regions US East (N.
      Virginia), US East (N. Virginia), US West (Oregon), Canada (Central), EU (Ireland), EU
      (London), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific
      (Singapore), Asia Pacific (Sydney) , China (Beijing), and China (Ningxia).
    """


_RequiredClientUpdateProjectLogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectLogsConfigcloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"]},
)
_OptionalClientUpdateProjectLogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectLogsConfigcloudWatchLogsTypeDef",
    {"groupName": str, "streamName": str},
    total=False,
)


class ClientUpdateProjectLogsConfigcloudWatchLogsTypeDef(
    _RequiredClientUpdateProjectLogsConfigcloudWatchLogsTypeDef,
    _OptionalClientUpdateProjectLogsConfigcloudWatchLogsTypeDef,
):
    """
    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.
      - **status** *(string) --***[REQUIRED]**

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
        are:
        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.
        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.
    """


_ClientUpdateProjectLogsConfigs3LogsTypeDef = TypedDict(
    "_ClientUpdateProjectLogsConfigs3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientUpdateProjectLogsConfigs3LogsTypeDef(_ClientUpdateProjectLogsConfigs3LogsTypeDef):
    pass


_ClientUpdateProjectLogsConfigTypeDef = TypedDict(
    "_ClientUpdateProjectLogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientUpdateProjectLogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientUpdateProjectLogsConfigs3LogsTypeDef,
    },
    total=False,
)


class ClientUpdateProjectLogsConfigTypeDef(_ClientUpdateProjectLogsConfigTypeDef):
    """
    Information about logs for the build project. A project can create logs in Amazon CloudWatch
    Logs, logs in an S3 bucket, or both.
    - **cloudWatchLogs** *(dict) --*

      Information about Amazon CloudWatch Logs for a build project. Amazon CloudWatch Logs are
      enabled by default.
      - **status** *(string) --***[REQUIRED]**

        The current status of the logs in Amazon CloudWatch Logs for a build project. Valid values
        are:
        * ``ENABLED`` : Amazon CloudWatch Logs are enabled for this build project.
        * ``DISABLED`` : Amazon CloudWatch Logs are not enabled for this build project.
    """


_ClientUpdateProjectResponseprojectartifactsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectartifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectartifactsTypeDef(
    _ClientUpdateProjectResponseprojectartifactsTypeDef
):
    pass


_ClientUpdateProjectResponseprojectbadgeTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectbadgeTypeDef",
    {"badgeEnabled": bool, "badgeRequestUrl": str},
    total=False,
)


class ClientUpdateProjectResponseprojectbadgeTypeDef(
    _ClientUpdateProjectResponseprojectbadgeTypeDef
):
    pass


_ClientUpdateProjectResponseprojectcacheTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectcacheTypeDef",
    {
        "type": Literal["NO_CACHE", "S3", "LOCAL"],
        "location": str,
        "modes": List[
            Literal["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE", "LOCAL_CUSTOM_CACHE"]
        ],
    },
    total=False,
)


class ClientUpdateProjectResponseprojectcacheTypeDef(
    _ClientUpdateProjectResponseprojectcacheTypeDef
):
    pass


_ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef",
    {"name": str, "value": str, "type": Literal["PLAINTEXT", "PARAMETER_STORE", "SECRETS_MANAGER"]},
    total=False,
)


class ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef(
    _ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef
):
    pass


_ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef",
    {"credential": str, "credentialProvider": str},
    total=False,
)


class ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef(
    _ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef
):
    pass


_ClientUpdateProjectResponseprojectenvironmentTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectenvironmentTypeDef",
    {
        "type": Literal[
            "WINDOWS_CONTAINER", "LINUX_CONTAINER", "LINUX_GPU_CONTAINER", "ARM_CONTAINER"
        ],
        "image": str,
        "computeType": Literal[
            "BUILD_GENERAL1_SMALL",
            "BUILD_GENERAL1_MEDIUM",
            "BUILD_GENERAL1_LARGE",
            "BUILD_GENERAL1_2XLARGE",
        ],
        "environmentVariables": List[
            ClientUpdateProjectResponseprojectenvironmentenvironmentVariablesTypeDef
        ],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": ClientUpdateProjectResponseprojectenvironmentregistryCredentialTypeDef,
        "imagePullCredentialsType": Literal["CODEBUILD", "SERVICE_ROLE"],
    },
    total=False,
)


class ClientUpdateProjectResponseprojectenvironmentTypeDef(
    _ClientUpdateProjectResponseprojectenvironmentTypeDef
):
    pass


_ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "groupName": str, "streamName": str},
    total=False,
)


class ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef(
    _ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef
):
    pass


_ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef",
    {"status": Literal["ENABLED", "DISABLED"], "location": str, "encryptionDisabled": bool},
    total=False,
)


class ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef(
    _ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef
):
    pass


_ClientUpdateProjectResponseprojectlogsConfigTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectlogsConfigTypeDef",
    {
        "cloudWatchLogs": ClientUpdateProjectResponseprojectlogsConfigcloudWatchLogsTypeDef,
        "s3Logs": ClientUpdateProjectResponseprojectlogsConfigs3LogsTypeDef,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectlogsConfigTypeDef(
    _ClientUpdateProjectResponseprojectlogsConfigTypeDef
):
    pass


_ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef",
    {
        "type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"],
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef(
    _ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef
):
    pass


_ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef",
    {"sourceIdentifier": str, "sourceVersion": str},
    total=False,
)


class ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef(
    _ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef
):
    pass


_ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef(
    _ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef
):
    pass


_ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef
):
    pass


_ClientUpdateProjectResponseprojectsecondarySourcesTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectResponseprojectsecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectResponseprojectsecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectsecondarySourcesTypeDef(
    _ClientUpdateProjectResponseprojectsecondarySourcesTypeDef
):
    pass


_ClientUpdateProjectResponseprojectsourceauthTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsourceauthTypeDef",
    {"type": str, "resource": str},
    total=False,
)


class ClientUpdateProjectResponseprojectsourceauthTypeDef(
    _ClientUpdateProjectResponseprojectsourceauthTypeDef
):
    pass


_ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef(
    _ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef
):
    pass


_ClientUpdateProjectResponseprojectsourceTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectsourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ],
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectResponseprojectsourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectResponseprojectsourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectsourceTypeDef(
    _ClientUpdateProjectResponseprojectsourceTypeDef
):
    pass


_ClientUpdateProjectResponseprojecttagsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojecttagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateProjectResponseprojecttagsTypeDef(_ClientUpdateProjectResponseprojecttagsTypeDef):
    pass


_ClientUpdateProjectResponseprojectvpcConfigTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectvpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientUpdateProjectResponseprojectvpcConfigTypeDef(
    _ClientUpdateProjectResponseprojectvpcConfigTypeDef
):
    pass


_ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef",
    {
        "type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"],
        "pattern": str,
        "excludeMatchedPattern": bool,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef(
    _ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef
):
    pass


_ClientUpdateProjectResponseprojectwebhookTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectwebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List[ClientUpdateProjectResponseprojectwebhookfilterGroupsTypeDef]],
        "lastModifiedSecret": datetime,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectwebhookTypeDef(
    _ClientUpdateProjectResponseprojectwebhookTypeDef
):
    pass


_ClientUpdateProjectResponseprojectTypeDef = TypedDict(
    "_ClientUpdateProjectResponseprojectTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": ClientUpdateProjectResponseprojectsourceTypeDef,
        "secondarySources": List[ClientUpdateProjectResponseprojectsecondarySourcesTypeDef],
        "sourceVersion": str,
        "secondarySourceVersions": List[
            ClientUpdateProjectResponseprojectsecondarySourceVersionsTypeDef
        ],
        "artifacts": ClientUpdateProjectResponseprojectartifactsTypeDef,
        "secondaryArtifacts": List[ClientUpdateProjectResponseprojectsecondaryArtifactsTypeDef],
        "cache": ClientUpdateProjectResponseprojectcacheTypeDef,
        "environment": ClientUpdateProjectResponseprojectenvironmentTypeDef,
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List[ClientUpdateProjectResponseprojecttagsTypeDef],
        "created": datetime,
        "lastModified": datetime,
        "webhook": ClientUpdateProjectResponseprojectwebhookTypeDef,
        "vpcConfig": ClientUpdateProjectResponseprojectvpcConfigTypeDef,
        "badge": ClientUpdateProjectResponseprojectbadgeTypeDef,
        "logsConfig": ClientUpdateProjectResponseprojectlogsConfigTypeDef,
    },
    total=False,
)


class ClientUpdateProjectResponseprojectTypeDef(_ClientUpdateProjectResponseprojectTypeDef):
    """
    - **project** *(dict) --*

      Information about the build project that was changed.
      - **name** *(string) --*

        The name of the build project.
    """


_ClientUpdateProjectResponseTypeDef = TypedDict(
    "_ClientUpdateProjectResponseTypeDef",
    {"project": ClientUpdateProjectResponseprojectTypeDef},
    total=False,
)


class ClientUpdateProjectResponseTypeDef(_ClientUpdateProjectResponseTypeDef):
    """
    - *(dict) --*

      - **project** *(dict) --*

        Information about the build project that was changed.
        - **name** *(string) --*

          The name of the build project.
    """


_RequiredClientUpdateProjectSecondaryArtifactsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectSecondaryArtifactsTypeDef",
    {"type": Literal["CODEPIPELINE", "S3", "NO_ARTIFACTS"]},
)
_OptionalClientUpdateProjectSecondaryArtifactsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectSecondaryArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": Literal["NONE", "BUILD_ID"],
        "name": str,
        "packaging": Literal["NONE", "ZIP"],
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectSecondaryArtifactsTypeDef(
    _RequiredClientUpdateProjectSecondaryArtifactsTypeDef,
    _OptionalClientUpdateProjectSecondaryArtifactsTypeDef,
):
    """
    - *(dict) --*

      Information about the build output artifacts for the build project.
      - **type** *(string) --***[REQUIRED]**

        The type of build output artifact. Valid values include:
        * ``CODEPIPELINE`` : The build project has build output generated through AWS CodePipeline.
        .. note::

          The ``CODEPIPELINE`` type is not supported for ``secondaryArtifacts`` .
    """


_RequiredClientUpdateProjectSecondarySourceVersionsTypeDef = TypedDict(
    "_RequiredClientUpdateProjectSecondarySourceVersionsTypeDef", {"sourceIdentifier": str}
)
_OptionalClientUpdateProjectSecondarySourceVersionsTypeDef = TypedDict(
    "_OptionalClientUpdateProjectSecondarySourceVersionsTypeDef",
    {"sourceVersion": str},
    total=False,
)


class ClientUpdateProjectSecondarySourceVersionsTypeDef(
    _RequiredClientUpdateProjectSecondarySourceVersionsTypeDef,
    _OptionalClientUpdateProjectSecondarySourceVersionsTypeDef,
):
    """
    - *(dict) --*

      A source identifier and its corresponding version.
      - **sourceIdentifier** *(string) --***[REQUIRED]**

        An identifier for a source in the build project.
    """


_ClientUpdateProjectSecondarySourcesauthTypeDef = TypedDict(
    "_ClientUpdateProjectSecondarySourcesauthTypeDef", {"type": str, "resource": str}, total=False
)


class ClientUpdateProjectSecondarySourcesauthTypeDef(
    _ClientUpdateProjectSecondarySourcesauthTypeDef
):
    pass


_ClientUpdateProjectSecondarySourcesgitSubmodulesConfigTypeDef = TypedDict(
    "_ClientUpdateProjectSecondarySourcesgitSubmodulesConfigTypeDef",
    {"fetchSubmodules": bool},
    total=False,
)


class ClientUpdateProjectSecondarySourcesgitSubmodulesConfigTypeDef(
    _ClientUpdateProjectSecondarySourcesgitSubmodulesConfigTypeDef
):
    pass


_RequiredClientUpdateProjectSecondarySourcesTypeDef = TypedDict(
    "_RequiredClientUpdateProjectSecondarySourcesTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalClientUpdateProjectSecondarySourcesTypeDef = TypedDict(
    "_OptionalClientUpdateProjectSecondarySourcesTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectSecondarySourcesgitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectSecondarySourcesauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectSecondarySourcesTypeDef(
    _RequiredClientUpdateProjectSecondarySourcesTypeDef,
    _OptionalClientUpdateProjectSecondarySourcesTypeDef,
):
    """
    - *(dict) --*

      Information about the build input source code for the build project.
      - **type** *(string) --***[REQUIRED]**

        The type of repository that contains the source code to be built. Valid values include:
        * ``BITBUCKET`` : The source code is in a Bitbucket repository.
        * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.
        * ``CODEPIPELINE`` : The source code settings are specified in the source action of a
        pipeline in AWS CodePipeline.
        * ``GITHUB`` : The source code is in a GitHub repository.
        * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.
        * ``NO_SOURCE`` : The project does not have input source code.
        * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    """


_ClientUpdateProjectSourceauthTypeDef = TypedDict(
    "_ClientUpdateProjectSourceauthTypeDef", {"type": str, "resource": str}, total=False
)


class ClientUpdateProjectSourceauthTypeDef(_ClientUpdateProjectSourceauthTypeDef):
    pass


_ClientUpdateProjectSourcegitSubmodulesConfigTypeDef = TypedDict(
    "_ClientUpdateProjectSourcegitSubmodulesConfigTypeDef", {"fetchSubmodules": bool}, total=False
)


class ClientUpdateProjectSourcegitSubmodulesConfigTypeDef(
    _ClientUpdateProjectSourcegitSubmodulesConfigTypeDef
):
    pass


_RequiredClientUpdateProjectSourceTypeDef = TypedDict(
    "_RequiredClientUpdateProjectSourceTypeDef",
    {
        "type": Literal[
            "CODECOMMIT",
            "CODEPIPELINE",
            "GITHUB",
            "S3",
            "BITBUCKET",
            "GITHUB_ENTERPRISE",
            "NO_SOURCE",
        ]
    },
)
_OptionalClientUpdateProjectSourceTypeDef = TypedDict(
    "_OptionalClientUpdateProjectSourceTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": ClientUpdateProjectSourcegitSubmodulesConfigTypeDef,
        "buildspec": str,
        "auth": ClientUpdateProjectSourceauthTypeDef,
        "reportBuildStatus": bool,
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ClientUpdateProjectSourceTypeDef(
    _RequiredClientUpdateProjectSourceTypeDef, _OptionalClientUpdateProjectSourceTypeDef
):
    """
    Information to be changed about the build input source code for the build project.
    - **type** *(string) --***[REQUIRED]**

      The type of repository that contains the source code to be built. Valid values include:
      * ``BITBUCKET`` : The source code is in a Bitbucket repository.
      * ``CODECOMMIT`` : The source code is in an AWS CodeCommit repository.
      * ``CODEPIPELINE`` : The source code settings are specified in the source action of a pipeline
      in AWS CodePipeline.
      * ``GITHUB`` : The source code is in a GitHub repository.
      * ``GITHUB_ENTERPRISE`` : The source code is in a GitHub Enterprise repository.
      * ``NO_SOURCE`` : The project does not have input source code.
      * ``S3`` : The source code is in an Amazon Simple Storage Service (Amazon S3) input bucket.
    """


_ClientUpdateProjectTagsTypeDef = TypedDict(
    "_ClientUpdateProjectTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateProjectTagsTypeDef(_ClientUpdateProjectTagsTypeDef):
    """
    - *(dict) --*

      A tag, consisting of a key and a value.
      This tag is available for use by AWS services that support tags in AWS CodeBuild.
      - **key** *(string) --*

        The tag's key.
    """


_ClientUpdateProjectVpcConfigTypeDef = TypedDict(
    "_ClientUpdateProjectVpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)


class ClientUpdateProjectVpcConfigTypeDef(_ClientUpdateProjectVpcConfigTypeDef):
    """
    VpcConfig enables AWS CodeBuild to access resources in an Amazon VPC.
    - **vpcId** *(string) --*

      The ID of the Amazon VPC.
    """


_ClientUpdateReportGroupExportConfigs3DestinationTypeDef = TypedDict(
    "_ClientUpdateReportGroupExportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)


class ClientUpdateReportGroupExportConfigs3DestinationTypeDef(
    _ClientUpdateReportGroupExportConfigs3DestinationTypeDef
):
    pass


_ClientUpdateReportGroupExportConfigTypeDef = TypedDict(
    "_ClientUpdateReportGroupExportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientUpdateReportGroupExportConfigs3DestinationTypeDef,
    },
    total=False,
)


class ClientUpdateReportGroupExportConfigTypeDef(_ClientUpdateReportGroupExportConfigTypeDef):
    """
    Used to specify an updated export type. Valid values are:
    * ``S3`` : The report results are exported to an S3 bucket.
    * ``NO_EXPORT`` : The report results are not exported.
    - **exportConfigType** *(string) --*

      The export configuration type. Valid values are:
      * ``S3`` : The report results are exported to an S3 bucket.
      * ``NO_EXPORT`` : The report results are not exported.
    """


_ClientUpdateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef = TypedDict(
    "_ClientUpdateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef",
    {
        "bucket": str,
        "path": str,
        "packaging": Literal["ZIP", "NONE"],
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)


class ClientUpdateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef(
    _ClientUpdateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef
):
    pass


_ClientUpdateReportGroupResponsereportGroupexportConfigTypeDef = TypedDict(
    "_ClientUpdateReportGroupResponsereportGroupexportConfigTypeDef",
    {
        "exportConfigType": Literal["S3", "NO_EXPORT"],
        "s3Destination": ClientUpdateReportGroupResponsereportGroupexportConfigs3DestinationTypeDef,
    },
    total=False,
)


class ClientUpdateReportGroupResponsereportGroupexportConfigTypeDef(
    _ClientUpdateReportGroupResponsereportGroupexportConfigTypeDef
):
    pass


_ClientUpdateReportGroupResponsereportGroupTypeDef = TypedDict(
    "_ClientUpdateReportGroupResponsereportGroupTypeDef",
    {
        "arn": str,
        "name": str,
        "type": str,
        "exportConfig": ClientUpdateReportGroupResponsereportGroupexportConfigTypeDef,
        "created": datetime,
        "lastModified": datetime,
    },
    total=False,
)


class ClientUpdateReportGroupResponsereportGroupTypeDef(
    _ClientUpdateReportGroupResponsereportGroupTypeDef
):
    """
    - **reportGroup** *(dict) --*

      Information about the updated report group.
      - **arn** *(string) --*

        The ARN of a ``ReportGroup`` .
    """


_ClientUpdateReportGroupResponseTypeDef = TypedDict(
    "_ClientUpdateReportGroupResponseTypeDef",
    {"reportGroup": ClientUpdateReportGroupResponsereportGroupTypeDef},
    total=False,
)


class ClientUpdateReportGroupResponseTypeDef(_ClientUpdateReportGroupResponseTypeDef):
    """
    - *(dict) --*

      - **reportGroup** *(dict) --*

        Information about the updated report group.
        - **arn** *(string) --*

          The ARN of a ``ReportGroup`` .
    """


_RequiredClientUpdateWebhookFilterGroupsTypeDef = TypedDict(
    "_RequiredClientUpdateWebhookFilterGroupsTypeDef",
    {"type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"]},
)
_OptionalClientUpdateWebhookFilterGroupsTypeDef = TypedDict(
    "_OptionalClientUpdateWebhookFilterGroupsTypeDef",
    {"pattern": str, "excludeMatchedPattern": bool},
    total=False,
)


class ClientUpdateWebhookFilterGroupsTypeDef(
    _RequiredClientUpdateWebhookFilterGroupsTypeDef, _OptionalClientUpdateWebhookFilterGroupsTypeDef
):
    """
    - *(dict) --*

      A filter used to determine which webhooks trigger a build.
      - **type** *(string) --***[REQUIRED]**

        The type of webhook filter. There are five webhook filter types: ``EVENT`` ,
        ``ACTOR_ACCOUNT_ID`` , ``HEAD_REF`` , ``BASE_REF`` , and ``FILE_PATH`` .

          EVENT
    """


_ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef = TypedDict(
    "_ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef",
    {
        "type": Literal["EVENT", "BASE_REF", "HEAD_REF", "ACTOR_ACCOUNT_ID", "FILE_PATH"],
        "pattern": str,
        "excludeMatchedPattern": bool,
    },
    total=False,
)


class ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef(
    _ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef
):
    pass


_ClientUpdateWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientUpdateWebhookResponsewebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List[ClientUpdateWebhookResponsewebhookfilterGroupsTypeDef]],
        "lastModifiedSecret": datetime,
    },
    total=False,
)


class ClientUpdateWebhookResponsewebhookTypeDef(_ClientUpdateWebhookResponsewebhookTypeDef):
    """
    - **webhook** *(dict) --*

      Information about a repository's webhook that is associated with a project in AWS CodeBuild.
      - **url** *(string) --*

        The URL to the webhook.
    """


_ClientUpdateWebhookResponseTypeDef = TypedDict(
    "_ClientUpdateWebhookResponseTypeDef",
    {"webhook": ClientUpdateWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientUpdateWebhookResponseTypeDef(_ClientUpdateWebhookResponseTypeDef):
    """
    - *(dict) --*

      - **webhook** *(dict) --*

        Information about a repository's webhook that is associated with a project in AWS CodeBuild.
        - **url** *(string) --*

          The URL to the webhook.
    """


_ListBuildsForProjectPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBuildsForProjectPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListBuildsForProjectPaginatePaginationConfigTypeDef(
    _ListBuildsForProjectPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBuildsForProjectPaginateResponseTypeDef = TypedDict(
    "_ListBuildsForProjectPaginateResponseTypeDef",
    {"ids": List[str], "NextToken": str},
    total=False,
)


class ListBuildsForProjectPaginateResponseTypeDef(_ListBuildsForProjectPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ids** *(list) --*

        A list of build IDs for the specified build project, with each build ID representing a
        single build.
        - *(string) --*
    """


_ListBuildsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBuildsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListBuildsPaginatePaginationConfigTypeDef(_ListBuildsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBuildsPaginateResponseTypeDef = TypedDict(
    "_ListBuildsPaginateResponseTypeDef", {"ids": List[str], "NextToken": str}, total=False
)


class ListBuildsPaginateResponseTypeDef(_ListBuildsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ids** *(list) --*

        A list of build IDs, with each build ID representing a single build.
        - *(string) --*
    """


_ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListProjectsPaginatePaginationConfigTypeDef(_ListProjectsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListProjectsPaginateResponseTypeDef = TypedDict(
    "_ListProjectsPaginateResponseTypeDef", {"projects": List[str], "NextToken": str}, total=False
)


class ListProjectsPaginateResponseTypeDef(_ListProjectsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **projects** *(list) --*

        The list of build project names, with each build project name representing a single build
        project.
        - *(string) --*
    """
