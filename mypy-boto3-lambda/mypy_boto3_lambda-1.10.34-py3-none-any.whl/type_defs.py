"Main interface for lambda service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientAddLayerVersionPermissionResponseTypeDef = TypedDict(
    "ClientAddLayerVersionPermissionResponseTypeDef",
    {"Statement": str, "RevisionId": str},
    total=False,
)

ClientAddPermissionResponseTypeDef = TypedDict(
    "ClientAddPermissionResponseTypeDef", {"Statement": str}, total=False
)

ClientCreateAliasResponseRoutingConfigTypeDef = TypedDict(
    "ClientCreateAliasResponseRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)

ClientCreateAliasResponseTypeDef = TypedDict(
    "ClientCreateAliasResponseTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": ClientCreateAliasResponseRoutingConfigTypeDef,
        "RevisionId": str,
    },
    total=False,
)

ClientCreateAliasRoutingConfigTypeDef = TypedDict(
    "ClientCreateAliasRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)

ClientCreateEventSourceMappingDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientCreateEventSourceMappingDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientCreateEventSourceMappingDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientCreateEventSourceMappingDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientCreateEventSourceMappingDestinationConfigTypeDef = TypedDict(
    "ClientCreateEventSourceMappingDestinationConfigTypeDef",
    {
        "OnSuccess": ClientCreateEventSourceMappingDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientCreateEventSourceMappingDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientCreateEventSourceMappingResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientCreateEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientCreateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientCreateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientCreateEventSourceMappingResponseDestinationConfigTypeDef = TypedDict(
    "ClientCreateEventSourceMappingResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientCreateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientCreateEventSourceMappingResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientCreateEventSourceMappingResponseTypeDef = TypedDict(
    "ClientCreateEventSourceMappingResponseTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": ClientCreateEventSourceMappingResponseDestinationConfigTypeDef,
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
    },
    total=False,
)

ClientCreateFunctionCodeTypeDef = TypedDict(
    "ClientCreateFunctionCodeTypeDef",
    {"ZipFile": bytes, "S3Bucket": str, "S3Key": str, "S3ObjectVersion": str},
    total=False,
)

ClientCreateFunctionDeadLetterConfigTypeDef = TypedDict(
    "ClientCreateFunctionDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

ClientCreateFunctionEnvironmentTypeDef = TypedDict(
    "ClientCreateFunctionEnvironmentTypeDef", {"Variables": Dict[str, str]}, total=False
)

ClientCreateFunctionResponseDeadLetterConfigTypeDef = TypedDict(
    "ClientCreateFunctionResponseDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

ClientCreateFunctionResponseEnvironmentErrorTypeDef = TypedDict(
    "ClientCreateFunctionResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ClientCreateFunctionResponseEnvironmentTypeDef = TypedDict(
    "ClientCreateFunctionResponseEnvironmentTypeDef",
    {"Variables": Dict[str, str], "Error": ClientCreateFunctionResponseEnvironmentErrorTypeDef},
    total=False,
)

ClientCreateFunctionResponseLayersTypeDef = TypedDict(
    "ClientCreateFunctionResponseLayersTypeDef", {"Arn": str, "CodeSize": int}, total=False
)

ClientCreateFunctionResponseTracingConfigTypeDef = TypedDict(
    "ClientCreateFunctionResponseTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ClientCreateFunctionResponseVpcConfigTypeDef = TypedDict(
    "ClientCreateFunctionResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

ClientCreateFunctionResponseTypeDef = TypedDict(
    "ClientCreateFunctionResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientCreateFunctionResponseVpcConfigTypeDef,
        "DeadLetterConfig": ClientCreateFunctionResponseDeadLetterConfigTypeDef,
        "Environment": ClientCreateFunctionResponseEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientCreateFunctionResponseTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientCreateFunctionResponseLayersTypeDef],
        "State": Literal["Pending", "Active", "Inactive", "Failed"],
        "StateReason": str,
        "StateReasonCode": Literal[
            "Idle",
            "Creating",
            "Restoring",
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
            "SubnetOutOfIPAddresses",
        ],
        "LastUpdateStatus": Literal["Successful", "Failed", "InProgress"],
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": Literal[
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
        ],
    },
    total=False,
)

ClientCreateFunctionTracingConfigTypeDef = TypedDict(
    "ClientCreateFunctionTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ClientCreateFunctionVpcConfigTypeDef = TypedDict(
    "ClientCreateFunctionVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientDeleteEventSourceMappingResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientDeleteEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientDeleteEventSourceMappingResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientDeleteEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientDeleteEventSourceMappingResponseDestinationConfigTypeDef = TypedDict(
    "ClientDeleteEventSourceMappingResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientDeleteEventSourceMappingResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientDeleteEventSourceMappingResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientDeleteEventSourceMappingResponseTypeDef = TypedDict(
    "ClientDeleteEventSourceMappingResponseTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": ClientDeleteEventSourceMappingResponseDestinationConfigTypeDef,
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
    },
    total=False,
)

ClientGetAccountSettingsResponseAccountLimitTypeDef = TypedDict(
    "ClientGetAccountSettingsResponseAccountLimitTypeDef",
    {
        "TotalCodeSize": int,
        "CodeSizeUnzipped": int,
        "CodeSizeZipped": int,
        "ConcurrentExecutions": int,
        "UnreservedConcurrentExecutions": int,
    },
    total=False,
)

ClientGetAccountSettingsResponseAccountUsageTypeDef = TypedDict(
    "ClientGetAccountSettingsResponseAccountUsageTypeDef",
    {"TotalCodeSize": int, "FunctionCount": int},
    total=False,
)

ClientGetAccountSettingsResponseTypeDef = TypedDict(
    "ClientGetAccountSettingsResponseTypeDef",
    {
        "AccountLimit": ClientGetAccountSettingsResponseAccountLimitTypeDef,
        "AccountUsage": ClientGetAccountSettingsResponseAccountUsageTypeDef,
    },
    total=False,
)

ClientGetAliasResponseRoutingConfigTypeDef = TypedDict(
    "ClientGetAliasResponseRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)

ClientGetAliasResponseTypeDef = TypedDict(
    "ClientGetAliasResponseTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": ClientGetAliasResponseRoutingConfigTypeDef,
        "RevisionId": str,
    },
    total=False,
)

ClientGetEventSourceMappingResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientGetEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientGetEventSourceMappingResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientGetEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientGetEventSourceMappingResponseDestinationConfigTypeDef = TypedDict(
    "ClientGetEventSourceMappingResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientGetEventSourceMappingResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientGetEventSourceMappingResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientGetEventSourceMappingResponseTypeDef = TypedDict(
    "ClientGetEventSourceMappingResponseTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": ClientGetEventSourceMappingResponseDestinationConfigTypeDef,
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
    },
    total=False,
)

ClientGetFunctionConcurrencyResponseTypeDef = TypedDict(
    "ClientGetFunctionConcurrencyResponseTypeDef",
    {"ReservedConcurrentExecutions": int},
    total=False,
)

ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef = TypedDict(
    "ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef = TypedDict(
    "ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ClientGetFunctionConfigurationResponseEnvironmentTypeDef = TypedDict(
    "ClientGetFunctionConfigurationResponseEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef,
    },
    total=False,
)

ClientGetFunctionConfigurationResponseLayersTypeDef = TypedDict(
    "ClientGetFunctionConfigurationResponseLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)

ClientGetFunctionConfigurationResponseTracingConfigTypeDef = TypedDict(
    "ClientGetFunctionConfigurationResponseTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ClientGetFunctionConfigurationResponseVpcConfigTypeDef = TypedDict(
    "ClientGetFunctionConfigurationResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

ClientGetFunctionConfigurationResponseTypeDef = TypedDict(
    "ClientGetFunctionConfigurationResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientGetFunctionConfigurationResponseVpcConfigTypeDef,
        "DeadLetterConfig": ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef,
        "Environment": ClientGetFunctionConfigurationResponseEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientGetFunctionConfigurationResponseTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientGetFunctionConfigurationResponseLayersTypeDef],
        "State": Literal["Pending", "Active", "Inactive", "Failed"],
        "StateReason": str,
        "StateReasonCode": Literal[
            "Idle",
            "Creating",
            "Restoring",
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
            "SubnetOutOfIPAddresses",
        ],
        "LastUpdateStatus": Literal["Successful", "Failed", "InProgress"],
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": Literal[
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
        ],
    },
    total=False,
)

ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientGetFunctionEventInvokeConfigResponseDestinationConfigTypeDef = TypedDict(
    "ClientGetFunctionEventInvokeConfigResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientGetFunctionEventInvokeConfigResponseTypeDef = TypedDict(
    "ClientGetFunctionEventInvokeConfigResponseTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": ClientGetFunctionEventInvokeConfigResponseDestinationConfigTypeDef,
    },
    total=False,
)

ClientGetFunctionResponseCodeTypeDef = TypedDict(
    "ClientGetFunctionResponseCodeTypeDef", {"RepositoryType": str, "Location": str}, total=False
)

ClientGetFunctionResponseConcurrencyTypeDef = TypedDict(
    "ClientGetFunctionResponseConcurrencyTypeDef",
    {"ReservedConcurrentExecutions": int},
    total=False,
)

ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef = TypedDict(
    "ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef = TypedDict(
    "ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ClientGetFunctionResponseConfigurationEnvironmentTypeDef = TypedDict(
    "ClientGetFunctionResponseConfigurationEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef,
    },
    total=False,
)

ClientGetFunctionResponseConfigurationLayersTypeDef = TypedDict(
    "ClientGetFunctionResponseConfigurationLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)

ClientGetFunctionResponseConfigurationTracingConfigTypeDef = TypedDict(
    "ClientGetFunctionResponseConfigurationTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ClientGetFunctionResponseConfigurationVpcConfigTypeDef = TypedDict(
    "ClientGetFunctionResponseConfigurationVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

ClientGetFunctionResponseConfigurationTypeDef = TypedDict(
    "ClientGetFunctionResponseConfigurationTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientGetFunctionResponseConfigurationVpcConfigTypeDef,
        "DeadLetterConfig": ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef,
        "Environment": ClientGetFunctionResponseConfigurationEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientGetFunctionResponseConfigurationTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientGetFunctionResponseConfigurationLayersTypeDef],
        "State": Literal["Pending", "Active", "Inactive", "Failed"],
        "StateReason": str,
        "StateReasonCode": Literal[
            "Idle",
            "Creating",
            "Restoring",
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
            "SubnetOutOfIPAddresses",
        ],
        "LastUpdateStatus": Literal["Successful", "Failed", "InProgress"],
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": Literal[
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
        ],
    },
    total=False,
)

ClientGetFunctionResponseTypeDef = TypedDict(
    "ClientGetFunctionResponseTypeDef",
    {
        "Configuration": ClientGetFunctionResponseConfigurationTypeDef,
        "Code": ClientGetFunctionResponseCodeTypeDef,
        "Tags": Dict[str, str],
        "Concurrency": ClientGetFunctionResponseConcurrencyTypeDef,
    },
    total=False,
)

ClientGetLayerVersionByArnResponseContentTypeDef = TypedDict(
    "ClientGetLayerVersionByArnResponseContentTypeDef",
    {"Location": str, "CodeSha256": str, "CodeSize": int},
    total=False,
)

ClientGetLayerVersionByArnResponseTypeDef = TypedDict(
    "ClientGetLayerVersionByArnResponseTypeDef",
    {
        "Content": ClientGetLayerVersionByArnResponseContentTypeDef,
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[
            Literal[
                "nodejs",
                "nodejs4.3",
                "nodejs6.10",
                "nodejs8.10",
                "nodejs10.x",
                "nodejs12.x",
                "java8",
                "java11",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "nodejs4.3-edge",
                "go1.x",
                "ruby2.5",
                "provided",
            ]
        ],
        "LicenseInfo": str,
    },
    total=False,
)

ClientGetLayerVersionPolicyResponseTypeDef = TypedDict(
    "ClientGetLayerVersionPolicyResponseTypeDef", {"Policy": str, "RevisionId": str}, total=False
)

ClientGetLayerVersionResponseContentTypeDef = TypedDict(
    "ClientGetLayerVersionResponseContentTypeDef",
    {"Location": str, "CodeSha256": str, "CodeSize": int},
    total=False,
)

ClientGetLayerVersionResponseTypeDef = TypedDict(
    "ClientGetLayerVersionResponseTypeDef",
    {
        "Content": ClientGetLayerVersionResponseContentTypeDef,
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[
            Literal[
                "nodejs",
                "nodejs4.3",
                "nodejs6.10",
                "nodejs8.10",
                "nodejs10.x",
                "nodejs12.x",
                "java8",
                "java11",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "nodejs4.3-edge",
                "go1.x",
                "ruby2.5",
                "provided",
            ]
        ],
        "LicenseInfo": str,
    },
    total=False,
)

ClientGetPolicyResponseTypeDef = TypedDict(
    "ClientGetPolicyResponseTypeDef", {"Policy": str, "RevisionId": str}, total=False
)

ClientGetProvisionedConcurrencyConfigResponseTypeDef = TypedDict(
    "ClientGetProvisionedConcurrencyConfigResponseTypeDef",
    {
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": Literal["IN_PROGRESS", "READY", "FAILED"],
        "StatusReason": str,
        "LastModified": str,
    },
    total=False,
)

ClientInvokeAsyncResponseTypeDef = TypedDict(
    "ClientInvokeAsyncResponseTypeDef", {"Status": int}, total=False
)

ClientInvokeResponseTypeDef = TypedDict(
    "ClientInvokeResponseTypeDef",
    {
        "StatusCode": int,
        "FunctionError": str,
        "LogResult": str,
        "Payload": StreamingBody,
        "ExecutedVersion": str,
    },
    total=False,
)

ClientListAliasesResponseAliasesRoutingConfigTypeDef = TypedDict(
    "ClientListAliasesResponseAliasesRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)

ClientListAliasesResponseAliasesTypeDef = TypedDict(
    "ClientListAliasesResponseAliasesTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": ClientListAliasesResponseAliasesRoutingConfigTypeDef,
        "RevisionId": str,
    },
    total=False,
)

ClientListAliasesResponseTypeDef = TypedDict(
    "ClientListAliasesResponseTypeDef",
    {"NextMarker": str, "Aliases": List[ClientListAliasesResponseAliasesTypeDef]},
    total=False,
)

ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigTypeDef = TypedDict(
    "ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigTypeDef",
    {
        "OnSuccess": ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef = TypedDict(
    "ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigTypeDef,
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
    },
    total=False,
)

ClientListEventSourceMappingsResponseTypeDef = TypedDict(
    "ClientListEventSourceMappingsResponseTypeDef",
    {
        "NextMarker": str,
        "EventSourceMappings": List[
            ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef
        ],
    },
    total=False,
)

ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigTypeDef = TypedDict(
    "ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigTypeDef",
    {
        "OnSuccess": ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsTypeDef = TypedDict(
    "ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigTypeDef,
    },
    total=False,
)

ClientListFunctionEventInvokeConfigsResponseTypeDef = TypedDict(
    "ClientListFunctionEventInvokeConfigsResponseTypeDef",
    {
        "FunctionEventInvokeConfigs": List[
            ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)

ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef = TypedDict(
    "ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef = TypedDict(
    "ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ClientListFunctionsResponseFunctionsEnvironmentTypeDef = TypedDict(
    "ClientListFunctionsResponseFunctionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef,
    },
    total=False,
)

ClientListFunctionsResponseFunctionsLayersTypeDef = TypedDict(
    "ClientListFunctionsResponseFunctionsLayersTypeDef", {"Arn": str, "CodeSize": int}, total=False
)

ClientListFunctionsResponseFunctionsTracingConfigTypeDef = TypedDict(
    "ClientListFunctionsResponseFunctionsTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ClientListFunctionsResponseFunctionsVpcConfigTypeDef = TypedDict(
    "ClientListFunctionsResponseFunctionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

ClientListFunctionsResponseFunctionsTypeDef = TypedDict(
    "ClientListFunctionsResponseFunctionsTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientListFunctionsResponseFunctionsVpcConfigTypeDef,
        "DeadLetterConfig": ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef,
        "Environment": ClientListFunctionsResponseFunctionsEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientListFunctionsResponseFunctionsTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientListFunctionsResponseFunctionsLayersTypeDef],
        "State": Literal["Pending", "Active", "Inactive", "Failed"],
        "StateReason": str,
        "StateReasonCode": Literal[
            "Idle",
            "Creating",
            "Restoring",
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
            "SubnetOutOfIPAddresses",
        ],
        "LastUpdateStatus": Literal["Successful", "Failed", "InProgress"],
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": Literal[
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
        ],
    },
    total=False,
)

ClientListFunctionsResponseTypeDef = TypedDict(
    "ClientListFunctionsResponseTypeDef",
    {"NextMarker": str, "Functions": List[ClientListFunctionsResponseFunctionsTypeDef]},
    total=False,
)

ClientListLayerVersionsResponseLayerVersionsTypeDef = TypedDict(
    "ClientListLayerVersionsResponseLayerVersionsTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[
            Literal[
                "nodejs",
                "nodejs4.3",
                "nodejs6.10",
                "nodejs8.10",
                "nodejs10.x",
                "nodejs12.x",
                "java8",
                "java11",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "nodejs4.3-edge",
                "go1.x",
                "ruby2.5",
                "provided",
            ]
        ],
        "LicenseInfo": str,
    },
    total=False,
)

ClientListLayerVersionsResponseTypeDef = TypedDict(
    "ClientListLayerVersionsResponseTypeDef",
    {"NextMarker": str, "LayerVersions": List[ClientListLayerVersionsResponseLayerVersionsTypeDef]},
    total=False,
)

ClientListLayersResponseLayersLatestMatchingVersionTypeDef = TypedDict(
    "ClientListLayersResponseLayersLatestMatchingVersionTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[
            Literal[
                "nodejs",
                "nodejs4.3",
                "nodejs6.10",
                "nodejs8.10",
                "nodejs10.x",
                "nodejs12.x",
                "java8",
                "java11",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "nodejs4.3-edge",
                "go1.x",
                "ruby2.5",
                "provided",
            ]
        ],
        "LicenseInfo": str,
    },
    total=False,
)

ClientListLayersResponseLayersTypeDef = TypedDict(
    "ClientListLayersResponseLayersTypeDef",
    {
        "LayerName": str,
        "LayerArn": str,
        "LatestMatchingVersion": ClientListLayersResponseLayersLatestMatchingVersionTypeDef,
    },
    total=False,
)

ClientListLayersResponseTypeDef = TypedDict(
    "ClientListLayersResponseTypeDef",
    {"NextMarker": str, "Layers": List[ClientListLayersResponseLayersTypeDef]},
    total=False,
)

ClientListProvisionedConcurrencyConfigsResponseProvisionedConcurrencyConfigsTypeDef = TypedDict(
    "ClientListProvisionedConcurrencyConfigsResponseProvisionedConcurrencyConfigsTypeDef",
    {
        "FunctionArn": str,
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": Literal["IN_PROGRESS", "READY", "FAILED"],
        "StatusReason": str,
        "LastModified": str,
    },
    total=False,
)

ClientListProvisionedConcurrencyConfigsResponseTypeDef = TypedDict(
    "ClientListProvisionedConcurrencyConfigsResponseTypeDef",
    {
        "ProvisionedConcurrencyConfigs": List[
            ClientListProvisionedConcurrencyConfigsResponseProvisionedConcurrencyConfigsTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef = TypedDict(
    "ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)

ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef = TypedDict(
    "ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef = TypedDict(
    "ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef,
    },
    total=False,
)

ClientListVersionsByFunctionResponseVersionsLayersTypeDef = TypedDict(
    "ClientListVersionsByFunctionResponseVersionsLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)

ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef = TypedDict(
    "ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef = TypedDict(
    "ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

ClientListVersionsByFunctionResponseVersionsTypeDef = TypedDict(
    "ClientListVersionsByFunctionResponseVersionsTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef,
        "DeadLetterConfig": ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef,
        "Environment": ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientListVersionsByFunctionResponseVersionsLayersTypeDef],
        "State": Literal["Pending", "Active", "Inactive", "Failed"],
        "StateReason": str,
        "StateReasonCode": Literal[
            "Idle",
            "Creating",
            "Restoring",
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
            "SubnetOutOfIPAddresses",
        ],
        "LastUpdateStatus": Literal["Successful", "Failed", "InProgress"],
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": Literal[
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
        ],
    },
    total=False,
)

ClientListVersionsByFunctionResponseTypeDef = TypedDict(
    "ClientListVersionsByFunctionResponseTypeDef",
    {"NextMarker": str, "Versions": List[ClientListVersionsByFunctionResponseVersionsTypeDef]},
    total=False,
)

ClientPublishLayerVersionContentTypeDef = TypedDict(
    "ClientPublishLayerVersionContentTypeDef",
    {"S3Bucket": str, "S3Key": str, "S3ObjectVersion": str, "ZipFile": bytes},
    total=False,
)

ClientPublishLayerVersionResponseContentTypeDef = TypedDict(
    "ClientPublishLayerVersionResponseContentTypeDef",
    {"Location": str, "CodeSha256": str, "CodeSize": int},
    total=False,
)

ClientPublishLayerVersionResponseTypeDef = TypedDict(
    "ClientPublishLayerVersionResponseTypeDef",
    {
        "Content": ClientPublishLayerVersionResponseContentTypeDef,
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[
            Literal[
                "nodejs",
                "nodejs4.3",
                "nodejs6.10",
                "nodejs8.10",
                "nodejs10.x",
                "nodejs12.x",
                "java8",
                "java11",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "nodejs4.3-edge",
                "go1.x",
                "ruby2.5",
                "provided",
            ]
        ],
        "LicenseInfo": str,
    },
    total=False,
)

ClientPublishVersionResponseDeadLetterConfigTypeDef = TypedDict(
    "ClientPublishVersionResponseDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

ClientPublishVersionResponseEnvironmentErrorTypeDef = TypedDict(
    "ClientPublishVersionResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ClientPublishVersionResponseEnvironmentTypeDef = TypedDict(
    "ClientPublishVersionResponseEnvironmentTypeDef",
    {"Variables": Dict[str, str], "Error": ClientPublishVersionResponseEnvironmentErrorTypeDef},
    total=False,
)

ClientPublishVersionResponseLayersTypeDef = TypedDict(
    "ClientPublishVersionResponseLayersTypeDef", {"Arn": str, "CodeSize": int}, total=False
)

ClientPublishVersionResponseTracingConfigTypeDef = TypedDict(
    "ClientPublishVersionResponseTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ClientPublishVersionResponseVpcConfigTypeDef = TypedDict(
    "ClientPublishVersionResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

ClientPublishVersionResponseTypeDef = TypedDict(
    "ClientPublishVersionResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientPublishVersionResponseVpcConfigTypeDef,
        "DeadLetterConfig": ClientPublishVersionResponseDeadLetterConfigTypeDef,
        "Environment": ClientPublishVersionResponseEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientPublishVersionResponseTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientPublishVersionResponseLayersTypeDef],
        "State": Literal["Pending", "Active", "Inactive", "Failed"],
        "StateReason": str,
        "StateReasonCode": Literal[
            "Idle",
            "Creating",
            "Restoring",
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
            "SubnetOutOfIPAddresses",
        ],
        "LastUpdateStatus": Literal["Successful", "Failed", "InProgress"],
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": Literal[
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
        ],
    },
    total=False,
)

ClientPutFunctionConcurrencyResponseTypeDef = TypedDict(
    "ClientPutFunctionConcurrencyResponseTypeDef",
    {"ReservedConcurrentExecutions": int},
    total=False,
)

ClientPutFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientPutFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientPutFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientPutFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientPutFunctionEventInvokeConfigDestinationConfigTypeDef = TypedDict(
    "ClientPutFunctionEventInvokeConfigDestinationConfigTypeDef",
    {
        "OnSuccess": ClientPutFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientPutFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientPutFunctionEventInvokeConfigResponseDestinationConfigTypeDef = TypedDict(
    "ClientPutFunctionEventInvokeConfigResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientPutFunctionEventInvokeConfigResponseTypeDef = TypedDict(
    "ClientPutFunctionEventInvokeConfigResponseTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": ClientPutFunctionEventInvokeConfigResponseDestinationConfigTypeDef,
    },
    total=False,
)

ClientPutProvisionedConcurrencyConfigResponseTypeDef = TypedDict(
    "ClientPutProvisionedConcurrencyConfigResponseTypeDef",
    {
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": Literal["IN_PROGRESS", "READY", "FAILED"],
        "StatusReason": str,
        "LastModified": str,
    },
    total=False,
)

ClientUpdateAliasResponseRoutingConfigTypeDef = TypedDict(
    "ClientUpdateAliasResponseRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)

ClientUpdateAliasResponseTypeDef = TypedDict(
    "ClientUpdateAliasResponseTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": ClientUpdateAliasResponseRoutingConfigTypeDef,
        "RevisionId": str,
    },
    total=False,
)

ClientUpdateAliasRoutingConfigTypeDef = TypedDict(
    "ClientUpdateAliasRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)

ClientUpdateEventSourceMappingDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientUpdateEventSourceMappingDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientUpdateEventSourceMappingDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientUpdateEventSourceMappingDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientUpdateEventSourceMappingDestinationConfigTypeDef = TypedDict(
    "ClientUpdateEventSourceMappingDestinationConfigTypeDef",
    {
        "OnSuccess": ClientUpdateEventSourceMappingDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientUpdateEventSourceMappingDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientUpdateEventSourceMappingResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientUpdateEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientUpdateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientUpdateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientUpdateEventSourceMappingResponseDestinationConfigTypeDef = TypedDict(
    "ClientUpdateEventSourceMappingResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientUpdateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientUpdateEventSourceMappingResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientUpdateEventSourceMappingResponseTypeDef = TypedDict(
    "ClientUpdateEventSourceMappingResponseTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": ClientUpdateEventSourceMappingResponseDestinationConfigTypeDef,
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
    },
    total=False,
)

ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef = TypedDict(
    "ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef = TypedDict(
    "ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ClientUpdateFunctionCodeResponseEnvironmentTypeDef = TypedDict(
    "ClientUpdateFunctionCodeResponseEnvironmentTypeDef",
    {"Variables": Dict[str, str], "Error": ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef},
    total=False,
)

ClientUpdateFunctionCodeResponseLayersTypeDef = TypedDict(
    "ClientUpdateFunctionCodeResponseLayersTypeDef", {"Arn": str, "CodeSize": int}, total=False
)

ClientUpdateFunctionCodeResponseTracingConfigTypeDef = TypedDict(
    "ClientUpdateFunctionCodeResponseTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ClientUpdateFunctionCodeResponseVpcConfigTypeDef = TypedDict(
    "ClientUpdateFunctionCodeResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

ClientUpdateFunctionCodeResponseTypeDef = TypedDict(
    "ClientUpdateFunctionCodeResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientUpdateFunctionCodeResponseVpcConfigTypeDef,
        "DeadLetterConfig": ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef,
        "Environment": ClientUpdateFunctionCodeResponseEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientUpdateFunctionCodeResponseTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientUpdateFunctionCodeResponseLayersTypeDef],
        "State": Literal["Pending", "Active", "Inactive", "Failed"],
        "StateReason": str,
        "StateReasonCode": Literal[
            "Idle",
            "Creating",
            "Restoring",
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
            "SubnetOutOfIPAddresses",
        ],
        "LastUpdateStatus": Literal["Successful", "Failed", "InProgress"],
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": Literal[
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
        ],
    },
    total=False,
)

ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

ClientUpdateFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationEnvironmentTypeDef",
    {"Variables": Dict[str, str]},
    total=False,
)

ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)

ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef,
    },
    total=False,
)

ClientUpdateFunctionConfigurationResponseLayersTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationResponseLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)

ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

ClientUpdateFunctionConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationResponseTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef,
        "DeadLetterConfig": ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef,
        "Environment": ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ClientUpdateFunctionConfigurationResponseLayersTypeDef],
        "State": Literal["Pending", "Active", "Inactive", "Failed"],
        "StateReason": str,
        "StateReasonCode": Literal[
            "Idle",
            "Creating",
            "Restoring",
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
            "SubnetOutOfIPAddresses",
        ],
        "LastUpdateStatus": Literal["Successful", "Failed", "InProgress"],
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": Literal[
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
        ],
    },
    total=False,
)

ClientUpdateFunctionConfigurationTracingConfigTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ClientUpdateFunctionConfigurationVpcConfigTypeDef = TypedDict(
    "ClientUpdateFunctionConfigurationVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)

ClientUpdateFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientUpdateFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientUpdateFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientUpdateFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientUpdateFunctionEventInvokeConfigDestinationConfigTypeDef = TypedDict(
    "ClientUpdateFunctionEventInvokeConfigDestinationConfigTypeDef",
    {
        "OnSuccess": ClientUpdateFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientUpdateFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigTypeDef = TypedDict(
    "ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ClientUpdateFunctionEventInvokeConfigResponseTypeDef = TypedDict(
    "ClientUpdateFunctionEventInvokeConfigResponseTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigTypeDef,
    },
    total=False,
)

FunctionActiveWaitWaiterConfigTypeDef = TypedDict(
    "FunctionActiveWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

FunctionExistsWaitWaiterConfigTypeDef = TypedDict(
    "FunctionExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

FunctionUpdatedWaitWaiterConfigTypeDef = TypedDict(
    "FunctionUpdatedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListAliasesPaginateResponseAliasesRoutingConfigTypeDef = TypedDict(
    "ListAliasesPaginateResponseAliasesRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)

ListAliasesPaginateResponseAliasesTypeDef = TypedDict(
    "ListAliasesPaginateResponseAliasesTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": ListAliasesPaginateResponseAliasesRoutingConfigTypeDef,
        "RevisionId": str,
    },
    total=False,
)

ListAliasesPaginateResponseTypeDef = TypedDict(
    "ListAliasesPaginateResponseTypeDef",
    {"Aliases": List[ListAliasesPaginateResponseAliasesTypeDef], "NextToken": str},
    total=False,
)

ListEventSourceMappingsPaginatePaginationConfigTypeDef = TypedDict(
    "ListEventSourceMappingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnFailureTypeDef = TypedDict(
    "ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef = TypedDict(
    "ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigTypeDef = TypedDict(
    "ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigTypeDef",
    {
        "OnSuccess": ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef,
        "OnFailure": ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef = TypedDict(
    "ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef",
    {
        "UUID": str,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigTypeDef,
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
    },
    total=False,
)

ListEventSourceMappingsPaginateResponseTypeDef = TypedDict(
    "ListEventSourceMappingsPaginateResponseTypeDef",
    {
        "EventSourceMappings": List[
            ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListFunctionEventInvokeConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)

ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)

ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigTypeDef",
    {
        "OnSuccess": ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef,
        "OnFailure": ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef,
    },
    total=False,
)

ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigTypeDef,
    },
    total=False,
)

ListFunctionEventInvokeConfigsPaginateResponseTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsPaginateResponseTypeDef",
    {
        "FunctionEventInvokeConfigs": List[
            ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListFunctionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListFunctionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef = TypedDict(
    "ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)

ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef = TypedDict(
    "ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef = TypedDict(
    "ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef,
    },
    total=False,
)

ListFunctionsPaginateResponseFunctionsLayersTypeDef = TypedDict(
    "ListFunctionsPaginateResponseFunctionsLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)

ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef = TypedDict(
    "ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef = TypedDict(
    "ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

ListFunctionsPaginateResponseFunctionsTypeDef = TypedDict(
    "ListFunctionsPaginateResponseFunctionsTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef,
        "DeadLetterConfig": ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef,
        "Environment": ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ListFunctionsPaginateResponseFunctionsLayersTypeDef],
        "State": Literal["Pending", "Active", "Inactive", "Failed"],
        "StateReason": str,
        "StateReasonCode": Literal[
            "Idle",
            "Creating",
            "Restoring",
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
            "SubnetOutOfIPAddresses",
        ],
        "LastUpdateStatus": Literal["Successful", "Failed", "InProgress"],
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": Literal[
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
        ],
    },
    total=False,
)

ListFunctionsPaginateResponseTypeDef = TypedDict(
    "ListFunctionsPaginateResponseTypeDef",
    {"Functions": List[ListFunctionsPaginateResponseFunctionsTypeDef], "NextToken": str},
    total=False,
)

ListLayerVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListLayerVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListLayerVersionsPaginateResponseLayerVersionsTypeDef = TypedDict(
    "ListLayerVersionsPaginateResponseLayerVersionsTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[
            Literal[
                "nodejs",
                "nodejs4.3",
                "nodejs6.10",
                "nodejs8.10",
                "nodejs10.x",
                "nodejs12.x",
                "java8",
                "java11",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "nodejs4.3-edge",
                "go1.x",
                "ruby2.5",
                "provided",
            ]
        ],
        "LicenseInfo": str,
    },
    total=False,
)

ListLayerVersionsPaginateResponseTypeDef = TypedDict(
    "ListLayerVersionsPaginateResponseTypeDef",
    {
        "LayerVersions": List[ListLayerVersionsPaginateResponseLayerVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListLayersPaginatePaginationConfigTypeDef = TypedDict(
    "ListLayersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef = TypedDict(
    "ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[
            Literal[
                "nodejs",
                "nodejs4.3",
                "nodejs6.10",
                "nodejs8.10",
                "nodejs10.x",
                "nodejs12.x",
                "java8",
                "java11",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "nodejs4.3-edge",
                "go1.x",
                "ruby2.5",
                "provided",
            ]
        ],
        "LicenseInfo": str,
    },
    total=False,
)

ListLayersPaginateResponseLayersTypeDef = TypedDict(
    "ListLayersPaginateResponseLayersTypeDef",
    {
        "LayerName": str,
        "LayerArn": str,
        "LatestMatchingVersion": ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef,
    },
    total=False,
)

ListLayersPaginateResponseTypeDef = TypedDict(
    "ListLayersPaginateResponseTypeDef",
    {"Layers": List[ListLayersPaginateResponseLayersTypeDef], "NextToken": str},
    total=False,
)

ListProvisionedConcurrencyConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "ListProvisionedConcurrencyConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListProvisionedConcurrencyConfigsPaginateResponseProvisionedConcurrencyConfigsTypeDef = TypedDict(
    "ListProvisionedConcurrencyConfigsPaginateResponseProvisionedConcurrencyConfigsTypeDef",
    {
        "FunctionArn": str,
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": Literal["IN_PROGRESS", "READY", "FAILED"],
        "StatusReason": str,
        "LastModified": str,
    },
    total=False,
)

ListProvisionedConcurrencyConfigsPaginateResponseTypeDef = TypedDict(
    "ListProvisionedConcurrencyConfigsPaginateResponseTypeDef",
    {
        "ProvisionedConcurrencyConfigs": List[
            ListProvisionedConcurrencyConfigsPaginateResponseProvisionedConcurrencyConfigsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ListVersionsByFunctionPaginatePaginationConfigTypeDef = TypedDict(
    "ListVersionsByFunctionPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef = TypedDict(
    "ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)

ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef = TypedDict(
    "ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)

ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef = TypedDict(
    "ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef,
    },
    total=False,
)

ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef = TypedDict(
    "ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)

ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef = TypedDict(
    "ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)

ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef = TypedDict(
    "ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

ListVersionsByFunctionPaginateResponseVersionsTypeDef = TypedDict(
    "ListVersionsByFunctionPaginateResponseVersionsTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef,
        "DeadLetterConfig": ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef,
        "Environment": ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef,
        "KMSKeyArn": str,
        "TracingConfig": ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef,
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List[ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef],
        "State": Literal["Pending", "Active", "Inactive", "Failed"],
        "StateReason": str,
        "StateReasonCode": Literal[
            "Idle",
            "Creating",
            "Restoring",
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
            "SubnetOutOfIPAddresses",
        ],
        "LastUpdateStatus": Literal["Successful", "Failed", "InProgress"],
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": Literal[
            "EniLimitExceeded",
            "InsufficientRolePermissions",
            "InvalidConfiguration",
            "InternalError",
        ],
    },
    total=False,
)

ListVersionsByFunctionPaginateResponseTypeDef = TypedDict(
    "ListVersionsByFunctionPaginateResponseTypeDef",
    {"Versions": List[ListVersionsByFunctionPaginateResponseVersionsTypeDef], "NextToken": str},
    total=False,
)
