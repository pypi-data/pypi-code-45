"Main interface for xray service type defs"
from __future__ import annotations

from datetime import datetime
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


BatchGetTracesPaginatePaginationConfigTypeDef = TypedDict(
    "BatchGetTracesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

BatchGetTracesPaginateResponseTracesSegmentsTypeDef = TypedDict(
    "BatchGetTracesPaginateResponseTracesSegmentsTypeDef", {"Id": str, "Document": str}, total=False
)

BatchGetTracesPaginateResponseTracesTypeDef = TypedDict(
    "BatchGetTracesPaginateResponseTracesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "Segments": List[BatchGetTracesPaginateResponseTracesSegmentsTypeDef],
    },
    total=False,
)

BatchGetTracesPaginateResponseTypeDef = TypedDict(
    "BatchGetTracesPaginateResponseTypeDef",
    {"Traces": List[BatchGetTracesPaginateResponseTracesTypeDef], "UnprocessedTraceIds": List[str]},
    total=False,
)

ClientBatchGetTracesResponseTracesSegmentsTypeDef = TypedDict(
    "ClientBatchGetTracesResponseTracesSegmentsTypeDef", {"Id": str, "Document": str}, total=False
)

ClientBatchGetTracesResponseTracesTypeDef = TypedDict(
    "ClientBatchGetTracesResponseTracesTypeDef",
    {
        "Id": str,
        "Duration": float,
        "Segments": List[ClientBatchGetTracesResponseTracesSegmentsTypeDef],
    },
    total=False,
)

ClientBatchGetTracesResponseTypeDef = TypedDict(
    "ClientBatchGetTracesResponseTypeDef",
    {
        "Traces": List[ClientBatchGetTracesResponseTracesTypeDef],
        "UnprocessedTraceIds": List[str],
        "NextToken": str,
    },
    total=False,
)

ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "ClientCreateGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)

ClientCreateGroupResponseTypeDef = TypedDict(
    "ClientCreateGroupResponseTypeDef",
    {"Group": ClientCreateGroupResponseGroupTypeDef},
    total=False,
)

ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
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

ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientCreateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

ClientCreateSamplingRuleResponseTypeDef = TypedDict(
    "ClientCreateSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientCreateSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)

ClientCreateSamplingRuleSamplingRuleTypeDef = TypedDict(
    "ClientCreateSamplingRuleSamplingRuleTypeDef",
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

ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
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

ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientDeleteSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

ClientDeleteSamplingRuleResponseTypeDef = TypedDict(
    "ClientDeleteSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientDeleteSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)

ClientGetEncryptionConfigResponseEncryptionConfigTypeDef = TypedDict(
    "ClientGetEncryptionConfigResponseEncryptionConfigTypeDef",
    {"KeyId": str, "Status": Literal["UPDATING", "ACTIVE"], "Type": Literal["NONE", "KMS"]},
    total=False,
)

ClientGetEncryptionConfigResponseTypeDef = TypedDict(
    "ClientGetEncryptionConfigResponseTypeDef",
    {"EncryptionConfig": ClientGetEncryptionConfigResponseEncryptionConfigTypeDef},
    total=False,
)

ClientGetGroupResponseGroupTypeDef = TypedDict(
    "ClientGetGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)

ClientGetGroupResponseTypeDef = TypedDict(
    "ClientGetGroupResponseTypeDef", {"Group": ClientGetGroupResponseGroupTypeDef}, total=False
)

ClientGetGroupsResponseGroupsTypeDef = TypedDict(
    "ClientGetGroupsResponseGroupsTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)

ClientGetGroupsResponseTypeDef = TypedDict(
    "ClientGetGroupsResponseTypeDef",
    {"Groups": List[ClientGetGroupsResponseGroupsTypeDef], "NextToken": str},
    total=False,
)

ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef = TypedDict(
    "ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef",
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

ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef = TypedDict(
    "ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef",
    {
        "SamplingRule": ClientGetSamplingRulesResponseSamplingRuleRecordsSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

ClientGetSamplingRulesResponseTypeDef = TypedDict(
    "ClientGetSamplingRulesResponseTypeDef",
    {
        "SamplingRuleRecords": List[ClientGetSamplingRulesResponseSamplingRuleRecordsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef = TypedDict(
    "ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef",
    {
        "RuleName": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "BorrowCount": int,
        "SampledCount": int,
    },
    total=False,
)

ClientGetSamplingStatisticSummariesResponseTypeDef = TypedDict(
    "ClientGetSamplingStatisticSummariesResponseTypeDef",
    {
        "SamplingStatisticSummaries": List[
            ClientGetSamplingStatisticSummariesResponseSamplingStatisticSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef = TypedDict(
    "ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef",
    {
        "RuleName": str,
        "FixedRate": float,
        "ReservoirQuota": int,
        "ReservoirQuotaTTL": datetime,
        "Interval": int,
    },
    total=False,
)

ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef = TypedDict(
    "ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef",
    {"RuleName": str, "ErrorCode": str, "Message": str},
    total=False,
)

ClientGetSamplingTargetsResponseTypeDef = TypedDict(
    "ClientGetSamplingTargetsResponseTypeDef",
    {
        "SamplingTargetDocuments": List[
            ClientGetSamplingTargetsResponseSamplingTargetDocumentsTypeDef
        ],
        "LastRuleModification": datetime,
        "UnprocessedStatistics": List[ClientGetSamplingTargetsResponseUnprocessedStatisticsTypeDef],
    },
    total=False,
)

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
    pass


ClientGetServiceGraphResponseServicesDurationHistogramTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetServiceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetServiceGraphResponseServicesEdgesTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesEdgesTypeDef",
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

ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetServiceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetServiceGraphResponseServicesTypeDef = TypedDict(
    "ClientGetServiceGraphResponseServicesTypeDef",
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

ClientGetServiceGraphResponseTypeDef = TypedDict(
    "ClientGetServiceGraphResponseTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List[ClientGetServiceGraphResponseServicesTypeDef],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef",
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

ClientGetTimeSeriesServiceStatisticsResponseTypeDef = TypedDict(
    "ClientGetTimeSeriesServiceStatisticsResponseTypeDef",
    {
        "TimeSeriesServiceStatistics": List[
            ClientGetTimeSeriesServiceStatisticsResponseTimeSeriesServiceStatisticsTypeDef
        ],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
    },
    total=False,
)

ClientGetTraceGraphResponseServicesDurationHistogramTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTraceGraphResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetTraceGraphResponseServicesEdgesTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesEdgesTypeDef",
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

ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": ClientGetTraceGraphResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ClientGetTraceGraphResponseServicesTypeDef = TypedDict(
    "ClientGetTraceGraphResponseServicesTypeDef",
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

ClientGetTraceGraphResponseTypeDef = TypedDict(
    "ClientGetTraceGraphResponseTypeDef",
    {"Services": List[ClientGetTraceGraphResponseServicesTypeDef], "NextToken": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    {"NumberValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesAnnotationsTypeDef",
    {
        "AnnotationValue": ClientGetTraceSummariesResponseTraceSummariesAnnotationsAnnotationValueTypeDef,
        "ServiceIds": List[
            ClientGetTraceSummariesResponseTraceSummariesAnnotationsServiceIdsTypeDef
        ],
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesEntryPointTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef",
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

ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesTypeDef",
    {"Services": List[ClientGetTraceSummariesResponseTraceSummariesErrorRootCausesServicesTypeDef]},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef",
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

ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesTypeDef",
    {"Services": List[ClientGetTraceSummariesResponseTraceSummariesFaultRootCausesServicesTypeDef]},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesHttpTypeDef",
    {"HttpURL": str, "HttpStatus": int, "HttpMethod": str, "UserAgent": str, "ClientIp": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesInstanceIdsTypeDef", {"Id": str}, total=False
)

ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesResourceARNsTypeDef", {"ARN": str}, total=False
)

ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    {"Name": str, "Coverage": float, "Remote": bool},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
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

ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesTypeDef",
    {
        "Services": List[
            ClientGetTraceSummariesResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
        ]
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesUsersTypeDef",
    {
        "UserName": str,
        "ServiceIds": List[ClientGetTraceSummariesResponseTraceSummariesUsersServiceIdsTypeDef],
    },
    total=False,
)

ClientGetTraceSummariesResponseTraceSummariesTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTraceSummariesTypeDef",
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

ClientGetTraceSummariesResponseTypeDef = TypedDict(
    "ClientGetTraceSummariesResponseTypeDef",
    {
        "TraceSummaries": List[ClientGetTraceSummariesResponseTraceSummariesTypeDef],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
        "NextToken": str,
    },
    total=False,
)

ClientGetTraceSummariesSamplingStrategyTypeDef = TypedDict(
    "ClientGetTraceSummariesSamplingStrategyTypeDef",
    {"Name": Literal["PartialScan", "FixedRate"], "Value": float},
    total=False,
)

ClientPutEncryptionConfigResponseEncryptionConfigTypeDef = TypedDict(
    "ClientPutEncryptionConfigResponseEncryptionConfigTypeDef",
    {"KeyId": str, "Status": Literal["UPDATING", "ACTIVE"], "Type": Literal["NONE", "KMS"]},
    total=False,
)

ClientPutEncryptionConfigResponseTypeDef = TypedDict(
    "ClientPutEncryptionConfigResponseTypeDef",
    {"EncryptionConfig": ClientPutEncryptionConfigResponseEncryptionConfigTypeDef},
    total=False,
)

ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef = TypedDict(
    "ClientPutTelemetryRecordsTelemetryRecordsBackendConnectionErrorsTypeDef",
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
    pass


ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef = TypedDict(
    "ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef",
    {"Id": str, "ErrorCode": str, "Message": str},
    total=False,
)

ClientPutTraceSegmentsResponseTypeDef = TypedDict(
    "ClientPutTraceSegmentsResponseTypeDef",
    {
        "UnprocessedTraceSegments": List[
            ClientPutTraceSegmentsResponseUnprocessedTraceSegmentsTypeDef
        ]
    },
    total=False,
)

ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "ClientUpdateGroupResponseGroupTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)

ClientUpdateGroupResponseTypeDef = TypedDict(
    "ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef},
    total=False,
)

ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef = TypedDict(
    "ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef",
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

ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef = TypedDict(
    "ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef",
    {
        "SamplingRule": ClientUpdateSamplingRuleResponseSamplingRuleRecordSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

ClientUpdateSamplingRuleResponseTypeDef = TypedDict(
    "ClientUpdateSamplingRuleResponseTypeDef",
    {"SamplingRuleRecord": ClientUpdateSamplingRuleResponseSamplingRuleRecordTypeDef},
    total=False,
)

ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef = TypedDict(
    "ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef",
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

GetGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "GetGroupsPaginatePaginationConfigTypeDef", {"MaxItems": int, "StartingToken": str}, total=False
)

GetGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "GetGroupsPaginateResponseGroupsTypeDef",
    {"GroupName": str, "GroupARN": str, "FilterExpression": str},
    total=False,
)

GetGroupsPaginateResponseTypeDef = TypedDict(
    "GetGroupsPaginateResponseTypeDef",
    {"Groups": List[GetGroupsPaginateResponseGroupsTypeDef]},
    total=False,
)

GetSamplingRulesPaginatePaginationConfigTypeDef = TypedDict(
    "GetSamplingRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef = TypedDict(
    "GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef",
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

GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef = TypedDict(
    "GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef",
    {
        "SamplingRule": GetSamplingRulesPaginateResponseSamplingRuleRecordsSamplingRuleTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

GetSamplingRulesPaginateResponseTypeDef = TypedDict(
    "GetSamplingRulesPaginateResponseTypeDef",
    {"SamplingRuleRecords": List[GetSamplingRulesPaginateResponseSamplingRuleRecordsTypeDef]},
    total=False,
)

GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef = TypedDict(
    "GetSamplingStatisticSummariesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef = TypedDict(
    "GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef",
    {
        "RuleName": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "BorrowCount": int,
        "SampledCount": int,
    },
    total=False,
)

GetSamplingStatisticSummariesPaginateResponseTypeDef = TypedDict(
    "GetSamplingStatisticSummariesPaginateResponseTypeDef",
    {
        "SamplingStatisticSummaries": List[
            GetSamplingStatisticSummariesPaginateResponseSamplingStatisticSummariesTypeDef
        ]
    },
    total=False,
)

GetServiceGraphPaginatePaginationConfigTypeDef = TypedDict(
    "GetServiceGraphPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)

GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetServiceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

GetServiceGraphPaginateResponseServicesEdgesTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesEdgesTypeDef",
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

GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetServiceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetServiceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

GetServiceGraphPaginateResponseServicesTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseServicesTypeDef",
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

GetServiceGraphPaginateResponseTypeDef = TypedDict(
    "GetServiceGraphPaginateResponseTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List[GetServiceGraphPaginateResponseServicesTypeDef],
        "ContainsOldGroupVersions": bool,
    },
    total=False,
)

GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsEdgeSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsServiceSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef",
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

GetTimeSeriesServiceStatisticsPaginateResponseTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsPaginateResponseTypeDef",
    {
        "TimeSeriesServiceStatistics": List[
            GetTimeSeriesServiceStatisticsPaginateResponseTimeSeriesServiceStatisticsTypeDef
        ],
        "ContainsOldGroupVersions": bool,
    },
    total=False,
)

GetTraceGraphPaginatePaginationConfigTypeDef = TypedDict(
    "GetTraceGraphPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesDurationHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesEdgesAliasesTypeDef",
    {"Name": str, "Names": List[str], "Type": str},
    total=False,
)

GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesEdgesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTraceGraphPaginateResponseServicesEdgesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

GetTraceGraphPaginateResponseServicesEdgesTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesEdgesTypeDef",
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

GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesResponseTimeHistogramTypeDef",
    {"Value": float, "Count": int},
    total=False,
)

GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef",
    {"ThrottleCount": int, "OtherCount": int, "TotalCount": int},
    total=False,
)

GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef",
    {"OtherCount": int, "TotalCount": int},
    total=False,
)

GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesSummaryStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": GetTraceGraphPaginateResponseServicesSummaryStatisticsErrorStatisticsTypeDef,
        "FaultStatistics": GetTraceGraphPaginateResponseServicesSummaryStatisticsFaultStatisticsTypeDef,
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

GetTraceGraphPaginateResponseServicesTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseServicesTypeDef",
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

GetTraceGraphPaginateResponseTypeDef = TypedDict(
    "GetTraceGraphPaginateResponseTypeDef",
    {"Services": List[GetTraceGraphPaginateResponseServicesTypeDef]},
    total=False,
)

GetTraceSummariesPaginatePaginationConfigTypeDef = TypedDict(
    "GetTraceSummariesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef",
    {"NumberValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesAnnotationsTypeDef",
    {
        "AnnotationValue": GetTraceSummariesPaginateResponseTraceSummariesAnnotationsAnnotationValueTypeDef,
        "ServiceIds": List[
            GetTraceSummariesPaginateResponseTraceSummariesAnnotationsServiceIdsTypeDef
        ],
    },
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesAvailabilityZonesTypeDef",
    {"Name": str},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesEntryPointTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef",
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

GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesTypeDef",
    {
        "Services": List[
            GetTraceSummariesPaginateResponseTraceSummariesErrorRootCausesServicesTypeDef
        ]
    },
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef",
    {"Name": str, "Message": str},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathTypeDef",
    {
        "Name": str,
        "Exceptions": List[
            GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesEntityPathExceptionsTypeDef
        ],
        "Remote": bool,
    },
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef",
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

GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesTypeDef",
    {
        "Services": List[
            GetTraceSummariesPaginateResponseTraceSummariesFaultRootCausesServicesTypeDef
        ]
    },
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesHttpTypeDef",
    {"HttpURL": str, "HttpStatus": int, "HttpMethod": str, "UserAgent": str, "ClientIp": str},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesInstanceIdsTypeDef", {"Id": str}, total=False
)

GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesResourceARNsTypeDef", {"ARN": str}, total=False
)

GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesEntityPathTypeDef",
    {"Name": str, "Coverage": float, "Remote": bool},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef",
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

GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesTypeDef",
    {
        "Services": List[
            GetTraceSummariesPaginateResponseTraceSummariesResponseTimeRootCausesServicesTypeDef
        ]
    },
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesUsersTypeDef",
    {
        "UserName": str,
        "ServiceIds": List[GetTraceSummariesPaginateResponseTraceSummariesUsersServiceIdsTypeDef],
    },
    total=False,
)

GetTraceSummariesPaginateResponseTraceSummariesTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTraceSummariesTypeDef",
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

GetTraceSummariesPaginateResponseTypeDef = TypedDict(
    "GetTraceSummariesPaginateResponseTypeDef",
    {
        "TraceSummaries": List[GetTraceSummariesPaginateResponseTraceSummariesTypeDef],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
    },
    total=False,
)

GetTraceSummariesPaginateSamplingStrategyTypeDef = TypedDict(
    "GetTraceSummariesPaginateSamplingStrategyTypeDef",
    {"Name": Literal["PartialScan", "FixedRate"], "Value": float},
    total=False,
)
