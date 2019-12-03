"Main interface for amplify service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateAppAutoBranchCreationConfigTypeDef",
    "ClientCreateAppCustomRulesTypeDef",
    "ClientCreateAppResponseappautoBranchCreationConfigTypeDef",
    "ClientCreateAppResponseappcustomRulesTypeDef",
    "ClientCreateAppResponseappproductionBranchTypeDef",
    "ClientCreateAppResponseappTypeDef",
    "ClientCreateAppResponseTypeDef",
    "ClientCreateBackendEnvironmentResponsebackendEnvironmentTypeDef",
    "ClientCreateBackendEnvironmentResponseTypeDef",
    "ClientCreateBranchResponsebranchTypeDef",
    "ClientCreateBranchResponseTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    "ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    "ClientCreateDomainAssociationResponsedomainAssociationTypeDef",
    "ClientCreateDomainAssociationResponseTypeDef",
    "ClientCreateDomainAssociationSubDomainSettingsTypeDef",
    "ClientCreateWebhookResponsewebhookTypeDef",
    "ClientCreateWebhookResponseTypeDef",
    "ClientDeleteAppResponseappautoBranchCreationConfigTypeDef",
    "ClientDeleteAppResponseappcustomRulesTypeDef",
    "ClientDeleteAppResponseappproductionBranchTypeDef",
    "ClientDeleteAppResponseappTypeDef",
    "ClientDeleteAppResponseTypeDef",
    "ClientDeleteBackendEnvironmentResponsebackendEnvironmentTypeDef",
    "ClientDeleteBackendEnvironmentResponseTypeDef",
    "ClientDeleteBranchResponsebranchTypeDef",
    "ClientDeleteBranchResponseTypeDef",
    "ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    "ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    "ClientDeleteDomainAssociationResponsedomainAssociationTypeDef",
    "ClientDeleteDomainAssociationResponseTypeDef",
    "ClientDeleteJobResponsejobSummaryTypeDef",
    "ClientDeleteJobResponseTypeDef",
    "ClientDeleteWebhookResponsewebhookTypeDef",
    "ClientDeleteWebhookResponseTypeDef",
    "ClientGenerateAccessLogsResponseTypeDef",
    "ClientGetAppResponseappautoBranchCreationConfigTypeDef",
    "ClientGetAppResponseappcustomRulesTypeDef",
    "ClientGetAppResponseappproductionBranchTypeDef",
    "ClientGetAppResponseappTypeDef",
    "ClientGetAppResponseTypeDef",
    "ClientGetArtifactUrlResponseTypeDef",
    "ClientGetBackendEnvironmentResponsebackendEnvironmentTypeDef",
    "ClientGetBackendEnvironmentResponseTypeDef",
    "ClientGetBranchResponsebranchTypeDef",
    "ClientGetBranchResponseTypeDef",
    "ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    "ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    "ClientGetDomainAssociationResponsedomainAssociationTypeDef",
    "ClientGetDomainAssociationResponseTypeDef",
    "ClientGetJobResponsejobstepsTypeDef",
    "ClientGetJobResponsejobsummaryTypeDef",
    "ClientGetJobResponsejobTypeDef",
    "ClientGetJobResponseTypeDef",
    "ClientGetWebhookResponsewebhookTypeDef",
    "ClientGetWebhookResponseTypeDef",
    "ClientListAppsResponseappsautoBranchCreationConfigTypeDef",
    "ClientListAppsResponseappscustomRulesTypeDef",
    "ClientListAppsResponseappsproductionBranchTypeDef",
    "ClientListAppsResponseappsTypeDef",
    "ClientListAppsResponseTypeDef",
    "ClientListArtifactsResponseartifactsTypeDef",
    "ClientListArtifactsResponseTypeDef",
    "ClientListBackendEnvironmentsResponsebackendEnvironmentsTypeDef",
    "ClientListBackendEnvironmentsResponseTypeDef",
    "ClientListBranchesResponsebranchesTypeDef",
    "ClientListBranchesResponseTypeDef",
    "ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef",
    "ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef",
    "ClientListDomainAssociationsResponsedomainAssociationsTypeDef",
    "ClientListDomainAssociationsResponseTypeDef",
    "ClientListJobsResponsejobSummariesTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWebhooksResponsewebhooksTypeDef",
    "ClientListWebhooksResponseTypeDef",
    "ClientStartDeploymentResponsejobSummaryTypeDef",
    "ClientStartDeploymentResponseTypeDef",
    "ClientStartJobResponsejobSummaryTypeDef",
    "ClientStartJobResponseTypeDef",
    "ClientStopJobResponsejobSummaryTypeDef",
    "ClientStopJobResponseTypeDef",
    "ClientUpdateAppAutoBranchCreationConfigTypeDef",
    "ClientUpdateAppCustomRulesTypeDef",
    "ClientUpdateAppResponseappautoBranchCreationConfigTypeDef",
    "ClientUpdateAppResponseappcustomRulesTypeDef",
    "ClientUpdateAppResponseappproductionBranchTypeDef",
    "ClientUpdateAppResponseappTypeDef",
    "ClientUpdateAppResponseTypeDef",
    "ClientUpdateBranchResponsebranchTypeDef",
    "ClientUpdateBranchResponseTypeDef",
    "ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    "ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    "ClientUpdateDomainAssociationResponsedomainAssociationTypeDef",
    "ClientUpdateDomainAssociationResponseTypeDef",
    "ClientUpdateDomainAssociationSubDomainSettingsTypeDef",
    "ClientUpdateWebhookResponsewebhookTypeDef",
    "ClientUpdateWebhookResponseTypeDef",
    "ListAppsPaginatePaginationConfigTypeDef",
    "ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef",
    "ListAppsPaginateResponseappscustomRulesTypeDef",
    "ListAppsPaginateResponseappsproductionBranchTypeDef",
    "ListAppsPaginateResponseappsTypeDef",
    "ListAppsPaginateResponseTypeDef",
    "ListBranchesPaginatePaginationConfigTypeDef",
    "ListBranchesPaginateResponsebranchesTypeDef",
    "ListBranchesPaginateResponseTypeDef",
    "ListDomainAssociationsPaginatePaginationConfigTypeDef",
    "ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef",
    "ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef",
    "ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef",
    "ListDomainAssociationsPaginateResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponsejobSummariesTypeDef",
    "ListJobsPaginateResponseTypeDef",
)


_ClientCreateAppAutoBranchCreationConfigTypeDef = TypedDict(
    "_ClientCreateAppAutoBranchCreationConfigTypeDef",
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


class ClientCreateAppAutoBranchCreationConfigTypeDef(
    _ClientCreateAppAutoBranchCreationConfigTypeDef
):
    """
    Automated branch creation config for the Amplify App.
    - **stage** *(string) --*

      Stage for the auto created branch.
    """


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
    """
    - *(dict) --*

      Custom rewrite / redirect rule.
      - **source** *(string) --***[REQUIRED]**

        The source pattern for a URL rewrite or redirect rule.
    """


_ClientCreateAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientCreateAppResponseappautoBranchCreationConfigTypeDef",
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


class ClientCreateAppResponseappautoBranchCreationConfigTypeDef(
    _ClientCreateAppResponseappautoBranchCreationConfigTypeDef
):
    pass


_ClientCreateAppResponseappcustomRulesTypeDef = TypedDict(
    "_ClientCreateAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ClientCreateAppResponseappcustomRulesTypeDef(_ClientCreateAppResponseappcustomRulesTypeDef):
    pass


_ClientCreateAppResponseappproductionBranchTypeDef = TypedDict(
    "_ClientCreateAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ClientCreateAppResponseappproductionBranchTypeDef(
    _ClientCreateAppResponseappproductionBranchTypeDef
):
    pass


_ClientCreateAppResponseappTypeDef = TypedDict(
    "_ClientCreateAppResponseappTypeDef",
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


class ClientCreateAppResponseappTypeDef(_ClientCreateAppResponseappTypeDef):
    """
    - **app** *(dict) --*

      Amplify App represents different branches of a repository for building, deploying, and
      hosting.
      - **appId** *(string) --*

        Unique Id for the Amplify App.
    """


_ClientCreateAppResponseTypeDef = TypedDict(
    "_ClientCreateAppResponseTypeDef", {"app": ClientCreateAppResponseappTypeDef}, total=False
)


class ClientCreateAppResponseTypeDef(_ClientCreateAppResponseTypeDef):
    """
    - *(dict) --*

      - **app** *(dict) --*

        Amplify App represents different branches of a repository for building, deploying, and
        hosting.
        - **appId** *(string) --*

          Unique Id for the Amplify App.
    """


_ClientCreateBackendEnvironmentResponsebackendEnvironmentTypeDef = TypedDict(
    "_ClientCreateBackendEnvironmentResponsebackendEnvironmentTypeDef",
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


class ClientCreateBackendEnvironmentResponsebackendEnvironmentTypeDef(
    _ClientCreateBackendEnvironmentResponsebackendEnvironmentTypeDef
):
    """
    - **backendEnvironment** *(dict) --*

      Backend environment structure for an amplify App.
      - **backendEnvironmentArn** *(string) --*

        Arn for a backend environment, part of an Amplify App.
    """


_ClientCreateBackendEnvironmentResponseTypeDef = TypedDict(
    "_ClientCreateBackendEnvironmentResponseTypeDef",
    {"backendEnvironment": ClientCreateBackendEnvironmentResponsebackendEnvironmentTypeDef},
    total=False,
)


class ClientCreateBackendEnvironmentResponseTypeDef(_ClientCreateBackendEnvironmentResponseTypeDef):
    """
    - *(dict) --*

      Result structure for create backend environment.
      - **backendEnvironment** *(dict) --*

        Backend environment structure for an amplify App.
        - **backendEnvironmentArn** *(string) --*

          Arn for a backend environment, part of an Amplify App.
    """


_ClientCreateBranchResponsebranchTypeDef = TypedDict(
    "_ClientCreateBranchResponsebranchTypeDef",
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


class ClientCreateBranchResponsebranchTypeDef(_ClientCreateBranchResponsebranchTypeDef):
    """
    - **branch** *(dict) --*

      Branch structure for an Amplify App.
      - **branchArn** *(string) --*

        ARN for a branch, part of an Amplify App.
    """


_ClientCreateBranchResponseTypeDef = TypedDict(
    "_ClientCreateBranchResponseTypeDef",
    {"branch": ClientCreateBranchResponsebranchTypeDef},
    total=False,
)


class ClientCreateBranchResponseTypeDef(_ClientCreateBranchResponseTypeDef):
    """
    - *(dict) --*

      Result structure for create branch request.
      - **branch** *(dict) --*

        Branch structure for an Amplify App.
        - **branchArn** *(string) --*

          ARN for a branch, part of an Amplify App.
    """


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef",
    {"jobId": str, "fileUploadUrls": Dict[str, str], "zipUploadUrl": str},
    total=False,
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    - *(dict) --*

      Result structure for create a new deployment.
      - **jobId** *(string) --*

        The jobId for this deployment, will supply to start deployment api.
    """


_ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "_ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef(
    _ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef
):
    pass


_ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "_ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientCreateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef(
    _ClientCreateDomainAssociationResponsedomainAssociationsubDomainsTypeDef
):
    pass


_ClientCreateDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "_ClientCreateDomainAssociationResponsedomainAssociationTypeDef",
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


class ClientCreateDomainAssociationResponsedomainAssociationTypeDef(
    _ClientCreateDomainAssociationResponsedomainAssociationTypeDef
):
    """
    - **domainAssociation** *(dict) --*

      Domain Association structure.
      - **domainAssociationArn** *(string) --*

        ARN for the Domain Association.
    """


_ClientCreateDomainAssociationResponseTypeDef = TypedDict(
    "_ClientCreateDomainAssociationResponseTypeDef",
    {"domainAssociation": ClientCreateDomainAssociationResponsedomainAssociationTypeDef},
    total=False,
)


class ClientCreateDomainAssociationResponseTypeDef(_ClientCreateDomainAssociationResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the create Domain Association request.
      - **domainAssociation** *(dict) --*

        Domain Association structure.
        - **domainAssociationArn** *(string) --*

          ARN for the Domain Association.
    """


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
    """
    - *(dict) --*

      Setting for the Subdomain.
      - **prefix** *(string) --***[REQUIRED]**

        Prefix setting for the Subdomain.
    """


_ClientCreateWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientCreateWebhookResponsewebhookTypeDef",
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


class ClientCreateWebhookResponsewebhookTypeDef(_ClientCreateWebhookResponsewebhookTypeDef):
    """
    - **webhook** *(dict) --*

      Webhook structure.
      - **webhookArn** *(string) --*

        ARN for the webhook.
    """


_ClientCreateWebhookResponseTypeDef = TypedDict(
    "_ClientCreateWebhookResponseTypeDef",
    {"webhook": ClientCreateWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientCreateWebhookResponseTypeDef(_ClientCreateWebhookResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the create webhook request.
      - **webhook** *(dict) --*

        Webhook structure.
        - **webhookArn** *(string) --*

          ARN for the webhook.
    """


_ClientDeleteAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientDeleteAppResponseappautoBranchCreationConfigTypeDef",
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


class ClientDeleteAppResponseappautoBranchCreationConfigTypeDef(
    _ClientDeleteAppResponseappautoBranchCreationConfigTypeDef
):
    pass


_ClientDeleteAppResponseappcustomRulesTypeDef = TypedDict(
    "_ClientDeleteAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ClientDeleteAppResponseappcustomRulesTypeDef(_ClientDeleteAppResponseappcustomRulesTypeDef):
    pass


_ClientDeleteAppResponseappproductionBranchTypeDef = TypedDict(
    "_ClientDeleteAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ClientDeleteAppResponseappproductionBranchTypeDef(
    _ClientDeleteAppResponseappproductionBranchTypeDef
):
    pass


_ClientDeleteAppResponseappTypeDef = TypedDict(
    "_ClientDeleteAppResponseappTypeDef",
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


class ClientDeleteAppResponseappTypeDef(_ClientDeleteAppResponseappTypeDef):
    """
    - **app** *(dict) --*

      Amplify App represents different branches of a repository for building, deploying, and
      hosting.
      - **appId** *(string) --*

        Unique Id for the Amplify App.
    """


_ClientDeleteAppResponseTypeDef = TypedDict(
    "_ClientDeleteAppResponseTypeDef", {"app": ClientDeleteAppResponseappTypeDef}, total=False
)


class ClientDeleteAppResponseTypeDef(_ClientDeleteAppResponseTypeDef):
    """
    - *(dict) --*

      Result structure for an Amplify App delete request.
      - **app** *(dict) --*

        Amplify App represents different branches of a repository for building, deploying, and
        hosting.
        - **appId** *(string) --*

          Unique Id for the Amplify App.
    """


_ClientDeleteBackendEnvironmentResponsebackendEnvironmentTypeDef = TypedDict(
    "_ClientDeleteBackendEnvironmentResponsebackendEnvironmentTypeDef",
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


class ClientDeleteBackendEnvironmentResponsebackendEnvironmentTypeDef(
    _ClientDeleteBackendEnvironmentResponsebackendEnvironmentTypeDef
):
    """
    - **backendEnvironment** *(dict) --*

      Backend environment structure for an Amplify App.
      - **backendEnvironmentArn** *(string) --*

        Arn for a backend environment, part of an Amplify App.
    """


_ClientDeleteBackendEnvironmentResponseTypeDef = TypedDict(
    "_ClientDeleteBackendEnvironmentResponseTypeDef",
    {"backendEnvironment": ClientDeleteBackendEnvironmentResponsebackendEnvironmentTypeDef},
    total=False,
)


class ClientDeleteBackendEnvironmentResponseTypeDef(_ClientDeleteBackendEnvironmentResponseTypeDef):
    """
    - *(dict) --*

      Result structure of a delete backend environment result.
      - **backendEnvironment** *(dict) --*

        Backend environment structure for an Amplify App.
        - **backendEnvironmentArn** *(string) --*

          Arn for a backend environment, part of an Amplify App.
    """


_ClientDeleteBranchResponsebranchTypeDef = TypedDict(
    "_ClientDeleteBranchResponsebranchTypeDef",
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


class ClientDeleteBranchResponsebranchTypeDef(_ClientDeleteBranchResponsebranchTypeDef):
    """
    - **branch** *(dict) --*

      Branch structure for an Amplify App.
      - **branchArn** *(string) --*

        ARN for a branch, part of an Amplify App.
    """


_ClientDeleteBranchResponseTypeDef = TypedDict(
    "_ClientDeleteBranchResponseTypeDef",
    {"branch": ClientDeleteBranchResponsebranchTypeDef},
    total=False,
)


class ClientDeleteBranchResponseTypeDef(_ClientDeleteBranchResponseTypeDef):
    """
    - *(dict) --*

      Result structure for delete branch request.
      - **branch** *(dict) --*

        Branch structure for an Amplify App.
        - **branchArn** *(string) --*

          ARN for a branch, part of an Amplify App.
    """


_ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "_ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef(
    _ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef
):
    pass


_ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "_ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientDeleteDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef(
    _ClientDeleteDomainAssociationResponsedomainAssociationsubDomainsTypeDef
):
    pass


_ClientDeleteDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "_ClientDeleteDomainAssociationResponsedomainAssociationTypeDef",
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


class ClientDeleteDomainAssociationResponsedomainAssociationTypeDef(
    _ClientDeleteDomainAssociationResponsedomainAssociationTypeDef
):
    """
    - **domainAssociation** *(dict) --*

      Structure for Domain Association, which associates a custom domain with an Amplify App.
      - **domainAssociationArn** *(string) --*

        ARN for the Domain Association.
    """


_ClientDeleteDomainAssociationResponseTypeDef = TypedDict(
    "_ClientDeleteDomainAssociationResponseTypeDef",
    {"domainAssociation": ClientDeleteDomainAssociationResponsedomainAssociationTypeDef},
    total=False,
)


class ClientDeleteDomainAssociationResponseTypeDef(_ClientDeleteDomainAssociationResponseTypeDef):
    """
    - *(dict) --*

      - **domainAssociation** *(dict) --*

        Structure for Domain Association, which associates a custom domain with an Amplify App.
        - **domainAssociationArn** *(string) --*

          ARN for the Domain Association.
    """


_ClientDeleteJobResponsejobSummaryTypeDef = TypedDict(
    "_ClientDeleteJobResponsejobSummaryTypeDef",
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


class ClientDeleteJobResponsejobSummaryTypeDef(_ClientDeleteJobResponsejobSummaryTypeDef):
    """
    - **jobSummary** *(dict) --*

      Structure for the summary of a Job.
      - **jobArn** *(string) --*

        Arn for the Job.
    """


_ClientDeleteJobResponseTypeDef = TypedDict(
    "_ClientDeleteJobResponseTypeDef",
    {"jobSummary": ClientDeleteJobResponsejobSummaryTypeDef},
    total=False,
)


class ClientDeleteJobResponseTypeDef(_ClientDeleteJobResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the delete job request.
      - **jobSummary** *(dict) --*

        Structure for the summary of a Job.
        - **jobArn** *(string) --*

          Arn for the Job.
    """


_ClientDeleteWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientDeleteWebhookResponsewebhookTypeDef",
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


class ClientDeleteWebhookResponsewebhookTypeDef(_ClientDeleteWebhookResponsewebhookTypeDef):
    """
    - **webhook** *(dict) --*

      Webhook structure.
      - **webhookArn** *(string) --*

        ARN for the webhook.
    """


_ClientDeleteWebhookResponseTypeDef = TypedDict(
    "_ClientDeleteWebhookResponseTypeDef",
    {"webhook": ClientDeleteWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientDeleteWebhookResponseTypeDef(_ClientDeleteWebhookResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the delete webhook request.
      - **webhook** *(dict) --*

        Webhook structure.
        - **webhookArn** *(string) --*

          ARN for the webhook.
    """


_ClientGenerateAccessLogsResponseTypeDef = TypedDict(
    "_ClientGenerateAccessLogsResponseTypeDef", {"logUrl": str}, total=False
)


class ClientGenerateAccessLogsResponseTypeDef(_ClientGenerateAccessLogsResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the generate access logs request.
      - **logUrl** *(string) --*

        Pre-signed URL for the requested access logs.
    """


_ClientGetAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientGetAppResponseappautoBranchCreationConfigTypeDef",
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


class ClientGetAppResponseappautoBranchCreationConfigTypeDef(
    _ClientGetAppResponseappautoBranchCreationConfigTypeDef
):
    pass


_ClientGetAppResponseappcustomRulesTypeDef = TypedDict(
    "_ClientGetAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ClientGetAppResponseappcustomRulesTypeDef(_ClientGetAppResponseappcustomRulesTypeDef):
    pass


_ClientGetAppResponseappproductionBranchTypeDef = TypedDict(
    "_ClientGetAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ClientGetAppResponseappproductionBranchTypeDef(
    _ClientGetAppResponseappproductionBranchTypeDef
):
    pass


_ClientGetAppResponseappTypeDef = TypedDict(
    "_ClientGetAppResponseappTypeDef",
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


class ClientGetAppResponseappTypeDef(_ClientGetAppResponseappTypeDef):
    """
    - **app** *(dict) --*

      Amplify App represents different branches of a repository for building, deploying, and
      hosting.
      - **appId** *(string) --*

        Unique Id for the Amplify App.
    """


_ClientGetAppResponseTypeDef = TypedDict(
    "_ClientGetAppResponseTypeDef", {"app": ClientGetAppResponseappTypeDef}, total=False
)


class ClientGetAppResponseTypeDef(_ClientGetAppResponseTypeDef):
    """
    - *(dict) --*

      - **app** *(dict) --*

        Amplify App represents different branches of a repository for building, deploying, and
        hosting.
        - **appId** *(string) --*

          Unique Id for the Amplify App.
    """


_ClientGetArtifactUrlResponseTypeDef = TypedDict(
    "_ClientGetArtifactUrlResponseTypeDef", {"artifactId": str, "artifactUrl": str}, total=False
)


class ClientGetArtifactUrlResponseTypeDef(_ClientGetArtifactUrlResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the get artifact request.
      - **artifactId** *(string) --*

        Unique Id for a artifact.
    """


_ClientGetBackendEnvironmentResponsebackendEnvironmentTypeDef = TypedDict(
    "_ClientGetBackendEnvironmentResponsebackendEnvironmentTypeDef",
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


class ClientGetBackendEnvironmentResponsebackendEnvironmentTypeDef(
    _ClientGetBackendEnvironmentResponsebackendEnvironmentTypeDef
):
    """
    - **backendEnvironment** *(dict) --*

      Backend environment structure for an an Amplify App.
      - **backendEnvironmentArn** *(string) --*

        Arn for a backend environment, part of an Amplify App.
    """


_ClientGetBackendEnvironmentResponseTypeDef = TypedDict(
    "_ClientGetBackendEnvironmentResponseTypeDef",
    {"backendEnvironment": ClientGetBackendEnvironmentResponsebackendEnvironmentTypeDef},
    total=False,
)


class ClientGetBackendEnvironmentResponseTypeDef(_ClientGetBackendEnvironmentResponseTypeDef):
    """
    - *(dict) --*

      Result structure for get backend environment result.
      - **backendEnvironment** *(dict) --*

        Backend environment structure for an an Amplify App.
        - **backendEnvironmentArn** *(string) --*

          Arn for a backend environment, part of an Amplify App.
    """


_ClientGetBranchResponsebranchTypeDef = TypedDict(
    "_ClientGetBranchResponsebranchTypeDef",
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


class ClientGetBranchResponsebranchTypeDef(_ClientGetBranchResponsebranchTypeDef):
    """
    - **branch** *(dict) --*

      Branch for an Amplify App, which maps to a 3rd party repository branch.
      - **branchArn** *(string) --*

        ARN for a branch, part of an Amplify App.
    """


_ClientGetBranchResponseTypeDef = TypedDict(
    "_ClientGetBranchResponseTypeDef", {"branch": ClientGetBranchResponsebranchTypeDef}, total=False
)


class ClientGetBranchResponseTypeDef(_ClientGetBranchResponseTypeDef):
    """
    - *(dict) --*

      - **branch** *(dict) --*

        Branch for an Amplify App, which maps to a 3rd party repository branch.
        - **branchArn** *(string) --*

          ARN for a branch, part of an Amplify App.
    """


_ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "_ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef(
    _ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef
):
    pass


_ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "_ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientGetDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef(
    _ClientGetDomainAssociationResponsedomainAssociationsubDomainsTypeDef
):
    pass


_ClientGetDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "_ClientGetDomainAssociationResponsedomainAssociationTypeDef",
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


class ClientGetDomainAssociationResponsedomainAssociationTypeDef(
    _ClientGetDomainAssociationResponsedomainAssociationTypeDef
):
    """
    - **domainAssociation** *(dict) --*

      Domain Association structure.
      - **domainAssociationArn** *(string) --*

        ARN for the Domain Association.
    """


_ClientGetDomainAssociationResponseTypeDef = TypedDict(
    "_ClientGetDomainAssociationResponseTypeDef",
    {"domainAssociation": ClientGetDomainAssociationResponsedomainAssociationTypeDef},
    total=False,
)


class ClientGetDomainAssociationResponseTypeDef(_ClientGetDomainAssociationResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the get Domain Association request.
      - **domainAssociation** *(dict) --*

        Domain Association structure.
        - **domainAssociationArn** *(string) --*

          ARN for the Domain Association.
    """


_ClientGetJobResponsejobstepsTypeDef = TypedDict(
    "_ClientGetJobResponsejobstepsTypeDef",
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


class ClientGetJobResponsejobstepsTypeDef(_ClientGetJobResponsejobstepsTypeDef):
    pass


_ClientGetJobResponsejobsummaryTypeDef = TypedDict(
    "_ClientGetJobResponsejobsummaryTypeDef",
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


class ClientGetJobResponsejobsummaryTypeDef(_ClientGetJobResponsejobsummaryTypeDef):
    """
    - **summary** *(dict) --*

      Summary for an execution job for an Amplify App.
      - **jobArn** *(string) --*

        Arn for the Job.
    """


_ClientGetJobResponsejobTypeDef = TypedDict(
    "_ClientGetJobResponsejobTypeDef",
    {
        "summary": ClientGetJobResponsejobsummaryTypeDef,
        "steps": List[ClientGetJobResponsejobstepsTypeDef],
    },
    total=False,
)


class ClientGetJobResponsejobTypeDef(_ClientGetJobResponsejobTypeDef):
    """
    - **job** *(dict) --*

      Structure for an execution job for an Amplify App.
      - **summary** *(dict) --*

        Summary for an execution job for an Amplify App.
        - **jobArn** *(string) --*

          Arn for the Job.
    """


_ClientGetJobResponseTypeDef = TypedDict(
    "_ClientGetJobResponseTypeDef", {"job": ClientGetJobResponsejobTypeDef}, total=False
)


class ClientGetJobResponseTypeDef(_ClientGetJobResponseTypeDef):
    """
    - *(dict) --*

      - **job** *(dict) --*

        Structure for an execution job for an Amplify App.
        - **summary** *(dict) --*

          Summary for an execution job for an Amplify App.
          - **jobArn** *(string) --*

            Arn for the Job.
    """


_ClientGetWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientGetWebhookResponsewebhookTypeDef",
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


class ClientGetWebhookResponsewebhookTypeDef(_ClientGetWebhookResponsewebhookTypeDef):
    """
    - **webhook** *(dict) --*

      Webhook structure.
      - **webhookArn** *(string) --*

        ARN for the webhook.
    """


_ClientGetWebhookResponseTypeDef = TypedDict(
    "_ClientGetWebhookResponseTypeDef",
    {"webhook": ClientGetWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientGetWebhookResponseTypeDef(_ClientGetWebhookResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the get webhook request.
      - **webhook** *(dict) --*

        Webhook structure.
        - **webhookArn** *(string) --*

          ARN for the webhook.
    """


_ClientListAppsResponseappsautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientListAppsResponseappsautoBranchCreationConfigTypeDef",
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


class ClientListAppsResponseappsautoBranchCreationConfigTypeDef(
    _ClientListAppsResponseappsautoBranchCreationConfigTypeDef
):
    pass


_ClientListAppsResponseappscustomRulesTypeDef = TypedDict(
    "_ClientListAppsResponseappscustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ClientListAppsResponseappscustomRulesTypeDef(_ClientListAppsResponseappscustomRulesTypeDef):
    pass


_ClientListAppsResponseappsproductionBranchTypeDef = TypedDict(
    "_ClientListAppsResponseappsproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ClientListAppsResponseappsproductionBranchTypeDef(
    _ClientListAppsResponseappsproductionBranchTypeDef
):
    pass


_ClientListAppsResponseappsTypeDef = TypedDict(
    "_ClientListAppsResponseappsTypeDef",
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


class ClientListAppsResponseappsTypeDef(_ClientListAppsResponseappsTypeDef):
    """
    - *(dict) --*

      Amplify App represents different branches of a repository for building, deploying, and
      hosting.
      - **appId** *(string) --*

        Unique Id for the Amplify App.
    """


_ClientListAppsResponseTypeDef = TypedDict(
    "_ClientListAppsResponseTypeDef",
    {"apps": List[ClientListAppsResponseappsTypeDef], "nextToken": str},
    total=False,
)


class ClientListAppsResponseTypeDef(_ClientListAppsResponseTypeDef):
    """
    - *(dict) --*

      Result structure for an Amplify App list request.
      - **apps** *(list) --*

        List of Amplify Apps.
        - *(dict) --*

          Amplify App represents different branches of a repository for building, deploying, and
          hosting.
          - **appId** *(string) --*

            Unique Id for the Amplify App.
    """


_ClientListArtifactsResponseartifactsTypeDef = TypedDict(
    "_ClientListArtifactsResponseartifactsTypeDef",
    {"artifactFileName": str, "artifactId": str},
    total=False,
)


class ClientListArtifactsResponseartifactsTypeDef(_ClientListArtifactsResponseartifactsTypeDef):
    """
    - *(dict) --*

      Structure for artifact.
      - **artifactFileName** *(string) --*

        File name for the artifact.
    """


_ClientListArtifactsResponseTypeDef = TypedDict(
    "_ClientListArtifactsResponseTypeDef",
    {"artifacts": List[ClientListArtifactsResponseartifactsTypeDef], "nextToken": str},
    total=False,
)


class ClientListArtifactsResponseTypeDef(_ClientListArtifactsResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the list artifacts request.
      - **artifacts** *(list) --*

        List of artifacts.
        - *(dict) --*

          Structure for artifact.
          - **artifactFileName** *(string) --*

            File name for the artifact.
    """


_ClientListBackendEnvironmentsResponsebackendEnvironmentsTypeDef = TypedDict(
    "_ClientListBackendEnvironmentsResponsebackendEnvironmentsTypeDef",
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


class ClientListBackendEnvironmentsResponsebackendEnvironmentsTypeDef(
    _ClientListBackendEnvironmentsResponsebackendEnvironmentsTypeDef
):
    """
    - *(dict) --*

      Backend environment for an Amplify App.
      - **backendEnvironmentArn** *(string) --*

        Arn for a backend environment, part of an Amplify App.
    """


_ClientListBackendEnvironmentsResponseTypeDef = TypedDict(
    "_ClientListBackendEnvironmentsResponseTypeDef",
    {
        "backendEnvironments": List[
            ClientListBackendEnvironmentsResponsebackendEnvironmentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListBackendEnvironmentsResponseTypeDef(_ClientListBackendEnvironmentsResponseTypeDef):
    """
    - *(dict) --*

      Result structure for list backend environments result.
      - **backendEnvironments** *(list) --*

        List of backend environments for an Amplify App.
        - *(dict) --*

          Backend environment for an Amplify App.
          - **backendEnvironmentArn** *(string) --*

            Arn for a backend environment, part of an Amplify App.
    """


_ClientListBranchesResponsebranchesTypeDef = TypedDict(
    "_ClientListBranchesResponsebranchesTypeDef",
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


class ClientListBranchesResponsebranchesTypeDef(_ClientListBranchesResponsebranchesTypeDef):
    """
    - *(dict) --*

      Branch for an Amplify App, which maps to a 3rd party repository branch.
      - **branchArn** *(string) --*

        ARN for a branch, part of an Amplify App.
    """


_ClientListBranchesResponseTypeDef = TypedDict(
    "_ClientListBranchesResponseTypeDef",
    {"branches": List[ClientListBranchesResponsebranchesTypeDef], "nextToken": str},
    total=False,
)


class ClientListBranchesResponseTypeDef(_ClientListBranchesResponseTypeDef):
    """
    - *(dict) --*

      Result structure for list branches request.
      - **branches** *(list) --*

        List of branches for an Amplify App.
        - *(dict) --*

          Branch for an Amplify App, which maps to a 3rd party repository branch.
          - **branchArn** *(string) --*

            ARN for a branch, part of an Amplify App.
    """


_ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef = TypedDict(
    "_ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef(
    _ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef
):
    pass


_ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef = TypedDict(
    "_ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef",
    {
        "subDomainSetting": ClientListDomainAssociationsResponsedomainAssociationssubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef(
    _ClientListDomainAssociationsResponsedomainAssociationssubDomainsTypeDef
):
    pass


_ClientListDomainAssociationsResponsedomainAssociationsTypeDef = TypedDict(
    "_ClientListDomainAssociationsResponsedomainAssociationsTypeDef",
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


class ClientListDomainAssociationsResponsedomainAssociationsTypeDef(
    _ClientListDomainAssociationsResponsedomainAssociationsTypeDef
):
    """
    - *(dict) --*

      Structure for Domain Association, which associates a custom domain with an Amplify App.
      - **domainAssociationArn** *(string) --*

        ARN for the Domain Association.
    """


_ClientListDomainAssociationsResponseTypeDef = TypedDict(
    "_ClientListDomainAssociationsResponseTypeDef",
    {
        "domainAssociations": List[ClientListDomainAssociationsResponsedomainAssociationsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListDomainAssociationsResponseTypeDef(_ClientListDomainAssociationsResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the list Domain Association request.
      - **domainAssociations** *(list) --*

        List of Domain Associations.
        - *(dict) --*

          Structure for Domain Association, which associates a custom domain with an Amplify App.
          - **domainAssociationArn** *(string) --*

            ARN for the Domain Association.
    """


_ClientListJobsResponsejobSummariesTypeDef = TypedDict(
    "_ClientListJobsResponsejobSummariesTypeDef",
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


class ClientListJobsResponsejobSummariesTypeDef(_ClientListJobsResponsejobSummariesTypeDef):
    """
    - *(dict) --*

      Structure for the summary of a Job.
      - **jobArn** *(string) --*

        Arn for the Job.
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"jobSummaries": List[ClientListJobsResponsejobSummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    - *(dict) --*

      Maximum number of records to list in a single response.
      - **jobSummaries** *(list) --*

        Result structure for list job result request.
        - *(dict) --*

          Structure for the summary of a Job.
          - **jobArn** *(string) --*

            Arn for the Job.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      Response for list tags.
      - **tags** *(dict) --*

        Tags result for response.
        - *(string) --*

          - *(string) --*
    """


_ClientListWebhooksResponsewebhooksTypeDef = TypedDict(
    "_ClientListWebhooksResponsewebhooksTypeDef",
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


class ClientListWebhooksResponsewebhooksTypeDef(_ClientListWebhooksResponsewebhooksTypeDef):
    """
    - *(dict) --*

      Structure for webhook, which associates a webhook with an Amplify App.
      - **webhookArn** *(string) --*

        ARN for the webhook.
    """


_ClientListWebhooksResponseTypeDef = TypedDict(
    "_ClientListWebhooksResponseTypeDef",
    {"webhooks": List[ClientListWebhooksResponsewebhooksTypeDef], "nextToken": str},
    total=False,
)


class ClientListWebhooksResponseTypeDef(_ClientListWebhooksResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the list webhooks request.
      - **webhooks** *(list) --*

        List of webhooks.
        - *(dict) --*

          Structure for webhook, which associates a webhook with an Amplify App.
          - **webhookArn** *(string) --*

            ARN for the webhook.
    """


_ClientStartDeploymentResponsejobSummaryTypeDef = TypedDict(
    "_ClientStartDeploymentResponsejobSummaryTypeDef",
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


class ClientStartDeploymentResponsejobSummaryTypeDef(
    _ClientStartDeploymentResponsejobSummaryTypeDef
):
    """
    - **jobSummary** *(dict) --*

      Summary for the Job.
      - **jobArn** *(string) --*

        Arn for the Job.
    """


_ClientStartDeploymentResponseTypeDef = TypedDict(
    "_ClientStartDeploymentResponseTypeDef",
    {"jobSummary": ClientStartDeploymentResponsejobSummaryTypeDef},
    total=False,
)


class ClientStartDeploymentResponseTypeDef(_ClientStartDeploymentResponseTypeDef):
    """
    - *(dict) --*

      Result structure for start a deployment.
      - **jobSummary** *(dict) --*

        Summary for the Job.
        - **jobArn** *(string) --*

          Arn for the Job.
    """


_ClientStartJobResponsejobSummaryTypeDef = TypedDict(
    "_ClientStartJobResponsejobSummaryTypeDef",
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


class ClientStartJobResponsejobSummaryTypeDef(_ClientStartJobResponsejobSummaryTypeDef):
    """
    - **jobSummary** *(dict) --*

      Summary for the Job.
      - **jobArn** *(string) --*

        Arn for the Job.
    """


_ClientStartJobResponseTypeDef = TypedDict(
    "_ClientStartJobResponseTypeDef",
    {"jobSummary": ClientStartJobResponsejobSummaryTypeDef},
    total=False,
)


class ClientStartJobResponseTypeDef(_ClientStartJobResponseTypeDef):
    """
    - *(dict) --*

      Result structure for run job request.
      - **jobSummary** *(dict) --*

        Summary for the Job.
        - **jobArn** *(string) --*

          Arn for the Job.
    """


_ClientStopJobResponsejobSummaryTypeDef = TypedDict(
    "_ClientStopJobResponsejobSummaryTypeDef",
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


class ClientStopJobResponsejobSummaryTypeDef(_ClientStopJobResponsejobSummaryTypeDef):
    """
    - **jobSummary** *(dict) --*

      Summary for the Job.
      - **jobArn** *(string) --*

        Arn for the Job.
    """


_ClientStopJobResponseTypeDef = TypedDict(
    "_ClientStopJobResponseTypeDef",
    {"jobSummary": ClientStopJobResponsejobSummaryTypeDef},
    total=False,
)


class ClientStopJobResponseTypeDef(_ClientStopJobResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the stop job request.
      - **jobSummary** *(dict) --*

        Summary for the Job.
        - **jobArn** *(string) --*

          Arn for the Job.
    """


_ClientUpdateAppAutoBranchCreationConfigTypeDef = TypedDict(
    "_ClientUpdateAppAutoBranchCreationConfigTypeDef",
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


class ClientUpdateAppAutoBranchCreationConfigTypeDef(
    _ClientUpdateAppAutoBranchCreationConfigTypeDef
):
    """
    Automated branch creation branchConfig for the Amplify App.
    - **stage** *(string) --*

      Stage for the auto created branch.
    """


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
    """
    - *(dict) --*

      Custom rewrite / redirect rule.
      - **source** *(string) --***[REQUIRED]**

        The source pattern for a URL rewrite or redirect rule.
    """


_ClientUpdateAppResponseappautoBranchCreationConfigTypeDef = TypedDict(
    "_ClientUpdateAppResponseappautoBranchCreationConfigTypeDef",
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


class ClientUpdateAppResponseappautoBranchCreationConfigTypeDef(
    _ClientUpdateAppResponseappautoBranchCreationConfigTypeDef
):
    pass


_ClientUpdateAppResponseappcustomRulesTypeDef = TypedDict(
    "_ClientUpdateAppResponseappcustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ClientUpdateAppResponseappcustomRulesTypeDef(_ClientUpdateAppResponseappcustomRulesTypeDef):
    pass


_ClientUpdateAppResponseappproductionBranchTypeDef = TypedDict(
    "_ClientUpdateAppResponseappproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ClientUpdateAppResponseappproductionBranchTypeDef(
    _ClientUpdateAppResponseappproductionBranchTypeDef
):
    pass


_ClientUpdateAppResponseappTypeDef = TypedDict(
    "_ClientUpdateAppResponseappTypeDef",
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


class ClientUpdateAppResponseappTypeDef(_ClientUpdateAppResponseappTypeDef):
    """
    - **app** *(dict) --*

      App structure for the updated App.
      - **appId** *(string) --*

        Unique Id for the Amplify App.
    """


_ClientUpdateAppResponseTypeDef = TypedDict(
    "_ClientUpdateAppResponseTypeDef", {"app": ClientUpdateAppResponseappTypeDef}, total=False
)


class ClientUpdateAppResponseTypeDef(_ClientUpdateAppResponseTypeDef):
    """
    - *(dict) --*

      Result structure for an Amplify App update request.
      - **app** *(dict) --*

        App structure for the updated App.
        - **appId** *(string) --*

          Unique Id for the Amplify App.
    """


_ClientUpdateBranchResponsebranchTypeDef = TypedDict(
    "_ClientUpdateBranchResponsebranchTypeDef",
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


class ClientUpdateBranchResponsebranchTypeDef(_ClientUpdateBranchResponsebranchTypeDef):
    """
    - **branch** *(dict) --*

      Branch structure for an Amplify App.
      - **branchArn** *(string) --*

        ARN for a branch, part of an Amplify App.
    """


_ClientUpdateBranchResponseTypeDef = TypedDict(
    "_ClientUpdateBranchResponseTypeDef",
    {"branch": ClientUpdateBranchResponsebranchTypeDef},
    total=False,
)


class ClientUpdateBranchResponseTypeDef(_ClientUpdateBranchResponseTypeDef):
    """
    - *(dict) --*

      Result structure for update branch request.
      - **branch** *(dict) --*

        Branch structure for an Amplify App.
        - **branchArn** *(string) --*

          ARN for a branch, part of an Amplify App.
    """


_ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef = TypedDict(
    "_ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef(
    _ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef
):
    pass


_ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef = TypedDict(
    "_ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef",
    {
        "subDomainSetting": ClientUpdateDomainAssociationResponsedomainAssociationsubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef(
    _ClientUpdateDomainAssociationResponsedomainAssociationsubDomainsTypeDef
):
    pass


_ClientUpdateDomainAssociationResponsedomainAssociationTypeDef = TypedDict(
    "_ClientUpdateDomainAssociationResponsedomainAssociationTypeDef",
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


class ClientUpdateDomainAssociationResponsedomainAssociationTypeDef(
    _ClientUpdateDomainAssociationResponsedomainAssociationTypeDef
):
    """
    - **domainAssociation** *(dict) --*

      Domain Association structure.
      - **domainAssociationArn** *(string) --*

        ARN for the Domain Association.
    """


_ClientUpdateDomainAssociationResponseTypeDef = TypedDict(
    "_ClientUpdateDomainAssociationResponseTypeDef",
    {"domainAssociation": ClientUpdateDomainAssociationResponsedomainAssociationTypeDef},
    total=False,
)


class ClientUpdateDomainAssociationResponseTypeDef(_ClientUpdateDomainAssociationResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the update Domain Association request.
      - **domainAssociation** *(dict) --*

        Domain Association structure.
        - **domainAssociationArn** *(string) --*

          ARN for the Domain Association.
    """


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
    """
    - *(dict) --*

      Setting for the Subdomain.
      - **prefix** *(string) --***[REQUIRED]**

        Prefix setting for the Subdomain.
    """


_ClientUpdateWebhookResponsewebhookTypeDef = TypedDict(
    "_ClientUpdateWebhookResponsewebhookTypeDef",
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


class ClientUpdateWebhookResponsewebhookTypeDef(_ClientUpdateWebhookResponsewebhookTypeDef):
    """
    - **webhook** *(dict) --*

      Webhook structure.
      - **webhookArn** *(string) --*

        ARN for the webhook.
    """


_ClientUpdateWebhookResponseTypeDef = TypedDict(
    "_ClientUpdateWebhookResponseTypeDef",
    {"webhook": ClientUpdateWebhookResponsewebhookTypeDef},
    total=False,
)


class ClientUpdateWebhookResponseTypeDef(_ClientUpdateWebhookResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the update webhook request.
      - **webhook** *(dict) --*

        Webhook structure.
        - **webhookArn** *(string) --*

          ARN for the webhook.
    """


_ListAppsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAppsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAppsPaginatePaginationConfigTypeDef(_ListAppsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef = TypedDict(
    "_ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef",
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


class ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef(
    _ListAppsPaginateResponseappsautoBranchCreationConfigTypeDef
):
    pass


_ListAppsPaginateResponseappscustomRulesTypeDef = TypedDict(
    "_ListAppsPaginateResponseappscustomRulesTypeDef",
    {"source": str, "target": str, "status": str, "condition": str},
    total=False,
)


class ListAppsPaginateResponseappscustomRulesTypeDef(
    _ListAppsPaginateResponseappscustomRulesTypeDef
):
    pass


_ListAppsPaginateResponseappsproductionBranchTypeDef = TypedDict(
    "_ListAppsPaginateResponseappsproductionBranchTypeDef",
    {"lastDeployTime": datetime, "status": str, "thumbnailUrl": str, "branchName": str},
    total=False,
)


class ListAppsPaginateResponseappsproductionBranchTypeDef(
    _ListAppsPaginateResponseappsproductionBranchTypeDef
):
    pass


_ListAppsPaginateResponseappsTypeDef = TypedDict(
    "_ListAppsPaginateResponseappsTypeDef",
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


class ListAppsPaginateResponseappsTypeDef(_ListAppsPaginateResponseappsTypeDef):
    """
    - *(dict) --*

      Amplify App represents different branches of a repository for building, deploying, and
      hosting.
      - **appId** *(string) --*

        Unique Id for the Amplify App.
    """


_ListAppsPaginateResponseTypeDef = TypedDict(
    "_ListAppsPaginateResponseTypeDef",
    {"apps": List[ListAppsPaginateResponseappsTypeDef], "NextToken": str},
    total=False,
)


class ListAppsPaginateResponseTypeDef(_ListAppsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Result structure for an Amplify App list request.
      - **apps** *(list) --*

        List of Amplify Apps.
        - *(dict) --*

          Amplify App represents different branches of a repository for building, deploying, and
          hosting.
          - **appId** *(string) --*

            Unique Id for the Amplify App.
    """


_ListBranchesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBranchesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBranchesPaginatePaginationConfigTypeDef(_ListBranchesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBranchesPaginateResponsebranchesTypeDef = TypedDict(
    "_ListBranchesPaginateResponsebranchesTypeDef",
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


class ListBranchesPaginateResponsebranchesTypeDef(_ListBranchesPaginateResponsebranchesTypeDef):
    """
    - *(dict) --*

      Branch for an Amplify App, which maps to a 3rd party repository branch.
      - **branchArn** *(string) --*

        ARN for a branch, part of an Amplify App.
    """


_ListBranchesPaginateResponseTypeDef = TypedDict(
    "_ListBranchesPaginateResponseTypeDef",
    {"branches": List[ListBranchesPaginateResponsebranchesTypeDef], "NextToken": str},
    total=False,
)


class ListBranchesPaginateResponseTypeDef(_ListBranchesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Result structure for list branches request.
      - **branches** *(list) --*

        List of branches for an Amplify App.
        - *(dict) --*

          Branch for an Amplify App, which maps to a 3rd party repository branch.
          - **branchArn** *(string) --*

            ARN for a branch, part of an Amplify App.
    """


_ListDomainAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDomainAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDomainAssociationsPaginatePaginationConfigTypeDef(
    _ListDomainAssociationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef = TypedDict(
    "_ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef",
    {"prefix": str, "branchName": str},
    total=False,
)


class ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef(
    _ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef
):
    pass


_ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef = TypedDict(
    "_ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef",
    {
        "subDomainSetting": ListDomainAssociationsPaginateResponsedomainAssociationssubDomainssubDomainSettingTypeDef,
        "verified": bool,
        "dnsRecord": str,
    },
    total=False,
)


class ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef(
    _ListDomainAssociationsPaginateResponsedomainAssociationssubDomainsTypeDef
):
    pass


_ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef = TypedDict(
    "_ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef",
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


class ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef(
    _ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef
):
    """
    - *(dict) --*

      Structure for Domain Association, which associates a custom domain with an Amplify App.
      - **domainAssociationArn** *(string) --*

        ARN for the Domain Association.
    """


_ListDomainAssociationsPaginateResponseTypeDef = TypedDict(
    "_ListDomainAssociationsPaginateResponseTypeDef",
    {
        "domainAssociations": List[ListDomainAssociationsPaginateResponsedomainAssociationsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListDomainAssociationsPaginateResponseTypeDef(_ListDomainAssociationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Result structure for the list Domain Association request.
      - **domainAssociations** *(list) --*

        List of Domain Associations.
        - *(dict) --*

          Structure for Domain Association, which associates a custom domain with an Amplify App.
          - **domainAssociationArn** *(string) --*

            ARN for the Domain Association.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobsPaginateResponsejobSummariesTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobSummariesTypeDef",
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


class ListJobsPaginateResponsejobSummariesTypeDef(_ListJobsPaginateResponsejobSummariesTypeDef):
    """
    - *(dict) --*

      Structure for the summary of a Job.
      - **jobArn** *(string) --*

        Arn for the Job.
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {"jobSummaries": List[ListJobsPaginateResponsejobSummariesTypeDef], "NextToken": str},
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Maximum number of records to list in a single response.
      - **jobSummaries** *(list) --*

        Result structure for list job result request.
        - *(dict) --*

          Structure for the summary of a Job.
          - **jobArn** *(string) --*

            Arn for the Job.
    """
