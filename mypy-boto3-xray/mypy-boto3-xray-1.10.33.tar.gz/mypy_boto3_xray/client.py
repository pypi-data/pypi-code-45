"Main interface for xray service Client"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_xray.client as client_scope

# pylint: disable=import-self
import mypy_boto3_xray.paginator as paginator_scope
from mypy_boto3_xray.type_defs import (
    ClientBatchGetTracesResponseTypeDef,
    ClientCreateGroupResponseTypeDef,
    ClientCreateSamplingRuleResponseTypeDef,
    ClientCreateSamplingRuleSamplingRuleTypeDef,
    ClientDeleteSamplingRuleResponseTypeDef,
    ClientGetEncryptionConfigResponseTypeDef,
    ClientGetGroupResponseTypeDef,
    ClientGetGroupsResponseTypeDef,
    ClientGetSamplingRulesResponseTypeDef,
    ClientGetSamplingStatisticSummariesResponseTypeDef,
    ClientGetSamplingTargetsResponseTypeDef,
    ClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef,
    ClientGetTimeSeriesServiceStatisticsResponseTypeDef,
    ClientGetTraceGraphResponseTypeDef,
    ClientGetTraceSummariesResponseTypeDef,
    ClientPutEncryptionConfigResponseTypeDef,
    ClientPutTelemetryRecordsTelemetryRecordsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
from typing import overload
from mypy_boto3_xray.type_defs import (
    ClientGetServiceGraphResponseTypeDef,
    ClientGetTraceSummariesSamplingStrategyTypeDef,
    ClientPutTraceSegmentsResponseTypeDef,
    ClientUpdateGroupResponseTypeDef,
    ClientUpdateSamplingRuleResponseTypeDef,
    ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    """
    [XRay.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_get_traces(
        self, TraceIds: List[str], NextToken: str = None
    ) -> ClientBatchGetTracesResponseTypeDef:
        """
        [Client.batch_get_traces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.batch_get_traces)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(
        self, GroupName: str, FilterExpression: str = None
    ) -> ClientCreateGroupResponseTypeDef:
        """
        [Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.create_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_sampling_rule(
        self, SamplingRule: ClientCreateSamplingRuleSamplingRuleTypeDef
    ) -> ClientCreateSamplingRuleResponseTypeDef:
        """
        [Client.create_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.create_sampling_rule)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_group(self, GroupName: str = None, GroupARN: str = None) -> Dict[str, Any]:
        """
        [Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.delete_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_sampling_rule(
        self, RuleName: str = None, RuleARN: str = None
    ) -> ClientDeleteSamplingRuleResponseTypeDef:
        """
        [Client.delete_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.delete_sampling_rule)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_encryption_config(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetEncryptionConfigResponseTypeDef:
        """
        [Client.get_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.get_encryption_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_group(
        self, GroupName: str = None, GroupARN: str = None
    ) -> ClientGetGroupResponseTypeDef:
        """
        [Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.get_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_groups(self, NextToken: str = None) -> ClientGetGroupsResponseTypeDef:
        """
        [Client.get_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.get_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_sampling_rules(self, NextToken: str = None) -> ClientGetSamplingRulesResponseTypeDef:
        """
        [Client.get_sampling_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.get_sampling_rules)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_sampling_statistic_summaries(
        self, NextToken: str = None
    ) -> ClientGetSamplingStatisticSummariesResponseTypeDef:
        """
        [Client.get_sampling_statistic_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.get_sampling_statistic_summaries)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_sampling_targets(
        self,
        SamplingStatisticsDocuments: List[
            ClientGetSamplingTargetsSamplingStatisticsDocumentsTypeDef
        ],
    ) -> ClientGetSamplingTargetsResponseTypeDef:
        """
        [Client.get_sampling_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.get_sampling_targets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_service_graph(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        NextToken: str = None,
    ) -> ClientGetServiceGraphResponseTypeDef:
        """
        [Client.get_service_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.get_service_graph)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_time_series_service_statistics(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        EntitySelectorExpression: str = None,
        Period: int = None,
        NextToken: str = None,
    ) -> ClientGetTimeSeriesServiceStatisticsResponseTypeDef:
        """
        [Client.get_time_series_service_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.get_time_series_service_statistics)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_trace_graph(
        self, TraceIds: List[str], NextToken: str = None
    ) -> ClientGetTraceGraphResponseTypeDef:
        """
        [Client.get_trace_graph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.get_trace_graph)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_trace_summaries(
        self,
        StartTime: datetime,
        EndTime: datetime,
        TimeRangeType: Literal["TraceId", "Event"] = None,
        Sampling: bool = None,
        SamplingStrategy: ClientGetTraceSummariesSamplingStrategyTypeDef = None,
        FilterExpression: str = None,
        NextToken: str = None,
    ) -> ClientGetTraceSummariesResponseTypeDef:
        """
        [Client.get_trace_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.get_trace_summaries)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_encryption_config(
        self, Type: Literal["NONE", "KMS"], KeyId: str = None
    ) -> ClientPutEncryptionConfigResponseTypeDef:
        """
        [Client.put_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.put_encryption_config)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_telemetry_records(
        self,
        TelemetryRecords: List[ClientPutTelemetryRecordsTelemetryRecordsTypeDef],
        EC2InstanceId: str = None,
        Hostname: str = None,
        ResourceARN: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_telemetry_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.put_telemetry_records)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_trace_segments(
        self, TraceSegmentDocuments: List[str]
    ) -> ClientPutTraceSegmentsResponseTypeDef:
        """
        [Client.put_trace_segments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.put_trace_segments)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_group(
        self, GroupName: str = None, GroupARN: str = None, FilterExpression: str = None
    ) -> ClientUpdateGroupResponseTypeDef:
        """
        [Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.update_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_sampling_rule(
        self, SamplingRuleUpdate: ClientUpdateSamplingRuleSamplingRuleUpdateTypeDef
    ) -> ClientUpdateSamplingRuleResponseTypeDef:
        """
        [Client.update_sampling_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Client.update_sampling_rule)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["batch_get_traces"]
    ) -> paginator_scope.BatchGetTracesPaginator:
        """
        [Paginator.BatchGetTraces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.BatchGetTraces)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_groups"]
    ) -> paginator_scope.GetGroupsPaginator:
        """
        [Paginator.GetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_sampling_rules"]
    ) -> paginator_scope.GetSamplingRulesPaginator:
        """
        [Paginator.GetSamplingRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetSamplingRules)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_sampling_statistic_summaries"]
    ) -> paginator_scope.GetSamplingStatisticSummariesPaginator:
        """
        [Paginator.GetSamplingStatisticSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_service_graph"]
    ) -> paginator_scope.GetServiceGraphPaginator:
        """
        [Paginator.GetServiceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetServiceGraph)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_time_series_service_statistics"]
    ) -> paginator_scope.GetTimeSeriesServiceStatisticsPaginator:
        """
        [Paginator.GetTimeSeriesServiceStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_trace_graph"]
    ) -> paginator_scope.GetTraceGraphPaginator:
        """
        [Paginator.GetTraceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetTraceGraph)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_trace_summaries"]
    ) -> paginator_scope.GetTraceSummariesPaginator:
        """
        [Paginator.GetTraceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/xray.html#XRay.Paginator.GetTraceSummaries)
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    RuleLimitExceededException: Boto3ClientError
    ThrottledException: Boto3ClientError
