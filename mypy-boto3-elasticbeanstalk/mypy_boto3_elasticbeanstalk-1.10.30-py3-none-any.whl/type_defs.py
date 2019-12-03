"Main interface for elasticbeanstalk service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientApplyEnvironmentManagedActionResponseTypeDef",
    "ClientCheckDnsAvailabilityResponseTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsTypeDef",
    "ClientComposeEnvironmentsResponseTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    "ClientCreateApplicationResponseApplicationTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationTagsTypeDef",
    "ClientCreateApplicationVersionBuildConfigurationTypeDef",
    "ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    "ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    "ClientCreateApplicationVersionResponseApplicationVersionTypeDef",
    "ClientCreateApplicationVersionResponseTypeDef",
    "ClientCreateApplicationVersionSourceBuildInformationTypeDef",
    "ClientCreateApplicationVersionSourceBundleTypeDef",
    "ClientCreateApplicationVersionTagsTypeDef",
    "ClientCreateConfigurationTemplateOptionSettingsTypeDef",
    "ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef",
    "ClientCreateConfigurationTemplateResponseTypeDef",
    "ClientCreateConfigurationTemplateSourceConfigurationTypeDef",
    "ClientCreateConfigurationTemplateTagsTypeDef",
    "ClientCreateEnvironmentOptionSettingsTypeDef",
    "ClientCreateEnvironmentOptionsToRemoveTypeDef",
    "ClientCreateEnvironmentResponseEnvironmentLinksTypeDef",
    "ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    "ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef",
    "ClientCreateEnvironmentResponseResourcesTypeDef",
    "ClientCreateEnvironmentResponseTierTypeDef",
    "ClientCreateEnvironmentResponseTypeDef",
    "ClientCreateEnvironmentTagsTypeDef",
    "ClientCreateEnvironmentTierTypeDef",
    "ClientCreatePlatformVersionOptionSettingsTypeDef",
    "ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef",
    "ClientCreatePlatformVersionResponseBuilderTypeDef",
    "ClientCreatePlatformVersionResponsePlatformSummaryTypeDef",
    "ClientCreatePlatformVersionResponseTypeDef",
    "ClientCreatePlatformVersionTagsTypeDef",
    "ClientCreateStorageLocationResponseTypeDef",
    "ClientDeletePlatformVersionResponsePlatformSummaryTypeDef",
    "ClientDeletePlatformVersionResponseTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef",
    "ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef",
    "ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef",
    "ClientDescribeApplicationVersionsResponseTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef",
    "ClientDescribeApplicationsResponseApplicationsTypeDef",
    "ClientDescribeApplicationsResponseTypeDef",
    "ClientDescribeConfigurationOptionsOptionsTypeDef",
    "ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef",
    "ClientDescribeConfigurationOptionsResponseOptionsTypeDef",
    "ClientDescribeConfigurationOptionsResponseTypeDef",
    "ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef",
    "ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef",
    "ClientDescribeConfigurationSettingsResponseTypeDef",
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef",
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef",
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef",
    "ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef",
    "ClientDescribeEnvironmentHealthResponseTypeDef",
    "ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef",
    "ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef",
    "ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef",
    "ClientDescribeEnvironmentManagedActionsResponseTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsTypeDef",
    "ClientDescribeEnvironmentsResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef",
    "ClientDescribeInstancesHealthResponseTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef",
    "ClientDescribePlatformVersionResponseTypeDef",
    "ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef",
    "ClientListAvailableSolutionStacksResponseTypeDef",
    "ClientListPlatformVersionsFiltersTypeDef",
    "ClientListPlatformVersionsResponsePlatformSummaryListTypeDef",
    "ClientListPlatformVersionsResponseTypeDef",
    "ClientListTagsForResourceResponseResourceTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef",
    "ClientRetrieveEnvironmentInfoResponseTypeDef",
    "ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef",
    "ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    "ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef",
    "ClientTerminateEnvironmentResponseResourcesTypeDef",
    "ClientTerminateEnvironmentResponseTierTypeDef",
    "ClientTerminateEnvironmentResponseTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    "ClientUpdateApplicationResponseApplicationTypeDef",
    "ClientUpdateApplicationResponseTypeDef",
    "ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    "ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    "ClientUpdateApplicationVersionResponseApplicationVersionTypeDef",
    "ClientUpdateApplicationVersionResponseTypeDef",
    "ClientUpdateConfigurationTemplateOptionSettingsTypeDef",
    "ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef",
    "ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef",
    "ClientUpdateConfigurationTemplateResponseTypeDef",
    "ClientUpdateEnvironmentOptionSettingsTypeDef",
    "ClientUpdateEnvironmentOptionsToRemoveTypeDef",
    "ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef",
    "ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    "ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef",
    "ClientUpdateEnvironmentResponseResourcesTypeDef",
    "ClientUpdateEnvironmentResponseTierTypeDef",
    "ClientUpdateEnvironmentResponseTypeDef",
    "ClientUpdateEnvironmentTierTypeDef",
    "ClientUpdateTagsForResourceTagsToAddTypeDef",
    "ClientValidateConfigurationSettingsOptionSettingsTypeDef",
    "ClientValidateConfigurationSettingsResponseMessagesTypeDef",
    "ClientValidateConfigurationSettingsResponseTypeDef",
    "DescribeApplicationVersionsPaginatePaginationConfigTypeDef",
    "DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef",
    "DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef",
    "DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef",
    "DescribeApplicationVersionsPaginateResponseTypeDef",
    "DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef",
    "DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef",
    "DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef",
    "DescribeEnvironmentsPaginatePaginationConfigTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef",
    "DescribeEnvironmentsPaginateResponseTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "ListPlatformVersionsPaginateFiltersTypeDef",
    "ListPlatformVersionsPaginatePaginationConfigTypeDef",
    "ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef",
    "ListPlatformVersionsPaginateResponseTypeDef",
)


_ClientApplyEnvironmentManagedActionResponseTypeDef = TypedDict(
    "_ClientApplyEnvironmentManagedActionResponseTypeDef",
    {
        "ActionId": str,
        "ActionDescription": str,
        "ActionType": Literal["InstanceRefresh", "PlatformUpdate", "Unknown"],
        "Status": str,
    },
    total=False,
)


class ClientApplyEnvironmentManagedActionResponseTypeDef(
    _ClientApplyEnvironmentManagedActionResponseTypeDef
):
    """
    - *(dict) --*

      The result message containing information about the managed action.
      - **ActionId** *(string) --*

        The action ID of the managed action.
    """


_ClientCheckDnsAvailabilityResponseTypeDef = TypedDict(
    "_ClientCheckDnsAvailabilityResponseTypeDef",
    {"Available": bool, "FullyQualifiedCNAME": str},
    total=False,
)


class ClientCheckDnsAvailabilityResponseTypeDef(_ClientCheckDnsAvailabilityResponseTypeDef):
    """
    - *(dict) --*

      Indicates if the specified CNAME is available.
      - **Available** *(boolean) --*

        Indicates if the specified CNAME is available:
        * ``true`` : The CNAME is available.
        * ``false`` : The CNAME is not available.
    """


_ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef
):
    pass


_ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
):
    pass


_ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef
):
    pass


_ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    {"LoadBalancer": ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef},
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef
):
    pass


_ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef
):
    pass


_ClientComposeEnvironmentsResponseEnvironmentsTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef,
        "Tier": ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef,
        "EnvironmentLinks": List[
            ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsTypeDef
):
    """
    - *(dict) --*

      Describes the properties of an environment.
      - **EnvironmentName** *(string) --*

        The name of this environment.
    """


_ClientComposeEnvironmentsResponseTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseTypeDef",
    {"Environments": List[ClientComposeEnvironmentsResponseEnvironmentsTypeDef], "NextToken": str},
    total=False,
)


class ClientComposeEnvironmentsResponseTypeDef(_ClientComposeEnvironmentsResponseTypeDef):
    """
    - *(dict) --*

      Result message containing a list of environment descriptions.
      - **Environments** *(list) --*

        Returns an  EnvironmentDescription list.
        - *(dict) --*

          Describes the properties of an environment.
          - **EnvironmentName** *(string) --*

            The name of this environment.
    """


_ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef
):
    pass


_ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef
):
    pass


_ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    pass


_ClientCreateApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientCreateApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResourceLifecycleConfigTypeDef(
    _ClientCreateApplicationResourceLifecycleConfigTypeDef
):
    """
    Specify an application resource lifecycle configuration to prevent your application from
    accumulating too many versions.
    - **ServiceRole** *(string) --*

      The ARN of an IAM service role that Elastic Beanstalk has permission to assume.
      The ``ServiceRole`` property is required the first time that you provide a
      ``VersionLifecycleConfig`` for the application in one of the supporting calls
      (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it once,
      in either one of the calls, Elastic Beanstalk persists the Service Role with the application,
      and you don't need to specify it again in subsequent ``UpdateApplicationResourceLifecycle``
      calls. You can, however, specify it in subsequent calls to change the Service Role to another
      value.
    """


_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef
):
    pass


_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef
):
    pass


_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    pass


_ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef(
    _ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef
):
    pass


_ClientCreateApplicationResponseApplicationTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationTypeDef(
    _ClientCreateApplicationResponseApplicationTypeDef
):
    """
    - **Application** *(dict) --*

      The  ApplicationDescription of the application.
      - **ApplicationArn** *(string) --*

        The Amazon Resource Name (ARN) of the application.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef",
    {"Application": ClientCreateApplicationResponseApplicationTypeDef},
    total=False,
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    - *(dict) --*

      Result message containing a single description of an application.
      - **Application** *(dict) --*

        The  ApplicationDescription of the application.
        - **ApplicationArn** *(string) --*

          The Amazon Resource Name (ARN) of the application.
    """


_ClientCreateApplicationTagsTypeDef = TypedDict(
    "_ClientCreateApplicationTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateApplicationTagsTypeDef(_ClientCreateApplicationTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag applied to a resource in an environment.
      - **Key** *(string) --*

        The key of the tag.
    """


_ClientCreateApplicationVersionBuildConfigurationTypeDef = TypedDict(
    "_ClientCreateApplicationVersionBuildConfigurationTypeDef",
    {
        "ArtifactName": str,
        "CodeBuildServiceRole": str,
        "ComputeType": Literal[
            "BUILD_GENERAL1_SMALL", "BUILD_GENERAL1_MEDIUM", "BUILD_GENERAL1_LARGE"
        ],
        "Image": str,
        "TimeoutInMinutes": int,
    },
    total=False,
)


class ClientCreateApplicationVersionBuildConfigurationTypeDef(
    _ClientCreateApplicationVersionBuildConfigurationTypeDef
):
    """
    Settings for an AWS CodeBuild build.
    - **ArtifactName** *(string) --*

      The name of the artifact of the CodeBuild build. If provided, Elastic Beanstalk stores the
      build artifact in the S3 location *S3-bucket* /resources/*application-name*
      /codebuild/codebuild-*version-label* -*artifact-name* .zip. If not provided, Elastic Beanstalk
      stores the build artifact in the S3 location *S3-bucket* /resources/*application-name*
      /codebuild/codebuild-*version-label* .zip.
    """


_ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    {
        "SourceType": Literal["Git", "Zip"],
        "SourceRepository": Literal["CodeCommit", "S3"],
        "SourceLocation": str,
    },
    total=False,
)


class ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef(
    _ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef
):
    pass


_ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef(
    _ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef
):
    pass


_ClientCreateApplicationVersionResponseApplicationVersionTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseApplicationVersionTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Processed", "Unprocessed", "Failed", "Processing", "Building"],
    },
    total=False,
)


class ClientCreateApplicationVersionResponseApplicationVersionTypeDef(
    _ClientCreateApplicationVersionResponseApplicationVersionTypeDef
):
    """
    - **ApplicationVersion** *(dict) --*

      The  ApplicationVersionDescription of the application version.
      - **ApplicationVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the application version.
    """


_ClientCreateApplicationVersionResponseTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseTypeDef",
    {"ApplicationVersion": ClientCreateApplicationVersionResponseApplicationVersionTypeDef},
    total=False,
)


class ClientCreateApplicationVersionResponseTypeDef(_ClientCreateApplicationVersionResponseTypeDef):
    """
    - *(dict) --*

      Result message wrapping a single description of an application version.
      - **ApplicationVersion** *(dict) --*

        The  ApplicationVersionDescription of the application version.
        - **ApplicationVersionArn** *(string) --*

          The Amazon Resource Name (ARN) of the application version.
    """


_RequiredClientCreateApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "_RequiredClientCreateApplicationVersionSourceBuildInformationTypeDef",
    {"SourceType": Literal["Git", "Zip"]},
)
_OptionalClientCreateApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "_OptionalClientCreateApplicationVersionSourceBuildInformationTypeDef",
    {"SourceRepository": Literal["CodeCommit", "S3"], "SourceLocation": str},
    total=False,
)


class ClientCreateApplicationVersionSourceBuildInformationTypeDef(
    _RequiredClientCreateApplicationVersionSourceBuildInformationTypeDef,
    _OptionalClientCreateApplicationVersionSourceBuildInformationTypeDef,
):
    """
    Specify a commit in an AWS CodeCommit Git repository to use as the source code for the
    application version.
    - **SourceType** *(string) --***[REQUIRED]**

      The type of repository.
      * ``Git``
      * ``Zip``
    """


_ClientCreateApplicationVersionSourceBundleTypeDef = TypedDict(
    "_ClientCreateApplicationVersionSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientCreateApplicationVersionSourceBundleTypeDef(
    _ClientCreateApplicationVersionSourceBundleTypeDef
):
    """
    The Amazon S3 bucket and key that identify the location of the source bundle for this version.
    .. note::

      The Amazon S3 bucket must be in the same region as the environment.
    """


_ClientCreateApplicationVersionTagsTypeDef = TypedDict(
    "_ClientCreateApplicationVersionTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateApplicationVersionTagsTypeDef(_ClientCreateApplicationVersionTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag applied to a resource in an environment.
      - **Key** *(string) --*

        The key of the tag.
    """


_ClientCreateConfigurationTemplateOptionSettingsTypeDef = TypedDict(
    "_ClientCreateConfigurationTemplateOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientCreateConfigurationTemplateOptionSettingsTypeDef(
    _ClientCreateConfigurationTemplateOptionSettingsTypeDef
):
    """
    - *(dict) --*

      A specification identifying an individual configuration option along with its current value.
      For a list of possible option values, go to `Option Values
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
      Elastic Beanstalk Developer Guide* .
      - **ResourceName** *(string) --*

        A unique resource name for a time-based scaling configuration option.
    """


_ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef = TypedDict(
    "_ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef(
    _ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef
):
    pass


_ClientCreateConfigurationTemplateResponseTypeDef = TypedDict(
    "_ClientCreateConfigurationTemplateResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": Literal["deployed", "pending", "failed"],
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List[ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef],
    },
    total=False,
)


class ClientCreateConfigurationTemplateResponseTypeDef(
    _ClientCreateConfigurationTemplateResponseTypeDef
):
    """
    - *(dict) --*

      Describes the settings for a configuration set.
      - **SolutionStackName** *(string) --*

        The name of the solution stack this configuration set uses.
    """


_ClientCreateConfigurationTemplateSourceConfigurationTypeDef = TypedDict(
    "_ClientCreateConfigurationTemplateSourceConfigurationTypeDef",
    {"ApplicationName": str, "TemplateName": str},
    total=False,
)


class ClientCreateConfigurationTemplateSourceConfigurationTypeDef(
    _ClientCreateConfigurationTemplateSourceConfigurationTypeDef
):
    """
    If specified, AWS Elastic Beanstalk uses the configuration values from the specified
    configuration template to create a new configuration.
    Values specified in the ``OptionSettings`` parameter of this call overrides any values obtained
    from the ``SourceConfiguration`` .
    If no configuration template is found, returns an ``InvalidParameterValue`` error.
    Constraint: If both the solution stack name parameter and the source configuration parameters
    are specified, the solution stack of the source configuration template must match the specified
    solution stack name or else AWS Elastic Beanstalk returns an ``InvalidParameterCombination``
    error.
    - **ApplicationName** *(string) --*

      The name of the application associated with the configuration.
    """


_ClientCreateConfigurationTemplateTagsTypeDef = TypedDict(
    "_ClientCreateConfigurationTemplateTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateConfigurationTemplateTagsTypeDef(_ClientCreateConfigurationTemplateTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag applied to a resource in an environment.
      - **Key** *(string) --*

        The key of the tag.
    """


_ClientCreateEnvironmentOptionSettingsTypeDef = TypedDict(
    "_ClientCreateEnvironmentOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientCreateEnvironmentOptionSettingsTypeDef(_ClientCreateEnvironmentOptionSettingsTypeDef):
    """
    - *(dict) --*

      A specification identifying an individual configuration option along with its current value.
      For a list of possible option values, go to `Option Values
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
      Elastic Beanstalk Developer Guide* .
      - **ResourceName** *(string) --*

        A unique resource name for a time-based scaling configuration option.
    """


_ClientCreateEnvironmentOptionsToRemoveTypeDef = TypedDict(
    "_ClientCreateEnvironmentOptionsToRemoveTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)


class ClientCreateEnvironmentOptionsToRemoveTypeDef(_ClientCreateEnvironmentOptionsToRemoveTypeDef):
    """
    - *(dict) --*

      A specification identifying an individual configuration option.
      - **ResourceName** *(string) --*

        A unique resource name for a time-based scaling configuration option.
    """


_ClientCreateEnvironmentResponseEnvironmentLinksTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class ClientCreateEnvironmentResponseEnvironmentLinksTypeDef(
    _ClientCreateEnvironmentResponseEnvironmentLinksTypeDef
):
    pass


_ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef(
    _ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef
):
    pass


_ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef],
    },
    total=False,
)


class ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef(
    _ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef
):
    pass


_ClientCreateEnvironmentResponseResourcesTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseResourcesTypeDef",
    {"LoadBalancer": ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef},
    total=False,
)


class ClientCreateEnvironmentResponseResourcesTypeDef(
    _ClientCreateEnvironmentResponseResourcesTypeDef
):
    pass


_ClientCreateEnvironmentResponseTierTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientCreateEnvironmentResponseTierTypeDef(_ClientCreateEnvironmentResponseTierTypeDef):
    pass


_ClientCreateEnvironmentResponseTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": ClientCreateEnvironmentResponseResourcesTypeDef,
        "Tier": ClientCreateEnvironmentResponseTierTypeDef,
        "EnvironmentLinks": List[ClientCreateEnvironmentResponseEnvironmentLinksTypeDef],
        "EnvironmentArn": str,
    },
    total=False,
)


class ClientCreateEnvironmentResponseTypeDef(_ClientCreateEnvironmentResponseTypeDef):
    """
    - *(dict) --*

      Describes the properties of an environment.
      - **EnvironmentName** *(string) --*

        The name of this environment.
    """


_ClientCreateEnvironmentTagsTypeDef = TypedDict(
    "_ClientCreateEnvironmentTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateEnvironmentTagsTypeDef(_ClientCreateEnvironmentTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag applied to a resource in an environment.
      - **Key** *(string) --*

        The key of the tag.
    """


_ClientCreateEnvironmentTierTypeDef = TypedDict(
    "_ClientCreateEnvironmentTierTypeDef", {"Name": str, "Type": str, "Version": str}, total=False
)


class ClientCreateEnvironmentTierTypeDef(_ClientCreateEnvironmentTierTypeDef):
    """
    This specifies the tier to use for creating this environment.
    - **Name** *(string) --*

      The name of this environment tier.
      Valid values:
      * For *Web server tier* – ``WebServer``
      * For *Worker tier* – ``Worker``
    """


_ClientCreatePlatformVersionOptionSettingsTypeDef = TypedDict(
    "_ClientCreatePlatformVersionOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientCreatePlatformVersionOptionSettingsTypeDef(
    _ClientCreatePlatformVersionOptionSettingsTypeDef
):
    """
    - *(dict) --*

      A specification identifying an individual configuration option along with its current value.
      For a list of possible option values, go to `Option Values
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
      Elastic Beanstalk Developer Guide* .
      - **ResourceName** *(string) --*

        A unique resource name for a time-based scaling configuration option.
    """


_ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef = TypedDict(
    "_ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef(
    _ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef
):
    """
    The location of the platform definition archive in Amazon S3.
    - **S3Bucket** *(string) --*

      The Amazon S3 bucket where the data is located.
    """


_ClientCreatePlatformVersionResponseBuilderTypeDef = TypedDict(
    "_ClientCreatePlatformVersionResponseBuilderTypeDef", {"ARN": str}, total=False
)


class ClientCreatePlatformVersionResponseBuilderTypeDef(
    _ClientCreatePlatformVersionResponseBuilderTypeDef
):
    pass


_ClientCreatePlatformVersionResponsePlatformSummaryTypeDef = TypedDict(
    "_ClientCreatePlatformVersionResponsePlatformSummaryTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": Literal["Creating", "Failed", "Ready", "Deleting", "Deleted"],
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)


class ClientCreatePlatformVersionResponsePlatformSummaryTypeDef(
    _ClientCreatePlatformVersionResponsePlatformSummaryTypeDef
):
    """
    - **PlatformSummary** *(dict) --*

      Detailed information about the new version of the custom platform.
      - **PlatformArn** *(string) --*

        The ARN of the platform.
    """


_ClientCreatePlatformVersionResponseTypeDef = TypedDict(
    "_ClientCreatePlatformVersionResponseTypeDef",
    {
        "PlatformSummary": ClientCreatePlatformVersionResponsePlatformSummaryTypeDef,
        "Builder": ClientCreatePlatformVersionResponseBuilderTypeDef,
    },
    total=False,
)


class ClientCreatePlatformVersionResponseTypeDef(_ClientCreatePlatformVersionResponseTypeDef):
    """
    - *(dict) --*

      - **PlatformSummary** *(dict) --*

        Detailed information about the new version of the custom platform.
        - **PlatformArn** *(string) --*

          The ARN of the platform.
    """


_ClientCreatePlatformVersionTagsTypeDef = TypedDict(
    "_ClientCreatePlatformVersionTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreatePlatformVersionTagsTypeDef(_ClientCreatePlatformVersionTagsTypeDef):
    """
    - *(dict) --*

      Describes a tag applied to a resource in an environment.
      - **Key** *(string) --*

        The key of the tag.
    """


_ClientCreateStorageLocationResponseTypeDef = TypedDict(
    "_ClientCreateStorageLocationResponseTypeDef", {"S3Bucket": str}, total=False
)


class ClientCreateStorageLocationResponseTypeDef(_ClientCreateStorageLocationResponseTypeDef):
    """
    - *(dict) --*

      Results of a  CreateStorageLocationResult call.
      - **S3Bucket** *(string) --*

        The name of the Amazon S3 bucket created.
    """


_ClientDeletePlatformVersionResponsePlatformSummaryTypeDef = TypedDict(
    "_ClientDeletePlatformVersionResponsePlatformSummaryTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": Literal["Creating", "Failed", "Ready", "Deleting", "Deleted"],
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)


class ClientDeletePlatformVersionResponsePlatformSummaryTypeDef(
    _ClientDeletePlatformVersionResponsePlatformSummaryTypeDef
):
    """
    - **PlatformSummary** *(dict) --*

      Detailed information about the version of the custom platform.
      - **PlatformArn** *(string) --*

        The ARN of the platform.
    """


_ClientDeletePlatformVersionResponseTypeDef = TypedDict(
    "_ClientDeletePlatformVersionResponseTypeDef",
    {"PlatformSummary": ClientDeletePlatformVersionResponsePlatformSummaryTypeDef},
    total=False,
)


class ClientDeletePlatformVersionResponseTypeDef(_ClientDeletePlatformVersionResponseTypeDef):
    """
    - *(dict) --*

      - **PlatformSummary** *(dict) --*

        Detailed information about the version of the custom platform.
        - **PlatformArn** *(string) --*

          The ARN of the platform.
    """


_ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef",
    {"Maximum": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef
):
    """
    - **ApplicationQuota** *(dict) --*

      The quota for applications in the AWS account.
      - **Maximum** *(integer) --*

        The maximum number of instances of this Elastic Beanstalk resource type that an AWS account
        can use.
    """


_ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef",
    {"Maximum": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef
):
    pass


_ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef",
    {"Maximum": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef
):
    pass


_ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef",
    {"Maximum": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef
):
    pass


_ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef",
    {"Maximum": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef
):
    pass


_ClientDescribeAccountAttributesResponseResourceQuotasTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasTypeDef",
    {
        "ApplicationQuota": ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef,
        "ApplicationVersionQuota": ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef,
        "EnvironmentQuota": ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef,
        "ConfigurationTemplateQuota": ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef,
        "CustomPlatformQuota": ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef,
    },
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasTypeDef
):
    """
    - **ResourceQuotas** *(dict) --*

      The Elastic Beanstalk resource quotas associated with the calling AWS account.
      - **ApplicationQuota** *(dict) --*

        The quota for applications in the AWS account.
        - **Maximum** *(integer) --*

          The maximum number of instances of this Elastic Beanstalk resource type that an AWS
          account can use.
    """


_ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseTypeDef",
    {"ResourceQuotas": ClientDescribeAccountAttributesResponseResourceQuotasTypeDef},
    total=False,
)


class ClientDescribeAccountAttributesResponseTypeDef(
    _ClientDescribeAccountAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **ResourceQuotas** *(dict) --*

        The Elastic Beanstalk resource quotas associated with the calling AWS account.
        - **ApplicationQuota** *(dict) --*

          The quota for applications in the AWS account.
          - **Maximum** *(integer) --*

            The maximum number of instances of this Elastic Beanstalk resource type that an AWS
            account can use.
    """


_ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef = TypedDict(
    "_ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef",
    {
        "SourceType": Literal["Git", "Zip"],
        "SourceRepository": Literal["CodeCommit", "S3"],
        "SourceLocation": str,
    },
    total=False,
)


class ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef(
    _ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef
):
    pass


_ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef = TypedDict(
    "_ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef(
    _ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef
):
    pass


_ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef = TypedDict(
    "_ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Processed", "Unprocessed", "Failed", "Processing", "Building"],
    },
    total=False,
)


class ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef(
    _ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef
):
    """
    - *(dict) --*

      Describes the properties of an application version.
      - **ApplicationVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the application version.
    """


_ClientDescribeApplicationVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeApplicationVersionsResponseTypeDef",
    {
        "ApplicationVersions": List[
            ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeApplicationVersionsResponseTypeDef(
    _ClientDescribeApplicationVersionsResponseTypeDef
):
    """
    - *(dict) --*

      Result message wrapping a list of application version descriptions.
      - **ApplicationVersions** *(list) --*

        List of ``ApplicationVersionDescription`` objects sorted in order of creation.
        - *(dict) --*

          Describes the properties of an application version.
          - **ApplicationVersionArn** *(string) --*

            The Amazon Resource Name (ARN) of the application version.
    """


_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef
):
    pass


_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef
):
    pass


_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    pass


_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef(
    _ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef
):
    pass


_ClientDescribeApplicationsResponseApplicationsTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseApplicationsTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationsResponseApplicationsTypeDef(
    _ClientDescribeApplicationsResponseApplicationsTypeDef
):
    """
    - *(dict) --*

      Describes the properties of an application.
      - **ApplicationArn** *(string) --*

        The Amazon Resource Name (ARN) of the application.
    """


_ClientDescribeApplicationsResponseTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseTypeDef",
    {"Applications": List[ClientDescribeApplicationsResponseApplicationsTypeDef]},
    total=False,
)


class ClientDescribeApplicationsResponseTypeDef(_ClientDescribeApplicationsResponseTypeDef):
    """
    - *(dict) --*

      Result message containing a list of application descriptions.
      - **Applications** *(list) --*

        This parameter contains a list of  ApplicationDescription .
        - *(dict) --*

          Describes the properties of an application.
          - **ApplicationArn** *(string) --*

            The Amazon Resource Name (ARN) of the application.
    """


_ClientDescribeConfigurationOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeConfigurationOptionsOptionsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)


class ClientDescribeConfigurationOptionsOptionsTypeDef(
    _ClientDescribeConfigurationOptionsOptionsTypeDef
):
    """
    - *(dict) --*

      A specification identifying an individual configuration option.
      - **ResourceName** *(string) --*

        A unique resource name for a time-based scaling configuration option.
    """


_ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef = TypedDict(
    "_ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef",
    {"Pattern": str, "Label": str},
    total=False,
)


class ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef(
    _ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef
):
    pass


_ClientDescribeConfigurationOptionsResponseOptionsTypeDef = TypedDict(
    "_ClientDescribeConfigurationOptionsResponseOptionsTypeDef",
    {
        "Namespace": str,
        "Name": str,
        "DefaultValue": str,
        "ChangeSeverity": str,
        "UserDefined": bool,
        "ValueType": Literal["Scalar", "List"],
        "ValueOptions": List[str],
        "MinValue": int,
        "MaxValue": int,
        "MaxLength": int,
        "Regex": ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef,
    },
    total=False,
)


class ClientDescribeConfigurationOptionsResponseOptionsTypeDef(
    _ClientDescribeConfigurationOptionsResponseOptionsTypeDef
):
    pass


_ClientDescribeConfigurationOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationOptionsResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "Options": List[ClientDescribeConfigurationOptionsResponseOptionsTypeDef],
    },
    total=False,
)


class ClientDescribeConfigurationOptionsResponseTypeDef(
    _ClientDescribeConfigurationOptionsResponseTypeDef
):
    """
    - *(dict) --*

      Describes the settings for a specified configuration set.
      - **SolutionStackName** *(string) --*

        The name of the solution stack these configuration options belong to.
    """


_ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef(
    _ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef
):
    pass


_ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": Literal["deployed", "pending", "failed"],
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List[
            ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef(
    _ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef
):
    """
    - *(dict) --*

      Describes the settings for a configuration set.
      - **SolutionStackName** *(string) --*

        The name of the solution stack this configuration set uses.
    """


_ClientDescribeConfigurationSettingsResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationSettingsResponseTypeDef",
    {
        "ConfigurationSettings": List[
            ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConfigurationSettingsResponseTypeDef(
    _ClientDescribeConfigurationSettingsResponseTypeDef
):
    """
    - *(dict) --*

      The results from a request to change the configuration settings of an environment.
      - **ConfigurationSettings** *(list) --*

        A list of  ConfigurationSettingsDescription .
        - *(dict) --*

          Describes the settings for a configuration set.
          - **SolutionStackName** *(string) --*

            The name of the solution stack this configuration set uses.
    """


_ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef = TypedDict(
    "_ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef",
    {
        "P999": float,
        "P99": float,
        "P95": float,
        "P90": float,
        "P85": float,
        "P75": float,
        "P50": float,
        "P10": float,
    },
    total=False,
)


class ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef(
    _ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef
):
    pass


_ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef",
    {"Status2xx": int, "Status3xx": int, "Status4xx": int, "Status5xx": int},
    total=False,
)


class ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef(
    _ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef
):
    pass


_ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef",
    {
        "Duration": int,
        "RequestCount": int,
        "StatusCodes": ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef,
        "Latency": ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef,
    },
    total=False,
)


class ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef(
    _ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef
):
    pass


_ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef = TypedDict(
    "_ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef",
    {
        "NoData": int,
        "Unknown": int,
        "Pending": int,
        "Ok": int,
        "Info": int,
        "Warning": int,
        "Degraded": int,
        "Severe": int,
    },
    total=False,
)


class ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef(
    _ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef
):
    pass


_ClientDescribeEnvironmentHealthResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentHealthResponseTypeDef",
    {
        "EnvironmentName": str,
        "HealthStatus": str,
        "Status": Literal["Green", "Yellow", "Red", "Grey"],
        "Color": str,
        "Causes": List[str],
        "ApplicationMetrics": ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef,
        "InstancesHealth": ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef,
        "RefreshedAt": datetime,
    },
    total=False,
)


class ClientDescribeEnvironmentHealthResponseTypeDef(
    _ClientDescribeEnvironmentHealthResponseTypeDef
):
    """
    - *(dict) --*

      Health details for an AWS Elastic Beanstalk environment.
      - **EnvironmentName** *(string) --*

        The environment's name.
    """


_ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef",
    {
        "ActionId": str,
        "ActionType": Literal["InstanceRefresh", "PlatformUpdate", "Unknown"],
        "ActionDescription": str,
        "FailureType": Literal[
            "UpdateCancelled",
            "CancellationFailed",
            "RollbackFailed",
            "RollbackSuccessful",
            "InternalFailure",
            "InvalidEnvironmentState",
            "PermissionsError",
        ],
        "Status": Literal["Completed", "Failed", "Unknown"],
        "FailureDescription": str,
        "ExecutedTime": datetime,
        "FinishedTime": datetime,
    },
    total=False,
)


class ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef(
    _ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef
):
    """
    - *(dict) --*

      The record of a completed or failed managed action.
      - **ActionId** *(string) --*

        A unique identifier for the managed action.
    """


_ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef",
    {
        "ManagedActionHistoryItems": List[
            ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef(
    _ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef
):
    """
    - *(dict) --*

      A result message containing a list of completed and failed managed actions.
      - **ManagedActionHistoryItems** *(list) --*

        A list of completed and failed managed actions.
        - *(dict) --*

          The record of a completed or failed managed action.
          - **ActionId** *(string) --*

            A unique identifier for the managed action.
    """


_ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef",
    {
        "ActionId": str,
        "ActionDescription": str,
        "ActionType": Literal["InstanceRefresh", "PlatformUpdate", "Unknown"],
        "Status": Literal["Scheduled", "Pending", "Running", "Unknown"],
        "WindowStartTime": datetime,
    },
    total=False,
)


class ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef(
    _ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef
):
    """
    - *(dict) --*

      The record of an upcoming or in-progress managed action.
      - **ActionId** *(string) --*

        A unique identifier for the managed action.
    """


_ClientDescribeEnvironmentManagedActionsResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentManagedActionsResponseTypeDef",
    {"ManagedActions": List[ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef]},
    total=False,
)


class ClientDescribeEnvironmentManagedActionsResponseTypeDef(
    _ClientDescribeEnvironmentManagedActionsResponseTypeDef
):
    """
    - *(dict) --*

      The result message containing a list of managed actions.
      - **ManagedActions** *(list) --*

        A list of upcoming and in-progress managed actions.
        - *(dict) --*

          The record of an upcoming or in-progress managed action.
          - **ActionId** *(string) --*

            A unique identifier for the managed action.
    """


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef
):
    pass


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef",
    {"Id": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef
):
    pass


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef
):
    pass


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef",
    {"Id": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef
):
    pass


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef
):
    pass


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef",
    {"Name": str, "URL": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef
):
    pass


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef
):
    pass


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef",
    {
        "EnvironmentName": str,
        "AutoScalingGroups": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef
        ],
        "Instances": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef
        ],
        "LaunchConfigurations": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef
        ],
        "LaunchTemplates": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef
        ],
        "LoadBalancers": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef
        ],
        "Triggers": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef
        ],
        "Queues": List[ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef],
    },
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef
):
    """
    - **EnvironmentResources** *(dict) --*

      A list of  EnvironmentResourceDescription .
      - **EnvironmentName** *(string) --*

        The name of the environment.
    """


_ClientDescribeEnvironmentResourcesResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseTypeDef",
    {"EnvironmentResources": ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseTypeDef(
    _ClientDescribeEnvironmentResourcesResponseTypeDef
):
    """
    - *(dict) --*

      Result message containing a list of environment resource descriptions.
      - **EnvironmentResources** *(dict) --*

        A list of  EnvironmentResourceDescription .
        - **EnvironmentName** *(string) --*

          The name of the environment.
    """


_ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef
):
    pass


_ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
):
    pass


_ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef
):
    pass


_ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    {"LoadBalancer": ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef},
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef
):
    pass


_ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef
):
    pass


_ClientDescribeEnvironmentsResponseEnvironmentsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef,
        "Tier": ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef,
        "EnvironmentLinks": List[
            ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsTypeDef
):
    """
    - *(dict) --*

      Describes the properties of an environment.
      - **EnvironmentName** *(string) --*

        The name of this environment.
    """


_ClientDescribeEnvironmentsResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseTypeDef",
    {"Environments": List[ClientDescribeEnvironmentsResponseEnvironmentsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeEnvironmentsResponseTypeDef(_ClientDescribeEnvironmentsResponseTypeDef):
    """
    - *(dict) --*

      Result message containing a list of environment descriptions.
      - **Environments** *(list) --*

        Returns an  EnvironmentDescription list.
        - *(dict) --*

          Describes the properties of an environment.
          - **EnvironmentName** *(string) --*

            The name of this environment.
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {
        "EventDate": datetime,
        "Message": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "TemplateName": str,
        "EnvironmentName": str,
        "PlatformArn": str,
        "RequestId": str,
        "Severity": Literal["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
    },
    total=False,
)


class ClientDescribeEventsResponseEventsTypeDef(_ClientDescribeEventsResponseEventsTypeDef):
    """
    - *(dict) --*

      Describes an event.
      - **EventDate** *(datetime) --*

        The date when the event occurred.
    """


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"Events": List[ClientDescribeEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    - *(dict) --*

      Result message wrapping a list of event descriptions.
      - **Events** *(list) --*

        A list of  EventDescription .
        - *(dict) --*

          Describes an event.
          - **EventDate** *(datetime) --*

            The date when the event occurred.
    """


_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef",
    {
        "P999": float,
        "P99": float,
        "P95": float,
        "P90": float,
        "P85": float,
        "P75": float,
        "P50": float,
        "P10": float,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef
):
    pass


_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef",
    {"Status2xx": int, "Status3xx": int, "Status4xx": int, "Status5xx": int},
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef
):
    pass


_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef",
    {
        "Duration": int,
        "RequestCount": int,
        "StatusCodes": ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef,
        "Latency": ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef
):
    pass


_ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef",
    {"VersionLabel": str, "DeploymentId": int, "Status": str, "DeploymentTime": datetime},
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef
):
    pass


_ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef",
    {
        "User": float,
        "Nice": float,
        "System": float,
        "Idle": float,
        "IOWait": float,
        "IRQ": float,
        "SoftIRQ": float,
        "Privileged": float,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef
):
    pass


_ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef",
    {
        "CPUUtilization": ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef,
        "LoadAverage": List[float],
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef
):
    pass


_ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef",
    {
        "InstanceId": str,
        "HealthStatus": str,
        "Color": str,
        "Causes": List[str],
        "LaunchedAt": datetime,
        "ApplicationMetrics": ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef,
        "System": ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef,
        "Deployment": ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef,
        "AvailabilityZone": str,
        "InstanceType": str,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef
):
    """
    - *(dict) --*

      Detailed health information about an Amazon EC2 instance in your Elastic Beanstalk
      environment.
      - **InstanceId** *(string) --*

        The ID of the Amazon EC2 instance.
    """


_ClientDescribeInstancesHealthResponseTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseTypeDef",
    {
        "InstanceHealthList": List[ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef],
        "RefreshedAt": datetime,
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseTypeDef(_ClientDescribeInstancesHealthResponseTypeDef):
    """
    - *(dict) --*

      Detailed health information about the Amazon EC2 instances in an AWS Elastic Beanstalk
      environment.
      - **InstanceHealthList** *(list) --*

        Detailed health information about each instance.
        The output differs slightly between Linux and Windows environments. There is a difference in
        the members that are supported under the ``<CPUUtilization>`` type.
        - *(dict) --*

          Detailed health information about an Amazon EC2 instance in your Elastic Beanstalk
          environment.
          - **InstanceId** *(string) --*

            The ID of the Amazon EC2 instance.
    """


_ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef = TypedDict(
    "_ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef",
    {"VirtualizationType": str, "ImageId": str},
    total=False,
)


class ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef(
    _ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef
):
    pass


_ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef = TypedDict(
    "_ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef(
    _ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef
):
    pass


_ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef = TypedDict(
    "_ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef(
    _ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef
):
    pass


_ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef = TypedDict(
    "_ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformName": str,
        "PlatformVersion": str,
        "SolutionStackName": str,
        "PlatformStatus": Literal["Creating", "Failed", "Ready", "Deleting", "Deleted"],
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "PlatformCategory": str,
        "Description": str,
        "Maintainer": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "ProgrammingLanguages": List[
            ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef
        ],
        "Frameworks": List[
            ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef
        ],
        "CustomAmiList": List[
            ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef
        ],
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)


class ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef(
    _ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef
):
    """
    - **PlatformDescription** *(dict) --*

      Detailed information about the version of the platform.
      - **PlatformArn** *(string) --*

        The ARN of the platform.
    """


_ClientDescribePlatformVersionResponseTypeDef = TypedDict(
    "_ClientDescribePlatformVersionResponseTypeDef",
    {"PlatformDescription": ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef},
    total=False,
)


class ClientDescribePlatformVersionResponseTypeDef(_ClientDescribePlatformVersionResponseTypeDef):
    """
    - *(dict) --*

      - **PlatformDescription** *(dict) --*

        Detailed information about the version of the platform.
        - **PlatformArn** *(string) --*

          The ARN of the platform.
    """


_ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef = TypedDict(
    "_ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef",
    {"SolutionStackName": str, "PermittedFileTypes": List[str]},
    total=False,
)


class ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef(
    _ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef
):
    pass


_ClientListAvailableSolutionStacksResponseTypeDef = TypedDict(
    "_ClientListAvailableSolutionStacksResponseTypeDef",
    {
        "SolutionStacks": List[str],
        "SolutionStackDetails": List[
            ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef
        ],
    },
    total=False,
)


class ClientListAvailableSolutionStacksResponseTypeDef(
    _ClientListAvailableSolutionStacksResponseTypeDef
):
    """
    - *(dict) --*

      A list of available AWS Elastic Beanstalk solution stacks.
      - **SolutionStacks** *(list) --*

        A list of available solution stacks.
        - *(string) --*
    """


_ClientListPlatformVersionsFiltersTypeDef = TypedDict(
    "_ClientListPlatformVersionsFiltersTypeDef",
    {"Type": str, "Operator": str, "Values": List[str]},
    total=False,
)


class ClientListPlatformVersionsFiltersTypeDef(_ClientListPlatformVersionsFiltersTypeDef):
    """
    - *(dict) --*

      Specify criteria to restrict the results when listing custom platforms.
      The filter is evaluated as the expression:

        ``Type``  ``Operator``  ``Values[i]``
    """


_ClientListPlatformVersionsResponsePlatformSummaryListTypeDef = TypedDict(
    "_ClientListPlatformVersionsResponsePlatformSummaryListTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": Literal["Creating", "Failed", "Ready", "Deleting", "Deleted"],
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)


class ClientListPlatformVersionsResponsePlatformSummaryListTypeDef(
    _ClientListPlatformVersionsResponsePlatformSummaryListTypeDef
):
    """
    - *(dict) --*

      Detailed information about a platform.
      - **PlatformArn** *(string) --*

        The ARN of the platform.
    """


_ClientListPlatformVersionsResponseTypeDef = TypedDict(
    "_ClientListPlatformVersionsResponseTypeDef",
    {
        "PlatformSummaryList": List[ClientListPlatformVersionsResponsePlatformSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListPlatformVersionsResponseTypeDef(_ClientListPlatformVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **PlatformSummaryList** *(list) --*

        Detailed information about the platforms.
        - *(dict) --*

          Detailed information about a platform.
          - **PlatformArn** *(string) --*

            The ARN of the platform.
    """


_ClientListTagsForResourceResponseResourceTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseResourceTagsTypeDef(
    _ClientListTagsForResourceResponseResourceTagsTypeDef
):
    pass


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {
        "ResourceArn": str,
        "ResourceTags": List[ClientListTagsForResourceResponseResourceTagsTypeDef],
    },
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the resouce for which a tag list was requested.
    """


_ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef = TypedDict(
    "_ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef",
    {
        "InfoType": Literal["tail", "bundle"],
        "Ec2InstanceId": str,
        "SampleTimestamp": datetime,
        "Message": str,
    },
    total=False,
)


class ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef(
    _ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef
):
    """
    - *(dict) --*

      The information retrieved from the Amazon EC2 instances.
      - **InfoType** *(string) --*

        The type of information retrieved.
    """


_ClientRetrieveEnvironmentInfoResponseTypeDef = TypedDict(
    "_ClientRetrieveEnvironmentInfoResponseTypeDef",
    {"EnvironmentInfo": List[ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef]},
    total=False,
)


class ClientRetrieveEnvironmentInfoResponseTypeDef(_ClientRetrieveEnvironmentInfoResponseTypeDef):
    """
    - *(dict) --*

      Result message containing a description of the requested environment info.
      - **EnvironmentInfo** *(list) --*

        The  EnvironmentInfoDescription of the environment.
        - *(dict) --*

          The information retrieved from the Amazon EC2 instances.
          - **InfoType** *(string) --*

            The type of information retrieved.
    """


_ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef(
    _ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef
):
    pass


_ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef(
    _ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef
):
    pass


_ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef],
    },
    total=False,
)


class ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef(
    _ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef
):
    pass


_ClientTerminateEnvironmentResponseResourcesTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseResourcesTypeDef",
    {"LoadBalancer": ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef},
    total=False,
)


class ClientTerminateEnvironmentResponseResourcesTypeDef(
    _ClientTerminateEnvironmentResponseResourcesTypeDef
):
    pass


_ClientTerminateEnvironmentResponseTierTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientTerminateEnvironmentResponseTierTypeDef(_ClientTerminateEnvironmentResponseTierTypeDef):
    pass


_ClientTerminateEnvironmentResponseTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": ClientTerminateEnvironmentResponseResourcesTypeDef,
        "Tier": ClientTerminateEnvironmentResponseTierTypeDef,
        "EnvironmentLinks": List[ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef],
        "EnvironmentArn": str,
    },
    total=False,
)


class ClientTerminateEnvironmentResponseTypeDef(_ClientTerminateEnvironmentResponseTypeDef):
    """
    - *(dict) --*

      Describes the properties of an environment.
      - **EnvironmentName** *(string) --*

        The name of this environment.
    """


_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef
):
    pass


_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef
):
    pass


_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    pass


_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef(
    _ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef
):
    """
    The lifecycle configuration.
    - **ServiceRole** *(string) --*

      The ARN of an IAM service role that Elastic Beanstalk has permission to assume.
      The ``ServiceRole`` property is required the first time that you provide a
      ``VersionLifecycleConfig`` for the application in one of the supporting calls
      (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it once,
      in either one of the calls, Elastic Beanstalk persists the Service Role with the application,
      and you don't need to specify it again in subsequent ``UpdateApplicationResourceLifecycle``
      calls. You can, however, specify it in subsequent calls to change the Service Role to another
      value.
    """


_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef
):
    pass


_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef
):
    pass


_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    pass


_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef(
    _ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef
):
    pass


_ClientUpdateApplicationResourceLifecycleResponseTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResponseTypeDef",
    {
        "ApplicationName": str,
        "ResourceLifecycleConfig": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResponseTypeDef(
    _ClientUpdateApplicationResourceLifecycleResponseTypeDef
):
    """
    - *(dict) --*

      - **ApplicationName** *(string) --*

        The name of the application.
    """


_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef
):
    pass


_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef
):
    pass


_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    pass


_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef(
    _ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef
):
    pass


_ClientUpdateApplicationResponseApplicationTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationTypeDef(
    _ClientUpdateApplicationResponseApplicationTypeDef
):
    """
    - **Application** *(dict) --*

      The  ApplicationDescription of the application.
      - **ApplicationArn** *(string) --*

        The Amazon Resource Name (ARN) of the application.
    """


_ClientUpdateApplicationResponseTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseTypeDef",
    {"Application": ClientUpdateApplicationResponseApplicationTypeDef},
    total=False,
)


class ClientUpdateApplicationResponseTypeDef(_ClientUpdateApplicationResponseTypeDef):
    """
    - *(dict) --*

      Result message containing a single description of an application.
      - **Application** *(dict) --*

        The  ApplicationDescription of the application.
        - **ApplicationArn** *(string) --*

          The Amazon Resource Name (ARN) of the application.
    """


_ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "_ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    {
        "SourceType": Literal["Git", "Zip"],
        "SourceRepository": Literal["CodeCommit", "S3"],
        "SourceLocation": str,
    },
    total=False,
)


class ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef(
    _ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef
):
    pass


_ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef = TypedDict(
    "_ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef(
    _ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef
):
    pass


_ClientUpdateApplicationVersionResponseApplicationVersionTypeDef = TypedDict(
    "_ClientUpdateApplicationVersionResponseApplicationVersionTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Processed", "Unprocessed", "Failed", "Processing", "Building"],
    },
    total=False,
)


class ClientUpdateApplicationVersionResponseApplicationVersionTypeDef(
    _ClientUpdateApplicationVersionResponseApplicationVersionTypeDef
):
    """
    - **ApplicationVersion** *(dict) --*

      The  ApplicationVersionDescription of the application version.
      - **ApplicationVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the application version.
    """


_ClientUpdateApplicationVersionResponseTypeDef = TypedDict(
    "_ClientUpdateApplicationVersionResponseTypeDef",
    {"ApplicationVersion": ClientUpdateApplicationVersionResponseApplicationVersionTypeDef},
    total=False,
)


class ClientUpdateApplicationVersionResponseTypeDef(_ClientUpdateApplicationVersionResponseTypeDef):
    """
    - *(dict) --*

      Result message wrapping a single description of an application version.
      - **ApplicationVersion** *(dict) --*

        The  ApplicationVersionDescription of the application version.
        - **ApplicationVersionArn** *(string) --*

          The Amazon Resource Name (ARN) of the application version.
    """


_ClientUpdateConfigurationTemplateOptionSettingsTypeDef = TypedDict(
    "_ClientUpdateConfigurationTemplateOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientUpdateConfigurationTemplateOptionSettingsTypeDef(
    _ClientUpdateConfigurationTemplateOptionSettingsTypeDef
):
    """
    - *(dict) --*

      A specification identifying an individual configuration option along with its current value.
      For a list of possible option values, go to `Option Values
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
      Elastic Beanstalk Developer Guide* .
      - **ResourceName** *(string) --*

        A unique resource name for a time-based scaling configuration option.
    """


_ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef = TypedDict(
    "_ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)


class ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef(
    _ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef
):
    """
    - *(dict) --*

      A specification identifying an individual configuration option.
      - **ResourceName** *(string) --*

        A unique resource name for a time-based scaling configuration option.
    """


_ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef = TypedDict(
    "_ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef(
    _ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef
):
    pass


_ClientUpdateConfigurationTemplateResponseTypeDef = TypedDict(
    "_ClientUpdateConfigurationTemplateResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": Literal["deployed", "pending", "failed"],
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List[ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef],
    },
    total=False,
)


class ClientUpdateConfigurationTemplateResponseTypeDef(
    _ClientUpdateConfigurationTemplateResponseTypeDef
):
    """
    - *(dict) --*

      Describes the settings for a configuration set.
      - **SolutionStackName** *(string) --*

        The name of the solution stack this configuration set uses.
    """


_ClientUpdateEnvironmentOptionSettingsTypeDef = TypedDict(
    "_ClientUpdateEnvironmentOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientUpdateEnvironmentOptionSettingsTypeDef(_ClientUpdateEnvironmentOptionSettingsTypeDef):
    """
    - *(dict) --*

      A specification identifying an individual configuration option along with its current value.
      For a list of possible option values, go to `Option Values
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
      Elastic Beanstalk Developer Guide* .
      - **ResourceName** *(string) --*

        A unique resource name for a time-based scaling configuration option.
    """


_ClientUpdateEnvironmentOptionsToRemoveTypeDef = TypedDict(
    "_ClientUpdateEnvironmentOptionsToRemoveTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)


class ClientUpdateEnvironmentOptionsToRemoveTypeDef(_ClientUpdateEnvironmentOptionsToRemoveTypeDef):
    """
    - *(dict) --*

      A specification identifying an individual configuration option.
      - **ResourceName** *(string) --*

        A unique resource name for a time-based scaling configuration option.
    """


_ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef(
    _ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef
):
    pass


_ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef(
    _ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef
):
    pass


_ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef],
    },
    total=False,
)


class ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef(
    _ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef
):
    pass


_ClientUpdateEnvironmentResponseResourcesTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseResourcesTypeDef",
    {"LoadBalancer": ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef},
    total=False,
)


class ClientUpdateEnvironmentResponseResourcesTypeDef(
    _ClientUpdateEnvironmentResponseResourcesTypeDef
):
    pass


_ClientUpdateEnvironmentResponseTierTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientUpdateEnvironmentResponseTierTypeDef(_ClientUpdateEnvironmentResponseTierTypeDef):
    pass


_ClientUpdateEnvironmentResponseTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": ClientUpdateEnvironmentResponseResourcesTypeDef,
        "Tier": ClientUpdateEnvironmentResponseTierTypeDef,
        "EnvironmentLinks": List[ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef],
        "EnvironmentArn": str,
    },
    total=False,
)


class ClientUpdateEnvironmentResponseTypeDef(_ClientUpdateEnvironmentResponseTypeDef):
    """
    - *(dict) --*

      Describes the properties of an environment.
      - **EnvironmentName** *(string) --*

        The name of this environment.
    """


_ClientUpdateEnvironmentTierTypeDef = TypedDict(
    "_ClientUpdateEnvironmentTierTypeDef", {"Name": str, "Type": str, "Version": str}, total=False
)


class ClientUpdateEnvironmentTierTypeDef(_ClientUpdateEnvironmentTierTypeDef):
    """
    This specifies the tier to use to update the environment.
    Condition: At this time, if you change the tier version, name, or type, AWS Elastic Beanstalk
    returns ``InvalidParameterValue`` error.
    - **Name** *(string) --*

      The name of this environment tier.
      Valid values:
      * For *Web server tier* – ``WebServer``
      * For *Worker tier* – ``Worker``
    """


_ClientUpdateTagsForResourceTagsToAddTypeDef = TypedDict(
    "_ClientUpdateTagsForResourceTagsToAddTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUpdateTagsForResourceTagsToAddTypeDef(_ClientUpdateTagsForResourceTagsToAddTypeDef):
    """
    - *(dict) --*

      Describes a tag applied to a resource in an environment.
      - **Key** *(string) --*

        The key of the tag.
    """


_ClientValidateConfigurationSettingsOptionSettingsTypeDef = TypedDict(
    "_ClientValidateConfigurationSettingsOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientValidateConfigurationSettingsOptionSettingsTypeDef(
    _ClientValidateConfigurationSettingsOptionSettingsTypeDef
):
    """
    - *(dict) --*

      A specification identifying an individual configuration option along with its current value.
      For a list of possible option values, go to `Option Values
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
      Elastic Beanstalk Developer Guide* .
      - **ResourceName** *(string) --*

        A unique resource name for a time-based scaling configuration option.
    """


_ClientValidateConfigurationSettingsResponseMessagesTypeDef = TypedDict(
    "_ClientValidateConfigurationSettingsResponseMessagesTypeDef",
    {"Message": str, "Severity": Literal["error", "warning"], "Namespace": str, "OptionName": str},
    total=False,
)


class ClientValidateConfigurationSettingsResponseMessagesTypeDef(
    _ClientValidateConfigurationSettingsResponseMessagesTypeDef
):
    """
    - *(dict) --*

      An error or warning for a desired configuration option value.
      - **Message** *(string) --*

        A message describing the error or warning.
    """


_ClientValidateConfigurationSettingsResponseTypeDef = TypedDict(
    "_ClientValidateConfigurationSettingsResponseTypeDef",
    {"Messages": List[ClientValidateConfigurationSettingsResponseMessagesTypeDef]},
    total=False,
)


class ClientValidateConfigurationSettingsResponseTypeDef(
    _ClientValidateConfigurationSettingsResponseTypeDef
):
    """
    - *(dict) --*

      Provides a list of validation messages.
      - **Messages** *(list) --*

        A list of  ValidationMessage .
        - *(dict) --*

          An error or warning for a desired configuration option value.
          - **Message** *(string) --*

            A message describing the error or warning.
    """


_DescribeApplicationVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeApplicationVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeApplicationVersionsPaginatePaginationConfigTypeDef(
    _DescribeApplicationVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef = TypedDict(
    "_DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef",
    {
        "SourceType": Literal["Git", "Zip"],
        "SourceRepository": Literal["CodeCommit", "S3"],
        "SourceLocation": str,
    },
    total=False,
)


class DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef(
    _DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef
):
    pass


_DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef = TypedDict(
    "_DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef(
    _DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef
):
    pass


_DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef = TypedDict(
    "_DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Processed", "Unprocessed", "Failed", "Processing", "Building"],
    },
    total=False,
)


class DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef(
    _DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef
):
    """
    - *(dict) --*

      Describes the properties of an application version.
      - **ApplicationVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the application version.
    """


_DescribeApplicationVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeApplicationVersionsPaginateResponseTypeDef",
    {
        "ApplicationVersions": List[
            DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef
        ]
    },
    total=False,
)


class DescribeApplicationVersionsPaginateResponseTypeDef(
    _DescribeApplicationVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Result message wrapping a list of application version descriptions.
      - **ApplicationVersions** *(list) --*

        List of ``ApplicationVersionDescription`` objects sorted in order of creation.
        - *(dict) --*

          Describes the properties of an application version.
          - **ApplicationVersionArn** *(string) --*

            The Amazon Resource Name (ARN) of the application version.
    """


_DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef(
    _DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef = TypedDict(
    "_DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef",
    {
        "ActionId": str,
        "ActionType": Literal["InstanceRefresh", "PlatformUpdate", "Unknown"],
        "ActionDescription": str,
        "FailureType": Literal[
            "UpdateCancelled",
            "CancellationFailed",
            "RollbackFailed",
            "RollbackSuccessful",
            "InternalFailure",
            "InvalidEnvironmentState",
            "PermissionsError",
        ],
        "Status": Literal["Completed", "Failed", "Unknown"],
        "FailureDescription": str,
        "ExecutedTime": datetime,
        "FinishedTime": datetime,
    },
    total=False,
)


class DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef(
    _DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef
):
    """
    - *(dict) --*

      The record of a completed or failed managed action.
      - **ActionId** *(string) --*

        A unique identifier for the managed action.
    """


_DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef = TypedDict(
    "_DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef",
    {
        "ManagedActionHistoryItems": List[
            DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef
        ]
    },
    total=False,
)


class DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef(
    _DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef
):
    """
    - *(dict) --*

      A result message containing a list of completed and failed managed actions.
      - **ManagedActionHistoryItems** *(list) --*

        A list of completed and failed managed actions.
        - *(dict) --*

          The record of a completed or failed managed action.
          - **ActionId** *(string) --*

            A unique identifier for the managed action.
    """


_DescribeEnvironmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEnvironmentsPaginatePaginationConfigTypeDef(
    _DescribeEnvironmentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef
):
    pass


_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
):
    pass


_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef
):
    pass


_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef",
    {"LoadBalancer": DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef},
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef
):
    pass


_DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef
):
    pass


_DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": Literal["Launching", "Updating", "Ready", "Terminating", "Terminated"],
        "AbortableOperationInProgress": bool,
        "Health": Literal["Green", "Yellow", "Red", "Grey"],
        "HealthStatus": Literal[
            "NoData",
            "Unknown",
            "Pending",
            "Ok",
            "Info",
            "Warning",
            "Degraded",
            "Severe",
            "Suspended",
        ],
        "Resources": DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef,
        "Tier": DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef,
        "EnvironmentLinks": List[
            DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef
):
    """
    - *(dict) --*

      Describes the properties of an environment.
      - **EnvironmentName** *(string) --*

        The name of this environment.
    """


_DescribeEnvironmentsPaginateResponseTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseTypeDef",
    {"Environments": List[DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef]},
    total=False,
)


class DescribeEnvironmentsPaginateResponseTypeDef(_DescribeEnvironmentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Result message containing a list of environment descriptions.
      - **Environments** *(list) --*

        Returns an  EnvironmentDescription list.
        - *(dict) --*

          Describes the properties of an environment.
          - **EnvironmentName** *(string) --*

            The name of this environment.
    """


_DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventsPaginatePaginationConfigTypeDef(_DescribeEventsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeEventsPaginateResponseEventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseEventsTypeDef",
    {
        "EventDate": datetime,
        "Message": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "TemplateName": str,
        "EnvironmentName": str,
        "PlatformArn": str,
        "RequestId": str,
        "Severity": Literal["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
    },
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(_DescribeEventsPaginateResponseEventsTypeDef):
    """
    - *(dict) --*

      Describes an event.
      - **EventDate** *(datetime) --*

        The date when the event occurred.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef]},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Result message wrapping a list of event descriptions.
      - **Events** *(list) --*

        A list of  EventDescription .
        - *(dict) --*

          Describes an event.
          - **EventDate** *(datetime) --*

            The date when the event occurred.
    """


_ListPlatformVersionsPaginateFiltersTypeDef = TypedDict(
    "_ListPlatformVersionsPaginateFiltersTypeDef",
    {"Type": str, "Operator": str, "Values": List[str]},
    total=False,
)


class ListPlatformVersionsPaginateFiltersTypeDef(_ListPlatformVersionsPaginateFiltersTypeDef):
    """
    - *(dict) --*

      Specify criteria to restrict the results when listing custom platforms.
      The filter is evaluated as the expression:

        ``Type``  ``Operator``  ``Values[i]``
    """


_ListPlatformVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPlatformVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPlatformVersionsPaginatePaginationConfigTypeDef(
    _ListPlatformVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef = TypedDict(
    "_ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": Literal["Creating", "Failed", "Ready", "Deleting", "Deleted"],
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)


class ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef(
    _ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef
):
    """
    - *(dict) --*

      Detailed information about a platform.
      - **PlatformArn** *(string) --*

        The ARN of the platform.
    """


_ListPlatformVersionsPaginateResponseTypeDef = TypedDict(
    "_ListPlatformVersionsPaginateResponseTypeDef",
    {"PlatformSummaryList": List[ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef]},
    total=False,
)


class ListPlatformVersionsPaginateResponseTypeDef(_ListPlatformVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **PlatformSummaryList** *(list) --*

        Detailed information about the platforms.
        - *(dict) --*

          Detailed information about a platform.
          - **PlatformArn** *(string) --*

            The ARN of the platform.
    """
