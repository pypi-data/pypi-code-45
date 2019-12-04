"Main interface for mgh service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAssociateCreatedArtifactCreatedArtifactTypeDef",
    "ClientAssociateDiscoveredResourceDiscoveredResourceTypeDef",
    "ClientDescribeApplicationStateResponseTypeDef",
    "ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef",
    "ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef",
    "ClientDescribeMigrationTaskResponseMigrationTaskTypeDef",
    "ClientDescribeMigrationTaskResponseTypeDef",
    "ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef",
    "ClientListCreatedArtifactsResponseTypeDef",
    "ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef",
    "ClientListDiscoveredResourcesResponseTypeDef",
    "ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef",
    "ClientListMigrationTasksResponseTypeDef",
    "ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef",
    "ClientListProgressUpdateStreamsResponseTypeDef",
    "ClientNotifyMigrationTaskStateTaskTypeDef",
    "ClientPutResourceAttributesResourceAttributeListTypeDef",
    "ListCreatedArtifactsPaginatePaginationConfigTypeDef",
    "ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef",
    "ListCreatedArtifactsPaginateResponseTypeDef",
    "ListDiscoveredResourcesPaginatePaginationConfigTypeDef",
    "ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef",
    "ListDiscoveredResourcesPaginateResponseTypeDef",
    "ListMigrationTasksPaginatePaginationConfigTypeDef",
    "ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef",
    "ListMigrationTasksPaginateResponseTypeDef",
    "ListProgressUpdateStreamsPaginatePaginationConfigTypeDef",
    "ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef",
    "ListProgressUpdateStreamsPaginateResponseTypeDef",
)


_RequiredClientAssociateCreatedArtifactCreatedArtifactTypeDef = TypedDict(
    "_RequiredClientAssociateCreatedArtifactCreatedArtifactTypeDef", {"Name": str}
)
_OptionalClientAssociateCreatedArtifactCreatedArtifactTypeDef = TypedDict(
    "_OptionalClientAssociateCreatedArtifactCreatedArtifactTypeDef",
    {"Description": str},
    total=False,
)


class ClientAssociateCreatedArtifactCreatedArtifactTypeDef(
    _RequiredClientAssociateCreatedArtifactCreatedArtifactTypeDef,
    _OptionalClientAssociateCreatedArtifactCreatedArtifactTypeDef,
):
    """
    An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance,
    etc.)
    - **Name** *(string) --***[REQUIRED]**

      An ARN that uniquely identifies the result of a migration task.
    """


_RequiredClientAssociateDiscoveredResourceDiscoveredResourceTypeDef = TypedDict(
    "_RequiredClientAssociateDiscoveredResourceDiscoveredResourceTypeDef", {"ConfigurationId": str}
)
_OptionalClientAssociateDiscoveredResourceDiscoveredResourceTypeDef = TypedDict(
    "_OptionalClientAssociateDiscoveredResourceDiscoveredResourceTypeDef",
    {"Description": str},
    total=False,
)


class ClientAssociateDiscoveredResourceDiscoveredResourceTypeDef(
    _RequiredClientAssociateDiscoveredResourceDiscoveredResourceTypeDef,
    _OptionalClientAssociateDiscoveredResourceDiscoveredResourceTypeDef,
):
    """
    Object representing a Resource.
    - **ConfigurationId** *(string) --***[REQUIRED]**

      The configurationId in Application Discovery Service that uniquely identifies the on-premise
      resource.
    """


_ClientDescribeApplicationStateResponseTypeDef = TypedDict(
    "_ClientDescribeApplicationStateResponseTypeDef",
    {
        "ApplicationStatus": Literal["NOT_STARTED", "IN_PROGRESS", "COMPLETED"],
        "LastUpdatedTime": datetime,
    },
    total=False,
)


class ClientDescribeApplicationStateResponseTypeDef(_ClientDescribeApplicationStateResponseTypeDef):
    """
    - *(dict) --*

      - **ApplicationStatus** *(string) --*

        Status of the application - Not Started, In-Progress, Complete.
    """


_ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef = TypedDict(
    "_ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef",
    {
        "Type": Literal[
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MAC_ADDRESS",
            "FQDN",
            "VM_MANAGER_ID",
            "VM_MANAGED_OBJECT_REFERENCE",
            "VM_NAME",
            "VM_PATH",
            "BIOS_ID",
            "MOTHERBOARD_SERIAL_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef(
    _ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef
):
    pass


_ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef = TypedDict(
    "_ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef",
    {
        "Status": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "StatusDetail": str,
        "ProgressPercent": int,
    },
    total=False,
)


class ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef(
    _ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef
):
    pass


_ClientDescribeMigrationTaskResponseMigrationTaskTypeDef = TypedDict(
    "_ClientDescribeMigrationTaskResponseMigrationTaskTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Task": ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef,
        "UpdateDateTime": datetime,
        "ResourceAttributeList": List[
            ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef
        ],
    },
    total=False,
)


class ClientDescribeMigrationTaskResponseMigrationTaskTypeDef(
    _ClientDescribeMigrationTaskResponseMigrationTaskTypeDef
):
    """
    - **MigrationTask** *(dict) --*

      Object encapsulating information about the migration task.
      - **ProgressUpdateStream** *(string) --*

        A name that identifies the vendor of the migration tool being used.
    """


_ClientDescribeMigrationTaskResponseTypeDef = TypedDict(
    "_ClientDescribeMigrationTaskResponseTypeDef",
    {"MigrationTask": ClientDescribeMigrationTaskResponseMigrationTaskTypeDef},
    total=False,
)


class ClientDescribeMigrationTaskResponseTypeDef(_ClientDescribeMigrationTaskResponseTypeDef):
    """
    - *(dict) --*

      - **MigrationTask** *(dict) --*

        Object encapsulating information about the migration task.
        - **ProgressUpdateStream** *(string) --*

          A name that identifies the vendor of the migration tool being used.
    """


_ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef = TypedDict(
    "_ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef",
    {"Name": str, "Description": str},
    total=False,
)


class ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef(
    _ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef
):
    pass


_ClientListCreatedArtifactsResponseTypeDef = TypedDict(
    "_ClientListCreatedArtifactsResponseTypeDef",
    {
        "NextToken": str,
        "CreatedArtifactList": List[ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef],
    },
    total=False,
)


class ClientListCreatedArtifactsResponseTypeDef(_ClientListCreatedArtifactsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If there are more created artifacts than the max result, return the next token to be passed
        to the next call as a bookmark of where to start from.
    """


_ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef = TypedDict(
    "_ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef",
    {"ConfigurationId": str, "Description": str},
    total=False,
)


class ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef(
    _ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef
):
    pass


_ClientListDiscoveredResourcesResponseTypeDef = TypedDict(
    "_ClientListDiscoveredResourcesResponseTypeDef",
    {
        "NextToken": str,
        "DiscoveredResourceList": List[
            ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef
        ],
    },
    total=False,
)


class ClientListDiscoveredResourcesResponseTypeDef(_ClientListDiscoveredResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If there are more discovered resources than the max result, return the next token to be
        passed to the next call as a bookmark of where to start from.
    """


_ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef = TypedDict(
    "_ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Status": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "ProgressPercent": int,
        "StatusDetail": str,
        "UpdateDateTime": datetime,
    },
    total=False,
)


class ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef(
    _ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef
):
    pass


_ClientListMigrationTasksResponseTypeDef = TypedDict(
    "_ClientListMigrationTasksResponseTypeDef",
    {
        "NextToken": str,
        "MigrationTaskSummaryList": List[
            ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef
        ],
    },
    total=False,
)


class ClientListMigrationTasksResponseTypeDef(_ClientListMigrationTasksResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If there are more migration tasks than the max result, return the next token to be passed to
        the next call as a bookmark of where to start from.
    """


_ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef = TypedDict(
    "_ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef",
    {"ProgressUpdateStreamName": str},
    total=False,
)


class ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef(
    _ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef
):
    """
    - *(dict) --*

      Summary of the AWS resource used for access control that is implicitly linked to your AWS
      account.
      - **ProgressUpdateStreamName** *(string) --*

        The name of the ProgressUpdateStream. *Do not store personal data in this field.*
    """


_ClientListProgressUpdateStreamsResponseTypeDef = TypedDict(
    "_ClientListProgressUpdateStreamsResponseTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List[
            ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListProgressUpdateStreamsResponseTypeDef(
    _ClientListProgressUpdateStreamsResponseTypeDef
):
    """
    - *(dict) --*

      - **ProgressUpdateStreamSummaryList** *(list) --*

        List of progress update streams up to the max number of results passed in the input.
        - *(dict) --*

          Summary of the AWS resource used for access control that is implicitly linked to your AWS
          account.
          - **ProgressUpdateStreamName** *(string) --*

            The name of the ProgressUpdateStream. *Do not store personal data in this field.*
    """


_RequiredClientNotifyMigrationTaskStateTaskTypeDef = TypedDict(
    "_RequiredClientNotifyMigrationTaskStateTaskTypeDef",
    {"Status": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "COMPLETED"]},
)
_OptionalClientNotifyMigrationTaskStateTaskTypeDef = TypedDict(
    "_OptionalClientNotifyMigrationTaskStateTaskTypeDef",
    {"StatusDetail": str, "ProgressPercent": int},
    total=False,
)


class ClientNotifyMigrationTaskStateTaskTypeDef(
    _RequiredClientNotifyMigrationTaskStateTaskTypeDef,
    _OptionalClientNotifyMigrationTaskStateTaskTypeDef,
):
    """
    Information about the task's progress and status.
    - **Status** *(string) --***[REQUIRED]**

      Status of the task - Not Started, In-Progress, Complete.
    """


_ClientPutResourceAttributesResourceAttributeListTypeDef = TypedDict(
    "_ClientPutResourceAttributesResourceAttributeListTypeDef",
    {
        "Type": Literal[
            "IPV4_ADDRESS",
            "IPV6_ADDRESS",
            "MAC_ADDRESS",
            "FQDN",
            "VM_MANAGER_ID",
            "VM_MANAGED_OBJECT_REFERENCE",
            "VM_NAME",
            "VM_PATH",
            "BIOS_ID",
            "MOTHERBOARD_SERIAL_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientPutResourceAttributesResourceAttributeListTypeDef(
    _ClientPutResourceAttributesResourceAttributeListTypeDef
):
    pass


_ListCreatedArtifactsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCreatedArtifactsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCreatedArtifactsPaginatePaginationConfigTypeDef(
    _ListCreatedArtifactsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef = TypedDict(
    "_ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef",
    {"Name": str, "Description": str},
    total=False,
)


class ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef(
    _ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef
):
    """
    - *(dict) --*

      An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance, RDS
      instance, etc.).
      - **Name** *(string) --*

        An ARN that uniquely identifies the result of a migration task.
    """


_ListCreatedArtifactsPaginateResponseTypeDef = TypedDict(
    "_ListCreatedArtifactsPaginateResponseTypeDef",
    {"CreatedArtifactList": List[ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef]},
    total=False,
)


class ListCreatedArtifactsPaginateResponseTypeDef(_ListCreatedArtifactsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **CreatedArtifactList** *(list) --*

        List of created artifacts up to the maximum number of results specified in the request.
        - *(dict) --*

          An ARN of the AWS cloud resource target receiving the migration (e.g., AMI, EC2 instance,
          RDS instance, etc.).
          - **Name** *(string) --*

            An ARN that uniquely identifies the result of a migration task.
    """


_ListDiscoveredResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDiscoveredResourcesPaginatePaginationConfigTypeDef(
    _ListDiscoveredResourcesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef",
    {"ConfigurationId": str, "Description": str},
    total=False,
)


class ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef(
    _ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef
):
    """
    - *(dict) --*

      Object representing the on-premises resource being migrated.
      - **ConfigurationId** *(string) --*

        The configurationId in Application Discovery Service that uniquely identifies the on-premise
        resource.
    """


_ListDiscoveredResourcesPaginateResponseTypeDef = TypedDict(
    "_ListDiscoveredResourcesPaginateResponseTypeDef",
    {
        "DiscoveredResourceList": List[
            ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef
        ]
    },
    total=False,
)


class ListDiscoveredResourcesPaginateResponseTypeDef(
    _ListDiscoveredResourcesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DiscoveredResourceList** *(list) --*

        Returned list of discovered resources associated with the given MigrationTask.
        - *(dict) --*

          Object representing the on-premises resource being migrated.
          - **ConfigurationId** *(string) --*

            The configurationId in Application Discovery Service that uniquely identifies the
            on-premise resource.
    """


_ListMigrationTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListMigrationTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListMigrationTasksPaginatePaginationConfigTypeDef(
    _ListMigrationTasksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef = TypedDict(
    "_ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Status": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "ProgressPercent": int,
        "StatusDetail": str,
        "UpdateDateTime": datetime,
    },
    total=False,
)


class ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef(
    _ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef
):
    """
    - *(dict) --*

      MigrationTaskSummary includes ``MigrationTaskName`` , ``ProgressPercent`` ,
      ``ProgressUpdateStream`` , ``Status`` , and ``UpdateDateTime`` for each task.
      - **ProgressUpdateStream** *(string) --*

        An AWS resource used for access control. It should uniquely identify the migration tool as
        it is used for all updates made by the tool.
    """


_ListMigrationTasksPaginateResponseTypeDef = TypedDict(
    "_ListMigrationTasksPaginateResponseTypeDef",
    {
        "MigrationTaskSummaryList": List[
            ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef
        ]
    },
    total=False,
)


class ListMigrationTasksPaginateResponseTypeDef(_ListMigrationTasksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **MigrationTaskSummaryList** *(list) --*

        Lists the migration task's summary which includes: ``MigrationTaskName`` ,
        ``ProgressPercent`` , ``ProgressUpdateStream`` , ``Status`` , and the ``UpdateDateTime`` for
        each task.
        - *(dict) --*

          MigrationTaskSummary includes ``MigrationTaskName`` , ``ProgressPercent`` ,
          ``ProgressUpdateStream`` , ``Status`` , and ``UpdateDateTime`` for each task.
          - **ProgressUpdateStream** *(string) --*

            An AWS resource used for access control. It should uniquely identify the migration tool
            as it is used for all updates made by the tool.
    """


_ListProgressUpdateStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProgressUpdateStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProgressUpdateStreamsPaginatePaginationConfigTypeDef(
    _ListProgressUpdateStreamsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef = TypedDict(
    "_ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef",
    {"ProgressUpdateStreamName": str},
    total=False,
)


class ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef(
    _ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef
):
    """
    - *(dict) --*

      Summary of the AWS resource used for access control that is implicitly linked to your AWS
      account.
      - **ProgressUpdateStreamName** *(string) --*

        The name of the ProgressUpdateStream. *Do not store personal data in this field.*
    """


_ListProgressUpdateStreamsPaginateResponseTypeDef = TypedDict(
    "_ListProgressUpdateStreamsPaginateResponseTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List[
            ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef
        ]
    },
    total=False,
)


class ListProgressUpdateStreamsPaginateResponseTypeDef(
    _ListProgressUpdateStreamsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **ProgressUpdateStreamSummaryList** *(list) --*

        List of progress update streams up to the max number of results passed in the input.
        - *(dict) --*

          Summary of the AWS resource used for access control that is implicitly linked to your AWS
          account.
          - **ProgressUpdateStreamName** *(string) --*

            The name of the ProgressUpdateStream. *Do not store personal data in this field.*
    """
