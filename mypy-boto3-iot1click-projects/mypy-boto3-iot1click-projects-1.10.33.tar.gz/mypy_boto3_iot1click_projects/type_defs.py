"Main interface for iot1click-projects service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)

ClientCreateProjectPlacementTemplateTypeDef = TypedDict(
    "ClientCreateProjectPlacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[str, ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef],
    },
    total=False,
)

ClientDescribePlacementResponseplacementTypeDef = TypedDict(
    "ClientDescribePlacementResponseplacementTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "attributes": Dict[str, str],
        "createdDate": datetime,
        "updatedDate": datetime,
    },
    total=False,
)

ClientDescribePlacementResponseTypeDef = TypedDict(
    "ClientDescribePlacementResponseTypeDef",
    {"placement": ClientDescribePlacementResponseplacementTypeDef},
    total=False,
)

ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)

ClientDescribeProjectResponseprojectplacementTemplateTypeDef = TypedDict(
    "ClientDescribeProjectResponseprojectplacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[
            str, ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef
        ],
    },
    total=False,
)

ClientDescribeProjectResponseprojectTypeDef = TypedDict(
    "ClientDescribeProjectResponseprojectTypeDef",
    {
        "arn": str,
        "projectName": str,
        "description": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "placementTemplate": ClientDescribeProjectResponseprojectplacementTemplateTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientDescribeProjectResponseTypeDef = TypedDict(
    "ClientDescribeProjectResponseTypeDef",
    {"project": ClientDescribeProjectResponseprojectTypeDef},
    total=False,
)

ClientGetDevicesInPlacementResponseTypeDef = TypedDict(
    "ClientGetDevicesInPlacementResponseTypeDef", {"devices": Dict[str, str]}, total=False
)

ClientListPlacementsResponseplacementsTypeDef = TypedDict(
    "ClientListPlacementsResponseplacementsTypeDef",
    {"projectName": str, "placementName": str, "createdDate": datetime, "updatedDate": datetime},
    total=False,
)

ClientListPlacementsResponseTypeDef = TypedDict(
    "ClientListPlacementsResponseTypeDef",
    {"placements": List[ClientListPlacementsResponseplacementsTypeDef], "nextToken": str},
    total=False,
)

ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "ClientListProjectsResponseprojectsTypeDef",
    {
        "arn": str,
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListProjectsResponseTypeDef = TypedDict(
    "ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)

ClientUpdateProjectPlacementTemplateTypeDef = TypedDict(
    "ClientUpdateProjectPlacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[str, ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef],
    },
    total=False,
)

ListPlacementsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPlacementsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPlacementsPaginateResponseplacementsTypeDef = TypedDict(
    "ListPlacementsPaginateResponseplacementsTypeDef",
    {"projectName": str, "placementName": str, "createdDate": datetime, "updatedDate": datetime},
    total=False,
)

ListPlacementsPaginateResponseTypeDef = TypedDict(
    "ListPlacementsPaginateResponseTypeDef",
    {"placements": List[ListPlacementsPaginateResponseplacementsTypeDef], "NextToken": str},
    total=False,
)

ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListProjectsPaginateResponseprojectsTypeDef = TypedDict(
    "ListProjectsPaginateResponseprojectsTypeDef",
    {
        "arn": str,
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ListProjectsPaginateResponseTypeDef = TypedDict(
    "ListProjectsPaginateResponseTypeDef",
    {"projects": List[ListProjectsPaginateResponseprojectsTypeDef], "NextToken": str},
    total=False,
)
