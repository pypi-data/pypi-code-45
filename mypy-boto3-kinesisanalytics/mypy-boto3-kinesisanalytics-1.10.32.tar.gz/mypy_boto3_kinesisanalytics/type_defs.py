"Main interface for kinesisanalytics service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef",
    "ClientAddApplicationInputInputInputParallelismTypeDef",
    "ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientAddApplicationInputInputInputProcessingConfigurationTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef",
    "ClientAddApplicationInputInputInputSchemaTypeDef",
    "ClientAddApplicationInputInputKinesisFirehoseInputTypeDef",
    "ClientAddApplicationInputInputKinesisStreamsInputTypeDef",
    "ClientAddApplicationInputInputTypeDef",
    "ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef",
    "ClientAddApplicationOutputOutputDestinationSchemaTypeDef",
    "ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef",
    "ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef",
    "ClientAddApplicationOutputOutputLambdaOutputTypeDef",
    "ClientAddApplicationOutputOutputTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef",
    "ClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef",
    "ClientCreateApplicationCloudWatchLoggingOptionsTypeDef",
    "ClientCreateApplicationInputsInputParallelismTypeDef",
    "ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientCreateApplicationInputsInputProcessingConfigurationTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef",
    "ClientCreateApplicationInputsInputSchemaTypeDef",
    "ClientCreateApplicationInputsKinesisFirehoseInputTypeDef",
    "ClientCreateApplicationInputsKinesisStreamsInputTypeDef",
    "ClientCreateApplicationInputsTypeDef",
    "ClientCreateApplicationOutputsDestinationSchemaTypeDef",
    "ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef",
    "ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef",
    "ClientCreateApplicationOutputsLambdaOutputTypeDef",
    "ClientCreateApplicationOutputsTypeDef",
    "ClientCreateApplicationResponseApplicationSummaryTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationTagsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef",
    "ClientDescribeApplicationResponseApplicationDetailTypeDef",
    "ClientDescribeApplicationResponseTypeDef",
    "ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef",
    "ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef",
    "ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef",
    "ClientDiscoverInputSchemaResponseInputSchemaTypeDef",
    "ClientDiscoverInputSchemaResponseTypeDef",
    "ClientDiscoverInputSchemaS3ConfigurationTypeDef",
    "ClientListApplicationsResponseApplicationSummariesTypeDef",
    "ClientListApplicationsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef",
    "ClientStartApplicationInputConfigurationsTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef",
    "ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef",
    "ClientUpdateApplicationApplicationUpdateTypeDef",
)


_RequiredClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef = TypedDict(
    "_RequiredClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef",
    {"LogStreamARN": str},
)
_OptionalClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef = TypedDict(
    "_OptionalClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef",
    {"RoleARN": str},
    total=False,
)


class ClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef(
    _RequiredClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef,
    _OptionalClientAddApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionTypeDef,
):
    """
    Provides the CloudWatch log stream Amazon Resource Name (ARN) and the IAM role ARN. Note: To
    write application messages to CloudWatch, the IAM role that is used must have the
    ``PutLogEvents`` policy action enabled.
    - **LogStreamARN** *(string) --***[REQUIRED]**

      ARN of the CloudWatch log to receive application messages.
    """


_ClientAddApplicationInputInputInputParallelismTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputParallelismTypeDef", {"Count": int}, total=False
)


class ClientAddApplicationInputInputInputParallelismTypeDef(
    _ClientAddApplicationInputInputInputParallelismTypeDef
):
    pass


_ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef
):
    pass


_ClientAddApplicationInputInputInputProcessingConfigurationTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientAddApplicationInputInputInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
    total=False,
)


class ClientAddApplicationInputInputInputProcessingConfigurationTypeDef(
    _ClientAddApplicationInputInputInputProcessingConfigurationTypeDef
):
    pass


_ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef(
    _ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef
):
    pass


_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    pass


_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    pass


_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef
):
    pass


_ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientAddApplicationInputInputInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef(
    _ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef
):
    pass


_ClientAddApplicationInputInputInputSchemaTypeDef = TypedDict(
    "_ClientAddApplicationInputInputInputSchemaTypeDef",
    {
        "RecordFormat": ClientAddApplicationInputInputInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[ClientAddApplicationInputInputInputSchemaRecordColumnsTypeDef],
    },
    total=False,
)


class ClientAddApplicationInputInputInputSchemaTypeDef(
    _ClientAddApplicationInputInputInputSchemaTypeDef
):
    pass


_ClientAddApplicationInputInputKinesisFirehoseInputTypeDef = TypedDict(
    "_ClientAddApplicationInputInputKinesisFirehoseInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationInputInputKinesisFirehoseInputTypeDef(
    _ClientAddApplicationInputInputKinesisFirehoseInputTypeDef
):
    pass


_ClientAddApplicationInputInputKinesisStreamsInputTypeDef = TypedDict(
    "_ClientAddApplicationInputInputKinesisStreamsInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationInputInputKinesisStreamsInputTypeDef(
    _ClientAddApplicationInputInputKinesisStreamsInputTypeDef
):
    pass


_RequiredClientAddApplicationInputInputTypeDef = TypedDict(
    "_RequiredClientAddApplicationInputInputTypeDef", {"NamePrefix": str}
)
_OptionalClientAddApplicationInputInputTypeDef = TypedDict(
    "_OptionalClientAddApplicationInputInputTypeDef",
    {
        "InputProcessingConfiguration": ClientAddApplicationInputInputInputProcessingConfigurationTypeDef,
        "KinesisStreamsInput": ClientAddApplicationInputInputKinesisStreamsInputTypeDef,
        "KinesisFirehoseInput": ClientAddApplicationInputInputKinesisFirehoseInputTypeDef,
        "InputParallelism": ClientAddApplicationInputInputInputParallelismTypeDef,
        "InputSchema": ClientAddApplicationInputInputInputSchemaTypeDef,
    },
    total=False,
)


class ClientAddApplicationInputInputTypeDef(
    _RequiredClientAddApplicationInputInputTypeDef, _OptionalClientAddApplicationInputInputTypeDef
):
    """
    The `Input <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_Input.html>`__ to add.
    - **NamePrefix** *(string) --***[REQUIRED]**

      Name prefix to use when creating an in-application stream. Suppose that you specify a prefix
      "MyInApplicationStream." Amazon Kinesis Analytics then creates one or more (as per the
      ``InputParallelism`` count you specified) in-application streams with names
      "MyInApplicationStream_001," "MyInApplicationStream_002," and so on.
    """


_RequiredClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_RequiredClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str},
)
_OptionalClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_OptionalClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"RoleARN": str},
    total=False,
)


class ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _RequiredClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef,
    _OptionalClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef,
):
    """
    - **InputLambdaProcessor** *(dict) --***[REQUIRED]**

      The `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
      that is used to preprocess the records in the stream before being processed by your
      application code.
      - **ResourceARN** *(string) --***[REQUIRED]**

        The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates
        on records in the stream.
        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef = TypedDict(
    "_ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
)


class ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef(
    _ClientAddApplicationInputProcessingConfigurationInputProcessingConfigurationTypeDef
):
    """
    The `InputProcessingConfiguration
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html>`__
    to add to the application.
    - **InputLambdaProcessor** *(dict) --***[REQUIRED]**

      The `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
      that is used to preprocess the records in the stream before being processed by your
      application code.
      - **ResourceARN** *(string) --***[REQUIRED]**

        The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates
        on records in the stream.
        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_ClientAddApplicationOutputOutputDestinationSchemaTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputDestinationSchemaTypeDef",
    {"RecordFormatType": Literal["JSON", "CSV"]},
    total=False,
)


class ClientAddApplicationOutputOutputDestinationSchemaTypeDef(
    _ClientAddApplicationOutputOutputDestinationSchemaTypeDef
):
    pass


_ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef(
    _ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef
):
    pass


_ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef(
    _ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef
):
    pass


_ClientAddApplicationOutputOutputLambdaOutputTypeDef = TypedDict(
    "_ClientAddApplicationOutputOutputLambdaOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientAddApplicationOutputOutputLambdaOutputTypeDef(
    _ClientAddApplicationOutputOutputLambdaOutputTypeDef
):
    pass


_RequiredClientAddApplicationOutputOutputTypeDef = TypedDict(
    "_RequiredClientAddApplicationOutputOutputTypeDef", {"Name": str}
)
_OptionalClientAddApplicationOutputOutputTypeDef = TypedDict(
    "_OptionalClientAddApplicationOutputOutputTypeDef",
    {
        "KinesisStreamsOutput": ClientAddApplicationOutputOutputKinesisStreamsOutputTypeDef,
        "KinesisFirehoseOutput": ClientAddApplicationOutputOutputKinesisFirehoseOutputTypeDef,
        "LambdaOutput": ClientAddApplicationOutputOutputLambdaOutputTypeDef,
        "DestinationSchema": ClientAddApplicationOutputOutputDestinationSchemaTypeDef,
    },
    total=False,
)


class ClientAddApplicationOutputOutputTypeDef(
    _RequiredClientAddApplicationOutputOutputTypeDef,
    _OptionalClientAddApplicationOutputOutputTypeDef,
):
    """
    An array of objects, each describing one output configuration. In the output configuration, you
    specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream,
    an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), and record the formation
    to use when writing to the destination.
    - **Name** *(string) --***[REQUIRED]**

      Name of the in-application stream.
    """


_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef
):
    pass


_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    pass


_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    pass


_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef
):
    pass


_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef
):
    pass


_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef
):
    pass


_ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef = TypedDict(
    "_ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef",
    {"BucketARN": str, "FileKey": str, "ReferenceRoleARN": str},
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef(
    _ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef
):
    pass


_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef = TypedDict(
    "_RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef", {"TableName": str}
)
_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef = TypedDict(
    "_OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef",
    {
        "S3ReferenceDataSource": ClientAddApplicationReferenceDataSourceReferenceDataSourceS3ReferenceDataSourceTypeDef,
        "ReferenceSchema": ClientAddApplicationReferenceDataSourceReferenceDataSourceReferenceSchemaTypeDef,
    },
    total=False,
)


class ClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef(
    _RequiredClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef,
    _OptionalClientAddApplicationReferenceDataSourceReferenceDataSourceTypeDef,
):
    """
    The reference data source can be an object in your Amazon S3 bucket. Amazon Kinesis Analytics
    reads the object and copies the data into the in-application table that is created. You provide
    an S3 bucket, object key name, and the resulting in-application table that is created. You must
    also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume
    to read the object from your S3 bucket on your behalf.
    - **TableName** *(string) --***[REQUIRED]**

      Name of the in-application table to create.
    """


_RequiredClientCreateApplicationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationCloudWatchLoggingOptionsTypeDef", {"LogStreamARN": str}
)
_OptionalClientCreateApplicationCloudWatchLoggingOptionsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationCloudWatchLoggingOptionsTypeDef", {"RoleARN": str}, total=False
)


class ClientCreateApplicationCloudWatchLoggingOptionsTypeDef(
    _RequiredClientCreateApplicationCloudWatchLoggingOptionsTypeDef,
    _OptionalClientCreateApplicationCloudWatchLoggingOptionsTypeDef,
):
    """
    - *(dict) --*

      Provides a description of CloudWatch logging options, including the log stream Amazon Resource
      Name (ARN) and the role ARN.
      - **LogStreamARN** *(string) --***[REQUIRED]**

        ARN of the CloudWatch log to receive application messages.
    """


_ClientCreateApplicationInputsInputParallelismTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputParallelismTypeDef", {"Count": int}, total=False
)


class ClientCreateApplicationInputsInputParallelismTypeDef(
    _ClientCreateApplicationInputsInputParallelismTypeDef
):
    pass


_ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef
):
    pass


_ClientCreateApplicationInputsInputProcessingConfigurationTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientCreateApplicationInputsInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
    total=False,
)


class ClientCreateApplicationInputsInputProcessingConfigurationTypeDef(
    _ClientCreateApplicationInputsInputProcessingConfigurationTypeDef
):
    pass


_ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef(
    _ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef
):
    pass


_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    pass


_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    pass


_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef
):
    pass


_ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientCreateApplicationInputsInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef(
    _ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef
):
    pass


_ClientCreateApplicationInputsInputSchemaTypeDef = TypedDict(
    "_ClientCreateApplicationInputsInputSchemaTypeDef",
    {
        "RecordFormat": ClientCreateApplicationInputsInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[ClientCreateApplicationInputsInputSchemaRecordColumnsTypeDef],
    },
    total=False,
)


class ClientCreateApplicationInputsInputSchemaTypeDef(
    _ClientCreateApplicationInputsInputSchemaTypeDef
):
    pass


_ClientCreateApplicationInputsKinesisFirehoseInputTypeDef = TypedDict(
    "_ClientCreateApplicationInputsKinesisFirehoseInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationInputsKinesisFirehoseInputTypeDef(
    _ClientCreateApplicationInputsKinesisFirehoseInputTypeDef
):
    pass


_ClientCreateApplicationInputsKinesisStreamsInputTypeDef = TypedDict(
    "_ClientCreateApplicationInputsKinesisStreamsInputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationInputsKinesisStreamsInputTypeDef(
    _ClientCreateApplicationInputsKinesisStreamsInputTypeDef
):
    pass


_RequiredClientCreateApplicationInputsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationInputsTypeDef", {"NamePrefix": str}
)
_OptionalClientCreateApplicationInputsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationInputsTypeDef",
    {
        "InputProcessingConfiguration": ClientCreateApplicationInputsInputProcessingConfigurationTypeDef,
        "KinesisStreamsInput": ClientCreateApplicationInputsKinesisStreamsInputTypeDef,
        "KinesisFirehoseInput": ClientCreateApplicationInputsKinesisFirehoseInputTypeDef,
        "InputParallelism": ClientCreateApplicationInputsInputParallelismTypeDef,
        "InputSchema": ClientCreateApplicationInputsInputSchemaTypeDef,
    },
    total=False,
)


class ClientCreateApplicationInputsTypeDef(
    _RequiredClientCreateApplicationInputsTypeDef, _OptionalClientCreateApplicationInputsTypeDef
):
    """
    - *(dict) --*

      When you configure the application input, you specify the streaming source, the in-application
      stream name that is created, and the mapping between the two. For more information, see
      `Configuring Application Input
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`__ .
      - **NamePrefix** *(string) --***[REQUIRED]**

        Name prefix to use when creating an in-application stream. Suppose that you specify a prefix
        "MyInApplicationStream." Amazon Kinesis Analytics then creates one or more (as per the
        ``InputParallelism`` count you specified) in-application streams with names
        "MyInApplicationStream_001," "MyInApplicationStream_002," and so on.
    """


_ClientCreateApplicationOutputsDestinationSchemaTypeDef = TypedDict(
    "_ClientCreateApplicationOutputsDestinationSchemaTypeDef",
    {"RecordFormatType": Literal["JSON", "CSV"]},
    total=False,
)


class ClientCreateApplicationOutputsDestinationSchemaTypeDef(
    _ClientCreateApplicationOutputsDestinationSchemaTypeDef
):
    pass


_ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef = TypedDict(
    "_ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef(
    _ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef
):
    pass


_ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef = TypedDict(
    "_ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef(
    _ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef
):
    pass


_ClientCreateApplicationOutputsLambdaOutputTypeDef = TypedDict(
    "_ClientCreateApplicationOutputsLambdaOutputTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientCreateApplicationOutputsLambdaOutputTypeDef(
    _ClientCreateApplicationOutputsLambdaOutputTypeDef
):
    pass


_RequiredClientCreateApplicationOutputsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationOutputsTypeDef", {"Name": str}
)
_OptionalClientCreateApplicationOutputsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationOutputsTypeDef",
    {
        "KinesisStreamsOutput": ClientCreateApplicationOutputsKinesisStreamsOutputTypeDef,
        "KinesisFirehoseOutput": ClientCreateApplicationOutputsKinesisFirehoseOutputTypeDef,
        "LambdaOutput": ClientCreateApplicationOutputsLambdaOutputTypeDef,
        "DestinationSchema": ClientCreateApplicationOutputsDestinationSchemaTypeDef,
    },
    total=False,
)


class ClientCreateApplicationOutputsTypeDef(
    _RequiredClientCreateApplicationOutputsTypeDef, _OptionalClientCreateApplicationOutputsTypeDef
):
    """
    - *(dict) --*

      Describes application output configuration in which you identify an in-application stream and
      a destination where you want the in-application stream data to be written. The destination can
      be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.
      For limits on how many destinations an application can write and other limitations, see
      `Limits <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`__ .
      - **Name** *(string) --***[REQUIRED]**

        Name of the in-application stream.
    """


_ClientCreateApplicationResponseApplicationSummaryTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationSummaryTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": Literal[
            "DELETING", "STARTING", "STOPPING", "READY", "RUNNING", "UPDATING"
        ],
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationSummaryTypeDef(
    _ClientCreateApplicationResponseApplicationSummaryTypeDef
):
    """
    - **ApplicationSummary** *(dict) --*

      In response to your ``CreateApplication`` request, Amazon Kinesis Analytics returns a response
      with a summary of the application it created, including the application Amazon Resource Name
      (ARN), name, and status.
      - **ApplicationName** *(string) --*

        Name of the application.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef",
    {"ApplicationSummary": ClientCreateApplicationResponseApplicationSummaryTypeDef},
    total=False,
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    - *(dict) --*

      TBD
      - **ApplicationSummary** *(dict) --*

        In response to your ``CreateApplication`` request, Amazon Kinesis Analytics returns a
        response with a summary of the application it created, including the application Amazon
        Resource Name (ARN), name, and status.
        - **ApplicationName** *(string) --*

          Name of the application.
    """


_RequiredClientCreateApplicationTagsTypeDef = TypedDict(
    "_RequiredClientCreateApplicationTagsTypeDef", {"Key": str}
)
_OptionalClientCreateApplicationTagsTypeDef = TypedDict(
    "_OptionalClientCreateApplicationTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateApplicationTagsTypeDef(
    _RequiredClientCreateApplicationTagsTypeDef, _OptionalClientCreateApplicationTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair (the value is optional) that you can define and assign to AWS resources. If
      you specify a tag that already exists, the tag value is replaced with the value that you
      specify in the request. Note that the maximum number of application tags includes system tags.
      The maximum number of user-defined application tags is 50. For more information, see `Using
      Tagging <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html>`__ .
      - **Key** *(string) --***[REQUIRED]**

        The key of the key-value tag.
    """


_ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef",
    {"CloudWatchLoggingOptionId": str, "LogStreamARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef",
    {"Count": int},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionInputLambdaProcessorDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef",
    {
        "RecordFormat": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": Literal["NOW", "TRIM_HORIZON", "LAST_STOPPED_POINT"]},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef",
    {
        "InputId": str,
        "NamePrefix": str,
        "InAppStreamNames": List[str],
        "InputProcessingConfigurationDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputProcessingConfigurationDescriptionTypeDef,
        "KinesisStreamsInputDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisStreamsInputDescriptionTypeDef,
        "KinesisFirehoseInputDescription": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsKinesisFirehoseInputDescriptionTypeDef,
        "InputSchema": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputSchemaTypeDef,
        "InputParallelism": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputParallelismTypeDef,
        "InputStartingPositionConfiguration": ClientDescribeApplicationResponseApplicationDetailInputDescriptionsInputStartingPositionConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef",
    {"RecordFormatType": Literal["JSON", "CSV"]},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef",
    {"ResourceARN": str, "RoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef",
    {
        "OutputId": str,
        "Name": str,
        "KinesisStreamsOutputDescription": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisStreamsOutputDescriptionTypeDef,
        "KinesisFirehoseOutputDescription": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsKinesisFirehoseOutputDescriptionTypeDef,
        "LambdaOutputDescription": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsLambdaOutputDescriptionTypeDef,
        "DestinationSchema": ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsDestinationSchemaTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef",
    {
        "RecordFormat": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef",
    {"BucketARN": str, "FileKey": str, "ReferenceRoleARN": str},
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsS3ReferenceDataSourceDescriptionTypeDef,
        "ReferenceSchema": ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsReferenceSchemaTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef
):
    pass


_ClientDescribeApplicationResponseApplicationDetailTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseApplicationDetailTypeDef",
    {
        "ApplicationName": str,
        "ApplicationDescription": str,
        "ApplicationARN": str,
        "ApplicationStatus": Literal[
            "DELETING", "STARTING", "STOPPING", "READY", "RUNNING", "UPDATING"
        ],
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "InputDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailInputDescriptionsTypeDef
        ],
        "OutputDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailOutputDescriptionsTypeDef
        ],
        "ReferenceDataSourceDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailReferenceDataSourceDescriptionsTypeDef
        ],
        "CloudWatchLoggingOptionDescriptions": List[
            ClientDescribeApplicationResponseApplicationDetailCloudWatchLoggingOptionDescriptionsTypeDef
        ],
        "ApplicationCode": str,
        "ApplicationVersionId": int,
    },
    total=False,
)


class ClientDescribeApplicationResponseApplicationDetailTypeDef(
    _ClientDescribeApplicationResponseApplicationDetailTypeDef
):
    """
    - **ApplicationDetail** *(dict) --*

      Provides a description of the application, such as the application Amazon Resource Name (ARN),
      status, latest version, and input and output configuration details.
      - **ApplicationName** *(string) --*

        Name of the application.
    """


_ClientDescribeApplicationResponseTypeDef = TypedDict(
    "_ClientDescribeApplicationResponseTypeDef",
    {"ApplicationDetail": ClientDescribeApplicationResponseApplicationDetailTypeDef},
    total=False,
)


class ClientDescribeApplicationResponseTypeDef(_ClientDescribeApplicationResponseTypeDef):
    """
    - *(dict) --*

      - **ApplicationDetail** *(dict) --*

        Provides a description of the application, such as the application Amazon Resource Name
        (ARN), status, latest version, and input and output configuration details.
        - **ApplicationName** *(string) --*

          Name of the application.
    """


_RequiredClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_RequiredClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"ResourceARN": str},
)
_OptionalClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef = TypedDict(
    "_OptionalClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef",
    {"RoleARN": str},
    total=False,
)


class ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef(
    _RequiredClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef,
    _OptionalClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef,
):
    """
    - **InputLambdaProcessor** *(dict) --***[REQUIRED]**

      The `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
      that is used to preprocess the records in the stream before being processed by your
      application code.
      - **ResourceARN** *(string) --***[REQUIRED]**

        The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates
        on records in the stream.
        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": ClientDiscoverInputSchemaInputProcessingConfigurationInputLambdaProcessorTypeDef
    },
)


class ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef(
    _ClientDiscoverInputSchemaInputProcessingConfigurationTypeDef
):
    """
    The `InputProcessingConfiguration
    <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html>`__
    to use to preprocess the records before discovering the schema of the records.
    - **InputLambdaProcessor** *(dict) --***[REQUIRED]**

      The `InputLambdaProcessor
      <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessor.html>`__
      that is used to preprocess the records in the stream before being processed by your
      application code.
      - **ResourceARN** *(string) --***[REQUIRED]**

        The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`__ function that operates
        on records in the stream.
        .. note::

          To specify an earlier version of the Lambda function than the latest, include the Lambda
          function version in the Lambda function ARN. For more information about Lambda ARNs, see
          `Example ARNs\\: AWS Lambda
          </general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`__
    """


_ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": Literal["NOW", "TRIM_HORIZON", "LAST_STOPPED_POINT"]},
    total=False,
)


class ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef(
    _ClientDiscoverInputSchemaInputStartingPositionConfigurationTypeDef
):
    """
    Point at which you want Amazon Kinesis Analytics to start reading records from the specified
    streaming source discovery purposes.
    - **InputStartingPosition** *(string) --*

      The starting position on the stream.
      * ``NOW`` - Start reading just after the most recent record in the stream, start at the
      request time stamp that the customer issued.
      * ``TRIM_HORIZON`` - Start reading at the last untrimmed record in the stream, which is the
      oldest record available in the stream. This option is not available for an Amazon Kinesis
      Firehose delivery stream.
      * ``LAST_STOPPED_POINT`` - Resume reading from where the application last stopped reading.
    """


_ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef
):
    pass


_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    pass


_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    pass


_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef
):
    pass


_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef
):
    """
    - **RecordFormat** *(dict) --*

      Specifies the format of the records on the streaming source.
      - **RecordFormatType** *(string) --*

        The type of record format.
    """


_ClientDiscoverInputSchemaResponseInputSchemaTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseInputSchemaTypeDef",
    {
        "RecordFormat": ClientDiscoverInputSchemaResponseInputSchemaRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[ClientDiscoverInputSchemaResponseInputSchemaRecordColumnsTypeDef],
    },
    total=False,
)


class ClientDiscoverInputSchemaResponseInputSchemaTypeDef(
    _ClientDiscoverInputSchemaResponseInputSchemaTypeDef
):
    """
    - **InputSchema** *(dict) --*

      Schema inferred from the streaming source. It identifies the format of the data in the
      streaming source and how each data element maps to corresponding columns in the in-application
      stream that you can create.
      - **RecordFormat** *(dict) --*

        Specifies the format of the records on the streaming source.
        - **RecordFormatType** *(string) --*

          The type of record format.
    """


_ClientDiscoverInputSchemaResponseTypeDef = TypedDict(
    "_ClientDiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": ClientDiscoverInputSchemaResponseInputSchemaTypeDef,
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
    },
    total=False,
)


class ClientDiscoverInputSchemaResponseTypeDef(_ClientDiscoverInputSchemaResponseTypeDef):
    """
    - *(dict) --*

      - **InputSchema** *(dict) --*

        Schema inferred from the streaming source. It identifies the format of the data in the
        streaming source and how each data element maps to corresponding columns in the
        in-application stream that you can create.
        - **RecordFormat** *(dict) --*

          Specifies the format of the records on the streaming source.
          - **RecordFormatType** *(string) --*

            The type of record format.
    """


_RequiredClientDiscoverInputSchemaS3ConfigurationTypeDef = TypedDict(
    "_RequiredClientDiscoverInputSchemaS3ConfigurationTypeDef", {"RoleARN": str}
)
_OptionalClientDiscoverInputSchemaS3ConfigurationTypeDef = TypedDict(
    "_OptionalClientDiscoverInputSchemaS3ConfigurationTypeDef",
    {"BucketARN": str, "FileKey": str},
    total=False,
)


class ClientDiscoverInputSchemaS3ConfigurationTypeDef(
    _RequiredClientDiscoverInputSchemaS3ConfigurationTypeDef,
    _OptionalClientDiscoverInputSchemaS3ConfigurationTypeDef,
):
    """
    Specify this parameter to discover a schema from data in an Amazon S3 object.
    - **RoleARN** *(string) --***[REQUIRED]**

      IAM ARN of the role used to access the data.
    """


_ClientListApplicationsResponseApplicationSummariesTypeDef = TypedDict(
    "_ClientListApplicationsResponseApplicationSummariesTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": Literal[
            "DELETING", "STARTING", "STOPPING", "READY", "RUNNING", "UPDATING"
        ],
    },
    total=False,
)


class ClientListApplicationsResponseApplicationSummariesTypeDef(
    _ClientListApplicationsResponseApplicationSummariesTypeDef
):
    """
    - *(dict) --*

      .. note::

        This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only
        supports SQL applications. Version 2 of the API supports SQL and Java applications. For more
        information about version 2, see `Amazon Kinesis Data Analytics API V2 Documentation
        </kinesisanalytics/latest/apiv2/Welcome.html>`__ .
    """


_ClientListApplicationsResponseTypeDef = TypedDict(
    "_ClientListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List[ClientListApplicationsResponseApplicationSummariesTypeDef],
        "HasMoreApplications": bool,
    },
    total=False,
)


class ClientListApplicationsResponseTypeDef(_ClientListApplicationsResponseTypeDef):
    """
    - *(dict) --*

      - **ApplicationSummaries** *(list) --*

        List of ``ApplicationSummary`` objects.
        - *(dict) --*

          .. note::

            This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only
            supports SQL applications. Version 2 of the API supports SQL and Java applications. For
            more information about version 2, see `Amazon Kinesis Data Analytics API V2
            Documentation </kinesisanalytics/latest/apiv2/Welcome.html>`__ .
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      A key-value pair (the value is optional) that you can define and assign to AWS resources. If
      you specify a tag that already exists, the tag value is replaced with the value that you
      specify in the request. Note that the maximum number of application tags includes system tags.
      The maximum number of user-defined application tags is 50. For more information, see `Using
      Tagging <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html>`__ .
      - **Key** *(string) --*

        The key of the key-value tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The key-value tags assigned to the application.
        - *(dict) --*

          A key-value pair (the value is optional) that you can define and assign to AWS resources.
          If you specify a tag that already exists, the tag value is replaced with the value that
          you specify in the request. Note that the maximum number of application tags includes
          system tags. The maximum number of user-defined application tags is 50. For more
          information, see `Using Tagging
          <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html>`__ .
          - **Key** *(string) --*

            The key of the key-value tag.
    """


_ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef = TypedDict(
    "_ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef",
    {"InputStartingPosition": Literal["NOW", "TRIM_HORIZON", "LAST_STOPPED_POINT"]},
    total=False,
)


class ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef(
    _ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef
):
    pass


_RequiredClientStartApplicationInputConfigurationsTypeDef = TypedDict(
    "_RequiredClientStartApplicationInputConfigurationsTypeDef", {"Id": str}
)
_OptionalClientStartApplicationInputConfigurationsTypeDef = TypedDict(
    "_OptionalClientStartApplicationInputConfigurationsTypeDef",
    {
        "InputStartingPositionConfiguration": ClientStartApplicationInputConfigurationsInputStartingPositionConfigurationTypeDef
    },
    total=False,
)


class ClientStartApplicationInputConfigurationsTypeDef(
    _RequiredClientStartApplicationInputConfigurationsTypeDef,
    _OptionalClientStartApplicationInputConfigurationsTypeDef,
):
    """
    - *(dict) --*

      When you start your application, you provide this configuration, which identifies the input
      source and the point in the input source at which you want the application to start processing
      records.
      - **Id** *(string) --***[REQUIRED]**

        Input source ID. You can get this ID by calling the `DescribeApplication
        <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html>`__
        operation.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair (the value is optional) that you can define and assign to AWS resources. If
      you specify a tag that already exists, the tag value is replaced with the value that you
      specify in the request. Note that the maximum number of application tags includes system tags.
      The maximum number of user-defined application tags is 50. For more information, see `Using
      Tagging <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html>`__ .
      - **Key** *(string) --***[REQUIRED]**

        The key of the key-value tag.
    """


_ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef",
    {"CloudWatchLoggingOptionId": str, "LogStreamARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef(
    _ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef",
    {"CountUpdate": int},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateInputLambdaProcessorUpdateTypeDef
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordFormatUpdateTypeDef,
        "RecordEncodingUpdate": str,
        "RecordColumnUpdates": List[
            ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateRecordColumnUpdatesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef
):
    pass


_RequiredClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef", {"InputId": str}
)
_OptionalClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef",
    {
        "NamePrefixUpdate": str,
        "InputProcessingConfigurationUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputProcessingConfigurationUpdateTypeDef,
        "KinesisStreamsInputUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisStreamsInputUpdateTypeDef,
        "KinesisFirehoseInputUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesKinesisFirehoseInputUpdateTypeDef,
        "InputSchemaUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputSchemaUpdateTypeDef,
        "InputParallelismUpdate": ClientUpdateApplicationApplicationUpdateInputUpdatesInputParallelismUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef(
    _RequiredClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef,
    _OptionalClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef,
):
    """
    - *(dict) --*

      Describes updates to a specific input configuration (identified by the ``InputId`` of an
      application).
      - **InputId** *(string) --***[REQUIRED]**

        Input ID of the application input to be updated.
    """


_ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef",
    {"RecordFormatType": Literal["JSON", "CSV"]},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef",
    {"ResourceARNUpdate": str, "RoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef",
    {
        "OutputId": str,
        "NameUpdate": str,
        "KinesisStreamsOutputUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisStreamsOutputUpdateTypeDef,
        "KinesisFirehoseOutputUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesKinesisFirehoseOutputUpdateTypeDef,
        "LambdaOutputUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesLambdaOutputUpdateTypeDef,
        "DestinationSchemaUpdate": ClientUpdateApplicationApplicationUpdateOutputUpdatesDestinationSchemaUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef(
    _ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef",
    {"Name": str, "Mapping": str, "SqlType": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef",
    {"RecordRowDelimiter": str, "RecordColumnDelimiter": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef",
    {"RecordRowPath": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef",
    {
        "JSONMappingParameters": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersJSONMappingParametersTypeDef,
        "CSVMappingParameters": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersCSVMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef",
    {
        "RecordFormatType": Literal["JSON", "CSV"],
        "MappingParameters": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatMappingParametersTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef",
    {
        "RecordFormat": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordFormatTypeDef,
        "RecordEncoding": str,
        "RecordColumns": List[
            ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateRecordColumnsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef",
    {"BucketARNUpdate": str, "FileKeyUpdate": str, "ReferenceRoleARNUpdate": str},
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef",
    {
        "ReferenceId": str,
        "TableNameUpdate": str,
        "S3ReferenceDataSourceUpdate": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesS3ReferenceDataSourceUpdateTypeDef,
        "ReferenceSchemaUpdate": ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesReferenceSchemaUpdateTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef(
    _ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef
):
    pass


_ClientUpdateApplicationApplicationUpdateTypeDef = TypedDict(
    "_ClientUpdateApplicationApplicationUpdateTypeDef",
    {
        "InputUpdates": List[ClientUpdateApplicationApplicationUpdateInputUpdatesTypeDef],
        "ApplicationCodeUpdate": str,
        "OutputUpdates": List[ClientUpdateApplicationApplicationUpdateOutputUpdatesTypeDef],
        "ReferenceDataSourceUpdates": List[
            ClientUpdateApplicationApplicationUpdateReferenceDataSourceUpdatesTypeDef
        ],
        "CloudWatchLoggingOptionUpdates": List[
            ClientUpdateApplicationApplicationUpdateCloudWatchLoggingOptionUpdatesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateApplicationApplicationUpdateTypeDef(
    _ClientUpdateApplicationApplicationUpdateTypeDef
):
    """
    Describes application updates.
    - **InputUpdates** *(list) --*

      Describes application input configuration updates.
      - *(dict) --*

        Describes updates to a specific input configuration (identified by the ``InputId`` of an
        application).
        - **InputId** *(string) --***[REQUIRED]**

          Input ID of the application input to be updated.
    """
