"Main interface for discovery service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchDeleteImportDataResponseerrorsTypeDef",
    "ClientBatchDeleteImportDataResponseTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateTagsTagsTypeDef",
    "ClientDeleteTagsTagsTypeDef",
    "ClientDescribeAgentsFiltersTypeDef",
    "ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef",
    "ClientDescribeAgentsResponseagentsInfoTypeDef",
    "ClientDescribeAgentsResponseTypeDef",
    "ClientDescribeConfigurationsResponseTypeDef",
    "ClientDescribeContinuousExportsResponsedescriptionsTypeDef",
    "ClientDescribeContinuousExportsResponseTypeDef",
    "ClientDescribeExportConfigurationsResponseexportsInfoTypeDef",
    "ClientDescribeExportConfigurationsResponseTypeDef",
    "ClientDescribeExportTasksFiltersTypeDef",
    "ClientDescribeExportTasksResponseexportsInfoTypeDef",
    "ClientDescribeExportTasksResponseTypeDef",
    "ClientDescribeImportTasksFiltersTypeDef",
    "ClientDescribeImportTasksResponsetasksTypeDef",
    "ClientDescribeImportTasksResponseTypeDef",
    "ClientDescribeTagsFiltersTypeDef",
    "ClientDescribeTagsResponsetagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientExportConfigurationsResponseTypeDef",
    "ClientGetDiscoverySummaryResponseagentSummaryTypeDef",
    "ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef",
    "ClientGetDiscoverySummaryResponseTypeDef",
    "ClientListConfigurationsFiltersTypeDef",
    "ClientListConfigurationsOrderByTypeDef",
    "ClientListConfigurationsResponseTypeDef",
    "ClientListServerNeighborsResponseneighborsTypeDef",
    "ClientListServerNeighborsResponseTypeDef",
    "ClientStartContinuousExportResponseTypeDef",
    "ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    "ClientStartDataCollectionByAgentIdsResponseTypeDef",
    "ClientStartExportTaskFiltersTypeDef",
    "ClientStartExportTaskResponseTypeDef",
    "ClientStartImportTaskResponsetaskTypeDef",
    "ClientStartImportTaskResponseTypeDef",
    "ClientStopContinuousExportResponseTypeDef",
    "ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    "ClientStopDataCollectionByAgentIdsResponseTypeDef",
    "DescribeAgentsPaginateFiltersTypeDef",
    "DescribeAgentsPaginatePaginationConfigTypeDef",
    "DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef",
    "DescribeAgentsPaginateResponseagentsInfoTypeDef",
    "DescribeAgentsPaginateResponseTypeDef",
    "DescribeContinuousExportsPaginatePaginationConfigTypeDef",
    "DescribeContinuousExportsPaginateResponsedescriptionsTypeDef",
    "DescribeContinuousExportsPaginateResponseTypeDef",
    "DescribeExportConfigurationsPaginatePaginationConfigTypeDef",
    "DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef",
    "DescribeExportConfigurationsPaginateResponseTypeDef",
    "DescribeExportTasksPaginateFiltersTypeDef",
    "DescribeExportTasksPaginatePaginationConfigTypeDef",
    "DescribeExportTasksPaginateResponseexportsInfoTypeDef",
    "DescribeExportTasksPaginateResponseTypeDef",
    "DescribeTagsPaginateFiltersTypeDef",
    "DescribeTagsPaginatePaginationConfigTypeDef",
    "DescribeTagsPaginateResponsetagsTypeDef",
    "DescribeTagsPaginateResponseTypeDef",
    "ListConfigurationsPaginateFiltersTypeDef",
    "ListConfigurationsPaginateOrderByTypeDef",
    "ListConfigurationsPaginatePaginationConfigTypeDef",
    "ListConfigurationsPaginateResponseTypeDef",
)


_ClientBatchDeleteImportDataResponseerrorsTypeDef = TypedDict(
    "_ClientBatchDeleteImportDataResponseerrorsTypeDef",
    {
        "importTaskId": str,
        "errorCode": Literal["NOT_FOUND", "INTERNAL_SERVER_ERROR", "OVER_LIMIT"],
        "errorDescription": str,
    },
    total=False,
)


class ClientBatchDeleteImportDataResponseerrorsTypeDef(
    _ClientBatchDeleteImportDataResponseerrorsTypeDef
):
    """
    - *(dict) --*

      Error messages returned for each import task that you deleted as a response for this command.
      - **importTaskId** *(string) --*

        The unique import ID associated with the error that occurred.
    """


_ClientBatchDeleteImportDataResponseTypeDef = TypedDict(
    "_ClientBatchDeleteImportDataResponseTypeDef",
    {"errors": List[ClientBatchDeleteImportDataResponseerrorsTypeDef]},
    total=False,
)


class ClientBatchDeleteImportDataResponseTypeDef(_ClientBatchDeleteImportDataResponseTypeDef):
    """
    - *(dict) --*

      - **errors** *(list) --*

        Error messages returned for each import task that you deleted as a response for this
        command.
        - *(dict) --*

          Error messages returned for each import task that you deleted as a response for this
          command.
          - **importTaskId** *(string) --*

            The unique import ID associated with the error that occurred.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef", {"configurationId": str}, total=False
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    - *(dict) --*

      - **configurationId** *(string) --*

        Configuration ID of an application to be created.
    """


_ClientCreateTagsTagsTypeDef = TypedDict(
    "_ClientCreateTagsTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateTagsTagsTypeDef(_ClientCreateTagsTagsTypeDef):
    pass


_ClientDeleteTagsTagsTypeDef = TypedDict(
    "_ClientDeleteTagsTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDeleteTagsTagsTypeDef(_ClientDeleteTagsTagsTypeDef):
    pass


_ClientDescribeAgentsFiltersTypeDef = TypedDict(
    "_ClientDescribeAgentsFiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
    total=False,
)


class ClientDescribeAgentsFiltersTypeDef(_ClientDescribeAgentsFiltersTypeDef):
    pass


_ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef = TypedDict(
    "_ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef",
    {"ipAddress": str, "macAddress": str},
    total=False,
)


class ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef(
    _ClientDescribeAgentsResponseagentsInfoagentNetworkInfoListTypeDef
):
    pass


_ClientDescribeAgentsResponseagentsInfoTypeDef = TypedDict(
    "_ClientDescribeAgentsResponseagentsInfoTypeDef",
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


class ClientDescribeAgentsResponseagentsInfoTypeDef(_ClientDescribeAgentsResponseagentsInfoTypeDef):
    """
    - *(dict) --*

      Information about agents or connectors associated with the user’s AWS account. Information
      includes agent or connector IDs, IP addresses, media access control (MAC) addresses, agent or
      connector health, hostname where the agent or connector resides, and agent version for each
      agent.
      - **agentId** *(string) --*

        The agent or connector ID.
    """


_ClientDescribeAgentsResponseTypeDef = TypedDict(
    "_ClientDescribeAgentsResponseTypeDef",
    {"agentsInfo": List[ClientDescribeAgentsResponseagentsInfoTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeAgentsResponseTypeDef(_ClientDescribeAgentsResponseTypeDef):
    """
    - *(dict) --*

      - **agentsInfo** *(list) --*

        Lists agents or the Connector by ID or lists all agents/Connectors associated with your user
        account if you did not specify an agent/Connector ID. The output includes agent/Connector
        IDs, IP addresses, media access control (MAC) addresses, agent/Connector health, host name
        where the agent/Connector resides, and the version number of each agent/Connector.
        - *(dict) --*

          Information about agents or connectors associated with the user’s AWS account. Information
          includes agent or connector IDs, IP addresses, media access control (MAC) addresses, agent
          or connector health, hostname where the agent or connector resides, and agent version for
          each agent.
          - **agentId** *(string) --*

            The agent or connector ID.
    """


_ClientDescribeConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationsResponseTypeDef",
    {"configurations": List[Dict[str, str]]},
    total=False,
)


class ClientDescribeConfigurationsResponseTypeDef(_ClientDescribeConfigurationsResponseTypeDef):
    """
    - *(dict) --*

      - **configurations** *(list) --*

        A key in the response map. The value is an array of data.
        - *(dict) --*

          - *(string) --*

            - *(string) --*
    """


_ClientDescribeContinuousExportsResponsedescriptionsTypeDef = TypedDict(
    "_ClientDescribeContinuousExportsResponsedescriptionsTypeDef",
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


class ClientDescribeContinuousExportsResponsedescriptionsTypeDef(
    _ClientDescribeContinuousExportsResponsedescriptionsTypeDef
):
    """
    - *(dict) --*

      A list of continuous export descriptions.
      - **exportId** *(string) --*

        The unique ID assigned to this export.
    """


_ClientDescribeContinuousExportsResponseTypeDef = TypedDict(
    "_ClientDescribeContinuousExportsResponseTypeDef",
    {
        "descriptions": List[ClientDescribeContinuousExportsResponsedescriptionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeContinuousExportsResponseTypeDef(
    _ClientDescribeContinuousExportsResponseTypeDef
):
    """
    - *(dict) --*

      - **descriptions** *(list) --*

        A list of continuous export descriptions.
        - *(dict) --*

          A list of continuous export descriptions.
          - **exportId** *(string) --*

            The unique ID assigned to this export.
    """


_ClientDescribeExportConfigurationsResponseexportsInfoTypeDef = TypedDict(
    "_ClientDescribeExportConfigurationsResponseexportsInfoTypeDef",
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


class ClientDescribeExportConfigurationsResponseexportsInfoTypeDef(
    _ClientDescribeExportConfigurationsResponseexportsInfoTypeDef
):
    """
    - *(dict) --*

      Information regarding the export status of discovered data. The value is an array of objects.
      - **exportId** *(string) --*

        A unique identifier used to query an export.
    """


_ClientDescribeExportConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeExportConfigurationsResponseTypeDef",
    {
        "exportsInfo": List[ClientDescribeExportConfigurationsResponseexportsInfoTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeExportConfigurationsResponseTypeDef(
    _ClientDescribeExportConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **exportsInfo** *(list) --*

        - *(dict) --*

          Information regarding the export status of discovered data. The value is an array of
          objects.
          - **exportId** *(string) --*

            A unique identifier used to query an export.
    """


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
    """
    - *(dict) --*

      Used to select which agent's data is to be exported. A single agent ID may be selected for
      export using the `StartExportTask
      <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html>`__
      action.
      - **name** *(string) --***[REQUIRED]**

        A single ``ExportFilter`` name. Supported filters: ``agentId`` .
    """


_ClientDescribeExportTasksResponseexportsInfoTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseexportsInfoTypeDef",
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


class ClientDescribeExportTasksResponseexportsInfoTypeDef(
    _ClientDescribeExportTasksResponseexportsInfoTypeDef
):
    """
    - *(dict) --*

      Information regarding the export status of discovered data. The value is an array of objects.
      - **exportId** *(string) --*

        A unique identifier used to query an export.
    """


_ClientDescribeExportTasksResponseTypeDef = TypedDict(
    "_ClientDescribeExportTasksResponseTypeDef",
    {"exportsInfo": List[ClientDescribeExportTasksResponseexportsInfoTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeExportTasksResponseTypeDef(_ClientDescribeExportTasksResponseTypeDef):
    """
    - *(dict) --*

      - **exportsInfo** *(list) --*

        Contains one or more sets of export request details. When the status of a request is
        ``SUCCEEDED`` , the response includes a URL for an Amazon S3 bucket where you can view the
        data in a CSV file.
        - *(dict) --*

          Information regarding the export status of discovered data. The value is an array of
          objects.
          - **exportId** *(string) --*

            A unique identifier used to query an export.
    """


_ClientDescribeImportTasksFiltersTypeDef = TypedDict(
    "_ClientDescribeImportTasksFiltersTypeDef",
    {"name": Literal["IMPORT_TASK_ID", "STATUS", "NAME"], "values": List[str]},
    total=False,
)


class ClientDescribeImportTasksFiltersTypeDef(_ClientDescribeImportTasksFiltersTypeDef):
    """
    - *(dict) --*

      A name-values pair of elements you can use to filter the results when querying your import
      tasks. Currently, wildcards are not supported for filters.
      .. note::

        When filtering by import status, all other filter values are ignored.
    """


_ClientDescribeImportTasksResponsetasksTypeDef = TypedDict(
    "_ClientDescribeImportTasksResponsetasksTypeDef",
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


class ClientDescribeImportTasksResponsetasksTypeDef(_ClientDescribeImportTasksResponsetasksTypeDef):
    pass


_ClientDescribeImportTasksResponseTypeDef = TypedDict(
    "_ClientDescribeImportTasksResponseTypeDef",
    {"nextToken": str, "tasks": List[ClientDescribeImportTasksResponsetasksTypeDef]},
    total=False,
)


class ClientDescribeImportTasksResponseTypeDef(_ClientDescribeImportTasksResponseTypeDef):
    """
    - *(dict) --*

      - **nextToken** *(string) --*

        The token to request the next page of results.
    """


_RequiredClientDescribeTagsFiltersTypeDef = TypedDict(
    "_RequiredClientDescribeTagsFiltersTypeDef", {"name": str}
)
_OptionalClientDescribeTagsFiltersTypeDef = TypedDict(
    "_OptionalClientDescribeTagsFiltersTypeDef", {"values": List[str]}, total=False
)


class ClientDescribeTagsFiltersTypeDef(
    _RequiredClientDescribeTagsFiltersTypeDef, _OptionalClientDescribeTagsFiltersTypeDef
):
    """
    - *(dict) --*

      The tag filter. Valid names are: ``tagKey`` , ``tagValue`` , ``configurationId`` .
      - **name** *(string) --***[REQUIRED]**

        A name of the tag filter.
    """


_ClientDescribeTagsResponsetagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponsetagsTypeDef",
    {
        "configurationType": Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        "configurationId": str,
        "key": str,
        "value": str,
        "timeOfCreation": datetime,
    },
    total=False,
)


class ClientDescribeTagsResponsetagsTypeDef(_ClientDescribeTagsResponsetagsTypeDef):
    """
    - *(dict) --*

      Tags for a configuration item. Tags are metadata that help you categorize IT assets.
      - **configurationType** *(string) --*

        A type of IT asset to tag.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"tags": List[ClientDescribeTagsResponsetagsTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        Depending on the input, this is a list of configuration items tagged with a specific tag, or
        a list of tags for a specific configuration item.
        - *(dict) --*

          Tags for a configuration item. Tags are metadata that help you categorize IT assets.
          - **configurationType** *(string) --*

            A type of IT asset to tag.
    """


_ClientExportConfigurationsResponseTypeDef = TypedDict(
    "_ClientExportConfigurationsResponseTypeDef", {"exportId": str}, total=False
)


class ClientExportConfigurationsResponseTypeDef(_ClientExportConfigurationsResponseTypeDef):
    """
    - *(dict) --*

      - **exportId** *(string) --*

        A unique identifier that you can use to query the export status.
    """


_ClientGetDiscoverySummaryResponseagentSummaryTypeDef = TypedDict(
    "_ClientGetDiscoverySummaryResponseagentSummaryTypeDef",
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


class ClientGetDiscoverySummaryResponseagentSummaryTypeDef(
    _ClientGetDiscoverySummaryResponseagentSummaryTypeDef
):
    pass


_ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef = TypedDict(
    "_ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef",
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


class ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef(
    _ClientGetDiscoverySummaryResponseconnectorSummaryTypeDef
):
    pass


_ClientGetDiscoverySummaryResponseTypeDef = TypedDict(
    "_ClientGetDiscoverySummaryResponseTypeDef",
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


class ClientGetDiscoverySummaryResponseTypeDef(_ClientGetDiscoverySummaryResponseTypeDef):
    """
    - *(dict) --*

      - **servers** *(integer) --*

        The number of servers discovered.
    """


_ClientListConfigurationsFiltersTypeDef = TypedDict(
    "_ClientListConfigurationsFiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
    total=False,
)


class ClientListConfigurationsFiltersTypeDef(_ClientListConfigurationsFiltersTypeDef):
    pass


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
    """
    - *(dict) --*

      A field and direction for ordered output.
      - **fieldName** *(string) --***[REQUIRED]**

        The field on which to order.
    """


_ClientListConfigurationsResponseTypeDef = TypedDict(
    "_ClientListConfigurationsResponseTypeDef",
    {"configurations": List[Dict[str, str]], "nextToken": str},
    total=False,
)


class ClientListConfigurationsResponseTypeDef(_ClientListConfigurationsResponseTypeDef):
    """
    - *(dict) --*

      - **configurations** *(list) --*

        Returns configuration details, including the configuration ID, attribute names, and
        attribute values.
        - *(dict) --*

          - *(string) --*

            - *(string) --*
    """


_ClientListServerNeighborsResponseneighborsTypeDef = TypedDict(
    "_ClientListServerNeighborsResponseneighborsTypeDef",
    {
        "sourceServerId": str,
        "destinationServerId": str,
        "destinationPort": int,
        "transportProtocol": str,
        "connectionsCount": int,
    },
    total=False,
)


class ClientListServerNeighborsResponseneighborsTypeDef(
    _ClientListServerNeighborsResponseneighborsTypeDef
):
    """
    - *(dict) --*

      Details about neighboring servers.
      - **sourceServerId** *(string) --*

        The ID of the server that opened the network connection.
    """


_ClientListServerNeighborsResponseTypeDef = TypedDict(
    "_ClientListServerNeighborsResponseTypeDef",
    {
        "neighbors": List[ClientListServerNeighborsResponseneighborsTypeDef],
        "nextToken": str,
        "knownDependencyCount": int,
    },
    total=False,
)


class ClientListServerNeighborsResponseTypeDef(_ClientListServerNeighborsResponseTypeDef):
    """
    - *(dict) --*

      - **neighbors** *(list) --*

        List of distinct servers that are one hop away from the given server.
        - *(dict) --*

          Details about neighboring servers.
          - **sourceServerId** *(string) --*

            The ID of the server that opened the network connection.
    """


_ClientStartContinuousExportResponseTypeDef = TypedDict(
    "_ClientStartContinuousExportResponseTypeDef",
    {
        "exportId": str,
        "s3Bucket": str,
        "startTime": datetime,
        "dataSource": str,
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)


class ClientStartContinuousExportResponseTypeDef(_ClientStartContinuousExportResponseTypeDef):
    """
    - *(dict) --*

      - **exportId** *(string) --*

        The unique ID assigned to this export.
    """


_ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef = TypedDict(
    "_ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    {"agentId": str, "operationSucceeded": bool, "description": str},
    total=False,
)


class ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef(
    _ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
):
    """
    - *(dict) --*

      Information about agents or connectors that were instructed to start collecting data.
      Information includes the agent/connector ID, a description of the operation, and whether the
      agent/connector configuration was updated.
      - **agentId** *(string) --*

        The agent/connector ID.
    """


_ClientStartDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "_ClientStartDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List[
            ClientStartDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
        ]
    },
    total=False,
)


class ClientStartDataCollectionByAgentIdsResponseTypeDef(
    _ClientStartDataCollectionByAgentIdsResponseTypeDef
):
    """
    - *(dict) --*

      - **agentsConfigurationStatus** *(list) --*

        Information about agents or the connector that were instructed to start collecting data.
        Information includes the agent/connector ID, a description of the operation performed, and
        whether the agent/connector configuration was updated.
        - *(dict) --*

          Information about agents or connectors that were instructed to start collecting data.
          Information includes the agent/connector ID, a description of the operation, and whether
          the agent/connector configuration was updated.
          - **agentId** *(string) --*

            The agent/connector ID.
    """


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
    """
    - *(dict) --*

      Used to select which agent's data is to be exported. A single agent ID may be selected for
      export using the `StartExportTask
      <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html>`__
      action.
      - **name** *(string) --***[REQUIRED]**

        A single ``ExportFilter`` name. Supported filters: ``agentId`` .
    """


_ClientStartExportTaskResponseTypeDef = TypedDict(
    "_ClientStartExportTaskResponseTypeDef", {"exportId": str}, total=False
)


class ClientStartExportTaskResponseTypeDef(_ClientStartExportTaskResponseTypeDef):
    """
    - *(dict) --*

      - **exportId** *(string) --*

        A unique identifier used to query the status of an export request.
    """


_ClientStartImportTaskResponsetaskTypeDef = TypedDict(
    "_ClientStartImportTaskResponsetaskTypeDef",
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


class ClientStartImportTaskResponsetaskTypeDef(_ClientStartImportTaskResponsetaskTypeDef):
    """
    - **task** *(dict) --*

      An array of information related to the import task request including status information,
      times, IDs, the Amazon S3 Object URL for the import file, and more.
      - **importTaskId** *(string) --*

        The unique ID for a specific import task. These IDs aren't globally unique, but they are
        unique within an AWS account.
    """


_ClientStartImportTaskResponseTypeDef = TypedDict(
    "_ClientStartImportTaskResponseTypeDef",
    {"task": ClientStartImportTaskResponsetaskTypeDef},
    total=False,
)


class ClientStartImportTaskResponseTypeDef(_ClientStartImportTaskResponseTypeDef):
    """
    - *(dict) --*

      - **task** *(dict) --*

        An array of information related to the import task request including status information,
        times, IDs, the Amazon S3 Object URL for the import file, and more.
        - **importTaskId** *(string) --*

          The unique ID for a specific import task. These IDs aren't globally unique, but they are
          unique within an AWS account.
    """


_ClientStopContinuousExportResponseTypeDef = TypedDict(
    "_ClientStopContinuousExportResponseTypeDef",
    {"startTime": datetime, "stopTime": datetime},
    total=False,
)


class ClientStopContinuousExportResponseTypeDef(_ClientStopContinuousExportResponseTypeDef):
    """
    - *(dict) --*

      - **startTime** *(datetime) --*

        Timestamp that represents when this continuous export started collecting data.
    """


_ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef = TypedDict(
    "_ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef",
    {"agentId": str, "operationSucceeded": bool, "description": str},
    total=False,
)


class ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef(
    _ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
):
    """
    - *(dict) --*

      Information about agents or connectors that were instructed to start collecting data.
      Information includes the agent/connector ID, a description of the operation, and whether the
      agent/connector configuration was updated.
      - **agentId** *(string) --*

        The agent/connector ID.
    """


_ClientStopDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "_ClientStopDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List[
            ClientStopDataCollectionByAgentIdsResponseagentsConfigurationStatusTypeDef
        ]
    },
    total=False,
)


class ClientStopDataCollectionByAgentIdsResponseTypeDef(
    _ClientStopDataCollectionByAgentIdsResponseTypeDef
):
    """
    - *(dict) --*

      - **agentsConfigurationStatus** *(list) --*

        Information about the agents or connector that were instructed to stop collecting data.
        Information includes the agent/connector ID, a description of the operation performed, and
        whether the agent/connector configuration was updated.
        - *(dict) --*

          Information about agents or connectors that were instructed to start collecting data.
          Information includes the agent/connector ID, a description of the operation, and whether
          the agent/connector configuration was updated.
          - **agentId** *(string) --*

            The agent/connector ID.
    """


_DescribeAgentsPaginateFiltersTypeDef = TypedDict(
    "_DescribeAgentsPaginateFiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
    total=False,
)


class DescribeAgentsPaginateFiltersTypeDef(_DescribeAgentsPaginateFiltersTypeDef):
    pass


_DescribeAgentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAgentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAgentsPaginatePaginationConfigTypeDef(_DescribeAgentsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef = TypedDict(
    "_DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef",
    {"ipAddress": str, "macAddress": str},
    total=False,
)


class DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef(
    _DescribeAgentsPaginateResponseagentsInfoagentNetworkInfoListTypeDef
):
    pass


_DescribeAgentsPaginateResponseagentsInfoTypeDef = TypedDict(
    "_DescribeAgentsPaginateResponseagentsInfoTypeDef",
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


class DescribeAgentsPaginateResponseagentsInfoTypeDef(
    _DescribeAgentsPaginateResponseagentsInfoTypeDef
):
    """
    - *(dict) --*

      Information about agents or connectors associated with the user’s AWS account. Information
      includes agent or connector IDs, IP addresses, media access control (MAC) addresses, agent or
      connector health, hostname where the agent or connector resides, and agent version for each
      agent.
      - **agentId** *(string) --*

        The agent or connector ID.
    """


_DescribeAgentsPaginateResponseTypeDef = TypedDict(
    "_DescribeAgentsPaginateResponseTypeDef",
    {"agentsInfo": List[DescribeAgentsPaginateResponseagentsInfoTypeDef], "NextToken": str},
    total=False,
)


class DescribeAgentsPaginateResponseTypeDef(_DescribeAgentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **agentsInfo** *(list) --*

        Lists agents or the Connector by ID or lists all agents/Connectors associated with your user
        account if you did not specify an agent/Connector ID. The output includes agent/Connector
        IDs, IP addresses, media access control (MAC) addresses, agent/Connector health, host name
        where the agent/Connector resides, and the version number of each agent/Connector.
        - *(dict) --*

          Information about agents or connectors associated with the user’s AWS account. Information
          includes agent or connector IDs, IP addresses, media access control (MAC) addresses, agent
          or connector health, hostname where the agent or connector resides, and agent version for
          each agent.
          - **agentId** *(string) --*

            The agent or connector ID.
    """


_DescribeContinuousExportsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeContinuousExportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeContinuousExportsPaginatePaginationConfigTypeDef(
    _DescribeContinuousExportsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeContinuousExportsPaginateResponsedescriptionsTypeDef = TypedDict(
    "_DescribeContinuousExportsPaginateResponsedescriptionsTypeDef",
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


class DescribeContinuousExportsPaginateResponsedescriptionsTypeDef(
    _DescribeContinuousExportsPaginateResponsedescriptionsTypeDef
):
    """
    - *(dict) --*

      A list of continuous export descriptions.
      - **exportId** *(string) --*

        The unique ID assigned to this export.
    """


_DescribeContinuousExportsPaginateResponseTypeDef = TypedDict(
    "_DescribeContinuousExportsPaginateResponseTypeDef",
    {
        "descriptions": List[DescribeContinuousExportsPaginateResponsedescriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeContinuousExportsPaginateResponseTypeDef(
    _DescribeContinuousExportsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **descriptions** *(list) --*

        A list of continuous export descriptions.
        - *(dict) --*

          A list of continuous export descriptions.
          - **exportId** *(string) --*

            The unique ID assigned to this export.
    """


_DescribeExportConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeExportConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeExportConfigurationsPaginatePaginationConfigTypeDef(
    _DescribeExportConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef = TypedDict(
    "_DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef",
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


class DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef(
    _DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef
):
    """
    - *(dict) --*

      Information regarding the export status of discovered data. The value is an array of objects.
      - **exportId** *(string) --*

        A unique identifier used to query an export.
    """


_DescribeExportConfigurationsPaginateResponseTypeDef = TypedDict(
    "_DescribeExportConfigurationsPaginateResponseTypeDef",
    {
        "exportsInfo": List[DescribeExportConfigurationsPaginateResponseexportsInfoTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeExportConfigurationsPaginateResponseTypeDef(
    _DescribeExportConfigurationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **exportsInfo** *(list) --*

        - *(dict) --*

          Information regarding the export status of discovered data. The value is an array of
          objects.
          - **exportId** *(string) --*

            A unique identifier used to query an export.
    """


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
    """
    - *(dict) --*

      Used to select which agent's data is to be exported. A single agent ID may be selected for
      export using the `StartExportTask
      <http://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html>`__
      action.
      - **name** *(string) --***[REQUIRED]**

        A single ``ExportFilter`` name. Supported filters: ``agentId`` .
    """


_DescribeExportTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeExportTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeExportTasksPaginatePaginationConfigTypeDef(
    _DescribeExportTasksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeExportTasksPaginateResponseexportsInfoTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseexportsInfoTypeDef",
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


class DescribeExportTasksPaginateResponseexportsInfoTypeDef(
    _DescribeExportTasksPaginateResponseexportsInfoTypeDef
):
    """
    - *(dict) --*

      Information regarding the export status of discovered data. The value is an array of objects.
      - **exportId** *(string) --*

        A unique identifier used to query an export.
    """


_DescribeExportTasksPaginateResponseTypeDef = TypedDict(
    "_DescribeExportTasksPaginateResponseTypeDef",
    {"exportsInfo": List[DescribeExportTasksPaginateResponseexportsInfoTypeDef], "NextToken": str},
    total=False,
)


class DescribeExportTasksPaginateResponseTypeDef(_DescribeExportTasksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **exportsInfo** *(list) --*

        Contains one or more sets of export request details. When the status of a request is
        ``SUCCEEDED`` , the response includes a URL for an Amazon S3 bucket where you can view the
        data in a CSV file.
        - *(dict) --*

          Information regarding the export status of discovered data. The value is an array of
          objects.
          - **exportId** *(string) --*

            A unique identifier used to query an export.
    """


_RequiredDescribeTagsPaginateFiltersTypeDef = TypedDict(
    "_RequiredDescribeTagsPaginateFiltersTypeDef", {"name": str}
)
_OptionalDescribeTagsPaginateFiltersTypeDef = TypedDict(
    "_OptionalDescribeTagsPaginateFiltersTypeDef", {"values": List[str]}, total=False
)


class DescribeTagsPaginateFiltersTypeDef(
    _RequiredDescribeTagsPaginateFiltersTypeDef, _OptionalDescribeTagsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      The tag filter. Valid names are: ``tagKey`` , ``tagValue`` , ``configurationId`` .
      - **name** *(string) --***[REQUIRED]**

        A name of the tag filter.
    """


_DescribeTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTagsPaginatePaginationConfigTypeDef(_DescribeTagsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeTagsPaginateResponsetagsTypeDef = TypedDict(
    "_DescribeTagsPaginateResponsetagsTypeDef",
    {
        "configurationType": Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        "configurationId": str,
        "key": str,
        "value": str,
        "timeOfCreation": datetime,
    },
    total=False,
)


class DescribeTagsPaginateResponsetagsTypeDef(_DescribeTagsPaginateResponsetagsTypeDef):
    """
    - *(dict) --*

      Tags for a configuration item. Tags are metadata that help you categorize IT assets.
      - **configurationType** *(string) --*

        A type of IT asset to tag.
    """


_DescribeTagsPaginateResponseTypeDef = TypedDict(
    "_DescribeTagsPaginateResponseTypeDef",
    {"tags": List[DescribeTagsPaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)


class DescribeTagsPaginateResponseTypeDef(_DescribeTagsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        Depending on the input, this is a list of configuration items tagged with a specific tag, or
        a list of tags for a specific configuration item.
        - *(dict) --*

          Tags for a configuration item. Tags are metadata that help you categorize IT assets.
          - **configurationType** *(string) --*

            A type of IT asset to tag.
    """


_ListConfigurationsPaginateFiltersTypeDef = TypedDict(
    "_ListConfigurationsPaginateFiltersTypeDef",
    {"name": str, "values": List[str], "condition": str},
    total=False,
)


class ListConfigurationsPaginateFiltersTypeDef(_ListConfigurationsPaginateFiltersTypeDef):
    pass


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
    """
    - *(dict) --*

      A field and direction for ordered output.
      - **fieldName** *(string) --***[REQUIRED]**

        The field on which to order.
    """


_ListConfigurationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConfigurationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConfigurationsPaginatePaginationConfigTypeDef(
    _ListConfigurationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListConfigurationsPaginateResponseTypeDef = TypedDict(
    "_ListConfigurationsPaginateResponseTypeDef",
    {"configurations": List[Dict[str, str]], "NextToken": str},
    total=False,
)


class ListConfigurationsPaginateResponseTypeDef(_ListConfigurationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **configurations** *(list) --*

        Returns configuration details, including the configuration ID, attribute names, and
        attribute values.
        - *(dict) --*

          - *(string) --*

            - *(string) --*
    """
