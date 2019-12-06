"Main interface for mobile service type defs"
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


ClientCreateProjectResponsedetailsresourcesTypeDef = TypedDict(
    "ClientCreateProjectResponsedetailsresourcesTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)

ClientCreateProjectResponsedetailsTypeDef = TypedDict(
    "ClientCreateProjectResponsedetailsTypeDef",
    {
        "name": str,
        "projectId": str,
        "region": str,
        "state": Literal["NORMAL", "SYNCING", "IMPORTING"],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "consoleUrl": str,
        "resources": List[ClientCreateProjectResponsedetailsresourcesTypeDef],
    },
    total=False,
)

ClientCreateProjectResponseTypeDef = TypedDict(
    "ClientCreateProjectResponseTypeDef",
    {"details": ClientCreateProjectResponsedetailsTypeDef},
    total=False,
)

ClientDeleteProjectResponsedeletedResourcesTypeDef = TypedDict(
    "ClientDeleteProjectResponsedeletedResourcesTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)

ClientDeleteProjectResponseorphanedResourcesTypeDef = TypedDict(
    "ClientDeleteProjectResponseorphanedResourcesTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)

ClientDeleteProjectResponseTypeDef = TypedDict(
    "ClientDeleteProjectResponseTypeDef",
    {
        "deletedResources": List[ClientDeleteProjectResponsedeletedResourcesTypeDef],
        "orphanedResources": List[ClientDeleteProjectResponseorphanedResourcesTypeDef],
    },
    total=False,
)

ClientDescribeBundleResponsedetailsTypeDef = TypedDict(
    "ClientDescribeBundleResponsedetailsTypeDef",
    {
        "bundleId": str,
        "title": str,
        "version": str,
        "description": str,
        "iconUrl": str,
        "availablePlatforms": List[
            Literal["OSX", "WINDOWS", "LINUX", "OBJC", "SWIFT", "ANDROID", "JAVASCRIPT"]
        ],
    },
    total=False,
)

ClientDescribeBundleResponseTypeDef = TypedDict(
    "ClientDescribeBundleResponseTypeDef",
    {"details": ClientDescribeBundleResponsedetailsTypeDef},
    total=False,
)

ClientDescribeProjectResponsedetailsresourcesTypeDef = TypedDict(
    "ClientDescribeProjectResponsedetailsresourcesTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)

ClientDescribeProjectResponsedetailsTypeDef = TypedDict(
    "ClientDescribeProjectResponsedetailsTypeDef",
    {
        "name": str,
        "projectId": str,
        "region": str,
        "state": Literal["NORMAL", "SYNCING", "IMPORTING"],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "consoleUrl": str,
        "resources": List[ClientDescribeProjectResponsedetailsresourcesTypeDef],
    },
    total=False,
)

ClientDescribeProjectResponseTypeDef = TypedDict(
    "ClientDescribeProjectResponseTypeDef",
    {"details": ClientDescribeProjectResponsedetailsTypeDef},
    total=False,
)

ClientExportBundleResponseTypeDef = TypedDict(
    "ClientExportBundleResponseTypeDef", {"downloadUrl": str}, total=False
)

ClientExportProjectResponseTypeDef = TypedDict(
    "ClientExportProjectResponseTypeDef",
    {"downloadUrl": str, "shareUrl": str, "snapshotId": str},
    total=False,
)

ClientListBundlesResponsebundleListTypeDef = TypedDict(
    "ClientListBundlesResponsebundleListTypeDef",
    {
        "bundleId": str,
        "title": str,
        "version": str,
        "description": str,
        "iconUrl": str,
        "availablePlatforms": List[
            Literal["OSX", "WINDOWS", "LINUX", "OBJC", "SWIFT", "ANDROID", "JAVASCRIPT"]
        ],
    },
    total=False,
)

ClientListBundlesResponseTypeDef = TypedDict(
    "ClientListBundlesResponseTypeDef",
    {"bundleList": List[ClientListBundlesResponsebundleListTypeDef], "nextToken": str},
    total=False,
)

ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "ClientListProjectsResponseprojectsTypeDef", {"name": str, "projectId": str}, total=False
)

ClientListProjectsResponseTypeDef = TypedDict(
    "ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)

ClientUpdateProjectResponsedetailsresourcesTypeDef = TypedDict(
    "ClientUpdateProjectResponsedetailsresourcesTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)

ClientUpdateProjectResponsedetailsTypeDef = TypedDict(
    "ClientUpdateProjectResponsedetailsTypeDef",
    {
        "name": str,
        "projectId": str,
        "region": str,
        "state": Literal["NORMAL", "SYNCING", "IMPORTING"],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "consoleUrl": str,
        "resources": List[ClientUpdateProjectResponsedetailsresourcesTypeDef],
    },
    total=False,
)

ClientUpdateProjectResponseTypeDef = TypedDict(
    "ClientUpdateProjectResponseTypeDef",
    {"details": ClientUpdateProjectResponsedetailsTypeDef},
    total=False,
)

ListBundlesPaginatePaginationConfigTypeDef = TypedDict(
    "ListBundlesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListBundlesPaginateResponsebundleListTypeDef = TypedDict(
    "ListBundlesPaginateResponsebundleListTypeDef",
    {
        "bundleId": str,
        "title": str,
        "version": str,
        "description": str,
        "iconUrl": str,
        "availablePlatforms": List[
            Literal["OSX", "WINDOWS", "LINUX", "OBJC", "SWIFT", "ANDROID", "JAVASCRIPT"]
        ],
    },
    total=False,
)

ListBundlesPaginateResponseTypeDef = TypedDict(
    "ListBundlesPaginateResponseTypeDef",
    {"bundleList": List[ListBundlesPaginateResponsebundleListTypeDef], "NextToken": str},
    total=False,
)

ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListProjectsPaginateResponseprojectsTypeDef = TypedDict(
    "ListProjectsPaginateResponseprojectsTypeDef", {"name": str, "projectId": str}, total=False
)

ListProjectsPaginateResponseTypeDef = TypedDict(
    "ListProjectsPaginateResponseTypeDef",
    {"projects": List[ListProjectsPaginateResponseprojectsTypeDef], "NextToken": str},
    total=False,
)
