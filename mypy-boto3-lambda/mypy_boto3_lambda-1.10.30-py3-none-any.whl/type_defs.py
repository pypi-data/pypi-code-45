"Main interface for lambda service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from botocore.response import StreamingBody
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddLayerVersionPermissionResponseTypeDef",
    "ClientAddPermissionResponseTypeDef",
    "ClientCreateAliasResponseRoutingConfigTypeDef",
    "ClientCreateAliasResponseTypeDef",
    "ClientCreateAliasRoutingConfigTypeDef",
    "ClientCreateEventSourceMappingDestinationConfigOnFailureTypeDef",
    "ClientCreateEventSourceMappingDestinationConfigOnSuccessTypeDef",
    "ClientCreateEventSourceMappingDestinationConfigTypeDef",
    "ClientCreateEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    "ClientCreateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    "ClientCreateEventSourceMappingResponseDestinationConfigTypeDef",
    "ClientCreateEventSourceMappingResponseTypeDef",
    "ClientCreateFunctionCodeTypeDef",
    "ClientCreateFunctionDeadLetterConfigTypeDef",
    "ClientCreateFunctionEnvironmentTypeDef",
    "ClientCreateFunctionResponseDeadLetterConfigTypeDef",
    "ClientCreateFunctionResponseEnvironmentErrorTypeDef",
    "ClientCreateFunctionResponseEnvironmentTypeDef",
    "ClientCreateFunctionResponseLayersTypeDef",
    "ClientCreateFunctionResponseTracingConfigTypeDef",
    "ClientCreateFunctionResponseVpcConfigTypeDef",
    "ClientCreateFunctionResponseTypeDef",
    "ClientCreateFunctionTracingConfigTypeDef",
    "ClientCreateFunctionVpcConfigTypeDef",
    "ClientDeleteEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    "ClientDeleteEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    "ClientDeleteEventSourceMappingResponseDestinationConfigTypeDef",
    "ClientDeleteEventSourceMappingResponseTypeDef",
    "ClientGetAccountSettingsResponseAccountLimitTypeDef",
    "ClientGetAccountSettingsResponseAccountUsageTypeDef",
    "ClientGetAccountSettingsResponseTypeDef",
    "ClientGetAliasResponseRoutingConfigTypeDef",
    "ClientGetAliasResponseTypeDef",
    "ClientGetEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    "ClientGetEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    "ClientGetEventSourceMappingResponseDestinationConfigTypeDef",
    "ClientGetEventSourceMappingResponseTypeDef",
    "ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef",
    "ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef",
    "ClientGetFunctionConfigurationResponseEnvironmentTypeDef",
    "ClientGetFunctionConfigurationResponseLayersTypeDef",
    "ClientGetFunctionConfigurationResponseTracingConfigTypeDef",
    "ClientGetFunctionConfigurationResponseVpcConfigTypeDef",
    "ClientGetFunctionConfigurationResponseTypeDef",
    "ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef",
    "ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef",
    "ClientGetFunctionEventInvokeConfigResponseDestinationConfigTypeDef",
    "ClientGetFunctionEventInvokeConfigResponseTypeDef",
    "ClientGetFunctionResponseCodeTypeDef",
    "ClientGetFunctionResponseConcurrencyTypeDef",
    "ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef",
    "ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef",
    "ClientGetFunctionResponseConfigurationEnvironmentTypeDef",
    "ClientGetFunctionResponseConfigurationLayersTypeDef",
    "ClientGetFunctionResponseConfigurationTracingConfigTypeDef",
    "ClientGetFunctionResponseConfigurationVpcConfigTypeDef",
    "ClientGetFunctionResponseConfigurationTypeDef",
    "ClientGetFunctionResponseTypeDef",
    "ClientGetLayerVersionByArnResponseContentTypeDef",
    "ClientGetLayerVersionByArnResponseTypeDef",
    "ClientGetLayerVersionPolicyResponseTypeDef",
    "ClientGetLayerVersionResponseContentTypeDef",
    "ClientGetLayerVersionResponseTypeDef",
    "ClientGetPolicyResponseTypeDef",
    "ClientInvokeAsyncResponseTypeDef",
    "ClientInvokeResponseTypeDef",
    "ClientListAliasesResponseAliasesRoutingConfigTypeDef",
    "ClientListAliasesResponseAliasesTypeDef",
    "ClientListAliasesResponseTypeDef",
    "ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnFailureTypeDef",
    "ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef",
    "ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigTypeDef",
    "ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef",
    "ClientListEventSourceMappingsResponseTypeDef",
    "ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef",
    "ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef",
    "ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigTypeDef",
    "ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsTypeDef",
    "ClientListFunctionEventInvokeConfigsResponseTypeDef",
    "ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef",
    "ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef",
    "ClientListFunctionsResponseFunctionsEnvironmentTypeDef",
    "ClientListFunctionsResponseFunctionsLayersTypeDef",
    "ClientListFunctionsResponseFunctionsTracingConfigTypeDef",
    "ClientListFunctionsResponseFunctionsVpcConfigTypeDef",
    "ClientListFunctionsResponseFunctionsTypeDef",
    "ClientListFunctionsResponseTypeDef",
    "ClientListLayerVersionsResponseLayerVersionsTypeDef",
    "ClientListLayerVersionsResponseTypeDef",
    "ClientListLayersResponseLayersLatestMatchingVersionTypeDef",
    "ClientListLayersResponseLayersTypeDef",
    "ClientListLayersResponseTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef",
    "ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef",
    "ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef",
    "ClientListVersionsByFunctionResponseVersionsLayersTypeDef",
    "ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef",
    "ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef",
    "ClientListVersionsByFunctionResponseVersionsTypeDef",
    "ClientListVersionsByFunctionResponseTypeDef",
    "ClientPublishLayerVersionContentTypeDef",
    "ClientPublishLayerVersionResponseContentTypeDef",
    "ClientPublishLayerVersionResponseTypeDef",
    "ClientPublishVersionResponseDeadLetterConfigTypeDef",
    "ClientPublishVersionResponseEnvironmentErrorTypeDef",
    "ClientPublishVersionResponseEnvironmentTypeDef",
    "ClientPublishVersionResponseLayersTypeDef",
    "ClientPublishVersionResponseTracingConfigTypeDef",
    "ClientPublishVersionResponseVpcConfigTypeDef",
    "ClientPublishVersionResponseTypeDef",
    "ClientPutFunctionConcurrencyResponseTypeDef",
    "ClientPutFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef",
    "ClientPutFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef",
    "ClientPutFunctionEventInvokeConfigDestinationConfigTypeDef",
    "ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef",
    "ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef",
    "ClientPutFunctionEventInvokeConfigResponseDestinationConfigTypeDef",
    "ClientPutFunctionEventInvokeConfigResponseTypeDef",
    "ClientUpdateAliasResponseRoutingConfigTypeDef",
    "ClientUpdateAliasResponseTypeDef",
    "ClientUpdateAliasRoutingConfigTypeDef",
    "ClientUpdateEventSourceMappingDestinationConfigOnFailureTypeDef",
    "ClientUpdateEventSourceMappingDestinationConfigOnSuccessTypeDef",
    "ClientUpdateEventSourceMappingDestinationConfigTypeDef",
    "ClientUpdateEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    "ClientUpdateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    "ClientUpdateEventSourceMappingResponseDestinationConfigTypeDef",
    "ClientUpdateEventSourceMappingResponseTypeDef",
    "ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef",
    "ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef",
    "ClientUpdateFunctionCodeResponseEnvironmentTypeDef",
    "ClientUpdateFunctionCodeResponseLayersTypeDef",
    "ClientUpdateFunctionCodeResponseTracingConfigTypeDef",
    "ClientUpdateFunctionCodeResponseVpcConfigTypeDef",
    "ClientUpdateFunctionCodeResponseTypeDef",
    "ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef",
    "ClientUpdateFunctionConfigurationEnvironmentTypeDef",
    "ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef",
    "ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef",
    "ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef",
    "ClientUpdateFunctionConfigurationResponseLayersTypeDef",
    "ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef",
    "ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef",
    "ClientUpdateFunctionConfigurationResponseTypeDef",
    "ClientUpdateFunctionConfigurationTracingConfigTypeDef",
    "ClientUpdateFunctionConfigurationVpcConfigTypeDef",
    "ClientUpdateFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef",
    "ClientUpdateFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef",
    "ClientUpdateFunctionEventInvokeConfigDestinationConfigTypeDef",
    "ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef",
    "ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef",
    "ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigTypeDef",
    "ClientUpdateFunctionEventInvokeConfigResponseTypeDef",
    "FunctionActiveWaitWaiterConfigTypeDef",
    "FunctionExistsWaitWaiterConfigTypeDef",
    "FunctionUpdatedWaitWaiterConfigTypeDef",
    "ListAliasesPaginatePaginationConfigTypeDef",
    "ListAliasesPaginateResponseAliasesRoutingConfigTypeDef",
    "ListAliasesPaginateResponseAliasesTypeDef",
    "ListAliasesPaginateResponseTypeDef",
    "ListEventSourceMappingsPaginatePaginationConfigTypeDef",
    "ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnFailureTypeDef",
    "ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef",
    "ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigTypeDef",
    "ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef",
    "ListEventSourceMappingsPaginateResponseTypeDef",
    "ListFunctionEventInvokeConfigsPaginatePaginationConfigTypeDef",
    "ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef",
    "ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef",
    "ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigTypeDef",
    "ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsTypeDef",
    "ListFunctionEventInvokeConfigsPaginateResponseTypeDef",
    "ListFunctionsPaginatePaginationConfigTypeDef",
    "ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef",
    "ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef",
    "ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef",
    "ListFunctionsPaginateResponseFunctionsLayersTypeDef",
    "ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef",
    "ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef",
    "ListFunctionsPaginateResponseFunctionsTypeDef",
    "ListFunctionsPaginateResponseTypeDef",
    "ListLayerVersionsPaginatePaginationConfigTypeDef",
    "ListLayerVersionsPaginateResponseLayerVersionsTypeDef",
    "ListLayerVersionsPaginateResponseTypeDef",
    "ListLayersPaginatePaginationConfigTypeDef",
    "ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef",
    "ListLayersPaginateResponseLayersTypeDef",
    "ListLayersPaginateResponseTypeDef",
    "ListVersionsByFunctionPaginatePaginationConfigTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef",
    "ListVersionsByFunctionPaginateResponseVersionsTypeDef",
    "ListVersionsByFunctionPaginateResponseTypeDef",
)


_ClientAddLayerVersionPermissionResponseTypeDef = TypedDict(
    "_ClientAddLayerVersionPermissionResponseTypeDef",
    {"Statement": str, "RevisionId": str},
    total=False,
)


class ClientAddLayerVersionPermissionResponseTypeDef(
    _ClientAddLayerVersionPermissionResponseTypeDef
):
    """
    - *(dict) --*

      - **Statement** *(string) --*

        The permission statement.
    """


_ClientAddPermissionResponseTypeDef = TypedDict(
    "_ClientAddPermissionResponseTypeDef", {"Statement": str}, total=False
)


class ClientAddPermissionResponseTypeDef(_ClientAddPermissionResponseTypeDef):
    """
    - *(dict) --*

      - **Statement** *(string) --*

        The permission statement that's added to the function policy.
    """


_ClientCreateAliasResponseRoutingConfigTypeDef = TypedDict(
    "_ClientCreateAliasResponseRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientCreateAliasResponseRoutingConfigTypeDef(_ClientCreateAliasResponseRoutingConfigTypeDef):
    pass


_ClientCreateAliasResponseTypeDef = TypedDict(
    "_ClientCreateAliasResponseTypeDef",
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


class ClientCreateAliasResponseTypeDef(_ClientCreateAliasResponseTypeDef):
    """
    - *(dict) --*

      Provides configuration information about a Lambda function `alias
      <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .
      - **AliasArn** *(string) --*

        The Amazon Resource Name (ARN) of the alias.
    """


_ClientCreateAliasRoutingConfigTypeDef = TypedDict(
    "_ClientCreateAliasRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientCreateAliasRoutingConfigTypeDef(_ClientCreateAliasRoutingConfigTypeDef):
    """
    The `routing configuration
    <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__ of
    the alias.
    - **AdditionalVersionWeights** *(dict) --*

      The name of the second alias, and the percentage of traffic that's routed to it.
      - *(string) --*

        - *(float) --*
    """


_ClientCreateEventSourceMappingDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientCreateEventSourceMappingDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientCreateEventSourceMappingDestinationConfigOnFailureTypeDef(
    _ClientCreateEventSourceMappingDestinationConfigOnFailureTypeDef
):
    pass


_ClientCreateEventSourceMappingDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientCreateEventSourceMappingDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientCreateEventSourceMappingDestinationConfigOnSuccessTypeDef(
    _ClientCreateEventSourceMappingDestinationConfigOnSuccessTypeDef
):
    """
    - **OnSuccess** *(dict) --*

      The destination configuration for successful invocations.
      - **Destination** *(string) --*

        The Amazon Resource Name (ARN) of the destination resource.
    """


_ClientCreateEventSourceMappingDestinationConfigTypeDef = TypedDict(
    "_ClientCreateEventSourceMappingDestinationConfigTypeDef",
    {
        "OnSuccess": ClientCreateEventSourceMappingDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientCreateEventSourceMappingDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientCreateEventSourceMappingDestinationConfigTypeDef(
    _ClientCreateEventSourceMappingDestinationConfigTypeDef
):
    """
    (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.
    - **OnSuccess** *(dict) --*

      The destination configuration for successful invocations.
      - **Destination** *(string) --*

        The Amazon Resource Name (ARN) of the destination resource.
    """


_ClientCreateEventSourceMappingResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientCreateEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientCreateEventSourceMappingResponseDestinationConfigOnFailureTypeDef(
    _ClientCreateEventSourceMappingResponseDestinationConfigOnFailureTypeDef
):
    pass


_ClientCreateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientCreateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientCreateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef(
    _ClientCreateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef
):
    pass


_ClientCreateEventSourceMappingResponseDestinationConfigTypeDef = TypedDict(
    "_ClientCreateEventSourceMappingResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientCreateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientCreateEventSourceMappingResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientCreateEventSourceMappingResponseDestinationConfigTypeDef(
    _ClientCreateEventSourceMappingResponseDestinationConfigTypeDef
):
    pass


_ClientCreateEventSourceMappingResponseTypeDef = TypedDict(
    "_ClientCreateEventSourceMappingResponseTypeDef",
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


class ClientCreateEventSourceMappingResponseTypeDef(_ClientCreateEventSourceMappingResponseTypeDef):
    """
    - *(dict) --*

      A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping
      for details.
      - **UUID** *(string) --*

        The identifier of the event source mapping.
    """


_ClientCreateFunctionCodeTypeDef = TypedDict(
    "_ClientCreateFunctionCodeTypeDef",
    {"ZipFile": bytes, "S3Bucket": str, "S3Key": str, "S3ObjectVersion": str},
    total=False,
)


class ClientCreateFunctionCodeTypeDef(_ClientCreateFunctionCodeTypeDef):
    """
    The code for the function.
    - **ZipFile** *(bytes) --*

      The base64-encoded contents of the deployment package. AWS SDK and AWS CLI clients handle the
      encoding for you.
    """


_ClientCreateFunctionDeadLetterConfigTypeDef = TypedDict(
    "_ClientCreateFunctionDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)


class ClientCreateFunctionDeadLetterConfigTypeDef(_ClientCreateFunctionDeadLetterConfigTypeDef):
    """
    A dead letter queue configuration that specifies the queue or topic where Lambda sends
    asynchronous events when they fail processing. For more information, see `Dead Letter Queues
    <https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#dlq>`__ .
    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientCreateFunctionEnvironmentTypeDef = TypedDict(
    "_ClientCreateFunctionEnvironmentTypeDef", {"Variables": Dict[str, str]}, total=False
)


class ClientCreateFunctionEnvironmentTypeDef(_ClientCreateFunctionEnvironmentTypeDef):
    """
    Environment variables that are accessible from function code during execution.
    - **Variables** *(dict) --*

      Environment variable key-value pairs.
      - *(string) --*

        - *(string) --*
    """


_ClientCreateFunctionResponseDeadLetterConfigTypeDef = TypedDict(
    "_ClientCreateFunctionResponseDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)


class ClientCreateFunctionResponseDeadLetterConfigTypeDef(
    _ClientCreateFunctionResponseDeadLetterConfigTypeDef
):
    pass


_ClientCreateFunctionResponseEnvironmentErrorTypeDef = TypedDict(
    "_ClientCreateFunctionResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientCreateFunctionResponseEnvironmentErrorTypeDef(
    _ClientCreateFunctionResponseEnvironmentErrorTypeDef
):
    pass


_ClientCreateFunctionResponseEnvironmentTypeDef = TypedDict(
    "_ClientCreateFunctionResponseEnvironmentTypeDef",
    {"Variables": Dict[str, str], "Error": ClientCreateFunctionResponseEnvironmentErrorTypeDef},
    total=False,
)


class ClientCreateFunctionResponseEnvironmentTypeDef(
    _ClientCreateFunctionResponseEnvironmentTypeDef
):
    pass


_ClientCreateFunctionResponseLayersTypeDef = TypedDict(
    "_ClientCreateFunctionResponseLayersTypeDef", {"Arn": str, "CodeSize": int}, total=False
)


class ClientCreateFunctionResponseLayersTypeDef(_ClientCreateFunctionResponseLayersTypeDef):
    pass


_ClientCreateFunctionResponseTracingConfigTypeDef = TypedDict(
    "_ClientCreateFunctionResponseTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ClientCreateFunctionResponseTracingConfigTypeDef(
    _ClientCreateFunctionResponseTracingConfigTypeDef
):
    pass


_ClientCreateFunctionResponseVpcConfigTypeDef = TypedDict(
    "_ClientCreateFunctionResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientCreateFunctionResponseVpcConfigTypeDef(_ClientCreateFunctionResponseVpcConfigTypeDef):
    pass


_ClientCreateFunctionResponseTypeDef = TypedDict(
    "_ClientCreateFunctionResponseTypeDef",
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


class ClientCreateFunctionResponseTypeDef(_ClientCreateFunctionResponseTypeDef):
    """
    - *(dict) --*

      Details about a function's configuration.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_ClientCreateFunctionTracingConfigTypeDef = TypedDict(
    "_ClientCreateFunctionTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ClientCreateFunctionTracingConfigTypeDef(_ClientCreateFunctionTracingConfigTypeDef):
    """
    Set ``Mode`` to ``Active`` to sample and trace a subset of incoming requests with AWS X-Ray.
    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientCreateFunctionVpcConfigTypeDef = TypedDict(
    "_ClientCreateFunctionVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateFunctionVpcConfigTypeDef(_ClientCreateFunctionVpcConfigTypeDef):
    """
    For network connectivity to AWS resources in a VPC, specify a list of security groups and
    subnets in the VPC. When you connect a function to a VPC, it can only access resources and the
    internet through that VPC. For more information, see `VPC Settings
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html>`__ .
    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.
      - *(string) --*
    """


_ClientDeleteEventSourceMappingResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientDeleteEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientDeleteEventSourceMappingResponseDestinationConfigOnFailureTypeDef(
    _ClientDeleteEventSourceMappingResponseDestinationConfigOnFailureTypeDef
):
    pass


_ClientDeleteEventSourceMappingResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientDeleteEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientDeleteEventSourceMappingResponseDestinationConfigOnSuccessTypeDef(
    _ClientDeleteEventSourceMappingResponseDestinationConfigOnSuccessTypeDef
):
    pass


_ClientDeleteEventSourceMappingResponseDestinationConfigTypeDef = TypedDict(
    "_ClientDeleteEventSourceMappingResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientDeleteEventSourceMappingResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientDeleteEventSourceMappingResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientDeleteEventSourceMappingResponseDestinationConfigTypeDef(
    _ClientDeleteEventSourceMappingResponseDestinationConfigTypeDef
):
    pass


_ClientDeleteEventSourceMappingResponseTypeDef = TypedDict(
    "_ClientDeleteEventSourceMappingResponseTypeDef",
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


class ClientDeleteEventSourceMappingResponseTypeDef(_ClientDeleteEventSourceMappingResponseTypeDef):
    """
    - *(dict) --*

      A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping
      for details.
      - **UUID** *(string) --*

        The identifier of the event source mapping.
    """


_ClientGetAccountSettingsResponseAccountLimitTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseAccountLimitTypeDef",
    {
        "TotalCodeSize": int,
        "CodeSizeUnzipped": int,
        "CodeSizeZipped": int,
        "ConcurrentExecutions": int,
        "UnreservedConcurrentExecutions": int,
    },
    total=False,
)


class ClientGetAccountSettingsResponseAccountLimitTypeDef(
    _ClientGetAccountSettingsResponseAccountLimitTypeDef
):
    """
    - **AccountLimit** *(dict) --*

      Limits that are related to concurrency and code storage.
      - **TotalCodeSize** *(integer) --*

        The amount of storage space that you can use for all deployment packages and layer archives.
    """


_ClientGetAccountSettingsResponseAccountUsageTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseAccountUsageTypeDef",
    {"TotalCodeSize": int, "FunctionCount": int},
    total=False,
)


class ClientGetAccountSettingsResponseAccountUsageTypeDef(
    _ClientGetAccountSettingsResponseAccountUsageTypeDef
):
    pass


_ClientGetAccountSettingsResponseTypeDef = TypedDict(
    "_ClientGetAccountSettingsResponseTypeDef",
    {
        "AccountLimit": ClientGetAccountSettingsResponseAccountLimitTypeDef,
        "AccountUsage": ClientGetAccountSettingsResponseAccountUsageTypeDef,
    },
    total=False,
)


class ClientGetAccountSettingsResponseTypeDef(_ClientGetAccountSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **AccountLimit** *(dict) --*

        Limits that are related to concurrency and code storage.
        - **TotalCodeSize** *(integer) --*

          The amount of storage space that you can use for all deployment packages and layer
          archives.
    """


_ClientGetAliasResponseRoutingConfigTypeDef = TypedDict(
    "_ClientGetAliasResponseRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientGetAliasResponseRoutingConfigTypeDef(_ClientGetAliasResponseRoutingConfigTypeDef):
    pass


_ClientGetAliasResponseTypeDef = TypedDict(
    "_ClientGetAliasResponseTypeDef",
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


class ClientGetAliasResponseTypeDef(_ClientGetAliasResponseTypeDef):
    """
    - *(dict) --*

      Provides configuration information about a Lambda function `alias
      <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .
      - **AliasArn** *(string) --*

        The Amazon Resource Name (ARN) of the alias.
    """


_ClientGetEventSourceMappingResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientGetEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientGetEventSourceMappingResponseDestinationConfigOnFailureTypeDef(
    _ClientGetEventSourceMappingResponseDestinationConfigOnFailureTypeDef
):
    pass


_ClientGetEventSourceMappingResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientGetEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientGetEventSourceMappingResponseDestinationConfigOnSuccessTypeDef(
    _ClientGetEventSourceMappingResponseDestinationConfigOnSuccessTypeDef
):
    pass


_ClientGetEventSourceMappingResponseDestinationConfigTypeDef = TypedDict(
    "_ClientGetEventSourceMappingResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientGetEventSourceMappingResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientGetEventSourceMappingResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientGetEventSourceMappingResponseDestinationConfigTypeDef(
    _ClientGetEventSourceMappingResponseDestinationConfigTypeDef
):
    pass


_ClientGetEventSourceMappingResponseTypeDef = TypedDict(
    "_ClientGetEventSourceMappingResponseTypeDef",
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


class ClientGetEventSourceMappingResponseTypeDef(_ClientGetEventSourceMappingResponseTypeDef):
    """
    - *(dict) --*

      A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping
      for details.
      - **UUID** *(string) --*

        The identifier of the event source mapping.
    """


_ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef(
    _ClientGetFunctionConfigurationResponseDeadLetterConfigTypeDef
):
    pass


_ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef(
    _ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef
):
    pass


_ClientGetFunctionConfigurationResponseEnvironmentTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientGetFunctionConfigurationResponseEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientGetFunctionConfigurationResponseEnvironmentTypeDef(
    _ClientGetFunctionConfigurationResponseEnvironmentTypeDef
):
    pass


_ClientGetFunctionConfigurationResponseLayersTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientGetFunctionConfigurationResponseLayersTypeDef(
    _ClientGetFunctionConfigurationResponseLayersTypeDef
):
    pass


_ClientGetFunctionConfigurationResponseTracingConfigTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ClientGetFunctionConfigurationResponseTracingConfigTypeDef(
    _ClientGetFunctionConfigurationResponseTracingConfigTypeDef
):
    pass


_ClientGetFunctionConfigurationResponseVpcConfigTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientGetFunctionConfigurationResponseVpcConfigTypeDef(
    _ClientGetFunctionConfigurationResponseVpcConfigTypeDef
):
    pass


_ClientGetFunctionConfigurationResponseTypeDef = TypedDict(
    "_ClientGetFunctionConfigurationResponseTypeDef",
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


class ClientGetFunctionConfigurationResponseTypeDef(_ClientGetFunctionConfigurationResponseTypeDef):
    """
    - *(dict) --*

      Details about a function's configuration.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef(
    _ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef
):
    pass


_ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef(
    _ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef
):
    pass


_ClientGetFunctionEventInvokeConfigResponseDestinationConfigTypeDef = TypedDict(
    "_ClientGetFunctionEventInvokeConfigResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientGetFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientGetFunctionEventInvokeConfigResponseDestinationConfigTypeDef(
    _ClientGetFunctionEventInvokeConfigResponseDestinationConfigTypeDef
):
    pass


_ClientGetFunctionEventInvokeConfigResponseTypeDef = TypedDict(
    "_ClientGetFunctionEventInvokeConfigResponseTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": ClientGetFunctionEventInvokeConfigResponseDestinationConfigTypeDef,
    },
    total=False,
)


class ClientGetFunctionEventInvokeConfigResponseTypeDef(
    _ClientGetFunctionEventInvokeConfigResponseTypeDef
):
    """
    - *(dict) --*

      - **LastModified** *(datetime) --*

        The date and time that the configuration was last updated.
    """


_ClientGetFunctionResponseCodeTypeDef = TypedDict(
    "_ClientGetFunctionResponseCodeTypeDef", {"RepositoryType": str, "Location": str}, total=False
)


class ClientGetFunctionResponseCodeTypeDef(_ClientGetFunctionResponseCodeTypeDef):
    pass


_ClientGetFunctionResponseConcurrencyTypeDef = TypedDict(
    "_ClientGetFunctionResponseConcurrencyTypeDef",
    {"ReservedConcurrentExecutions": int},
    total=False,
)


class ClientGetFunctionResponseConcurrencyTypeDef(_ClientGetFunctionResponseConcurrencyTypeDef):
    pass


_ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef(
    _ClientGetFunctionResponseConfigurationDeadLetterConfigTypeDef
):
    pass


_ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef(
    _ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef
):
    pass


_ClientGetFunctionResponseConfigurationEnvironmentTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientGetFunctionResponseConfigurationEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientGetFunctionResponseConfigurationEnvironmentTypeDef(
    _ClientGetFunctionResponseConfigurationEnvironmentTypeDef
):
    pass


_ClientGetFunctionResponseConfigurationLayersTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientGetFunctionResponseConfigurationLayersTypeDef(
    _ClientGetFunctionResponseConfigurationLayersTypeDef
):
    pass


_ClientGetFunctionResponseConfigurationTracingConfigTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ClientGetFunctionResponseConfigurationTracingConfigTypeDef(
    _ClientGetFunctionResponseConfigurationTracingConfigTypeDef
):
    pass


_ClientGetFunctionResponseConfigurationVpcConfigTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientGetFunctionResponseConfigurationVpcConfigTypeDef(
    _ClientGetFunctionResponseConfigurationVpcConfigTypeDef
):
    pass


_ClientGetFunctionResponseConfigurationTypeDef = TypedDict(
    "_ClientGetFunctionResponseConfigurationTypeDef",
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


class ClientGetFunctionResponseConfigurationTypeDef(_ClientGetFunctionResponseConfigurationTypeDef):
    """
    - **Configuration** *(dict) --*

      The configuration of the function or version.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_ClientGetFunctionResponseTypeDef = TypedDict(
    "_ClientGetFunctionResponseTypeDef",
    {
        "Configuration": ClientGetFunctionResponseConfigurationTypeDef,
        "Code": ClientGetFunctionResponseCodeTypeDef,
        "Tags": Dict[str, str],
        "Concurrency": ClientGetFunctionResponseConcurrencyTypeDef,
    },
    total=False,
)


class ClientGetFunctionResponseTypeDef(_ClientGetFunctionResponseTypeDef):
    """
    - *(dict) --*

      - **Configuration** *(dict) --*

        The configuration of the function or version.
        - **FunctionName** *(string) --*

          The name of the function.
    """


_ClientGetLayerVersionByArnResponseContentTypeDef = TypedDict(
    "_ClientGetLayerVersionByArnResponseContentTypeDef",
    {"Location": str, "CodeSha256": str, "CodeSize": int},
    total=False,
)


class ClientGetLayerVersionByArnResponseContentTypeDef(
    _ClientGetLayerVersionByArnResponseContentTypeDef
):
    """
    - **Content** *(dict) --*

      Details about the layer version.
      - **Location** *(string) --*

        A link to the layer archive in Amazon S3 that is valid for 10 minutes.
    """


_ClientGetLayerVersionByArnResponseTypeDef = TypedDict(
    "_ClientGetLayerVersionByArnResponseTypeDef",
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


class ClientGetLayerVersionByArnResponseTypeDef(_ClientGetLayerVersionByArnResponseTypeDef):
    """
    - *(dict) --*

      - **Content** *(dict) --*

        Details about the layer version.
        - **Location** *(string) --*

          A link to the layer archive in Amazon S3 that is valid for 10 minutes.
    """


_ClientGetLayerVersionPolicyResponseTypeDef = TypedDict(
    "_ClientGetLayerVersionPolicyResponseTypeDef", {"Policy": str, "RevisionId": str}, total=False
)


class ClientGetLayerVersionPolicyResponseTypeDef(_ClientGetLayerVersionPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(string) --*

        The policy document.
    """


_ClientGetLayerVersionResponseContentTypeDef = TypedDict(
    "_ClientGetLayerVersionResponseContentTypeDef",
    {"Location": str, "CodeSha256": str, "CodeSize": int},
    total=False,
)


class ClientGetLayerVersionResponseContentTypeDef(_ClientGetLayerVersionResponseContentTypeDef):
    """
    - **Content** *(dict) --*

      Details about the layer version.
      - **Location** *(string) --*

        A link to the layer archive in Amazon S3 that is valid for 10 minutes.
    """


_ClientGetLayerVersionResponseTypeDef = TypedDict(
    "_ClientGetLayerVersionResponseTypeDef",
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


class ClientGetLayerVersionResponseTypeDef(_ClientGetLayerVersionResponseTypeDef):
    """
    - *(dict) --*

      - **Content** *(dict) --*

        Details about the layer version.
        - **Location** *(string) --*

          A link to the layer archive in Amazon S3 that is valid for 10 minutes.
    """


_ClientGetPolicyResponseTypeDef = TypedDict(
    "_ClientGetPolicyResponseTypeDef", {"Policy": str, "RevisionId": str}, total=False
)


class ClientGetPolicyResponseTypeDef(_ClientGetPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(string) --*

        The resource-based policy.
    """


_ClientInvokeAsyncResponseTypeDef = TypedDict(
    "_ClientInvokeAsyncResponseTypeDef", {"Status": int}, total=False
)


class ClientInvokeAsyncResponseTypeDef(_ClientInvokeAsyncResponseTypeDef):
    """
    - *(dict) --*

      A success response (``202 Accepted`` ) indicates that the request is queued for invocation.
      - **Status** *(integer) --*

        The status code.
    """


_ClientInvokeResponseTypeDef = TypedDict(
    "_ClientInvokeResponseTypeDef",
    {
        "StatusCode": int,
        "FunctionError": str,
        "LogResult": str,
        "Payload": StreamingBody,
        "ExecutedVersion": str,
    },
    total=False,
)


class ClientInvokeResponseTypeDef(_ClientInvokeResponseTypeDef):
    """
    - *(dict) --*

      - **StatusCode** *(integer) --*

        The HTTP status code is in the 200 range for a successful request. For the
        ``RequestResponse`` invocation type, this status code is 200. For the ``Event`` invocation
        type, this status code is 202. For the ``DryRun`` invocation type, the status code is 204.
    """


_ClientListAliasesResponseAliasesRoutingConfigTypeDef = TypedDict(
    "_ClientListAliasesResponseAliasesRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientListAliasesResponseAliasesRoutingConfigTypeDef(
    _ClientListAliasesResponseAliasesRoutingConfigTypeDef
):
    pass


_ClientListAliasesResponseAliasesTypeDef = TypedDict(
    "_ClientListAliasesResponseAliasesTypeDef",
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


class ClientListAliasesResponseAliasesTypeDef(_ClientListAliasesResponseAliasesTypeDef):
    pass


_ClientListAliasesResponseTypeDef = TypedDict(
    "_ClientListAliasesResponseTypeDef",
    {"NextMarker": str, "Aliases": List[ClientListAliasesResponseAliasesTypeDef]},
    total=False,
)


class ClientListAliasesResponseTypeDef(_ClientListAliasesResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        The pagination token that's included if more results are available.
    """


_ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnFailureTypeDef(
    _ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnFailureTypeDef
):
    pass


_ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef(
    _ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef
):
    pass


_ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigTypeDef = TypedDict(
    "_ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigTypeDef",
    {
        "OnSuccess": ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigTypeDef(
    _ClientListEventSourceMappingsResponseEventSourceMappingsDestinationConfigTypeDef
):
    pass


_ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef = TypedDict(
    "_ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef",
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


class ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef(
    _ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef
):
    pass


_ClientListEventSourceMappingsResponseTypeDef = TypedDict(
    "_ClientListEventSourceMappingsResponseTypeDef",
    {
        "NextMarker": str,
        "EventSourceMappings": List[
            ClientListEventSourceMappingsResponseEventSourceMappingsTypeDef
        ],
    },
    total=False,
)


class ClientListEventSourceMappingsResponseTypeDef(_ClientListEventSourceMappingsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        A pagination token that's returned when the response doesn't contain all event source
        mappings.
    """


_ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef(
    _ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef
):
    pass


_ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef(
    _ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef
):
    pass


_ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigTypeDef = TypedDict(
    "_ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigTypeDef",
    {
        "OnSuccess": ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigTypeDef(
    _ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigTypeDef
):
    pass


_ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsTypeDef = TypedDict(
    "_ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsDestinationConfigTypeDef,
    },
    total=False,
)


class ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsTypeDef(
    _ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsTypeDef
):
    """
    - *(dict) --*

      - **LastModified** *(datetime) --*

        The date and time that the configuration was last updated.
    """


_ClientListFunctionEventInvokeConfigsResponseTypeDef = TypedDict(
    "_ClientListFunctionEventInvokeConfigsResponseTypeDef",
    {
        "FunctionEventInvokeConfigs": List[
            ClientListFunctionEventInvokeConfigsResponseFunctionEventInvokeConfigsTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)


class ClientListFunctionEventInvokeConfigsResponseTypeDef(
    _ClientListFunctionEventInvokeConfigsResponseTypeDef
):
    """
    - *(dict) --*

      - **FunctionEventInvokeConfigs** *(list) --*

        A list of configurations.
        - *(dict) --*

          - **LastModified** *(datetime) --*

            The date and time that the configuration was last updated.
    """


_ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)


class ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef(
    _ClientListFunctionsResponseFunctionsDeadLetterConfigTypeDef
):
    pass


_ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef(
    _ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef
):
    pass


_ClientListFunctionsResponseFunctionsEnvironmentTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientListFunctionsResponseFunctionsEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientListFunctionsResponseFunctionsEnvironmentTypeDef(
    _ClientListFunctionsResponseFunctionsEnvironmentTypeDef
):
    pass


_ClientListFunctionsResponseFunctionsLayersTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsLayersTypeDef", {"Arn": str, "CodeSize": int}, total=False
)


class ClientListFunctionsResponseFunctionsLayersTypeDef(
    _ClientListFunctionsResponseFunctionsLayersTypeDef
):
    pass


_ClientListFunctionsResponseFunctionsTracingConfigTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ClientListFunctionsResponseFunctionsTracingConfigTypeDef(
    _ClientListFunctionsResponseFunctionsTracingConfigTypeDef
):
    pass


_ClientListFunctionsResponseFunctionsVpcConfigTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientListFunctionsResponseFunctionsVpcConfigTypeDef(
    _ClientListFunctionsResponseFunctionsVpcConfigTypeDef
):
    pass


_ClientListFunctionsResponseFunctionsTypeDef = TypedDict(
    "_ClientListFunctionsResponseFunctionsTypeDef",
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


class ClientListFunctionsResponseFunctionsTypeDef(_ClientListFunctionsResponseFunctionsTypeDef):
    pass


_ClientListFunctionsResponseTypeDef = TypedDict(
    "_ClientListFunctionsResponseTypeDef",
    {"NextMarker": str, "Functions": List[ClientListFunctionsResponseFunctionsTypeDef]},
    total=False,
)


class ClientListFunctionsResponseTypeDef(_ClientListFunctionsResponseTypeDef):
    """
    - *(dict) --*

      A list of Lambda functions.
      - **NextMarker** *(string) --*

        The pagination token that's included if more results are available.
    """


_ClientListLayerVersionsResponseLayerVersionsTypeDef = TypedDict(
    "_ClientListLayerVersionsResponseLayerVersionsTypeDef",
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


class ClientListLayerVersionsResponseLayerVersionsTypeDef(
    _ClientListLayerVersionsResponseLayerVersionsTypeDef
):
    pass


_ClientListLayerVersionsResponseTypeDef = TypedDict(
    "_ClientListLayerVersionsResponseTypeDef",
    {"NextMarker": str, "LayerVersions": List[ClientListLayerVersionsResponseLayerVersionsTypeDef]},
    total=False,
)


class ClientListLayerVersionsResponseTypeDef(_ClientListLayerVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        A pagination token returned when the response doesn't contain all versions.
    """


_ClientListLayersResponseLayersLatestMatchingVersionTypeDef = TypedDict(
    "_ClientListLayersResponseLayersLatestMatchingVersionTypeDef",
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


class ClientListLayersResponseLayersLatestMatchingVersionTypeDef(
    _ClientListLayersResponseLayersLatestMatchingVersionTypeDef
):
    pass


_ClientListLayersResponseLayersTypeDef = TypedDict(
    "_ClientListLayersResponseLayersTypeDef",
    {
        "LayerName": str,
        "LayerArn": str,
        "LatestMatchingVersion": ClientListLayersResponseLayersLatestMatchingVersionTypeDef,
    },
    total=False,
)


class ClientListLayersResponseLayersTypeDef(_ClientListLayersResponseLayersTypeDef):
    pass


_ClientListLayersResponseTypeDef = TypedDict(
    "_ClientListLayersResponseTypeDef",
    {"NextMarker": str, "Layers": List[ClientListLayersResponseLayersTypeDef]},
    total=False,
)


class ClientListLayersResponseTypeDef(_ClientListLayersResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        A pagination token returned when the response doesn't contain all layers.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        The function's tags.
        - *(string) --*

          - *(string) --*
    """


_ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef(
    _ClientListVersionsByFunctionResponseVersionsDeadLetterConfigTypeDef
):
    pass


_ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef(
    _ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef
):
    pass


_ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientListVersionsByFunctionResponseVersionsEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef(
    _ClientListVersionsByFunctionResponseVersionsEnvironmentTypeDef
):
    pass


_ClientListVersionsByFunctionResponseVersionsLayersTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsLayersTypeDef(
    _ClientListVersionsByFunctionResponseVersionsLayersTypeDef
):
    pass


_ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef(
    _ClientListVersionsByFunctionResponseVersionsTracingConfigTypeDef
):
    pass


_ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef(
    _ClientListVersionsByFunctionResponseVersionsVpcConfigTypeDef
):
    pass


_ClientListVersionsByFunctionResponseVersionsTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseVersionsTypeDef",
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


class ClientListVersionsByFunctionResponseVersionsTypeDef(
    _ClientListVersionsByFunctionResponseVersionsTypeDef
):
    pass


_ClientListVersionsByFunctionResponseTypeDef = TypedDict(
    "_ClientListVersionsByFunctionResponseTypeDef",
    {"NextMarker": str, "Versions": List[ClientListVersionsByFunctionResponseVersionsTypeDef]},
    total=False,
)


class ClientListVersionsByFunctionResponseTypeDef(_ClientListVersionsByFunctionResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        The pagination token that's included if more results are available.
    """


_ClientPublishLayerVersionContentTypeDef = TypedDict(
    "_ClientPublishLayerVersionContentTypeDef",
    {"S3Bucket": str, "S3Key": str, "S3ObjectVersion": str, "ZipFile": bytes},
    total=False,
)


class ClientPublishLayerVersionContentTypeDef(_ClientPublishLayerVersionContentTypeDef):
    """
    The function layer archive.
    - **S3Bucket** *(string) --*

      The Amazon S3 bucket of the layer archive.
    """


_ClientPublishLayerVersionResponseContentTypeDef = TypedDict(
    "_ClientPublishLayerVersionResponseContentTypeDef",
    {"Location": str, "CodeSha256": str, "CodeSize": int},
    total=False,
)


class ClientPublishLayerVersionResponseContentTypeDef(
    _ClientPublishLayerVersionResponseContentTypeDef
):
    """
    - **Content** *(dict) --*

      Details about the layer version.
      - **Location** *(string) --*

        A link to the layer archive in Amazon S3 that is valid for 10 minutes.
    """


_ClientPublishLayerVersionResponseTypeDef = TypedDict(
    "_ClientPublishLayerVersionResponseTypeDef",
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


class ClientPublishLayerVersionResponseTypeDef(_ClientPublishLayerVersionResponseTypeDef):
    """
    - *(dict) --*

      - **Content** *(dict) --*

        Details about the layer version.
        - **Location** *(string) --*

          A link to the layer archive in Amazon S3 that is valid for 10 minutes.
    """


_ClientPublishVersionResponseDeadLetterConfigTypeDef = TypedDict(
    "_ClientPublishVersionResponseDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)


class ClientPublishVersionResponseDeadLetterConfigTypeDef(
    _ClientPublishVersionResponseDeadLetterConfigTypeDef
):
    pass


_ClientPublishVersionResponseEnvironmentErrorTypeDef = TypedDict(
    "_ClientPublishVersionResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientPublishVersionResponseEnvironmentErrorTypeDef(
    _ClientPublishVersionResponseEnvironmentErrorTypeDef
):
    pass


_ClientPublishVersionResponseEnvironmentTypeDef = TypedDict(
    "_ClientPublishVersionResponseEnvironmentTypeDef",
    {"Variables": Dict[str, str], "Error": ClientPublishVersionResponseEnvironmentErrorTypeDef},
    total=False,
)


class ClientPublishVersionResponseEnvironmentTypeDef(
    _ClientPublishVersionResponseEnvironmentTypeDef
):
    pass


_ClientPublishVersionResponseLayersTypeDef = TypedDict(
    "_ClientPublishVersionResponseLayersTypeDef", {"Arn": str, "CodeSize": int}, total=False
)


class ClientPublishVersionResponseLayersTypeDef(_ClientPublishVersionResponseLayersTypeDef):
    pass


_ClientPublishVersionResponseTracingConfigTypeDef = TypedDict(
    "_ClientPublishVersionResponseTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ClientPublishVersionResponseTracingConfigTypeDef(
    _ClientPublishVersionResponseTracingConfigTypeDef
):
    pass


_ClientPublishVersionResponseVpcConfigTypeDef = TypedDict(
    "_ClientPublishVersionResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientPublishVersionResponseVpcConfigTypeDef(_ClientPublishVersionResponseVpcConfigTypeDef):
    pass


_ClientPublishVersionResponseTypeDef = TypedDict(
    "_ClientPublishVersionResponseTypeDef",
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


class ClientPublishVersionResponseTypeDef(_ClientPublishVersionResponseTypeDef):
    """
    - *(dict) --*

      Details about a function's configuration.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_ClientPutFunctionConcurrencyResponseTypeDef = TypedDict(
    "_ClientPutFunctionConcurrencyResponseTypeDef",
    {"ReservedConcurrentExecutions": int},
    total=False,
)


class ClientPutFunctionConcurrencyResponseTypeDef(_ClientPutFunctionConcurrencyResponseTypeDef):
    """
    - *(dict) --*

      - **ReservedConcurrentExecutions** *(integer) --*

        The number of concurrent executions that are reserved for this function. For more
        information, see `Managing Concurrency
        <https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .
    """


_ClientPutFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientPutFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientPutFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef(
    _ClientPutFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef
):
    pass


_ClientPutFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientPutFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientPutFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef(
    _ClientPutFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef
):
    pass


_ClientPutFunctionEventInvokeConfigDestinationConfigTypeDef = TypedDict(
    "_ClientPutFunctionEventInvokeConfigDestinationConfigTypeDef",
    {
        "OnSuccess": ClientPutFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientPutFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientPutFunctionEventInvokeConfigDestinationConfigTypeDef(
    _ClientPutFunctionEventInvokeConfigDestinationConfigTypeDef
):
    """
    A destination for events after they have been sent to a function for processing.

      **Destinations**
    """


_ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef(
    _ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef
):
    pass


_ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef(
    _ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef
):
    pass


_ClientPutFunctionEventInvokeConfigResponseDestinationConfigTypeDef = TypedDict(
    "_ClientPutFunctionEventInvokeConfigResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientPutFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientPutFunctionEventInvokeConfigResponseDestinationConfigTypeDef(
    _ClientPutFunctionEventInvokeConfigResponseDestinationConfigTypeDef
):
    pass


_ClientPutFunctionEventInvokeConfigResponseTypeDef = TypedDict(
    "_ClientPutFunctionEventInvokeConfigResponseTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": ClientPutFunctionEventInvokeConfigResponseDestinationConfigTypeDef,
    },
    total=False,
)


class ClientPutFunctionEventInvokeConfigResponseTypeDef(
    _ClientPutFunctionEventInvokeConfigResponseTypeDef
):
    """
    - *(dict) --*

      - **LastModified** *(datetime) --*

        The date and time that the configuration was last updated.
    """


_ClientUpdateAliasResponseRoutingConfigTypeDef = TypedDict(
    "_ClientUpdateAliasResponseRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientUpdateAliasResponseRoutingConfigTypeDef(_ClientUpdateAliasResponseRoutingConfigTypeDef):
    pass


_ClientUpdateAliasResponseTypeDef = TypedDict(
    "_ClientUpdateAliasResponseTypeDef",
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


class ClientUpdateAliasResponseTypeDef(_ClientUpdateAliasResponseTypeDef):
    """
    - *(dict) --*

      Provides configuration information about a Lambda function `alias
      <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .
      - **AliasArn** *(string) --*

        The Amazon Resource Name (ARN) of the alias.
    """


_ClientUpdateAliasRoutingConfigTypeDef = TypedDict(
    "_ClientUpdateAliasRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ClientUpdateAliasRoutingConfigTypeDef(_ClientUpdateAliasRoutingConfigTypeDef):
    """
    The `routing configuration
    <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__ of
    the alias.
    - **AdditionalVersionWeights** *(dict) --*

      The name of the second alias, and the percentage of traffic that's routed to it.
      - *(string) --*

        - *(float) --*
    """


_ClientUpdateEventSourceMappingDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientUpdateEventSourceMappingDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientUpdateEventSourceMappingDestinationConfigOnFailureTypeDef(
    _ClientUpdateEventSourceMappingDestinationConfigOnFailureTypeDef
):
    pass


_ClientUpdateEventSourceMappingDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientUpdateEventSourceMappingDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientUpdateEventSourceMappingDestinationConfigOnSuccessTypeDef(
    _ClientUpdateEventSourceMappingDestinationConfigOnSuccessTypeDef
):
    """
    - **OnSuccess** *(dict) --*

      The destination configuration for successful invocations.
      - **Destination** *(string) --*

        The Amazon Resource Name (ARN) of the destination resource.
    """


_ClientUpdateEventSourceMappingDestinationConfigTypeDef = TypedDict(
    "_ClientUpdateEventSourceMappingDestinationConfigTypeDef",
    {
        "OnSuccess": ClientUpdateEventSourceMappingDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientUpdateEventSourceMappingDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientUpdateEventSourceMappingDestinationConfigTypeDef(
    _ClientUpdateEventSourceMappingDestinationConfigTypeDef
):
    """
    (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.
    - **OnSuccess** *(dict) --*

      The destination configuration for successful invocations.
      - **Destination** *(string) --*

        The Amazon Resource Name (ARN) of the destination resource.
    """


_ClientUpdateEventSourceMappingResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientUpdateEventSourceMappingResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientUpdateEventSourceMappingResponseDestinationConfigOnFailureTypeDef(
    _ClientUpdateEventSourceMappingResponseDestinationConfigOnFailureTypeDef
):
    pass


_ClientUpdateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientUpdateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientUpdateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef(
    _ClientUpdateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef
):
    pass


_ClientUpdateEventSourceMappingResponseDestinationConfigTypeDef = TypedDict(
    "_ClientUpdateEventSourceMappingResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientUpdateEventSourceMappingResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientUpdateEventSourceMappingResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientUpdateEventSourceMappingResponseDestinationConfigTypeDef(
    _ClientUpdateEventSourceMappingResponseDestinationConfigTypeDef
):
    pass


_ClientUpdateEventSourceMappingResponseTypeDef = TypedDict(
    "_ClientUpdateEventSourceMappingResponseTypeDef",
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


class ClientUpdateEventSourceMappingResponseTypeDef(_ClientUpdateEventSourceMappingResponseTypeDef):
    """
    - *(dict) --*

      A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping
      for details.
      - **UUID** *(string) --*

        The identifier of the event source mapping.
    """


_ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)


class ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef(
    _ClientUpdateFunctionCodeResponseDeadLetterConfigTypeDef
):
    pass


_ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef(
    _ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef
):
    pass


_ClientUpdateFunctionCodeResponseEnvironmentTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseEnvironmentTypeDef",
    {"Variables": Dict[str, str], "Error": ClientUpdateFunctionCodeResponseEnvironmentErrorTypeDef},
    total=False,
)


class ClientUpdateFunctionCodeResponseEnvironmentTypeDef(
    _ClientUpdateFunctionCodeResponseEnvironmentTypeDef
):
    pass


_ClientUpdateFunctionCodeResponseLayersTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseLayersTypeDef", {"Arn": str, "CodeSize": int}, total=False
)


class ClientUpdateFunctionCodeResponseLayersTypeDef(_ClientUpdateFunctionCodeResponseLayersTypeDef):
    pass


_ClientUpdateFunctionCodeResponseTracingConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ClientUpdateFunctionCodeResponseTracingConfigTypeDef(
    _ClientUpdateFunctionCodeResponseTracingConfigTypeDef
):
    pass


_ClientUpdateFunctionCodeResponseVpcConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientUpdateFunctionCodeResponseVpcConfigTypeDef(
    _ClientUpdateFunctionCodeResponseVpcConfigTypeDef
):
    pass


_ClientUpdateFunctionCodeResponseTypeDef = TypedDict(
    "_ClientUpdateFunctionCodeResponseTypeDef",
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


class ClientUpdateFunctionCodeResponseTypeDef(_ClientUpdateFunctionCodeResponseTypeDef):
    """
    - *(dict) --*

      Details about a function's configuration.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef", {"TargetArn": str}, total=False
)


class ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef(
    _ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef
):
    """
    A dead letter queue configuration that specifies the queue or topic where Lambda sends
    asynchronous events when they fail processing. For more information, see `Dead Letter Queues
    <https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#dlq>`__ .
    - **TargetArn** *(string) --*

      The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.
    """


_ClientUpdateFunctionConfigurationEnvironmentTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationEnvironmentTypeDef",
    {"Variables": Dict[str, str]},
    total=False,
)


class ClientUpdateFunctionConfigurationEnvironmentTypeDef(
    _ClientUpdateFunctionConfigurationEnvironmentTypeDef
):
    """
    Environment variables that are accessible from function code during execution.
    - **Variables** *(dict) --*

      Environment variable key-value pairs.
      - *(string) --*

        - *(string) --*
    """


_ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef(
    _ClientUpdateFunctionConfigurationResponseDeadLetterConfigTypeDef
):
    pass


_ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef(
    _ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef
):
    pass


_ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ClientUpdateFunctionConfigurationResponseEnvironmentErrorTypeDef,
    },
    total=False,
)


class ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef(
    _ClientUpdateFunctionConfigurationResponseEnvironmentTypeDef
):
    pass


_ClientUpdateFunctionConfigurationResponseLayersTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ClientUpdateFunctionConfigurationResponseLayersTypeDef(
    _ClientUpdateFunctionConfigurationResponseLayersTypeDef
):
    pass


_ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef(
    _ClientUpdateFunctionConfigurationResponseTracingConfigTypeDef
):
    pass


_ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef(
    _ClientUpdateFunctionConfigurationResponseVpcConfigTypeDef
):
    pass


_ClientUpdateFunctionConfigurationResponseTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationResponseTypeDef",
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


class ClientUpdateFunctionConfigurationResponseTypeDef(
    _ClientUpdateFunctionConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      Details about a function's configuration.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_ClientUpdateFunctionConfigurationTracingConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ClientUpdateFunctionConfigurationTracingConfigTypeDef(
    _ClientUpdateFunctionConfigurationTracingConfigTypeDef
):
    """
    Set ``Mode`` to ``Active`` to sample and trace a subset of incoming requests with AWS X-Ray.
    - **Mode** *(string) --*

      The tracing mode.
    """


_ClientUpdateFunctionConfigurationVpcConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionConfigurationVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientUpdateFunctionConfigurationVpcConfigTypeDef(
    _ClientUpdateFunctionConfigurationVpcConfigTypeDef
):
    """
    For network connectivity to AWS resources in a VPC, specify a list of security groups and
    subnets in the VPC. When you connect a function to a VPC, it can only access resources and the
    internet through that VPC. For more information, see `VPC Settings
    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html>`__ .
    - **SubnetIds** *(list) --*

      A list of VPC subnet IDs.
      - *(string) --*
    """


_ClientUpdateFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientUpdateFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientUpdateFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef(
    _ClientUpdateFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef
):
    pass


_ClientUpdateFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientUpdateFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientUpdateFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef(
    _ClientUpdateFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef
):
    pass


_ClientUpdateFunctionEventInvokeConfigDestinationConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionEventInvokeConfigDestinationConfigTypeDef",
    {
        "OnSuccess": ClientUpdateFunctionEventInvokeConfigDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientUpdateFunctionEventInvokeConfigDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientUpdateFunctionEventInvokeConfigDestinationConfigTypeDef(
    _ClientUpdateFunctionEventInvokeConfigDestinationConfigTypeDef
):
    """
    A destination for events after they have been sent to a function for processing.

      **Destinations**
    """


_ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef = TypedDict(
    "_ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef(
    _ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef
):
    pass


_ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef(
    _ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef
):
    pass


_ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigTypeDef = TypedDict(
    "_ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigTypeDef",
    {
        "OnSuccess": ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnSuccessTypeDef,
        "OnFailure": ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigTypeDef(
    _ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigTypeDef
):
    pass


_ClientUpdateFunctionEventInvokeConfigResponseTypeDef = TypedDict(
    "_ClientUpdateFunctionEventInvokeConfigResponseTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": ClientUpdateFunctionEventInvokeConfigResponseDestinationConfigTypeDef,
    },
    total=False,
)


class ClientUpdateFunctionEventInvokeConfigResponseTypeDef(
    _ClientUpdateFunctionEventInvokeConfigResponseTypeDef
):
    """
    - *(dict) --*

      - **LastModified** *(datetime) --*

        The date and time that the configuration was last updated.
    """


_FunctionActiveWaitWaiterConfigTypeDef = TypedDict(
    "_FunctionActiveWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class FunctionActiveWaitWaiterConfigTypeDef(_FunctionActiveWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5
    """


_FunctionExistsWaitWaiterConfigTypeDef = TypedDict(
    "_FunctionExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class FunctionExistsWaitWaiterConfigTypeDef(_FunctionExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 1
    """


_FunctionUpdatedWaitWaiterConfigTypeDef = TypedDict(
    "_FunctionUpdatedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class FunctionUpdatedWaitWaiterConfigTypeDef(_FunctionUpdatedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5
    """


_ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAliasesPaginatePaginationConfigTypeDef(_ListAliasesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAliasesPaginateResponseAliasesRoutingConfigTypeDef = TypedDict(
    "_ListAliasesPaginateResponseAliasesRoutingConfigTypeDef",
    {"AdditionalVersionWeights": Dict[str, float]},
    total=False,
)


class ListAliasesPaginateResponseAliasesRoutingConfigTypeDef(
    _ListAliasesPaginateResponseAliasesRoutingConfigTypeDef
):
    pass


_ListAliasesPaginateResponseAliasesTypeDef = TypedDict(
    "_ListAliasesPaginateResponseAliasesTypeDef",
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


class ListAliasesPaginateResponseAliasesTypeDef(_ListAliasesPaginateResponseAliasesTypeDef):
    """
    - *(dict) --*

      Provides configuration information about a Lambda function `alias
      <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .
      - **AliasArn** *(string) --*

        The Amazon Resource Name (ARN) of the alias.
    """


_ListAliasesPaginateResponseTypeDef = TypedDict(
    "_ListAliasesPaginateResponseTypeDef",
    {"Aliases": List[ListAliasesPaginateResponseAliasesTypeDef], "NextToken": str},
    total=False,
)


class ListAliasesPaginateResponseTypeDef(_ListAliasesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Aliases** *(list) --*

        A list of aliases.
        - *(dict) --*

          Provides configuration information about a Lambda function `alias
          <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .
          - **AliasArn** *(string) --*

            The Amazon Resource Name (ARN) of the alias.
    """


_ListEventSourceMappingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEventSourceMappingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEventSourceMappingsPaginatePaginationConfigTypeDef(
    _ListEventSourceMappingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnFailureTypeDef = TypedDict(
    "_ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnFailureTypeDef(
    _ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnFailureTypeDef
):
    pass


_ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef(
    _ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef
):
    pass


_ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigTypeDef = TypedDict(
    "_ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigTypeDef",
    {
        "OnSuccess": ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnSuccessTypeDef,
        "OnFailure": ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigTypeDef(
    _ListEventSourceMappingsPaginateResponseEventSourceMappingsDestinationConfigTypeDef
):
    pass


_ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef = TypedDict(
    "_ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef",
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


class ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef(
    _ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef
):
    """
    - *(dict) --*

      A mapping between an AWS resource and an AWS Lambda function. See  CreateEventSourceMapping
      for details.
      - **UUID** *(string) --*

        The identifier of the event source mapping.
    """


_ListEventSourceMappingsPaginateResponseTypeDef = TypedDict(
    "_ListEventSourceMappingsPaginateResponseTypeDef",
    {
        "EventSourceMappings": List[
            ListEventSourceMappingsPaginateResponseEventSourceMappingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListEventSourceMappingsPaginateResponseTypeDef(
    _ListEventSourceMappingsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **EventSourceMappings** *(list) --*

        A list of event source mappings.
        - *(dict) --*

          A mapping between an AWS resource and an AWS Lambda function. See
          CreateEventSourceMapping for details.
          - **UUID** *(string) --*

            The identifier of the event source mapping.
    """


_ListFunctionEventInvokeConfigsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFunctionEventInvokeConfigsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFunctionEventInvokeConfigsPaginatePaginationConfigTypeDef(
    _ListFunctionEventInvokeConfigsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef = TypedDict(
    "_ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef",
    {"Destination": str},
    total=False,
)


class ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef(
    _ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef
):
    pass


_ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef = TypedDict(
    "_ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef",
    {"Destination": str},
    total=False,
)


class ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef(
    _ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef
):
    pass


_ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigTypeDef = TypedDict(
    "_ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigTypeDef",
    {
        "OnSuccess": ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnSuccessTypeDef,
        "OnFailure": ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigOnFailureTypeDef,
    },
    total=False,
)


class ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigTypeDef(
    _ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigTypeDef
):
    pass


_ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsTypeDef = TypedDict(
    "_ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsDestinationConfigTypeDef,
    },
    total=False,
)


class ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsTypeDef(
    _ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsTypeDef
):
    """
    - *(dict) --*

      - **LastModified** *(datetime) --*

        The date and time that the configuration was last updated.
    """


_ListFunctionEventInvokeConfigsPaginateResponseTypeDef = TypedDict(
    "_ListFunctionEventInvokeConfigsPaginateResponseTypeDef",
    {
        "FunctionEventInvokeConfigs": List[
            ListFunctionEventInvokeConfigsPaginateResponseFunctionEventInvokeConfigsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListFunctionEventInvokeConfigsPaginateResponseTypeDef(
    _ListFunctionEventInvokeConfigsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **FunctionEventInvokeConfigs** *(list) --*

        A list of configurations.
        - *(dict) --*

          - **LastModified** *(datetime) --*

            The date and time that the configuration was last updated.
    """


_ListFunctionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFunctionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFunctionsPaginatePaginationConfigTypeDef(_ListFunctionsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef(
    _ListFunctionsPaginateResponseFunctionsDeadLetterConfigTypeDef
):
    pass


_ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef(
    _ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef
):
    pass


_ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ListFunctionsPaginateResponseFunctionsEnvironmentErrorTypeDef,
    },
    total=False,
)


class ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef(
    _ListFunctionsPaginateResponseFunctionsEnvironmentTypeDef
):
    pass


_ListFunctionsPaginateResponseFunctionsLayersTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ListFunctionsPaginateResponseFunctionsLayersTypeDef(
    _ListFunctionsPaginateResponseFunctionsLayersTypeDef
):
    pass


_ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef(
    _ListFunctionsPaginateResponseFunctionsTracingConfigTypeDef
):
    pass


_ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef(
    _ListFunctionsPaginateResponseFunctionsVpcConfigTypeDef
):
    pass


_ListFunctionsPaginateResponseFunctionsTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseFunctionsTypeDef",
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


class ListFunctionsPaginateResponseFunctionsTypeDef(_ListFunctionsPaginateResponseFunctionsTypeDef):
    """
    - *(dict) --*

      Details about a function's configuration.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_ListFunctionsPaginateResponseTypeDef = TypedDict(
    "_ListFunctionsPaginateResponseTypeDef",
    {"Functions": List[ListFunctionsPaginateResponseFunctionsTypeDef], "NextToken": str},
    total=False,
)


class ListFunctionsPaginateResponseTypeDef(_ListFunctionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      A list of Lambda functions.
      - **Functions** *(list) --*

        A list of Lambda functions.
        - *(dict) --*

          Details about a function's configuration.
          - **FunctionName** *(string) --*

            The name of the function.
    """


_ListLayerVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLayerVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLayerVersionsPaginatePaginationConfigTypeDef(
    _ListLayerVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLayerVersionsPaginateResponseLayerVersionsTypeDef = TypedDict(
    "_ListLayerVersionsPaginateResponseLayerVersionsTypeDef",
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


class ListLayerVersionsPaginateResponseLayerVersionsTypeDef(
    _ListLayerVersionsPaginateResponseLayerVersionsTypeDef
):
    """
    - *(dict) --*

      Details about a version of an `AWS Lambda layer
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .
      - **LayerVersionArn** *(string) --*

        The ARN of the layer version.
    """


_ListLayerVersionsPaginateResponseTypeDef = TypedDict(
    "_ListLayerVersionsPaginateResponseTypeDef",
    {
        "LayerVersions": List[ListLayerVersionsPaginateResponseLayerVersionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListLayerVersionsPaginateResponseTypeDef(_ListLayerVersionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **LayerVersions** *(list) --*

        A list of versions.
        - *(dict) --*

          Details about a version of an `AWS Lambda layer
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .
          - **LayerVersionArn** *(string) --*

            The ARN of the layer version.
    """


_ListLayersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLayersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLayersPaginatePaginationConfigTypeDef(_ListLayersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef = TypedDict(
    "_ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef",
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


class ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef(
    _ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef
):
    pass


_ListLayersPaginateResponseLayersTypeDef = TypedDict(
    "_ListLayersPaginateResponseLayersTypeDef",
    {
        "LayerName": str,
        "LayerArn": str,
        "LatestMatchingVersion": ListLayersPaginateResponseLayersLatestMatchingVersionTypeDef,
    },
    total=False,
)


class ListLayersPaginateResponseLayersTypeDef(_ListLayersPaginateResponseLayersTypeDef):
    """
    - *(dict) --*

      Details about an `AWS Lambda layer
      <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .
      - **LayerName** *(string) --*

        The name of the layer.
    """


_ListLayersPaginateResponseTypeDef = TypedDict(
    "_ListLayersPaginateResponseTypeDef",
    {"Layers": List[ListLayersPaginateResponseLayersTypeDef], "NextToken": str},
    total=False,
)


class ListLayersPaginateResponseTypeDef(_ListLayersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Layers** *(list) --*

        A list of function layers.
        - *(dict) --*

          Details about an `AWS Lambda layer
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .
          - **LayerName** *(string) --*

            The name of the layer.
    """


_ListVersionsByFunctionPaginatePaginationConfigTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListVersionsByFunctionPaginatePaginationConfigTypeDef(
    _ListVersionsByFunctionPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef",
    {"TargetArn": str},
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsDeadLetterConfigTypeDef
):
    pass


_ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef",
    {"ErrorCode": str, "Message": str},
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef
):
    pass


_ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": ListVersionsByFunctionPaginateResponseVersionsEnvironmentErrorTypeDef,
    },
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsEnvironmentTypeDef
):
    pass


_ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef",
    {"Arn": str, "CodeSize": int},
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsLayersTypeDef
):
    pass


_ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef",
    {"Mode": Literal["Active", "PassThrough"]},
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsTracingConfigTypeDef
):
    pass


_ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)


class ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsVpcConfigTypeDef
):
    pass


_ListVersionsByFunctionPaginateResponseVersionsTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseVersionsTypeDef",
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


class ListVersionsByFunctionPaginateResponseVersionsTypeDef(
    _ListVersionsByFunctionPaginateResponseVersionsTypeDef
):
    """
    - *(dict) --*

      Details about a function's configuration.
      - **FunctionName** *(string) --*

        The name of the function.
    """


_ListVersionsByFunctionPaginateResponseTypeDef = TypedDict(
    "_ListVersionsByFunctionPaginateResponseTypeDef",
    {"Versions": List[ListVersionsByFunctionPaginateResponseVersionsTypeDef], "NextToken": str},
    total=False,
)


class ListVersionsByFunctionPaginateResponseTypeDef(_ListVersionsByFunctionPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Versions** *(list) --*

        A list of Lambda function versions.
        - *(dict) --*

          Details about a function's configuration.
          - **FunctionName** *(string) --*

            The name of the function.
    """
