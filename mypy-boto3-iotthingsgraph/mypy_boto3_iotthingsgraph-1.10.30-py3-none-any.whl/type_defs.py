"Main interface for iotthingsgraph service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateFlowTemplateDefinitionTypeDef",
    "ClientCreateFlowTemplateResponsesummaryTypeDef",
    "ClientCreateFlowTemplateResponseTypeDef",
    "ClientCreateSystemInstanceDefinitionTypeDef",
    "ClientCreateSystemInstanceMetricsConfigurationTypeDef",
    "ClientCreateSystemInstanceResponsesummaryTypeDef",
    "ClientCreateSystemInstanceResponseTypeDef",
    "ClientCreateSystemInstanceTagsTypeDef",
    "ClientCreateSystemTemplateDefinitionTypeDef",
    "ClientCreateSystemTemplateResponsesummaryTypeDef",
    "ClientCreateSystemTemplateResponseTypeDef",
    "ClientDeleteNamespaceResponseTypeDef",
    "ClientDeploySystemInstanceResponsesummaryTypeDef",
    "ClientDeploySystemInstanceResponseTypeDef",
    "ClientDescribeNamespaceResponseTypeDef",
    "ClientGetEntitiesResponsedescriptionsdefinitionTypeDef",
    "ClientGetEntitiesResponsedescriptionsTypeDef",
    "ClientGetEntitiesResponseTypeDef",
    "ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef",
    "ClientGetFlowTemplateResponsedescriptionsummaryTypeDef",
    "ClientGetFlowTemplateResponsedescriptionTypeDef",
    "ClientGetFlowTemplateResponseTypeDef",
    "ClientGetFlowTemplateRevisionsResponsesummariesTypeDef",
    "ClientGetFlowTemplateRevisionsResponseTypeDef",
    "ClientGetNamespaceDeletionStatusResponseTypeDef",
    "ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef",
    "ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef",
    "ClientGetSystemInstanceResponsedescriptionsummaryTypeDef",
    "ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef",
    "ClientGetSystemInstanceResponsedescriptionTypeDef",
    "ClientGetSystemInstanceResponseTypeDef",
    "ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef",
    "ClientGetSystemTemplateResponsedescriptionsummaryTypeDef",
    "ClientGetSystemTemplateResponsedescriptionTypeDef",
    "ClientGetSystemTemplateResponseTypeDef",
    "ClientGetSystemTemplateRevisionsResponsesummariesTypeDef",
    "ClientGetSystemTemplateRevisionsResponseTypeDef",
    "ClientGetUploadStatusResponseTypeDef",
    "ClientListFlowExecutionMessagesResponsemessagesTypeDef",
    "ClientListFlowExecutionMessagesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientSearchEntitiesFiltersTypeDef",
    "ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef",
    "ClientSearchEntitiesResponsedescriptionsTypeDef",
    "ClientSearchEntitiesResponseTypeDef",
    "ClientSearchFlowExecutionsResponsesummariesTypeDef",
    "ClientSearchFlowExecutionsResponseTypeDef",
    "ClientSearchFlowTemplatesFiltersTypeDef",
    "ClientSearchFlowTemplatesResponsesummariesTypeDef",
    "ClientSearchFlowTemplatesResponseTypeDef",
    "ClientSearchSystemInstancesFiltersTypeDef",
    "ClientSearchSystemInstancesResponsesummariesTypeDef",
    "ClientSearchSystemInstancesResponseTypeDef",
    "ClientSearchSystemTemplatesFiltersTypeDef",
    "ClientSearchSystemTemplatesResponsesummariesTypeDef",
    "ClientSearchSystemTemplatesResponseTypeDef",
    "ClientSearchThingsResponsethingsTypeDef",
    "ClientSearchThingsResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUndeploySystemInstanceResponsesummaryTypeDef",
    "ClientUndeploySystemInstanceResponseTypeDef",
    "ClientUpdateFlowTemplateDefinitionTypeDef",
    "ClientUpdateFlowTemplateResponsesummaryTypeDef",
    "ClientUpdateFlowTemplateResponseTypeDef",
    "ClientUpdateSystemTemplateDefinitionTypeDef",
    "ClientUpdateSystemTemplateResponsesummaryTypeDef",
    "ClientUpdateSystemTemplateResponseTypeDef",
    "ClientUploadEntityDefinitionsDocumentTypeDef",
    "ClientUploadEntityDefinitionsResponseTypeDef",
    "GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef",
    "GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef",
    "GetFlowTemplateRevisionsPaginateResponseTypeDef",
    "GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef",
    "GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef",
    "GetSystemTemplateRevisionsPaginateResponseTypeDef",
    "ListFlowExecutionMessagesPaginatePaginationConfigTypeDef",
    "ListFlowExecutionMessagesPaginateResponsemessagesTypeDef",
    "ListFlowExecutionMessagesPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponsetagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "SearchEntitiesPaginateFiltersTypeDef",
    "SearchEntitiesPaginatePaginationConfigTypeDef",
    "SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef",
    "SearchEntitiesPaginateResponsedescriptionsTypeDef",
    "SearchEntitiesPaginateResponseTypeDef",
    "SearchFlowExecutionsPaginatePaginationConfigTypeDef",
    "SearchFlowExecutionsPaginateResponsesummariesTypeDef",
    "SearchFlowExecutionsPaginateResponseTypeDef",
    "SearchFlowTemplatesPaginateFiltersTypeDef",
    "SearchFlowTemplatesPaginatePaginationConfigTypeDef",
    "SearchFlowTemplatesPaginateResponsesummariesTypeDef",
    "SearchFlowTemplatesPaginateResponseTypeDef",
    "SearchSystemInstancesPaginateFiltersTypeDef",
    "SearchSystemInstancesPaginatePaginationConfigTypeDef",
    "SearchSystemInstancesPaginateResponsesummariesTypeDef",
    "SearchSystemInstancesPaginateResponseTypeDef",
    "SearchSystemTemplatesPaginateFiltersTypeDef",
    "SearchSystemTemplatesPaginatePaginationConfigTypeDef",
    "SearchSystemTemplatesPaginateResponsesummariesTypeDef",
    "SearchSystemTemplatesPaginateResponseTypeDef",
    "SearchThingsPaginatePaginationConfigTypeDef",
    "SearchThingsPaginateResponsethingsTypeDef",
    "SearchThingsPaginateResponseTypeDef",
)


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
    """
    The workflow ``DefinitionDocument`` .
    - **language** *(string) --***[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.
    """


_ClientCreateFlowTemplateResponsesummaryTypeDef = TypedDict(
    "_ClientCreateFlowTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientCreateFlowTemplateResponsesummaryTypeDef(
    _ClientCreateFlowTemplateResponsesummaryTypeDef
):
    """
    - **summary** *(dict) --*

      The summary object that describes the created workflow.
      - **id** *(string) --*

        The ID of the workflow.
    """


_ClientCreateFlowTemplateResponseTypeDef = TypedDict(
    "_ClientCreateFlowTemplateResponseTypeDef",
    {"summary": ClientCreateFlowTemplateResponsesummaryTypeDef},
    total=False,
)


class ClientCreateFlowTemplateResponseTypeDef(_ClientCreateFlowTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **summary** *(dict) --*

        The summary object that describes the created workflow.
        - **id** *(string) --*

          The ID of the workflow.
    """


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
    """
    A document that defines an entity.
    - **language** *(string) --***[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.
    """


_ClientCreateSystemInstanceMetricsConfigurationTypeDef = TypedDict(
    "_ClientCreateSystemInstanceMetricsConfigurationTypeDef",
    {"cloudMetricEnabled": bool, "metricRuleRoleArn": str},
    total=False,
)


class ClientCreateSystemInstanceMetricsConfigurationTypeDef(
    _ClientCreateSystemInstanceMetricsConfigurationTypeDef
):
    """
    An object that specifies whether cloud metrics are collected in a deployment and, if so, what
    role is used to collect metrics.
    - **cloudMetricEnabled** *(boolean) --*

      A Boolean that specifies whether cloud metrics are collected.
    """


_ClientCreateSystemInstanceResponsesummaryTypeDef = TypedDict(
    "_ClientCreateSystemInstanceResponsesummaryTypeDef",
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


class ClientCreateSystemInstanceResponsesummaryTypeDef(
    _ClientCreateSystemInstanceResponsesummaryTypeDef
):
    """
    - **summary** *(dict) --*

      The summary object that describes the new system instance.
      - **id** *(string) --*

        The ID of the system instance.
    """


_ClientCreateSystemInstanceResponseTypeDef = TypedDict(
    "_ClientCreateSystemInstanceResponseTypeDef",
    {"summary": ClientCreateSystemInstanceResponsesummaryTypeDef},
    total=False,
)


class ClientCreateSystemInstanceResponseTypeDef(_ClientCreateSystemInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **summary** *(dict) --*

        The summary object that describes the new system instance.
        - **id** *(string) --*

          The ID of the system instance.
    """


_RequiredClientCreateSystemInstanceTagsTypeDef = TypedDict(
    "_RequiredClientCreateSystemInstanceTagsTypeDef", {"key": str}
)
_OptionalClientCreateSystemInstanceTagsTypeDef = TypedDict(
    "_OptionalClientCreateSystemInstanceTagsTypeDef", {"value": str}, total=False
)


class ClientCreateSystemInstanceTagsTypeDef(
    _RequiredClientCreateSystemInstanceTagsTypeDef, _OptionalClientCreateSystemInstanceTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.
      - **key** *(string) --***[REQUIRED]**

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length.
    """


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
    """
    The ``DefinitionDocument`` used to create the system.
    - **language** *(string) --***[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.
    """


_ClientCreateSystemTemplateResponsesummaryTypeDef = TypedDict(
    "_ClientCreateSystemTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientCreateSystemTemplateResponsesummaryTypeDef(
    _ClientCreateSystemTemplateResponsesummaryTypeDef
):
    """
    - **summary** *(dict) --*

      The summary object that describes the created system.
      - **id** *(string) --*

        The ID of the system.
    """


_ClientCreateSystemTemplateResponseTypeDef = TypedDict(
    "_ClientCreateSystemTemplateResponseTypeDef",
    {"summary": ClientCreateSystemTemplateResponsesummaryTypeDef},
    total=False,
)


class ClientCreateSystemTemplateResponseTypeDef(_ClientCreateSystemTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **summary** *(dict) --*

        The summary object that describes the created system.
        - **id** *(string) --*

          The ID of the system.
    """


_ClientDeleteNamespaceResponseTypeDef = TypedDict(
    "_ClientDeleteNamespaceResponseTypeDef",
    {"namespaceArn": str, "namespaceName": str},
    total=False,
)


class ClientDeleteNamespaceResponseTypeDef(_ClientDeleteNamespaceResponseTypeDef):
    """
    - *(dict) --*

      - **namespaceArn** *(string) --*

        The ARN of the namespace to be deleted.
    """


_ClientDeploySystemInstanceResponsesummaryTypeDef = TypedDict(
    "_ClientDeploySystemInstanceResponsesummaryTypeDef",
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


class ClientDeploySystemInstanceResponsesummaryTypeDef(
    _ClientDeploySystemInstanceResponsesummaryTypeDef
):
    """
    - **summary** *(dict) --*

      An object that contains summary information about a system instance that was deployed.
      - **id** *(string) --*

        The ID of the system instance.
    """


_ClientDeploySystemInstanceResponseTypeDef = TypedDict(
    "_ClientDeploySystemInstanceResponseTypeDef",
    {"summary": ClientDeploySystemInstanceResponsesummaryTypeDef, "greengrassDeploymentId": str},
    total=False,
)


class ClientDeploySystemInstanceResponseTypeDef(_ClientDeploySystemInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **summary** *(dict) --*

        An object that contains summary information about a system instance that was deployed.
        - **id** *(string) --*

          The ID of the system instance.
    """


_ClientDescribeNamespaceResponseTypeDef = TypedDict(
    "_ClientDescribeNamespaceResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "trackingNamespaceName": str,
        "trackingNamespaceVersion": int,
        "namespaceVersion": int,
    },
    total=False,
)


class ClientDescribeNamespaceResponseTypeDef(_ClientDescribeNamespaceResponseTypeDef):
    """
    - *(dict) --*

      - **namespaceArn** *(string) --*

        The ARN of the namespace.
    """


_ClientGetEntitiesResponsedescriptionsdefinitionTypeDef = TypedDict(
    "_ClientGetEntitiesResponsedescriptionsdefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class ClientGetEntitiesResponsedescriptionsdefinitionTypeDef(
    _ClientGetEntitiesResponsedescriptionsdefinitionTypeDef
):
    pass


_ClientGetEntitiesResponsedescriptionsTypeDef = TypedDict(
    "_ClientGetEntitiesResponsedescriptionsTypeDef",
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


class ClientGetEntitiesResponsedescriptionsTypeDef(_ClientGetEntitiesResponsedescriptionsTypeDef):
    """
    - *(dict) --*

      Describes the properties of an entity.
      - **id** *(string) --*

        The entity ID.
    """


_ClientGetEntitiesResponseTypeDef = TypedDict(
    "_ClientGetEntitiesResponseTypeDef",
    {"descriptions": List[ClientGetEntitiesResponsedescriptionsTypeDef]},
    total=False,
)


class ClientGetEntitiesResponseTypeDef(_ClientGetEntitiesResponseTypeDef):
    """
    - *(dict) --*

      - **descriptions** *(list) --*

        An array of descriptions for the specified entities.
        - *(dict) --*

          Describes the properties of an entity.
          - **id** *(string) --*

            The entity ID.
    """


_ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef = TypedDict(
    "_ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef(
    _ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef
):
    pass


_ClientGetFlowTemplateResponsedescriptionsummaryTypeDef = TypedDict(
    "_ClientGetFlowTemplateResponsedescriptionsummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientGetFlowTemplateResponsedescriptionsummaryTypeDef(
    _ClientGetFlowTemplateResponsedescriptionsummaryTypeDef
):
    """
    - **summary** *(dict) --*

      An object that contains summary information about a workflow.
      - **id** *(string) --*

        The ID of the workflow.
    """


_ClientGetFlowTemplateResponsedescriptionTypeDef = TypedDict(
    "_ClientGetFlowTemplateResponsedescriptionTypeDef",
    {
        "summary": ClientGetFlowTemplateResponsedescriptionsummaryTypeDef,
        "definition": ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef,
        "validatedNamespaceVersion": int,
    },
    total=False,
)


class ClientGetFlowTemplateResponsedescriptionTypeDef(
    _ClientGetFlowTemplateResponsedescriptionTypeDef
):
    """
    - **description** *(dict) --*

      The object that describes the specified workflow.
      - **summary** *(dict) --*

        An object that contains summary information about a workflow.
        - **id** *(string) --*

          The ID of the workflow.
    """


_ClientGetFlowTemplateResponseTypeDef = TypedDict(
    "_ClientGetFlowTemplateResponseTypeDef",
    {"description": ClientGetFlowTemplateResponsedescriptionTypeDef},
    total=False,
)


class ClientGetFlowTemplateResponseTypeDef(_ClientGetFlowTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **description** *(dict) --*

        The object that describes the specified workflow.
        - **summary** *(dict) --*

          An object that contains summary information about a workflow.
          - **id** *(string) --*

            The ID of the workflow.
    """


_ClientGetFlowTemplateRevisionsResponsesummariesTypeDef = TypedDict(
    "_ClientGetFlowTemplateRevisionsResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientGetFlowTemplateRevisionsResponsesummariesTypeDef(
    _ClientGetFlowTemplateRevisionsResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains summary information about a workflow.
      - **id** *(string) --*

        The ID of the workflow.
    """


_ClientGetFlowTemplateRevisionsResponseTypeDef = TypedDict(
    "_ClientGetFlowTemplateRevisionsResponseTypeDef",
    {"summaries": List[ClientGetFlowTemplateRevisionsResponsesummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientGetFlowTemplateRevisionsResponseTypeDef(_ClientGetFlowTemplateRevisionsResponseTypeDef):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that provide summary data about each revision.
        - *(dict) --*

          An object that contains summary information about a workflow.
          - **id** *(string) --*

            The ID of the workflow.
    """


_ClientGetNamespaceDeletionStatusResponseTypeDef = TypedDict(
    "_ClientGetNamespaceDeletionStatusResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)


class ClientGetNamespaceDeletionStatusResponseTypeDef(
    _ClientGetNamespaceDeletionStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **namespaceArn** *(string) --*

        The ARN of the namespace that is being deleted.
    """


_ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef(
    _ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef
):
    pass


_ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef",
    {"cloudMetricEnabled": bool, "metricRuleRoleArn": str},
    total=False,
)


class ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef(
    _ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef
):
    pass


_ClientGetSystemInstanceResponsedescriptionsummaryTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponsedescriptionsummaryTypeDef",
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


class ClientGetSystemInstanceResponsedescriptionsummaryTypeDef(
    _ClientGetSystemInstanceResponsedescriptionsummaryTypeDef
):
    """
    - **summary** *(dict) --*

      An object that contains summary information about a system instance.
      - **id** *(string) --*

        The ID of the system instance.
    """


_ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef",
    {"id": str, "revisionNumber": int},
    total=False,
)


class ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef(
    _ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef
):
    pass


_ClientGetSystemInstanceResponsedescriptionTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponsedescriptionTypeDef",
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


class ClientGetSystemInstanceResponsedescriptionTypeDef(
    _ClientGetSystemInstanceResponsedescriptionTypeDef
):
    """
    - **description** *(dict) --*

      An object that describes the system instance.
      - **summary** *(dict) --*

        An object that contains summary information about a system instance.
        - **id** *(string) --*

          The ID of the system instance.
    """


_ClientGetSystemInstanceResponseTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponseTypeDef",
    {"description": ClientGetSystemInstanceResponsedescriptionTypeDef},
    total=False,
)


class ClientGetSystemInstanceResponseTypeDef(_ClientGetSystemInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **description** *(dict) --*

        An object that describes the system instance.
        - **summary** *(dict) --*

          An object that contains summary information about a system instance.
          - **id** *(string) --*

            The ID of the system instance.
    """


_ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef = TypedDict(
    "_ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef(
    _ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef
):
    pass


_ClientGetSystemTemplateResponsedescriptionsummaryTypeDef = TypedDict(
    "_ClientGetSystemTemplateResponsedescriptionsummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientGetSystemTemplateResponsedescriptionsummaryTypeDef(
    _ClientGetSystemTemplateResponsedescriptionsummaryTypeDef
):
    """
    - **summary** *(dict) --*

      An object that contains summary information about a system.
      - **id** *(string) --*

        The ID of the system.
    """


_ClientGetSystemTemplateResponsedescriptionTypeDef = TypedDict(
    "_ClientGetSystemTemplateResponsedescriptionTypeDef",
    {
        "summary": ClientGetSystemTemplateResponsedescriptionsummaryTypeDef,
        "definition": ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef,
        "validatedNamespaceVersion": int,
    },
    total=False,
)


class ClientGetSystemTemplateResponsedescriptionTypeDef(
    _ClientGetSystemTemplateResponsedescriptionTypeDef
):
    """
    - **description** *(dict) --*

      An object that contains summary data about the system.
      - **summary** *(dict) --*

        An object that contains summary information about a system.
        - **id** *(string) --*

          The ID of the system.
    """


_ClientGetSystemTemplateResponseTypeDef = TypedDict(
    "_ClientGetSystemTemplateResponseTypeDef",
    {"description": ClientGetSystemTemplateResponsedescriptionTypeDef},
    total=False,
)


class ClientGetSystemTemplateResponseTypeDef(_ClientGetSystemTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **description** *(dict) --*

        An object that contains summary data about the system.
        - **summary** *(dict) --*

          An object that contains summary information about a system.
          - **id** *(string) --*

            The ID of the system.
    """


_ClientGetSystemTemplateRevisionsResponsesummariesTypeDef = TypedDict(
    "_ClientGetSystemTemplateRevisionsResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientGetSystemTemplateRevisionsResponsesummariesTypeDef(
    _ClientGetSystemTemplateRevisionsResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains information about a system.
      - **id** *(string) --*

        The ID of the system.
    """


_ClientGetSystemTemplateRevisionsResponseTypeDef = TypedDict(
    "_ClientGetSystemTemplateRevisionsResponseTypeDef",
    {"summaries": List[ClientGetSystemTemplateRevisionsResponsesummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientGetSystemTemplateRevisionsResponseTypeDef(
    _ClientGetSystemTemplateRevisionsResponseTypeDef
):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that contain summary data about the system template revisions.
        - *(dict) --*

          An object that contains information about a system.
          - **id** *(string) --*

            The ID of the system.
    """


_ClientGetUploadStatusResponseTypeDef = TypedDict(
    "_ClientGetUploadStatusResponseTypeDef",
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


class ClientGetUploadStatusResponseTypeDef(_ClientGetUploadStatusResponseTypeDef):
    """
    - *(dict) --*

      - **uploadId** *(string) --*

        The ID of the upload.
    """


_ClientListFlowExecutionMessagesResponsemessagesTypeDef = TypedDict(
    "_ClientListFlowExecutionMessagesResponsemessagesTypeDef",
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


class ClientListFlowExecutionMessagesResponsemessagesTypeDef(
    _ClientListFlowExecutionMessagesResponsemessagesTypeDef
):
    """
    - *(dict) --*

      An object that contains information about a flow event.
      - **messageId** *(string) --*

        The unique identifier of the message.
    """


_ClientListFlowExecutionMessagesResponseTypeDef = TypedDict(
    "_ClientListFlowExecutionMessagesResponseTypeDef",
    {"messages": List[ClientListFlowExecutionMessagesResponsemessagesTypeDef], "nextToken": str},
    total=False,
)


class ClientListFlowExecutionMessagesResponseTypeDef(
    _ClientListFlowExecutionMessagesResponseTypeDef
):
    """
    - *(dict) --*

      - **messages** *(list) --*

        A list of objects that contain information about events in the specified flow execution.
        - *(dict) --*

          An object that contains information about a flow event.
          - **messageId** *(string) --*

            The unique identifier of the message.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientListTagsForResourceResponsetagsTypeDef(_ClientListTagsForResourceResponsetagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.
      - **key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef], "nextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        List of tags returned by the ``ListTagsForResource`` operation.
        - *(dict) --*

          Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.
          - **key** *(string) --*

            The required name of the tag. The string value can be from 1 to 128 Unicode characters
            in length.
    """


_ClientSearchEntitiesFiltersTypeDef = TypedDict(
    "_ClientSearchEntitiesFiltersTypeDef",
    {
        "name": Literal["NAME", "NAMESPACE", "SEMANTIC_TYPE_PATH", "REFERENCED_ENTITY_ID"],
        "value": List[str],
    },
    total=False,
)


class ClientSearchEntitiesFiltersTypeDef(_ClientSearchEntitiesFiltersTypeDef):
    """
    - *(dict) --*

      An object that filters an entity search. Multiple filters function as OR criteria in the
      search. For example a search that includes a ``NAMESPACE`` and a ``REFERENCED_ENTITY_ID``
      filter searches for entities in the specified namespace that use the entity specified by the
      value of ``REFERENCED_ENTITY_ID`` .
      - **name** *(string) --*

        The name of the entity search filter field. ``REFERENCED_ENTITY_ID`` filters on entities
        that are used by the entity in the result set. For example, you can filter on the ID of a
        property that is used in a state.
    """


_ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef = TypedDict(
    "_ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef(
    _ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef
):
    pass


_ClientSearchEntitiesResponsedescriptionsTypeDef = TypedDict(
    "_ClientSearchEntitiesResponsedescriptionsTypeDef",
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


class ClientSearchEntitiesResponsedescriptionsTypeDef(
    _ClientSearchEntitiesResponsedescriptionsTypeDef
):
    """
    - *(dict) --*

      Describes the properties of an entity.
      - **id** *(string) --*

        The entity ID.
    """


_ClientSearchEntitiesResponseTypeDef = TypedDict(
    "_ClientSearchEntitiesResponseTypeDef",
    {"descriptions": List[ClientSearchEntitiesResponsedescriptionsTypeDef], "nextToken": str},
    total=False,
)


class ClientSearchEntitiesResponseTypeDef(_ClientSearchEntitiesResponseTypeDef):
    """
    - *(dict) --*

      - **descriptions** *(list) --*

        An array of descriptions for each entity returned in the search result.
        - *(dict) --*

          Describes the properties of an entity.
          - **id** *(string) --*

            The entity ID.
    """


_ClientSearchFlowExecutionsResponsesummariesTypeDef = TypedDict(
    "_ClientSearchFlowExecutionsResponsesummariesTypeDef",
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


class ClientSearchFlowExecutionsResponsesummariesTypeDef(
    _ClientSearchFlowExecutionsResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains summary information about a flow execution.
      - **flowExecutionId** *(string) --*

        The ID of the flow execution.
    """


_ClientSearchFlowExecutionsResponseTypeDef = TypedDict(
    "_ClientSearchFlowExecutionsResponseTypeDef",
    {"summaries": List[ClientSearchFlowExecutionsResponsesummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientSearchFlowExecutionsResponseTypeDef(_ClientSearchFlowExecutionsResponseTypeDef):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that contain summary information about each workflow execution in the
        result set.
        - *(dict) --*

          An object that contains summary information about a flow execution.
          - **flowExecutionId** *(string) --*

            The ID of the flow execution.
    """


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
    """
    - *(dict) --*

      An object that filters a workflow search.
      - **name** *(string) --***[REQUIRED]**

        The name of the search filter field.
    """


_ClientSearchFlowTemplatesResponsesummariesTypeDef = TypedDict(
    "_ClientSearchFlowTemplatesResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientSearchFlowTemplatesResponsesummariesTypeDef(
    _ClientSearchFlowTemplatesResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains summary information about a workflow.
      - **id** *(string) --*

        The ID of the workflow.
    """


_ClientSearchFlowTemplatesResponseTypeDef = TypedDict(
    "_ClientSearchFlowTemplatesResponseTypeDef",
    {"summaries": List[ClientSearchFlowTemplatesResponsesummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientSearchFlowTemplatesResponseTypeDef(_ClientSearchFlowTemplatesResponseTypeDef):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that contain summary information about each workflow in the result set.
        - *(dict) --*

          An object that contains summary information about a workflow.
          - **id** *(string) --*

            The ID of the workflow.
    """


_ClientSearchSystemInstancesFiltersTypeDef = TypedDict(
    "_ClientSearchSystemInstancesFiltersTypeDef",
    {"name": Literal["SYSTEM_TEMPLATE_ID", "STATUS", "GREENGRASS_GROUP_NAME"], "value": List[str]},
    total=False,
)


class ClientSearchSystemInstancesFiltersTypeDef(_ClientSearchSystemInstancesFiltersTypeDef):
    """
    - *(dict) --*

      An object that filters a system instance search. Multiple filters function as OR criteria in
      the search. For example a search that includes a GREENGRASS_GROUP_NAME and a STATUS filter
      searches for system instances in the specified Greengrass group that have the specified
      status.
      - **name** *(string) --*

        The name of the search filter field.
    """


_ClientSearchSystemInstancesResponsesummariesTypeDef = TypedDict(
    "_ClientSearchSystemInstancesResponsesummariesTypeDef",
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


class ClientSearchSystemInstancesResponsesummariesTypeDef(
    _ClientSearchSystemInstancesResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains summary information about a system instance.
      - **id** *(string) --*

        The ID of the system instance.
    """


_ClientSearchSystemInstancesResponseTypeDef = TypedDict(
    "_ClientSearchSystemInstancesResponseTypeDef",
    {"summaries": List[ClientSearchSystemInstancesResponsesummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientSearchSystemInstancesResponseTypeDef(_ClientSearchSystemInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that contain summary data abour the system instances in the result set.
        - *(dict) --*

          An object that contains summary information about a system instance.
          - **id** *(string) --*

            The ID of the system instance.
    """


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
    """
    - *(dict) --*

      An object that filters a system search.
      - **name** *(string) --***[REQUIRED]**

        The name of the system search filter field.
    """


_ClientSearchSystemTemplatesResponsesummariesTypeDef = TypedDict(
    "_ClientSearchSystemTemplatesResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientSearchSystemTemplatesResponsesummariesTypeDef(
    _ClientSearchSystemTemplatesResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains information about a system.
      - **id** *(string) --*

        The ID of the system.
    """


_ClientSearchSystemTemplatesResponseTypeDef = TypedDict(
    "_ClientSearchSystemTemplatesResponseTypeDef",
    {"summaries": List[ClientSearchSystemTemplatesResponsesummariesTypeDef], "nextToken": str},
    total=False,
)


class ClientSearchSystemTemplatesResponseTypeDef(_ClientSearchSystemTemplatesResponseTypeDef):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that contain summary information about each system deployment in the
        result set.
        - *(dict) --*

          An object that contains information about a system.
          - **id** *(string) --*

            The ID of the system.
    """


_ClientSearchThingsResponsethingsTypeDef = TypedDict(
    "_ClientSearchThingsResponsethingsTypeDef", {"thingArn": str, "thingName": str}, total=False
)


class ClientSearchThingsResponsethingsTypeDef(_ClientSearchThingsResponsethingsTypeDef):
    """
    - *(dict) --*

      An AWS IoT thing.
      - **thingArn** *(string) --*

        The ARN of the thing.
    """


_ClientSearchThingsResponseTypeDef = TypedDict(
    "_ClientSearchThingsResponseTypeDef",
    {"things": List[ClientSearchThingsResponsethingsTypeDef], "nextToken": str},
    total=False,
)


class ClientSearchThingsResponseTypeDef(_ClientSearchThingsResponseTypeDef):
    """
    - *(dict) --*

      - **things** *(list) --*

        An array of things in the result set.
        - *(dict) --*

          An AWS IoT thing.
          - **thingArn** *(string) --*

            The ARN of the thing.
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

      Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.
      - **key** *(string) --***[REQUIRED]**

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length.
    """


_ClientUndeploySystemInstanceResponsesummaryTypeDef = TypedDict(
    "_ClientUndeploySystemInstanceResponsesummaryTypeDef",
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


class ClientUndeploySystemInstanceResponsesummaryTypeDef(
    _ClientUndeploySystemInstanceResponsesummaryTypeDef
):
    """
    - **summary** *(dict) --*

      An object that contains summary information about the system instance that was removed from
      its target.
      - **id** *(string) --*

        The ID of the system instance.
    """


_ClientUndeploySystemInstanceResponseTypeDef = TypedDict(
    "_ClientUndeploySystemInstanceResponseTypeDef",
    {"summary": ClientUndeploySystemInstanceResponsesummaryTypeDef},
    total=False,
)


class ClientUndeploySystemInstanceResponseTypeDef(_ClientUndeploySystemInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **summary** *(dict) --*

        An object that contains summary information about the system instance that was removed from
        its target.
        - **id** *(string) --*

          The ID of the system instance.
    """


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
    """
    The ``DefinitionDocument`` that contains the updated workflow definition.
    - **language** *(string) --***[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.
    """


_ClientUpdateFlowTemplateResponsesummaryTypeDef = TypedDict(
    "_ClientUpdateFlowTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientUpdateFlowTemplateResponsesummaryTypeDef(
    _ClientUpdateFlowTemplateResponsesummaryTypeDef
):
    """
    - **summary** *(dict) --*

      An object containing summary information about the updated workflow.
      - **id** *(string) --*

        The ID of the workflow.
    """


_ClientUpdateFlowTemplateResponseTypeDef = TypedDict(
    "_ClientUpdateFlowTemplateResponseTypeDef",
    {"summary": ClientUpdateFlowTemplateResponsesummaryTypeDef},
    total=False,
)


class ClientUpdateFlowTemplateResponseTypeDef(_ClientUpdateFlowTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **summary** *(dict) --*

        An object containing summary information about the updated workflow.
        - **id** *(string) --*

          The ID of the workflow.
    """


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
    """
    The ``DefinitionDocument`` that contains the updated system definition.
    - **language** *(string) --***[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.
    """


_ClientUpdateSystemTemplateResponsesummaryTypeDef = TypedDict(
    "_ClientUpdateSystemTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientUpdateSystemTemplateResponsesummaryTypeDef(
    _ClientUpdateSystemTemplateResponsesummaryTypeDef
):
    """
    - **summary** *(dict) --*

      An object containing summary information about the updated system.
      - **id** *(string) --*

        The ID of the system.
    """


_ClientUpdateSystemTemplateResponseTypeDef = TypedDict(
    "_ClientUpdateSystemTemplateResponseTypeDef",
    {"summary": ClientUpdateSystemTemplateResponsesummaryTypeDef},
    total=False,
)


class ClientUpdateSystemTemplateResponseTypeDef(_ClientUpdateSystemTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **summary** *(dict) --*

        An object containing summary information about the updated system.
        - **id** *(string) --*

          The ID of the system.
    """


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
    """
    The ``DefinitionDocument`` that defines the updated entities.
    - **language** *(string) --***[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.
    """


_ClientUploadEntityDefinitionsResponseTypeDef = TypedDict(
    "_ClientUploadEntityDefinitionsResponseTypeDef", {"uploadId": str}, total=False
)


class ClientUploadEntityDefinitionsResponseTypeDef(_ClientUploadEntityDefinitionsResponseTypeDef):
    """
    - *(dict) --*

      - **uploadId** *(string) --*

        The ID that specifies the upload action. You can use this to track the status of the upload.
    """


_GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef(
    _GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef = TypedDict(
    "_GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef(
    _GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains summary information about a workflow.
      - **id** *(string) --*

        The ID of the workflow.
    """


_GetFlowTemplateRevisionsPaginateResponseTypeDef = TypedDict(
    "_GetFlowTemplateRevisionsPaginateResponseTypeDef",
    {"summaries": List[GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef], "NextToken": str},
    total=False,
)


class GetFlowTemplateRevisionsPaginateResponseTypeDef(
    _GetFlowTemplateRevisionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that provide summary data about each revision.
        - *(dict) --*

          An object that contains summary information about a workflow.
          - **id** *(string) --*

            The ID of the workflow.
    """


_GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef(
    _GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef = TypedDict(
    "_GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef(
    _GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains information about a system.
      - **id** *(string) --*

        The ID of the system.
    """


_GetSystemTemplateRevisionsPaginateResponseTypeDef = TypedDict(
    "_GetSystemTemplateRevisionsPaginateResponseTypeDef",
    {
        "summaries": List[GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetSystemTemplateRevisionsPaginateResponseTypeDef(
    _GetSystemTemplateRevisionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that contain summary data about the system template revisions.
        - *(dict) --*

          An object that contains information about a system.
          - **id** *(string) --*

            The ID of the system.
    """


_ListFlowExecutionMessagesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFlowExecutionMessagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFlowExecutionMessagesPaginatePaginationConfigTypeDef(
    _ListFlowExecutionMessagesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFlowExecutionMessagesPaginateResponsemessagesTypeDef = TypedDict(
    "_ListFlowExecutionMessagesPaginateResponsemessagesTypeDef",
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


class ListFlowExecutionMessagesPaginateResponsemessagesTypeDef(
    _ListFlowExecutionMessagesPaginateResponsemessagesTypeDef
):
    """
    - *(dict) --*

      An object that contains information about a flow event.
      - **messageId** *(string) --*

        The unique identifier of the message.
    """


_ListFlowExecutionMessagesPaginateResponseTypeDef = TypedDict(
    "_ListFlowExecutionMessagesPaginateResponseTypeDef",
    {"messages": List[ListFlowExecutionMessagesPaginateResponsemessagesTypeDef], "NextToken": str},
    total=False,
)


class ListFlowExecutionMessagesPaginateResponseTypeDef(
    _ListFlowExecutionMessagesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **messages** *(list) --*

        A list of objects that contain information about events in the specified flow execution.
        - *(dict) --*

          An object that contains information about a flow event.
          - **messageId** *(string) --*

            The unique identifier of the message.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ListTagsForResourcePaginateResponsetagsTypeDef(
    _ListTagsForResourcePaginateResponsetagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.
      - **key** *(string) --*

        The required name of the tag. The string value can be from 1 to 128 Unicode characters in
        length.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(_ListTagsForResourcePaginateResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(list) --*

        List of tags returned by the ``ListTagsForResource`` operation.
        - *(dict) --*

          Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.
          - **key** *(string) --*

            The required name of the tag. The string value can be from 1 to 128 Unicode characters
            in length.
    """


_SearchEntitiesPaginateFiltersTypeDef = TypedDict(
    "_SearchEntitiesPaginateFiltersTypeDef",
    {
        "name": Literal["NAME", "NAMESPACE", "SEMANTIC_TYPE_PATH", "REFERENCED_ENTITY_ID"],
        "value": List[str],
    },
    total=False,
)


class SearchEntitiesPaginateFiltersTypeDef(_SearchEntitiesPaginateFiltersTypeDef):
    """
    - *(dict) --*

      An object that filters an entity search. Multiple filters function as OR criteria in the
      search. For example a search that includes a ``NAMESPACE`` and a ``REFERENCED_ENTITY_ID``
      filter searches for entities in the specified namespace that use the entity specified by the
      value of ``REFERENCED_ENTITY_ID`` .
      - **name** *(string) --*

        The name of the entity search filter field. ``REFERENCED_ENTITY_ID`` filters on entities
        that are used by the entity in the result set. For example, you can filter on the ID of a
        property that is used in a state.
    """


_SearchEntitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchEntitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchEntitiesPaginatePaginationConfigTypeDef(_SearchEntitiesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef = TypedDict(
    "_SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef(
    _SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef
):
    pass


_SearchEntitiesPaginateResponsedescriptionsTypeDef = TypedDict(
    "_SearchEntitiesPaginateResponsedescriptionsTypeDef",
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


class SearchEntitiesPaginateResponsedescriptionsTypeDef(
    _SearchEntitiesPaginateResponsedescriptionsTypeDef
):
    """
    - *(dict) --*

      Describes the properties of an entity.
      - **id** *(string) --*

        The entity ID.
    """


_SearchEntitiesPaginateResponseTypeDef = TypedDict(
    "_SearchEntitiesPaginateResponseTypeDef",
    {"descriptions": List[SearchEntitiesPaginateResponsedescriptionsTypeDef], "NextToken": str},
    total=False,
)


class SearchEntitiesPaginateResponseTypeDef(_SearchEntitiesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **descriptions** *(list) --*

        An array of descriptions for each entity returned in the search result.
        - *(dict) --*

          Describes the properties of an entity.
          - **id** *(string) --*

            The entity ID.
    """


_SearchFlowExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchFlowExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchFlowExecutionsPaginatePaginationConfigTypeDef(
    _SearchFlowExecutionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchFlowExecutionsPaginateResponsesummariesTypeDef = TypedDict(
    "_SearchFlowExecutionsPaginateResponsesummariesTypeDef",
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


class SearchFlowExecutionsPaginateResponsesummariesTypeDef(
    _SearchFlowExecutionsPaginateResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains summary information about a flow execution.
      - **flowExecutionId** *(string) --*

        The ID of the flow execution.
    """


_SearchFlowExecutionsPaginateResponseTypeDef = TypedDict(
    "_SearchFlowExecutionsPaginateResponseTypeDef",
    {"summaries": List[SearchFlowExecutionsPaginateResponsesummariesTypeDef], "NextToken": str},
    total=False,
)


class SearchFlowExecutionsPaginateResponseTypeDef(_SearchFlowExecutionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that contain summary information about each workflow execution in the
        result set.
        - *(dict) --*

          An object that contains summary information about a flow execution.
          - **flowExecutionId** *(string) --*

            The ID of the flow execution.
    """


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
    """
    - *(dict) --*

      An object that filters a workflow search.
      - **name** *(string) --***[REQUIRED]**

        The name of the search filter field.
    """


_SearchFlowTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchFlowTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchFlowTemplatesPaginatePaginationConfigTypeDef(
    _SearchFlowTemplatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchFlowTemplatesPaginateResponsesummariesTypeDef = TypedDict(
    "_SearchFlowTemplatesPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class SearchFlowTemplatesPaginateResponsesummariesTypeDef(
    _SearchFlowTemplatesPaginateResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains summary information about a workflow.
      - **id** *(string) --*

        The ID of the workflow.
    """


_SearchFlowTemplatesPaginateResponseTypeDef = TypedDict(
    "_SearchFlowTemplatesPaginateResponseTypeDef",
    {"summaries": List[SearchFlowTemplatesPaginateResponsesummariesTypeDef], "NextToken": str},
    total=False,
)


class SearchFlowTemplatesPaginateResponseTypeDef(_SearchFlowTemplatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that contain summary information about each workflow in the result set.
        - *(dict) --*

          An object that contains summary information about a workflow.
          - **id** *(string) --*

            The ID of the workflow.
    """


_SearchSystemInstancesPaginateFiltersTypeDef = TypedDict(
    "_SearchSystemInstancesPaginateFiltersTypeDef",
    {"name": Literal["SYSTEM_TEMPLATE_ID", "STATUS", "GREENGRASS_GROUP_NAME"], "value": List[str]},
    total=False,
)


class SearchSystemInstancesPaginateFiltersTypeDef(_SearchSystemInstancesPaginateFiltersTypeDef):
    """
    - *(dict) --*

      An object that filters a system instance search. Multiple filters function as OR criteria in
      the search. For example a search that includes a GREENGRASS_GROUP_NAME and a STATUS filter
      searches for system instances in the specified Greengrass group that have the specified
      status.
      - **name** *(string) --*

        The name of the search filter field.
    """


_SearchSystemInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchSystemInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchSystemInstancesPaginatePaginationConfigTypeDef(
    _SearchSystemInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchSystemInstancesPaginateResponsesummariesTypeDef = TypedDict(
    "_SearchSystemInstancesPaginateResponsesummariesTypeDef",
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


class SearchSystemInstancesPaginateResponsesummariesTypeDef(
    _SearchSystemInstancesPaginateResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains summary information about a system instance.
      - **id** *(string) --*

        The ID of the system instance.
    """


_SearchSystemInstancesPaginateResponseTypeDef = TypedDict(
    "_SearchSystemInstancesPaginateResponseTypeDef",
    {"summaries": List[SearchSystemInstancesPaginateResponsesummariesTypeDef], "NextToken": str},
    total=False,
)


class SearchSystemInstancesPaginateResponseTypeDef(_SearchSystemInstancesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that contain summary data abour the system instances in the result set.
        - *(dict) --*

          An object that contains summary information about a system instance.
          - **id** *(string) --*

            The ID of the system instance.
    """


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
    """
    - *(dict) --*

      An object that filters a system search.
      - **name** *(string) --***[REQUIRED]**

        The name of the system search filter field.
    """


_SearchSystemTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchSystemTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchSystemTemplatesPaginatePaginationConfigTypeDef(
    _SearchSystemTemplatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchSystemTemplatesPaginateResponsesummariesTypeDef = TypedDict(
    "_SearchSystemTemplatesPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class SearchSystemTemplatesPaginateResponsesummariesTypeDef(
    _SearchSystemTemplatesPaginateResponsesummariesTypeDef
):
    """
    - *(dict) --*

      An object that contains information about a system.
      - **id** *(string) --*

        The ID of the system.
    """


_SearchSystemTemplatesPaginateResponseTypeDef = TypedDict(
    "_SearchSystemTemplatesPaginateResponseTypeDef",
    {"summaries": List[SearchSystemTemplatesPaginateResponsesummariesTypeDef], "NextToken": str},
    total=False,
)


class SearchSystemTemplatesPaginateResponseTypeDef(_SearchSystemTemplatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **summaries** *(list) --*

        An array of objects that contain summary information about each system deployment in the
        result set.
        - *(dict) --*

          An object that contains information about a system.
          - **id** *(string) --*

            The ID of the system.
    """


_SearchThingsPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchThingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchThingsPaginatePaginationConfigTypeDef(_SearchThingsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_SearchThingsPaginateResponsethingsTypeDef = TypedDict(
    "_SearchThingsPaginateResponsethingsTypeDef", {"thingArn": str, "thingName": str}, total=False
)


class SearchThingsPaginateResponsethingsTypeDef(_SearchThingsPaginateResponsethingsTypeDef):
    """
    - *(dict) --*

      An AWS IoT thing.
      - **thingArn** *(string) --*

        The ARN of the thing.
    """


_SearchThingsPaginateResponseTypeDef = TypedDict(
    "_SearchThingsPaginateResponseTypeDef",
    {"things": List[SearchThingsPaginateResponsethingsTypeDef], "NextToken": str},
    total=False,
)


class SearchThingsPaginateResponseTypeDef(_SearchThingsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **things** *(list) --*

        An array of things in the result set.
        - *(dict) --*

          An AWS IoT thing.
          - **thingArn** *(string) --*

            The ARN of the thing.
    """
