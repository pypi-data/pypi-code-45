"Main interface for iotthingsgraph service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


_RequiredClientCreateFlowTemplateDefinitionTypeDef = TypedDict(
    "_RequiredClientCreateFlowTemplateDefinitionTypeDef", {"language": str}
)
_OptionalClientCreateFlowTemplateDefinitionTypeDef = TypedDict(
    "_OptionalClientCreateFlowTemplateDefinitionTypeDef", {"text": str}, total=False
)


class ClientCreateFlowTemplateDefinitionTypeDef(
    _RequiredClientCreateFlowTemplateDefinitionTypeDef,
    _OptionalClientCreateFlowTemplateDefinitionTypeDef,
):
    pass


ClientCreateFlowTemplateResponsesummaryTypeDef = TypedDict(
    "ClientCreateFlowTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

ClientCreateFlowTemplateResponseTypeDef = TypedDict(
    "ClientCreateFlowTemplateResponseTypeDef",
    {"summary": ClientCreateFlowTemplateResponsesummaryTypeDef},
    total=False,
)

_RequiredClientCreateSystemInstanceDefinitionTypeDef = TypedDict(
    "_RequiredClientCreateSystemInstanceDefinitionTypeDef", {"language": str}
)
_OptionalClientCreateSystemInstanceDefinitionTypeDef = TypedDict(
    "_OptionalClientCreateSystemInstanceDefinitionTypeDef", {"text": str}, total=False
)


class ClientCreateSystemInstanceDefinitionTypeDef(
    _RequiredClientCreateSystemInstanceDefinitionTypeDef,
    _OptionalClientCreateSystemInstanceDefinitionTypeDef,
):
    pass


ClientCreateSystemInstanceMetricsConfigurationTypeDef = TypedDict(
    "ClientCreateSystemInstanceMetricsConfigurationTypeDef",
    {"cloudMetricEnabled": bool, "metricRuleRoleArn": str},
    total=False,
)

ClientCreateSystemInstanceResponsesummaryTypeDef = TypedDict(
    "ClientCreateSystemInstanceResponsesummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": Literal[
            "NOT_DEPLOYED",
            "BOOTSTRAP",
            "DEPLOY_IN_PROGRESS",
            "DEPLOYED_IN_TARGET",
            "UNDEPLOY_IN_PROGRESS",
            "FAILED",
            "PENDING_DELETE",
            "DELETED_IN_TARGET",
        ],
        "target": Literal["GREENGRASS", "CLOUD"],
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)

ClientCreateSystemInstanceResponseTypeDef = TypedDict(
    "ClientCreateSystemInstanceResponseTypeDef",
    {"summary": ClientCreateSystemInstanceResponsesummaryTypeDef},
    total=False,
)

_RequiredClientCreateSystemInstanceTagsTypeDef = TypedDict(
    "_RequiredClientCreateSystemInstanceTagsTypeDef", {"key": str}
)
_OptionalClientCreateSystemInstanceTagsTypeDef = TypedDict(
    "_OptionalClientCreateSystemInstanceTagsTypeDef", {"value": str}, total=False
)


class ClientCreateSystemInstanceTagsTypeDef(
    _RequiredClientCreateSystemInstanceTagsTypeDef, _OptionalClientCreateSystemInstanceTagsTypeDef
):
    pass


_RequiredClientCreateSystemTemplateDefinitionTypeDef = TypedDict(
    "_RequiredClientCreateSystemTemplateDefinitionTypeDef", {"language": str}
)
_OptionalClientCreateSystemTemplateDefinitionTypeDef = TypedDict(
    "_OptionalClientCreateSystemTemplateDefinitionTypeDef", {"text": str}, total=False
)


class ClientCreateSystemTemplateDefinitionTypeDef(
    _RequiredClientCreateSystemTemplateDefinitionTypeDef,
    _OptionalClientCreateSystemTemplateDefinitionTypeDef,
):
    pass


ClientCreateSystemTemplateResponsesummaryTypeDef = TypedDict(
    "ClientCreateSystemTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

ClientCreateSystemTemplateResponseTypeDef = TypedDict(
    "ClientCreateSystemTemplateResponseTypeDef",
    {"summary": ClientCreateSystemTemplateResponsesummaryTypeDef},
    total=False,
)

ClientDeleteNamespaceResponseTypeDef = TypedDict(
    "ClientDeleteNamespaceResponseTypeDef", {"namespaceArn": str, "namespaceName": str}, total=False
)

ClientDeploySystemInstanceResponsesummaryTypeDef = TypedDict(
    "ClientDeploySystemInstanceResponsesummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": Literal[
            "NOT_DEPLOYED",
            "BOOTSTRAP",
            "DEPLOY_IN_PROGRESS",
            "DEPLOYED_IN_TARGET",
            "UNDEPLOY_IN_PROGRESS",
            "FAILED",
            "PENDING_DELETE",
            "DELETED_IN_TARGET",
        ],
        "target": Literal["GREENGRASS", "CLOUD"],
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)

ClientDeploySystemInstanceResponseTypeDef = TypedDict(
    "ClientDeploySystemInstanceResponseTypeDef",
    {"summary": ClientDeploySystemInstanceResponsesummaryTypeDef, "greengrassDeploymentId": str},
    total=False,
)

ClientDescribeNamespaceResponseTypeDef = TypedDict(
    "ClientDescribeNamespaceResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "trackingNamespaceName": str,
        "trackingNamespaceVersion": int,
        "namespaceVersion": int,
    },
    total=False,
)

ClientGetEntitiesResponsedescriptionsdefinitionTypeDef = TypedDict(
    "ClientGetEntitiesResponsedescriptionsdefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)

ClientGetEntitiesResponsedescriptionsTypeDef = TypedDict(
    "ClientGetEntitiesResponsedescriptionsTypeDef",
    {
        "id": str,
        "arn": str,
        "type": Literal[
            "DEVICE",
            "SERVICE",
            "DEVICE_MODEL",
            "CAPABILITY",
            "STATE",
            "ACTION",
            "EVENT",
            "PROPERTY",
            "MAPPING",
            "ENUM",
        ],
        "createdAt": datetime,
        "definition": ClientGetEntitiesResponsedescriptionsdefinitionTypeDef,
    },
    total=False,
)

ClientGetEntitiesResponseTypeDef = TypedDict(
    "ClientGetEntitiesResponseTypeDef",
    {"descriptions": List[ClientGetEntitiesResponsedescriptionsTypeDef]},
    total=False,
)

ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef = TypedDict(
    "ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)

ClientGetFlowTemplateResponsedescriptionsummaryTypeDef = TypedDict(
    "ClientGetFlowTemplateResponsedescriptionsummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

ClientGetFlowTemplateResponsedescriptionTypeDef = TypedDict(
    "ClientGetFlowTemplateResponsedescriptionTypeDef",
    {
        "summary": ClientGetFlowTemplateResponsedescriptionsummaryTypeDef,
        "definition": ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef,
        "validatedNamespaceVersion": int,
    },
    total=False,
)

ClientGetFlowTemplateResponseTypeDef = TypedDict(
    "ClientGetFlowTemplateResponseTypeDef",
    {"description": ClientGetFlowTemplateResponsedescriptionTypeDef},
    total=False,
)

ClientGetFlowTemplateRevisionsResponsesummariesTypeDef = TypedDict(
    "ClientGetFlowTemplateRevisionsResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

ClientGetFlowTemplateRevisionsResponseTypeDef = TypedDict(
    "ClientGetFlowTemplateRevisionsResponseTypeDef",
    {"summaries": List[ClientGetFlowTemplateRevisionsResponsesummariesTypeDef], "nextToken": str},
    total=False,
)

ClientGetNamespaceDeletionStatusResponseTypeDef = TypedDict(
    "ClientGetNamespaceDeletionStatusResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef = TypedDict(
    "ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)

ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef = TypedDict(
    "ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef",
    {"cloudMetricEnabled": bool, "metricRuleRoleArn": str},
    total=False,
)

ClientGetSystemInstanceResponsedescriptionsummaryTypeDef = TypedDict(
    "ClientGetSystemInstanceResponsedescriptionsummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": Literal[
            "NOT_DEPLOYED",
            "BOOTSTRAP",
            "DEPLOY_IN_PROGRESS",
            "DEPLOYED_IN_TARGET",
            "UNDEPLOY_IN_PROGRESS",
            "FAILED",
            "PENDING_DELETE",
            "DELETED_IN_TARGET",
        ],
        "target": Literal["GREENGRASS", "CLOUD"],
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)

ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef = TypedDict(
    "ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef",
    {"id": str, "revisionNumber": int},
    total=False,
)

ClientGetSystemInstanceResponsedescriptionTypeDef = TypedDict(
    "ClientGetSystemInstanceResponsedescriptionTypeDef",
    {
        "summary": ClientGetSystemInstanceResponsedescriptionsummaryTypeDef,
        "definition": ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef,
        "s3BucketName": str,
        "metricsConfiguration": ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef,
        "validatedNamespaceVersion": int,
        "validatedDependencyRevisions": List[
            ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef
        ],
        "flowActionsRoleArn": str,
    },
    total=False,
)

ClientGetSystemInstanceResponseTypeDef = TypedDict(
    "ClientGetSystemInstanceResponseTypeDef",
    {"description": ClientGetSystemInstanceResponsedescriptionTypeDef},
    total=False,
)

ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef = TypedDict(
    "ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)

ClientGetSystemTemplateResponsedescriptionsummaryTypeDef = TypedDict(
    "ClientGetSystemTemplateResponsedescriptionsummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

ClientGetSystemTemplateResponsedescriptionTypeDef = TypedDict(
    "ClientGetSystemTemplateResponsedescriptionTypeDef",
    {
        "summary": ClientGetSystemTemplateResponsedescriptionsummaryTypeDef,
        "definition": ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef,
        "validatedNamespaceVersion": int,
    },
    total=False,
)

ClientGetSystemTemplateResponseTypeDef = TypedDict(
    "ClientGetSystemTemplateResponseTypeDef",
    {"description": ClientGetSystemTemplateResponsedescriptionTypeDef},
    total=False,
)

ClientGetSystemTemplateRevisionsResponsesummariesTypeDef = TypedDict(
    "ClientGetSystemTemplateRevisionsResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

ClientGetSystemTemplateRevisionsResponseTypeDef = TypedDict(
    "ClientGetSystemTemplateRevisionsResponseTypeDef",
    {"summaries": List[ClientGetSystemTemplateRevisionsResponsesummariesTypeDef], "nextToken": str},
    total=False,
)

ClientGetUploadStatusResponseTypeDef = TypedDict(
    "ClientGetUploadStatusResponseTypeDef",
    {
        "uploadId": str,
        "uploadStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "namespaceArn": str,
        "namespaceName": str,
        "namespaceVersion": int,
        "failureReason": List[str],
        "createdDate": datetime,
    },
    total=False,
)

ClientListFlowExecutionMessagesResponsemessagesTypeDef = TypedDict(
    "ClientListFlowExecutionMessagesResponsemessagesTypeDef",
    {
        "messageId": str,
        "eventType": Literal[
            "EXECUTION_STARTED",
            "EXECUTION_FAILED",
            "EXECUTION_ABORTED",
            "EXECUTION_SUCCEEDED",
            "STEP_STARTED",
            "STEP_FAILED",
            "STEP_SUCCEEDED",
            "ACTIVITY_SCHEDULED",
            "ACTIVITY_STARTED",
            "ACTIVITY_FAILED",
            "ACTIVITY_SUCCEEDED",
            "START_FLOW_EXECUTION_TASK",
            "SCHEDULE_NEXT_READY_STEPS_TASK",
            "THING_ACTION_TASK",
            "THING_ACTION_TASK_FAILED",
            "THING_ACTION_TASK_SUCCEEDED",
            "ACKNOWLEDGE_TASK_MESSAGE",
        ],
        "timestamp": datetime,
        "payload": str,
    },
    total=False,
)

ClientListFlowExecutionMessagesResponseTypeDef = TypedDict(
    "ClientListFlowExecutionMessagesResponseTypeDef",
    {"messages": List[ClientListFlowExecutionMessagesResponsemessagesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef], "nextToken": str},
    total=False,
)

ClientSearchEntitiesFiltersTypeDef = TypedDict(
    "ClientSearchEntitiesFiltersTypeDef",
    {
        "name": Literal["NAME", "NAMESPACE", "SEMANTIC_TYPE_PATH", "REFERENCED_ENTITY_ID"],
        "value": List[str],
    },
    total=False,
)

ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef = TypedDict(
    "ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)

ClientSearchEntitiesResponsedescriptionsTypeDef = TypedDict(
    "ClientSearchEntitiesResponsedescriptionsTypeDef",
    {
        "id": str,
        "arn": str,
        "type": Literal[
            "DEVICE",
            "SERVICE",
            "DEVICE_MODEL",
            "CAPABILITY",
            "STATE",
            "ACTION",
            "EVENT",
            "PROPERTY",
            "MAPPING",
            "ENUM",
        ],
        "createdAt": datetime,
        "definition": ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef,
    },
    total=False,
)

ClientSearchEntitiesResponseTypeDef = TypedDict(
    "ClientSearchEntitiesResponseTypeDef",
    {"descriptions": List[ClientSearchEntitiesResponsedescriptionsTypeDef], "nextToken": str},
    total=False,
)

ClientSearchFlowExecutionsResponsesummariesTypeDef = TypedDict(
    "ClientSearchFlowExecutionsResponsesummariesTypeDef",
    {
        "flowExecutionId": str,
        "status": Literal["RUNNING", "ABORTED", "SUCCEEDED", "FAILED"],
        "systemInstanceId": str,
        "flowTemplateId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)

ClientSearchFlowExecutionsResponseTypeDef = TypedDict(
    "ClientSearchFlowExecutionsResponseTypeDef",
    {"summaries": List[ClientSearchFlowExecutionsResponsesummariesTypeDef], "nextToken": str},
    total=False,
)

_RequiredClientSearchFlowTemplatesFiltersTypeDef = TypedDict(
    "_RequiredClientSearchFlowTemplatesFiltersTypeDef", {"name": str}
)
_OptionalClientSearchFlowTemplatesFiltersTypeDef = TypedDict(
    "_OptionalClientSearchFlowTemplatesFiltersTypeDef", {"value": List[str]}, total=False
)


class ClientSearchFlowTemplatesFiltersTypeDef(
    _RequiredClientSearchFlowTemplatesFiltersTypeDef,
    _OptionalClientSearchFlowTemplatesFiltersTypeDef,
):
    pass


ClientSearchFlowTemplatesResponsesummariesTypeDef = TypedDict(
    "ClientSearchFlowTemplatesResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

ClientSearchFlowTemplatesResponseTypeDef = TypedDict(
    "ClientSearchFlowTemplatesResponseTypeDef",
    {"summaries": List[ClientSearchFlowTemplatesResponsesummariesTypeDef], "nextToken": str},
    total=False,
)

ClientSearchSystemInstancesFiltersTypeDef = TypedDict(
    "ClientSearchSystemInstancesFiltersTypeDef",
    {"name": Literal["SYSTEM_TEMPLATE_ID", "STATUS", "GREENGRASS_GROUP_NAME"], "value": List[str]},
    total=False,
)

ClientSearchSystemInstancesResponsesummariesTypeDef = TypedDict(
    "ClientSearchSystemInstancesResponsesummariesTypeDef",
    {
        "id": str,
        "arn": str,
        "status": Literal[
            "NOT_DEPLOYED",
            "BOOTSTRAP",
            "DEPLOY_IN_PROGRESS",
            "DEPLOYED_IN_TARGET",
            "UNDEPLOY_IN_PROGRESS",
            "FAILED",
            "PENDING_DELETE",
            "DELETED_IN_TARGET",
        ],
        "target": Literal["GREENGRASS", "CLOUD"],
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)

ClientSearchSystemInstancesResponseTypeDef = TypedDict(
    "ClientSearchSystemInstancesResponseTypeDef",
    {"summaries": List[ClientSearchSystemInstancesResponsesummariesTypeDef], "nextToken": str},
    total=False,
)

_RequiredClientSearchSystemTemplatesFiltersTypeDef = TypedDict(
    "_RequiredClientSearchSystemTemplatesFiltersTypeDef", {"name": str}
)
_OptionalClientSearchSystemTemplatesFiltersTypeDef = TypedDict(
    "_OptionalClientSearchSystemTemplatesFiltersTypeDef", {"value": List[str]}, total=False
)


class ClientSearchSystemTemplatesFiltersTypeDef(
    _RequiredClientSearchSystemTemplatesFiltersTypeDef,
    _OptionalClientSearchSystemTemplatesFiltersTypeDef,
):
    pass


ClientSearchSystemTemplatesResponsesummariesTypeDef = TypedDict(
    "ClientSearchSystemTemplatesResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

ClientSearchSystemTemplatesResponseTypeDef = TypedDict(
    "ClientSearchSystemTemplatesResponseTypeDef",
    {"summaries": List[ClientSearchSystemTemplatesResponsesummariesTypeDef], "nextToken": str},
    total=False,
)

ClientSearchThingsResponsethingsTypeDef = TypedDict(
    "ClientSearchThingsResponsethingsTypeDef", {"thingArn": str, "thingName": str}, total=False
)

ClientSearchThingsResponseTypeDef = TypedDict(
    "ClientSearchThingsResponseTypeDef",
    {"things": List[ClientSearchThingsResponsethingsTypeDef], "nextToken": str},
    total=False,
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUndeploySystemInstanceResponsesummaryTypeDef = TypedDict(
    "ClientUndeploySystemInstanceResponsesummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": Literal[
            "NOT_DEPLOYED",
            "BOOTSTRAP",
            "DEPLOY_IN_PROGRESS",
            "DEPLOYED_IN_TARGET",
            "UNDEPLOY_IN_PROGRESS",
            "FAILED",
            "PENDING_DELETE",
            "DELETED_IN_TARGET",
        ],
        "target": Literal["GREENGRASS", "CLOUD"],
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)

ClientUndeploySystemInstanceResponseTypeDef = TypedDict(
    "ClientUndeploySystemInstanceResponseTypeDef",
    {"summary": ClientUndeploySystemInstanceResponsesummaryTypeDef},
    total=False,
)

_RequiredClientUpdateFlowTemplateDefinitionTypeDef = TypedDict(
    "_RequiredClientUpdateFlowTemplateDefinitionTypeDef", {"language": str}
)
_OptionalClientUpdateFlowTemplateDefinitionTypeDef = TypedDict(
    "_OptionalClientUpdateFlowTemplateDefinitionTypeDef", {"text": str}, total=False
)


class ClientUpdateFlowTemplateDefinitionTypeDef(
    _RequiredClientUpdateFlowTemplateDefinitionTypeDef,
    _OptionalClientUpdateFlowTemplateDefinitionTypeDef,
):
    pass


ClientUpdateFlowTemplateResponsesummaryTypeDef = TypedDict(
    "ClientUpdateFlowTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

ClientUpdateFlowTemplateResponseTypeDef = TypedDict(
    "ClientUpdateFlowTemplateResponseTypeDef",
    {"summary": ClientUpdateFlowTemplateResponsesummaryTypeDef},
    total=False,
)

_RequiredClientUpdateSystemTemplateDefinitionTypeDef = TypedDict(
    "_RequiredClientUpdateSystemTemplateDefinitionTypeDef", {"language": str}
)
_OptionalClientUpdateSystemTemplateDefinitionTypeDef = TypedDict(
    "_OptionalClientUpdateSystemTemplateDefinitionTypeDef", {"text": str}, total=False
)


class ClientUpdateSystemTemplateDefinitionTypeDef(
    _RequiredClientUpdateSystemTemplateDefinitionTypeDef,
    _OptionalClientUpdateSystemTemplateDefinitionTypeDef,
):
    pass


ClientUpdateSystemTemplateResponsesummaryTypeDef = TypedDict(
    "ClientUpdateSystemTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

ClientUpdateSystemTemplateResponseTypeDef = TypedDict(
    "ClientUpdateSystemTemplateResponseTypeDef",
    {"summary": ClientUpdateSystemTemplateResponsesummaryTypeDef},
    total=False,
)

_RequiredClientUploadEntityDefinitionsDocumentTypeDef = TypedDict(
    "_RequiredClientUploadEntityDefinitionsDocumentTypeDef", {"language": str}
)
_OptionalClientUploadEntityDefinitionsDocumentTypeDef = TypedDict(
    "_OptionalClientUploadEntityDefinitionsDocumentTypeDef", {"text": str}, total=False
)


class ClientUploadEntityDefinitionsDocumentTypeDef(
    _RequiredClientUploadEntityDefinitionsDocumentTypeDef,
    _OptionalClientUploadEntityDefinitionsDocumentTypeDef,
):
    pass


ClientUploadEntityDefinitionsResponseTypeDef = TypedDict(
    "ClientUploadEntityDefinitionsResponseTypeDef", {"uploadId": str}, total=False
)

GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef = TypedDict(
    "GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

GetFlowTemplateRevisionsPaginateResponseTypeDef = TypedDict(
    "GetFlowTemplateRevisionsPaginateResponseTypeDef",
    {"summaries": List[GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef], "NextToken": str},
    total=False,
)

GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef = TypedDict(
    "GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

GetSystemTemplateRevisionsPaginateResponseTypeDef = TypedDict(
    "GetSystemTemplateRevisionsPaginateResponseTypeDef",
    {
        "summaries": List[GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListFlowExecutionMessagesPaginatePaginationConfigTypeDef = TypedDict(
    "ListFlowExecutionMessagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListFlowExecutionMessagesPaginateResponsemessagesTypeDef = TypedDict(
    "ListFlowExecutionMessagesPaginateResponsemessagesTypeDef",
    {
        "messageId": str,
        "eventType": Literal[
            "EXECUTION_STARTED",
            "EXECUTION_FAILED",
            "EXECUTION_ABORTED",
            "EXECUTION_SUCCEEDED",
            "STEP_STARTED",
            "STEP_FAILED",
            "STEP_SUCCEEDED",
            "ACTIVITY_SCHEDULED",
            "ACTIVITY_STARTED",
            "ACTIVITY_FAILED",
            "ACTIVITY_SUCCEEDED",
            "START_FLOW_EXECUTION_TASK",
            "SCHEDULE_NEXT_READY_STEPS_TASK",
            "THING_ACTION_TASK",
            "THING_ACTION_TASK_FAILED",
            "THING_ACTION_TASK_SUCCEEDED",
            "ACKNOWLEDGE_TASK_MESSAGE",
        ],
        "timestamp": datetime,
        "payload": str,
    },
    total=False,
)

ListFlowExecutionMessagesPaginateResponseTypeDef = TypedDict(
    "ListFlowExecutionMessagesPaginateResponseTypeDef",
    {"messages": List[ListFlowExecutionMessagesPaginateResponsemessagesTypeDef], "NextToken": str},
    total=False,
)

ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "ListTagsForResourcePaginateResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)

SearchEntitiesPaginateFiltersTypeDef = TypedDict(
    "SearchEntitiesPaginateFiltersTypeDef",
    {
        "name": Literal["NAME", "NAMESPACE", "SEMANTIC_TYPE_PATH", "REFERENCED_ENTITY_ID"],
        "value": List[str],
    },
    total=False,
)

SearchEntitiesPaginatePaginationConfigTypeDef = TypedDict(
    "SearchEntitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef = TypedDict(
    "SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)

SearchEntitiesPaginateResponsedescriptionsTypeDef = TypedDict(
    "SearchEntitiesPaginateResponsedescriptionsTypeDef",
    {
        "id": str,
        "arn": str,
        "type": Literal[
            "DEVICE",
            "SERVICE",
            "DEVICE_MODEL",
            "CAPABILITY",
            "STATE",
            "ACTION",
            "EVENT",
            "PROPERTY",
            "MAPPING",
            "ENUM",
        ],
        "createdAt": datetime,
        "definition": SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef,
    },
    total=False,
)

SearchEntitiesPaginateResponseTypeDef = TypedDict(
    "SearchEntitiesPaginateResponseTypeDef",
    {"descriptions": List[SearchEntitiesPaginateResponsedescriptionsTypeDef], "NextToken": str},
    total=False,
)

SearchFlowExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "SearchFlowExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

SearchFlowExecutionsPaginateResponsesummariesTypeDef = TypedDict(
    "SearchFlowExecutionsPaginateResponsesummariesTypeDef",
    {
        "flowExecutionId": str,
        "status": Literal["RUNNING", "ABORTED", "SUCCEEDED", "FAILED"],
        "systemInstanceId": str,
        "flowTemplateId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)

SearchFlowExecutionsPaginateResponseTypeDef = TypedDict(
    "SearchFlowExecutionsPaginateResponseTypeDef",
    {"summaries": List[SearchFlowExecutionsPaginateResponsesummariesTypeDef], "NextToken": str},
    total=False,
)

_RequiredSearchFlowTemplatesPaginateFiltersTypeDef = TypedDict(
    "_RequiredSearchFlowTemplatesPaginateFiltersTypeDef", {"name": str}
)
_OptionalSearchFlowTemplatesPaginateFiltersTypeDef = TypedDict(
    "_OptionalSearchFlowTemplatesPaginateFiltersTypeDef", {"value": List[str]}, total=False
)


class SearchFlowTemplatesPaginateFiltersTypeDef(
    _RequiredSearchFlowTemplatesPaginateFiltersTypeDef,
    _OptionalSearchFlowTemplatesPaginateFiltersTypeDef,
):
    pass


SearchFlowTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "SearchFlowTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

SearchFlowTemplatesPaginateResponsesummariesTypeDef = TypedDict(
    "SearchFlowTemplatesPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

SearchFlowTemplatesPaginateResponseTypeDef = TypedDict(
    "SearchFlowTemplatesPaginateResponseTypeDef",
    {"summaries": List[SearchFlowTemplatesPaginateResponsesummariesTypeDef], "NextToken": str},
    total=False,
)

SearchSystemInstancesPaginateFiltersTypeDef = TypedDict(
    "SearchSystemInstancesPaginateFiltersTypeDef",
    {"name": Literal["SYSTEM_TEMPLATE_ID", "STATUS", "GREENGRASS_GROUP_NAME"], "value": List[str]},
    total=False,
)

SearchSystemInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "SearchSystemInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

SearchSystemInstancesPaginateResponsesummariesTypeDef = TypedDict(
    "SearchSystemInstancesPaginateResponsesummariesTypeDef",
    {
        "id": str,
        "arn": str,
        "status": Literal[
            "NOT_DEPLOYED",
            "BOOTSTRAP",
            "DEPLOY_IN_PROGRESS",
            "DEPLOYED_IN_TARGET",
            "UNDEPLOY_IN_PROGRESS",
            "FAILED",
            "PENDING_DELETE",
            "DELETED_IN_TARGET",
        ],
        "target": Literal["GREENGRASS", "CLOUD"],
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)

SearchSystemInstancesPaginateResponseTypeDef = TypedDict(
    "SearchSystemInstancesPaginateResponseTypeDef",
    {"summaries": List[SearchSystemInstancesPaginateResponsesummariesTypeDef], "NextToken": str},
    total=False,
)

_RequiredSearchSystemTemplatesPaginateFiltersTypeDef = TypedDict(
    "_RequiredSearchSystemTemplatesPaginateFiltersTypeDef", {"name": str}
)
_OptionalSearchSystemTemplatesPaginateFiltersTypeDef = TypedDict(
    "_OptionalSearchSystemTemplatesPaginateFiltersTypeDef", {"value": List[str]}, total=False
)


class SearchSystemTemplatesPaginateFiltersTypeDef(
    _RequiredSearchSystemTemplatesPaginateFiltersTypeDef,
    _OptionalSearchSystemTemplatesPaginateFiltersTypeDef,
):
    pass


SearchSystemTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "SearchSystemTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

SearchSystemTemplatesPaginateResponsesummariesTypeDef = TypedDict(
    "SearchSystemTemplatesPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

SearchSystemTemplatesPaginateResponseTypeDef = TypedDict(
    "SearchSystemTemplatesPaginateResponseTypeDef",
    {"summaries": List[SearchSystemTemplatesPaginateResponsesummariesTypeDef], "NextToken": str},
    total=False,
)

SearchThingsPaginatePaginationConfigTypeDef = TypedDict(
    "SearchThingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

SearchThingsPaginateResponsethingsTypeDef = TypedDict(
    "SearchThingsPaginateResponsethingsTypeDef", {"thingArn": str, "thingName": str}, total=False
)

SearchThingsPaginateResponseTypeDef = TypedDict(
    "SearchThingsPaginateResponseTypeDef",
    {"things": List[SearchThingsPaginateResponsethingsTypeDef], "NextToken": str},
    total=False,
)
