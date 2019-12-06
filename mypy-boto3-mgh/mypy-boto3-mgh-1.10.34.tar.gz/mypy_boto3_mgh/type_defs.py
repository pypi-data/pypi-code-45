"Main interface for mgh service type defs"
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
    pass


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
    pass


ClientDescribeApplicationStateResponseTypeDef = TypedDict(
    "ClientDescribeApplicationStateResponseTypeDef",
    {
        "ApplicationStatus": Literal["NOT_STARTED", "IN_PROGRESS", "COMPLETED"],
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef = TypedDict(
    "ClientDescribeMigrationTaskResponseMigrationTaskResourceAttributeListTypeDef",
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

ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef = TypedDict(
    "ClientDescribeMigrationTaskResponseMigrationTaskTaskTypeDef",
    {
        "Status": Literal["NOT_STARTED", "IN_PROGRESS", "FAILED", "COMPLETED"],
        "StatusDetail": str,
        "ProgressPercent": int,
    },
    total=False,
)

ClientDescribeMigrationTaskResponseMigrationTaskTypeDef = TypedDict(
    "ClientDescribeMigrationTaskResponseMigrationTaskTypeDef",
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

ClientDescribeMigrationTaskResponseTypeDef = TypedDict(
    "ClientDescribeMigrationTaskResponseTypeDef",
    {"MigrationTask": ClientDescribeMigrationTaskResponseMigrationTaskTypeDef},
    total=False,
)

ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef = TypedDict(
    "ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef",
    {"Name": str, "Description": str},
    total=False,
)

ClientListCreatedArtifactsResponseTypeDef = TypedDict(
    "ClientListCreatedArtifactsResponseTypeDef",
    {
        "NextToken": str,
        "CreatedArtifactList": List[ClientListCreatedArtifactsResponseCreatedArtifactListTypeDef],
    },
    total=False,
)

ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef = TypedDict(
    "ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef",
    {"ConfigurationId": str, "Description": str},
    total=False,
)

ClientListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ClientListDiscoveredResourcesResponseTypeDef",
    {
        "NextToken": str,
        "DiscoveredResourceList": List[
            ClientListDiscoveredResourcesResponseDiscoveredResourceListTypeDef
        ],
    },
    total=False,
)

ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef = TypedDict(
    "ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef",
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

ClientListMigrationTasksResponseTypeDef = TypedDict(
    "ClientListMigrationTasksResponseTypeDef",
    {
        "NextToken": str,
        "MigrationTaskSummaryList": List[
            ClientListMigrationTasksResponseMigrationTaskSummaryListTypeDef
        ],
    },
    total=False,
)

ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef = TypedDict(
    "ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef",
    {"ProgressUpdateStreamName": str},
    total=False,
)

ClientListProgressUpdateStreamsResponseTypeDef = TypedDict(
    "ClientListProgressUpdateStreamsResponseTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List[
            ClientListProgressUpdateStreamsResponseProgressUpdateStreamSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

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
    pass


ClientPutResourceAttributesResourceAttributeListTypeDef = TypedDict(
    "ClientPutResourceAttributesResourceAttributeListTypeDef",
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

ListCreatedArtifactsPaginatePaginationConfigTypeDef = TypedDict(
    "ListCreatedArtifactsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef = TypedDict(
    "ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef",
    {"Name": str, "Description": str},
    total=False,
)

ListCreatedArtifactsPaginateResponseTypeDef = TypedDict(
    "ListCreatedArtifactsPaginateResponseTypeDef",
    {"CreatedArtifactList": List[ListCreatedArtifactsPaginateResponseCreatedArtifactListTypeDef]},
    total=False,
)

ListDiscoveredResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "ListDiscoveredResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef = TypedDict(
    "ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef",
    {"ConfigurationId": str, "Description": str},
    total=False,
)

ListDiscoveredResourcesPaginateResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesPaginateResponseTypeDef",
    {
        "DiscoveredResourceList": List[
            ListDiscoveredResourcesPaginateResponseDiscoveredResourceListTypeDef
        ]
    },
    total=False,
)

ListMigrationTasksPaginatePaginationConfigTypeDef = TypedDict(
    "ListMigrationTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef = TypedDict(
    "ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef",
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

ListMigrationTasksPaginateResponseTypeDef = TypedDict(
    "ListMigrationTasksPaginateResponseTypeDef",
    {
        "MigrationTaskSummaryList": List[
            ListMigrationTasksPaginateResponseMigrationTaskSummaryListTypeDef
        ]
    },
    total=False,
)

ListProgressUpdateStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "ListProgressUpdateStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef = TypedDict(
    "ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef",
    {"ProgressUpdateStreamName": str},
    total=False,
)

ListProgressUpdateStreamsPaginateResponseTypeDef = TypedDict(
    "ListProgressUpdateStreamsPaginateResponseTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List[
            ListProgressUpdateStreamsPaginateResponseProgressUpdateStreamSummaryListTypeDef
        ]
    },
    total=False,
)
