"Main interface for greengrass service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_greengrass.client as client_scope

# pylint: disable=import-self
import mypy_boto3_greengrass.paginator as paginator_scope
from mypy_boto3_greengrass.type_defs import (
    ClientAssociateRoleToGroupResponseTypeDef,
    ClientAssociateServiceRoleToAccountResponseTypeDef,
    ClientCreateConnectorDefinitionInitialVersionTypeDef,
    ClientCreateConnectorDefinitionResponseTypeDef,
    ClientCreateConnectorDefinitionVersionConnectorsTypeDef,
    ClientCreateConnectorDefinitionVersionResponseTypeDef,
    ClientCreateCoreDefinitionInitialVersionTypeDef,
    ClientCreateCoreDefinitionResponseTypeDef,
    ClientCreateCoreDefinitionVersionCoresTypeDef,
    ClientCreateCoreDefinitionVersionResponseTypeDef,
    ClientCreateDeploymentResponseTypeDef,
    ClientCreateDeviceDefinitionInitialVersionTypeDef,
    ClientCreateDeviceDefinitionResponseTypeDef,
    ClientCreateDeviceDefinitionVersionDevicesTypeDef,
    ClientCreateDeviceDefinitionVersionResponseTypeDef,
    ClientCreateFunctionDefinitionInitialVersionTypeDef,
    ClientCreateFunctionDefinitionResponseTypeDef,
    ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef,
    ClientCreateFunctionDefinitionVersionFunctionsTypeDef,
    ClientCreateFunctionDefinitionVersionResponseTypeDef,
    ClientCreateGroupCertificateAuthorityResponseTypeDef,
    ClientCreateGroupInitialVersionTypeDef,
    ClientCreateGroupResponseTypeDef,
    ClientCreateGroupVersionResponseTypeDef,
    ClientCreateLoggerDefinitionInitialVersionTypeDef,
    ClientCreateLoggerDefinitionResponseTypeDef,
    ClientCreateLoggerDefinitionVersionLoggersTypeDef,
    ClientCreateLoggerDefinitionVersionResponseTypeDef,
    ClientCreateResourceDefinitionInitialVersionTypeDef,
    ClientCreateResourceDefinitionResponseTypeDef,
    ClientCreateResourceDefinitionVersionResourcesTypeDef,
    ClientCreateResourceDefinitionVersionResponseTypeDef,
    ClientCreateSoftwareUpdateJobResponseTypeDef,
    ClientCreateSubscriptionDefinitionInitialVersionTypeDef,
    ClientCreateSubscriptionDefinitionResponseTypeDef,
    ClientCreateSubscriptionDefinitionVersionResponseTypeDef,
    ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef,
    ClientDisassociateRoleFromGroupResponseTypeDef,
    ClientDisassociateServiceRoleFromAccountResponseTypeDef,
    ClientGetAssociatedRoleResponseTypeDef,
    ClientGetBulkDeploymentStatusResponseTypeDef,
    ClientGetConnectivityInfoResponseTypeDef,
    ClientGetConnectorDefinitionResponseTypeDef,
    ClientGetConnectorDefinitionVersionResponseTypeDef,
    ClientGetCoreDefinitionResponseTypeDef,
    ClientGetCoreDefinitionVersionResponseTypeDef,
    ClientGetDeploymentStatusResponseTypeDef,
    ClientGetDeviceDefinitionResponseTypeDef,
    ClientGetDeviceDefinitionVersionResponseTypeDef,
    ClientGetFunctionDefinitionResponseTypeDef,
    ClientGetFunctionDefinitionVersionResponseTypeDef,
    ClientGetGroupCertificateAuthorityResponseTypeDef,
    ClientGetGroupCertificateConfigurationResponseTypeDef,
    ClientGetGroupResponseTypeDef,
    ClientGetGroupVersionResponseTypeDef,
    ClientGetLoggerDefinitionResponseTypeDef,
    ClientGetLoggerDefinitionVersionResponseTypeDef,
    ClientGetResourceDefinitionResponseTypeDef,
    ClientGetResourceDefinitionVersionResponseTypeDef,
    ClientGetServiceRoleForAccountResponseTypeDef,
    ClientGetSubscriptionDefinitionResponseTypeDef,
    ClientGetSubscriptionDefinitionVersionResponseTypeDef,
    ClientListBulkDeploymentDetailedReportsResponseTypeDef,
    ClientListBulkDeploymentsResponseTypeDef,
    ClientListConnectorDefinitionVersionsResponseTypeDef,
    ClientListConnectorDefinitionsResponseTypeDef,
    ClientListCoreDefinitionVersionsResponseTypeDef,
    ClientListCoreDefinitionsResponseTypeDef,
    ClientListDeploymentsResponseTypeDef,
    ClientListDeviceDefinitionVersionsResponseTypeDef,
    ClientListDeviceDefinitionsResponseTypeDef,
    ClientListFunctionDefinitionVersionsResponseTypeDef,
    ClientListFunctionDefinitionsResponseTypeDef,
    ClientListGroupCertificateAuthoritiesResponseTypeDef,
    ClientListGroupVersionsResponseTypeDef,
    ClientListGroupsResponseTypeDef,
    ClientListLoggerDefinitionVersionsResponseTypeDef,
    ClientListLoggerDefinitionsResponseTypeDef,
    ClientListResourceDefinitionVersionsResponseTypeDef,
    ClientListResourceDefinitionsResponseTypeDef,
    ClientListSubscriptionDefinitionVersionsResponseTypeDef,
    ClientListSubscriptionDefinitionsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientResetDeploymentsResponseTypeDef,
    ClientStartBulkDeploymentResponseTypeDef,
    ClientUpdateConnectivityInfoConnectivityInfoTypeDef,
    ClientUpdateConnectivityInfoResponseTypeDef,
    ClientUpdateGroupCertificateConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [Greengrass.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_role_to_group(
        self, GroupId: str, RoleArn: str
    ) -> ClientAssociateRoleToGroupResponseTypeDef:
        """
        [Client.associate_role_to_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.associate_role_to_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_service_role_to_account(
        self, RoleArn: str
    ) -> ClientAssociateServiceRoleToAccountResponseTypeDef:
        """
        [Client.associate_service_role_to_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.associate_service_role_to_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_connector_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateConnectorDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateConnectorDefinitionResponseTypeDef:
        """
        [Client.create_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_connector_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_connector_definition_version(
        self,
        ConnectorDefinitionId: str,
        AmznClientToken: str = None,
        Connectors: List[ClientCreateConnectorDefinitionVersionConnectorsTypeDef] = None,
    ) -> ClientCreateConnectorDefinitionVersionResponseTypeDef:
        """
        [Client.create_connector_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_connector_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_core_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateCoreDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateCoreDefinitionResponseTypeDef:
        """
        [Client.create_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_core_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_core_definition_version(
        self,
        CoreDefinitionId: str,
        AmznClientToken: str = None,
        Cores: List[ClientCreateCoreDefinitionVersionCoresTypeDef] = None,
    ) -> ClientCreateCoreDefinitionVersionResponseTypeDef:
        """
        [Client.create_core_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_core_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_deployment(
        self,
        DeploymentType: Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        GroupId: str,
        AmznClientToken: str = None,
        DeploymentId: str = None,
        GroupVersionId: str = None,
    ) -> ClientCreateDeploymentResponseTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_device_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateDeviceDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateDeviceDefinitionResponseTypeDef:
        """
        [Client.create_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_device_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_device_definition_version(
        self,
        DeviceDefinitionId: str,
        AmznClientToken: str = None,
        Devices: List[ClientCreateDeviceDefinitionVersionDevicesTypeDef] = None,
    ) -> ClientCreateDeviceDefinitionVersionResponseTypeDef:
        """
        [Client.create_device_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_device_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_function_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateFunctionDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateFunctionDefinitionResponseTypeDef:
        """
        [Client.create_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_function_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_function_definition_version(
        self,
        FunctionDefinitionId: str,
        AmznClientToken: str = None,
        DefaultConfig: ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef = None,
        Functions: List[ClientCreateFunctionDefinitionVersionFunctionsTypeDef] = None,
    ) -> ClientCreateFunctionDefinitionVersionResponseTypeDef:
        """
        [Client.create_function_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_function_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateGroupInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group_certificate_authority(
        self, GroupId: str, AmznClientToken: str = None
    ) -> ClientCreateGroupCertificateAuthorityResponseTypeDef:
        """
        [Client.create_group_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_group_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group_version(
        self,
        GroupId: str,
        AmznClientToken: str = None,
        ConnectorDefinitionVersionArn: str = None,
        CoreDefinitionVersionArn: str = None,
        DeviceDefinitionVersionArn: str = None,
        FunctionDefinitionVersionArn: str = None,
        LoggerDefinitionVersionArn: str = None,
        ResourceDefinitionVersionArn: str = None,
        SubscriptionDefinitionVersionArn: str = None,
    ) -> ClientCreateGroupVersionResponseTypeDef:
        """
        [Client.create_group_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_group_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_logger_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateLoggerDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateLoggerDefinitionResponseTypeDef:
        """
        [Client.create_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_logger_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_logger_definition_version(
        self,
        LoggerDefinitionId: str,
        AmznClientToken: str = None,
        Loggers: List[ClientCreateLoggerDefinitionVersionLoggersTypeDef] = None,
    ) -> ClientCreateLoggerDefinitionVersionResponseTypeDef:
        """
        [Client.create_logger_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_logger_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateResourceDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateResourceDefinitionResponseTypeDef:
        """
        [Client.create_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_resource_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource_definition_version(
        self,
        ResourceDefinitionId: str,
        AmznClientToken: str = None,
        Resources: List[ClientCreateResourceDefinitionVersionResourcesTypeDef] = None,
    ) -> ClientCreateResourceDefinitionVersionResponseTypeDef:
        """
        [Client.create_resource_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_resource_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_software_update_job(
        self,
        S3UrlSignerRole: str,
        SoftwareToUpdate: Literal["core", "ota_agent"],
        UpdateTargets: List[str],
        UpdateTargetsArchitecture: Literal["armv6l", "armv7l", "x86_64", "aarch64"],
        UpdateTargetsOperatingSystem: Literal["ubuntu", "raspbian", "amazon_linux", "openwrt"],
        AmznClientToken: str = None,
        UpdateAgentLogLevel: Literal[
            "NONE", "TRACE", "DEBUG", "VERBOSE", "INFO", "WARN", "ERROR", "FATAL"
        ] = None,
    ) -> ClientCreateSoftwareUpdateJobResponseTypeDef:
        """
        [Client.create_software_update_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_software_update_job)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subscription_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: ClientCreateSubscriptionDefinitionInitialVersionTypeDef = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateSubscriptionDefinitionResponseTypeDef:
        """
        [Client.create_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_subscription_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        AmznClientToken: str = None,
        Subscriptions: List[ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef] = None,
    ) -> ClientCreateSubscriptionDefinitionVersionResponseTypeDef:
        """
        [Client.create_subscription_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.create_subscription_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_connector_definition(self, ConnectorDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.delete_connector_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_core_definition(self, CoreDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.delete_core_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_device_definition(self, DeviceDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.delete_device_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_function_definition(self, FunctionDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.delete_function_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_group(self, GroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.delete_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_logger_definition(self, LoggerDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.delete_logger_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource_definition(self, ResourceDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.delete_resource_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_subscription_definition(self, SubscriptionDefinitionId: str) -> Dict[str, Any]:
        """
        [Client.delete_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.delete_subscription_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_role_from_group(
        self, GroupId: str
    ) -> ClientDisassociateRoleFromGroupResponseTypeDef:
        """
        [Client.disassociate_role_from_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.disassociate_role_from_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_service_role_from_account(
        self, *args: Any, **kwargs: Any
    ) -> ClientDisassociateServiceRoleFromAccountResponseTypeDef:
        """
        [Client.disassociate_service_role_from_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.disassociate_service_role_from_account)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_associated_role(self, GroupId: str) -> ClientGetAssociatedRoleResponseTypeDef:
        """
        [Client.get_associated_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_associated_role)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_bulk_deployment_status(
        self, BulkDeploymentId: str
    ) -> ClientGetBulkDeploymentStatusResponseTypeDef:
        """
        [Client.get_bulk_deployment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_bulk_deployment_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connectivity_info(self, ThingName: str) -> ClientGetConnectivityInfoResponseTypeDef:
        """
        [Client.get_connectivity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_connectivity_info)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connector_definition(
        self, ConnectorDefinitionId: str
    ) -> ClientGetConnectorDefinitionResponseTypeDef:
        """
        [Client.get_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_connector_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_connector_definition_version(
        self, ConnectorDefinitionId: str, ConnectorDefinitionVersionId: str, NextToken: str = None
    ) -> ClientGetConnectorDefinitionVersionResponseTypeDef:
        """
        [Client.get_connector_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_connector_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_core_definition(self, CoreDefinitionId: str) -> ClientGetCoreDefinitionResponseTypeDef:
        """
        [Client.get_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_core_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_core_definition_version(
        self, CoreDefinitionId: str, CoreDefinitionVersionId: str
    ) -> ClientGetCoreDefinitionVersionResponseTypeDef:
        """
        [Client.get_core_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_core_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_deployment_status(
        self, DeploymentId: str, GroupId: str
    ) -> ClientGetDeploymentStatusResponseTypeDef:
        """
        [Client.get_deployment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_deployment_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device_definition(
        self, DeviceDefinitionId: str
    ) -> ClientGetDeviceDefinitionResponseTypeDef:
        """
        [Client.get_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_device_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_device_definition_version(
        self, DeviceDefinitionId: str, DeviceDefinitionVersionId: str, NextToken: str = None
    ) -> ClientGetDeviceDefinitionVersionResponseTypeDef:
        """
        [Client.get_device_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_device_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_definition(
        self, FunctionDefinitionId: str
    ) -> ClientGetFunctionDefinitionResponseTypeDef:
        """
        [Client.get_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_function_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_definition_version(
        self, FunctionDefinitionId: str, FunctionDefinitionVersionId: str, NextToken: str = None
    ) -> ClientGetFunctionDefinitionVersionResponseTypeDef:
        """
        [Client.get_function_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_function_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group(self, GroupId: str) -> ClientGetGroupResponseTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group_certificate_authority(
        self, CertificateAuthorityId: str, GroupId: str
    ) -> ClientGetGroupCertificateAuthorityResponseTypeDef:
        """
        [Client.get_group_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_group_certificate_authority)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group_certificate_configuration(
        self, GroupId: str
    ) -> ClientGetGroupCertificateConfigurationResponseTypeDef:
        """
        [Client.get_group_certificate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_group_certificate_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group_version(
        self, GroupId: str, GroupVersionId: str
    ) -> ClientGetGroupVersionResponseTypeDef:
        """
        [Client.get_group_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_group_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_logger_definition(
        self, LoggerDefinitionId: str
    ) -> ClientGetLoggerDefinitionResponseTypeDef:
        """
        [Client.get_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_logger_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_logger_definition_version(
        self, LoggerDefinitionId: str, LoggerDefinitionVersionId: str, NextToken: str = None
    ) -> ClientGetLoggerDefinitionVersionResponseTypeDef:
        """
        [Client.get_logger_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_logger_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_definition(
        self, ResourceDefinitionId: str
    ) -> ClientGetResourceDefinitionResponseTypeDef:
        """
        [Client.get_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_resource_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_definition_version(
        self, ResourceDefinitionId: str, ResourceDefinitionVersionId: str
    ) -> ClientGetResourceDefinitionVersionResponseTypeDef:
        """
        [Client.get_resource_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_resource_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_role_for_account(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetServiceRoleForAccountResponseTypeDef:
        """
        [Client.get_service_role_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_service_role_for_account)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_subscription_definition(
        self, SubscriptionDefinitionId: str
    ) -> ClientGetSubscriptionDefinitionResponseTypeDef:
        """
        [Client.get_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        SubscriptionDefinitionVersionId: str,
        NextToken: str = None,
    ) -> ClientGetSubscriptionDefinitionVersionResponseTypeDef:
        """
        [Client.get_subscription_definition_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bulk_deployment_detailed_reports(
        self, BulkDeploymentId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListBulkDeploymentDetailedReportsResponseTypeDef:
        """
        [Client.list_bulk_deployment_detailed_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_bulk_deployment_detailed_reports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_bulk_deployments(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListBulkDeploymentsResponseTypeDef:
        """
        [Client.list_bulk_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_bulk_deployments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_connector_definition_versions(
        self, ConnectorDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListConnectorDefinitionVersionsResponseTypeDef:
        """
        [Client.list_connector_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_connector_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_connector_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListConnectorDefinitionsResponseTypeDef:
        """
        [Client.list_connector_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_connector_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_core_definition_versions(
        self, CoreDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListCoreDefinitionVersionsResponseTypeDef:
        """
        [Client.list_core_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_core_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_core_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListCoreDefinitionsResponseTypeDef:
        """
        [Client.list_core_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_core_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_deployments(
        self, GroupId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListDeploymentsResponseTypeDef:
        """
        [Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_deployments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_device_definition_versions(
        self, DeviceDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListDeviceDefinitionVersionsResponseTypeDef:
        """
        [Client.list_device_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_device_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_device_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListDeviceDefinitionsResponseTypeDef:
        """
        [Client.list_device_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_device_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_function_definition_versions(
        self, FunctionDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListFunctionDefinitionVersionsResponseTypeDef:
        """
        [Client.list_function_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_function_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_function_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListFunctionDefinitionsResponseTypeDef:
        """
        [Client.list_function_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_function_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_group_certificate_authorities(
        self, GroupId: str
    ) -> ClientListGroupCertificateAuthoritiesResponseTypeDef:
        """
        [Client.list_group_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_group_certificate_authorities)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_group_versions(
        self, GroupId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListGroupVersionsResponseTypeDef:
        """
        [Client.list_group_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_group_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_groups(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListGroupsResponseTypeDef:
        """
        [Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_logger_definition_versions(
        self, LoggerDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListLoggerDefinitionVersionsResponseTypeDef:
        """
        [Client.list_logger_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_logger_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_logger_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListLoggerDefinitionsResponseTypeDef:
        """
        [Client.list_logger_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_logger_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_definition_versions(
        self, ResourceDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListResourceDefinitionVersionsResponseTypeDef:
        """
        [Client.list_resource_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_resource_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListResourceDefinitionsResponseTypeDef:
        """
        [Client.list_resource_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_resource_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_subscription_definition_versions(
        self, SubscriptionDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ClientListSubscriptionDefinitionVersionsResponseTypeDef:
        """
        [Client.list_subscription_definition_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_subscription_definition_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_subscription_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ClientListSubscriptionDefinitionsResponseTypeDef:
        """
        [Client.list_subscription_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_subscription_definitions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.list_tags_for_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_deployments(
        self, GroupId: str, AmznClientToken: str = None, Force: bool = None
    ) -> ClientResetDeploymentsResponseTypeDef:
        """
        [Client.reset_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.reset_deployments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_bulk_deployment(
        self,
        ExecutionRoleArn: str,
        InputFileUri: str,
        AmznClientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientStartBulkDeploymentResponseTypeDef:
        """
        [Client.start_bulk_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.start_bulk_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_bulk_deployment(self, BulkDeploymentId: str) -> Dict[str, Any]:
        """
        [Client.stop_bulk_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.stop_bulk_deployment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, tags: Dict[str, str] = None) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.tag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.untag_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_connectivity_info(
        self,
        ThingName: str,
        ConnectivityInfo: List[ClientUpdateConnectivityInfoConnectivityInfoTypeDef] = None,
    ) -> ClientUpdateConnectivityInfoResponseTypeDef:
        """
        [Client.update_connectivity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.update_connectivity_info)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_connector_definition(
        self, ConnectorDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_connector_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.update_connector_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_core_definition(self, CoreDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_core_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.update_core_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_device_definition(self, DeviceDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_device_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.update_device_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_function_definition(
        self, FunctionDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_function_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.update_function_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group(self, GroupId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.update_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group_certificate_configuration(
        self, GroupId: str, CertificateExpiryInMilliseconds: str = None
    ) -> ClientUpdateGroupCertificateConfigurationResponseTypeDef:
        """
        [Client.update_group_certificate_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.update_group_certificate_configuration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_logger_definition(self, LoggerDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Client.update_logger_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.update_logger_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_resource_definition(
        self, ResourceDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_resource_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.update_resource_definition)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_subscription_definition(
        self, SubscriptionDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_subscription_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Client.update_subscription_definition)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_bulk_deployment_detailed_reports"]
    ) -> paginator_scope.ListBulkDeploymentDetailedReportsPaginator:
        """
        [Paginator.ListBulkDeploymentDetailedReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_bulk_deployments"]
    ) -> paginator_scope.ListBulkDeploymentsPaginator:
        """
        [Paginator.ListBulkDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeployments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_connector_definition_versions"]
    ) -> paginator_scope.ListConnectorDefinitionVersionsPaginator:
        """
        [Paginator.ListConnectorDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_connector_definitions"]
    ) -> paginator_scope.ListConnectorDefinitionsPaginator:
        """
        [Paginator.ListConnectorDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_core_definition_versions"]
    ) -> paginator_scope.ListCoreDefinitionVersionsPaginator:
        """
        [Paginator.ListCoreDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_core_definitions"]
    ) -> paginator_scope.ListCoreDefinitionsPaginator:
        """
        [Paginator.ListCoreDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> paginator_scope.ListDeploymentsPaginator:
        """
        [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListDeployments)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_device_definition_versions"]
    ) -> paginator_scope.ListDeviceDefinitionVersionsPaginator:
        """
        [Paginator.ListDeviceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_device_definitions"]
    ) -> paginator_scope.ListDeviceDefinitionsPaginator:
        """
        [Paginator.ListDeviceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_function_definition_versions"]
    ) -> paginator_scope.ListFunctionDefinitionVersionsPaginator:
        """
        [Paginator.ListFunctionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_function_definitions"]
    ) -> paginator_scope.ListFunctionDefinitionsPaginator:
        """
        [Paginator.ListFunctionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_group_versions"]
    ) -> paginator_scope.ListGroupVersionsPaginator:
        """
        [Paginator.ListGroupVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListGroupVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_groups"]
    ) -> paginator_scope.ListGroupsPaginator:
        """
        [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_logger_definition_versions"]
    ) -> paginator_scope.ListLoggerDefinitionVersionsPaginator:
        """
        [Paginator.ListLoggerDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_logger_definitions"]
    ) -> paginator_scope.ListLoggerDefinitionsPaginator:
        """
        [Paginator.ListLoggerDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_definition_versions"]
    ) -> paginator_scope.ListResourceDefinitionVersionsPaginator:
        """
        [Paginator.ListResourceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_definitions"]
    ) -> paginator_scope.ListResourceDefinitionsPaginator:
        """
        [Paginator.ListResourceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_subscription_definition_versions"]
    ) -> paginator_scope.ListSubscriptionDefinitionVersionsPaginator:
        """
        [Paginator.ListSubscriptionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_subscription_definitions"]
    ) -> paginator_scope.ListSubscriptionDefinitionsPaginator:
        """
        [Paginator.ListSubscriptionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitions)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
