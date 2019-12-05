"Main interface for greengrass service type defs"
from __future__ import annotations

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


ClientAssociateRoleToGroupResponseTypeDef = TypedDict(
    "ClientAssociateRoleToGroupResponseTypeDef", {"AssociatedAt": str}, total=False
)

ClientAssociateServiceRoleToAccountResponseTypeDef = TypedDict(
    "ClientAssociateServiceRoleToAccountResponseTypeDef", {"AssociatedAt": str}, total=False
)

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
    pass


ClientCreateConnectorDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateConnectorDefinitionInitialVersionTypeDef",
    {"Connectors": List[ClientCreateConnectorDefinitionInitialVersionConnectorsTypeDef]},
    total=False,
)

ClientCreateConnectorDefinitionResponseTypeDef = TypedDict(
    "ClientCreateConnectorDefinitionResponseTypeDef",
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
    pass


ClientCreateConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateConnectorDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

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
    pass


ClientCreateCoreDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateCoreDefinitionInitialVersionTypeDef",
    {"Cores": List[ClientCreateCoreDefinitionInitialVersionCoresTypeDef]},
    total=False,
)

ClientCreateCoreDefinitionResponseTypeDef = TypedDict(
    "ClientCreateCoreDefinitionResponseTypeDef",
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
    pass


ClientCreateCoreDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateCoreDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateDeploymentResponseTypeDef = TypedDict(
    "ClientCreateDeploymentResponseTypeDef",
    {"DeploymentArn": str, "DeploymentId": str},
    total=False,
)

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
    pass


ClientCreateDeviceDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateDeviceDefinitionInitialVersionTypeDef",
    {"Devices": List[ClientCreateDeviceDefinitionInitialVersionDevicesTypeDef]},
    total=False,
)

ClientCreateDeviceDefinitionResponseTypeDef = TypedDict(
    "ClientCreateDeviceDefinitionResponseTypeDef",
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
    pass


ClientCreateDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateDeviceDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionRunAsTypeDef,
    },
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef",
    {"Execution": ClientCreateFunctionDefinitionInitialVersionDefaultConfigExecutionTypeDef},
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef,
    },
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    {"Permission": Literal["ro", "rw"], "ResourceId": str},
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
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

ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef",
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

ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientCreateFunctionDefinitionInitialVersionFunctionsFunctionConfigurationTypeDef,
        "Id": str,
    },
    total=False,
)

ClientCreateFunctionDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionInitialVersionTypeDef",
    {
        "DefaultConfig": ClientCreateFunctionDefinitionInitialVersionDefaultConfigTypeDef,
        "Functions": List[ClientCreateFunctionDefinitionInitialVersionFunctionsTypeDef],
    },
    total=False,
)

ClientCreateFunctionDefinitionResponseTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionResponseTypeDef",
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

ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionVersionDefaultConfigExecutionRunAsTypeDef,
    },
    total=False,
)

ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionDefaultConfigTypeDef",
    {"Execution": ClientCreateFunctionDefinitionVersionDefaultConfigExecutionTypeDef},
    total=False,
)

ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef,
    },
    total=False,
)

ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    {"Permission": Literal["ro", "rw"], "ResourceId": str},
    total=False,
)

ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationEnvironmentTypeDef",
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

ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef",
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

ClientCreateFunctionDefinitionVersionFunctionsTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientCreateFunctionDefinitionVersionFunctionsFunctionConfigurationTypeDef,
        "Id": str,
    },
    total=False,
)

ClientCreateFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateFunctionDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "ClientCreateGroupCertificateAuthorityResponseTypeDef",
    {"GroupCertificateAuthorityArn": str},
    total=False,
)

ClientCreateGroupInitialVersionTypeDef = TypedDict(
    "ClientCreateGroupInitialVersionTypeDef",
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

ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef",
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

ClientCreateGroupVersionResponseTypeDef = TypedDict(
    "ClientCreateGroupVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

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
    pass


ClientCreateLoggerDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateLoggerDefinitionInitialVersionTypeDef",
    {"Loggers": List[ClientCreateLoggerDefinitionInitialVersionLoggersTypeDef]},
    total=False,
)

ClientCreateLoggerDefinitionResponseTypeDef = TypedDict(
    "ClientCreateLoggerDefinitionResponseTypeDef",
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
    pass


ClientCreateLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateLoggerDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef,
        "S3Uri": str,
    },
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef,
        "SageMakerJobArn": str,
    },
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    {"ARN": str, "AdditionalStagingLabelsToDownload": List[str]},
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef,
        "LocalVolumeResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef,
        "S3MachineLearningModelResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef,
        "SageMakerMachineLearningModelResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef,
        "SecretsManagerSecretResourceData": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef,
    },
    total=False,
)

ClientCreateResourceDefinitionInitialVersionResourcesTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionResourcesTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ClientCreateResourceDefinitionInitialVersionResourcesResourceDataContainerTypeDef,
    },
)

ClientCreateResourceDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateResourceDefinitionInitialVersionTypeDef",
    {"Resources": List[ClientCreateResourceDefinitionInitialVersionResourcesTypeDef]},
    total=False,
)

ClientCreateResourceDefinitionResponseTypeDef = TypedDict(
    "ClientCreateResourceDefinitionResponseTypeDef",
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

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef,
        "S3Uri": str,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef,
        "SageMakerJobArn": str,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    {"ARN": str, "AdditionalStagingLabelsToDownload": List[str]},
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef,
        "LocalVolumeResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef,
        "S3MachineLearningModelResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef,
        "SageMakerMachineLearningModelResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef,
        "SecretsManagerSecretResourceData": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef,
    },
    total=False,
)

ClientCreateResourceDefinitionVersionResourcesTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResourcesTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ClientCreateResourceDefinitionVersionResourcesResourceDataContainerTypeDef,
    },
)

ClientCreateResourceDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateResourceDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateSoftwareUpdateJobResponseTypeDef = TypedDict(
    "ClientCreateSoftwareUpdateJobResponseTypeDef",
    {"IotJobArn": str, "IotJobId": str, "PlatformSoftwareVersion": str},
    total=False,
)

ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef = TypedDict(
    "ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
)

ClientCreateSubscriptionDefinitionInitialVersionTypeDef = TypedDict(
    "ClientCreateSubscriptionDefinitionInitialVersionTypeDef",
    {"Subscriptions": List[ClientCreateSubscriptionDefinitionInitialVersionSubscriptionsTypeDef]},
    total=False,
)

ClientCreateSubscriptionDefinitionResponseTypeDef = TypedDict(
    "ClientCreateSubscriptionDefinitionResponseTypeDef",
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

ClientCreateSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "ClientCreateSubscriptionDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef = TypedDict(
    "ClientCreateSubscriptionDefinitionVersionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
)

ClientDisassociateRoleFromGroupResponseTypeDef = TypedDict(
    "ClientDisassociateRoleFromGroupResponseTypeDef", {"DisassociatedAt": str}, total=False
)

ClientDisassociateServiceRoleFromAccountResponseTypeDef = TypedDict(
    "ClientDisassociateServiceRoleFromAccountResponseTypeDef", {"DisassociatedAt": str}, total=False
)

ClientGetAssociatedRoleResponseTypeDef = TypedDict(
    "ClientGetAssociatedRoleResponseTypeDef", {"AssociatedAt": str, "RoleArn": str}, total=False
)

ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef = TypedDict(
    "ClientGetBulkDeploymentStatusResponseBulkDeploymentMetricsTypeDef",
    {"InvalidInputRecords": int, "RecordsProcessed": int, "RetryAttempts": int},
    total=False,
)

ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef = TypedDict(
    "ClientGetBulkDeploymentStatusResponseErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)

ClientGetBulkDeploymentStatusResponseTypeDef = TypedDict(
    "ClientGetBulkDeploymentStatusResponseTypeDef",
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

ClientGetConnectivityInfoResponseConnectivityInfoTypeDef = TypedDict(
    "ClientGetConnectivityInfoResponseConnectivityInfoTypeDef",
    {"HostAddress": str, "Id": str, "Metadata": str, "PortNumber": int},
    total=False,
)

ClientGetConnectivityInfoResponseTypeDef = TypedDict(
    "ClientGetConnectivityInfoResponseTypeDef",
    {
        "ConnectivityInfo": List[ClientGetConnectivityInfoResponseConnectivityInfoTypeDef],
        "Message": str,
    },
    total=False,
)

ClientGetConnectorDefinitionResponseTypeDef = TypedDict(
    "ClientGetConnectorDefinitionResponseTypeDef",
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

ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef = TypedDict(
    "ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef",
    {"ConnectorArn": str, "Id": str, "Parameters": Dict[str, str]},
    total=False,
)

ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetConnectorDefinitionVersionResponseDefinitionTypeDef",
    {"Connectors": List[ClientGetConnectorDefinitionVersionResponseDefinitionConnectorsTypeDef]},
    total=False,
)

ClientGetConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetConnectorDefinitionVersionResponseTypeDef",
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

ClientGetCoreDefinitionResponseTypeDef = TypedDict(
    "ClientGetCoreDefinitionResponseTypeDef",
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

ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef = TypedDict(
    "ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef",
    {"CertificateArn": str, "Id": str, "SyncShadow": bool, "ThingArn": str},
    total=False,
)

ClientGetCoreDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetCoreDefinitionVersionResponseDefinitionTypeDef",
    {"Cores": List[ClientGetCoreDefinitionVersionResponseDefinitionCoresTypeDef]},
    total=False,
)

ClientGetCoreDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetCoreDefinitionVersionResponseTypeDef",
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

ClientGetDeploymentStatusResponseErrorDetailsTypeDef = TypedDict(
    "ClientGetDeploymentStatusResponseErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)

ClientGetDeploymentStatusResponseTypeDef = TypedDict(
    "ClientGetDeploymentStatusResponseTypeDef",
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

ClientGetDeviceDefinitionResponseTypeDef = TypedDict(
    "ClientGetDeviceDefinitionResponseTypeDef",
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

ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef = TypedDict(
    "ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef",
    {"CertificateArn": str, "Id": str, "SyncShadow": bool, "ThingArn": str},
    total=False,
)

ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetDeviceDefinitionVersionResponseDefinitionTypeDef",
    {"Devices": List[ClientGetDeviceDefinitionVersionResponseDefinitionDevicesTypeDef]},
    total=False,
)

ClientGetDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetDeviceDefinitionVersionResponseTypeDef",
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

ClientGetFunctionDefinitionResponseTypeDef = TypedDict(
    "ClientGetFunctionDefinitionResponseTypeDef",
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

ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionRunAsTypeDef,
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef",
    {
        "Execution": ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigExecutionTypeDef
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef",
    {"Gid": int, "Uid": int},
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentExecutionRunAsTypeDef,
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentResourceAccessPoliciesTypeDef",
    {"Permission": Literal["ro", "rw"], "ResourceId": str},
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationEnvironmentTypeDef",
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

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef",
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

ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsFunctionConfigurationTypeDef,
        "Id": str,
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseDefinitionTypeDef",
    {
        "DefaultConfig": ClientGetFunctionDefinitionVersionResponseDefinitionDefaultConfigTypeDef,
        "Functions": List[ClientGetFunctionDefinitionVersionResponseDefinitionFunctionsTypeDef],
    },
    total=False,
)

ClientGetFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetFunctionDefinitionVersionResponseTypeDef",
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

ClientGetGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "ClientGetGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
        "PemEncodedCertificate": str,
    },
    total=False,
)

ClientGetGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "ClientGetGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
    },
    total=False,
)

ClientGetGroupResponseTypeDef = TypedDict(
    "ClientGetGroupResponseTypeDef",
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

ClientGetGroupVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetGroupVersionResponseDefinitionTypeDef",
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

ClientGetGroupVersionResponseTypeDef = TypedDict(
    "ClientGetGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetGroupVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)

ClientGetLoggerDefinitionResponseTypeDef = TypedDict(
    "ClientGetLoggerDefinitionResponseTypeDef",
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

ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef = TypedDict(
    "ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef",
    {
        "Component": Literal["GreengrassSystem", "Lambda"],
        "Id": str,
        "Level": Literal["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
        "Space": int,
        "Type": Literal["FileSystem", "AWSCloudWatch"],
    },
    total=False,
)

ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef",
    {"Loggers": List[ClientGetLoggerDefinitionVersionResponseDefinitionLoggersTypeDef]},
    total=False,
)

ClientGetLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetLoggerDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)

ClientGetResourceDefinitionResponseTypeDef = TypedDict(
    "ClientGetResourceDefinitionResponseTypeDef",
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

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef",
    {"AutoAddGroupOwner": bool, "GroupOwner": str},
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataGroupOwnerSettingTypeDef,
        "SourcePath": str,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataOwnerSettingTypeDef,
        "S3Uri": str,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataOwnerSettingTypeDef,
        "SageMakerJobArn": str,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef",
    {"ARN": str, "AdditionalStagingLabelsToDownload": List[str]},
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalDeviceResourceDataTypeDef,
        "LocalVolumeResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerLocalVolumeResourceDataTypeDef,
        "S3MachineLearningModelResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerS3MachineLearningModelResourceDataTypeDef,
        "SageMakerMachineLearningModelResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSageMakerMachineLearningModelResourceDataTypeDef,
        "SecretsManagerSecretResourceData": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerSecretsManagerSecretResourceDataTypeDef,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ClientGetResourceDefinitionVersionResponseDefinitionResourcesResourceDataContainerTypeDef,
    },
    total=False,
)

ClientGetResourceDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseDefinitionTypeDef",
    {"Resources": List[ClientGetResourceDefinitionVersionResponseDefinitionResourcesTypeDef]},
    total=False,
)

ClientGetResourceDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ClientGetResourceDefinitionVersionResponseDefinitionTypeDef,
        "Id": str,
        "Version": str,
    },
    total=False,
)

ClientGetServiceRoleForAccountResponseTypeDef = TypedDict(
    "ClientGetServiceRoleForAccountResponseTypeDef",
    {"AssociatedAt": str, "RoleArn": str},
    total=False,
)

ClientGetSubscriptionDefinitionResponseTypeDef = TypedDict(
    "ClientGetSubscriptionDefinitionResponseTypeDef",
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

ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef = TypedDict(
    "ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef",
    {"Id": str, "Source": str, "Subject": str, "Target": str},
    total=False,
)

ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef = TypedDict(
    "ClientGetSubscriptionDefinitionVersionResponseDefinitionTypeDef",
    {
        "Subscriptions": List[
            ClientGetSubscriptionDefinitionVersionResponseDefinitionSubscriptionsTypeDef
        ]
    },
    total=False,
)

ClientGetSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "ClientGetSubscriptionDefinitionVersionResponseTypeDef",
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

ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef = TypedDict(
    "ClientListBulkDeploymentDetailedReportsResponseDeploymentsErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)

ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef = TypedDict(
    "ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef",
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

ClientListBulkDeploymentDetailedReportsResponseTypeDef = TypedDict(
    "ClientListBulkDeploymentDetailedReportsResponseTypeDef",
    {
        "Deployments": List[ClientListBulkDeploymentDetailedReportsResponseDeploymentsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef = TypedDict(
    "ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str, "CreatedAt": str},
    total=False,
)

ClientListBulkDeploymentsResponseTypeDef = TypedDict(
    "ClientListBulkDeploymentsResponseTypeDef",
    {
        "BulkDeployments": List[ClientListBulkDeploymentsResponseBulkDeploymentsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListConnectorDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListConnectorDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListConnectorDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListConnectorDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListConnectorDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)

ClientListConnectorDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListConnectorDefinitionsResponseDefinitionsTypeDef",
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

ClientListConnectorDefinitionsResponseTypeDef = TypedDict(
    "ClientListConnectorDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListConnectorDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListCoreDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListCoreDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListCoreDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListCoreDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListCoreDefinitionVersionsResponseVersionsTypeDef]},
    total=False,
)

ClientListCoreDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListCoreDefinitionsResponseDefinitionsTypeDef",
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

ClientListCoreDefinitionsResponseTypeDef = TypedDict(
    "ClientListCoreDefinitionsResponseTypeDef",
    {"Definitions": List[ClientListCoreDefinitionsResponseDefinitionsTypeDef], "NextToken": str},
    total=False,
)

ClientListDeploymentsResponseDeploymentsTypeDef = TypedDict(
    "ClientListDeploymentsResponseDeploymentsTypeDef",
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

ClientListDeploymentsResponseTypeDef = TypedDict(
    "ClientListDeploymentsResponseTypeDef",
    {"Deployments": List[ClientListDeploymentsResponseDeploymentsTypeDef], "NextToken": str},
    total=False,
)

ClientListDeviceDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListDeviceDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListDeviceDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListDeviceDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListDeviceDefinitionVersionsResponseVersionsTypeDef]},
    total=False,
)

ClientListDeviceDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListDeviceDefinitionsResponseDefinitionsTypeDef",
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

ClientListDeviceDefinitionsResponseTypeDef = TypedDict(
    "ClientListDeviceDefinitionsResponseTypeDef",
    {"Definitions": List[ClientListDeviceDefinitionsResponseDefinitionsTypeDef], "NextToken": str},
    total=False,
)

ClientListFunctionDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListFunctionDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListFunctionDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListFunctionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListFunctionDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)

ClientListFunctionDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListFunctionDefinitionsResponseDefinitionsTypeDef",
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

ClientListFunctionDefinitionsResponseTypeDef = TypedDict(
    "ClientListFunctionDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListFunctionDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef = TypedDict(
    "ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef",
    {"GroupCertificateAuthorityArn": str, "GroupCertificateAuthorityId": str},
    total=False,
)

ClientListGroupCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ClientListGroupCertificateAuthoritiesResponseTypeDef",
    {
        "GroupCertificateAuthorities": List[
            ClientListGroupCertificateAuthoritiesResponseGroupCertificateAuthoritiesTypeDef
        ]
    },
    total=False,
)

ClientListGroupVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListGroupVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListGroupVersionsResponseTypeDef = TypedDict(
    "ClientListGroupVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListGroupVersionsResponseVersionsTypeDef]},
    total=False,
)

ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "ClientListGroupsResponseGroupsTypeDef",
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

ClientListGroupsResponseTypeDef = TypedDict(
    "ClientListGroupsResponseTypeDef",
    {"Groups": List[ClientListGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientListLoggerDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListLoggerDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListLoggerDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListLoggerDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List[ClientListLoggerDefinitionVersionsResponseVersionsTypeDef]},
    total=False,
)

ClientListLoggerDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListLoggerDefinitionsResponseDefinitionsTypeDef",
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

ClientListLoggerDefinitionsResponseTypeDef = TypedDict(
    "ClientListLoggerDefinitionsResponseTypeDef",
    {"Definitions": List[ClientListLoggerDefinitionsResponseDefinitionsTypeDef], "NextToken": str},
    total=False,
)

ClientListResourceDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListResourceDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListResourceDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListResourceDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListResourceDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)

ClientListResourceDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListResourceDefinitionsResponseDefinitionsTypeDef",
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

ClientListResourceDefinitionsResponseTypeDef = TypedDict(
    "ClientListResourceDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListResourceDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef = TypedDict(
    "ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ClientListSubscriptionDefinitionVersionsResponseTypeDef = TypedDict(
    "ClientListSubscriptionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List[ClientListSubscriptionDefinitionVersionsResponseVersionsTypeDef],
    },
    total=False,
)

ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef = TypedDict(
    "ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef",
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

ClientListSubscriptionDefinitionsResponseTypeDef = TypedDict(
    "ClientListSubscriptionDefinitionsResponseTypeDef",
    {
        "Definitions": List[ClientListSubscriptionDefinitionsResponseDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientResetDeploymentsResponseTypeDef = TypedDict(
    "ClientResetDeploymentsResponseTypeDef",
    {"DeploymentArn": str, "DeploymentId": str},
    total=False,
)

ClientStartBulkDeploymentResponseTypeDef = TypedDict(
    "ClientStartBulkDeploymentResponseTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str},
    total=False,
)

ClientUpdateConnectivityInfoConnectivityInfoTypeDef = TypedDict(
    "ClientUpdateConnectivityInfoConnectivityInfoTypeDef",
    {"HostAddress": str, "Id": str, "Metadata": str, "PortNumber": int},
    total=False,
)

ClientUpdateConnectivityInfoResponseTypeDef = TypedDict(
    "ClientUpdateConnectivityInfoResponseTypeDef", {"Message": str, "Version": str}, total=False
)

ClientUpdateGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
    },
    total=False,
)

ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsErrorDetailsTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsErrorDetailsTypeDef",
    {"DetailedErrorCode": str, "DetailedErrorMessage": str},
    total=False,
)

ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsTypeDef",
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

ListBulkDeploymentDetailedReportsPaginateResponseTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsPaginateResponseTypeDef",
    {"Deployments": List[ListBulkDeploymentDetailedReportsPaginateResponseDeploymentsTypeDef]},
    total=False,
)

ListBulkDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "ListBulkDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListBulkDeploymentsPaginateResponseBulkDeploymentsTypeDef = TypedDict(
    "ListBulkDeploymentsPaginateResponseBulkDeploymentsTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str, "CreatedAt": str},
    total=False,
)

ListBulkDeploymentsPaginateResponseTypeDef = TypedDict(
    "ListBulkDeploymentsPaginateResponseTypeDef",
    {"BulkDeployments": List[ListBulkDeploymentsPaginateResponseBulkDeploymentsTypeDef]},
    total=False,
)

ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ListConnectorDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListConnectorDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)

ListConnectorDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListConnectorDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef",
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

ListConnectorDefinitionsPaginateResponseTypeDef = TypedDict(
    "ListConnectorDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListConnectorDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)

ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ListCoreDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "ListCoreDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListCoreDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)

ListCoreDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListCoreDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListCoreDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "ListCoreDefinitionsPaginateResponseDefinitionsTypeDef",
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

ListCoreDefinitionsPaginateResponseTypeDef = TypedDict(
    "ListCoreDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListCoreDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)

ListDeploymentsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDeploymentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDeploymentsPaginateResponseDeploymentsTypeDef = TypedDict(
    "ListDeploymentsPaginateResponseDeploymentsTypeDef",
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

ListDeploymentsPaginateResponseTypeDef = TypedDict(
    "ListDeploymentsPaginateResponseTypeDef",
    {"Deployments": List[ListDeploymentsPaginateResponseDeploymentsTypeDef]},
    total=False,
)

ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ListDeviceDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListDeviceDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)

ListDeviceDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListDeviceDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef",
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

ListDeviceDefinitionsPaginateResponseTypeDef = TypedDict(
    "ListDeviceDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListDeviceDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)

ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ListFunctionDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListFunctionDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)

ListFunctionDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListFunctionDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListFunctionDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "ListFunctionDefinitionsPaginateResponseDefinitionsTypeDef",
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

ListFunctionDefinitionsPaginateResponseTypeDef = TypedDict(
    "ListFunctionDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListFunctionDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)

ListGroupVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListGroupVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListGroupVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListGroupVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ListGroupVersionsPaginateResponseTypeDef = TypedDict(
    "ListGroupVersionsPaginateResponseTypeDef",
    {"Versions": List[ListGroupVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)

ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "ListGroupsPaginateResponseGroupsTypeDef",
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

ListGroupsPaginateResponseTypeDef = TypedDict(
    "ListGroupsPaginateResponseTypeDef",
    {"Groups": List[ListGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)

ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ListLoggerDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListLoggerDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)

ListLoggerDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListLoggerDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef",
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

ListLoggerDefinitionsPaginateResponseTypeDef = TypedDict(
    "ListLoggerDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListLoggerDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)

ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ListResourceDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "ListResourceDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListResourceDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)

ListResourceDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListResourceDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListResourceDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "ListResourceDefinitionsPaginateResponseDefinitionsTypeDef",
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

ListResourceDefinitionsPaginateResponseTypeDef = TypedDict(
    "ListResourceDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListResourceDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)

ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

ListSubscriptionDefinitionVersionsPaginateResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsPaginateResponseTypeDef",
    {"Versions": List[ListSubscriptionDefinitionVersionsPaginateResponseVersionsTypeDef]},
    total=False,
)

ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef = TypedDict(
    "ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef",
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

ListSubscriptionDefinitionsPaginateResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionsPaginateResponseTypeDef",
    {"Definitions": List[ListSubscriptionDefinitionsPaginateResponseDefinitionsTypeDef]},
    total=False,
)
