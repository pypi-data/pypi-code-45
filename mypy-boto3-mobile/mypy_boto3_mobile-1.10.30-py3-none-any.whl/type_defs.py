"Main interface for mobile service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateProjectResponsedetailsresourcesTypeDef",
    "ClientCreateProjectResponsedetailsTypeDef",
    "ClientCreateProjectResponseTypeDef",
    "ClientDeleteProjectResponsedeletedResourcesTypeDef",
    "ClientDeleteProjectResponseorphanedResourcesTypeDef",
    "ClientDeleteProjectResponseTypeDef",
    "ClientDescribeBundleResponsedetailsTypeDef",
    "ClientDescribeBundleResponseTypeDef",
    "ClientDescribeProjectResponsedetailsresourcesTypeDef",
    "ClientDescribeProjectResponsedetailsTypeDef",
    "ClientDescribeProjectResponseTypeDef",
    "ClientExportBundleResponseTypeDef",
    "ClientExportProjectResponseTypeDef",
    "ClientListBundlesResponsebundleListTypeDef",
    "ClientListBundlesResponseTypeDef",
    "ClientListProjectsResponseprojectsTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientUpdateProjectResponsedetailsresourcesTypeDef",
    "ClientUpdateProjectResponsedetailsTypeDef",
    "ClientUpdateProjectResponseTypeDef",
    "ListBundlesPaginatePaginationConfigTypeDef",
    "ListBundlesPaginateResponsebundleListTypeDef",
    "ListBundlesPaginateResponseTypeDef",
    "ListProjectsPaginatePaginationConfigTypeDef",
    "ListProjectsPaginateResponseprojectsTypeDef",
    "ListProjectsPaginateResponseTypeDef",
)


_ClientCreateProjectResponsedetailsresourcesTypeDef = TypedDict(
    "_ClientCreateProjectResponsedetailsresourcesTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)


class ClientCreateProjectResponsedetailsresourcesTypeDef(
    _ClientCreateProjectResponsedetailsresourcesTypeDef
):
    pass


_ClientCreateProjectResponsedetailsTypeDef = TypedDict(
    "_ClientCreateProjectResponsedetailsTypeDef",
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


class ClientCreateProjectResponsedetailsTypeDef(_ClientCreateProjectResponsedetailsTypeDef):
    """
    - **details** *(dict) --*

      Detailed information about the created AWS Mobile Hub project.
      - **name** *(string) --*

        Name of the project.
    """


_ClientCreateProjectResponseTypeDef = TypedDict(
    "_ClientCreateProjectResponseTypeDef",
    {"details": ClientCreateProjectResponsedetailsTypeDef},
    total=False,
)


class ClientCreateProjectResponseTypeDef(_ClientCreateProjectResponseTypeDef):
    """
    - *(dict) --*

      Result structure used in response to a request to create a project.
      - **details** *(dict) --*

        Detailed information about the created AWS Mobile Hub project.
        - **name** *(string) --*

          Name of the project.
    """


_ClientDeleteProjectResponsedeletedResourcesTypeDef = TypedDict(
    "_ClientDeleteProjectResponsedeletedResourcesTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)


class ClientDeleteProjectResponsedeletedResourcesTypeDef(
    _ClientDeleteProjectResponsedeletedResourcesTypeDef
):
    """
    - *(dict) --*

      Information about an instance of an AWS resource associated with a project.
      - **type** *(string) --*

        Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).
    """


_ClientDeleteProjectResponseorphanedResourcesTypeDef = TypedDict(
    "_ClientDeleteProjectResponseorphanedResourcesTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)


class ClientDeleteProjectResponseorphanedResourcesTypeDef(
    _ClientDeleteProjectResponseorphanedResourcesTypeDef
):
    pass


_ClientDeleteProjectResponseTypeDef = TypedDict(
    "_ClientDeleteProjectResponseTypeDef",
    {
        "deletedResources": List[ClientDeleteProjectResponsedeletedResourcesTypeDef],
        "orphanedResources": List[ClientDeleteProjectResponseorphanedResourcesTypeDef],
    },
    total=False,
)


class ClientDeleteProjectResponseTypeDef(_ClientDeleteProjectResponseTypeDef):
    """
    - *(dict) --*

      Result structure used in response to request to delete a project.
      - **deletedResources** *(list) --*

        Resources which were deleted.
        - *(dict) --*

          Information about an instance of an AWS resource associated with a project.
          - **type** *(string) --*

            Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).
    """


_ClientDescribeBundleResponsedetailsTypeDef = TypedDict(
    "_ClientDescribeBundleResponsedetailsTypeDef",
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


class ClientDescribeBundleResponsedetailsTypeDef(_ClientDescribeBundleResponsedetailsTypeDef):
    """
    - **details** *(dict) --*

      The details of the bundle.
      - **bundleId** *(string) --*

        Unique bundle identifier.
    """


_ClientDescribeBundleResponseTypeDef = TypedDict(
    "_ClientDescribeBundleResponseTypeDef",
    {"details": ClientDescribeBundleResponsedetailsTypeDef},
    total=False,
)


class ClientDescribeBundleResponseTypeDef(_ClientDescribeBundleResponseTypeDef):
    """
    - *(dict) --*

      Result structure contains the details of the bundle.
      - **details** *(dict) --*

        The details of the bundle.
        - **bundleId** *(string) --*

          Unique bundle identifier.
    """


_ClientDescribeProjectResponsedetailsresourcesTypeDef = TypedDict(
    "_ClientDescribeProjectResponsedetailsresourcesTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)


class ClientDescribeProjectResponsedetailsresourcesTypeDef(
    _ClientDescribeProjectResponsedetailsresourcesTypeDef
):
    pass


_ClientDescribeProjectResponsedetailsTypeDef = TypedDict(
    "_ClientDescribeProjectResponsedetailsTypeDef",
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


class ClientDescribeProjectResponsedetailsTypeDef(_ClientDescribeProjectResponsedetailsTypeDef):
    """
    - **details** *(dict) --*

      Detailed information about an AWS Mobile Hub project.
      - **name** *(string) --*

        Name of the project.
    """


_ClientDescribeProjectResponseTypeDef = TypedDict(
    "_ClientDescribeProjectResponseTypeDef",
    {"details": ClientDescribeProjectResponsedetailsTypeDef},
    total=False,
)


class ClientDescribeProjectResponseTypeDef(_ClientDescribeProjectResponseTypeDef):
    """
    - *(dict) --*

      Result structure used for requests of project details.
      - **details** *(dict) --*

        Detailed information about an AWS Mobile Hub project.
        - **name** *(string) --*

          Name of the project.
    """


_ClientExportBundleResponseTypeDef = TypedDict(
    "_ClientExportBundleResponseTypeDef", {"downloadUrl": str}, total=False
)


class ClientExportBundleResponseTypeDef(_ClientExportBundleResponseTypeDef):
    """
    - *(dict) --*

      Result structure which contains link to download custom-generated SDK and tool packages used
      to integrate mobile web or app clients with backed AWS resources.
      - **downloadUrl** *(string) --*

        URL which contains the custom-generated SDK and tool packages used to integrate the client
        mobile app or web app with the AWS resources created by the AWS Mobile Hub project.
    """


_ClientExportProjectResponseTypeDef = TypedDict(
    "_ClientExportProjectResponseTypeDef",
    {"downloadUrl": str, "shareUrl": str, "snapshotId": str},
    total=False,
)


class ClientExportProjectResponseTypeDef(_ClientExportProjectResponseTypeDef):
    """
    - *(dict) --*

      Result structure used for requests to export project configuration details.
      - **downloadUrl** *(string) --*

        URL which can be used to download the exported project configuation file(s).
    """


_ClientListBundlesResponsebundleListTypeDef = TypedDict(
    "_ClientListBundlesResponsebundleListTypeDef",
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


class ClientListBundlesResponsebundleListTypeDef(_ClientListBundlesResponsebundleListTypeDef):
    """
    - *(dict) --*

      The details of the bundle.
      - **bundleId** *(string) --*

        Unique bundle identifier.
    """


_ClientListBundlesResponseTypeDef = TypedDict(
    "_ClientListBundlesResponseTypeDef",
    {"bundleList": List[ClientListBundlesResponsebundleListTypeDef], "nextToken": str},
    total=False,
)


class ClientListBundlesResponseTypeDef(_ClientListBundlesResponseTypeDef):
    """
    - *(dict) --*

      Result structure contains a list of all available bundles with details.
      - **bundleList** *(list) --*

        A list of bundles.
        - *(dict) --*

          The details of the bundle.
          - **bundleId** *(string) --*

            Unique bundle identifier.
    """


_ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "_ClientListProjectsResponseprojectsTypeDef", {"name": str, "projectId": str}, total=False
)


class ClientListProjectsResponseprojectsTypeDef(_ClientListProjectsResponseprojectsTypeDef):
    """
    - *(dict) --*

      Summary information about an AWS Mobile Hub project.
      - **name** *(string) --*

        Name of the project.
    """


_ClientListProjectsResponseTypeDef = TypedDict(
    "_ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)


class ClientListProjectsResponseTypeDef(_ClientListProjectsResponseTypeDef):
    """
    - *(dict) --*

      Result structure used for requests to list projects in AWS Mobile Hub.
      - **projects** *(list) --*

        List of projects.
        - *(dict) --*

          Summary information about an AWS Mobile Hub project.
          - **name** *(string) --*

            Name of the project.
    """


_ClientUpdateProjectResponsedetailsresourcesTypeDef = TypedDict(
    "_ClientUpdateProjectResponsedetailsresourcesTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)


class ClientUpdateProjectResponsedetailsresourcesTypeDef(
    _ClientUpdateProjectResponsedetailsresourcesTypeDef
):
    pass


_ClientUpdateProjectResponsedetailsTypeDef = TypedDict(
    "_ClientUpdateProjectResponsedetailsTypeDef",
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


class ClientUpdateProjectResponsedetailsTypeDef(_ClientUpdateProjectResponsedetailsTypeDef):
    """
    - **details** *(dict) --*

      Detailed information about the updated AWS Mobile Hub project.
      - **name** *(string) --*

        Name of the project.
    """


_ClientUpdateProjectResponseTypeDef = TypedDict(
    "_ClientUpdateProjectResponseTypeDef",
    {"details": ClientUpdateProjectResponsedetailsTypeDef},
    total=False,
)


class ClientUpdateProjectResponseTypeDef(_ClientUpdateProjectResponseTypeDef):
    """
    - *(dict) --*

      Result structure used for requests to updated project configuration.
      - **details** *(dict) --*

        Detailed information about the updated AWS Mobile Hub project.
        - **name** *(string) --*

          Name of the project.
    """


_ListBundlesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBundlesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBundlesPaginatePaginationConfigTypeDef(_ListBundlesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBundlesPaginateResponsebundleListTypeDef = TypedDict(
    "_ListBundlesPaginateResponsebundleListTypeDef",
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


class ListBundlesPaginateResponsebundleListTypeDef(_ListBundlesPaginateResponsebundleListTypeDef):
    """
    - *(dict) --*

      The details of the bundle.
      - **bundleId** *(string) --*

        Unique bundle identifier.
    """


_ListBundlesPaginateResponseTypeDef = TypedDict(
    "_ListBundlesPaginateResponseTypeDef",
    {"bundleList": List[ListBundlesPaginateResponsebundleListTypeDef], "NextToken": str},
    total=False,
)


class ListBundlesPaginateResponseTypeDef(_ListBundlesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Result structure contains a list of all available bundles with details.
      - **bundleList** *(list) --*

        A list of bundles.
        - *(dict) --*

          The details of the bundle.
          - **bundleId** *(string) --*

            Unique bundle identifier.
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
    "_ListProjectsPaginateResponseprojectsTypeDef", {"name": str, "projectId": str}, total=False
)


class ListProjectsPaginateResponseprojectsTypeDef(_ListProjectsPaginateResponseprojectsTypeDef):
    """
    - *(dict) --*

      Summary information about an AWS Mobile Hub project.
      - **name** *(string) --*

        Name of the project.
    """


_ListProjectsPaginateResponseTypeDef = TypedDict(
    "_ListProjectsPaginateResponseTypeDef",
    {"projects": List[ListProjectsPaginateResponseprojectsTypeDef], "NextToken": str},
    total=False,
)


class ListProjectsPaginateResponseTypeDef(_ListProjectsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Result structure used for requests to list projects in AWS Mobile Hub.
      - **projects** *(list) --*

        List of projects.
        - *(dict) --*

          Summary information about an AWS Mobile Hub project.
          - **name** *(string) --*

            Name of the project.
    """
