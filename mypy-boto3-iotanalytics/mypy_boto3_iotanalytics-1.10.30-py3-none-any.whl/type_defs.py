"Main interface for iotanalytics service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchPutMessageMessagesTypeDef",
    "ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef",
    "ClientBatchPutMessageResponseTypeDef",
    "ClientCreateChannelChannelStoragecustomerManagedS3TypeDef",
    "ClientCreateChannelChannelStorageTypeDef",
    "ClientCreateChannelResponseretentionPeriodTypeDef",
    "ClientCreateChannelResponseTypeDef",
    "ClientCreateChannelRetentionPeriodTypeDef",
    "ClientCreateChannelTagsTypeDef",
    "ClientCreateDatasetActionscontainerActionresourceConfigurationTypeDef",
    "ClientCreateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    "ClientCreateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef",
    "ClientCreateDatasetActionscontainerActionvariablesTypeDef",
    "ClientCreateDatasetActionscontainerActionTypeDef",
    "ClientCreateDatasetActionsqueryActionfiltersdeltaTimeTypeDef",
    "ClientCreateDatasetActionsqueryActionfiltersTypeDef",
    "ClientCreateDatasetActionsqueryActionTypeDef",
    "ClientCreateDatasetActionsTypeDef",
    "ClientCreateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    "ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    "ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    "ClientCreateDatasetContentDeliveryRulesdestinationTypeDef",
    "ClientCreateDatasetContentDeliveryRulesTypeDef",
    "ClientCreateDatasetContentResponseTypeDef",
    "ClientCreateDatasetResponseretentionPeriodTypeDef",
    "ClientCreateDatasetResponseTypeDef",
    "ClientCreateDatasetRetentionPeriodTypeDef",
    "ClientCreateDatasetTagsTypeDef",
    "ClientCreateDatasetTriggersdatasetTypeDef",
    "ClientCreateDatasetTriggersscheduleTypeDef",
    "ClientCreateDatasetTriggersTypeDef",
    "ClientCreateDatasetVersioningConfigurationTypeDef",
    "ClientCreateDatastoreDatastoreStoragecustomerManagedS3TypeDef",
    "ClientCreateDatastoreDatastoreStorageTypeDef",
    "ClientCreateDatastoreResponseretentionPeriodTypeDef",
    "ClientCreateDatastoreResponseTypeDef",
    "ClientCreateDatastoreRetentionPeriodTypeDef",
    "ClientCreateDatastoreTagsTypeDef",
    "ClientCreatePipelinePipelineActivitiesaddAttributesTypeDef",
    "ClientCreatePipelinePipelineActivitieschannelTypeDef",
    "ClientCreatePipelinePipelineActivitiesdatastoreTypeDef",
    "ClientCreatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef",
    "ClientCreatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef",
    "ClientCreatePipelinePipelineActivitiesfilterTypeDef",
    "ClientCreatePipelinePipelineActivitieslambdaTypeDef",
    "ClientCreatePipelinePipelineActivitiesmathTypeDef",
    "ClientCreatePipelinePipelineActivitiesremoveAttributesTypeDef",
    "ClientCreatePipelinePipelineActivitiesselectAttributesTypeDef",
    "ClientCreatePipelinePipelineActivitiesTypeDef",
    "ClientCreatePipelineResponseTypeDef",
    "ClientCreatePipelineTagsTypeDef",
    "ClientDescribeChannelResponsechannelretentionPeriodTypeDef",
    "ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef",
    "ClientDescribeChannelResponsechannelstorageTypeDef",
    "ClientDescribeChannelResponsechannelTypeDef",
    "ClientDescribeChannelResponsestatisticssizeTypeDef",
    "ClientDescribeChannelResponsestatisticsTypeDef",
    "ClientDescribeChannelResponseTypeDef",
    "ClientDescribeDatasetResponsedatasetactionscontainerActionresourceConfigurationTypeDef",
    "ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    "ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesoutputFileUriValueTypeDef",
    "ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesTypeDef",
    "ClientDescribeDatasetResponsedatasetactionscontainerActionTypeDef",
    "ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersdeltaTimeTypeDef",
    "ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersTypeDef",
    "ClientDescribeDatasetResponsedatasetactionsqueryActionTypeDef",
    "ClientDescribeDatasetResponsedatasetactionsTypeDef",
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationTypeDef",
    "ClientDescribeDatasetResponsedatasetcontentDeliveryRulesTypeDef",
    "ClientDescribeDatasetResponsedatasetretentionPeriodTypeDef",
    "ClientDescribeDatasetResponsedatasettriggersdatasetTypeDef",
    "ClientDescribeDatasetResponsedatasettriggersscheduleTypeDef",
    "ClientDescribeDatasetResponsedatasettriggersTypeDef",
    "ClientDescribeDatasetResponsedatasetversioningConfigurationTypeDef",
    "ClientDescribeDatasetResponsedatasetTypeDef",
    "ClientDescribeDatasetResponseTypeDef",
    "ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef",
    "ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef",
    "ClientDescribeDatastoreResponsedatastorestorageTypeDef",
    "ClientDescribeDatastoreResponsedatastoreTypeDef",
    "ClientDescribeDatastoreResponsestatisticssizeTypeDef",
    "ClientDescribeDatastoreResponsestatisticsTypeDef",
    "ClientDescribeDatastoreResponseTypeDef",
    "ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    "ClientDescribeLoggingOptionsResponseTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef",
    "ClientDescribePipelineResponsepipelineactivitieschannelTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef",
    "ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesmathTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef",
    "ClientDescribePipelineResponsepipelineactivitiesTypeDef",
    "ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef",
    "ClientDescribePipelineResponsepipelineTypeDef",
    "ClientDescribePipelineResponseTypeDef",
    "ClientGetDatasetContentResponseentriesTypeDef",
    "ClientGetDatasetContentResponsestatusTypeDef",
    "ClientGetDatasetContentResponseTypeDef",
    "ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef",
    "ClientListChannelsResponsechannelSummarieschannelStorageTypeDef",
    "ClientListChannelsResponsechannelSummariesTypeDef",
    "ClientListChannelsResponseTypeDef",
    "ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef",
    "ClientListDatasetContentsResponsedatasetContentSummariesTypeDef",
    "ClientListDatasetContentsResponseTypeDef",
    "ClientListDatasetsResponsedatasetSummariesactionsTypeDef",
    "ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef",
    "ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef",
    "ClientListDatasetsResponsedatasetSummariestriggersTypeDef",
    "ClientListDatasetsResponsedatasetSummariesTypeDef",
    "ClientListDatasetsResponseTypeDef",
    "ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef",
    "ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef",
    "ClientListDatastoresResponsedatastoreSummariesTypeDef",
    "ClientListDatastoresResponseTypeDef",
    "ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef",
    "ClientListPipelinesResponsepipelineSummariesTypeDef",
    "ClientListPipelinesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutLoggingOptionsLoggingOptionsTypeDef",
    "ClientRunPipelineActivityPipelineActivityaddAttributesTypeDef",
    "ClientRunPipelineActivityPipelineActivitychannelTypeDef",
    "ClientRunPipelineActivityPipelineActivitydatastoreTypeDef",
    "ClientRunPipelineActivityPipelineActivitydeviceRegistryEnrichTypeDef",
    "ClientRunPipelineActivityPipelineActivitydeviceShadowEnrichTypeDef",
    "ClientRunPipelineActivityPipelineActivityfilterTypeDef",
    "ClientRunPipelineActivityPipelineActivitylambdaTypeDef",
    "ClientRunPipelineActivityPipelineActivitymathTypeDef",
    "ClientRunPipelineActivityPipelineActivityremoveAttributesTypeDef",
    "ClientRunPipelineActivityPipelineActivityselectAttributesTypeDef",
    "ClientRunPipelineActivityPipelineActivityTypeDef",
    "ClientRunPipelineActivityResponseTypeDef",
    "ClientSampleChannelDataResponseTypeDef",
    "ClientStartPipelineReprocessingResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateChannelChannelStoragecustomerManagedS3TypeDef",
    "ClientUpdateChannelChannelStorageTypeDef",
    "ClientUpdateChannelRetentionPeriodTypeDef",
    "ClientUpdateDatasetActionscontainerActionresourceConfigurationTypeDef",
    "ClientUpdateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    "ClientUpdateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef",
    "ClientUpdateDatasetActionscontainerActionvariablesTypeDef",
    "ClientUpdateDatasetActionscontainerActionTypeDef",
    "ClientUpdateDatasetActionsqueryActionfiltersdeltaTimeTypeDef",
    "ClientUpdateDatasetActionsqueryActionfiltersTypeDef",
    "ClientUpdateDatasetActionsqueryActionTypeDef",
    "ClientUpdateDatasetActionsTypeDef",
    "ClientUpdateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    "ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    "ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    "ClientUpdateDatasetContentDeliveryRulesdestinationTypeDef",
    "ClientUpdateDatasetContentDeliveryRulesTypeDef",
    "ClientUpdateDatasetRetentionPeriodTypeDef",
    "ClientUpdateDatasetTriggersdatasetTypeDef",
    "ClientUpdateDatasetTriggersscheduleTypeDef",
    "ClientUpdateDatasetTriggersTypeDef",
    "ClientUpdateDatasetVersioningConfigurationTypeDef",
    "ClientUpdateDatastoreDatastoreStoragecustomerManagedS3TypeDef",
    "ClientUpdateDatastoreDatastoreStorageTypeDef",
    "ClientUpdateDatastoreRetentionPeriodTypeDef",
    "ClientUpdatePipelinePipelineActivitiesaddAttributesTypeDef",
    "ClientUpdatePipelinePipelineActivitieschannelTypeDef",
    "ClientUpdatePipelinePipelineActivitiesdatastoreTypeDef",
    "ClientUpdatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef",
    "ClientUpdatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef",
    "ClientUpdatePipelinePipelineActivitiesfilterTypeDef",
    "ClientUpdatePipelinePipelineActivitieslambdaTypeDef",
    "ClientUpdatePipelinePipelineActivitiesmathTypeDef",
    "ClientUpdatePipelinePipelineActivitiesremoveAttributesTypeDef",
    "ClientUpdatePipelinePipelineActivitiesselectAttributesTypeDef",
    "ClientUpdatePipelinePipelineActivitiesTypeDef",
    "ListChannelsPaginatePaginationConfigTypeDef",
    "ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef",
    "ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef",
    "ListChannelsPaginateResponsechannelSummariesTypeDef",
    "ListChannelsPaginateResponseTypeDef",
    "ListDatasetContentsPaginatePaginationConfigTypeDef",
    "ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef",
    "ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef",
    "ListDatasetContentsPaginateResponseTypeDef",
    "ListDatasetsPaginatePaginationConfigTypeDef",
    "ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef",
    "ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef",
    "ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef",
    "ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef",
    "ListDatasetsPaginateResponsedatasetSummariesTypeDef",
    "ListDatasetsPaginateResponseTypeDef",
    "ListDatastoresPaginatePaginationConfigTypeDef",
    "ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef",
    "ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef",
    "ListDatastoresPaginateResponsedatastoreSummariesTypeDef",
    "ListDatastoresPaginateResponseTypeDef",
    "ListPipelinesPaginatePaginationConfigTypeDef",
    "ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef",
    "ListPipelinesPaginateResponsepipelineSummariesTypeDef",
    "ListPipelinesPaginateResponseTypeDef",
)


_RequiredClientBatchPutMessageMessagesTypeDef = TypedDict(
    "_RequiredClientBatchPutMessageMessagesTypeDef", {"messageId": str}
)
_OptionalClientBatchPutMessageMessagesTypeDef = TypedDict(
    "_OptionalClientBatchPutMessageMessagesTypeDef", {"payload": bytes}, total=False
)


class ClientBatchPutMessageMessagesTypeDef(
    _RequiredClientBatchPutMessageMessagesTypeDef, _OptionalClientBatchPutMessageMessagesTypeDef
):
    """
    - *(dict) --*

      Information about a message.
      - **messageId** *(string) --***[REQUIRED]**

        The ID you wish to assign to the message. Each "messageId" must be unique within each batch
        sent.
    """


_ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef = TypedDict(
    "_ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef",
    {"messageId": str, "errorCode": str, "errorMessage": str},
    total=False,
)


class ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef(
    _ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef
):
    """
    - *(dict) --*

      Contains informations about errors.
      - **messageId** *(string) --*

        The ID of the message that caused the error. (See the value corresponding to the "messageId"
        key in the message object.)
    """


_ClientBatchPutMessageResponseTypeDef = TypedDict(
    "_ClientBatchPutMessageResponseTypeDef",
    {
        "batchPutMessageErrorEntries": List[
            ClientBatchPutMessageResponsebatchPutMessageErrorEntriesTypeDef
        ]
    },
    total=False,
)


class ClientBatchPutMessageResponseTypeDef(_ClientBatchPutMessageResponseTypeDef):
    """
    - *(dict) --*

      - **batchPutMessageErrorEntries** *(list) --*

        A list of any errors encountered when sending the messages to the channel.
        - *(dict) --*

          Contains informations about errors.
          - **messageId** *(string) --*

            The ID of the message that caused the error. (See the value corresponding to the
            "messageId" key in the message object.)
    """


_ClientCreateChannelChannelStoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientCreateChannelChannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientCreateChannelChannelStoragecustomerManagedS3TypeDef(
    _ClientCreateChannelChannelStoragecustomerManagedS3TypeDef
):
    pass


_ClientCreateChannelChannelStorageTypeDef = TypedDict(
    "_ClientCreateChannelChannelStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientCreateChannelChannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientCreateChannelChannelStorageTypeDef(_ClientCreateChannelChannelStorageTypeDef):
    """
    Where channel data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
    storage. If not specified, the default is "serviceManagedS3". This cannot be changed after
    creation of the channel.
    - **serviceManagedS3** *(dict) --*

      Use this to store channel data in an S3 bucket managed by the AWS IoT Analytics service. The
      choice of service-managed or customer-managed S3 storage cannot be changed after creation of
      the channel.
    """


_ClientCreateChannelResponseretentionPeriodTypeDef = TypedDict(
    "_ClientCreateChannelResponseretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateChannelResponseretentionPeriodTypeDef(
    _ClientCreateChannelResponseretentionPeriodTypeDef
):
    pass


_ClientCreateChannelResponseTypeDef = TypedDict(
    "_ClientCreateChannelResponseTypeDef",
    {
        "channelName": str,
        "channelArn": str,
        "retentionPeriod": ClientCreateChannelResponseretentionPeriodTypeDef,
    },
    total=False,
)


class ClientCreateChannelResponseTypeDef(_ClientCreateChannelResponseTypeDef):
    """
    - *(dict) --*

      - **channelName** *(string) --*

        The name of the channel.
    """


_ClientCreateChannelRetentionPeriodTypeDef = TypedDict(
    "_ClientCreateChannelRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateChannelRetentionPeriodTypeDef(_ClientCreateChannelRetentionPeriodTypeDef):
    """
    How long, in days, message data is kept for the channel. When "customerManagedS3" storage is
    selected, this parameter is ignored.
    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.
    """


_RequiredClientCreateChannelTagsTypeDef = TypedDict(
    "_RequiredClientCreateChannelTagsTypeDef", {"key": str}
)
_OptionalClientCreateChannelTagsTypeDef = TypedDict(
    "_OptionalClientCreateChannelTagsTypeDef", {"value": str}, total=False
)


class ClientCreateChannelTagsTypeDef(
    _RequiredClientCreateChannelTagsTypeDef, _OptionalClientCreateChannelTagsTypeDef
):
    """
    - *(dict) --*

      A set of key/value pairs which are used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientCreateDatasetActionscontainerActionresourceConfigurationTypeDef = TypedDict(
    "_ClientCreateDatasetActionscontainerActionresourceConfigurationTypeDef",
    {"computeType": Literal["ACU_1", "ACU_2"], "volumeSizeInGB": int},
    total=False,
)


class ClientCreateDatasetActionscontainerActionresourceConfigurationTypeDef(
    _ClientCreateDatasetActionscontainerActionresourceConfigurationTypeDef
):
    pass


_ClientCreateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef = TypedDict(
    "_ClientCreateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    {"datasetName": str},
    total=False,
)


class ClientCreateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef(
    _ClientCreateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef
):
    pass


_ClientCreateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef = TypedDict(
    "_ClientCreateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef",
    {"fileName": str},
    total=False,
)


class ClientCreateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef(
    _ClientCreateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef
):
    pass


_ClientCreateDatasetActionscontainerActionvariablesTypeDef = TypedDict(
    "_ClientCreateDatasetActionscontainerActionvariablesTypeDef",
    {
        "name": str,
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": ClientCreateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef,
        "outputFileUriValue": ClientCreateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef,
    },
    total=False,
)


class ClientCreateDatasetActionscontainerActionvariablesTypeDef(
    _ClientCreateDatasetActionscontainerActionvariablesTypeDef
):
    pass


_ClientCreateDatasetActionscontainerActionTypeDef = TypedDict(
    "_ClientCreateDatasetActionscontainerActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ClientCreateDatasetActionscontainerActionresourceConfigurationTypeDef,
        "variables": List[ClientCreateDatasetActionscontainerActionvariablesTypeDef],
    },
    total=False,
)


class ClientCreateDatasetActionscontainerActionTypeDef(
    _ClientCreateDatasetActionscontainerActionTypeDef
):
    pass


_ClientCreateDatasetActionsqueryActionfiltersdeltaTimeTypeDef = TypedDict(
    "_ClientCreateDatasetActionsqueryActionfiltersdeltaTimeTypeDef",
    {"offsetSeconds": int, "timeExpression": str},
    total=False,
)


class ClientCreateDatasetActionsqueryActionfiltersdeltaTimeTypeDef(
    _ClientCreateDatasetActionsqueryActionfiltersdeltaTimeTypeDef
):
    pass


_ClientCreateDatasetActionsqueryActionfiltersTypeDef = TypedDict(
    "_ClientCreateDatasetActionsqueryActionfiltersTypeDef",
    {"deltaTime": ClientCreateDatasetActionsqueryActionfiltersdeltaTimeTypeDef},
    total=False,
)


class ClientCreateDatasetActionsqueryActionfiltersTypeDef(
    _ClientCreateDatasetActionsqueryActionfiltersTypeDef
):
    pass


_ClientCreateDatasetActionsqueryActionTypeDef = TypedDict(
    "_ClientCreateDatasetActionsqueryActionTypeDef",
    {"sqlQuery": str, "filters": List[ClientCreateDatasetActionsqueryActionfiltersTypeDef]},
    total=False,
)


class ClientCreateDatasetActionsqueryActionTypeDef(_ClientCreateDatasetActionsqueryActionTypeDef):
    pass


_ClientCreateDatasetActionsTypeDef = TypedDict(
    "_ClientCreateDatasetActionsTypeDef",
    {
        "actionName": str,
        "queryAction": ClientCreateDatasetActionsqueryActionTypeDef,
        "containerAction": ClientCreateDatasetActionscontainerActionTypeDef,
    },
    total=False,
)


class ClientCreateDatasetActionsTypeDef(_ClientCreateDatasetActionsTypeDef):
    """
    - *(dict) --*

      A "DatasetAction" object that specifies how data set contents are automatically created.
      - **actionName** *(string) --*

        The name of the data set action by which data set contents are automatically created.
    """


_ClientCreateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef = TypedDict(
    "_ClientCreateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    {"inputName": str, "roleArn": str},
    total=False,
)


class ClientCreateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef(
    _ClientCreateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef
):
    pass


_ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef = TypedDict(
    "_ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    {"tableName": str, "databaseName": str},
    total=False,
)


class ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef(
    _ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef
):
    pass


_ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef = TypedDict(
    "_ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "glueConfiguration": ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef,
        "roleArn": str,
    },
    total=False,
)


class ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef(
    _ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef
):
    pass


_ClientCreateDatasetContentDeliveryRulesdestinationTypeDef = TypedDict(
    "_ClientCreateDatasetContentDeliveryRulesdestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": ClientCreateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef,
        "s3DestinationConfiguration": ClientCreateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateDatasetContentDeliveryRulesdestinationTypeDef(
    _ClientCreateDatasetContentDeliveryRulesdestinationTypeDef
):
    pass


_ClientCreateDatasetContentDeliveryRulesTypeDef = TypedDict(
    "_ClientCreateDatasetContentDeliveryRulesTypeDef",
    {"entryName": str, "destination": ClientCreateDatasetContentDeliveryRulesdestinationTypeDef},
    total=False,
)


class ClientCreateDatasetContentDeliveryRulesTypeDef(
    _ClientCreateDatasetContentDeliveryRulesTypeDef
):
    """
    - *(dict) --*

      When data set contents are created they are delivered to destination specified here.
      - **entryName** *(string) --*

        The name of the data set content delivery rules entry.
    """


_ClientCreateDatasetContentResponseTypeDef = TypedDict(
    "_ClientCreateDatasetContentResponseTypeDef", {"versionId": str}, total=False
)


class ClientCreateDatasetContentResponseTypeDef(_ClientCreateDatasetContentResponseTypeDef):
    """
    - *(dict) --*

      - **versionId** *(string) --*

        The version ID of the data set contents which are being created.
    """


_ClientCreateDatasetResponseretentionPeriodTypeDef = TypedDict(
    "_ClientCreateDatasetResponseretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateDatasetResponseretentionPeriodTypeDef(
    _ClientCreateDatasetResponseretentionPeriodTypeDef
):
    pass


_ClientCreateDatasetResponseTypeDef = TypedDict(
    "_ClientCreateDatasetResponseTypeDef",
    {
        "datasetName": str,
        "datasetArn": str,
        "retentionPeriod": ClientCreateDatasetResponseretentionPeriodTypeDef,
    },
    total=False,
)


class ClientCreateDatasetResponseTypeDef(_ClientCreateDatasetResponseTypeDef):
    """
    - *(dict) --*

      - **datasetName** *(string) --*

        The name of the data set.
    """


_ClientCreateDatasetRetentionPeriodTypeDef = TypedDict(
    "_ClientCreateDatasetRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateDatasetRetentionPeriodTypeDef(_ClientCreateDatasetRetentionPeriodTypeDef):
    """
    [Optional] How long, in days, versions of data set contents are kept for the data set. If not
    specified or set to null, versions of data set contents are retained for at most 90 days. The
    number of versions of data set contents retained is determined by the
    ``versioningConfiguration`` parameter. (For more information, see
    https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)
    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.
    """


_RequiredClientCreateDatasetTagsTypeDef = TypedDict(
    "_RequiredClientCreateDatasetTagsTypeDef", {"key": str}
)
_OptionalClientCreateDatasetTagsTypeDef = TypedDict(
    "_OptionalClientCreateDatasetTagsTypeDef", {"value": str}, total=False
)


class ClientCreateDatasetTagsTypeDef(
    _RequiredClientCreateDatasetTagsTypeDef, _OptionalClientCreateDatasetTagsTypeDef
):
    """
    - *(dict) --*

      A set of key/value pairs which are used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientCreateDatasetTriggersdatasetTypeDef = TypedDict(
    "_ClientCreateDatasetTriggersdatasetTypeDef", {"name": str}, total=False
)


class ClientCreateDatasetTriggersdatasetTypeDef(_ClientCreateDatasetTriggersdatasetTypeDef):
    pass


_ClientCreateDatasetTriggersscheduleTypeDef = TypedDict(
    "_ClientCreateDatasetTriggersscheduleTypeDef", {"expression": str}, total=False
)


class ClientCreateDatasetTriggersscheduleTypeDef(_ClientCreateDatasetTriggersscheduleTypeDef):
    """
    - **schedule** *(dict) --*

      The "Schedule" when the trigger is initiated.
      - **expression** *(string) --*

        The expression that defines when to trigger an update. For more information, see `Schedule
        Expressions for Rules
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the
        Amazon CloudWatch Events User Guide.
    """


_ClientCreateDatasetTriggersTypeDef = TypedDict(
    "_ClientCreateDatasetTriggersTypeDef",
    {
        "schedule": ClientCreateDatasetTriggersscheduleTypeDef,
        "dataset": ClientCreateDatasetTriggersdatasetTypeDef,
    },
    total=False,
)


class ClientCreateDatasetTriggersTypeDef(_ClientCreateDatasetTriggersTypeDef):
    """
    - *(dict) --*

      The "DatasetTrigger" that specifies when the data set is automatically updated.
      - **schedule** *(dict) --*

        The "Schedule" when the trigger is initiated.
        - **expression** *(string) --*

          The expression that defines when to trigger an update. For more information, see `Schedule
          Expressions for Rules
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in
          the Amazon CloudWatch Events User Guide.
    """


_ClientCreateDatasetVersioningConfigurationTypeDef = TypedDict(
    "_ClientCreateDatasetVersioningConfigurationTypeDef",
    {"unlimited": bool, "maxVersions": int},
    total=False,
)


class ClientCreateDatasetVersioningConfigurationTypeDef(
    _ClientCreateDatasetVersioningConfigurationTypeDef
):
    """
    [Optional] How many versions of data set contents are kept. If not specified or set to null,
    only the latest version plus the latest succeeded version (if they are different) are kept for
    the time period specified by the "retentionPeriod" parameter. (For more information, see
    https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)
    - **unlimited** *(boolean) --*

      If true, unlimited versions of data set contents will be kept.
    """


_ClientCreateDatastoreDatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientCreateDatastoreDatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientCreateDatastoreDatastoreStoragecustomerManagedS3TypeDef(
    _ClientCreateDatastoreDatastoreStoragecustomerManagedS3TypeDef
):
    pass


_ClientCreateDatastoreDatastoreStorageTypeDef = TypedDict(
    "_ClientCreateDatastoreDatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientCreateDatastoreDatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientCreateDatastoreDatastoreStorageTypeDef(_ClientCreateDatastoreDatastoreStorageTypeDef):
    """
    Where data store data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
    storage. If not specified, the default is "serviceManagedS3". This cannot be changed after the
    data store is created.
    - **serviceManagedS3** *(dict) --*

      Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics service.
      The choice of service-managed or customer-managed S3 storage cannot be changed after creation
      of the data store.
    """


_ClientCreateDatastoreResponseretentionPeriodTypeDef = TypedDict(
    "_ClientCreateDatastoreResponseretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateDatastoreResponseretentionPeriodTypeDef(
    _ClientCreateDatastoreResponseretentionPeriodTypeDef
):
    pass


_ClientCreateDatastoreResponseTypeDef = TypedDict(
    "_ClientCreateDatastoreResponseTypeDef",
    {
        "datastoreName": str,
        "datastoreArn": str,
        "retentionPeriod": ClientCreateDatastoreResponseretentionPeriodTypeDef,
    },
    total=False,
)


class ClientCreateDatastoreResponseTypeDef(_ClientCreateDatastoreResponseTypeDef):
    """
    - *(dict) --*

      - **datastoreName** *(string) --*

        The name of the data store.
    """


_ClientCreateDatastoreRetentionPeriodTypeDef = TypedDict(
    "_ClientCreateDatastoreRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientCreateDatastoreRetentionPeriodTypeDef(_ClientCreateDatastoreRetentionPeriodTypeDef):
    """
    How long, in days, message data is kept for the data store. When "customerManagedS3" storage is
    selected, this parameter is ignored.
    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.
    """


_RequiredClientCreateDatastoreTagsTypeDef = TypedDict(
    "_RequiredClientCreateDatastoreTagsTypeDef", {"key": str}
)
_OptionalClientCreateDatastoreTagsTypeDef = TypedDict(
    "_OptionalClientCreateDatastoreTagsTypeDef", {"value": str}, total=False
)


class ClientCreateDatastoreTagsTypeDef(
    _RequiredClientCreateDatastoreTagsTypeDef, _OptionalClientCreateDatastoreTagsTypeDef
):
    """
    - *(dict) --*

      A set of key/value pairs which are used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientCreatePipelinePipelineActivitiesaddAttributesTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitiesaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str], "next": str},
    total=False,
)


class ClientCreatePipelinePipelineActivitiesaddAttributesTypeDef(
    _ClientCreatePipelinePipelineActivitiesaddAttributesTypeDef
):
    pass


_ClientCreatePipelinePipelineActivitieschannelTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitieschannelTypeDef",
    {"name": str, "channelName": str, "next": str},
    total=False,
)


class ClientCreatePipelinePipelineActivitieschannelTypeDef(
    _ClientCreatePipelinePipelineActivitieschannelTypeDef
):
    pass


_ClientCreatePipelinePipelineActivitiesdatastoreTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitiesdatastoreTypeDef",
    {"name": str, "datastoreName": str},
    total=False,
)


class ClientCreatePipelinePipelineActivitiesdatastoreTypeDef(
    _ClientCreatePipelinePipelineActivitiesdatastoreTypeDef
):
    pass


_ClientCreatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)


class ClientCreatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef(
    _ClientCreatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef
):
    pass


_ClientCreatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)


class ClientCreatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef(
    _ClientCreatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef
):
    pass


_ClientCreatePipelinePipelineActivitiesfilterTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitiesfilterTypeDef",
    {"name": str, "filter": str, "next": str},
    total=False,
)


class ClientCreatePipelinePipelineActivitiesfilterTypeDef(
    _ClientCreatePipelinePipelineActivitiesfilterTypeDef
):
    pass


_ClientCreatePipelinePipelineActivitieslambdaTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitieslambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int, "next": str},
    total=False,
)


class ClientCreatePipelinePipelineActivitieslambdaTypeDef(
    _ClientCreatePipelinePipelineActivitieslambdaTypeDef
):
    pass


_ClientCreatePipelinePipelineActivitiesmathTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitiesmathTypeDef",
    {"name": str, "attribute": str, "math": str, "next": str},
    total=False,
)


class ClientCreatePipelinePipelineActivitiesmathTypeDef(
    _ClientCreatePipelinePipelineActivitiesmathTypeDef
):
    pass


_ClientCreatePipelinePipelineActivitiesremoveAttributesTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitiesremoveAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)


class ClientCreatePipelinePipelineActivitiesremoveAttributesTypeDef(
    _ClientCreatePipelinePipelineActivitiesremoveAttributesTypeDef
):
    pass


_ClientCreatePipelinePipelineActivitiesselectAttributesTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitiesselectAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)


class ClientCreatePipelinePipelineActivitiesselectAttributesTypeDef(
    _ClientCreatePipelinePipelineActivitiesselectAttributesTypeDef
):
    pass


_ClientCreatePipelinePipelineActivitiesTypeDef = TypedDict(
    "_ClientCreatePipelinePipelineActivitiesTypeDef",
    {
        "channel": ClientCreatePipelinePipelineActivitieschannelTypeDef,
        "lambda": ClientCreatePipelinePipelineActivitieslambdaTypeDef,
        "datastore": ClientCreatePipelinePipelineActivitiesdatastoreTypeDef,
        "addAttributes": ClientCreatePipelinePipelineActivitiesaddAttributesTypeDef,
        "removeAttributes": ClientCreatePipelinePipelineActivitiesremoveAttributesTypeDef,
        "selectAttributes": ClientCreatePipelinePipelineActivitiesselectAttributesTypeDef,
        "filter": ClientCreatePipelinePipelineActivitiesfilterTypeDef,
        "math": ClientCreatePipelinePipelineActivitiesmathTypeDef,
        "deviceRegistryEnrich": ClientCreatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientCreatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef,
    },
    total=False,
)


class ClientCreatePipelinePipelineActivitiesTypeDef(_ClientCreatePipelinePipelineActivitiesTypeDef):
    pass


_ClientCreatePipelineResponseTypeDef = TypedDict(
    "_ClientCreatePipelineResponseTypeDef", {"pipelineName": str, "pipelineArn": str}, total=False
)


class ClientCreatePipelineResponseTypeDef(_ClientCreatePipelineResponseTypeDef):
    """
    - *(dict) --*

      - **pipelineName** *(string) --*

        The name of the pipeline.
    """


_RequiredClientCreatePipelineTagsTypeDef = TypedDict(
    "_RequiredClientCreatePipelineTagsTypeDef", {"key": str}
)
_OptionalClientCreatePipelineTagsTypeDef = TypedDict(
    "_OptionalClientCreatePipelineTagsTypeDef", {"value": str}, total=False
)


class ClientCreatePipelineTagsTypeDef(
    _RequiredClientCreatePipelineTagsTypeDef, _OptionalClientCreatePipelineTagsTypeDef
):
    """
    - *(dict) --*

      A set of key/value pairs which are used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientDescribeChannelResponsechannelretentionPeriodTypeDef = TypedDict(
    "_ClientDescribeChannelResponsechannelretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientDescribeChannelResponsechannelretentionPeriodTypeDef(
    _ClientDescribeChannelResponsechannelretentionPeriodTypeDef
):
    pass


_ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef(
    _ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef
):
    pass


_ClientDescribeChannelResponsechannelstorageTypeDef = TypedDict(
    "_ClientDescribeChannelResponsechannelstorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientDescribeChannelResponsechannelstoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientDescribeChannelResponsechannelstorageTypeDef(
    _ClientDescribeChannelResponsechannelstorageTypeDef
):
    pass


_ClientDescribeChannelResponsechannelTypeDef = TypedDict(
    "_ClientDescribeChannelResponsechannelTypeDef",
    {
        "name": str,
        "storage": ClientDescribeChannelResponsechannelstorageTypeDef,
        "arn": str,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "retentionPeriod": ClientDescribeChannelResponsechannelretentionPeriodTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeChannelResponsechannelTypeDef(_ClientDescribeChannelResponsechannelTypeDef):
    """
    - **channel** *(dict) --*

      An object that contains information about the channel.
      - **name** *(string) --*

        The name of the channel.
    """


_ClientDescribeChannelResponsestatisticssizeTypeDef = TypedDict(
    "_ClientDescribeChannelResponsestatisticssizeTypeDef",
    {"estimatedSizeInBytes": float, "estimatedOn": datetime},
    total=False,
)


class ClientDescribeChannelResponsestatisticssizeTypeDef(
    _ClientDescribeChannelResponsestatisticssizeTypeDef
):
    pass


_ClientDescribeChannelResponsestatisticsTypeDef = TypedDict(
    "_ClientDescribeChannelResponsestatisticsTypeDef",
    {"size": ClientDescribeChannelResponsestatisticssizeTypeDef},
    total=False,
)


class ClientDescribeChannelResponsestatisticsTypeDef(
    _ClientDescribeChannelResponsestatisticsTypeDef
):
    pass


_ClientDescribeChannelResponseTypeDef = TypedDict(
    "_ClientDescribeChannelResponseTypeDef",
    {
        "channel": ClientDescribeChannelResponsechannelTypeDef,
        "statistics": ClientDescribeChannelResponsestatisticsTypeDef,
    },
    total=False,
)


class ClientDescribeChannelResponseTypeDef(_ClientDescribeChannelResponseTypeDef):
    """
    - *(dict) --*

      - **channel** *(dict) --*

        An object that contains information about the channel.
        - **name** *(string) --*

          The name of the channel.
    """


_ClientDescribeDatasetResponsedatasetactionscontainerActionresourceConfigurationTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetactionscontainerActionresourceConfigurationTypeDef",
    {"computeType": Literal["ACU_1", "ACU_2"], "volumeSizeInGB": int},
    total=False,
)


class ClientDescribeDatasetResponsedatasetactionscontainerActionresourceConfigurationTypeDef(
    _ClientDescribeDatasetResponsedatasetactionscontainerActionresourceConfigurationTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    {"datasetName": str},
    total=False,
)


class ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef(
    _ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesoutputFileUriValueTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesoutputFileUriValueTypeDef",
    {"fileName": str},
    total=False,
)


class ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesoutputFileUriValueTypeDef(
    _ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesoutputFileUriValueTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesTypeDef",
    {
        "name": str,
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesdatasetContentVersionValueTypeDef,
        "outputFileUriValue": ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesoutputFileUriValueTypeDef,
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesTypeDef(
    _ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetactionscontainerActionTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetactionscontainerActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ClientDescribeDatasetResponsedatasetactionscontainerActionresourceConfigurationTypeDef,
        "variables": List[
            ClientDescribeDatasetResponsedatasetactionscontainerActionvariablesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasetactionscontainerActionTypeDef(
    _ClientDescribeDatasetResponsedatasetactionscontainerActionTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersdeltaTimeTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersdeltaTimeTypeDef",
    {"offsetSeconds": int, "timeExpression": str},
    total=False,
)


class ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersdeltaTimeTypeDef(
    _ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersdeltaTimeTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersTypeDef",
    {"deltaTime": ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersdeltaTimeTypeDef},
    total=False,
)


class ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersTypeDef(
    _ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetactionsqueryActionTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetactionsqueryActionTypeDef",
    {
        "sqlQuery": str,
        "filters": List[ClientDescribeDatasetResponsedatasetactionsqueryActionfiltersTypeDef],
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasetactionsqueryActionTypeDef(
    _ClientDescribeDatasetResponsedatasetactionsqueryActionTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetactionsTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetactionsTypeDef",
    {
        "actionName": str,
        "queryAction": ClientDescribeDatasetResponsedatasetactionsqueryActionTypeDef,
        "containerAction": ClientDescribeDatasetResponsedatasetactionscontainerActionTypeDef,
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasetactionsTypeDef(
    _ClientDescribeDatasetResponsedatasetactionsTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    {"inputName": str, "roleArn": str},
    total=False,
)


class ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef(
    _ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    {"tableName": str, "databaseName": str},
    total=False,
)


class ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef(
    _ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "glueConfiguration": ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef,
        "roleArn": str,
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef(
    _ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef,
        "s3DestinationConfiguration": ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationTypeDef(
    _ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetcontentDeliveryRulesTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetcontentDeliveryRulesTypeDef",
    {
        "entryName": str,
        "destination": ClientDescribeDatasetResponsedatasetcontentDeliveryRulesdestinationTypeDef,
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasetcontentDeliveryRulesTypeDef(
    _ClientDescribeDatasetResponsedatasetcontentDeliveryRulesTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetretentionPeriodTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientDescribeDatasetResponsedatasetretentionPeriodTypeDef(
    _ClientDescribeDatasetResponsedatasetretentionPeriodTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasettriggersdatasetTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasettriggersdatasetTypeDef", {"name": str}, total=False
)


class ClientDescribeDatasetResponsedatasettriggersdatasetTypeDef(
    _ClientDescribeDatasetResponsedatasettriggersdatasetTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasettriggersscheduleTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasettriggersscheduleTypeDef", {"expression": str}, total=False
)


class ClientDescribeDatasetResponsedatasettriggersscheduleTypeDef(
    _ClientDescribeDatasetResponsedatasettriggersscheduleTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasettriggersTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasettriggersTypeDef",
    {
        "schedule": ClientDescribeDatasetResponsedatasettriggersscheduleTypeDef,
        "dataset": ClientDescribeDatasetResponsedatasettriggersdatasetTypeDef,
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasettriggersTypeDef(
    _ClientDescribeDatasetResponsedatasettriggersTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetversioningConfigurationTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetversioningConfigurationTypeDef",
    {"unlimited": bool, "maxVersions": int},
    total=False,
)


class ClientDescribeDatasetResponsedatasetversioningConfigurationTypeDef(
    _ClientDescribeDatasetResponsedatasetversioningConfigurationTypeDef
):
    pass


_ClientDescribeDatasetResponsedatasetTypeDef = TypedDict(
    "_ClientDescribeDatasetResponsedatasetTypeDef",
    {
        "name": str,
        "arn": str,
        "actions": List[ClientDescribeDatasetResponsedatasetactionsTypeDef],
        "triggers": List[ClientDescribeDatasetResponsedatasettriggersTypeDef],
        "contentDeliveryRules": List[
            ClientDescribeDatasetResponsedatasetcontentDeliveryRulesTypeDef
        ],
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "retentionPeriod": ClientDescribeDatasetResponsedatasetretentionPeriodTypeDef,
        "versioningConfiguration": ClientDescribeDatasetResponsedatasetversioningConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeDatasetResponsedatasetTypeDef(_ClientDescribeDatasetResponsedatasetTypeDef):
    """
    - **dataset** *(dict) --*

      An object that contains information about the data set.
      - **name** *(string) --*

        The name of the data set.
    """


_ClientDescribeDatasetResponseTypeDef = TypedDict(
    "_ClientDescribeDatasetResponseTypeDef",
    {"dataset": ClientDescribeDatasetResponsedatasetTypeDef},
    total=False,
)


class ClientDescribeDatasetResponseTypeDef(_ClientDescribeDatasetResponseTypeDef):
    """
    - *(dict) --*

      - **dataset** *(dict) --*

        An object that contains information about the data set.
        - **name** *(string) --*

          The name of the data set.
    """


_ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef(
    _ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef
):
    pass


_ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef(
    _ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef
):
    pass


_ClientDescribeDatastoreResponsedatastorestorageTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsedatastorestorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientDescribeDatastoreResponsedatastorestoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientDescribeDatastoreResponsedatastorestorageTypeDef(
    _ClientDescribeDatastoreResponsedatastorestorageTypeDef
):
    pass


_ClientDescribeDatastoreResponsedatastoreTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsedatastoreTypeDef",
    {
        "name": str,
        "storage": ClientDescribeDatastoreResponsedatastorestorageTypeDef,
        "arn": str,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "retentionPeriod": ClientDescribeDatastoreResponsedatastoreretentionPeriodTypeDef,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribeDatastoreResponsedatastoreTypeDef(
    _ClientDescribeDatastoreResponsedatastoreTypeDef
):
    """
    - **datastore** *(dict) --*

      Information about the data store.
      - **name** *(string) --*

        The name of the data store.
    """


_ClientDescribeDatastoreResponsestatisticssizeTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsestatisticssizeTypeDef",
    {"estimatedSizeInBytes": float, "estimatedOn": datetime},
    total=False,
)


class ClientDescribeDatastoreResponsestatisticssizeTypeDef(
    _ClientDescribeDatastoreResponsestatisticssizeTypeDef
):
    pass


_ClientDescribeDatastoreResponsestatisticsTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponsestatisticsTypeDef",
    {"size": ClientDescribeDatastoreResponsestatisticssizeTypeDef},
    total=False,
)


class ClientDescribeDatastoreResponsestatisticsTypeDef(
    _ClientDescribeDatastoreResponsestatisticsTypeDef
):
    pass


_ClientDescribeDatastoreResponseTypeDef = TypedDict(
    "_ClientDescribeDatastoreResponseTypeDef",
    {
        "datastore": ClientDescribeDatastoreResponsedatastoreTypeDef,
        "statistics": ClientDescribeDatastoreResponsestatisticsTypeDef,
    },
    total=False,
)


class ClientDescribeDatastoreResponseTypeDef(_ClientDescribeDatastoreResponseTypeDef):
    """
    - *(dict) --*

      - **datastore** *(dict) --*

        Information about the data store.
        - **name** *(string) --*

          The name of the data store.
    """


_ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef = TypedDict(
    "_ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef",
    {"roleArn": str, "level": str, "enabled": bool},
    total=False,
)


class ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef(
    _ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef
):
    """
    - **loggingOptions** *(dict) --*

      The current settings of the AWS IoT Analytics logging options.
      - **roleArn** *(string) --*

        The ARN of the role that grants permission to AWS IoT Analytics to perform logging.
    """


_ClientDescribeLoggingOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeLoggingOptionsResponseTypeDef",
    {"loggingOptions": ClientDescribeLoggingOptionsResponseloggingOptionsTypeDef},
    total=False,
)


class ClientDescribeLoggingOptionsResponseTypeDef(_ClientDescribeLoggingOptionsResponseTypeDef):
    """
    - *(dict) --*

      - **loggingOptions** *(dict) --*

        The current settings of the AWS IoT Analytics logging options.
        - **roleArn** *(string) --*

          The ARN of the role that grants permission to AWS IoT Analytics to perform logging.
    """


_ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str], "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineactivitieschannelTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitieschannelTypeDef",
    {"name": str, "channelName": str, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitieschannelTypeDef(
    _ClientDescribePipelineResponsepipelineactivitieschannelTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef",
    {"name": str, "datastoreName": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef",
    {"name": str, "filter": str, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef(
    _ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineactivitiesmathTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesmathTypeDef",
    {"name": str, "attribute": str, "math": str, "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesmathTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesmathTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineactivitiesTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineactivitiesTypeDef",
    {
        "channel": ClientDescribePipelineResponsepipelineactivitieschannelTypeDef,
        "lambda": ClientDescribePipelineResponsepipelineactivitieslambdaTypeDef,
        "datastore": ClientDescribePipelineResponsepipelineactivitiesdatastoreTypeDef,
        "addAttributes": ClientDescribePipelineResponsepipelineactivitiesaddAttributesTypeDef,
        "removeAttributes": ClientDescribePipelineResponsepipelineactivitiesremoveAttributesTypeDef,
        "selectAttributes": ClientDescribePipelineResponsepipelineactivitiesselectAttributesTypeDef,
        "filter": ClientDescribePipelineResponsepipelineactivitiesfilterTypeDef,
        "math": ClientDescribePipelineResponsepipelineactivitiesmathTypeDef,
        "deviceRegistryEnrich": ClientDescribePipelineResponsepipelineactivitiesdeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientDescribePipelineResponsepipelineactivitiesdeviceShadowEnrichTypeDef,
    },
    total=False,
)


class ClientDescribePipelineResponsepipelineactivitiesTypeDef(
    _ClientDescribePipelineResponsepipelineactivitiesTypeDef
):
    pass


_ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef",
    {
        "id": str,
        "status": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "creationTime": datetime,
    },
    total=False,
)


class ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef(
    _ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef
):
    pass


_ClientDescribePipelineResponsepipelineTypeDef = TypedDict(
    "_ClientDescribePipelineResponsepipelineTypeDef",
    {
        "name": str,
        "arn": str,
        "activities": List[ClientDescribePipelineResponsepipelineactivitiesTypeDef],
        "reprocessingSummaries": List[
            ClientDescribePipelineResponsepipelinereprocessingSummariesTypeDef
        ],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientDescribePipelineResponsepipelineTypeDef(_ClientDescribePipelineResponsepipelineTypeDef):
    """
    - **pipeline** *(dict) --*

      A "Pipeline" object that contains information about the pipeline.
      - **name** *(string) --*

        The name of the pipeline.
    """


_ClientDescribePipelineResponseTypeDef = TypedDict(
    "_ClientDescribePipelineResponseTypeDef",
    {"pipeline": ClientDescribePipelineResponsepipelineTypeDef},
    total=False,
)


class ClientDescribePipelineResponseTypeDef(_ClientDescribePipelineResponseTypeDef):
    """
    - *(dict) --*

      - **pipeline** *(dict) --*

        A "Pipeline" object that contains information about the pipeline.
        - **name** *(string) --*

          The name of the pipeline.
    """


_ClientGetDatasetContentResponseentriesTypeDef = TypedDict(
    "_ClientGetDatasetContentResponseentriesTypeDef",
    {"entryName": str, "dataURI": str},
    total=False,
)


class ClientGetDatasetContentResponseentriesTypeDef(_ClientGetDatasetContentResponseentriesTypeDef):
    """
    - *(dict) --*

      The reference to a data set entry.
      - **entryName** *(string) --*

        The name of the data set item.
    """


_ClientGetDatasetContentResponsestatusTypeDef = TypedDict(
    "_ClientGetDatasetContentResponsestatusTypeDef",
    {"state": Literal["CREATING", "SUCCEEDED", "FAILED"], "reason": str},
    total=False,
)


class ClientGetDatasetContentResponsestatusTypeDef(_ClientGetDatasetContentResponsestatusTypeDef):
    pass


_ClientGetDatasetContentResponseTypeDef = TypedDict(
    "_ClientGetDatasetContentResponseTypeDef",
    {
        "entries": List[ClientGetDatasetContentResponseentriesTypeDef],
        "timestamp": datetime,
        "status": ClientGetDatasetContentResponsestatusTypeDef,
    },
    total=False,
)


class ClientGetDatasetContentResponseTypeDef(_ClientGetDatasetContentResponseTypeDef):
    """
    - *(dict) --*

      - **entries** *(list) --*

        A list of "DatasetEntry" objects.
        - *(dict) --*

          The reference to a data set entry.
          - **entryName** *(string) --*

            The name of the data set item.
    """


_ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef(
    _ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef
):
    pass


_ClientListChannelsResponsechannelSummarieschannelStorageTypeDef = TypedDict(
    "_ClientListChannelsResponsechannelSummarieschannelStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientListChannelsResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientListChannelsResponsechannelSummarieschannelStorageTypeDef(
    _ClientListChannelsResponsechannelSummarieschannelStorageTypeDef
):
    pass


_ClientListChannelsResponsechannelSummariesTypeDef = TypedDict(
    "_ClientListChannelsResponsechannelSummariesTypeDef",
    {
        "channelName": str,
        "channelStorage": ClientListChannelsResponsechannelSummarieschannelStorageTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientListChannelsResponsechannelSummariesTypeDef(
    _ClientListChannelsResponsechannelSummariesTypeDef
):
    """
    - *(dict) --*

      A summary of information about a channel.
      - **channelName** *(string) --*

        The name of the channel.
    """


_ClientListChannelsResponseTypeDef = TypedDict(
    "_ClientListChannelsResponseTypeDef",
    {"channelSummaries": List[ClientListChannelsResponsechannelSummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientListChannelsResponseTypeDef(_ClientListChannelsResponseTypeDef):
    """
    - *(dict) --*

      - **channelSummaries** *(list) --*

        A list of "ChannelSummary" objects.
        - *(dict) --*

          A summary of information about a channel.
          - **channelName** *(string) --*

            The name of the channel.
    """


_ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef = TypedDict(
    "_ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef",
    {"state": Literal["CREATING", "SUCCEEDED", "FAILED"], "reason": str},
    total=False,
)


class ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef(
    _ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef
):
    pass


_ClientListDatasetContentsResponsedatasetContentSummariesTypeDef = TypedDict(
    "_ClientListDatasetContentsResponsedatasetContentSummariesTypeDef",
    {
        "version": str,
        "status": ClientListDatasetContentsResponsedatasetContentSummariesstatusTypeDef,
        "creationTime": datetime,
        "scheduleTime": datetime,
        "completionTime": datetime,
    },
    total=False,
)


class ClientListDatasetContentsResponsedatasetContentSummariesTypeDef(
    _ClientListDatasetContentsResponsedatasetContentSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information about data set contents.
      - **version** *(string) --*

        The version of the data set contents.
    """


_ClientListDatasetContentsResponseTypeDef = TypedDict(
    "_ClientListDatasetContentsResponseTypeDef",
    {
        "datasetContentSummaries": List[
            ClientListDatasetContentsResponsedatasetContentSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListDatasetContentsResponseTypeDef(_ClientListDatasetContentsResponseTypeDef):
    """
    - *(dict) --*

      - **datasetContentSummaries** *(list) --*

        Summary information about data set contents that have been created.
        - *(dict) --*

          Summary information about data set contents.
          - **version** *(string) --*

            The version of the data set contents.
    """


_ClientListDatasetsResponsedatasetSummariesactionsTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetSummariesactionsTypeDef",
    {"actionName": str, "actionType": Literal["QUERY", "CONTAINER"]},
    total=False,
)


class ClientListDatasetsResponsedatasetSummariesactionsTypeDef(
    _ClientListDatasetsResponsedatasetSummariesactionsTypeDef
):
    pass


_ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef", {"name": str}, total=False
)


class ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef(
    _ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef
):
    pass


_ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef",
    {"expression": str},
    total=False,
)


class ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef(
    _ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef
):
    pass


_ClientListDatasetsResponsedatasetSummariestriggersTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetSummariestriggersTypeDef",
    {
        "schedule": ClientListDatasetsResponsedatasetSummariestriggersscheduleTypeDef,
        "dataset": ClientListDatasetsResponsedatasetSummariestriggersdatasetTypeDef,
    },
    total=False,
)


class ClientListDatasetsResponsedatasetSummariestriggersTypeDef(
    _ClientListDatasetsResponsedatasetSummariestriggersTypeDef
):
    pass


_ClientListDatasetsResponsedatasetSummariesTypeDef = TypedDict(
    "_ClientListDatasetsResponsedatasetSummariesTypeDef",
    {
        "datasetName": str,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "triggers": List[ClientListDatasetsResponsedatasetSummariestriggersTypeDef],
        "actions": List[ClientListDatasetsResponsedatasetSummariesactionsTypeDef],
    },
    total=False,
)


class ClientListDatasetsResponsedatasetSummariesTypeDef(
    _ClientListDatasetsResponsedatasetSummariesTypeDef
):
    """
    - *(dict) --*

      A summary of information about a data set.
      - **datasetName** *(string) --*

        The name of the data set.
    """


_ClientListDatasetsResponseTypeDef = TypedDict(
    "_ClientListDatasetsResponseTypeDef",
    {"datasetSummaries": List[ClientListDatasetsResponsedatasetSummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientListDatasetsResponseTypeDef(_ClientListDatasetsResponseTypeDef):
    """
    - *(dict) --*

      - **datasetSummaries** *(list) --*

        A list of "DatasetSummary" objects.
        - *(dict) --*

          A summary of information about a data set.
          - **datasetName** *(string) --*

            The name of the data set.
    """


_ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef(
    _ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef
):
    pass


_ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef = TypedDict(
    "_ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientListDatastoresResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef(
    _ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef
):
    pass


_ClientListDatastoresResponsedatastoreSummariesTypeDef = TypedDict(
    "_ClientListDatastoresResponsedatastoreSummariesTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": ClientListDatastoresResponsedatastoreSummariesdatastoreStorageTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientListDatastoresResponsedatastoreSummariesTypeDef(
    _ClientListDatastoresResponsedatastoreSummariesTypeDef
):
    """
    - *(dict) --*

      A summary of information about a data store.
      - **datastoreName** *(string) --*

        The name of the data store.
    """


_ClientListDatastoresResponseTypeDef = TypedDict(
    "_ClientListDatastoresResponseTypeDef",
    {
        "datastoreSummaries": List[ClientListDatastoresResponsedatastoreSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListDatastoresResponseTypeDef(_ClientListDatastoresResponseTypeDef):
    """
    - *(dict) --*

      - **datastoreSummaries** *(list) --*

        A list of "DatastoreSummary" objects.
        - *(dict) --*

          A summary of information about a data store.
          - **datastoreName** *(string) --*

            The name of the data store.
    """


_ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef = TypedDict(
    "_ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef",
    {
        "id": str,
        "status": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "creationTime": datetime,
    },
    total=False,
)


class ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef(
    _ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef
):
    pass


_ClientListPipelinesResponsepipelineSummariesTypeDef = TypedDict(
    "_ClientListPipelinesResponsepipelineSummariesTypeDef",
    {
        "pipelineName": str,
        "reprocessingSummaries": List[
            ClientListPipelinesResponsepipelineSummariesreprocessingSummariesTypeDef
        ],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ClientListPipelinesResponsepipelineSummariesTypeDef(
    _ClientListPipelinesResponsepipelineSummariesTypeDef
):
    """
    - *(dict) --*

      A summary of information about a pipeline.
      - **pipelineName** *(string) --*

        The name of the pipeline.
    """


_ClientListPipelinesResponseTypeDef = TypedDict(
    "_ClientListPipelinesResponseTypeDef",
    {
        "pipelineSummaries": List[ClientListPipelinesResponsepipelineSummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListPipelinesResponseTypeDef(_ClientListPipelinesResponseTypeDef):
    """
    - *(dict) --*

      - **pipelineSummaries** *(list) --*

        A list of "PipelineSummary" objects.
        - *(dict) --*

          A summary of information about a pipeline.
          - **pipelineName** *(string) --*

            The name of the pipeline.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientListTagsForResourceResponsetagsTypeDef(_ClientListTagsForResourceResponsetagsTypeDef):
    """
    - *(dict) --*

      A set of key/value pairs which are used to manage the resource.
      - **key** *(string) --*

        The tag's key.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        The tags (metadata) which you have assigned to the resource.
        - *(dict) --*

          A set of key/value pairs which are used to manage the resource.
          - **key** *(string) --*

            The tag's key.
    """


_RequiredClientPutLoggingOptionsLoggingOptionsTypeDef = TypedDict(
    "_RequiredClientPutLoggingOptionsLoggingOptionsTypeDef", {"roleArn": str}
)
_OptionalClientPutLoggingOptionsLoggingOptionsTypeDef = TypedDict(
    "_OptionalClientPutLoggingOptionsLoggingOptionsTypeDef",
    {"level": str, "enabled": bool},
    total=False,
)


class ClientPutLoggingOptionsLoggingOptionsTypeDef(
    _RequiredClientPutLoggingOptionsLoggingOptionsTypeDef,
    _OptionalClientPutLoggingOptionsLoggingOptionsTypeDef,
):
    """
    The new values of the AWS IoT Analytics logging options.
    - **roleArn** *(string) --***[REQUIRED]**

      The ARN of the role that grants permission to AWS IoT Analytics to perform logging.
    """


_ClientRunPipelineActivityPipelineActivityaddAttributesTypeDef = TypedDict(
    "_ClientRunPipelineActivityPipelineActivityaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str], "next": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivityaddAttributesTypeDef(
    _ClientRunPipelineActivityPipelineActivityaddAttributesTypeDef
):
    pass


_RequiredClientRunPipelineActivityPipelineActivitychannelTypeDef = TypedDict(
    "_RequiredClientRunPipelineActivityPipelineActivitychannelTypeDef", {"name": str}
)
_OptionalClientRunPipelineActivityPipelineActivitychannelTypeDef = TypedDict(
    "_OptionalClientRunPipelineActivityPipelineActivitychannelTypeDef",
    {"channelName": str, "next": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivitychannelTypeDef(
    _RequiredClientRunPipelineActivityPipelineActivitychannelTypeDef,
    _OptionalClientRunPipelineActivityPipelineActivitychannelTypeDef,
):
    """
    - **channel** *(dict) --*

      Determines the source of the messages to be processed.
      - **name** *(string) --***[REQUIRED]**

        The name of the 'channel' activity.
    """


_ClientRunPipelineActivityPipelineActivitydatastoreTypeDef = TypedDict(
    "_ClientRunPipelineActivityPipelineActivitydatastoreTypeDef",
    {"name": str, "datastoreName": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivitydatastoreTypeDef(
    _ClientRunPipelineActivityPipelineActivitydatastoreTypeDef
):
    pass


_ClientRunPipelineActivityPipelineActivitydeviceRegistryEnrichTypeDef = TypedDict(
    "_ClientRunPipelineActivityPipelineActivitydeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivitydeviceRegistryEnrichTypeDef(
    _ClientRunPipelineActivityPipelineActivitydeviceRegistryEnrichTypeDef
):
    pass


_ClientRunPipelineActivityPipelineActivitydeviceShadowEnrichTypeDef = TypedDict(
    "_ClientRunPipelineActivityPipelineActivitydeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivitydeviceShadowEnrichTypeDef(
    _ClientRunPipelineActivityPipelineActivitydeviceShadowEnrichTypeDef
):
    pass


_ClientRunPipelineActivityPipelineActivityfilterTypeDef = TypedDict(
    "_ClientRunPipelineActivityPipelineActivityfilterTypeDef",
    {"name": str, "filter": str, "next": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivityfilterTypeDef(
    _ClientRunPipelineActivityPipelineActivityfilterTypeDef
):
    pass


_ClientRunPipelineActivityPipelineActivitylambdaTypeDef = TypedDict(
    "_ClientRunPipelineActivityPipelineActivitylambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int, "next": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivitylambdaTypeDef(
    _ClientRunPipelineActivityPipelineActivitylambdaTypeDef
):
    pass


_ClientRunPipelineActivityPipelineActivitymathTypeDef = TypedDict(
    "_ClientRunPipelineActivityPipelineActivitymathTypeDef",
    {"name": str, "attribute": str, "math": str, "next": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivitymathTypeDef(
    _ClientRunPipelineActivityPipelineActivitymathTypeDef
):
    pass


_ClientRunPipelineActivityPipelineActivityremoveAttributesTypeDef = TypedDict(
    "_ClientRunPipelineActivityPipelineActivityremoveAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivityremoveAttributesTypeDef(
    _ClientRunPipelineActivityPipelineActivityremoveAttributesTypeDef
):
    pass


_ClientRunPipelineActivityPipelineActivityselectAttributesTypeDef = TypedDict(
    "_ClientRunPipelineActivityPipelineActivityselectAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)


class ClientRunPipelineActivityPipelineActivityselectAttributesTypeDef(
    _ClientRunPipelineActivityPipelineActivityselectAttributesTypeDef
):
    pass


_ClientRunPipelineActivityPipelineActivityTypeDef = TypedDict(
    "_ClientRunPipelineActivityPipelineActivityTypeDef",
    {
        "channel": ClientRunPipelineActivityPipelineActivitychannelTypeDef,
        "lambda": ClientRunPipelineActivityPipelineActivitylambdaTypeDef,
        "datastore": ClientRunPipelineActivityPipelineActivitydatastoreTypeDef,
        "addAttributes": ClientRunPipelineActivityPipelineActivityaddAttributesTypeDef,
        "removeAttributes": ClientRunPipelineActivityPipelineActivityremoveAttributesTypeDef,
        "selectAttributes": ClientRunPipelineActivityPipelineActivityselectAttributesTypeDef,
        "filter": ClientRunPipelineActivityPipelineActivityfilterTypeDef,
        "math": ClientRunPipelineActivityPipelineActivitymathTypeDef,
        "deviceRegistryEnrich": ClientRunPipelineActivityPipelineActivitydeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientRunPipelineActivityPipelineActivitydeviceShadowEnrichTypeDef,
    },
    total=False,
)


class ClientRunPipelineActivityPipelineActivityTypeDef(
    _ClientRunPipelineActivityPipelineActivityTypeDef
):
    """
    The pipeline activity that is run. This must not be a 'channel' activity or a 'datastore'
    activity because these activities are used in a pipeline only to load the original message and
    to store the (possibly) transformed message. If a 'lambda' activity is specified, only
    short-running Lambda functions (those with a timeout of less than 30 seconds or less) can be
    used.
    - **channel** *(dict) --*

      Determines the source of the messages to be processed.
      - **name** *(string) --***[REQUIRED]**

        The name of the 'channel' activity.
    """


_ClientRunPipelineActivityResponseTypeDef = TypedDict(
    "_ClientRunPipelineActivityResponseTypeDef",
    {"payloads": List[bytes], "logResult": str},
    total=False,
)


class ClientRunPipelineActivityResponseTypeDef(_ClientRunPipelineActivityResponseTypeDef):
    """
    - *(dict) --*

      - **payloads** *(list) --*

        The enriched or transformed sample message payloads as base64-encoded strings. (The results
        of running the pipeline activity on each input sample message payload, encoded in base64.)
        - *(bytes) --*
    """


_ClientSampleChannelDataResponseTypeDef = TypedDict(
    "_ClientSampleChannelDataResponseTypeDef", {"payloads": List[bytes]}, total=False
)


class ClientSampleChannelDataResponseTypeDef(_ClientSampleChannelDataResponseTypeDef):
    """
    - *(dict) --*

      - **payloads** *(list) --*

        The list of message samples. Each sample message is returned as a base64-encoded string.
        - *(bytes) --*
    """


_ClientStartPipelineReprocessingResponseTypeDef = TypedDict(
    "_ClientStartPipelineReprocessingResponseTypeDef", {"reprocessingId": str}, total=False
)


class ClientStartPipelineReprocessingResponseTypeDef(
    _ClientStartPipelineReprocessingResponseTypeDef
):
    """
    - *(dict) --*

      - **reprocessingId** *(string) --*

        The ID of the pipeline reprocessing activity that was started.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      A set of key/value pairs which are used to manage the resource.
      - **key** *(string) --***[REQUIRED]**

        The tag's key.
    """


_ClientUpdateChannelChannelStoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientUpdateChannelChannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientUpdateChannelChannelStoragecustomerManagedS3TypeDef(
    _ClientUpdateChannelChannelStoragecustomerManagedS3TypeDef
):
    pass


_ClientUpdateChannelChannelStorageTypeDef = TypedDict(
    "_ClientUpdateChannelChannelStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientUpdateChannelChannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientUpdateChannelChannelStorageTypeDef(_ClientUpdateChannelChannelStorageTypeDef):
    """
    Where channel data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
    storage. If not specified, the default is "serviceManagedS3". This cannot be changed after
    creation of the channel.
    - **serviceManagedS3** *(dict) --*

      Use this to store channel data in an S3 bucket managed by the AWS IoT Analytics service. The
      choice of service-managed or customer-managed S3 storage cannot be changed after creation of
      the channel.
    """


_ClientUpdateChannelRetentionPeriodTypeDef = TypedDict(
    "_ClientUpdateChannelRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientUpdateChannelRetentionPeriodTypeDef(_ClientUpdateChannelRetentionPeriodTypeDef):
    """
    How long, in days, message data is kept for the channel. The retention period cannot be updated
    if the channel's S3 storage is customer-managed.
    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.
    """


_ClientUpdateDatasetActionscontainerActionresourceConfigurationTypeDef = TypedDict(
    "_ClientUpdateDatasetActionscontainerActionresourceConfigurationTypeDef",
    {"computeType": Literal["ACU_1", "ACU_2"], "volumeSizeInGB": int},
    total=False,
)


class ClientUpdateDatasetActionscontainerActionresourceConfigurationTypeDef(
    _ClientUpdateDatasetActionscontainerActionresourceConfigurationTypeDef
):
    pass


_ClientUpdateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef = TypedDict(
    "_ClientUpdateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef",
    {"datasetName": str},
    total=False,
)


class ClientUpdateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef(
    _ClientUpdateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef
):
    pass


_ClientUpdateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef = TypedDict(
    "_ClientUpdateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef",
    {"fileName": str},
    total=False,
)


class ClientUpdateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef(
    _ClientUpdateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef
):
    pass


_ClientUpdateDatasetActionscontainerActionvariablesTypeDef = TypedDict(
    "_ClientUpdateDatasetActionscontainerActionvariablesTypeDef",
    {
        "name": str,
        "stringValue": str,
        "doubleValue": float,
        "datasetContentVersionValue": ClientUpdateDatasetActionscontainerActionvariablesdatasetContentVersionValueTypeDef,
        "outputFileUriValue": ClientUpdateDatasetActionscontainerActionvariablesoutputFileUriValueTypeDef,
    },
    total=False,
)


class ClientUpdateDatasetActionscontainerActionvariablesTypeDef(
    _ClientUpdateDatasetActionscontainerActionvariablesTypeDef
):
    pass


_ClientUpdateDatasetActionscontainerActionTypeDef = TypedDict(
    "_ClientUpdateDatasetActionscontainerActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ClientUpdateDatasetActionscontainerActionresourceConfigurationTypeDef,
        "variables": List[ClientUpdateDatasetActionscontainerActionvariablesTypeDef],
    },
    total=False,
)


class ClientUpdateDatasetActionscontainerActionTypeDef(
    _ClientUpdateDatasetActionscontainerActionTypeDef
):
    pass


_ClientUpdateDatasetActionsqueryActionfiltersdeltaTimeTypeDef = TypedDict(
    "_ClientUpdateDatasetActionsqueryActionfiltersdeltaTimeTypeDef",
    {"offsetSeconds": int, "timeExpression": str},
    total=False,
)


class ClientUpdateDatasetActionsqueryActionfiltersdeltaTimeTypeDef(
    _ClientUpdateDatasetActionsqueryActionfiltersdeltaTimeTypeDef
):
    pass


_ClientUpdateDatasetActionsqueryActionfiltersTypeDef = TypedDict(
    "_ClientUpdateDatasetActionsqueryActionfiltersTypeDef",
    {"deltaTime": ClientUpdateDatasetActionsqueryActionfiltersdeltaTimeTypeDef},
    total=False,
)


class ClientUpdateDatasetActionsqueryActionfiltersTypeDef(
    _ClientUpdateDatasetActionsqueryActionfiltersTypeDef
):
    pass


_ClientUpdateDatasetActionsqueryActionTypeDef = TypedDict(
    "_ClientUpdateDatasetActionsqueryActionTypeDef",
    {"sqlQuery": str, "filters": List[ClientUpdateDatasetActionsqueryActionfiltersTypeDef]},
    total=False,
)


class ClientUpdateDatasetActionsqueryActionTypeDef(_ClientUpdateDatasetActionsqueryActionTypeDef):
    pass


_ClientUpdateDatasetActionsTypeDef = TypedDict(
    "_ClientUpdateDatasetActionsTypeDef",
    {
        "actionName": str,
        "queryAction": ClientUpdateDatasetActionsqueryActionTypeDef,
        "containerAction": ClientUpdateDatasetActionscontainerActionTypeDef,
    },
    total=False,
)


class ClientUpdateDatasetActionsTypeDef(_ClientUpdateDatasetActionsTypeDef):
    """
    - *(dict) --*

      A "DatasetAction" object that specifies how data set contents are automatically created.
      - **actionName** *(string) --*

        The name of the data set action by which data set contents are automatically created.
    """


_ClientUpdateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef = TypedDict(
    "_ClientUpdateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef",
    {"inputName": str, "roleArn": str},
    total=False,
)


class ClientUpdateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef(
    _ClientUpdateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef
):
    pass


_ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef = TypedDict(
    "_ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef",
    {"tableName": str, "databaseName": str},
    total=False,
)


class ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef(
    _ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef
):
    pass


_ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef = TypedDict(
    "_ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "glueConfiguration": ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationglueConfigurationTypeDef,
        "roleArn": str,
    },
    total=False,
)


class ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef(
    _ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef
):
    pass


_ClientUpdateDatasetContentDeliveryRulesdestinationTypeDef = TypedDict(
    "_ClientUpdateDatasetContentDeliveryRulesdestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": ClientUpdateDatasetContentDeliveryRulesdestinationiotEventsDestinationConfigurationTypeDef,
        "s3DestinationConfiguration": ClientUpdateDatasetContentDeliveryRulesdestinations3DestinationConfigurationTypeDef,
    },
    total=False,
)


class ClientUpdateDatasetContentDeliveryRulesdestinationTypeDef(
    _ClientUpdateDatasetContentDeliveryRulesdestinationTypeDef
):
    pass


_ClientUpdateDatasetContentDeliveryRulesTypeDef = TypedDict(
    "_ClientUpdateDatasetContentDeliveryRulesTypeDef",
    {"entryName": str, "destination": ClientUpdateDatasetContentDeliveryRulesdestinationTypeDef},
    total=False,
)


class ClientUpdateDatasetContentDeliveryRulesTypeDef(
    _ClientUpdateDatasetContentDeliveryRulesTypeDef
):
    """
    - *(dict) --*

      When data set contents are created they are delivered to destination specified here.
      - **entryName** *(string) --*

        The name of the data set content delivery rules entry.
    """


_ClientUpdateDatasetRetentionPeriodTypeDef = TypedDict(
    "_ClientUpdateDatasetRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientUpdateDatasetRetentionPeriodTypeDef(_ClientUpdateDatasetRetentionPeriodTypeDef):
    """
    How long, in days, data set contents are kept for the data set.
    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.
    """


_ClientUpdateDatasetTriggersdatasetTypeDef = TypedDict(
    "_ClientUpdateDatasetTriggersdatasetTypeDef", {"name": str}, total=False
)


class ClientUpdateDatasetTriggersdatasetTypeDef(_ClientUpdateDatasetTriggersdatasetTypeDef):
    pass


_ClientUpdateDatasetTriggersscheduleTypeDef = TypedDict(
    "_ClientUpdateDatasetTriggersscheduleTypeDef", {"expression": str}, total=False
)


class ClientUpdateDatasetTriggersscheduleTypeDef(_ClientUpdateDatasetTriggersscheduleTypeDef):
    """
    - **schedule** *(dict) --*

      The "Schedule" when the trigger is initiated.
      - **expression** *(string) --*

        The expression that defines when to trigger an update. For more information, see `Schedule
        Expressions for Rules
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in the
        Amazon CloudWatch Events User Guide.
    """


_ClientUpdateDatasetTriggersTypeDef = TypedDict(
    "_ClientUpdateDatasetTriggersTypeDef",
    {
        "schedule": ClientUpdateDatasetTriggersscheduleTypeDef,
        "dataset": ClientUpdateDatasetTriggersdatasetTypeDef,
    },
    total=False,
)


class ClientUpdateDatasetTriggersTypeDef(_ClientUpdateDatasetTriggersTypeDef):
    """
    - *(dict) --*

      The "DatasetTrigger" that specifies when the data set is automatically updated.
      - **schedule** *(dict) --*

        The "Schedule" when the trigger is initiated.
        - **expression** *(string) --*

          The expression that defines when to trigger an update. For more information, see `Schedule
          Expressions for Rules
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`__ in
          the Amazon CloudWatch Events User Guide.
    """


_ClientUpdateDatasetVersioningConfigurationTypeDef = TypedDict(
    "_ClientUpdateDatasetVersioningConfigurationTypeDef",
    {"unlimited": bool, "maxVersions": int},
    total=False,
)


class ClientUpdateDatasetVersioningConfigurationTypeDef(
    _ClientUpdateDatasetVersioningConfigurationTypeDef
):
    """
    [Optional] How many versions of data set contents are kept. If not specified or set to null,
    only the latest version plus the latest succeeded version (if they are different) are kept for
    the time period specified by the "retentionPeriod" parameter. (For more information, see
    https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions)
    - **unlimited** *(boolean) --*

      If true, unlimited versions of data set contents will be kept.
    """


_ClientUpdateDatastoreDatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "_ClientUpdateDatastoreDatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ClientUpdateDatastoreDatastoreStoragecustomerManagedS3TypeDef(
    _ClientUpdateDatastoreDatastoreStoragecustomerManagedS3TypeDef
):
    pass


_ClientUpdateDatastoreDatastoreStorageTypeDef = TypedDict(
    "_ClientUpdateDatastoreDatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ClientUpdateDatastoreDatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ClientUpdateDatastoreDatastoreStorageTypeDef(_ClientUpdateDatastoreDatastoreStorageTypeDef):
    """
    Where data store data is stored. You may choose one of "serviceManagedS3" or "customerManagedS3"
    storage. If not specified, the default is "serviceManagedS3". This cannot be changed after the
    data store is created.
    - **serviceManagedS3** *(dict) --*

      Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics service.
      The choice of service-managed or customer-managed S3 storage cannot be changed after creation
      of the data store.
    """


_ClientUpdateDatastoreRetentionPeriodTypeDef = TypedDict(
    "_ClientUpdateDatastoreRetentionPeriodTypeDef",
    {"unlimited": bool, "numberOfDays": int},
    total=False,
)


class ClientUpdateDatastoreRetentionPeriodTypeDef(_ClientUpdateDatastoreRetentionPeriodTypeDef):
    """
    How long, in days, message data is kept for the data store. The retention period cannot be
    updated if the data store's S3 storage is customer-managed.
    - **unlimited** *(boolean) --*

      If true, message data is kept indefinitely.
    """


_ClientUpdatePipelinePipelineActivitiesaddAttributesTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitiesaddAttributesTypeDef",
    {"name": str, "attributes": Dict[str, str], "next": str},
    total=False,
)


class ClientUpdatePipelinePipelineActivitiesaddAttributesTypeDef(
    _ClientUpdatePipelinePipelineActivitiesaddAttributesTypeDef
):
    pass


_ClientUpdatePipelinePipelineActivitieschannelTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitieschannelTypeDef",
    {"name": str, "channelName": str, "next": str},
    total=False,
)


class ClientUpdatePipelinePipelineActivitieschannelTypeDef(
    _ClientUpdatePipelinePipelineActivitieschannelTypeDef
):
    pass


_ClientUpdatePipelinePipelineActivitiesdatastoreTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitiesdatastoreTypeDef",
    {"name": str, "datastoreName": str},
    total=False,
)


class ClientUpdatePipelinePipelineActivitiesdatastoreTypeDef(
    _ClientUpdatePipelinePipelineActivitiesdatastoreTypeDef
):
    pass


_ClientUpdatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)


class ClientUpdatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef(
    _ClientUpdatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef
):
    pass


_ClientUpdatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str, "next": str},
    total=False,
)


class ClientUpdatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef(
    _ClientUpdatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef
):
    pass


_ClientUpdatePipelinePipelineActivitiesfilterTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitiesfilterTypeDef",
    {"name": str, "filter": str, "next": str},
    total=False,
)


class ClientUpdatePipelinePipelineActivitiesfilterTypeDef(
    _ClientUpdatePipelinePipelineActivitiesfilterTypeDef
):
    pass


_ClientUpdatePipelinePipelineActivitieslambdaTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitieslambdaTypeDef",
    {"name": str, "lambdaName": str, "batchSize": int, "next": str},
    total=False,
)


class ClientUpdatePipelinePipelineActivitieslambdaTypeDef(
    _ClientUpdatePipelinePipelineActivitieslambdaTypeDef
):
    pass


_ClientUpdatePipelinePipelineActivitiesmathTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitiesmathTypeDef",
    {"name": str, "attribute": str, "math": str, "next": str},
    total=False,
)


class ClientUpdatePipelinePipelineActivitiesmathTypeDef(
    _ClientUpdatePipelinePipelineActivitiesmathTypeDef
):
    pass


_ClientUpdatePipelinePipelineActivitiesremoveAttributesTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitiesremoveAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)


class ClientUpdatePipelinePipelineActivitiesremoveAttributesTypeDef(
    _ClientUpdatePipelinePipelineActivitiesremoveAttributesTypeDef
):
    pass


_ClientUpdatePipelinePipelineActivitiesselectAttributesTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitiesselectAttributesTypeDef",
    {"name": str, "attributes": List[str], "next": str},
    total=False,
)


class ClientUpdatePipelinePipelineActivitiesselectAttributesTypeDef(
    _ClientUpdatePipelinePipelineActivitiesselectAttributesTypeDef
):
    pass


_ClientUpdatePipelinePipelineActivitiesTypeDef = TypedDict(
    "_ClientUpdatePipelinePipelineActivitiesTypeDef",
    {
        "channel": ClientUpdatePipelinePipelineActivitieschannelTypeDef,
        "lambda": ClientUpdatePipelinePipelineActivitieslambdaTypeDef,
        "datastore": ClientUpdatePipelinePipelineActivitiesdatastoreTypeDef,
        "addAttributes": ClientUpdatePipelinePipelineActivitiesaddAttributesTypeDef,
        "removeAttributes": ClientUpdatePipelinePipelineActivitiesremoveAttributesTypeDef,
        "selectAttributes": ClientUpdatePipelinePipelineActivitiesselectAttributesTypeDef,
        "filter": ClientUpdatePipelinePipelineActivitiesfilterTypeDef,
        "math": ClientUpdatePipelinePipelineActivitiesmathTypeDef,
        "deviceRegistryEnrich": ClientUpdatePipelinePipelineActivitiesdeviceRegistryEnrichTypeDef,
        "deviceShadowEnrich": ClientUpdatePipelinePipelineActivitiesdeviceShadowEnrichTypeDef,
    },
    total=False,
)


class ClientUpdatePipelinePipelineActivitiesTypeDef(_ClientUpdatePipelinePipelineActivitiesTypeDef):
    pass


_ListChannelsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListChannelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListChannelsPaginatePaginationConfigTypeDef(_ListChannelsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef = TypedDict(
    "_ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef(
    _ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef
):
    pass


_ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef = TypedDict(
    "_ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ListChannelsPaginateResponsechannelSummarieschannelStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef(
    _ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef
):
    pass


_ListChannelsPaginateResponsechannelSummariesTypeDef = TypedDict(
    "_ListChannelsPaginateResponsechannelSummariesTypeDef",
    {
        "channelName": str,
        "channelStorage": ListChannelsPaginateResponsechannelSummarieschannelStorageTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ListChannelsPaginateResponsechannelSummariesTypeDef(
    _ListChannelsPaginateResponsechannelSummariesTypeDef
):
    """
    - *(dict) --*

      A summary of information about a channel.
      - **channelName** *(string) --*

        The name of the channel.
    """


_ListChannelsPaginateResponseTypeDef = TypedDict(
    "_ListChannelsPaginateResponseTypeDef",
    {
        "channelSummaries": List[ListChannelsPaginateResponsechannelSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListChannelsPaginateResponseTypeDef(_ListChannelsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **channelSummaries** *(list) --*

        A list of "ChannelSummary" objects.
        - *(dict) --*

          A summary of information about a channel.
          - **channelName** *(string) --*

            The name of the channel.
    """


_ListDatasetContentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatasetContentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatasetContentsPaginatePaginationConfigTypeDef(
    _ListDatasetContentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef = TypedDict(
    "_ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef",
    {"state": Literal["CREATING", "SUCCEEDED", "FAILED"], "reason": str},
    total=False,
)


class ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef(
    _ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef
):
    pass


_ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef = TypedDict(
    "_ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef",
    {
        "version": str,
        "status": ListDatasetContentsPaginateResponsedatasetContentSummariesstatusTypeDef,
        "creationTime": datetime,
        "scheduleTime": datetime,
        "completionTime": datetime,
    },
    total=False,
)


class ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef(
    _ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef
):
    """
    - *(dict) --*

      Summary information about data set contents.
      - **version** *(string) --*

        The version of the data set contents.
    """


_ListDatasetContentsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetContentsPaginateResponseTypeDef",
    {
        "datasetContentSummaries": List[
            ListDatasetContentsPaginateResponsedatasetContentSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListDatasetContentsPaginateResponseTypeDef(_ListDatasetContentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **datasetContentSummaries** *(list) --*

        Summary information about data set contents that have been created.
        - *(dict) --*

          Summary information about data set contents.
          - **version** *(string) --*

            The version of the data set contents.
    """


_ListDatasetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatasetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatasetsPaginatePaginationConfigTypeDef(_ListDatasetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef",
    {"actionName": str, "actionType": Literal["QUERY", "CONTAINER"]},
    total=False,
)


class ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef(
    _ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef
):
    pass


_ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef",
    {"name": str},
    total=False,
)


class ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef(
    _ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef
):
    pass


_ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef",
    {"expression": str},
    total=False,
)


class ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef(
    _ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef
):
    pass


_ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef",
    {
        "schedule": ListDatasetsPaginateResponsedatasetSummariestriggersscheduleTypeDef,
        "dataset": ListDatasetsPaginateResponsedatasetSummariestriggersdatasetTypeDef,
    },
    total=False,
)


class ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef(
    _ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef
):
    pass


_ListDatasetsPaginateResponsedatasetSummariesTypeDef = TypedDict(
    "_ListDatasetsPaginateResponsedatasetSummariesTypeDef",
    {
        "datasetName": str,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "triggers": List[ListDatasetsPaginateResponsedatasetSummariestriggersTypeDef],
        "actions": List[ListDatasetsPaginateResponsedatasetSummariesactionsTypeDef],
    },
    total=False,
)


class ListDatasetsPaginateResponsedatasetSummariesTypeDef(
    _ListDatasetsPaginateResponsedatasetSummariesTypeDef
):
    """
    - *(dict) --*

      A summary of information about a data set.
      - **datasetName** *(string) --*

        The name of the data set.
    """


_ListDatasetsPaginateResponseTypeDef = TypedDict(
    "_ListDatasetsPaginateResponseTypeDef",
    {
        "datasetSummaries": List[ListDatasetsPaginateResponsedatasetSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListDatasetsPaginateResponseTypeDef(_ListDatasetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **datasetSummaries** *(list) --*

        A list of "DatasetSummary" objects.
        - *(dict) --*

          A summary of information about a data set.
          - **datasetName** *(string) --*

            The name of the data set.
    """


_ListDatastoresPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDatastoresPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDatastoresPaginatePaginationConfigTypeDef(_ListDatastoresPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef = TypedDict(
    "_ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef",
    {"bucket": str, "keyPrefix": str, "roleArn": str},
    total=False,
)


class ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef(
    _ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef
):
    pass


_ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef = TypedDict(
    "_ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef",
    {
        "serviceManagedS3": Dict[str, Any],
        "customerManagedS3": ListDatastoresPaginateResponsedatastoreSummariesdatastoreStoragecustomerManagedS3TypeDef,
    },
    total=False,
)


class ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef(
    _ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef
):
    pass


_ListDatastoresPaginateResponsedatastoreSummariesTypeDef = TypedDict(
    "_ListDatastoresPaginateResponsedatastoreSummariesTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": ListDatastoresPaginateResponsedatastoreSummariesdatastoreStorageTypeDef,
        "status": Literal["CREATING", "ACTIVE", "DELETING"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ListDatastoresPaginateResponsedatastoreSummariesTypeDef(
    _ListDatastoresPaginateResponsedatastoreSummariesTypeDef
):
    """
    - *(dict) --*

      A summary of information about a data store.
      - **datastoreName** *(string) --*

        The name of the data store.
    """


_ListDatastoresPaginateResponseTypeDef = TypedDict(
    "_ListDatastoresPaginateResponseTypeDef",
    {
        "datastoreSummaries": List[ListDatastoresPaginateResponsedatastoreSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListDatastoresPaginateResponseTypeDef(_ListDatastoresPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **datastoreSummaries** *(list) --*

        A list of "DatastoreSummary" objects.
        - *(dict) --*

          A summary of information about a data store.
          - **datastoreName** *(string) --*

            The name of the data store.
    """


_ListPipelinesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPipelinesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPipelinesPaginatePaginationConfigTypeDef(_ListPipelinesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef",
    {
        "id": str,
        "status": Literal["RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "creationTime": datetime,
    },
    total=False,
)


class ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef(
    _ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef
):
    pass


_ListPipelinesPaginateResponsepipelineSummariesTypeDef = TypedDict(
    "_ListPipelinesPaginateResponsepipelineSummariesTypeDef",
    {
        "pipelineName": str,
        "reprocessingSummaries": List[
            ListPipelinesPaginateResponsepipelineSummariesreprocessingSummariesTypeDef
        ],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)


class ListPipelinesPaginateResponsepipelineSummariesTypeDef(
    _ListPipelinesPaginateResponsepipelineSummariesTypeDef
):
    """
    - *(dict) --*

      A summary of information about a pipeline.
      - **pipelineName** *(string) --*

        The name of the pipeline.
    """


_ListPipelinesPaginateResponseTypeDef = TypedDict(
    "_ListPipelinesPaginateResponseTypeDef",
    {
        "pipelineSummaries": List[ListPipelinesPaginateResponsepipelineSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPipelinesPaginateResponseTypeDef(_ListPipelinesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **pipelineSummaries** *(list) --*

        A list of "PipelineSummary" objects.
        - *(dict) --*

          A summary of information about a pipeline.
          - **pipelineName** *(string) --*

            The name of the pipeline.
    """
