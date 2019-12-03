"Main interface for greengrass service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAssociateRoleToGroupResponseTypeDef",
    "ClientAssociateServiceRoleToAccountResponseTypeDef",
    "ClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef",
    "ClientCreateConnectorDefinitionInitialVersionTypeDef",
    "ClientCreateConnectorDefinitionResponseTypeDef",
    "ClientCreateConnectorDefinitionVersionConnectorsTypeDef",
    "ClientCreateConnectorDefinitionVersionResponseTypeDef",
    "ClientCreateCoreDefinitionInitialVersionCoresTypeDef",
    "ClientCreateCoreDefinitionInitialVersionTypeDef",
    "ClientCreateCoreDefinitionResponseTypeDef",
    "ClientCreateCoreDefinitionVersionCoresTypeDef",
    "ClientCreateCoreDefinitionVersionResponseTypeDef",
    "ClientCreateDeploymentResponseTypeDef",
    "ClientCreateDeviceDefinitionInitialVersionDevicesTypeDef",
    "ClientCreateDeviceDefinitionInitialVersionTypeDef",
    "ClientCreateDeviceDefinitionResponseTypeDef",
    "ClientCreateDeviceDefinitionVersionDevicesTypeDef",
    "ClientCreateDeviceDefinitionVersionResponseTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef",
    "ClientCreateFunctionDefinitionInitialVersionTypeDef",
    "ClientCreateFunctionDefinitionResponseTypeDef",
    "ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef",
    "ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef",
    "ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef",
    "ClientCreateFunctionDefinitionVersionFunctionsTypeDef",
    "ClientCreateFunctionDefinitionVersionResponseTypeDef",
    "ClientCreateGroupCertificateAuthorityResponseTypeDef",
    "ClientCreateGroupInitialVersionTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateGroupVersionResponseTypeDef",
    "ClientCreateLoggerDefinitionInitialVersionLoggersTypeDef",
    "ClientCreateLoggerDefinitionInitialVersionTypeDef",
    "ClientCreateLoggerDefinitionResponseTypeDef",
    "ClientCreateLoggerDefinitionVersionLoggersTypeDef",
    "ClientCreateLoggerDefinitionVersionResponseTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef",
    "ClientCreateResourceDefinitionInitialVersionResourcesTypeDef",
    "ClientCreateResourceDefinitionInitialVersionTypeDef",
    "ClientCreateResourceDefinitionResponseTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef",
    "ClientCreateResourceDefinitionVersionResourcesTypeDef",
    "ClientCreateResourceDefinitionVersionResponseTypeDef",
    "ClientCreateSoftwareUpdateJobResponseTypeDef",
    "ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef",
    "ClientCreateSubscriptionDefinitionInitialVersionTypeDef",
    "ClientCreateSubscriptionDefinitionResponseTypeDef",
    "ClientCreateSubscriptionDefinitionVersionResponseTypeDef",
    "ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef",
    "ClientDisassociateRoleFromGroupResponseTypeDef",
    "ClientDisassociateServiceRoleFromAccountResponseTypeDef",
    "ClientGetAssociatedRoleResponseTypeDef",
    "ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef",
    "ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef",
    "ClientGetBulkDeploymentStatusResponseTypeDef",
    "ClientGetConnectivityInfoResponseConnectivityInfoTypeDef",
    "ClientGetConnectivityInfoResponseTypeDef",
    "ClientGetConnectorDefinitionResponseTypeDef",
    "ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef",
    "ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetConnectorDefinitionVersionResponseTypeDef",
    "ClientGetCoreDefinitionResponseTypeDef",
    "ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef",
    "ClientGetCoreDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetCoreDefinitionVersionResponseTypeDef",
    "ClientGetDeploymentStatusResponseErrorDetailsTypeDef",
    "ClientGetDeploymentStatusResponseTypeDef",
    "ClientGetDeviceDefinitionResponseTypeDef",
    "ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef",
    "ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetDeviceDefinitionVersionResponseTypeDef",
    "ClientGetFunctionDefinitionResponseTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef",
    "ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetFunctionDefinitionVersionResponseTypeDef",
    "ClientGetGroupCertificateAuthorityResponseTypeDef",
    "ClientGetGroupCertificateConfigurationResponseTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetGroupVersionResponseDefinitionTypeDef",
    "ClientGetGroupVersionResponseTypeDef",
    "ClientGetLoggerDefinitionResponseTypeDef",
    "ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef",
    "ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetLoggerDefinitionVersionResponseTypeDef",
    "ClientGetResourceDefinitionResponseTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef",
    "ClientGetResourceDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetResourceDefinitionVersionResponseTypeDef",
    "ClientGetServiceRoleForAccountResponseTypeDef",
    "ClientGetSubscriptionDefinitionResponseTypeDef",
    "ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef",
    "ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef",
    "ClientGetSubscriptionDefinitionVersionResponseTypeDef",
    "ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef",
    "ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef",
    "ClientListBulkDeploymentDetailedReportsResponseTypeDef",
    "ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef",
    "ClientListBulkDeploymentsResponseTypeDef",
    "ClientListConnectorDefinitionVersionsResponseVersionsTypeDef",
    "ClientListConnectorDefinitionVersionsResponseTypeDef",
    "ClientListConnectorDefinitionsResponseDefinitionsTypeDef",
    "ClientListConnectorDefinitionsResponseTypeDef",
    "ClientListCoreDefinitionVersionsResponseVersionsTypeDef",
    "ClientListCoreDefinitionVersionsResponseTypeDef",
    "ClientListCoreDefinitionsResponseDefinitionsTypeDef",
    "ClientListCoreDefinitionsResponseTypeDef",
    "ClientListDeploymentsResponseDeploymentsTypeDef",
    "ClientListDeploymentsResponseTypeDef",
    "ClientListDeviceDefinitionVersionsResponseVersionsTypeDef",
    "ClientListDeviceDefinitionVersionsResponseTypeDef",
    "ClientListDeviceDefinitionsResponseDefinitionsTypeDef",
    "ClientListDeviceDefinitionsResponseTypeDef",
    "ClientListFunctionDefinitionVersionsResponseVersionsTypeDef",
    "ClientListFunctionDefinitionVersionsResponseTypeDef",
    "ClientListFunctionDefinitionsResponseDefinitionsTypeDef",
    "ClientListFunctionDefinitionsResponseTypeDef",
    "ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef",
    "ClientListGroupCertificateAuthoritiesResponseTypeDef",
    "ClientListGroupVersionsResponseVersionsTypeDef",
    "ClientListGroupVersionsResponseTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientListLoggerDefinitionVersionsResponseVersionsTypeDef",
    "ClientListLoggerDefinitionVersionsResponseTypeDef",
    "ClientListLoggerDefinitionsResponseDefinitionsTypeDef",
    "ClientListLoggerDefinitionsResponseTypeDef",
    "ClientListResourceDefinitionVersionsResponseVersionsTypeDef",
    "ClientListResourceDefinitionVersionsResponseTypeDef",
    "ClientListResourceDefinitionsResponseDefinitionsTypeDef",
    "ClientListResourceDefinitionsResponseTypeDef",
    "ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef",
    "ClientListSubscriptionDefinitionVersionsResponseTypeDef",
    "ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef",
    "ClientListSubscriptionDefinitionsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientResetDeploymentsResponseTypeDef",
    "ClientStartBulkDeploymentResponseTypeDef",
    "ClientUpdateConnectivityInfoConnectivityInfoTypeDef",
    "ClientUpdateConnectivityInfoResponseTypeDef",
    "ClientUpdateGroupCertificateConfigurationResponseTypeDef",
    "ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef",
    "ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsErrorDetailsTypeDef",
    "ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsTypeDef",
    "ListBulkDeploymentDetailedReportsPaginateResponseTypeDef",
    "ListBulkDeploymentsPaginatePaginationConfigTypeDef",
    "ListBulkDeploymentsPaginateResponseBulkDeploymentsTypeDef",
    "ListBulkDeploymentsPaginateResponseTypeDef",
    "ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListConnectorDefinitionVersionsPaginateResponseTypeDef",
    "ListConnectorDefinitionsPaginatePaginationConfigTypeDef",
    "ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListConnectorDefinitionsPaginateResponseTypeDef",
    "ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListCoreDefinitionVersionsPaginateResponseTypeDef",
    "ListCoreDefinitionsPaginatePaginationConfigTypeDef",
    "ListCoreDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListCoreDefinitionsPaginateResponseTypeDef",
    "ListDeploymentsPaginatePaginationConfigTypeDef",
    "ListDeploymentsPaginateResponseDeploymentsTypeDef",
    "ListDeploymentsPaginateResponseTypeDef",
    "ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListDeviceDefinitionVersionsPaginateResponseTypeDef",
    "ListDeviceDefinitionsPaginatePaginationConfigTypeDef",
    "ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListDeviceDefinitionsPaginateResponseTypeDef",
    "ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListFunctionDefinitionVersionsPaginateResponseTypeDef",
    "ListFunctionDefinitionsPaginatePaginationConfigTypeDef",
    "ListFunctionDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListFunctionDefinitionsPaginateResponseTypeDef",
    "ListGroupVersionsPaginatePaginationConfigTypeDef",
    "ListGroupVersionsPaginateResponseVersionsTypeDef",
    "ListGroupVersionsPaginateResponseTypeDef",
    "ListGroupsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginateResponseGroupsTypeDef",
    "ListGroupsPaginateResponseTypeDef",
    "ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListLoggerDefinitionVersionsPaginateResponseTypeDef",
    "ListLoggerDefinitionsPaginatePaginationConfigTypeDef",
    "ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListLoggerDefinitionsPaginateResponseTypeDef",
    "ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListResourceDefinitionVersionsPaginateResponseTypeDef",
    "ListResourceDefinitionsPaginatePaginationConfigTypeDef",
    "ListResourceDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListResourceDefinitionsPaginateResponseTypeDef",
    "ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef",
    "ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef",
    "ListSubscriptionDefinitionVersionsPaginateResponseTypeDef",
    "ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef",
    "ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef",
    "ListSubscriptionDefinitionsPaginateResponseTypeDef",
)


_ClientAssociateRoleToGroupResponseTypeDef = TypedDict(
    "_ClientAssociateRoleToGroupResponseTypeDef", {"AssociatedAt": str}, total=False
)


class ClientAssociateRoleToGroupResponseTypeDef(_ClientAssociateRoleToGroupResponseTypeDef):
    """
    - *(dict) --*success

      - **AssociatedAt** *(string) --*The time, in milliseconds since the epoch, when the role ARN
      was associated with the group.
    """


_ClientAssociateServiceRoleToAccountResponseTypeDef = TypedDict(
    "_ClientAssociateServiceRoleToAccountResponseTypeDef", {"AssociatedAt": str}, total=False
)


class ClientAssociateServiceRoleToAccountResponseTypeDef(
    _ClientAssociateServiceRoleToAccountResponseTypeDef
):
    """
    - *(dict) --*success

      - **AssociatedAt** *(string) --*The time when the service role was associated with the
      account.
    """


_RequiredClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef = TypedDict(
    "_RequiredClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef",
    {"ConnectorArn": str, "Id": str},
)
_OptionalClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef = TypedDict(
    "_OptionalClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef",
    {"Parameters": Dict[str, str]},
    total=False,
)


class ClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef(
    _RequiredClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef,
    _OptionalClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef,
):
    """
    - *(dict) --*Information about a connector. Connectors run on the Greengrass core and contain
    built-in integration with local infrastructure, device protocols, AWS, and other cloud services.

      - **ConnectorArn** *(string) --***[REQUIRED]** The ARN of the connector.
      - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the connector. This
      value must be unique within the connector definition version. Max length is 128 characters
      with pattern [a-zA-Z0-9:_-]+.
      - **Parameters** *(dict) --*The parameters or configuration that the connector uses.

        - *(string) --*

          - *(string) --*
    """


_ClientCreateConnectorDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateConnectorDefinitionInitialVersionTypeDef",
    {"Connectors": List[ClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef]},
    total=False,
)


class ClientCreateConnectorDefinitionInitialVersionTypeDef(
    _ClientCreateConnectorDefinitionInitialVersionTypeDef
):
    """
    - **Connectors** *(list) --*A list of references to connectors in this version, with their
    corresponding configuration settings.

      - *(dict) --*Information about a connector. Connectors run on the Greengrass core and contain
      built-in integration with local infrastructure, device protocols, AWS, and other cloud
      services.

        - **ConnectorArn** *(string) --***[REQUIRED]** The ARN of the connector.
        - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the connector. This
        value must be unique within the connector definition version. Max length is 128 characters
        with pattern [a-zA-Z0-9:_-]+.
        - **Parameters** *(dict) --*The parameters or configuration that the connector uses.

          - *(string) --*

            - *(string) --*
    """


_ClientCreateConnectorDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateConnectorDefinitionResponseTypeDef(
    _ClientCreateConnectorDefinitionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
    """


_RequiredClientCreateConnectorDefinitionVersionConnectorsTypeDef = TypedDict(
    "_RequiredClientCreateConnectorDefinitionVersionConnectorsTypeDef",
    {"ConnectorArn": str, "Id": str},
)
_OptionalClientCreateConnectorDefinitionVersionConnectorsTypeDef = TypedDict(
    "_OptionalClientCreateConnectorDefinitionVersionConnectorsTypeDef",
    {"Parameters": Dict[str, str]},
    total=False,
)


class ClientCreateConnectorDefinitionVersionConnectorsTypeDef(
    _RequiredClientCreateConnectorDefinitionVersionConnectorsTypeDef,
    _OptionalClientCreateConnectorDefinitionVersionConnectorsTypeDef,
):
    """
    - *(dict) --*Information about a connector. Connectors run on the Greengrass core and contain
    built-in integration with local infrastructure, device protocols, AWS, and other cloud services.

      - **ConnectorArn** *(string) --***[REQUIRED]** The ARN of the connector.
      - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the connector. This
      value must be unique within the connector definition version. Max length is 128 characters
      with pattern [a-zA-Z0-9:_-]+.
      - **Parameters** *(dict) --*The parameters or configuration that the connector uses.

        - *(string) --*

          - *(string) --*
    """


_ClientCreateConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateConnectorDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateConnectorDefinitionVersionResponseTypeDef(
    _ClientCreateConnectorDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_RequiredClientCreateCoreDefinitionInitialVersionCoresTypeDef = TypedDict(
    "_RequiredClientCreateCoreDefinitionInitialVersionCoresTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateCoreDefinitionInitialVersionCoresTypeDef = TypedDict(
    "_OptionalClientCreateCoreDefinitionInitialVersionCoresTypeDef",
    {"SyncShadow": bool},
    total=False,
)


class ClientCreateCoreDefinitionInitialVersionCoresTypeDef(
    _RequiredClientCreateCoreDefinitionInitialVersionCoresTypeDef,
    _OptionalClientCreateCoreDefinitionInitialVersionCoresTypeDef,
):
    """
    - *(dict) --*Information about a core.

      - **CertificateArn** *(string) --***[REQUIRED]** The ARN of the certificate associated with
      the core.
      - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the core. This value
      must be unique within the core definition version. Max length is 128 characters with pattern
      ''[a-zA-Z0-9:_-]+''.
      - **SyncShadow** *(boolean) --*If true, the core's local shadow is automatically synced with
      the cloud.
      - **ThingArn** *(string) --***[REQUIRED]** The ARN of the thing which is the core.
    """


_ClientCreateCoreDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateCoreDefinitionInitialVersionTypeDef",
    {"Cores": List[ClientCreateCoreDefinitionInitialVersionCoresTypeDef]},
    total=False,
)


class ClientCreateCoreDefinitionInitialVersionTypeDef(
    _ClientCreateCoreDefinitionInitialVersionTypeDef
):
    """
    - **Cores** *(list) --*A list of cores in the core definition version.

      - *(dict) --*Information about a core.

        - **CertificateArn** *(string) --***[REQUIRED]** The ARN of the certificate associated with
        the core.
        - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the core. This value
        must be unique within the core definition version. Max length is 128 characters with pattern
        ''[a-zA-Z0-9:_-]+''.
        - **SyncShadow** *(boolean) --*If true, the core's local shadow is automatically synced with
        the cloud.
        - **ThingArn** *(string) --***[REQUIRED]** The ARN of the thing which is the core.
    """


_ClientCreateCoreDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateCoreDefinitionResponseTypeDef(_ClientCreateCoreDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
    """


_RequiredClientCreateCoreDefinitionVersionCoresTypeDef = TypedDict(
    "_RequiredClientCreateCoreDefinitionVersionCoresTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateCoreDefinitionVersionCoresTypeDef = TypedDict(
    "_OptionalClientCreateCoreDefinitionVersionCoresTypeDef", {"SyncShadow": bool}, total=False
)


class ClientCreateCoreDefinitionVersionCoresTypeDef(
    _RequiredClientCreateCoreDefinitionVersionCoresTypeDef,
    _OptionalClientCreateCoreDefinitionVersionCoresTypeDef,
):
    """
    - *(dict) --*Information about a core.

      - **CertificateArn** *(string) --***[REQUIRED]** The ARN of the certificate associated with
      the core.
      - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the core. This value
      must be unique within the core definition version. Max length is 128 characters with pattern
      ''[a-zA-Z0-9:_-]+''.
      - **SyncShadow** *(boolean) --*If true, the core's local shadow is automatically synced with
      the cloud.
      - **ThingArn** *(string) --***[REQUIRED]** The ARN of the thing which is the core.
    """


_ClientCreateCoreDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateCoreDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateCoreDefinitionVersionResponseTypeDef(
    _ClientCreateCoreDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientCreateDeploymentResponseTypeDef = TypedDict(
    "_ClientCreateDeploymentResponseTypeDef",
    {"DeploymentArn": str, "DeploymentId": str},
    total=False,
)


class ClientCreateDeploymentResponseTypeDef(_ClientCreateDeploymentResponseTypeDef):
    """
    - *(dict) --*Success. The group was deployed.

      - **DeploymentArn** *(string) --*The ARN of the deployment.
      - **DeploymentId** *(string) --*The ID of the deployment.
    """


_RequiredClientCreateDeviceDefinitionInitialVersionDevicesTypeDef = TypedDict(
    "_RequiredClientCreateDeviceDefinitionInitialVersionDevicesTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateDeviceDefinitionInitialVersionDevicesTypeDef = TypedDict(
    "_OptionalClientCreateDeviceDefinitionInitialVersionDevicesTypeDef",
    {"SyncShadow": bool},
    total=False,
)


class ClientCreateDeviceDefinitionInitialVersionDevicesTypeDef(
    _RequiredClientCreateDeviceDefinitionInitialVersionDevicesTypeDef,
    _OptionalClientCreateDeviceDefinitionInitialVersionDevicesTypeDef,
):
    """
    - *(dict) --*Information about a device.

      - **CertificateArn** *(string) --***[REQUIRED]** The ARN of the certificate associated with
      the device.
      - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the device. This value
      must be unique within the device definition version. Max length is 128 characters with pattern
      ''[a-zA-Z0-9:_-]+''.
      - **SyncShadow** *(boolean) --*If true, the device's local shadow will be automatically synced
      with the cloud.
      - **ThingArn** *(string) --***[REQUIRED]** The thing ARN of the device.
    """


_ClientCreateDeviceDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateDeviceDefinitionInitialVersionTypeDef",
    {"Devices": List[ClientCreateDeviceDefinitionInitialVersionDevicesTypeDef]},
    total=False,
)


class ClientCreateDeviceDefinitionInitialVersionTypeDef(
    _ClientCreateDeviceDefinitionInitialVersionTypeDef
):
    """
    - **Devices** *(list) --*A list of devices in the definition version.

      - *(dict) --*Information about a device.

        - **CertificateArn** *(string) --***[REQUIRED]** The ARN of the certificate associated with
        the device.
        - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the device. This
        value must be unique within the device definition version. Max length is 128 characters with
        pattern ''[a-zA-Z0-9:_-]+''.
        - **SyncShadow** *(boolean) --*If true, the device's local shadow will be automatically
        synced with the cloud.
        - **ThingArn** *(string) --***[REQUIRED]** The thing ARN of the device.
    """


_ClientCreateDeviceDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateDeviceDefinitionResponseTypeDef(_ClientCreateDeviceDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
    """


_RequiredClientCreateDeviceDefinitionVersionDevicesTypeDef = TypedDict(
    "_RequiredClientCreateDeviceDefinitionVersionDevicesTypeDef",
    {"CertificateArn": str, "Id": str, "ThingArn": str},
)
_OptionalClientCreateDeviceDefinitionVersionDevicesTypeDef = TypedDict(
    "_OptionalClientCreateDeviceDefinitionVersionDevicesTypeDef", {"SyncShadow": bool}, total=False
)


class ClientCreateDeviceDefinitionVersionDevicesTypeDef(
    _RequiredClientCreateDeviceDefinitionVersionDevicesTypeDef,
    _OptionalClientCreateDeviceDefinitionVersionDevicesTypeDef,
):
    """
    - *(dict) --*Information about a device.

      - **CertificateArn** *(string) --***[REQUIRED]** The ARN of the certificate associated with
      the device.
      - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the device. This value
      must be unique within the device definition version. Max length is 128 characters with pattern
      ''[a-zA-Z0-9:_-]+''.
      - **SyncShadow** *(boolean) --*If true, the device's local shadow will be automatically synced
      with the cloud.
      - **ThingArn** *(string) --***[REQUIRED]** The thing ARN of the device.
    """


_ClientCreateDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateDeviceDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateDeviceDefinitionVersionResponseTypeDef(
    _ClientCreateDeviceDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef
):
    """
    - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running the
    Lambda function. You can specify one or both values to override the default values. We recommend
    that you avoid running as root unless absolutely necessary to minimize the risk of unintended
    changes or malicious attacks. To run as root, you must set ''IsolationMode'' to ''NoContainer''
    and update config.json in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to
    ''yes''.

      - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
      - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef,
    },
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef
):
    """
    - **Execution** *(dict) --*Configuration information that specifies how a Lambda function runs.

      - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a Greengrass
      container (default) or without containerization. Unless your scenario requires that you run
      without containerization, we recommend that you run in a Greengrass container. Omit this value
      to run the Lambda function with the default containerization for the group.
      - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running
      the Lambda function. You can specify one or both values to override the default values. We
      recommend that you avoid running as root unless absolutely necessary to minimize the risk of
      unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
      ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
      ''allowFunctionsToRunAsRoot'' to ''yes''.

        - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
        - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef",
    {"Execution": ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef},
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef
):
    """
    - **DefaultConfig** *(dict) --*The default configuration that applies to all Lambda functions in
    this function definition version. Individual Lambda functions can override these settings.

      - **Execution** *(dict) --*Configuration information that specifies how a Lambda function
      runs.

        - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a Greengrass
        container (default) or without containerization. Unless your scenario requires that you run
        without containerization, we recommend that you run in a Greengrass container. Omit this
        value to run the Lambda function with the default containerization for the group.
        - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running
        the Lambda function. You can specify one or both values to override the default values. We
        recommend that you avoid running as root unless absolutely necessary to minimize the risk of
        unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
        ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
        ''allowFunctionsToRunAsRoot'' to ''yes''.

          - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
          - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef
):
    pass


_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef,
    },
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef
):
    pass


_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    {"Permission": Literal["ro", "rw"], "ResourceId": str},
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef
):
    pass


_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef,
        "ResourceAccessPolicies": List[
            ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef
        ],
        "Variables": Dict[str, str],
    },
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef
):
    pass


_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef",
    {
        "EncodingType": Literal["binary", "json"],
        "Environment": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef,
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef
):
    pass


_ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef,
        "Id": str,
    },
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef
):
    pass


_ClientCreateFunctionDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionInitialVersionTypeDef",
    {
        "DefaultConfig": ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef,
        "Functions": List[ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef],
    },
    total=False,
)


class ClientCreateFunctionDefinitionInitialVersionTypeDef(
    _ClientCreateFunctionDefinitionInitialVersionTypeDef
):
    """
    - **DefaultConfig** *(dict) --*The default configuration that applies to all Lambda functions in
    this function definition version. Individual Lambda functions can override these settings.

      - **Execution** *(dict) --*Configuration information that specifies how a Lambda function
      runs.

        - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a Greengrass
        container (default) or without containerization. Unless your scenario requires that you run
        without containerization, we recommend that you run in a Greengrass container. Omit this
        value to run the Lambda function with the default containerization for the group.
        - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running
        the Lambda function. You can specify one or both values to override the default values. We
        recommend that you avoid running as root unless absolutely necessary to minimize the risk of
        unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
        ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
        ''allowFunctionsToRunAsRoot'' to ''yes''.

          - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
          - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateFunctionDefinitionResponseTypeDef(_ClientCreateFunctionDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
    """


_ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)


class ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef(
    _ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef
):
    """
    - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running the
    Lambda function. You can specify one or both values to override the default values. We recommend
    that you avoid running as root unless absolutely necessary to minimize the risk of unintended
    changes or malicious attacks. To run as root, you must set ''IsolationMode'' to ''NoContainer''
    and update config.json in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to
    ''yes''.

      - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
      - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef,
    },
    total=False,
)


class ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef(
    _ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef
):
    """
    - **Execution** *(dict) --*Configuration information that specifies how a Lambda function runs.

      - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a Greengrass
      container (default) or without containerization. Unless your scenario requires that you run
      without containerization, we recommend that you run in a Greengrass container. Omit this value
      to run the Lambda function with the default containerization for the group.
      - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running
      the Lambda function. You can specify one or both values to override the default values. We
      recommend that you avoid running as root unless absolutely necessary to minimize the risk of
      unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
      ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
      ''allowFunctionsToRunAsRoot'' to ''yes''.

        - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
        - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef",
    {"Execution": ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef},
    total=False,
)


class ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef(
    _ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef
):
    """
    - **Execution** *(dict) --*Configuration information that specifies how a Lambda function runs.

      - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a Greengrass
      container (default) or without containerization. Unless your scenario requires that you run
      without containerization, we recommend that you run in a Greengrass container. Omit this value
      to run the Lambda function with the default containerization for the group.
      - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running
      the Lambda function. You can specify one or both values to override the default values. We
      recommend that you avoid running as root unless absolutely necessary to minimize the risk of
      unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
      ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
      ''allowFunctionsToRunAsRoot'' to ''yes''.

        - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
        - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)


class ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef(
    _ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef
):
    """
    - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running the
    Lambda function. You can specify one or both values to override the default values. We recommend
    that you avoid running as root unless absolutely necessary to minimize the risk of unintended
    changes or malicious attacks. To run as root, you must set ''IsolationMode'' to ''NoContainer''
    and update config.json in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to
    ''yes''.

      - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
      - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef,
    },
    total=False,
)


class ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef(
    _ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef
):
    """
    - **Execution** *(dict) --*Configuration related to executing the Lambda function

      - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a Greengrass
      container (default) or without containerization. Unless your scenario requires that you run
      without containerization, we recommend that you run in a Greengrass container. Omit this value
      to run the Lambda function with the default containerization for the group.
      - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running
      the Lambda function. You can specify one or both values to override the default values. We
      recommend that you avoid running as root unless absolutely necessary to minimize the risk of
      unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
      ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
      ''allowFunctionsToRunAsRoot'' to ''yes''.

        - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
        - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    {"Permission": Literal["ro", "rw"], "ResourceId": str},
    total=False,
)


class ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef(
    _ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef
):
    pass


_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef,
        "ResourceAccessPolicies": List[
            ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef
        ],
        "Variables": Dict[str, str],
    },
    total=False,
)


class ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef(
    _ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef
):
    """
    - **Environment** *(dict) --*The environment configuration of the function.

      - **AccessSysfs** *(boolean) --*If true, the Lambda function is allowed to access the host's
      /sys folder. Use this when the Lambda function needs to read device information from /sys.
      This setting applies only when you run the Lambda function in a Greengrass container.
      - **Execution** *(dict) --*Configuration related to executing the Lambda function

        - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a Greengrass
        container (default) or without containerization. Unless your scenario requires that you run
        without containerization, we recommend that you run in a Greengrass container. Omit this
        value to run the Lambda function with the default containerization for the group.
        - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running
        the Lambda function. You can specify one or both values to override the default values. We
        recommend that you avoid running as root unless absolutely necessary to minimize the risk of
        unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
        ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
        ''allowFunctionsToRunAsRoot'' to ''yes''.

          - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
          - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef",
    {
        "EncodingType": Literal["binary", "json"],
        "Environment": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef,
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)


class ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef(
    _ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef
):
    """
    - **FunctionConfiguration** *(dict) --*The configuration of the Lambda function.

      - **EncodingType** *(string) --*The expected encoding type of the input payload for the
      function. The default is ''json''.
      - **Environment** *(dict) --*The environment configuration of the function.

        - **AccessSysfs** *(boolean) --*If true, the Lambda function is allowed to access the host's
        /sys folder. Use this when the Lambda function needs to read device information from /sys.
        This setting applies only when you run the Lambda function in a Greengrass container.
        - **Execution** *(dict) --*Configuration related to executing the Lambda function

          - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a
          Greengrass container (default) or without containerization. Unless your scenario requires
          that you run without containerization, we recommend that you run in a Greengrass
          container. Omit this value to run the Lambda function with the default containerization
          for the group.
          - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when
          running the Lambda function. You can specify one or both values to override the default
          values. We recommend that you avoid running as root unless absolutely necessary to
          minimize the risk of unintended changes or malicious attacks. To run as root, you must set
          ''IsolationMode'' to ''NoContainer'' and update config.json in ''greengrass-root/config''
          to set ''allowFunctionsToRunAsRoot'' to ''yes''.

            - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda
            function.
            - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientCreateFunctionDefinitionVersionFunctionsTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef,
        "Id": str,
    },
    total=False,
)


class ClientCreateFunctionDefinitionVersionFunctionsTypeDef(
    _ClientCreateFunctionDefinitionVersionFunctionsTypeDef
):
    """
    - *(dict) --*Information about a Lambda function.

      - **FunctionArn** *(string) --*The ARN of the Lambda function.
      - **FunctionConfiguration** *(dict) --*The configuration of the Lambda function.

        - **EncodingType** *(string) --*The expected encoding type of the input payload for the
        function. The default is ''json''.
        - **Environment** *(dict) --*The environment configuration of the function.

          - **AccessSysfs** *(boolean) --*If true, the Lambda function is allowed to access the
          host's /sys folder. Use this when the Lambda function needs to read device information
          from /sys. This setting applies only when you run the Lambda function in a Greengrass
          container.
          - **Execution** *(dict) --*Configuration related to executing the Lambda function

            - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a
            Greengrass container (default) or without containerization. Unless your scenario
            requires that you run without containerization, we recommend that you run in a
            Greengrass container. Omit this value to run the Lambda function with the default
            containerization for the group.
            - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when
            running the Lambda function. You can specify one or both values to override the default
            values. We recommend that you avoid running as root unless absolutely necessary to
            minimize the risk of unintended changes or malicious attacks. To run as root, you must
            set ''IsolationMode'' to ''NoContainer'' and update config.json in
            ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

              - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda
              function.
              - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda
              function.
    """


_ClientCreateFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateFunctionDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateFunctionDefinitionVersionResponseTypeDef(
    _ClientCreateFunctionDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientCreateGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientCreateGroupCertificateAuthorityResponseTypeDef",
    {"GroupCertificateAuthorityArn": str},
    total=False,
)


class ClientCreateGroupCertificateAuthorityResponseTypeDef(
    _ClientCreateGroupCertificateAuthorityResponseTypeDef
):
    """
    - *(dict) --*Success. The response body contains the new active CA ARN.

      - **GroupCertificateAuthorityArn** *(string) --*The ARN of the group certificate authority.
    """


_ClientCreateGroupInitialVersionTypeDef = TypedDict(
    "_ClientCreateGroupInitialVersionTypeDef",
    {
        "ConnectorDefinitionVersionArn": str,
        "CoreDefinitionVersionArn": str,
        "DeviceDefinitionVersionArn": str,
        "FunctionDefinitionVersionArn": str,
        "LoggerDefinitionVersionArn": str,
        "ResourceDefinitionVersionArn": str,
        "SubscriptionDefinitionVersionArn": str,
    },
    total=False,
)


class ClientCreateGroupInitialVersionTypeDef(_ClientCreateGroupInitialVersionTypeDef):
    """
    - **ConnectorDefinitionVersionArn** *(string) --*The ARN of the connector definition version for
    this group.
    - **CoreDefinitionVersionArn** *(string) --*The ARN of the core definition version for this
    group.
    - **DeviceDefinitionVersionArn** *(string) --*The ARN of the device definition version for this
    group.
    - **FunctionDefinitionVersionArn** *(string) --*The ARN of the function definition version for
    this group.
    - **LoggerDefinitionVersionArn** *(string) --*The ARN of the logger definition version for this
    group.
    - **ResourceDefinitionVersionArn** *(string) --*The ARN of the resource definition version for
    this group.
    - **SubscriptionDefinitionVersionArn** *(string) --*The ARN of the subscription definition
    version for this group.
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    - *(dict) --*Success. The group was created.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
    """


_ClientCreateGroupVersionResponseTypeDef = TypedDict(
    "_ClientCreateGroupVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateGroupVersionResponseTypeDef(_ClientCreateGroupVersionResponseTypeDef):
    """
    - *(dict) --*Success. The response contains information about the group version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_RequiredClientCreateLoggerDefinitionInitialVersionLoggersTypeDef = TypedDict(
    "_RequiredClientCreateLoggerDefinitionInitialVersionLoggersTypeDef",
    {
        "Component": Literal["GreengrassSystem", "Lambda"],
        "Id": str,
        "Level": Literal["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
        "Type": Literal["FileSystem", "AWSCloudWatch"],
    },
)
_OptionalClientCreateLoggerDefinitionInitialVersionLoggersTypeDef = TypedDict(
    "_OptionalClientCreateLoggerDefinitionInitialVersionLoggersTypeDef", {"Space": int}, total=False
)


class ClientCreateLoggerDefinitionInitialVersionLoggersTypeDef(
    _RequiredClientCreateLoggerDefinitionInitialVersionLoggersTypeDef,
    _OptionalClientCreateLoggerDefinitionInitialVersionLoggersTypeDef,
):
    """
    - *(dict) --*Information about a logger

      - **Component** *(string) --***[REQUIRED]** The component that will be subject to logging.
      - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the logger. This value
      must be unique within the logger definition version. Max length is 128 characters with pattern
      ''[a-zA-Z0-9:_-]+''.
      - **Level** *(string) --***[REQUIRED]** The level of the logs.
      - **Space** *(integer) --*The amount of file space, in KB, to use if the local file system is
      used for logging purposes.
      - **Type** *(string) --***[REQUIRED]** The type of log output which will be used.
    """


_ClientCreateLoggerDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateLoggerDefinitionInitialVersionTypeDef",
    {"Loggers": List[ClientCreateLoggerDefinitionInitialVersionLoggersTypeDef]},
    total=False,
)


class ClientCreateLoggerDefinitionInitialVersionTypeDef(
    _ClientCreateLoggerDefinitionInitialVersionTypeDef
):
    """
    - **Loggers** *(list) --*A list of loggers.

      - *(dict) --*Information about a logger

        - **Component** *(string) --***[REQUIRED]** The component that will be subject to logging.
        - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the logger. This
        value must be unique within the logger definition version. Max length is 128 characters with
        pattern ''[a-zA-Z0-9:_-]+''.
        - **Level** *(string) --***[REQUIRED]** The level of the logs.
        - **Space** *(integer) --*The amount of file space, in KB, to use if the local file system
        is used for logging purposes.
        - **Type** *(string) --***[REQUIRED]** The type of log output which will be used.
    """


_ClientCreateLoggerDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateLoggerDefinitionResponseTypeDef(_ClientCreateLoggerDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
    """


_RequiredClientCreateLoggerDefinitionVersionLoggersTypeDef = TypedDict(
    "_RequiredClientCreateLoggerDefinitionVersionLoggersTypeDef",
    {
        "Component": Literal["GreengrassSystem", "Lambda"],
        "Id": str,
        "Level": Literal["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
        "Type": Literal["FileSystem", "AWSCloudWatch"],
    },
)
_OptionalClientCreateLoggerDefinitionVersionLoggersTypeDef = TypedDict(
    "_OptionalClientCreateLoggerDefinitionVersionLoggersTypeDef", {"Space": int}, total=False
)


class ClientCreateLoggerDefinitionVersionLoggersTypeDef(
    _RequiredClientCreateLoggerDefinitionVersionLoggersTypeDef,
    _OptionalClientCreateLoggerDefinitionVersionLoggersTypeDef,
):
    """
    - *(dict) --*Information about a logger

      - **Component** *(string) --***[REQUIRED]** The component that will be subject to logging.
      - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the logger. This value
      must be unique within the logger definition version. Max length is 128 characters with pattern
      ''[a-zA-Z0-9:_-]+''.
      - **Level** *(string) --***[REQUIRED]** The level of the logs.
      - **Space** *(integer) --*The amount of file space, in KB, to use if the local file system is
      used for logging purposes.
      - **Type** *(string) --***[REQUIRED]** The type of log output which will be used.
    """


_ClientCreateLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateLoggerDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateLoggerDefinitionVersionResponseTypeDef(
    _ClientCreateLoggerDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef
):
    """
    - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

      - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
      specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
      Lambda process will have the file access permissions of the added Linux group.
      - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be added to
      the Lambda process. This field is optional.
    """


_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef
):
    """
    - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device resource.

      - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

        - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
        specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
        Lambda process will have the file access permissions of the added Linux group.
        - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be added
        to the Lambda process. This field is optional.
    """


_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef
):
    pass


_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef
):
    pass


_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef
):
    pass


_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef,
        "S3Uri": str,
    },
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef
):
    pass


_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef
):
    pass


_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef,
        "SageMakerJobArn": str,
    },
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef
):
    pass


_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    {"ARN": str, "AdditionalStagingLabelsToDownload": List[str]},
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef
):
    pass


_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef,
        "LocalVolumeResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef,
        "S3MachineLearningModelResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef,
        "SageMakerMachineLearningModelResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef,
        "SecretsManagerSecretResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef,
    },
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef
):
    """
    - **ResourceDataContainer** *(dict) --***[REQUIRED]** A container of data for all resource
    types.

      - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device resource.

        - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

          - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
          specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
          Lambda process will have the file access permissions of the added Linux group.
          - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be
          added to the Lambda process. This field is optional.
    """


_ClientCreateResourceDefinitionInitialVersionResourcesTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionResourcesTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef,
    },
)


class ClientCreateResourceDefinitionInitialVersionResourcesTypeDef(
    _ClientCreateResourceDefinitionInitialVersionResourcesTypeDef
):
    """
    - *(dict) --*Information about a resource.

      - **Id** *(string) --***[REQUIRED]** The resource ID, used to refer to a resource in the
      Lambda function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
      This must be unique within a Greengrass group.
      - **Name** *(string) --***[REQUIRED]** The descriptive resource name, which is displayed on
      the AWS IoT Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
      This must be unique within a Greengrass group.
      - **ResourceDataContainer** *(dict) --***[REQUIRED]** A container of data for all resource
      types.

        - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device resource.

          - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

            - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
            specified Linux OS group owner of the resource to the Lambda process privileges. Thus
            the Lambda process will have the file access permissions of the added Linux group.
            - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be
            added to the Lambda process. This field is optional.
    """


_ClientCreateResourceDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionInitialVersionTypeDef",
    {"Resources": List[ClientCreateResourceDefinitionInitialVersionResourcesTypeDef]},
    total=False,
)


class ClientCreateResourceDefinitionInitialVersionTypeDef(
    _ClientCreateResourceDefinitionInitialVersionTypeDef
):
    """
    - **Resources** *(list) --*A list of resources.

      - *(dict) --*Information about a resource.

        - **Id** *(string) --***[REQUIRED]** The resource ID, used to refer to a resource in the
        Lambda function configuration. Max length is 128 characters with pattern
        ''[a-zA-Z0-9:_-]+''. This must be unique within a Greengrass group.
        - **Name** *(string) --***[REQUIRED]** The descriptive resource name, which is displayed on
        the AWS IoT Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
        This must be unique within a Greengrass group.
        - **ResourceDataContainer** *(dict) --***[REQUIRED]** A container of data for all resource
        types.

          - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device resource.

            - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

              - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds
              the specified Linux OS group owner of the resource to the Lambda process privileges.
              Thus the Lambda process will have the file access permissions of the added Linux
              group.
              - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be
              added to the Lambda process. This field is optional.
    """


_ClientCreateResourceDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateResourceDefinitionResponseTypeDef(_ClientCreateResourceDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
    """


_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)


class ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef
):
    """
    - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

      - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
      specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
      Lambda process will have the file access permissions of the added Linux group.
      - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be added to
      the Lambda process. This field is optional.
    """


_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)


class ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef
):
    """
    - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device resource.

      - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

        - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
        specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
        Lambda process will have the file access permissions of the added Linux group.
        - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be added
        to the Lambda process. This field is optional.
    """


_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)


class ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef
):
    pass


_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)


class ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef
):
    pass


_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)


class ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef
):
    pass


_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef,
        "S3Uri": str,
    },
    total=False,
)


class ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef
):
    pass


_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)


class ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef
):
    pass


_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef,
        "SageMakerJobArn": str,
    },
    total=False,
)


class ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef
):
    pass


_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    {"ARN": str, "AdditionalStagingLabelsToDownload": List[str]},
    total=False,
)


class ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef
):
    pass


_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef,
        "LocalVolumeResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef,
        "S3MachineLearningModelResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef,
        "SageMakerMachineLearningModelResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef,
        "SecretsManagerSecretResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef,
    },
    total=False,
)


class ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef
):
    """
    - **ResourceDataContainer** *(dict) --***[REQUIRED]** A container of data for all resource
    types.

      - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device resource.

        - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

          - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
          specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
          Lambda process will have the file access permissions of the added Linux group.
          - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be
          added to the Lambda process. This field is optional.
    """


_ClientCreateResourceDefinitionVersionResourcesTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResourcesTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef,
    },
)


class ClientCreateResourceDefinitionVersionResourcesTypeDef(
    _ClientCreateResourceDefinitionVersionResourcesTypeDef
):
    """
    - *(dict) --*Information about a resource.

      - **Id** *(string) --***[REQUIRED]** The resource ID, used to refer to a resource in the
      Lambda function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
      This must be unique within a Greengrass group.
      - **Name** *(string) --***[REQUIRED]** The descriptive resource name, which is displayed on
      the AWS IoT Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
      This must be unique within a Greengrass group.
      - **ResourceDataContainer** *(dict) --***[REQUIRED]** A container of data for all resource
      types.

        - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device resource.

          - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

            - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
            specified Linux OS group owner of the resource to the Lambda process privileges. Thus
            the Lambda process will have the file access permissions of the added Linux group.
            - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be
            added to the Lambda process. This field is optional.
    """


_ClientCreateResourceDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateResourceDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateResourceDefinitionVersionResponseTypeDef(
    _ClientCreateResourceDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientCreateSoftwareUpdateJobResponseTypeDef = TypedDict(
    "_ClientCreateSoftwareUpdateJobResponseTypeDef",
    {"IotJobArn": str, "IotJobId": str, "PlatformSoftwareVersion": str},
    total=False,
)


class ClientCreateSoftwareUpdateJobResponseTypeDef(_ClientCreateSoftwareUpdateJobResponseTypeDef):
    """
    - *(dict) --*success

      - **IotJobArn** *(string) --*The IoT Job ARN corresponding to this update.
      - **IotJobId** *(string) --*The IoT Job Id corresponding to this update.
      - **PlatformSoftwareVersion** *(string) --*The software version installed on the device or
      devices after the update.
    """


_ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef = TypedDict(
    "_ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
)


class ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef(
    _ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef
):
    """
    - *(dict) --*Information about a subscription.

      - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the subscription. This
      value must be unique within the subscription definition version. Max length is 128 characters
      with pattern ''[a-zA-Z0-9:_-]+''.
      - **Source** *(string) --***[REQUIRED]** The source of the subscription. Can be a thing ARN, a
      Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
      'GGShadowService'.
      - **Subject** *(string) --***[REQUIRED]** The MQTT topic used to route the message.
      - **Target** *(string) --***[REQUIRED]** Where the message is sent to. Can be a thing ARN, a
      Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
      'GGShadowService'.
    """


_ClientCreateSubscriptionDefinitionInitialVersionTypeDef = TypedDict(
    "_ClientCreateSubscriptionDefinitionInitialVersionTypeDef",
    {"Subscriptions": List[ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef]},
    total=False,
)


class ClientCreateSubscriptionDefinitionInitialVersionTypeDef(
    _ClientCreateSubscriptionDefinitionInitialVersionTypeDef
):
    """
    - **Subscriptions** *(list) --*A list of subscriptions.

      - *(dict) --*Information about a subscription.

        - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the subscription.
        This value must be unique within the subscription definition version. Max length is 128
        characters with pattern ''[a-zA-Z0-9:_-]+''.
        - **Source** *(string) --***[REQUIRED]** The source of the subscription. Can be a thing ARN,
        a Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
        'GGShadowService'.
        - **Subject** *(string) --***[REQUIRED]** The MQTT topic used to route the message.
        - **Target** *(string) --***[REQUIRED]** Where the message is sent to. Can be a thing ARN, a
        Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
        'GGShadowService'.
    """


_ClientCreateSubscriptionDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientCreateSubscriptionDefinitionResponseTypeDef(
    _ClientCreateSubscriptionDefinitionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
    """


_ClientCreateSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientCreateSubscriptionDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientCreateSubscriptionDefinitionVersionResponseTypeDef(
    _ClientCreateSubscriptionDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef = TypedDict(
    "_ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
)


class ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef(
    _ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef
):
    """
    - *(dict) --*Information about a subscription.

      - **Id** *(string) --***[REQUIRED]** A descriptive or arbitrary ID for the subscription. This
      value must be unique within the subscription definition version. Max length is 128 characters
      with pattern ''[a-zA-Z0-9:_-]+''.
      - **Source** *(string) --***[REQUIRED]** The source of the subscription. Can be a thing ARN, a
      Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
      'GGShadowService'.
      - **Subject** *(string) --***[REQUIRED]** The MQTT topic used to route the message.
      - **Target** *(string) --***[REQUIRED]** Where the message is sent to. Can be a thing ARN, a
      Lambda function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
      'GGShadowService'.
    """


_ClientDisassociateRoleFromGroupResponseTypeDef = TypedDict(
    "_ClientDisassociateRoleFromGroupResponseTypeDef", {"DisassociatedAt": str}, total=False
)


class ClientDisassociateRoleFromGroupResponseTypeDef(
    _ClientDisassociateRoleFromGroupResponseTypeDef
):
    """
    - *(dict) --*success

      - **DisassociatedAt** *(string) --*The time, in milliseconds since the epoch, when the role
      was disassociated from the group.
    """


_ClientDisassociateServiceRoleFromAccountResponseTypeDef = TypedDict(
    "_ClientDisassociateServiceRoleFromAccountResponseTypeDef",
    {"DisassociatedAt": str},
    total=False,
)


class ClientDisassociateServiceRoleFromAccountResponseTypeDef(
    _ClientDisassociateServiceRoleFromAccountResponseTypeDef
):
    """
    - *(dict) --*success

      - **DisassociatedAt** *(string) --*The time when the service role was disassociated from the
      account.
    """


_ClientGetAssociatedRoleResponseTypeDef = TypedDict(
    "_ClientGetAssociatedRoleResponseTypeDef", {"AssociatedAt": str, "RoleArn": str}, total=False
)


class ClientGetAssociatedRoleResponseTypeDef(_ClientGetAssociatedRoleResponseTypeDef):
    """
    - *(dict) --*success

      - **AssociatedAt** *(string) --*The time when the role was associated with the group.
      - **RoleArn** *(string) --*The ARN of the role that is associated with the group.
    """


_ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef = TypedDict(
    "_ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef",
    {"InvalidInputRecords": int, "RecordsProcessed": int, "RetryAttempts": int},
    total=False,
)


class ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef(
    _ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef
):
    """
    - **BulkDeploymentMetrics** *(dict) --*Relevant metrics on input records processed during bulk
    deployment.

      - **InvalidInputRecords** *(integer) --*The total number of records that returned a
      non-retryable error. For example, this can occur if a group record from the input file uses an
      invalid format or specifies a nonexistent group version, or if the execution role doesn't
      grant permission to deploy a group or group version.
      - **RecordsProcessed** *(integer) --*The total number of group records from the input file
      that have been processed so far, or attempted.
      - **RetryAttempts** *(integer) --*The total number of deployment attempts that returned a
      retryable error. For example, a retry is triggered if the attempt to deploy a group returns a
      throttling error. ''StartBulkDeployment'' retries a group deployment up to five times.
    """


_ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef = TypedDict(
    "_ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)


class ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef(
    _ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef
):
    pass


_ClientGetBulkDeploymentStatusResponseTypeDef = TypedDict(
    "_ClientGetBulkDeploymentStatusResponseTypeDef",
    {
        "BulkDeploymentMetrics": ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef,
        "BulkDeploymentStatus": Literal[
            "Initializing", "Running", "Completed", "Stopping", "Stopped", "Failed"
        ],
        "CreatedAt": str,
        "ErrorDetails": List[ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef],
        "ErrorMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetBulkDeploymentStatusResponseTypeDef(_ClientGetBulkDeploymentStatusResponseTypeDef):
    """
    - *(dict) --*Success. The response body contains the status of the bulk deployment.

      - **BulkDeploymentMetrics** *(dict) --*Relevant metrics on input records processed during bulk
      deployment.

        - **InvalidInputRecords** *(integer) --*The total number of records that returned a
        non-retryable error. For example, this can occur if a group record from the input file uses
        an invalid format or specifies a nonexistent group version, or if the execution role doesn't
        grant permission to deploy a group or group version.
        - **RecordsProcessed** *(integer) --*The total number of group records from the input file
        that have been processed so far, or attempted.
        - **RetryAttempts** *(integer) --*The total number of deployment attempts that returned a
        retryable error. For example, a retry is triggered if the attempt to deploy a group returns
        a throttling error. ''StartBulkDeployment'' retries a group deployment up to five times.
    """


_ClientGetConnectivityInfoResponseConnectivityInfoTypeDef = TypedDict(
    "_ClientGetConnectivityInfoResponseConnectivityInfoTypeDef",
    {"HostAddress": str, "Id": str, "Metadata": str, "PortNumber": int},
    total=False,
)


class ClientGetConnectivityInfoResponseConnectivityInfoTypeDef(
    _ClientGetConnectivityInfoResponseConnectivityInfoTypeDef
):
    """
    - *(dict) --*Information about a Greengrass core's connectivity.

      - **HostAddress** *(string) --*The endpoint for the Greengrass core. Can be an IP address or
      DNS.
      - **Id** *(string) --*The ID of the connectivity information.
      - **Metadata** *(string) --*Metadata for this endpoint.
      - **PortNumber** *(integer) --*The port of the Greengrass core. Usually 8883.
    """


_ClientGetConnectivityInfoResponseTypeDef = TypedDict(
    "_ClientGetConnectivityInfoResponseTypeDef",
    {
        "ConnectivityInfo": List[ClientGetConnectivityInfoResponseConnectivityInfoTypeDef],
        "Message": str,
    },
    total=False,
)


class ClientGetConnectivityInfoResponseTypeDef(_ClientGetConnectivityInfoResponseTypeDef):
    """
    - *(dict) --*success

      - **ConnectivityInfo** *(list) --*Connectivity info list.

        - *(dict) --*Information about a Greengrass core's connectivity.

          - **HostAddress** *(string) --*The endpoint for the Greengrass core. Can be an IP address
          or DNS.
          - **Id** *(string) --*The ID of the connectivity information.
          - **Metadata** *(string) --*Metadata for this endpoint.
          - **PortNumber** *(integer) --*The port of the Greengrass core. Usually 8883.
    """


_ClientGetConnectorDefinitionResponseTypeDef = TypedDict(
    "_ClientGetConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetConnectorDefinitionResponseTypeDef(_ClientGetConnectorDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef = TypedDict(
    "_ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef",
    {"ConnectorArn": str, "Id": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef(
    _ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef
):
    """
    - *(dict) --*Information about a connector. Connectors run on the Greengrass core and contain
    built-in integration with local infrastructure, device protocols, AWS, and other cloud services.

      - **ConnectorArn** *(string) --*The ARN of the connector.
      - **Id** *(string) --*A descriptive or arbitrary ID for the connector. This value must be
      unique within the connector definition version. Max length is 128 characters with pattern
      [a-zA-Z0-9:_-]+.
      - **Parameters** *(dict) --*The parameters or configuration that the connector uses.

        - *(string) --*

          - *(string) --*
    """


_ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef",
    {"Connectors": List[ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef]},
    total=False,
)


class ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef
):
    """
    - **Definition** *(dict) --*Information about the connector definition version.

      - **Connectors** *(list) --*A list of references to connectors in this version, with their
      corresponding configuration settings.

        - *(dict) --*Information about a connector. Connectors run on the Greengrass core and
        contain built-in integration with local infrastructure, device protocols, AWS, and other
        cloud services.

          - **ConnectorArn** *(string) --*The ARN of the connector.
          - **Id** *(string) --*A descriptive or arbitrary ID for the connector. This value must be
          unique within the connector definition version. Max length is 128 characters with pattern
          [a-zA-Z0-9:_-]+.
          - **Parameters** *(dict) --*The parameters or configuration that the connector uses.

            - *(string) --*

              - *(string) --*
    """


_ClientGetConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetConnectorDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)


class ClientGetConnectorDefinitionVersionResponseTypeDef(
    _ClientGetConnectorDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the connector definition version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      connector definition version was created.
      - **Definition** *(dict) --*Information about the connector definition version.

        - **Connectors** *(list) --*A list of references to connectors in this version, with their
        corresponding configuration settings.

          - *(dict) --*Information about a connector. Connectors run on the Greengrass core and
          contain built-in integration with local infrastructure, device protocols, AWS, and other
          cloud services.

            - **ConnectorArn** *(string) --*The ARN of the connector.
            - **Id** *(string) --*A descriptive or arbitrary ID for the connector. This value must
            be unique within the connector definition version. Max length is 128 characters with
            pattern [a-zA-Z0-9:_-]+.
            - **Parameters** *(dict) --*The parameters or configuration that the connector uses.

              - *(string) --*

                - *(string) --*
    """


_ClientGetCoreDefinitionResponseTypeDef = TypedDict(
    "_ClientGetCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetCoreDefinitionResponseTypeDef(_ClientGetCoreDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef = TypedDict(
    "_ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef",
    {"CertificateArn": str, "Id": str, "SyncShadow": bool, "ThingArn": str},
    total=False,
)


class ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef(
    _ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef
):
    """
    - *(dict) --*Information about a core.

      - **CertificateArn** *(string) --*The ARN of the certificate associated with the core.
      - **Id** *(string) --*A descriptive or arbitrary ID for the core. This value must be unique
      within the core definition version. Max length is 128 characters with pattern
      ''[a-zA-Z0-9:_-]+''.
      - **SyncShadow** *(boolean) --*If true, the core's local shadow is automatically synced with
      the cloud.
      - **ThingArn** *(string) --*The ARN of the thing which is the core.
    """


_ClientGetCoreDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetCoreDefinitionVersionResponseDefinitionTypeDef",
    {"Cores": List[ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef]},
    total=False,
)


class ClientGetCoreDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetCoreDefinitionVersionResponseDefinitionTypeDef
):
    """
    - **Definition** *(dict) --*Information about the core definition version.

      - **Cores** *(list) --*A list of cores in the core definition version.

        - *(dict) --*Information about a core.

          - **CertificateArn** *(string) --*The ARN of the certificate associated with the core.
          - **Id** *(string) --*A descriptive or arbitrary ID for the core. This value must be
          unique within the core definition version. Max length is 128 characters with pattern
          ''[a-zA-Z0-9:_-]+''.
          - **SyncShadow** *(boolean) --*If true, the core's local shadow is automatically synced
          with the cloud.
          - **ThingArn** *(string) --*The ARN of the thing which is the core.
    """


_ClientGetCoreDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetCoreDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetCoreDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)


class ClientGetCoreDefinitionVersionResponseTypeDef(_ClientGetCoreDefinitionVersionResponseTypeDef):
    """
    - *(dict) --*success

      - **Arn** *(string) --*The ARN of the core definition version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the core
      definition version was created.
      - **Definition** *(dict) --*Information about the core definition version.

        - **Cores** *(list) --*A list of cores in the core definition version.

          - *(dict) --*Information about a core.

            - **CertificateArn** *(string) --*The ARN of the certificate associated with the core.
            - **Id** *(string) --*A descriptive or arbitrary ID for the core. This value must be
            unique within the core definition version. Max length is 128 characters with pattern
            ''[a-zA-Z0-9:_-]+''.
            - **SyncShadow** *(boolean) --*If true, the core's local shadow is automatically synced
            with the cloud.
            - **ThingArn** *(string) --*The ARN of the thing which is the core.
    """


_ClientGetDeploymentStatusResponseErrorDetailsTypeDef = TypedDict(
    "_ClientGetDeploymentStatusResponseErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)


class ClientGetDeploymentStatusResponseErrorDetailsTypeDef(
    _ClientGetDeploymentStatusResponseErrorDetailsTypeDef
):
    """
    - *(dict) --*Details about the error.

      - **DetailedErrorCode** *(string) --*A detailed error code.
      - **DetailedErrorMessage** *(string) --*A detailed error message.
    """


_ClientGetDeploymentStatusResponseTypeDef = TypedDict(
    "_ClientGetDeploymentStatusResponseTypeDef",
    {
        "DeploymentStatus": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "ErrorDetails": List[ClientGetDeploymentStatusResponseErrorDetailsTypeDef],
        "ErrorMessage": str,
        "UpdatedAt": str,
    },
    total=False,
)


class ClientGetDeploymentStatusResponseTypeDef(_ClientGetDeploymentStatusResponseTypeDef):
    """
    - *(dict) --*Success. The response body contains the status of the deployment for the group.

      - **DeploymentStatus** *(string) --*The status of the deployment: ''InProgress'',
      ''Building'', ''Success'', or ''Failure''.
      - **DeploymentType** *(string) --*The type of the deployment.
      - **ErrorDetails** *(list) --*Error details

        - *(dict) --*Details about the error.

          - **DetailedErrorCode** *(string) --*A detailed error code.
          - **DetailedErrorMessage** *(string) --*A detailed error message.
    """


_ClientGetDeviceDefinitionResponseTypeDef = TypedDict(
    "_ClientGetDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetDeviceDefinitionResponseTypeDef(_ClientGetDeviceDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef = TypedDict(
    "_ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef",
    {"CertificateArn": str, "Id": str, "SyncShadow": bool, "ThingArn": str},
    total=False,
)


class ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef(
    _ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef
):
    """
    - *(dict) --*Information about a device.

      - **CertificateArn** *(string) --*The ARN of the certificate associated with the device.
      - **Id** *(string) --*A descriptive or arbitrary ID for the device. This value must be unique
      within the device definition version. Max length is 128 characters with pattern
      ''[a-zA-Z0-9:_-]+''.
      - **SyncShadow** *(boolean) --*If true, the device's local shadow will be automatically synced
      with the cloud.
      - **ThingArn** *(string) --*The thing ARN of the device.
    """


_ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef",
    {"Devices": List[ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef]},
    total=False,
)


class ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef
):
    """
    - **Definition** *(dict) --*Information about the device definition version.

      - **Devices** *(list) --*A list of devices in the definition version.

        - *(dict) --*Information about a device.

          - **CertificateArn** *(string) --*The ARN of the certificate associated with the device.
          - **Id** *(string) --*A descriptive or arbitrary ID for the device. This value must be
          unique within the device definition version. Max length is 128 characters with pattern
          ''[a-zA-Z0-9:_-]+''.
          - **SyncShadow** *(boolean) --*If true, the device's local shadow will be automatically
          synced with the cloud.
          - **ThingArn** *(string) --*The thing ARN of the device.
    """


_ClientGetDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetDeviceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)


class ClientGetDeviceDefinitionVersionResponseTypeDef(
    _ClientGetDeviceDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the device definition version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      device definition version was created.
      - **Definition** *(dict) --*Information about the device definition version.

        - **Devices** *(list) --*A list of devices in the definition version.

          - *(dict) --*Information about a device.

            - **CertificateArn** *(string) --*The ARN of the certificate associated with the device.
            - **Id** *(string) --*A descriptive or arbitrary ID for the device. This value must be
            unique within the device definition version. Max length is 128 characters with pattern
            ''[a-zA-Z0-9:_-]+''.
            - **SyncShadow** *(boolean) --*If true, the device's local shadow will be automatically
            synced with the cloud.
            - **ThingArn** *(string) --*The thing ARN of the device.
    """


_ClientGetFunctionDefinitionResponseTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetFunctionDefinitionResponseTypeDef(_ClientGetFunctionDefinitionResponseTypeDef):
    """
    - *(dict) --*success

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef
):
    """
    - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running the
    Lambda function. You can specify one or both values to override the default values. We recommend
    that you avoid running as root unless absolutely necessary to minimize the risk of unintended
    changes or malicious attacks. To run as root, you must set ''IsolationMode'' to ''NoContainer''
    and update config.json in ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to
    ''yes''.

      - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
      - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef,
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef
):
    """
    - **Execution** *(dict) --*Configuration information that specifies how a Lambda function runs.

      - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a Greengrass
      container (default) or without containerization. Unless your scenario requires that you run
      without containerization, we recommend that you run in a Greengrass container. Omit this value
      to run the Lambda function with the default containerization for the group.
      - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running
      the Lambda function. You can specify one or both values to override the default values. We
      recommend that you avoid running as root unless absolutely necessary to minimize the risk of
      unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
      ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
      ''allowFunctionsToRunAsRoot'' to ''yes''.

        - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
        - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef",
    {
        "Execution": ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef
):
    """
    - **DefaultConfig** *(dict) --*The default configuration that applies to all Lambda functions in
    this function definition version. Individual Lambda functions can override these settings.

      - **Execution** *(dict) --*Configuration information that specifies how a Lambda function
      runs.

        - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a Greengrass
        container (default) or without containerization. Unless your scenario requires that you run
        without containerization, we recommend that you run in a Greengrass container. Omit this
        value to run the Lambda function with the default containerization for the group.
        - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when running
        the Lambda function. You can specify one or both values to override the default values. We
        recommend that you avoid running as root unless absolutely necessary to minimize the risk of
        unintended changes or malicious attacks. To run as root, you must set ''IsolationMode'' to
        ''NoContainer'' and update config.json in ''greengrass-root/config'' to set
        ''allowFunctionsToRunAsRoot'' to ''yes''.

          - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda function.
          - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef
):
    pass


_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef,
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef
):
    pass


_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    {"Permission": Literal["ro", "rw"], "ResourceId": str},
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef
):
    pass


_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef,
        "ResourceAccessPolicies": List[
            ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef
        ],
        "Variables": Dict[str, str],
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef
):
    pass


_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef",
    {
        "EncodingType": Literal["binary", "json"],
        "Environment": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef,
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef
):
    pass


_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef,
        "Id": str,
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef
):
    pass


_ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef",
    {
        "DefaultConfig": ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef,
        "Functions": List[ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef],
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef
):
    """
    - **Definition** *(dict) --*Information on the definition.

      - **DefaultConfig** *(dict) --*The default configuration that applies to all Lambda functions
      in this function definition version. Individual Lambda functions can override these settings.

        - **Execution** *(dict) --*Configuration information that specifies how a Lambda function
        runs.

          - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a
          Greengrass container (default) or without containerization. Unless your scenario requires
          that you run without containerization, we recommend that you run in a Greengrass
          container. Omit this value to run the Lambda function with the default containerization
          for the group.
          - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when
          running the Lambda function. You can specify one or both values to override the default
          values. We recommend that you avoid running as root unless absolutely necessary to
          minimize the risk of unintended changes or malicious attacks. To run as root, you must set
          ''IsolationMode'' to ''NoContainer'' and update config.json in ''greengrass-root/config''
          to set ''allowFunctionsToRunAsRoot'' to ''yes''.

            - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda
            function.
            - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda function.
    """


_ClientGetFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetFunctionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)


class ClientGetFunctionDefinitionVersionResponseTypeDef(
    _ClientGetFunctionDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*success

      - **Arn** *(string) --*The ARN of the function definition version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      function definition version was created.
      - **Definition** *(dict) --*Information on the definition.

        - **DefaultConfig** *(dict) --*The default configuration that applies to all Lambda
        functions in this function definition version. Individual Lambda functions can override
        these settings.

          - **Execution** *(dict) --*Configuration information that specifies how a Lambda function
          runs.

            - **IsolationMode** *(string) --*Specifies whether the Lambda function runs in a
            Greengrass container (default) or without containerization. Unless your scenario
            requires that you run without containerization, we recommend that you run in a
            Greengrass container. Omit this value to run the Lambda function with the default
            containerization for the group.
            - **RunAs** *(dict) --*Specifies the user and group whose permissions are used when
            running the Lambda function. You can specify one or both values to override the default
            values. We recommend that you avoid running as root unless absolutely necessary to
            minimize the risk of unintended changes or malicious attacks. To run as root, you must
            set ''IsolationMode'' to ''NoContainer'' and update config.json in
            ''greengrass-root/config'' to set ''allowFunctionsToRunAsRoot'' to ''yes''.

              - **Gid** *(integer) --*The group ID whose permissions are used to run a Lambda
              function.
              - **Uid** *(integer) --*The user ID whose permissions are used to run a Lambda
              function.
    """


_ClientGetGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientGetGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
        "PemEncodedCertificate": str,
    },
    total=False,
)


class ClientGetGroupCertificateAuthorityResponseTypeDef(
    _ClientGetGroupCertificateAuthorityResponseTypeDef
):
    """
    - *(dict) --*Success. The response body contains the PKI Configuration.

      - **GroupCertificateAuthorityArn** *(string) --*The ARN of the certificate authority for the
      group.
      - **GroupCertificateAuthorityId** *(string) --*The ID of the certificate authority for the
      group.
      - **PemEncodedCertificate** *(string) --*The PEM encoded certificate for the group.
    """


_ClientGetGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "_ClientGetGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
    },
    total=False,
)


class ClientGetGroupCertificateConfigurationResponseTypeDef(
    _ClientGetGroupCertificateConfigurationResponseTypeDef
):
    """
    - *(dict) --*Success. The response body contains the PKI Configuration.

      - **CertificateAuthorityExpiryInMilliseconds** *(string) --*The amount of time remaining
      before the certificate authority expires, in milliseconds.
      - **CertificateExpiryInMilliseconds** *(string) --*The amount of time remaining before the
      certificate expires, in milliseconds.
      - **GroupId** *(string) --*The ID of the group certificate configuration.
    """


_ClientGetGroupResponseTypeDef = TypedDict(
    "_ClientGetGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetGroupResponseTypeDef(_ClientGetGroupResponseTypeDef):
    """
    - *(dict) --*success

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientGetGroupVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetGroupVersionResponseDefinitionTypeDef",
    {
        "ConnectorDefinitionVersionArn": str,
        "CoreDefinitionVersionArn": str,
        "DeviceDefinitionVersionArn": str,
        "FunctionDefinitionVersionArn": str,
        "LoggerDefinitionVersionArn": str,
        "ResourceDefinitionVersionArn": str,
        "SubscriptionDefinitionVersionArn": str,
    },
    total=False,
)


class ClientGetGroupVersionResponseDefinitionTypeDef(
    _ClientGetGroupVersionResponseDefinitionTypeDef
):
    """
    - **Definition** *(dict) --*Information about the group version definition.

      - **ConnectorDefinitionVersionArn** *(string) --*The ARN of the connector definition version
      for this group.
      - **CoreDefinitionVersionArn** *(string) --*The ARN of the core definition version for this
      group.
      - **DeviceDefinitionVersionArn** *(string) --*The ARN of the device definition version for
      this group.
      - **FunctionDefinitionVersionArn** *(string) --*The ARN of the function definition version for
      this group.
      - **LoggerDefinitionVersionArn** *(string) --*The ARN of the logger definition version for
      this group.
      - **ResourceDefinitionVersionArn** *(string) --*The ARN of the resource definition version for
      this group.
      - **SubscriptionDefinitionVersionArn** *(string) --*The ARN of the subscription definition
      version for this group.
    """


_ClientGetGroupVersionResponseTypeDef = TypedDict(
    "_ClientGetGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetGroupVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)


class ClientGetGroupVersionResponseTypeDef(_ClientGetGroupVersionResponseTypeDef):
    """
    - *(dict) --*success

      - **Arn** *(string) --*The ARN of the group version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the group
      version was created.
      - **Definition** *(dict) --*Information about the group version definition.

        - **ConnectorDefinitionVersionArn** *(string) --*The ARN of the connector definition version
        for this group.
        - **CoreDefinitionVersionArn** *(string) --*The ARN of the core definition version for this
        group.
        - **DeviceDefinitionVersionArn** *(string) --*The ARN of the device definition version for
        this group.
        - **FunctionDefinitionVersionArn** *(string) --*The ARN of the function definition version
        for this group.
        - **LoggerDefinitionVersionArn** *(string) --*The ARN of the logger definition version for
        this group.
        - **ResourceDefinitionVersionArn** *(string) --*The ARN of the resource definition version
        for this group.
        - **SubscriptionDefinitionVersionArn** *(string) --*The ARN of the subscription definition
        version for this group.
    """


_ClientGetLoggerDefinitionResponseTypeDef = TypedDict(
    "_ClientGetLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetLoggerDefinitionResponseTypeDef(_ClientGetLoggerDefinitionResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef = TypedDict(
    "_ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef",
    {
        "Component": Literal["GreengrassSystem", "Lambda"],
        "Id": str,
        "Level": Literal["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
        "Space": int,
        "Type": Literal["FileSystem", "AWSCloudWatch"],
    },
    total=False,
)


class ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef(
    _ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef
):
    """
    - *(dict) --*Information about a logger

      - **Component** *(string) --*The component that will be subject to logging.
      - **Id** *(string) --*A descriptive or arbitrary ID for the logger. This value must be unique
      within the logger definition version. Max length is 128 characters with pattern
      ''[a-zA-Z0-9:_-]+''.
      - **Level** *(string) --*The level of the logs.
      - **Space** *(integer) --*The amount of file space, in KB, to use if the local file system is
      used for logging purposes.
      - **Type** *(string) --*The type of log output which will be used.
    """


_ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef",
    {"Loggers": List[ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef]},
    total=False,
)


class ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef
):
    """
    - **Definition** *(dict) --*Information about the logger definition version.

      - **Loggers** *(list) --*A list of loggers.

        - *(dict) --*Information about a logger

          - **Component** *(string) --*The component that will be subject to logging.
          - **Id** *(string) --*A descriptive or arbitrary ID for the logger. This value must be
          unique within the logger definition version. Max length is 128 characters with pattern
          ''[a-zA-Z0-9:_-]+''.
          - **Level** *(string) --*The level of the logs.
          - **Space** *(integer) --*The amount of file space, in KB, to use if the local file system
          is used for logging purposes.
          - **Type** *(string) --*The type of log output which will be used.
    """


_ClientGetLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)


class ClientGetLoggerDefinitionVersionResponseTypeDef(
    _ClientGetLoggerDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*success

      - **Arn** *(string) --*The ARN of the logger definition version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      logger definition version was created.
      - **Definition** *(dict) --*Information about the logger definition version.

        - **Loggers** *(list) --*A list of loggers.

          - *(dict) --*Information about a logger

            - **Component** *(string) --*The component that will be subject to logging.
            - **Id** *(string) --*A descriptive or arbitrary ID for the logger. This value must be
            unique within the logger definition version. Max length is 128 characters with pattern
            ''[a-zA-Z0-9:_-]+''.
            - **Level** *(string) --*The level of the logs.
            - **Space** *(integer) --*The amount of file space, in KB, to use if the local file
            system is used for logging purposes.
            - **Type** *(string) --*The type of log output which will be used.
    """


_ClientGetResourceDefinitionResponseTypeDef = TypedDict(
    "_ClientGetResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetResourceDefinitionResponseTypeDef(_ClientGetResourceDefinitionResponseTypeDef):
    """
    - *(dict) --*success

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef
):
    """
    - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

      - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
      specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
      Lambda process will have the file access permissions of the added Linux group.
      - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be added to
      the Lambda process. This field is optional.
    """


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef
):
    """
    - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device resource.

      - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

        - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
        specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
        Lambda process will have the file access permissions of the added Linux group.
        - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be added
        to the Lambda process. This field is optional.
    """


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef
):
    pass


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef
):
    pass


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef
):
    pass


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef,
        "S3Uri": str,
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef
):
    pass


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef
):
    pass


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef,
        "SageMakerJobArn": str,
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef
):
    pass


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    {"ARN": str, "AdditionalStagingLabelsToDownload": List[str]},
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef
):
    pass


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef,
        "LocalVolumeResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef,
        "S3MachineLearningModelResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef,
        "SageMakerMachineLearningModelResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef,
        "SecretsManagerSecretResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef,
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef
):
    """
    - **ResourceDataContainer** *(dict) --*A container of data for all resource types.

      - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device resource.

        - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

          - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
          specified Linux OS group owner of the resource to the Lambda process privileges. Thus the
          Lambda process will have the file access permissions of the added Linux group.
          - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be
          added to the Lambda process. This field is optional.
    """


_ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef,
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef
):
    """
    - *(dict) --*Information about a resource.

      - **Id** *(string) --*The resource ID, used to refer to a resource in the Lambda function
      configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This must be
      unique within a Greengrass group.
      - **Name** *(string) --*The descriptive resource name, which is displayed on the AWS IoT
      Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This must be
      unique within a Greengrass group.
      - **ResourceDataContainer** *(dict) --*A container of data for all resource types.

        - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device resource.

          - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

            - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds the
            specified Linux OS group owner of the resource to the Lambda process privileges. Thus
            the Lambda process will have the file access permissions of the added Linux group.
            - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will be
            added to the Lambda process. This field is optional.
    """


_ClientGetResourceDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseDefinitionTypeDef",
    {"Resources": List[ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef]},
    total=False,
)


class ClientGetResourceDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetResourceDefinitionVersionResponseDefinitionTypeDef
):
    """
    - **Definition** *(dict) --*Information about the definition.

      - **Resources** *(list) --*A list of resources.

        - *(dict) --*Information about a resource.

          - **Id** *(string) --*The resource ID, used to refer to a resource in the Lambda function
          configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This must be
          unique within a Greengrass group.
          - **Name** *(string) --*The descriptive resource name, which is displayed on the AWS IoT
          Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This must
          be unique within a Greengrass group.
          - **ResourceDataContainer** *(dict) --*A container of data for all resource types.

            - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device
            resource.

              - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

                - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically adds
                the specified Linux OS group owner of the resource to the Lambda process privileges.
                Thus the Lambda process will have the file access permissions of the added Linux
                group.
                - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will
                be added to the Lambda process. This field is optional.
    """


_ClientGetResourceDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetResourceDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)


class ClientGetResourceDefinitionVersionResponseTypeDef(
    _ClientGetResourceDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*success

      - **Arn** *(string) --*Arn of the resource definition version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      resource definition version was created.
      - **Definition** *(dict) --*Information about the definition.

        - **Resources** *(list) --*A list of resources.

          - *(dict) --*Information about a resource.

            - **Id** *(string) --*The resource ID, used to refer to a resource in the Lambda
            function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''.
            This must be unique within a Greengrass group.
            - **Name** *(string) --*The descriptive resource name, which is displayed on the AWS IoT
            Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This
            must be unique within a Greengrass group.
            - **ResourceDataContainer** *(dict) --*A container of data for all resource types.

              - **LocalDeviceResourceData** *(dict) --*Attributes that define the local device
              resource.

                - **GroupOwnerSetting** *(dict) --*Group/owner related settings for local resources.

                  - **AutoAddGroupOwner** *(boolean) --*If true, AWS IoT Greengrass automatically
                  adds the specified Linux OS group owner of the resource to the Lambda process
                  privileges. Thus the Lambda process will have the file access permissions of the
                  added Linux group.
                  - **GroupOwner** *(string) --*The name of the Linux OS group whose privileges will
                  be added to the Lambda process. This field is optional.
    """


_ClientGetServiceRoleForAccountResponseTypeDef = TypedDict(
    "_ClientGetServiceRoleForAccountResponseTypeDef",
    {"AssociatedAt": str, "RoleArn": str},
    total=False,
)


class ClientGetServiceRoleForAccountResponseTypeDef(_ClientGetServiceRoleForAccountResponseTypeDef):
    """
    - *(dict) --*success

      - **AssociatedAt** *(string) --*The time when the service role was associated with the
      account.
      - **RoleArn** *(string) --*The ARN of the role which is associated with the account.
    """


_ClientGetSubscriptionDefinitionResponseTypeDef = TypedDict(
    "_ClientGetSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientGetSubscriptionDefinitionResponseTypeDef(
    _ClientGetSubscriptionDefinitionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef = TypedDict(
    "_ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
    total=False,
)


class ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef(
    _ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef
):
    """
    - *(dict) --*Information about a subscription.

      - **Id** *(string) --*A descriptive or arbitrary ID for the subscription. This value must be
      unique within the subscription definition version. Max length is 128 characters with pattern
      ''[a-zA-Z0-9:_-]+''.
      - **Source** *(string) --*The source of the subscription. Can be a thing ARN, a Lambda
      function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
      'GGShadowService'.
      - **Subject** *(string) --*The MQTT topic used to route the message.
      - **Target** *(string) --*Where the message is sent to. Can be a thing ARN, a Lambda function
      ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or 'GGShadowService'.
    """


_ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "_ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef",
    {
        "Subscriptions": List[
            ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef
        ]
    },
    total=False,
)


class ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef(
    _ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef
):
    """
    - **Definition** *(dict) --*Information about the subscription definition version.

      - **Subscriptions** *(list) --*A list of subscriptions.

        - *(dict) --*Information about a subscription.

          - **Id** *(string) --*A descriptive or arbitrary ID for the subscription. This value must
          be unique within the subscription definition version. Max length is 128 characters with
          pattern ''[a-zA-Z0-9:_-]+''.
          - **Source** *(string) --*The source of the subscription. Can be a thing ARN, a Lambda
          function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
          'GGShadowService'.
          - **Subject** *(string) --*The MQTT topic used to route the message.
          - **Target** *(string) --*Where the message is sent to. Can be a thing ARN, a Lambda
          function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
          'GGShadowService'.
    """


_ClientGetSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "_ClientGetSubscriptionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)


class ClientGetSubscriptionDefinitionVersionResponseTypeDef(
    _ClientGetSubscriptionDefinitionVersionResponseTypeDef
):
    """
    - *(dict) --*

      - **Arn** *(string) --*The ARN of the subscription definition version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      subscription definition version was created.
      - **Definition** *(dict) --*Information about the subscription definition version.

        - **Subscriptions** *(list) --*A list of subscriptions.

          - *(dict) --*Information about a subscription.

            - **Id** *(string) --*A descriptive or arbitrary ID for the subscription. This value
            must be unique within the subscription definition version. Max length is 128 characters
            with pattern ''[a-zA-Z0-9:_-]+''.
            - **Source** *(string) --*The source of the subscription. Can be a thing ARN, a Lambda
            function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
            'GGShadowService'.
            - **Subject** *(string) --*The MQTT topic used to route the message.
            - **Target** *(string) --*Where the message is sent to. Can be a thing ARN, a Lambda
            function ARN, a connector ARN, 'cloud' (which represents the AWS IoT cloud), or
            'GGShadowService'.
    """


_ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef = TypedDict(
    "_ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)


class ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef(
    _ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef
):
    """
    - *(dict) --*Details about the error.

      - **DetailedErrorCode** *(string) --*A detailed error code.
      - **DetailedErrorMessage** *(string) --*A detailed error message.
    """


_ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef = TypedDict(
    "_ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "ErrorDetails": List[
            ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef
        ],
        "ErrorMessage": str,
        "GroupArn": str,
    },
    total=False,
)


class ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef(
    _ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef
):
    """
    - *(dict) --*Information about an individual group deployment in a bulk deployment operation.

      - **CreatedAt** *(string) --*The time, in ISO format, when the deployment was created.
      - **DeploymentArn** *(string) --*The ARN of the group deployment.
      - **DeploymentId** *(string) --*The ID of the group deployment.
      - **DeploymentStatus** *(string) --*The current status of the group deployment:
      ''InProgress'', ''Building'', ''Success'', or ''Failure''.
      - **DeploymentType** *(string) --*The type of the deployment.
      - **ErrorDetails** *(list) --*Details about the error.

        - *(dict) --*Details about the error.

          - **DetailedErrorCode** *(string) --*A detailed error code.
          - **DetailedErrorMessage** *(string) --*A detailed error message.
    """


_ClientListBulkDeploymentDetailedReportsResponseTypeDef = TypedDict(
    "_ClientListBulkDeploymentDetailedReportsResponseTypeDef",
    {
        "Deployments": List[ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListBulkDeploymentDetailedReportsResponseTypeDef(
    _ClientListBulkDeploymentDetailedReportsResponseTypeDef
):
    """
    - *(dict) --*Success. The response body contains the list of deployments for the given group.

      - **Deployments** *(list) --*A list of the individual group deployments in the bulk deployment
      operation.

        - *(dict) --*Information about an individual group deployment in a bulk deployment
        operation.

          - **CreatedAt** *(string) --*The time, in ISO format, when the deployment was created.
          - **DeploymentArn** *(string) --*The ARN of the group deployment.
          - **DeploymentId** *(string) --*The ID of the group deployment.
          - **DeploymentStatus** *(string) --*The current status of the group deployment:
          ''InProgress'', ''Building'', ''Success'', or ''Failure''.
          - **DeploymentType** *(string) --*The type of the deployment.
          - **ErrorDetails** *(list) --*Details about the error.

            - *(dict) --*Details about the error.

              - **DetailedErrorCode** *(string) --*A detailed error code.
              - **DetailedErrorMessage** *(string) --*A detailed error message.
    """


_ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef = TypedDict(
    "_ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str, "CreatedAt": str},
    total=False,
)


class ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef(
    _ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef
):
    """
    - *(dict) --*Information about a bulk deployment. You cannot start a new bulk deployment while
    another one is still running or in a non-terminal state.

      - **BulkDeploymentArn** *(string) --*The ARN of the bulk deployment.
      - **BulkDeploymentId** *(string) --*The ID of the bulk deployment.
      - **CreatedAt** *(string) --*The time, in ISO format, when the deployment was created.
    """


_ClientListBulkDeploymentsResponseTypeDef = TypedDict(
    "_ClientListBulkDeploymentsResponseTypeDef",
    {
        "BulkDeployments": List[ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListBulkDeploymentsResponseTypeDef(_ClientListBulkDeploymentsResponseTypeDef):
    """
    - *(dict) --*Success. The response body contains the list of bulk deployments.

      - **BulkDeployments** *(list) --*A list of bulk deployments.

        - *(dict) --*Information about a bulk deployment. You cannot start a new bulk deployment
        while another one is still running or in a non-terminal state.

          - **BulkDeploymentArn** *(string) --*The ARN of the bulk deployment.
          - **BulkDeploymentId** *(string) --*The ID of the bulk deployment.
          - **CreatedAt** *(string) --*The time, in ISO format, when the deployment was created.
    """


_ClientListConnectorDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListConnectorDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListConnectorDefinitionVersionsResponseVersionsTypeDef(
    _ClientListConnectorDefinitionVersionsResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientListConnectorDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListConnectorDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListConnectorDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListConnectorDefinitionVersionsResponseTypeDef(
    _ClientListConnectorDefinitionVersionsResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*The token for the next set of results, or ''null'' if there are
      no additional results.
      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ClientListConnectorDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListConnectorDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListConnectorDefinitionsResponseDefinitionsTypeDef(
    _ClientListConnectorDefinitionsResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientListConnectorDefinitionsResponseTypeDef = TypedDict(
    "_ClientListConnectorDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListConnectorDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListConnectorDefinitionsResponseTypeDef(_ClientListConnectorDefinitionsResponseTypeDef):
    """
    - *(dict) --*

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ClientListCoreDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListCoreDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListCoreDefinitionVersionsResponseVersionsTypeDef(
    _ClientListCoreDefinitionVersionsResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientListCoreDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListCoreDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListCoreDefinitionVersionsResponseVersionsTypeDef]},
    total=False,
)


class ClientListCoreDefinitionVersionsResponseTypeDef(
    _ClientListCoreDefinitionVersionsResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*The token for the next set of results, or ''null'' if there are
      no additional results.
      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ClientListCoreDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListCoreDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListCoreDefinitionsResponseDefinitionsTypeDef(
    _ClientListCoreDefinitionsResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientListCoreDefinitionsResponseTypeDef = TypedDict(
    "_ClientListCoreDefinitionsResponseTypeDef",
    {"Definitions": List[ClientListCoreDefinitionsResponseDefinitionsTypeDef], "NextToken": str},
    total=False,
)


class ClientListCoreDefinitionsResponseTypeDef(_ClientListCoreDefinitionsResponseTypeDef):
    """
    - *(dict) --*

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ClientListDeploymentsResponseDeploymentsTypeDef = TypedDict(
    "_ClientListDeploymentsResponseDeploymentsTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "GroupArn": str,
    },
    total=False,
)


class ClientListDeploymentsResponseDeploymentsTypeDef(
    _ClientListDeploymentsResponseDeploymentsTypeDef
):
    """
    - *(dict) --*Information about a deployment.

      - **CreatedAt** *(string) --*The time, in milliseconds since the epoch, when the deployment
      was created.
      - **DeploymentArn** *(string) --*The ARN of the deployment.
      - **DeploymentId** *(string) --*The ID of the deployment.
      - **DeploymentType** *(string) --*The type of the deployment.
      - **GroupArn** *(string) --*The ARN of the group for this deployment.
    """


_ClientListDeploymentsResponseTypeDef = TypedDict(
    "_ClientListDeploymentsResponseTypeDef",
    {"Deployments": List[ClientListDeploymentsResponseDeploymentsTypeDef], "NextToken": str},
    total=False,
)


class ClientListDeploymentsResponseTypeDef(_ClientListDeploymentsResponseTypeDef):
    """
    - *(dict) --*Success. The response body contains the list of deployments for the given group.

      - **Deployments** *(list) --*A list of deployments for the requested groups.

        - *(dict) --*Information about a deployment.

          - **CreatedAt** *(string) --*The time, in milliseconds since the epoch, when the
          deployment was created.
          - **DeploymentArn** *(string) --*The ARN of the deployment.
          - **DeploymentId** *(string) --*The ID of the deployment.
          - **DeploymentType** *(string) --*The type of the deployment.
          - **GroupArn** *(string) --*The ARN of the group for this deployment.
    """


_ClientListDeviceDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListDeviceDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListDeviceDefinitionVersionsResponseVersionsTypeDef(
    _ClientListDeviceDefinitionVersionsResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientListDeviceDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListDeviceDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListDeviceDefinitionVersionsResponseVersionsTypeDef]},
    total=False,
)


class ClientListDeviceDefinitionVersionsResponseTypeDef(
    _ClientListDeviceDefinitionVersionsResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*The token for the next set of results, or ''null'' if there are
      no additional results.
      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ClientListDeviceDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListDeviceDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListDeviceDefinitionsResponseDefinitionsTypeDef(
    _ClientListDeviceDefinitionsResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientListDeviceDefinitionsResponseTypeDef = TypedDict(
    "_ClientListDeviceDefinitionsResponseTypeDef",
    {"Definitions": List[ClientListDeviceDefinitionsResponseDefinitionsTypeDef], "NextToken": str},
    total=False,
)


class ClientListDeviceDefinitionsResponseTypeDef(_ClientListDeviceDefinitionsResponseTypeDef):
    """
    - *(dict) --*

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ClientListFunctionDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListFunctionDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListFunctionDefinitionVersionsResponseVersionsTypeDef(
    _ClientListFunctionDefinitionVersionsResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientListFunctionDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListFunctionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListFunctionDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListFunctionDefinitionVersionsResponseTypeDef(
    _ClientListFunctionDefinitionVersionsResponseTypeDef
):
    """
    - *(dict) --*success

      - **NextToken** *(string) --*The token for the next set of results, or ''null'' if there are
      no additional results.
      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ClientListFunctionDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListFunctionDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListFunctionDefinitionsResponseDefinitionsTypeDef(
    _ClientListFunctionDefinitionsResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientListFunctionDefinitionsResponseTypeDef = TypedDict(
    "_ClientListFunctionDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListFunctionDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListFunctionDefinitionsResponseTypeDef(_ClientListFunctionDefinitionsResponseTypeDef):
    """
    - *(dict) --*Success. The response contains the IDs of all the Greengrass Lambda function
    definitions in this account.

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef = TypedDict(
    "_ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef",
    {"GroupCertificateAuthorityArn": str, "GroupCertificateAuthorityId": str},
    total=False,
)


class ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef(
    _ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef
):
    """
    - *(dict) --*Information about a certificate authority for a group.

      - **GroupCertificateAuthorityArn** *(string) --*The ARN of the certificate authority for the
      group.
      - **GroupCertificateAuthorityId** *(string) --*The ID of the certificate authority for the
      group.
    """


_ClientListGroupCertificateAuthoritiesResponseTypeDef = TypedDict(
    "_ClientListGroupCertificateAuthoritiesResponseTypeDef",
    {
        "GroupCertificateAuthorities": List[
            ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef
        ]
    },
    total=False,
)


class ClientListGroupCertificateAuthoritiesResponseTypeDef(
    _ClientListGroupCertificateAuthoritiesResponseTypeDef
):
    """
    - *(dict) --*Success. The response body contains the PKI Configuration.

      - **GroupCertificateAuthorities** *(list) --*A list of certificate authorities associated with
      the group.

        - *(dict) --*Information about a certificate authority for a group.

          - **GroupCertificateAuthorityArn** *(string) --*The ARN of the certificate authority for
          the group.
          - **GroupCertificateAuthorityId** *(string) --*The ID of the certificate authority for the
          group.
    """


_ClientListGroupVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListGroupVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListGroupVersionsResponseVersionsTypeDef(
    _ClientListGroupVersionsResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientListGroupVersionsResponseTypeDef = TypedDict(
    "_ClientListGroupVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListGroupVersionsResponseVersionsTypeDef]},
    total=False,
)


class ClientListGroupVersionsResponseTypeDef(_ClientListGroupVersionsResponseTypeDef):
    """
    - *(dict) --*Success. The response contains the list of versions and metadata for the given
    group.

      - **NextToken** *(string) --*The token for the next set of results, or ''null'' if there are
      no additional results.
      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ClientListGroupsResponseGroupsTypeDef(_ClientListGroupsResponseGroupsTypeDef):
    """
    - *(dict) --*Information about a group.

      - **Arn** *(string) --*The ARN of the group.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the group
      was created.
      - **Id** *(string) --*The ID of the group.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      group was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the group.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the group.
      - **Name** *(string) --*The name of the group.
    """


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*Information about a group.

        - *(dict) --*Information about a group.

          - **Arn** *(string) --*The ARN of the group.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          group was created.
          - **Id** *(string) --*The ID of the group.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the group was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the group.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          group.
          - **Name** *(string) --*The name of the group.
    """


_ClientListLoggerDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListLoggerDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListLoggerDefinitionVersionsResponseVersionsTypeDef(
    _ClientListLoggerDefinitionVersionsResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientListLoggerDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListLoggerDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListLoggerDefinitionVersionsResponseVersionsTypeDef]},
    total=False,
)


class ClientListLoggerDefinitionVersionsResponseTypeDef(
    _ClientListLoggerDefinitionVersionsResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*The token for the next set of results, or ''null'' if there are
      no additional results.
      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ClientListLoggerDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListLoggerDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListLoggerDefinitionsResponseDefinitionsTypeDef(
    _ClientListLoggerDefinitionsResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientListLoggerDefinitionsResponseTypeDef = TypedDict(
    "_ClientListLoggerDefinitionsResponseTypeDef",
    {"Definitions": List[ClientListLoggerDefinitionsResponseDefinitionsTypeDef], "NextToken": str},
    total=False,
)


class ClientListLoggerDefinitionsResponseTypeDef(_ClientListLoggerDefinitionsResponseTypeDef):
    """
    - *(dict) --*

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ClientListResourceDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListResourceDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListResourceDefinitionVersionsResponseVersionsTypeDef(
    _ClientListResourceDefinitionVersionsResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientListResourceDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListResourceDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListResourceDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListResourceDefinitionVersionsResponseTypeDef(
    _ClientListResourceDefinitionVersionsResponseTypeDef
):
    """
    - *(dict) --*success

      - **NextToken** *(string) --*The token for the next set of results, or ''null'' if there are
      no additional results.
      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ClientListResourceDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListResourceDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListResourceDefinitionsResponseDefinitionsTypeDef(
    _ClientListResourceDefinitionsResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientListResourceDefinitionsResponseTypeDef = TypedDict(
    "_ClientListResourceDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListResourceDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourceDefinitionsResponseTypeDef(_ClientListResourceDefinitionsResponseTypeDef):
    """
    - *(dict) --*The IDs of all the Greengrass resource definitions in this account.

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "_ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef(
    _ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ClientListSubscriptionDefinitionVersionsResponseTypeDef = TypedDict(
    "_ClientListSubscriptionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)


class ClientListSubscriptionDefinitionVersionsResponseTypeDef(
    _ClientListSubscriptionDefinitionVersionsResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*The token for the next set of results, or ''null'' if there are
      no additional results.
      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "_ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef(
    _ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ClientListSubscriptionDefinitionsResponseTypeDef = TypedDict(
    "_ClientListSubscriptionDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListSubscriptionDefinitionsResponseTypeDef(
    _ClientListSubscriptionDefinitionsResponseTypeDef
):
    """
    - *(dict) --*

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*HTTP Status Code 200: OK.

      - **tags** *(dict) --*The key-value pair for the resource tag.

        - *(string) --*

          - *(string) --*
    """


_ClientResetDeploymentsResponseTypeDef = TypedDict(
    "_ClientResetDeploymentsResponseTypeDef",
    {"DeploymentArn": str, "DeploymentId": str},
    total=False,
)


class ClientResetDeploymentsResponseTypeDef(_ClientResetDeploymentsResponseTypeDef):
    """
    - *(dict) --*Success. The group's deployments were reset.

      - **DeploymentArn** *(string) --*The ARN of the deployment.
      - **DeploymentId** *(string) --*The ID of the deployment.
    """


_ClientStartBulkDeploymentResponseTypeDef = TypedDict(
    "_ClientStartBulkDeploymentResponseTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str},
    total=False,
)


class ClientStartBulkDeploymentResponseTypeDef(_ClientStartBulkDeploymentResponseTypeDef):
    """
    - *(dict) --*success

      - **BulkDeploymentArn** *(string) --*The ARN of the bulk deployment.
      - **BulkDeploymentId** *(string) --*The ID of the bulk deployment.
    """


_ClientUpdateConnectivityInfoConnectivityInfoTypeDef = TypedDict(
    "_ClientUpdateConnectivityInfoConnectivityInfoTypeDef",
    {"HostAddress": str, "Id": str, "Metadata": str, "PortNumber": int},
    total=False,
)


class ClientUpdateConnectivityInfoConnectivityInfoTypeDef(
    _ClientUpdateConnectivityInfoConnectivityInfoTypeDef
):
    """
    - *(dict) --*Information about a Greengrass core's connectivity.

      - **HostAddress** *(string) --*The endpoint for the Greengrass core. Can be an IP address or
      DNS.
      - **Id** *(string) --*The ID of the connectivity information.
      - **Metadata** *(string) --*Metadata for this endpoint.
      - **PortNumber** *(integer) --*The port of the Greengrass core. Usually 8883.
    """


_ClientUpdateConnectivityInfoResponseTypeDef = TypedDict(
    "_ClientUpdateConnectivityInfoResponseTypeDef", {"Message": str, "Version": str}, total=False
)


class ClientUpdateConnectivityInfoResponseTypeDef(_ClientUpdateConnectivityInfoResponseTypeDef):
    """
    - *(dict) --*success

      - **Message** *(string) --*A message about the connectivity info update request.
      - **Version** *(string) --*The new version of the connectivity info.
    """


_ClientUpdateGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
    },
    total=False,
)


class ClientUpdateGroupCertificateConfigurationResponseTypeDef(
    _ClientUpdateGroupCertificateConfigurationResponseTypeDef
):
    """
    - *(dict) --*Success. The response body contains the PKI Configuration.

      - **CertificateAuthorityExpiryInMilliseconds** *(string) --*The amount of time remaining
      before the certificate authority expires, in milliseconds.
      - **CertificateExpiryInMilliseconds** *(string) --*The amount of time remaining before the
      certificate expires, in milliseconds.
      - **GroupId** *(string) --*The ID of the group certificate configuration.
    """


_ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef(
    _ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsErrorDetailsTypeDef = TypedDict(
    "_ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)


class ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsErrorDetailsTypeDef(
    _ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsErrorDetailsTypeDef
):
    """
    - *(dict) --*Details about the error.

      - **DetailedErrorCode** *(string) --*A detailed error code.
      - **DetailedErrorMessage** *(string) --*A detailed error message.
    """


_ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsTypeDef = TypedDict(
    "_ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "ErrorDetails": List[
            ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsErrorDetailsTypeDef
        ],
        "ErrorMessage": str,
        "GroupArn": str,
    },
    total=False,
)


class ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsTypeDef(
    _ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsTypeDef
):
    """
    - *(dict) --*Information about an individual group deployment in a bulk deployment operation.

      - **CreatedAt** *(string) --*The time, in ISO format, when the deployment was created.
      - **DeploymentArn** *(string) --*The ARN of the group deployment.
      - **DeploymentId** *(string) --*The ID of the group deployment.
      - **DeploymentStatus** *(string) --*The current status of the group deployment:
      ''InProgress'', ''Building'', ''Success'', or ''Failure''.
      - **DeploymentType** *(string) --*The type of the deployment.
      - **ErrorDetails** *(list) --*Details about the error.

        - *(dict) --*Details about the error.

          - **DetailedErrorCode** *(string) --*A detailed error code.
          - **DetailedErrorMessage** *(string) --*A detailed error message.
    """


_ListBulkDeploymentDetailedReportsPaginateResponseTypeDef = TypedDict(
    "_ListBulkDeploymentDetailedReportsPaginateResponseTypeDef",
    {"Deployments": List[ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsTypeDef]},
    total=False,
)


class ListBulkDeploymentDetailedReportsPaginateResponseTypeDef(
    _ListBulkDeploymentDetailedReportsPaginateResponseTypeDef
):
    """
    - *(dict) --*Success. The response body contains the list of deployments for the given group.

      - **Deployments** *(list) --*A list of the individual group deployments in the bulk deployment
      operation.

        - *(dict) --*Information about an individual group deployment in a bulk deployment
        operation.

          - **CreatedAt** *(string) --*The time, in ISO format, when the deployment was created.
          - **DeploymentArn** *(string) --*The ARN of the group deployment.
          - **DeploymentId** *(string) --*The ID of the group deployment.
          - **DeploymentStatus** *(string) --*The current status of the group deployment:
          ''InProgress'', ''Building'', ''Success'', or ''Failure''.
          - **DeploymentType** *(string) --*The type of the deployment.
          - **ErrorDetails** *(list) --*Details about the error.

            - *(dict) --*Details about the error.

              - **DetailedErrorCode** *(string) --*A detailed error code.
              - **DetailedErrorMessage** *(string) --*A detailed error message.
    """


_ListBulkDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBulkDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBulkDeploymentsPaginatePaginationConfigTypeDef(
    _ListBulkDeploymentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBulkDeploymentsPaginateResponseBulkDeploymentsTypeDef = TypedDict(
    "_ListBulkDeploymentsPaginateResponseBulkDeploymentsTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str, "CreatedAt": str},
    total=False,
)


class ListBulkDeploymentsPaginateResponseBulkDeploymentsTypeDef(
    _ListBulkDeploymentsPaginateResponseBulkDeploymentsTypeDef
):
    """
    - *(dict) --*Information about a bulk deployment. You cannot start a new bulk deployment while
    another one is still running or in a non-terminal state.

      - **BulkDeploymentArn** *(string) --*The ARN of the bulk deployment.
      - **BulkDeploymentId** *(string) --*The ID of the bulk deployment.
      - **CreatedAt** *(string) --*The time, in ISO format, when the deployment was created.
    """


_ListBulkDeploymentsPaginateResponseTypeDef = TypedDict(
    "_ListBulkDeploymentsPaginateResponseTypeDef",
    {"BulkDeployments": List[ListBulkDeploymentsPaginateResponseBulkDeploymentsTypeDef]},
    total=False,
)


class ListBulkDeploymentsPaginateResponseTypeDef(_ListBulkDeploymentsPaginateResponseTypeDef):
    """
    - *(dict) --*Success. The response body contains the list of bulk deployments.

      - **BulkDeployments** *(list) --*A list of bulk deployments.

        - *(dict) --*Information about a bulk deployment. You cannot start a new bulk deployment
        while another one is still running or in a non-terminal state.

          - **BulkDeploymentArn** *(string) --*The ARN of the bulk deployment.
          - **BulkDeploymentId** *(string) --*The ID of the bulk deployment.
          - **CreatedAt** *(string) --*The time, in ISO format, when the deployment was created.
    """


_ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ListConnectorDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListConnectorDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListConnectorDefinitionVersionsPaginateResponseTypeDef(
    _ListConnectorDefinitionVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ListConnectorDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConnectorDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConnectorDefinitionsPaginatePaginationConfigTypeDef(
    _ListConnectorDefinitionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ListConnectorDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListConnectorDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListConnectorDefinitionsPaginateResponseTypeDef(
    _ListConnectorDefinitionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ListCoreDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListCoreDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListCoreDefinitionVersionsPaginateResponseTypeDef(
    _ListCoreDefinitionVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ListCoreDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCoreDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCoreDefinitionsPaginatePaginationConfigTypeDef(
    _ListCoreDefinitionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCoreDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListCoreDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListCoreDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListCoreDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ListCoreDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListCoreDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListCoreDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListCoreDefinitionsPaginateResponseTypeDef(_ListCoreDefinitionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ListDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeploymentsPaginatePaginationConfigTypeDef(
    _ListDeploymentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeploymentsPaginateResponseDeploymentsTypeDef = TypedDict(
    "_ListDeploymentsPaginateResponseDeploymentsTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "GroupArn": str,
    },
    total=False,
)


class ListDeploymentsPaginateResponseDeploymentsTypeDef(
    _ListDeploymentsPaginateResponseDeploymentsTypeDef
):
    """
    - *(dict) --*Information about a deployment.

      - **CreatedAt** *(string) --*The time, in milliseconds since the epoch, when the deployment
      was created.
      - **DeploymentArn** *(string) --*The ARN of the deployment.
      - **DeploymentId** *(string) --*The ID of the deployment.
      - **DeploymentType** *(string) --*The type of the deployment.
      - **GroupArn** *(string) --*The ARN of the group for this deployment.
    """


_ListDeploymentsPaginateResponseTypeDef = TypedDict(
    "_ListDeploymentsPaginateResponseTypeDef",
    {"Deployments": List[ListDeploymentsPaginateResponseDeploymentsTypeDef]},
    total=False,
)


class ListDeploymentsPaginateResponseTypeDef(_ListDeploymentsPaginateResponseTypeDef):
    """
    - *(dict) --*Success. The response body contains the list of deployments for the given group.

      - **Deployments** *(list) --*A list of deployments for the requested groups.

        - *(dict) --*Information about a deployment.

          - **CreatedAt** *(string) --*The time, in milliseconds since the epoch, when the
          deployment was created.
          - **DeploymentArn** *(string) --*The ARN of the deployment.
          - **DeploymentId** *(string) --*The ID of the deployment.
          - **DeploymentType** *(string) --*The type of the deployment.
          - **GroupArn** *(string) --*The ARN of the group for this deployment.
    """


_ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ListDeviceDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListDeviceDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListDeviceDefinitionVersionsPaginateResponseTypeDef(
    _ListDeviceDefinitionVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ListDeviceDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeviceDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeviceDefinitionsPaginatePaginationConfigTypeDef(
    _ListDeviceDefinitionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ListDeviceDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListDeviceDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListDeviceDefinitionsPaginateResponseTypeDef(_ListDeviceDefinitionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ListFunctionDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListFunctionDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListFunctionDefinitionVersionsPaginateResponseTypeDef(
    _ListFunctionDefinitionVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*success

      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ListFunctionDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFunctionDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFunctionDefinitionsPaginatePaginationConfigTypeDef(
    _ListFunctionDefinitionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFunctionDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListFunctionDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListFunctionDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListFunctionDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ListFunctionDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListFunctionDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListFunctionDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListFunctionDefinitionsPaginateResponseTypeDef(
    _ListFunctionDefinitionsPaginateResponseTypeDef
):
    """
    - *(dict) --*Success. The response contains the IDs of all the Greengrass Lambda function
    definitions in this account.

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ListGroupVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupVersionsPaginatePaginationConfigTypeDef(
    _ListGroupVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroupVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListGroupVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListGroupVersionsPaginateResponseVersionsTypeDef(
    _ListGroupVersionsPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ListGroupVersionsPaginateResponseTypeDef = TypedDict(
    "_ListGroupVersionsPaginateResponseTypeDef",
    {"Versions": List[ListGroupVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListGroupVersionsPaginateResponseTypeDef(_ListGroupVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*Success. The response contains the list of versions and metadata for the given
    group.

      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsPaginatePaginationConfigTypeDef(_ListGroupsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)


class ListGroupsPaginateResponseGroupsTypeDef(_ListGroupsPaginateResponseGroupsTypeDef):
    """
    - *(dict) --*Information about a group.

      - **Arn** *(string) --*The ARN of the group.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the group
      was created.
      - **Id** *(string) --*The ID of the group.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      group was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the group.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the group.
      - **Name** *(string) --*The name of the group.
    """


_ListGroupsPaginateResponseTypeDef = TypedDict(
    "_ListGroupsPaginateResponseTypeDef",
    {"Groups": List[ListGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)


class ListGroupsPaginateResponseTypeDef(_ListGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*Information about a group.

        - *(dict) --*Information about a group.

          - **Arn** *(string) --*The ARN of the group.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          group was created.
          - **Id** *(string) --*The ID of the group.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the group was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the group.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          group.
          - **Name** *(string) --*The name of the group.
    """


_ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ListLoggerDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListLoggerDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListLoggerDefinitionVersionsPaginateResponseTypeDef(
    _ListLoggerDefinitionVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ListLoggerDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLoggerDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLoggerDefinitionsPaginatePaginationConfigTypeDef(
    _ListLoggerDefinitionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ListLoggerDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListLoggerDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListLoggerDefinitionsPaginateResponseTypeDef(_ListLoggerDefinitionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ListResourceDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListResourceDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListResourceDefinitionVersionsPaginateResponseTypeDef(
    _ListResourceDefinitionVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*success

      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ListResourceDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourceDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourceDefinitionsPaginatePaginationConfigTypeDef(
    _ListResourceDefinitionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourceDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListResourceDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListResourceDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListResourceDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ListResourceDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListResourceDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListResourceDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListResourceDefinitionsPaginateResponseTypeDef(
    _ListResourceDefinitionsPaginateResponseTypeDef
):
    """
    - *(dict) --*The IDs of all the Greengrass resource definitions in this account.

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """


_ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef(
    _ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "_ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)


class ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef(
    _ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*Information about a version.

      - **Arn** *(string) --*The ARN of the version.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      version was created.
      - **Id** *(string) --*The ID of the parent definition that the version is associated with.
      - **Version** *(string) --*The ID of the version.
    """


_ListSubscriptionDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "_ListSubscriptionDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)


class ListSubscriptionDefinitionVersionsPaginateResponseTypeDef(
    _ListSubscriptionDefinitionVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Versions** *(list) --*Information about a version.

        - *(dict) --*Information about a version.

          - **Arn** *(string) --*The ARN of the version.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          version was created.
          - **Id** *(string) --*The ID of the parent definition that the version is associated with.
          - **Version** *(string) --*The ID of the version.
    """


_ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef(
    _ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "_ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef(
    _ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef
):
    """
    - *(dict) --*Information about a definition.

      - **Arn** *(string) --*The ARN of the definition.
      - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was created.
      - **Id** *(string) --*The ID of the definition.
      - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
      definition was last updated.
      - **LatestVersion** *(string) --*The ID of the latest version associated with the definition.
      - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
      definition.
      - **Name** *(string) --*The name of the definition.
      - **Tags** *(dict) --*Tag(s) attached to the resource arn.

        - *(string) --*

          - *(string) --*
    """


_ListSubscriptionDefinitionsPaginateResponseTypeDef = TypedDict(
    "_ListSubscriptionDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)


class ListSubscriptionDefinitionsPaginateResponseTypeDef(
    _ListSubscriptionDefinitionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Definitions** *(list) --*Information about a definition.

        - *(dict) --*Information about a definition.

          - **Arn** *(string) --*The ARN of the definition.
          - **CreationTimestamp** *(string) --*The time, in milliseconds since the epoch, when the
          definition was created.
          - **Id** *(string) --*The ID of the definition.
          - **LastUpdatedTimestamp** *(string) --*The time, in milliseconds since the epoch, when
          the definition was last updated.
          - **LatestVersion** *(string) --*The ID of the latest version associated with the
          definition.
          - **LatestVersionArn** *(string) --*The ARN of the latest version associated with the
          definition.
          - **Name** *(string) --*The name of the definition.
          - **Tags** *(dict) --*Tag(s) attached to the resource arn.

            - *(string) --*

              - *(string) --*
    """
