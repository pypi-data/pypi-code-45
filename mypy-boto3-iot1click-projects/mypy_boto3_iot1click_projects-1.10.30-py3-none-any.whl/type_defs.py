"Main interface for iot1click-projects service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef",
    "ClientCreateProjectPlacementTemplateTypeDef",
    "ClientDescribePlacementResponseplacementTypeDef",
    "ClientDescribePlacementResponseTypeDef",
    "ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef",
    "ClientDescribeProjectResponseprojectplacementTemplateTypeDef",
    "ClientDescribeProjectResponseprojectTypeDef",
    "ClientDescribeProjectResponseTypeDef",
    "ClientGetDevicesInPlacementResponseTypeDef",
    "ClientListPlacementsResponseplacementsTypeDef",
    "ClientListPlacementsResponseTypeDef",
    "ClientListProjectsResponseprojectsTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef",
    "ClientUpdateProjectPlacementTemplateTypeDef",
    "ListPlacementsPaginatePaginationConfigTypeDef",
    "ListPlacementsPaginateResponseplacementsTypeDef",
    "ListPlacementsPaginateResponseTypeDef",
    "ListProjectsPaginatePaginationConfigTypeDef",
    "ListProjectsPaginateResponseprojectsTypeDef",
    "ListProjectsPaginateResponseTypeDef",
)


_ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "_ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)


class ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef(
    _ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef
):
    pass


_ClientCreateProjectPlacementTemplateTypeDef = TypedDict(
    "_ClientCreateProjectPlacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[str, ClientCreateProjectPlacementTemplatedeviceTemplatesTypeDef],
    },
    total=False,
)


class ClientCreateProjectPlacementTemplateTypeDef(_ClientCreateProjectPlacementTemplateTypeDef):
    """
    The schema defining the placement to be created. A placement template defines placement default
    attributes and device templates. You cannot add or remove device templates after the project has
    been created. However, you can update ``callbackOverrides`` for the device templates using the
    ``UpdateProject`` API.
    - **defaultAttributes** *(dict) --*

      The default attributes (key/value pairs) to be applied to all placements using this template.
      - *(string) --*

        - *(string) --*
    """


_ClientDescribePlacementResponseplacementTypeDef = TypedDict(
    "_ClientDescribePlacementResponseplacementTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "attributes": Dict[str, str],
        "createdDate": datetime,
        "updatedDate": datetime,
    },
    total=False,
)


class ClientDescribePlacementResponseplacementTypeDef(
    _ClientDescribePlacementResponseplacementTypeDef
):
    """
    - **placement** *(dict) --*

      An object describing the placement.
      - **projectName** *(string) --*

        The name of the project containing the placement.
    """


_ClientDescribePlacementResponseTypeDef = TypedDict(
    "_ClientDescribePlacementResponseTypeDef",
    {"placement": ClientDescribePlacementResponseplacementTypeDef},
    total=False,
)


class ClientDescribePlacementResponseTypeDef(_ClientDescribePlacementResponseTypeDef):
    """
    - *(dict) --*

      - **placement** *(dict) --*

        An object describing the placement.
        - **projectName** *(string) --*

          The name of the project containing the placement.
    """


_ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "_ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)


class ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef(
    _ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef
):
    pass


_ClientDescribeProjectResponseprojectplacementTemplateTypeDef = TypedDict(
    "_ClientDescribeProjectResponseprojectplacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[
            str, ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeProjectResponseprojectplacementTemplateTypeDef(
    _ClientDescribeProjectResponseprojectplacementTemplateTypeDef
):
    pass


_ClientDescribeProjectResponseprojectTypeDef = TypedDict(
    "_ClientDescribeProjectResponseprojectTypeDef",
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


class ClientDescribeProjectResponseprojectTypeDef(_ClientDescribeProjectResponseprojectTypeDef):
    """
    - **project** *(dict) --*

      An object describing the project.
      - **arn** *(string) --*

        The ARN of the project.
    """


_ClientDescribeProjectResponseTypeDef = TypedDict(
    "_ClientDescribeProjectResponseTypeDef",
    {"project": ClientDescribeProjectResponseprojectTypeDef},
    total=False,
)


class ClientDescribeProjectResponseTypeDef(_ClientDescribeProjectResponseTypeDef):
    """
    - *(dict) --*

      - **project** *(dict) --*

        An object describing the project.
        - **arn** *(string) --*

          The ARN of the project.
    """


_ClientGetDevicesInPlacementResponseTypeDef = TypedDict(
    "_ClientGetDevicesInPlacementResponseTypeDef", {"devices": Dict[str, str]}, total=False
)


class ClientGetDevicesInPlacementResponseTypeDef(_ClientGetDevicesInPlacementResponseTypeDef):
    """
    - *(dict) --*

      - **devices** *(dict) --*

        An object containing the devices (zero or more) within the placement.
        - *(string) --*

          - *(string) --*
    """


_ClientListPlacementsResponseplacementsTypeDef = TypedDict(
    "_ClientListPlacementsResponseplacementsTypeDef",
    {"projectName": str, "placementName": str, "createdDate": datetime, "updatedDate": datetime},
    total=False,
)


class ClientListPlacementsResponseplacementsTypeDef(_ClientListPlacementsResponseplacementsTypeDef):
    """
    - *(dict) --*

      An object providing summary information for a particular placement.
      - **projectName** *(string) --*

        The name of the project containing the placement.
    """


_ClientListPlacementsResponseTypeDef = TypedDict(
    "_ClientListPlacementsResponseTypeDef",
    {"placements": List[ClientListPlacementsResponseplacementsTypeDef], "nextToken": str},
    total=False,
)


class ClientListPlacementsResponseTypeDef(_ClientListPlacementsResponseTypeDef):
    """
    - *(dict) --*

      - **placements** *(list) --*

        An object listing the requested placements.
        - *(dict) --*

          An object providing summary information for a particular placement.
          - **projectName** *(string) --*

            The name of the project containing the placement.
    """


_ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "_ClientListProjectsResponseprojectsTypeDef",
    {
        "arn": str,
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientListProjectsResponseprojectsTypeDef(_ClientListProjectsResponseprojectsTypeDef):
    """
    - *(dict) --*

      An object providing summary information for a particular project for an associated AWS account
      and region.
      - **arn** *(string) --*

        The ARN of the project.
    """


_ClientListProjectsResponseTypeDef = TypedDict(
    "_ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)


class ClientListProjectsResponseTypeDef(_ClientListProjectsResponseTypeDef):
    """
    - *(dict) --*

      - **projects** *(list) --*

        An object containing the list of projects.
        - *(dict) --*

          An object providing summary information for a particular project for an associated AWS
          account and region.
          - **arn** *(string) --*

            The ARN of the project.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        The tags (metadata key/value pairs) which you have assigned to the resource.
        - *(string) --*

          - *(string) --*
    """


_ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "_ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)


class ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef(
    _ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef
):
    pass


_ClientUpdateProjectPlacementTemplateTypeDef = TypedDict(
    "_ClientUpdateProjectPlacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[str, ClientUpdateProjectPlacementTemplatedeviceTemplatesTypeDef],
    },
    total=False,
)


class ClientUpdateProjectPlacementTemplateTypeDef(_ClientUpdateProjectPlacementTemplateTypeDef):
    """
    An object defining the project update. Once a project has been created, you cannot add device
    template names to the project. However, for a given ``placementTemplate`` , you can update the
    associated ``callbackOverrides`` for the device definition using this API.
    - **defaultAttributes** *(dict) --*

      The default attributes (key/value pairs) to be applied to all placements using this template.
      - *(string) --*

        - *(string) --*
    """


_ListPlacementsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPlacementsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPlacementsPaginatePaginationConfigTypeDef(_ListPlacementsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPlacementsPaginateResponseplacementsTypeDef = TypedDict(
    "_ListPlacementsPaginateResponseplacementsTypeDef",
    {"projectName": str, "placementName": str, "createdDate": datetime, "updatedDate": datetime},
    total=False,
)


class ListPlacementsPaginateResponseplacementsTypeDef(
    _ListPlacementsPaginateResponseplacementsTypeDef
):
    """
    - *(dict) --*

      An object providing summary information for a particular placement.
      - **projectName** *(string) --*

        The name of the project containing the placement.
    """


_ListPlacementsPaginateResponseTypeDef = TypedDict(
    "_ListPlacementsPaginateResponseTypeDef",
    {"placements": List[ListPlacementsPaginateResponseplacementsTypeDef], "NextToken": str},
    total=False,
)


class ListPlacementsPaginateResponseTypeDef(_ListPlacementsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **placements** *(list) --*

        An object listing the requested placements.
        - *(dict) --*

          An object providing summary information for a particular placement.
          - **projectName** *(string) --*

            The name of the project containing the placement.
    """


_ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProjectsPaginatePaginationConfigTypeDef(_ListProjectsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListProjectsPaginateResponseprojectsTypeDef = TypedDict(
    "_ListProjectsPaginateResponseprojectsTypeDef",
    {
        "arn": str,
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ListProjectsPaginateResponseprojectsTypeDef(_ListProjectsPaginateResponseprojectsTypeDef):
    """
    - *(dict) --*

      An object providing summary information for a particular project for an associated AWS account
      and region.
      - **arn** *(string) --*

        The ARN of the project.
    """


_ListProjectsPaginateResponseTypeDef = TypedDict(
    "_ListProjectsPaginateResponseTypeDef",
    {"projects": List[ListProjectsPaginateResponseprojectsTypeDef], "NextToken": str},
    total=False,
)


class ListProjectsPaginateResponseTypeDef(_ListProjectsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **projects** *(list) --*

        An object containing the list of projects.
        - *(dict) --*

          An object providing summary information for a particular project for an associated AWS
          account and region.
          - **arn** *(string) --*

            The ARN of the project.
    """
