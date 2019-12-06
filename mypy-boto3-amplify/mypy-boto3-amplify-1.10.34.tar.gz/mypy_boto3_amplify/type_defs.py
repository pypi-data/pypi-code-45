"Main interface for amplify service type defs"
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


ClientCreateAppAutoBranchCreationConfigTypeDef = TypedDict(
    "ClientCreateAppAutoBranchCreationConfigTypeDef",
    {
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)

_RequiredClientCreateAppCustomRulesTypeDef = TypedDict(
    "_RequiredClientCreateAppCustomRulesTypeDef", {"source": str}
)
_OptionalClientCreateAppCustomRulesTypeDef = TypedDict(
    "_OptionalClientCreateAppCustomRulesTypeDef",
    {"target": str, "status": str, "condition": str},
    total=False,
)


class ClientCreateAppCustomRulesTypeDef(
    _RequiredClientCreateAppCustomRulesTypeDef, _OptionalClientCreateAppCustomRulesTypeDef
):
    pass


ClientCreateAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "ClientCreateAppResponseappautoBranchCreationConfigTypeDef",
    {
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)

ClientCreateAppResponseappcustomRulesTypeDef = TypedDict(
    "ClientCreateAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)

ClientCreateAppResponseappproductionBranchTypeDef = TypedDict(
    "ClientCreateAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)

ClientCreateAppResponseappTypeDef = TypedDict(
    "ClientCreateAppResponseappTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ClientCreateAppResponseappcustomRulesTypeDef],
        "productionBranch": ClientCreateAppResponseappproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ClientCreateAppResponseappautoBranchCreationConfigTypeDef,
    },
    total=False,
)

ClientCreateAppResponseTypeDef = TypedDict(
    "ClientCreateAppResponseTypeDef", {"app": ClientCreateAppResponseappTypeDef}, total=False
)

ClientCreateBackendEnvironmentResponsebackendEnvironmentTypeDef = TypedDict(
    "ClientCreateBackendEnvironmentResponsebackendEnvironmentTypeDef",
    {
        "backendEnvironmentArn": str,
        "environmentName": str,
        "stackName": str,
        "deploymentArtifacts": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)

ClientCreateBackendEnvironmentResponseTypeDef = TypedDict(
    "ClientCreateBackendEnvironmentResponseTypeDef",
    {"backendEnvironment": ClientCreateBackendEnvironmentResponsebackendEnvironmentTypeDef},
    total=False,
)

ClientCreateBranchResponsebranchTypeDef = TypedDict(
    "ClientCreateBranchResponsebranchTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)

ClientCreateBranchResponseTypeDef = TypedDict(
    "ClientCreateBranchResponseTypeDef",
    {"branch": ClientCreateBranchResponsebranchTypeDef},
    total=False,
)

ClientCreateDeploymentResponseTypeDef = TypedDict(
    "ClientCreateDeploymentResponseTypeDef",
    {"jobId": str, "fileUploadUrls": Dict[str, str], "zipUploadUrl": str},
    total=False,
)

ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)

ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)

ClientCreateDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "ClientCreateDomainAssociationResponsedomainAssociationTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": Literal[
            "PENDING_VERIFICATION",
            "IN_PROGRESS",
            "AVAILABLE",
            "PENDING_DEPLOYMENT",
            "FAILED",
            "CREATING",
            "REQUESTING_CERTIFICATE",
            "UPDATING",
        ],
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef],
    },
    total=False,
)

ClientCreateDomainAssociationResponseTypeDef = TypedDict(
    "ClientCreateDomainAssociationResponseTypeDef",
    {"domainAssociation": ClientCreateDomainAssociationResponsedomainAssociationTypeDef},
    total=False,
)

_RequiredClientCreateDomainAssociationSubDomainSettingsTypeDef = TypedDict(
    "_RequiredClientCreateDomainAssociationSubDomainSettingsTypeDef", {"prefix": str}
)
_OptionalClientCreateDomainAssociationSubDomainSettingsTypeDef = TypedDict(
    "_OptionalClientCreateDomainAssociationSubDomainSettingsTypeDef",
    {"branchName": str},
    total=False,
)


class ClientCreateDomainAssociationSubDomainSettingsTypeDef(
    _RequiredClientCreateDomainAssociationSubDomainSettingsTypeDef,
    _OptionalClientCreateDomainAssociationSubDomainSettingsTypeDef,
):
    pass


ClientCreateWebhookResponsewebhookTypeDef = TypedDict(
    "ClientCreateWebhookResponsewebhookTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)

ClientCreateWebhookResponseTypeDef = TypedDict(
    "ClientCreateWebhookResponseTypeDef",
    {"webhook": ClientCreateWebhookResponsewebhookTypeDef},
    total=False,
)

ClientDeleteAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "ClientDeleteAppResponseappautoBranchCreationConfigTypeDef",
    {
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)

ClientDeleteAppResponseappcustomRulesTypeDef = TypedDict(
    "ClientDeleteAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)

ClientDeleteAppResponseappproductionBranchTypeDef = TypedDict(
    "ClientDeleteAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)

ClientDeleteAppResponseappTypeDef = TypedDict(
    "ClientDeleteAppResponseappTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ClientDeleteAppResponseappcustomRulesTypeDef],
        "productionBranch": ClientDeleteAppResponseappproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ClientDeleteAppResponseappautoBranchCreationConfigTypeDef,
    },
    total=False,
)

ClientDeleteAppResponseTypeDef = TypedDict(
    "ClientDeleteAppResponseTypeDef", {"app": ClientDeleteAppResponseappTypeDef}, total=False
)

ClientDeleteBackendEnvironmentResponsebackendEnvironmentTypeDef = TypedDict(
    "ClientDeleteBackendEnvironmentResponsebackendEnvironmentTypeDef",
    {
        "backendEnvironmentArn": str,
        "environmentName": str,
        "stackName": str,
        "deploymentArtifacts": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)

ClientDeleteBackendEnvironmentResponseTypeDef = TypedDict(
    "ClientDeleteBackendEnvironmentResponseTypeDef",
    {"backendEnvironment": ClientDeleteBackendEnvironmentResponsebackendEnvironmentTypeDef},
    total=False,
)

ClientDeleteBranchResponsebranchTypeDef = TypedDict(
    "ClientDeleteBranchResponsebranchTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)

ClientDeleteBranchResponseTypeDef = TypedDict(
    "ClientDeleteBranchResponseTypeDef",
    {"branch": ClientDeleteBranchResponsebranchTypeDef},
    total=False,
)

ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)

ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)

ClientDeleteDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "ClientDeleteDomainAssociationResponsedomainAssociationTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": Literal[
            "PENDING_VERIFICATION",
            "IN_PROGRESS",
            "AVAILABLE",
            "PENDING_DEPLOYMENT",
            "FAILED",
            "CREATING",
            "REQUESTING_CERTIFICATE",
            "UPDATING",
        ],
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef],
    },
    total=False,
)

ClientDeleteDomainAssociationResponseTypeDef = TypedDict(
    "ClientDeleteDomainAssociationResponseTypeDef",
    {"domainAssociation": ClientDeleteDomainAssociationResponsedomainAssociationTypeDef},
    total=False,
)

ClientDeleteJobResponsejobSummaryTypeDef = TypedDict(
    "ClientDeleteJobResponsejobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": Literal[
            "PENDING", "PROVISIONING", "RUNNING", "FAILED", "SUCCEED", "CANCELLING", "CANCELLED"
        ],
        "endTime": datetime,
        "jobType": Literal["RELEASE", "RETRY", "MANUAL", "WEB_HOOK"],
    },
    total=False,
)

ClientDeleteJobResponseTypeDef = TypedDict(
    "ClientDeleteJobResponseTypeDef",
    {"jobSummary": ClientDeleteJobResponsejobSummaryTypeDef},
    total=False,
)

ClientDeleteWebhookResponsewebhookTypeDef = TypedDict(
    "ClientDeleteWebhookResponsewebhookTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)

ClientDeleteWebhookResponseTypeDef = TypedDict(
    "ClientDeleteWebhookResponseTypeDef",
    {"webhook": ClientDeleteWebhookResponsewebhookTypeDef},
    total=False,
)

ClientGenerateAccessLogsResponseTypeDef = TypedDict(
    "ClientGenerateAccessLogsResponseTypeDef", {"logUrl": str}, total=False
)

ClientGetAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "ClientGetAppResponseappautoBranchCreationConfigTypeDef",
    {
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)

ClientGetAppResponseappcustomRulesTypeDef = TypedDict(
    "ClientGetAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)

ClientGetAppResponseappproductionBranchTypeDef = TypedDict(
    "ClientGetAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)

ClientGetAppResponseappTypeDef = TypedDict(
    "ClientGetAppResponseappTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ClientGetAppResponseappcustomRulesTypeDef],
        "productionBranch": ClientGetAppResponseappproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ClientGetAppResponseappautoBranchCreationConfigTypeDef,
    },
    total=False,
)

ClientGetAppResponseTypeDef = TypedDict(
    "ClientGetAppResponseTypeDef", {"app": ClientGetAppResponseappTypeDef}, total=False
)

ClientGetArtifactUrlResponseTypeDef = TypedDict(
    "ClientGetArtifactUrlResponseTypeDef", {"artifactId": str, "artifactUrl": str}, total=False
)

ClientGetBackendEnvironmentResponsebackendEnvironmentTypeDef = TypedDict(
    "ClientGetBackendEnvironmentResponsebackendEnvironmentTypeDef",
    {
        "backendEnvironmentArn": str,
        "environmentName": str,
        "stackName": str,
        "deploymentArtifacts": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)

ClientGetBackendEnvironmentResponseTypeDef = TypedDict(
    "ClientGetBackendEnvironmentResponseTypeDef",
    {"backendEnvironment": ClientGetBackendEnvironmentResponsebackendEnvironmentTypeDef},
    total=False,
)

ClientGetBranchResponsebranchTypeDef = TypedDict(
    "ClientGetBranchResponsebranchTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)

ClientGetBranchResponseTypeDef = TypedDict(
    "ClientGetBranchResponseTypeDef", {"branch": ClientGetBranchResponsebranchTypeDef}, total=False
)

ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)

ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)

ClientGetDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "ClientGetDomainAssociationResponsedomainAssociationTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": Literal[
            "PENDING_VERIFICATION",
            "IN_PROGRESS",
            "AVAILABLE",
            "PENDING_DEPLOYMENT",
            "FAILED",
            "CREATING",
            "REQUESTING_CERTIFICATE",
            "UPDATING",
        ],
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef],
    },
    total=False,
)

ClientGetDomainAssociationResponseTypeDef = TypedDict(
    "ClientGetDomainAssociationResponseTypeDef",
    {"domainAssociation": ClientGetDomainAssociationResponsedomainAssociationTypeDef},
    total=False,
)

ClientGetJobResponsejobstepsTypeDef = TypedDict(
    "ClientGetJobResponsejobstepsTypeDef",
    {
        "stepName": str,
        "startTime": datetime,
        "status": Literal[
            "PENDING", "PROVISIONING", "RUNNING", "FAILED", "SUCCEED", "CANCELLING", "CANCELLED"
        ],
        "endTime": datetime,
        "logUrl": str,
        "artifactsUrl": str,
        "testArtifactsUrl": str,
        "testConfigUrl": str,
        "screenshots": Dict[str, str],
        "statusReason": str,
        "context": str,
    },
    total=False,
)

ClientGetJobResponsejobsummaryTypeDef = TypedDict(
    "ClientGetJobResponsejobsummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": Literal[
            "PENDING", "PROVISIONING", "RUNNING", "FAILED", "SUCCEED", "CANCELLING", "CANCELLED"
        ],
        "endTime": datetime,
        "jobType": Literal["RELEASE", "RETRY", "MANUAL", "WEB_HOOK"],
    },
    total=False,
)

ClientGetJobResponsejobTypeDef = TypedDict(
    "ClientGetJobResponsejobTypeDef",
    {
        "summary": ClientGetJobResponsejobsummaryTypeDef,
        "steps": List[ClientGetJobResponsejobstepsTypeDef],
    },
    total=False,
)

ClientGetJobResponseTypeDef = TypedDict(
    "ClientGetJobResponseTypeDef", {"job": ClientGetJobResponsejobTypeDef}, total=False
)

ClientGetWebhookResponsewebhookTypeDef = TypedDict(
    "ClientGetWebhookResponsewebhookTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)

ClientGetWebhookResponseTypeDef = TypedDict(
    "ClientGetWebhookResponseTypeDef",
    {"webhook": ClientGetWebhookResponsewebhookTypeDef},
    total=False,
)

ClientListAppsResponseappsautoBranchCreationConfigTypeDef = TypedDict(
    "ClientListAppsResponseappsautoBranchCreationConfigTypeDef",
    {
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)

ClientListAppsResponseappscustomRulesTypeDef = TypedDict(
    "ClientListAppsResponseappscustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)

ClientListAppsResponseappsproductionBranchTypeDef = TypedDict(
    "ClientListAppsResponseappsproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)

ClientListAppsResponseappsTypeDef = TypedDict(
    "ClientListAppsResponseappsTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ClientListAppsResponseappscustomRulesTypeDef],
        "productionBranch": ClientListAppsResponseappsproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ClientListAppsResponseappsautoBranchCreationConfigTypeDef,
    },
    total=False,
)

ClientListAppsResponseTypeDef = TypedDict(
    "ClientListAppsResponseTypeDef",
    {"apps": List[ClientListAppsResponseappsTypeDef], "nextToken": str},
    total=False,
)

ClientListArtifactsResponseartifactsTypeDef = TypedDict(
    "ClientListArtifactsResponseartifactsTypeDef",
    {"artifactFileName": str, "artifactId": str},
    total=False,
)

ClientListArtifactsResponseTypeDef = TypedDict(
    "ClientListArtifactsResponseTypeDef",
    {"artifacts": List[ClientListArtifactsResponseartifactsTypeDef], "nextToken": str},
    total=False,
)

ClientListBackendEnvironmentsResponsebackendEnvironmentsTypeDef = TypedDict(
    "ClientListBackendEnvironmentsResponsebackendEnvironmentsTypeDef",
    {
        "backendEnvironmentArn": str,
        "environmentName": str,
        "stackName": str,
        "deploymentArtifacts": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)

ClientListBackendEnvironmentsResponseTypeDef = TypedDict(
    "ClientListBackendEnvironmentsResponseTypeDef",
    {
        "backendEnvironments": List[
            ClientListBackendEnvironmentsResponsebackendEnvironmentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListBranchesResponsebranchesTypeDef = TypedDict(
    "ClientListBranchesResponsebranchesTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)

ClientListBranchesResponseTypeDef = TypedDict(
    "ClientListBranchesResponseTypeDef",
    {"branches": List[ClientListBranchesResponsebranchesTypeDef], "nextToken": str},
    total=False,
)

ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef = TypedDict(
    "ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)

ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef = TypedDict(
    "ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef",
    {
        "subDomainSetting": ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)

ClientListDomainAssociationsResponsedomainAssociationsTypeDef = TypedDict(
    "ClientListDomainAssociationsResponsedomainAssociationsTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": Literal[
            "PENDING_VERIFICATION",
            "IN_PROGRESS",
            "AVAILABLE",
            "PENDING_DEPLOYMENT",
            "FAILED",
            "CREATING",
            "REQUESTING_CERTIFICATE",
            "UPDATING",
        ],
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef],
    },
    total=False,
)

ClientListDomainAssociationsResponseTypeDef = TypedDict(
    "ClientListDomainAssociationsResponseTypeDef",
    {
        "domainAssociations": List[ClientListDomainAssociationsResponsedomainAssociationsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListJobsResponsejobSummariesTypeDef = TypedDict(
    "ClientListJobsResponsejobSummariesTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": Literal[
            "PENDING", "PROVISIONING", "RUNNING", "FAILED", "SUCCEED", "CANCELLING", "CANCELLED"
        ],
        "endTime": datetime,
        "jobType": Literal["RELEASE", "RETRY", "MANUAL", "WEB_HOOK"],
    },
    total=False,
)

ClientListJobsResponseTypeDef = TypedDict(
    "ClientListJobsResponseTypeDef",
    {"jobSummaries": List[ClientListJobsResponsejobSummariesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientListWebhooksResponsewebhooksTypeDef = TypedDict(
    "ClientListWebhooksResponsewebhooksTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)

ClientListWebhooksResponseTypeDef = TypedDict(
    "ClientListWebhooksResponseTypeDef",
    {"webhooks": List[ClientListWebhooksResponsewebhooksTypeDef], "nextToken": str},
    total=False,
)

ClientStartDeploymentResponsejobSummaryTypeDef = TypedDict(
    "ClientStartDeploymentResponsejobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": Literal[
            "PENDING", "PROVISIONING", "RUNNING", "FAILED", "SUCCEED", "CANCELLING", "CANCELLED"
        ],
        "endTime": datetime,
        "jobType": Literal["RELEASE", "RETRY", "MANUAL", "WEB_HOOK"],
    },
    total=False,
)

ClientStartDeploymentResponseTypeDef = TypedDict(
    "ClientStartDeploymentResponseTypeDef",
    {"jobSummary": ClientStartDeploymentResponsejobSummaryTypeDef},
    total=False,
)

ClientStartJobResponsejobSummaryTypeDef = TypedDict(
    "ClientStartJobResponsejobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": Literal[
            "PENDING", "PROVISIONING", "RUNNING", "FAILED", "SUCCEED", "CANCELLING", "CANCELLED"
        ],
        "endTime": datetime,
        "jobType": Literal["RELEASE", "RETRY", "MANUAL", "WEB_HOOK"],
    },
    total=False,
)

ClientStartJobResponseTypeDef = TypedDict(
    "ClientStartJobResponseTypeDef",
    {"jobSummary": ClientStartJobResponsejobSummaryTypeDef},
    total=False,
)

ClientStopJobResponsejobSummaryTypeDef = TypedDict(
    "ClientStopJobResponsejobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": Literal[
            "PENDING", "PROVISIONING", "RUNNING", "FAILED", "SUCCEED", "CANCELLING", "CANCELLED"
        ],
        "endTime": datetime,
        "jobType": Literal["RELEASE", "RETRY", "MANUAL", "WEB_HOOK"],
    },
    total=False,
)

ClientStopJobResponseTypeDef = TypedDict(
    "ClientStopJobResponseTypeDef",
    {"jobSummary": ClientStopJobResponsejobSummaryTypeDef},
    total=False,
)

ClientUpdateAppAutoBranchCreationConfigTypeDef = TypedDict(
    "ClientUpdateAppAutoBranchCreationConfigTypeDef",
    {
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)

_RequiredClientUpdateAppCustomRulesTypeDef = TypedDict(
    "_RequiredClientUpdateAppCustomRulesTypeDef", {"source": str}
)
_OptionalClientUpdateAppCustomRulesTypeDef = TypedDict(
    "_OptionalClientUpdateAppCustomRulesTypeDef",
    {"target": str, "status": str, "condition": str},
    total=False,
)


class ClientUpdateAppCustomRulesTypeDef(
    _RequiredClientUpdateAppCustomRulesTypeDef, _OptionalClientUpdateAppCustomRulesTypeDef
):
    pass


ClientUpdateAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "ClientUpdateAppResponseappautoBranchCreationConfigTypeDef",
    {
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)

ClientUpdateAppResponseappcustomRulesTypeDef = TypedDict(
    "ClientUpdateAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)

ClientUpdateAppResponseappproductionBranchTypeDef = TypedDict(
    "ClientUpdateAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)

ClientUpdateAppResponseappTypeDef = TypedDict(
    "ClientUpdateAppResponseappTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ClientUpdateAppResponseappcustomRulesTypeDef],
        "productionBranch": ClientUpdateAppResponseappproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ClientUpdateAppResponseappautoBranchCreationConfigTypeDef,
    },
    total=False,
)

ClientUpdateAppResponseTypeDef = TypedDict(
    "ClientUpdateAppResponseTypeDef", {"app": ClientUpdateAppResponseappTypeDef}, total=False
)

ClientUpdateBranchResponsebranchTypeDef = TypedDict(
    "ClientUpdateBranchResponsebranchTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)

ClientUpdateBranchResponseTypeDef = TypedDict(
    "ClientUpdateBranchResponseTypeDef",
    {"branch": ClientUpdateBranchResponsebranchTypeDef},
    total=False,
)

ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)

ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)

ClientUpdateDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "ClientUpdateDomainAssociationResponsedomainAssociationTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": Literal[
            "PENDING_VERIFICATION",
            "IN_PROGRESS",
            "AVAILABLE",
            "PENDING_DEPLOYMENT",
            "FAILED",
            "CREATING",
            "REQUESTING_CERTIFICATE",
            "UPDATING",
        ],
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef],
    },
    total=False,
)

ClientUpdateDomainAssociationResponseTypeDef = TypedDict(
    "ClientUpdateDomainAssociationResponseTypeDef",
    {"domainAssociation": ClientUpdateDomainAssociationResponsedomainAssociationTypeDef},
    total=False,
)

_RequiredClientUpdateDomainAssociationSubDomainSettingsTypeDef = TypedDict(
    "_RequiredClientUpdateDomainAssociationSubDomainSettingsTypeDef", {"prefix": str}
)
_OptionalClientUpdateDomainAssociationSubDomainSettingsTypeDef = TypedDict(
    "_OptionalClientUpdateDomainAssociationSubDomainSettingsTypeDef",
    {"branchName": str},
    total=False,
)


class ClientUpdateDomainAssociationSubDomainSettingsTypeDef(
    _RequiredClientUpdateDomainAssociationSubDomainSettingsTypeDef,
    _OptionalClientUpdateDomainAssociationSubDomainSettingsTypeDef,
):
    pass


ClientUpdateWebhookResponsewebhookTypeDef = TypedDict(
    "ClientUpdateWebhookResponsewebhookTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
    total=False,
)

ClientUpdateWebhookResponseTypeDef = TypedDict(
    "ClientUpdateWebhookResponseTypeDef",
    {"webhook": ClientUpdateWebhookResponsewebhookTypeDef},
    total=False,
)

ListAppsPaginatePaginationConfigTypeDef = TypedDict(
    "ListAppsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef = TypedDict(
    "ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef",
    {
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)

ListAppsPaginateResponseappscustomRulesTypeDef = TypedDict(
    "ListAppsPaginateResponseappscustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)

ListAppsPaginateResponseappsproductionBranchTypeDef = TypedDict(
    "ListAppsPaginateResponseappsproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)

ListAppsPaginateResponseappsTypeDef = TypedDict(
    "ListAppsPaginateResponseappsTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "tags": Dict[str, str],
        "description": str,
        "repository": str,
        "platform": str,
        "createTime": datetime,
        "updateTime": datetime,
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List[ListAppsPaginateResponseappscustomRulesTypeDef],
        "productionBranch": ListAppsPaginateResponseappsproductionBranchTypeDef,
        "buildSpec": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef,
    },
    total=False,
)

ListAppsPaginateResponseTypeDef = TypedDict(
    "ListAppsPaginateResponseTypeDef",
    {"apps": List[ListAppsPaginateResponseappsTypeDef], "NextToken": str},
    total=False,
)

ListBranchesPaginatePaginationConfigTypeDef = TypedDict(
    "ListBranchesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListBranchesPaginateResponsebranchesTypeDef = TypedDict(
    "ListBranchesPaginateResponsebranchesTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "tags": Dict[str, str],
        "stage": Literal["PRODUCTION", "BETA", "DEVELOPMENT", "EXPERIMENTAL", "PULL_REQUEST"],
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "ttl": str,
        "associatedResources": List[str],
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)

ListBranchesPaginateResponseTypeDef = TypedDict(
    "ListBranchesPaginateResponseTypeDef",
    {"branches": List[ListBranchesPaginateResponsebranchesTypeDef], "NextToken": str},
    total=False,
)

ListDomainAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDomainAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef = TypedDict(
    "ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)

ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef = TypedDict(
    "ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef",
    {
        "subDomainSetting": ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)

ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef = TypedDict(
    "ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": Literal[
            "PENDING_VERIFICATION",
            "IN_PROGRESS",
            "AVAILABLE",
            "PENDING_DEPLOYMENT",
            "FAILED",
            "CREATING",
            "REQUESTING_CERTIFICATE",
            "UPDATING",
        ],
        "statusReason": str,
        "certificateVerificationDNSRecord": str,
        "subDomains": List[
            ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef
        ],
    },
    total=False,
)

ListDomainAssociationsPaginateResponseTypeDef = TypedDict(
    "ListDomainAssociationsPaginateResponseTypeDef",
    {
        "domainAssociations": List[ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListJobsPaginateResponsejobSummariesTypeDef = TypedDict(
    "ListJobsPaginateResponsejobSummariesTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": Literal[
            "PENDING", "PROVISIONING", "RUNNING", "FAILED", "SUCCEED", "CANCELLING", "CANCELLED"
        ],
        "endTime": datetime,
        "jobType": Literal["RELEASE", "RETRY", "MANUAL", "WEB_HOOK"],
    },
    total=False,
)

ListJobsPaginateResponseTypeDef = TypedDict(
    "ListJobsPaginateResponseTypeDef",
    {"jobSummaries": List[ListJobsPaginateResponsejobSummariesTypeDef], "NextToken": str},
    total=False,
)
