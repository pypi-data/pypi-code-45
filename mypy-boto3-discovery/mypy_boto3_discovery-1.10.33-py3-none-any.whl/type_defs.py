"Main interface for discovery service type defs"
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


ClientBatchDeleteImportDataResponseerrorsTypeDef = TypedDict(
    "ClientBatchDeleteImportDataResponseerrorsTypeDef",
    {
        "importTaskId": str,
        "errorCode": Literal["NOT_FOUND", "INTERNAL_SERVER_ERROR", "OVER_LIMIT"],
        "errorDescription": str,
    },
    total=False,
)

ClientBatchDeleteImportDataResponseTypeDef = TypedDict(
    "ClientBatchDeleteImportDataResponseTypeDef",
    {"errors": List[ClientBatchDeleteImportDataResponseerrorsTypeDef]},
    total=False,
)

ClientCreateApplicationResponseTypeDef = TypedDict(
    "ClientCreateApplicationResponseTypeDef", {"configurationId": str}, total=False
)

ClientCreateTagsTagsTypeDef = TypedDict(
    "ClientCreateTagsTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDeleteTagsTagsTypeDef = TypedDict(
    "ClientDeleteTagsTagsTypeDef", {"key": str, "value": str}, total=False
)

ClientDescribeAgentsFiltersTypeDef = TypedDict(
    "ClientDescribeAgentsFiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
    total=False,
)

ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef = TypedDict(
    "ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef",
    {"ipAddress": str, "macAddress": str},
    total=False,
)

ClientDescribeAgentsResponseagentsInfoTypeDef = TypedDict(
    "ClientDescribeAgentsResponseagentsInfoTypeDef",
    {
        "agentId": str,
        "hostName": str,
        "agentNetworkInfoList": List[
            ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef
        ],
        "connectorId": str,
        "version": str,
        "health": Literal["HEALTHY", "UNHEALTHY", "RUNNING", "UNKNOWN", "BLACKLISTED", "SHUTDOWN"],
        "lastHealthPingTime": str,
        "collectionStatus": str,
        "agentType": str,
        "registeredTime": str,
    },
    total=False,
)

ClientDescribeAgentsResponseTypeDef = TypedDict(
    "ClientDescribeAgentsResponseTypeDef",
    {"agentsInfo": List[ClientDescribeAgentsResponseagentsInfoTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeConfigurationsResponseTypeDef",
    {"configurations": List[Dict[str, str]]},
    total=False,
)

ClientDescribeContinuousExportsResponsedescriptionsTypeDef = TypedDict(
    "ClientDescribeContinuousExportsResponsedescriptionsTypeDef",
    {
        "exportId": str,
        "status": Literal[
            "START_IN_PROGRESS",
            "START_FAILED",
            "ACTIVE",
            "ERROR",
            "STOP_IN_PROGRESS",
            "STOP_FAILED",
            "INACTIVE",
        ],
        "statusDetail": str,
        "s3Bucket": str,
        "startTime": datetime,
        "stopTime": datetime,
        "dataSource": str,
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)

ClientDescribeContinuousExportsResponseTypeDef = TypedDict(
    "ClientDescribeContinuousExportsResponseTypeDef",
    {
        "descriptions": List[ClientDescribeContinuousExportsResponsedescriptionsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeExportConfigurationsResponseexportsInfoTypeDef = TypedDict(
    "ClientDescribeExportConfigurationsResponseexportsInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": Literal["FAILED", "SUCCEEDED", "IN_PROGRESS"],
        "statusMessage": str,
        "configurationsDownloadUrl": str,
        "exportRequestTime": datetime,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)

ClientDescribeExportConfigurationsResponseTypeDef = TypedDict(
    "ClientDescribeExportConfigurationsResponseTypeDef",
    {
        "exportsInfo": List[ClientDescribeExportConfigurationsResponseexportsInfoTypeDef],
        "nextToken": str,
    },
    total=False,
)

_RequiredClientDescribeExportTasksFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeExportTasksFiltersTypeDef", {"name": str}
)
_OptionalClientDescribeExportTasksFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeExportTasksFiltersTypeDef",
    {"values": List[str], "condition": str},
    total=False,
)


class ClientDescribeExportTasksFiltersTypeDef(
    _RequiredClientDescribeExportTasksFiltersTypeDef,
    _OptionalClientDescribeExportTasksFiltersTypeDef,
):
    pass


ClientDescribeExportTasksResponseexportsInfoTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseexportsInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": Literal["FAILED", "SUCCEEDED", "IN_PROGRESS"],
        "statusMessage": str,
        "configurationsDownloadUrl": str,
        "exportRequestTime": datetime,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)

ClientDescribeExportTasksResponseTypeDef = TypedDict(
    "ClientDescribeExportTasksResponseTypeDef",
    {"exportsInfo": List[ClientDescribeExportTasksResponseexportsInfoTypeDef], "nextToken": str},
    total=False,
)

ClientDescribeImportTasksFiltersTypeDef = TypedDict(
    "ClientDescribeImportTasksFiltersTypeDef",
    {"name": Literal["IMPORT_TASK_ID", "STATUS", "NAME"], "values": List[str]},
    total=False,
)

ClientDescribeImportTasksResponsetasksTypeDef = TypedDict(
    "ClientDescribeImportTasksResponsetasksTypeDef",
    {
        "importTaskId": str,
        "clientRequestToken": str,
        "name": str,
        "importUrl": str,
        "status": Literal[
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_COMPLETE_WITH_ERRORS",
            "IMPORT_FAILED",
            "IMPORT_FAILED_SERVER_LIMIT_EXCEEDED",
            "IMPORT_FAILED_RECORD_LIMIT_EXCEEDED",
            "DELETE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_FAILED_LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "importRequestTime": datetime,
        "importCompletionTime": datetime,
        "importDeletedTime": datetime,
        "serverImportSuccess": int,
        "serverImportFailure": int,
        "applicationImportSuccess": int,
        "applicationImportFailure": int,
        "errorsAndFailedEntriesZip": str,
    },
    total=False,
)

ClientDescribeImportTasksResponseTypeDef = TypedDict(
    "ClientDescribeImportTasksResponseTypeDef",
    {"nextToken": str, "tasks": List[ClientDescribeImportTasksResponsetasksTypeDef]},
    total=False,
)

_RequiredClientDescribeTagsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeTagsFiltersTypeDef", {"name": str}
)
_OptionalClientDescribeTagsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeTagsFiltersTypeDef", {"values": List[str]}, total=False
)


class ClientDescribeTagsFiltersTypeDef(
    _RequiredClientDescribeTagsFiltersTypeDef, _OptionalClientDescribeTagsFiltersTypeDef
):
    pass


ClientDescribeTagsResponsetagsTypeDef = TypedDict(
    "ClientDescribeTagsResponsetagsTypeDef",
    {
        "configurationType": Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        "configurationId": str,
        "key": str,
        "value": str,
        "timeOfCreation": datetime,
    },
    total=False,
)

ClientDescribeTagsResponseTypeDef = TypedDict(
    "ClientDescribeTagsResponseTypeDef",
    {"tags": List[ClientDescribeTagsResponsetagsTypeDef], "nextToken": str},
    total=False,
)

ClientExportConfigurationsResponseTypeDef = TypedDict(
    "ClientExportConfigurationsResponseTypeDef", {"exportId": str}, total=False
)

ClientGetDiscoverySummaryResponseagentSummaryTypeDef = TypedDict(
    "ClientGetDiscoverySummaryResponseagentSummaryTypeDef",
    {
        "activeAgents": int,
        "healthyAgents": int,
        "blackListedAgents": int,
        "shutdownAgents": int,
        "unhealthyAgents": int,
        "totalAgents": int,
        "unknownAgents": int,
    },
    total=False,
)

ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef = TypedDict(
    "ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef",
    {
        "activeConnectors": int,
        "healthyConnectors": int,
        "blackListedConnectors": int,
        "shutdownConnectors": int,
        "unhealthyConnectors": int,
        "totalConnectors": int,
        "unknownConnectors": int,
    },
    total=False,
)

ClientGetDiscoverySummaryResponseTypeDef = TypedDict(
    "ClientGetDiscoverySummaryResponseTypeDef",
    {
        "servers": int,
        "applications": int,
        "serversMappedToApplications": int,
        "serversMappedtoTags": int,
        "agentSummary": ClientGetDiscoverySummaryResponseagentSummaryTypeDef,
        "connectorSummary": ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef,
    },
    total=False,
)

ClientListConfigurationsFiltersTypeDef = TypedDict(
    "ClientListConfigurationsFiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
    total=False,
)

_RequiredClientListConfigurationsOrderByTypeDef = TypedDict(
    "_RequiredClientListConfigurationsOrderByTypeDef", {"fieldName": str}
)
_OptionalClientListConfigurationsOrderByTypeDef = TypedDict(
    "_OptionalClientListConfigurationsOrderByTypeDef",
    {"sortOrder": Literal["ASC", "DESC"]},
    total=False,
)


class ClientListConfigurationsOrderByTypeDef(
    _RequiredClientListConfigurationsOrderByTypeDef, _OptionalClientListConfigurationsOrderByTypeDef
):
    pass


ClientListConfigurationsResponseTypeDef = TypedDict(
    "ClientListConfigurationsResponseTypeDef",
    {"configurations": List[Dict[str, str]], "nextToken": str},
    total=False,
)

ClientListServerNeighborsResponseneighborsTypeDef = TypedDict(
    "ClientListServerNeighborsResponseneighborsTypeDef",
    {
        "sourceServerId": str,
        "destinationServerId": str,
        "destinationPort": int,
        "transportProtocol": str,
        "connectionsCount": int,
    },
    total=False,
)

ClientListServerNeighborsResponseTypeDef = TypedDict(
    "ClientListServerNeighborsResponseTypeDef",
    {
        "neighbors": List[ClientListServerNeighborsResponseneighborsTypeDef],
        "nextToken": str,
        "knownDependencyCount": int,
    },
    total=False,
)

ClientStartContinuousExportResponseTypeDef = TypedDict(
    "ClientStartContinuousExportResponseTypeDef",
    {
        "exportId": str,
        "s3Bucket": str,
        "startTime": datetime,
        "dataSource": str,
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)

ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef = TypedDict(
    "ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    {"agentId": str, "operationSucceeded": bool, "description": str},
    total=False,
)

ClientStartDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "ClientStartDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List[
            ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
        ]
    },
    total=False,
)

_RequiredClientStartExportTaskFiltersTypeDef = TypedDict(
    "_RequiredClientStartExportTaskFiltersTypeDef", {"name": str}
)
_OptionalClientStartExportTaskFiltersTypeDef = TypedDict(
    "_OptionalClientStartExportTaskFiltersTypeDef",
    {"values": List[str], "condition": str},
    total=False,
)


class ClientStartExportTaskFiltersTypeDef(
    _RequiredClientStartExportTaskFiltersTypeDef, _OptionalClientStartExportTaskFiltersTypeDef
):
    pass


ClientStartExportTaskResponseTypeDef = TypedDict(
    "ClientStartExportTaskResponseTypeDef", {"exportId": str}, total=False
)

ClientStartImportTaskResponsetaskTypeDef = TypedDict(
    "ClientStartImportTaskResponsetaskTypeDef",
    {
        "importTaskId": str,
        "clientRequestToken": str,
        "name": str,
        "importUrl": str,
        "status": Literal[
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_COMPLETE_WITH_ERRORS",
            "IMPORT_FAILED",
            "IMPORT_FAILED_SERVER_LIMIT_EXCEEDED",
            "IMPORT_FAILED_RECORD_LIMIT_EXCEEDED",
            "DELETE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_FAILED_LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "importRequestTime": datetime,
        "importCompletionTime": datetime,
        "importDeletedTime": datetime,
        "serverImportSuccess": int,
        "serverImportFailure": int,
        "applicationImportSuccess": int,
        "applicationImportFailure": int,
        "errorsAndFailedEntriesZip": str,
    },
    total=False,
)

ClientStartImportTaskResponseTypeDef = TypedDict(
    "ClientStartImportTaskResponseTypeDef",
    {"task": ClientStartImportTaskResponsetaskTypeDef},
    total=False,
)

ClientStopContinuousExportResponseTypeDef = TypedDict(
    "ClientStopContinuousExportResponseTypeDef",
    {"startTime": datetime, "stopTime": datetime},
    total=False,
)

ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef = TypedDict(
    "ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    {"agentId": str, "operationSucceeded": bool, "description": str},
    total=False,
)

ClientStopDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "ClientStopDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List[
            ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
        ]
    },
    total=False,
)

DescribeAgentsPaginateFiltersTypeDef = TypedDict(
    "DescribeAgentsPaginateFiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
    total=False,
)

DescribeAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef = TypedDict(
    "DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef",
    {"ipAddress": str, "macAddress": str},
    total=False,
)

DescribeAgentsPaginateResponseagentsInfoTypeDef = TypedDict(
    "DescribeAgentsPaginateResponseagentsInfoTypeDef",
    {
        "agentId": str,
        "hostName": str,
        "agentNetworkInfoList": List[
            DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef
        ],
        "connectorId": str,
        "version": str,
        "health": Literal["HEALTHY", "UNHEALTHY", "RUNNING", "UNKNOWN", "BLACKLISTED", "SHUTDOWN"],
        "lastHealthPingTime": str,
        "collectionStatus": str,
        "agentType": str,
        "registeredTime": str,
    },
    total=False,
)

DescribeAgentsPaginateResponseTypeDef = TypedDict(
    "DescribeAgentsPaginateResponseTypeDef",
    {"agentsInfo": List[DescribeAgentsPaginateResponseagentsInfoTypeDef], "NextToken": str},
    total=False,
)

DescribeContinuousExportsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeContinuousExportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeContinuousExportsPaginateResponsedescriptionsTypeDef = TypedDict(
    "DescribeContinuousExportsPaginateResponsedescriptionsTypeDef",
    {
        "exportId": str,
        "status": Literal[
            "START_IN_PROGRESS",
            "START_FAILED",
            "ACTIVE",
            "ERROR",
            "STOP_IN_PROGRESS",
            "STOP_FAILED",
            "INACTIVE",
        ],
        "statusDetail": str,
        "s3Bucket": str,
        "startTime": datetime,
        "stopTime": datetime,
        "dataSource": str,
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)

DescribeContinuousExportsPaginateResponseTypeDef = TypedDict(
    "DescribeContinuousExportsPaginateResponseTypeDef",
    {
        "descriptions": List[DescribeContinuousExportsPaginateResponsedescriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

DescribeExportConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeExportConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef = TypedDict(
    "DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": Literal["FAILED", "SUCCEEDED", "IN_PROGRESS"],
        "statusMessage": str,
        "configurationsDownloadUrl": str,
        "exportRequestTime": datetime,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)

DescribeExportConfigurationsPaginateResponseTypeDef = TypedDict(
    "DescribeExportConfigurationsPaginateResponseTypeDef",
    {
        "exportsInfo": List[DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef],
        "NextToken": str,
    },
    total=False,
)

_RequiredDescribeExportTasksPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeExportTasksPaginateFiltersTypeDef", {"name": str}
)
_OptionalDescribeExportTasksPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeExportTasksPaginateFiltersTypeDef",
    {"values": List[str], "condition": str},
    total=False,
)


class DescribeExportTasksPaginateFiltersTypeDef(
    _RequiredDescribeExportTasksPaginateFiltersTypeDef,
    _OptionalDescribeExportTasksPaginateFiltersTypeDef,
):
    pass


DescribeExportTasksPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeExportTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeExportTasksPaginateResponseexportsInfoTypeDef = TypedDict(
    "DescribeExportTasksPaginateResponseexportsInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": Literal["FAILED", "SUCCEEDED", "IN_PROGRESS"],
        "statusMessage": str,
        "configurationsDownloadUrl": str,
        "exportRequestTime": datetime,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)

DescribeExportTasksPaginateResponseTypeDef = TypedDict(
    "DescribeExportTasksPaginateResponseTypeDef",
    {"exportsInfo": List[DescribeExportTasksPaginateResponseexportsInfoTypeDef], "NextToken": str},
    total=False,
)

_RequiredDescribeTagsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeTagsPaginateFiltersTypeDef", {"name": str}
)
_OptionalDescribeTagsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeTagsPaginateFiltersTypeDef", {"values": List[str]}, total=False
)


class DescribeTagsPaginateFiltersTypeDef(
    _RequiredDescribeTagsPaginateFiltersTypeDef, _OptionalDescribeTagsPaginateFiltersTypeDef
):
    pass


DescribeTagsPaginatePaginationConfigTypeDef = TypedDict(
    "DescribeTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

DescribeTagsPaginateResponsetagsTypeDef = TypedDict(
    "DescribeTagsPaginateResponsetagsTypeDef",
    {
        "configurationType": Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        "configurationId": str,
        "key": str,
        "value": str,
        "timeOfCreation": datetime,
    },
    total=False,
)

DescribeTagsPaginateResponseTypeDef = TypedDict(
    "DescribeTagsPaginateResponseTypeDef",
    {"tags": List[DescribeTagsPaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)

ListConfigurationsPaginateFiltersTypeDef = TypedDict(
    "ListConfigurationsPaginateFiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
    total=False,
)

_RequiredListConfigurationsPaginateOrderByTypeDef = TypedDict(
    "_RequiredListConfigurationsPaginateOrderByTypeDef", {"fieldName": str}
)
_OptionalListConfigurationsPaginateOrderByTypeDef = TypedDict(
    "_OptionalListConfigurationsPaginateOrderByTypeDef",
    {"sortOrder": Literal["ASC", "DESC"]},
    total=False,
)


class ListConfigurationsPaginateOrderByTypeDef(
    _RequiredListConfigurationsPaginateOrderByTypeDef,
    _OptionalListConfigurationsPaginateOrderByTypeDef,
):
    pass


ListConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListConfigurationsPaginateResponseTypeDef = TypedDict(
    "ListConfigurationsPaginateResponseTypeDef",
    {"configurations": List[Dict[str, str]], "NextToken": str},
    total=False,
)
