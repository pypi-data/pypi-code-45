"Main interface for xray service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "BatchGetTracesPaginatePaginationConfigTypeDef",
    "BatchGetTracesPaginateResponseTracesSegmentsTypeDef",
    "BatchGetTracesPaginateResponseTracesTypeDef",
    "BatchGetTracesPaginateResponseTypeDef",
    "ClientBatchGetTracesResponseTracesSegmentsTypeDef",
    "ClientBatchGetTracesResponseTracesTypeDef",
    "ClientBatchGetTracesResponseTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    "ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef",
    "ClientCreateSamplingRuleResponseTypeDef",
    "ClientCreateSamplingRuleSamplingRuleTypeDef",
    "ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    "ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef",
    "ClientDeleteSamplingRuleResponseTypeDef",
    "ClientGetEncryptionConfigResponseEncryptionConfigTypeDef",
    "ClientGetEncryptionConfigResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetGroupsResponseGroupsTypeDef",
    "ClientGetGroupsResponseTypeDef",
    "ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef",
    "ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef",
    "ClientGetSamplingRulesResponseTypeDef",
    "ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef",
    "ClientGetSamplingStatisticSummariesResponseTypeDef",
    "ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef",
    "ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef",
    "ClientGetSamplingTargetsResponseTypeDef",
    "ClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef",
    "ClientGetServiceGraphResponseServicesDurationHistogramTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesEdgesTypeDef",
    "ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef",
    "ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef",
    "ClientGetServiceGraphResponseServicesTypeDef",
    "ClientGetServiceGraphResponseTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef",
    "ClientGetTimeSeriesServiceStatisticsResponseTypeDef",
    "ClientGetTraceGraphResponseServicesDurationHistogramTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesEdgesTypeDef",
    "ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef",
    "ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef",
    "ClientGetTraceGraphResponseServicesTypeDef",
    "ClientGetTraceGraphResponseTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef",
    "ClientGetTraceSummariesResponseTraceSummariesTypeDef",
    "ClientGetTraceSummariesResponseTypeDef",
    "ClientGetTraceSummariesSamplingStrategyTypeDef",
    "ClientPutEncryptionConfigResponseEncryptionConfigTypeDef",
    "ClientPutEncryptionConfigResponseTypeDef",
    "ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef",
    "ClientPutTelemetryRecordsTelemetryRecordsTypeDef",
    "ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef",
    "ClientPutTraceSegmentsResponseTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    "ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef",
    "ClientUpdateSamplingRuleResponseTypeDef",
    "ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef",
    "GetGroupsPaginatePaginationConfigTypeDef",
    "GetGroupsPaginateResponseGroupsTypeDef",
    "GetGroupsPaginateResponseTypeDef",
    "GetSamplingRulesPaginatePaginationConfigTypeDef",
    "GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef",
    "GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef",
    "GetSamplingRulesPaginateResponseTypeDef",
    "GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef",
    "GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef",
    "GetSamplingStatisticSummariesPaginateResponseTypeDef",
    "GetServiceGraphPaginatePaginationConfigTypeDef",
    "GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesEdgesTypeDef",
    "GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef",
    "GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef",
    "GetServiceGraphPaginateResponseServicesTypeDef",
    "GetServiceGraphPaginateResponseTypeDef",
    "GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef",
    "GetTimeSeriesServiceStatisticsPaginateResponseTypeDef",
    "GetTraceGraphPaginatePaginationConfigTypeDef",
    "GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesEdgesTypeDef",
    "GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef",
    "GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef",
    "GetTraceGraphPaginateResponseServicesTypeDef",
    "GetTraceGraphPaginateResponseTypeDef",
    "GetTraceSummariesPaginatePaginationConfigTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef",
    "GetTraceSummariesPaginateResponseTraceSummariesTypeDef",
    "GetTraceSummariesPaginateResponseTypeDef",
    "GetTraceSummariesPaginateSamplingStrategyTypeDef",
)


_BatchGetTracesPaginatePaginationConfigTypeDef = TypedDict(
    "_BatchGetTracesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class BatchGetTracesPaginatePaginationConfigTypeDef(_BatchGetTracesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_BatchGetTracesPaginateResponseTracesSegmentsTypeDef = TypedDict(
    "_BatchGetTracesPaginateResponseTracesSegmentsTypeDef",
    {"Id": str, "Document": str},
    total=False,
)


class BatchGetTracesPaginateResponseTracesSegmentsTypeDef(
    _BatchGetTracesPaginateResponseTracesSegmentsTypeDef
):
    pass


_BatchGetTracesPaginateResponseTracesTypeDef = TypedDict(
    "_BatchGetTracesPaginateResponseTracesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "Segments": List[BatchGetTracesPaginateResponseTracesSegmentsTypeDef],
    },
    total=False,
)


class BatchGetTracesPaginateResponseTracesTypeDef(_BatchGetTracesPaginateResponseTracesTypeDef):
    """
    - *(dict) --*

      A collection of segment documents with matching trace IDs.
      - **Id** *(string) --*

        The unique identifier for the request that generated the trace's segments and subsegments.
    """


_BatchGetTracesPaginateResponseTypeDef = TypedDict(
    "_BatchGetTracesPaginateResponseTypeDef",
    {"Traces": List[BatchGetTracesPaginateResponseTracesTypeDef], "UnprocessedTraceIds": List[str]},
    total=False,
)


class BatchGetTracesPaginateResponseTypeDef(_BatchGetTracesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Traces** *(list) --*

        Full traces for the specified requests.
        - *(dict) --*

          A collection of segment documents with matching trace IDs.
          - **Id** *(string) --*

            The unique identifier for the request that generated the trace's segments and
            subsegments.
    """


_ClientBatchGetTracesResponseTracesSegmentsTypeDef = TypedDict(
    "_ClientBatchGetTracesResponseTracesSegmentsTypeDef", {"Id": str, "Document": str}, total=False
)


class ClientBatchGetTracesResponseTracesSegmentsTypeDef(
    _ClientBatchGetTracesResponseTracesSegmentsTypeDef
):
    pass


_ClientBatchGetTracesResponseTracesTypeDef = TypedDict(
    "_ClientBatchGetTracesResponseTracesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "Segments": List[ClientBatchGetTracesResponseTracesSegmentsTypeDef],
    },
    total=False,
)


class ClientBatchGetTracesResponseTracesTypeDef(_ClientBatchGetTracesResponseTracesTypeDef):
    """
    - *(dict) --*

      A collection of segment documents with matching trace IDs.
      - **Id** *(string) --*

        The unique identifier for the request that generated the trace's segments and subsegments.
    """


_ClientBatchGetTracesResponseTypeDef = TypedDict(
    "_ClientBatchGetTracesResponseTypeDef",
    {
        "Traces": List[ClientBatchGetTracesResponseTracesTypeDef],
        "UnprocessedTraceIds": List[str],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchGetTracesResponseTypeDef(_ClientBatchGetTracesResponseTypeDef):
    """
    - *(dict) --*

      - **Traces** *(list) --*

        Full traces for the specified requests.
        - *(dict) --*

          A collection of segment documents with matching trace IDs.
          - **Id** *(string) --*

            The unique identifier for the request that generated the trace's segments and
            subsegments.
    """


_ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "_ClientCreateGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)


class ClientCreateGroupResponseGroupTypeDef(_ClientCreateGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      The group that was created. Contains the name of the group that was created, the ARN of the
      group that was generated based on the group name, and the filter expression that was assigned
      to the group.
      - **GroupName** *(string) --*

        The unique case-sensitive name of the group.
    """


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        The group that was created. Contains the name of the group that was created, the ARN of the
        group that was generated based on the group name, and the filter expression that was
        assigned to the group.
        - **GroupName** *(string) --*

          The unique case-sensitive name of the group.
    """


_ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "_ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef(
    _ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef
):
    """
    - **SamplingRule** *(dict) --*

      The sampling rule.
      - **RuleName** *(string) --*

        The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "_ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)


class ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef(
    _ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef
):
    """
    - **SamplingRuleRecord** *(dict) --*

      The saved rule definition and metadata.
      - **SamplingRule** *(dict) --*

        The sampling rule.
        - **RuleName** *(string) --*

          The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientCreateSamplingRuleResponseTypeDef = TypedDict(
    "_ClientCreateSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)


class ClientCreateSamplingRuleResponseTypeDef(_ClientCreateSamplingRuleResponseTypeDef):
    """
    - *(dict) --*

      - **SamplingRuleRecord** *(dict) --*

        The saved rule definition and metadata.
        - **SamplingRule** *(dict) --*

          The sampling rule.
          - **RuleName** *(string) --*

            The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientCreateSamplingRuleSamplingRuleTypeDef = TypedDict(
    "_ClientCreateSamplingRuleSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientCreateSamplingRuleSamplingRuleTypeDef(_ClientCreateSamplingRuleSamplingRuleTypeDef):
    """
    The rule definition.
    - **RuleName** *(string) --*

      The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "_ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef(
    _ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef
):
    """
    - **SamplingRule** *(dict) --*

      The sampling rule.
      - **RuleName** *(string) --*

        The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "_ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)


class ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef(
    _ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef
):
    """
    - **SamplingRuleRecord** *(dict) --*

      The deleted rule definition and metadata.
      - **SamplingRule** *(dict) --*

        The sampling rule.
        - **RuleName** *(string) --*

          The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientDeleteSamplingRuleResponseTypeDef = TypedDict(
    "_ClientDeleteSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)


class ClientDeleteSamplingRuleResponseTypeDef(_ClientDeleteSamplingRuleResponseTypeDef):
    """
    - *(dict) --*

      - **SamplingRuleRecord** *(dict) --*

        The deleted rule definition and metadata.
        - **SamplingRule** *(dict) --*

          The sampling rule.
          - **RuleName** *(string) --*

            The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientGetEncryptionConfigResponseEncryptionConfigTypeDef = TypedDict(
    "_ClientGetEncryptionConfigResponseEncryptionConfigTypeDef",
    {"KeyId": str, "Status": Literal["UPDATING", "ACTIVE"], "Type": Literal["NONE", "KMS"]},
    total=False,
)


class ClientGetEncryptionConfigResponseEncryptionConfigTypeDef(
    _ClientGetEncryptionConfigResponseEncryptionConfigTypeDef
):
    """
    - **EncryptionConfig** *(dict) --*

      The encryption configuration document.
      - **KeyId** *(string) --*

        The ID of the customer master key (CMK) used for encryption, if applicable.
    """


_ClientGetEncryptionConfigResponseTypeDef = TypedDict(
    "_ClientGetEncryptionConfigResponseTypeDef",
    {"EncryptionConfig": ClientGetEncryptionConfigResponseEncryptionConfigTypeDef},
    total=False,
)


class ClientGetEncryptionConfigResponseTypeDef(_ClientGetEncryptionConfigResponseTypeDef):
    """
    - *(dict) --*

      - **EncryptionConfig** *(dict) --*

        The encryption configuration document.
        - **KeyId** *(string) --*

          The ID of the customer master key (CMK) used for encryption, if applicable.
    """


_ClientGetGroupResponseGroupTypeDef = TypedDict(
    "_ClientGetGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)


class ClientGetGroupResponseGroupTypeDef(_ClientGetGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      The group that was requested. Contains the name of the group, the ARN of the group, and the
      filter expression that assigned to the group.
      - **GroupName** *(string) --*

        The unique case-sensitive name of the group.
    """


_ClientGetGroupResponseTypeDef = TypedDict(
    "_ClientGetGroupResponseTypeDef", {"Group": ClientGetGroupResponseGroupTypeDef}, total=False
)


class ClientGetGroupResponseTypeDef(_ClientGetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        The group that was requested. Contains the name of the group, the ARN of the group, and the
        filter expression that assigned to the group.
        - **GroupName** *(string) --*

          The unique case-sensitive name of the group.
    """


_ClientGetGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientGetGroupsResponseGroupsTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)


class ClientGetGroupsResponseGroupsTypeDef(_ClientGetGroupsResponseGroupsTypeDef):
    """
    - *(dict) --*

      Details for a group without metadata.
      - **GroupName** *(string) --*

        The unique case-sensitive name of the group.
    """


_ClientGetGroupsResponseTypeDef = TypedDict(
    "_ClientGetGroupsResponseTypeDef",
    {"Groups": List[ClientGetGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetGroupsResponseTypeDef(_ClientGetGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*

        The collection of all active groups.
        - *(dict) --*

          Details for a group without metadata.
          - **GroupName** *(string) --*

            The unique case-sensitive name of the group.
    """


_ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef = TypedDict(
    "_ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef(
    _ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef
):
    """
    - **SamplingRule** *(dict) --*

      The sampling rule.
      - **RuleName** *(string) --*

        The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef = TypedDict(
    "_ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef",
    {
        "SamplingRule": ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)


class ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef(
    _ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef
):
    """
    - *(dict) --*

      A  SamplingRule and its metadata.
      - **SamplingRule** *(dict) --*

        The sampling rule.
        - **RuleName** *(string) --*

          The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientGetSamplingRulesResponseTypeDef = TypedDict(
    "_ClientGetSamplingRulesResponseTypeDef",
    {
        "SamplingRuleRecords": List[ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetSamplingRulesResponseTypeDef(_ClientGetSamplingRulesResponseTypeDef):
    """
    - *(dict) --*

      - **SamplingRuleRecords** *(list) --*

        Rule definitions and metadata.
        - *(dict) --*

          A  SamplingRule and its metadata.
          - **SamplingRule** *(dict) --*

            The sampling rule.
            - **RuleName** *(string) --*

              The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef = TypedDict(
    "_ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef",
    {
        "RuleName": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "BorrowCount": int,
        "SampledCount": int,
    },
    total=False,
)


class ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef(
    _ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef
):
    """
    - *(dict) --*

      Aggregated request sampling data for a sampling rule across all services for a 10 second
      window.
      - **RuleName** *(string) --*

        The name of the sampling rule.
    """


_ClientGetSamplingStatisticSummariesResponseTypeDef = TypedDict(
    "_ClientGetSamplingStatisticSummariesResponseTypeDef",
    {
        "SamplingStatisticSummaries": List[
            ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetSamplingStatisticSummariesResponseTypeDef(
    _ClientGetSamplingStatisticSummariesResponseTypeDef
):
    """
    - *(dict) --*

      - **SamplingStatisticSummaries** *(list) --*

        Information about the number of requests instrumented for each sampling rule.
        - *(dict) --*

          Aggregated request sampling data for a sampling rule across all services for a 10 second
          window.
          - **RuleName** *(string) --*

            The name of the sampling rule.
    """


_ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef = TypedDict(
    "_ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef",
    {
        "RuleName": str,
        "FixedRate": float,
        "ReservoirQuota": int,
        "ReservoirQuotaTTL": datetime,
        "Interval": int,
    },
    total=False,
)


class ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef(
    _ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef
):
    """
    - *(dict) --*

      Temporary changes to a sampling rule configuration. To meet the global sampling target for a
      rule, X-Ray calculates a new reservoir for each service based on the recent sampling results
      of all services that called  GetSamplingTargets .
      - **RuleName** *(string) --*

        The name of the sampling rule.
    """


_ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef = TypedDict(
    "_ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef",
    {"RuleName": str, "ErrorCode": str, "Message": str},
    total=False,
)


class ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef(
    _ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef
):
    pass


_ClientGetSamplingTargetsResponseTypeDef = TypedDict(
    "_ClientGetSamplingTargetsResponseTypeDef",
    {
        "SamplingTargetDocuments": List[
            ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef
        ],
        "LastRuleModification": datetime,
        "UnprocessedStatistics": List[ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef],
    },
    total=False,
)


class ClientGetSamplingTargetsResponseTypeDef(_ClientGetSamplingTargetsResponseTypeDef):
    """
    - *(dict) --*

      - **SamplingTargetDocuments** *(list) --*

        Updated rules that the service should use to sample requests.
        - *(dict) --*

          Temporary changes to a sampling rule configuration. To meet the global sampling target for
          a rule, X-Ray calculates a new reservoir for each service based on the recent sampling
          results of all services that called  GetSamplingTargets .
          - **RuleName** *(string) --*

            The name of the sampling rule.
    """


_RequiredClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef = TypedDict(
    "_RequiredClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef", {"RuleName": str}
)
_OptionalClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef = TypedDict(
    "_OptionalClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef",
    {
        "ClientID": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "SampledCount": int,
        "BorrowCount": int,
    },
    total=False,
)


class ClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef(
    _RequiredClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef,
    _OptionalClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef,
):
    """
    - *(dict) --*

      Request sampling results for a single rule from a service. Results are for the last 10 seconds
      unless the service has been assigned a longer reporting interval after a previous call to
      GetSamplingTargets .
      - **RuleName** *(string) --***[REQUIRED]**

        The name of the sampling rule.
    """


_ClientGetServiceGraphResponseServicesDurationHistogramTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesDurationHistogramTypeDef(
    _ClientGetServiceGraphResponseServicesDurationHistogramTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesEdgesTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesEdgesTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef
        ],
        "Aliases": List[ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef],
    },
    total=False,
)


class ClientGetServiceGraphResponseServicesEdgesTypeDef(
    _ClientGetServiceGraphResponseServicesEdgesTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef(
    _ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef(
    _ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef
):
    pass


_ClientGetServiceGraphResponseServicesTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseServicesTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[ClientGetServiceGraphResponseServicesEdgesTypeDef],
        "SummaryStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef,
        "DurationHistogram": List[ClientGetServiceGraphResponseServicesDurationHistogramTypeDef],
        "ResponseTimeHistogram": List[
            ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class ClientGetServiceGraphResponseServicesTypeDef(_ClientGetServiceGraphResponseServicesTypeDef):
    pass


_ClientGetServiceGraphResponseTypeDef = TypedDict(
    "_ClientGetServiceGraphResponseTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List[ClientGetServiceGraphResponseServicesTypeDef],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)


class ClientGetServiceGraphResponseTypeDef(_ClientGetServiceGraphResponseTypeDef):
    """
    - *(dict) --*

      - **StartTime** *(datetime) --*

        The start of the time frame for which the graph was generated.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef
):
    pass


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef
):
    pass


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef
):
    pass


_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": datetime,
        "EdgeSummaryStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef,
        "ServiceSummaryStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef
):
    """
    - *(dict) --*

      A list of TimeSeriesStatistic structures.
      - **Timestamp** *(datetime) --*

        Timestamp of the window for which statistics are aggregated.
    """


_ClientGetTimeSeriesServiceStatisticsResponseTypeDef = TypedDict(
    "_ClientGetTimeSeriesServiceStatisticsResponseTypeDef",
    {
        "TimeSeriesServiceStatistics": List[
            ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef
        ],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)


class ClientGetTimeSeriesServiceStatisticsResponseTypeDef(
    _ClientGetTimeSeriesServiceStatisticsResponseTypeDef
):
    """
    - *(dict) --*

      - **TimeSeriesServiceStatistics** *(list) --*

        The collection of statistics.
        - *(dict) --*

          A list of TimeSeriesStatistic structures.
          - **Timestamp** *(datetime) --*

            Timestamp of the window for which statistics are aggregated.
    """


_ClientGetTraceGraphResponseServicesDurationHistogramTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesDurationHistogramTypeDef(
    _ClientGetTraceGraphResponseServicesDurationHistogramTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesEdgesTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesEdgesTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef
        ],
        "Aliases": List[ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef],
    },
    total=False,
)


class ClientGetTraceGraphResponseServicesEdgesTypeDef(
    _ClientGetTraceGraphResponseServicesEdgesTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef(
    _ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef(
    _ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef
):
    pass


_ClientGetTraceGraphResponseServicesTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseServicesTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[ClientGetTraceGraphResponseServicesEdgesTypeDef],
        "SummaryStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef,
        "DurationHistogram": List[ClientGetTraceGraphResponseServicesDurationHistogramTypeDef],
        "ResponseTimeHistogram": List[
            ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class ClientGetTraceGraphResponseServicesTypeDef(_ClientGetTraceGraphResponseServicesTypeDef):
    """
    - *(dict) --*

      Information about an application that processed requests, users that made requests, or
      downstream services, resources and applications that an application used.
      - **ReferenceId** *(integer) --*

        Identifier for the service. Unique within the service map.
    """


_ClientGetTraceGraphResponseTypeDef = TypedDict(
    "_ClientGetTraceGraphResponseTypeDef",
    {"Services": List[ClientGetTraceGraphResponseServicesTypeDef], "NextToken": str},
    total=False,
)


class ClientGetTraceGraphResponseTypeDef(_ClientGetTraceGraphResponseTypeDef):
    """
    - *(dict) --*

      - **Services** *(list) --*

        The services that have processed one of the specified requests.
        - *(dict) --*

          Information about an application that processed requests, users that made requests, or
          downstream services, resources and applications that an application used.
          - **ReferenceId** *(integer) --*

            Identifier for the service. Unique within the service map.
    """


_ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    {"NumberValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef",
    {
        "AnnotationValue": ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef,
        "ServiceIds": List[
            ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef
        ],
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef",
    {"Services": List[ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef]},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef",
    {"Services": List[ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef]},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef",
    {"HttpURL": str, "HttpStatus": int, "HttpMethod": str, "UserAgent": str, "ClientIp": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef", {"Id": str}, total=False
)


class ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef", {"ARN": str}, total=False
)


class ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    {"Name": str, "Coverage": float, "Remote": bool},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef",
    {
        "Services": List[
            ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
        ]
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef",
    {
        "UserName": str,
        "ServiceIds": List[ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef],
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef
):
    pass


_ClientGetTraceSummariesResponseTraceSummariesTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTraceSummariesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "ResponseTime": float,
        "HasFault": bool,
        "HasError": bool,
        "HasThrottle": bool,
        "IsPartial": bool,
        "Http": ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef,
        "Annotations": Dict[
            str, List[ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef]
        ],
        "Users": List[ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef],
        "ServiceIds": List[ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef],
        "ResourceARNs": List[ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef],
        "InstanceIds": List[ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef],
        "AvailabilityZones": List[
            ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef
        ],
        "EntryPoint": ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef,
        "FaultRootCauses": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef
        ],
        "ErrorRootCauses": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef
        ],
        "ResponseTimeRootCauses": List[
            ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef
        ],
        "Revision": int,
        "MatchedEventTime": datetime,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTraceSummariesTypeDef(
    _ClientGetTraceSummariesResponseTraceSummariesTypeDef
):
    """
    - *(dict) --*

      Metadata generated from the segment documents in a trace.
      - **Id** *(string) --*

        The unique identifier for the request that generated the trace's segments and subsegments.
    """


_ClientGetTraceSummariesResponseTypeDef = TypedDict(
    "_ClientGetTraceSummariesResponseTypeDef",
    {
        "TraceSummaries": List[ClientGetTraceSummariesResponseTraceSummariesTypeDef],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
        "NextToken": str,
    },
    total=False,
)


class ClientGetTraceSummariesResponseTypeDef(_ClientGetTraceSummariesResponseTypeDef):
    """
    - *(dict) --*

      - **TraceSummaries** *(list) --*

        Trace IDs and metadata for traces that were found in the specified time frame.
        - *(dict) --*

          Metadata generated from the segment documents in a trace.
          - **Id** *(string) --*

            The unique identifier for the request that generated the trace's segments and
            subsegments.
    """


_ClientGetTraceSummariesSamplingStrategyTypeDef = TypedDict(
    "_ClientGetTraceSummariesSamplingStrategyTypeDef",
    {"Name": Literal["PartialScan", "FixedRate"], "Value": float},
    total=False,
)


class ClientGetTraceSummariesSamplingStrategyTypeDef(
    _ClientGetTraceSummariesSamplingStrategyTypeDef
):
    """
    A paramater to indicate whether to enable sampling on trace summaries. Input parameters are Name
    and Value.
    - **Name** *(string) --*

      The name of a sampling rule.
    """


_ClientPutEncryptionConfigResponseEncryptionConfigTypeDef = TypedDict(
    "_ClientPutEncryptionConfigResponseEncryptionConfigTypeDef",
    {"KeyId": str, "Status": Literal["UPDATING", "ACTIVE"], "Type": Literal["NONE", "KMS"]},
    total=False,
)


class ClientPutEncryptionConfigResponseEncryptionConfigTypeDef(
    _ClientPutEncryptionConfigResponseEncryptionConfigTypeDef
):
    """
    - **EncryptionConfig** *(dict) --*

      The new encryption configuration.
      - **KeyId** *(string) --*

        The ID of the customer master key (CMK) used for encryption, if applicable.
    """


_ClientPutEncryptionConfigResponseTypeDef = TypedDict(
    "_ClientPutEncryptionConfigResponseTypeDef",
    {"EncryptionConfig": ClientPutEncryptionConfigResponseEncryptionConfigTypeDef},
    total=False,
)


class ClientPutEncryptionConfigResponseTypeDef(_ClientPutEncryptionConfigResponseTypeDef):
    """
    - *(dict) --*

      - **EncryptionConfig** *(dict) --*

        The new encryption configuration.
        - **KeyId** *(string) --*

          The ID of the customer master key (CMK) used for encryption, if applicable.
    """


_ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef = TypedDict(
    "_ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef",
    {
        "TimeoutCount": int,
        "ConnectionRefusedCount": int,
        "HTTPCode4XXCount": int,
        "HTTPCode5XXCount": int,
        "UnknownHostCount": int,
        "OtherCount": int,
    },
    total=False,
)


class ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef(
    _ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef
):
    """
    - **BackendConnectionErrors** *(dict) --*

      - **TimeoutCount** *(integer) --*
      - **ConnectionRefusedCount** *(integer) --*
      - **HTTPCode4XXCount** *(integer) --*
      - **HTTPCode5XXCount** *(integer) --*
      - **UnknownHostCount** *(integer) --*
      - **OtherCount** *(integer) --*
    """


_RequiredClientPutTelemetryRecordsTelemetryRecordsTypeDef = TypedDict(
    "_RequiredClientPutTelemetryRecordsTelemetryRecordsTypeDef", {"Timestamp": datetime}
)
_OptionalClientPutTelemetryRecordsTelemetryRecordsTypeDef = TypedDict(
    "_OptionalClientPutTelemetryRecordsTelemetryRecordsTypeDef",
    {
        "SegmentsReceivedCount": int,
        "SegmentsSentCount": int,
        "SegmentsSpilloverCount": int,
        "SegmentsRejectedCount": int,
        "BackendConnectionErrors": ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef,
    },
    total=False,
)


class ClientPutTelemetryRecordsTelemetryRecordsTypeDef(
    _RequiredClientPutTelemetryRecordsTelemetryRecordsTypeDef,
    _OptionalClientPutTelemetryRecordsTelemetryRecordsTypeDef,
):
    """
    - *(dict) --*

      - **Timestamp** *(datetime) --***[REQUIRED]**
      - **SegmentsReceivedCount** *(integer) --*
      - **SegmentsSentCount** *(integer) --*
      - **SegmentsSpilloverCount** *(integer) --*
      - **SegmentsRejectedCount** *(integer) --*
      - **BackendConnectionErrors** *(dict) --*

        - **TimeoutCount** *(integer) --*
        - **ConnectionRefusedCount** *(integer) --*
        - **HTTPCode4XXCount** *(integer) --*
        - **HTTPCode5XXCount** *(integer) --*
        - **UnknownHostCount** *(integer) --*
        - **OtherCount** *(integer) --*
    """


_ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef = TypedDict(
    "_ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef",
    {"Id": str, "ErrorCode": str, "Message": str},
    total=False,
)


class ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef(
    _ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef
):
    """
    - *(dict) --*

      Information about a segment that failed processing.
      - **Id** *(string) --*

        The segment's ID.
    """


_ClientPutTraceSegmentsResponseTypeDef = TypedDict(
    "_ClientPutTraceSegmentsResponseTypeDef",
    {
        "UnprocessedTraceSegments": List[
            ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef
        ]
    },
    total=False,
)


class ClientPutTraceSegmentsResponseTypeDef(_ClientPutTraceSegmentsResponseTypeDef):
    """
    - *(dict) --*

      - **UnprocessedTraceSegments** *(list) --*

        Segments that failed processing.
        - *(dict) --*

          Information about a segment that failed processing.
          - **Id** *(string) --*

            The segment's ID.
    """


_ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "_ClientUpdateGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)


class ClientUpdateGroupResponseGroupTypeDef(_ClientUpdateGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      The group that was updated. Contains the name of the group that was updated, the ARN of the
      group that was updated, and the updated filter expression assigned to the group.
      - **GroupName** *(string) --*

        The unique case-sensitive name of the group.
    """


_ClientUpdateGroupResponseTypeDef = TypedDict(
    "_ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef},
    total=False,
)


class ClientUpdateGroupResponseTypeDef(_ClientUpdateGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        The group that was updated. Contains the name of the group that was updated, the ARN of the
        group that was updated, and the updated filter expression assigned to the group.
        - **GroupName** *(string) --*

          The unique case-sensitive name of the group.
    """


_ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "_ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef(
    _ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef
):
    """
    - **SamplingRule** *(dict) --*

      The sampling rule.
      - **RuleName** *(string) --*

        The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "_ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)


class ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef(
    _ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef
):
    """
    - **SamplingRuleRecord** *(dict) --*

      The updated rule definition and metadata.
      - **SamplingRule** *(dict) --*

        The sampling rule.
        - **RuleName** *(string) --*

          The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientUpdateSamplingRuleResponseTypeDef = TypedDict(
    "_ClientUpdateSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)


class ClientUpdateSamplingRuleResponseTypeDef(_ClientUpdateSamplingRuleResponseTypeDef):
    """
    - *(dict) --*

      - **SamplingRuleRecord** *(dict) --*

        The updated rule definition and metadata.
        - **SamplingRule** *(dict) --*

          The sampling rule.
          - **RuleName** *(string) --*

            The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef = TypedDict(
    "_ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "Host": str,
        "ServiceName": str,
        "ServiceType": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef(
    _ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef
):
    """
    The rule and fields to change.
    - **RuleName** *(string) --*

      The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_GetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetGroupsPaginatePaginationConfigTypeDef(_GetGroupsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_GetGroupsPaginateResponseGroupsTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)


class GetGroupsPaginateResponseGroupsTypeDef(_GetGroupsPaginateResponseGroupsTypeDef):
    """
    - *(dict) --*

      Details for a group without metadata.
      - **GroupName** *(string) --*

        The unique case-sensitive name of the group.
    """


_GetGroupsPaginateResponseTypeDef = TypedDict(
    "_GetGroupsPaginateResponseTypeDef",
    {"Groups": List[GetGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)


class GetGroupsPaginateResponseTypeDef(_GetGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Groups** *(list) --*

        The collection of all active groups.
        - *(dict) --*

          Details for a group without metadata.
          - **GroupName** *(string) --*

            The unique case-sensitive name of the group.
    """


_GetSamplingRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSamplingRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetSamplingRulesPaginatePaginationConfigTypeDef(
    _GetSamplingRulesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef = TypedDict(
    "_GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef(
    _GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef
):
    """
    - **SamplingRule** *(dict) --*

      The sampling rule.
      - **RuleName** *(string) --*

        The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef = TypedDict(
    "_GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef",
    {
        "SamplingRule": GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)


class GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef(
    _GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef
):
    """
    - *(dict) --*

      A  SamplingRule and its metadata.
      - **SamplingRule** *(dict) --*

        The sampling rule.
        - **RuleName** *(string) --*

          The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_GetSamplingRulesPaginateResponseTypeDef = TypedDict(
    "_GetSamplingRulesPaginateResponseTypeDef",
    {"SamplingRuleRecords": List[GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef]},
    total=False,
)


class GetSamplingRulesPaginateResponseTypeDef(_GetSamplingRulesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SamplingRuleRecords** *(list) --*

        Rule definitions and metadata.
        - *(dict) --*

          A  SamplingRule and its metadata.
          - **SamplingRule** *(dict) --*

            The sampling rule.
            - **RuleName** *(string) --*

              The name of the sampling rule. Specify a rule by either name or ARN, but not both.
    """


_GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef(
    _GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef = TypedDict(
    "_GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef",
    {
        "RuleName": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "BorrowCount": int,
        "SampledCount": int,
    },
    total=False,
)


class GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef(
    _GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef
):
    """
    - *(dict) --*

      Aggregated request sampling data for a sampling rule across all services for a 10 second
      window.
      - **RuleName** *(string) --*

        The name of the sampling rule.
    """


_GetSamplingStatisticSummariesPaginateResponseTypeDef = TypedDict(
    "_GetSamplingStatisticSummariesPaginateResponseTypeDef",
    {
        "SamplingStatisticSummaries": List[
            GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef
        ]
    },
    total=False,
)


class GetSamplingStatisticSummariesPaginateResponseTypeDef(
    _GetSamplingStatisticSummariesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SamplingStatisticSummaries** *(list) --*

        Information about the number of requests instrumented for each sampling rule.
        - *(dict) --*

          Aggregated request sampling data for a sampling rule across all services for a 10 second
          window.
          - **RuleName** *(string) --*

            The name of the sampling rule.
    """


_GetServiceGraphPaginatePaginationConfigTypeDef = TypedDict(
    "_GetServiceGraphPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetServiceGraphPaginatePaginationConfigTypeDef(
    _GetServiceGraphPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef(
    _GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesEdgesTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesEdgesTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef
        ],
        "Aliases": List[GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef],
    },
    total=False,
)


class GetServiceGraphPaginateResponseServicesEdgesTypeDef(
    _GetServiceGraphPaginateResponseServicesEdgesTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef(
    _GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef(
    _GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef
):
    pass


_GetServiceGraphPaginateResponseServicesTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseServicesTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[GetServiceGraphPaginateResponseServicesEdgesTypeDef],
        "SummaryStatistics": GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef,
        "DurationHistogram": List[GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef],
        "ResponseTimeHistogram": List[
            GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class GetServiceGraphPaginateResponseServicesTypeDef(
    _GetServiceGraphPaginateResponseServicesTypeDef
):
    pass


_GetServiceGraphPaginateResponseTypeDef = TypedDict(
    "_GetServiceGraphPaginateResponseTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List[GetServiceGraphPaginateResponseServicesTypeDef],
        "ContainsOldGroupVersions": bool,
    },
    total=False,
)


class GetServiceGraphPaginateResponseTypeDef(_GetServiceGraphPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **StartTime** *(datetime) --*

        The start of the time frame for which the graph was generated.
    """


_GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef(
    _GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef
):
    pass


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef
):
    pass


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef
):
    pass


_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": datetime,
        "EdgeSummaryStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef,
        "ServiceSummaryStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef
):
    """
    - *(dict) --*

      A list of TimeSeriesStatistic structures.
      - **Timestamp** *(datetime) --*

        Timestamp of the window for which statistics are aggregated.
    """


_GetTimeSeriesServiceStatisticsPaginateResponseTypeDef = TypedDict(
    "_GetTimeSeriesServiceStatisticsPaginateResponseTypeDef",
    {
        "TimeSeriesServiceStatistics": List[
            GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef
        ],
        "ContainsOldGroupVersions": bool,
    },
    total=False,
)


class GetTimeSeriesServiceStatisticsPaginateResponseTypeDef(
    _GetTimeSeriesServiceStatisticsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **TimeSeriesServiceStatistics** *(list) --*

        The collection of statistics.
        - *(dict) --*

          A list of TimeSeriesStatistic structures.
          - **Timestamp** *(datetime) --*

            Timestamp of the window for which statistics are aggregated.
    """


_GetTraceGraphPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTraceGraphPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetTraceGraphPaginatePaginationConfigTypeDef(_GetTraceGraphPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef(
    _GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesEdgesTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesEdgesTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef,
        "ResponseTimeHistogram": List[
            GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef
        ],
        "Aliases": List[GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef],
    },
    total=False,
)


class GetTraceGraphPaginateResponseServicesEdgesTypeDef(
    _GetTraceGraphPaginateResponseServicesEdgesTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef(
    _GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)


class GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)


class GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef(
    _GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef
):
    pass


_GetTraceGraphPaginateResponseServicesTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseServicesTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List[GetTraceGraphPaginateResponseServicesEdgesTypeDef],
        "SummaryStatistics": GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef,
        "DurationHistogram": List[GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef],
        "ResponseTimeHistogram": List[
            GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef
        ],
    },
    total=False,
)


class GetTraceGraphPaginateResponseServicesTypeDef(_GetTraceGraphPaginateResponseServicesTypeDef):
    """
    - *(dict) --*

      Information about an application that processed requests, users that made requests, or
      downstream services, resources and applications that an application used.
      - **ReferenceId** *(integer) --*

        Identifier for the service. Unique within the service map.
    """


_GetTraceGraphPaginateResponseTypeDef = TypedDict(
    "_GetTraceGraphPaginateResponseTypeDef",
    {"Services": List[GetTraceGraphPaginateResponseServicesTypeDef]},
    total=False,
)


class GetTraceGraphPaginateResponseTypeDef(_GetTraceGraphPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Services** *(list) --*

        The services that have processed one of the specified requests.
        - *(dict) --*

          Information about an application that processed requests, users that made requests, or
          downstream services, resources and applications that an application used.
          - **ReferenceId** *(integer) --*

            Identifier for the service. Unique within the service map.
    """


_GetTraceSummariesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetTraceSummariesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class GetTraceSummariesPaginatePaginationConfigTypeDef(
    _GetTraceSummariesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    {"NumberValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef",
    {
        "AnnotationValue": GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef,
        "ServiceIds": List[
            GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef
        ],
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef",
    {
        "Services": List[
            GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef
        ]
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef",
    {
        "Services": List[
            GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef
        ]
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef",
    {"HttpURL": str, "HttpStatus": int, "HttpMethod": str, "UserAgent": str, "ClientIp": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef", {"Id": str}, total=False
)


class GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef", {"ARN": str}, total=False
)


class GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    {"Name": str, "Coverage": float, "Remote": bool},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List[
            GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef
        ],
        "Inferred": bool,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef",
    {
        "Services": List[
            GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
        ]
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef",
    {
        "UserName": str,
        "ServiceIds": List[GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef],
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef
):
    pass


_GetTraceSummariesPaginateResponseTraceSummariesTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTraceSummariesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "ResponseTime": float,
        "HasFault": bool,
        "HasError": bool,
        "HasThrottle": bool,
        "IsPartial": bool,
        "Http": GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef,
        "Annotations": Dict[
            str, List[GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef]
        ],
        "Users": List[GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef],
        "ServiceIds": List[GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef],
        "ResourceARNs": List[GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef],
        "InstanceIds": List[GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef],
        "AvailabilityZones": List[
            GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef
        ],
        "EntryPoint": GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef,
        "FaultRootCauses": List[
            GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef
        ],
        "ErrorRootCauses": List[
            GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef
        ],
        "ResponseTimeRootCauses": List[
            GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef
        ],
        "Revision": int,
        "MatchedEventTime": datetime,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTraceSummariesTypeDef(
    _GetTraceSummariesPaginateResponseTraceSummariesTypeDef
):
    """
    - *(dict) --*

      Metadata generated from the segment documents in a trace.
      - **Id** *(string) --*

        The unique identifier for the request that generated the trace's segments and subsegments.
    """


_GetTraceSummariesPaginateResponseTypeDef = TypedDict(
    "_GetTraceSummariesPaginateResponseTypeDef",
    {
        "TraceSummaries": List[GetTraceSummariesPaginateResponseTraceSummariesTypeDef],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
    },
    total=False,
)


class GetTraceSummariesPaginateResponseTypeDef(_GetTraceSummariesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TraceSummaries** *(list) --*

        Trace IDs and metadata for traces that were found in the specified time frame.
        - *(dict) --*

          Metadata generated from the segment documents in a trace.
          - **Id** *(string) --*

            The unique identifier for the request that generated the trace's segments and
            subsegments.
    """


_GetTraceSummariesPaginateSamplingStrategyTypeDef = TypedDict(
    "_GetTraceSummariesPaginateSamplingStrategyTypeDef",
    {"Name": Literal["PartialScan", "FixedRate"], "Value": float},
    total=False,
)


class GetTraceSummariesPaginateSamplingStrategyTypeDef(
    _GetTraceSummariesPaginateSamplingStrategyTypeDef
):
    """
    A paramater to indicate whether to enable sampling on trace summaries. Input parameters are Name
    and Value.
    - **Name** *(string) --*

      The name of a sampling rule.
    """
