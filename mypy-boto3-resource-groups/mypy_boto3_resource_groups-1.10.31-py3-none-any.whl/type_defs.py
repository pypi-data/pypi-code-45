"Main interface for resource-groups service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateGroupResourceQueryTypeDef",
    "ClientCreateGroupResponseGroupTypeDef",
    "ClientCreateGroupResponseResourceQueryTypeDef",
    "ClientCreateGroupResponseTypeDef",
    "ClientDeleteGroupResponseGroupTypeDef",
    "ClientDeleteGroupResponseTypeDef",
    "ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef",
    "ClientGetGroupQueryResponseGroupQueryTypeDef",
    "ClientGetGroupQueryResponseTypeDef",
    "ClientGetGroupResponseGroupTypeDef",
    "ClientGetGroupResponseTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientListGroupResourcesFiltersTypeDef",
    "ClientListGroupResourcesResponseQueryErrorsTypeDef",
    "ClientListGroupResourcesResponseResourceIdentifiersTypeDef",
    "ClientListGroupResourcesResponseTypeDef",
    "ClientListGroupsFiltersTypeDef",
    "ClientListGroupsResponseGroupIdentifiersTypeDef",
    "ClientListGroupsResponseGroupsTypeDef",
    "ClientListGroupsResponseTypeDef",
    "ClientSearchResourcesResourceQueryTypeDef",
    "ClientSearchResourcesResponseQueryErrorsTypeDef",
    "ClientSearchResourcesResponseResourceIdentifiersTypeDef",
    "ClientSearchResourcesResponseTypeDef",
    "ClientTagResponseTypeDef",
    "ClientUntagResponseTypeDef",
    "ClientUpdateGroupQueryResourceQueryTypeDef",
    "ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef",
    "ClientUpdateGroupQueryResponseGroupQueryTypeDef",
    "ClientUpdateGroupQueryResponseTypeDef",
    "ClientUpdateGroupResponseGroupTypeDef",
    "ClientUpdateGroupResponseTypeDef",
    "ListGroupResourcesPaginateFiltersTypeDef",
    "ListGroupResourcesPaginatePaginationConfigTypeDef",
    "ListGroupResourcesPaginateResponseQueryErrorsTypeDef",
    "ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef",
    "ListGroupResourcesPaginateResponseTypeDef",
    "ListGroupsPaginateFiltersTypeDef",
    "ListGroupsPaginatePaginationConfigTypeDef",
    "ListGroupsPaginateResponseGroupIdentifiersTypeDef",
    "ListGroupsPaginateResponseGroupsTypeDef",
    "ListGroupsPaginateResponseTypeDef",
    "SearchResourcesPaginatePaginationConfigTypeDef",
    "SearchResourcesPaginateResourceQueryTypeDef",
    "SearchResourcesPaginateResponseQueryErrorsTypeDef",
    "SearchResourcesPaginateResponseResourceIdentifiersTypeDef",
    "SearchResourcesPaginateResponseTypeDef",
)


_RequiredClientCreateGroupResourceQueryTypeDef = TypedDict(
    "_RequiredClientCreateGroupResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"]},
)
_OptionalClientCreateGroupResourceQueryTypeDef = TypedDict(
    "_OptionalClientCreateGroupResourceQueryTypeDef", {"Query": str}, total=False
)


class ClientCreateGroupResourceQueryTypeDef(
    _RequiredClientCreateGroupResourceQueryTypeDef, _OptionalClientCreateGroupResourceQueryTypeDef
):
    """
    The resource query that determines which AWS resources are members of this group.
    - **Type** *(string) --***[REQUIRED]**

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

        * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
        filters for resource types and tags, as supported by the AWS Tagging API `GetResources
        <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
        operation. If you specify more than one tag key, only resources that match all tag keys, and
        at least one value of each specified tag key, are returned in your query. If you specify
        more than one value for a tag key, a resource matches the filter if it has a tag key value
        that matches *any* of the specified values.
    """


_ClientCreateGroupResponseGroupTypeDef = TypedDict(
    "_ClientCreateGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientCreateGroupResponseGroupTypeDef(_ClientCreateGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      A full description of the resource group after it is created.
      - **GroupArn** *(string) --*

        The ARN of a resource group.
    """


_ClientCreateGroupResponseResourceQueryTypeDef = TypedDict(
    "_ClientCreateGroupResponseResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"], "Query": str},
    total=False,
)


class ClientCreateGroupResponseResourceQueryTypeDef(_ClientCreateGroupResponseResourceQueryTypeDef):
    pass


_ClientCreateGroupResponseTypeDef = TypedDict(
    "_ClientCreateGroupResponseTypeDef",
    {
        "Group": ClientCreateGroupResponseGroupTypeDef,
        "ResourceQuery": ClientCreateGroupResponseResourceQueryTypeDef,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientCreateGroupResponseTypeDef(_ClientCreateGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        A full description of the resource group after it is created.
        - **GroupArn** *(string) --*

          The ARN of a resource group.
    """


_ClientDeleteGroupResponseGroupTypeDef = TypedDict(
    "_ClientDeleteGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientDeleteGroupResponseGroupTypeDef(_ClientDeleteGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      A full description of the deleted resource group.
      - **GroupArn** *(string) --*

        The ARN of a resource group.
    """


_ClientDeleteGroupResponseTypeDef = TypedDict(
    "_ClientDeleteGroupResponseTypeDef",
    {"Group": ClientDeleteGroupResponseGroupTypeDef},
    total=False,
)


class ClientDeleteGroupResponseTypeDef(_ClientDeleteGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        A full description of the deleted resource group.
        - **GroupArn** *(string) --*

          The ARN of a resource group.
    """


_ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef = TypedDict(
    "_ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"], "Query": str},
    total=False,
)


class ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef(
    _ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef
):
    pass


_ClientGetGroupQueryResponseGroupQueryTypeDef = TypedDict(
    "_ClientGetGroupQueryResponseGroupQueryTypeDef",
    {"GroupName": str, "ResourceQuery": ClientGetGroupQueryResponseGroupQueryResourceQueryTypeDef},
    total=False,
)


class ClientGetGroupQueryResponseGroupQueryTypeDef(_ClientGetGroupQueryResponseGroupQueryTypeDef):
    """
    - **GroupQuery** *(dict) --*

      The resource query associated with the specified group.
      - **GroupName** *(string) --*

        The name of a resource group that is associated with a specific resource query.
    """


_ClientGetGroupQueryResponseTypeDef = TypedDict(
    "_ClientGetGroupQueryResponseTypeDef",
    {"GroupQuery": ClientGetGroupQueryResponseGroupQueryTypeDef},
    total=False,
)


class ClientGetGroupQueryResponseTypeDef(_ClientGetGroupQueryResponseTypeDef):
    """
    - *(dict) --*

      - **GroupQuery** *(dict) --*

        The resource query associated with the specified group.
        - **GroupName** *(string) --*

          The name of a resource group that is associated with a specific resource query.
    """


_ClientGetGroupResponseGroupTypeDef = TypedDict(
    "_ClientGetGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientGetGroupResponseGroupTypeDef(_ClientGetGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      A full description of the resource group.
      - **GroupArn** *(string) --*

        The ARN of a resource group.
    """


_ClientGetGroupResponseTypeDef = TypedDict(
    "_ClientGetGroupResponseTypeDef", {"Group": ClientGetGroupResponseGroupTypeDef}, total=False
)


class ClientGetGroupResponseTypeDef(_ClientGetGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        A full description of the resource group.
        - **GroupArn** *(string) --*

          The ARN of a resource group.
    """


_ClientGetTagsResponseTypeDef = TypedDict(
    "_ClientGetTagsResponseTypeDef", {"Arn": str, "Tags": Dict[str, str]}, total=False
)


class ClientGetTagsResponseTypeDef(_ClientGetTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The ARN of the tagged resource group.
    """


_RequiredClientListGroupResourcesFiltersTypeDef = TypedDict(
    "_RequiredClientListGroupResourcesFiltersTypeDef", {"Name": str}
)
_OptionalClientListGroupResourcesFiltersTypeDef = TypedDict(
    "_OptionalClientListGroupResourcesFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientListGroupResourcesFiltersTypeDef(
    _RequiredClientListGroupResourcesFiltersTypeDef, _OptionalClientListGroupResourcesFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to obtain more specific results from a list of
      resources.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case-sensitive.
    """


_ClientListGroupResourcesResponseQueryErrorsTypeDef = TypedDict(
    "_ClientListGroupResourcesResponseQueryErrorsTypeDef",
    {
        "ErrorCode": Literal["CLOUDFORMATION_STACK_INACTIVE", "CLOUDFORMATION_STACK_NOT_EXISTING"],
        "Message": str,
    },
    total=False,
)


class ClientListGroupResourcesResponseQueryErrorsTypeDef(
    _ClientListGroupResourcesResponseQueryErrorsTypeDef
):
    pass


_ClientListGroupResourcesResponseResourceIdentifiersTypeDef = TypedDict(
    "_ClientListGroupResourcesResponseResourceIdentifiersTypeDef",
    {"ResourceArn": str, "ResourceType": str},
    total=False,
)


class ClientListGroupResourcesResponseResourceIdentifiersTypeDef(
    _ClientListGroupResourcesResponseResourceIdentifiersTypeDef
):
    """
    - *(dict) --*

      The ARN of a resource, and its resource type.
      - **ResourceArn** *(string) --*

        The ARN of a resource.
    """


_ClientListGroupResourcesResponseTypeDef = TypedDict(
    "_ClientListGroupResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[ClientListGroupResourcesResponseResourceIdentifiersTypeDef],
        "NextToken": str,
        "QueryErrors": List[ClientListGroupResourcesResponseQueryErrorsTypeDef],
    },
    total=False,
)


class ClientListGroupResourcesResponseTypeDef(_ClientListGroupResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceIdentifiers** *(list) --*

        The ARNs and resource types of resources that are members of the group that you specified.
        - *(dict) --*

          The ARN of a resource, and its resource type.
          - **ResourceArn** *(string) --*

            The ARN of a resource.
    """


_RequiredClientListGroupsFiltersTypeDef = TypedDict(
    "_RequiredClientListGroupsFiltersTypeDef", {"Name": str}
)
_OptionalClientListGroupsFiltersTypeDef = TypedDict(
    "_OptionalClientListGroupsFiltersTypeDef", {"Values": List[str]}, total=False
)


class ClientListGroupsFiltersTypeDef(
    _RequiredClientListGroupsFiltersTypeDef, _OptionalClientListGroupsFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to obtain more specific results from a list of
      groups.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case-sensitive.
    """


_ClientListGroupsResponseGroupIdentifiersTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupIdentifiersTypeDef",
    {"GroupName": str, "GroupArn": str},
    total=False,
)


class ClientListGroupsResponseGroupIdentifiersTypeDef(
    _ClientListGroupsResponseGroupIdentifiersTypeDef
):
    """
    - *(dict) --*

      The ARN and group name of a group.
      - **GroupName** *(string) --*

        The name of a resource group.
    """


_ClientListGroupsResponseGroupsTypeDef = TypedDict(
    "_ClientListGroupsResponseGroupsTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientListGroupsResponseGroupsTypeDef(_ClientListGroupsResponseGroupsTypeDef):
    pass


_ClientListGroupsResponseTypeDef = TypedDict(
    "_ClientListGroupsResponseTypeDef",
    {
        "GroupIdentifiers": List[ClientListGroupsResponseGroupIdentifiersTypeDef],
        "Groups": List[ClientListGroupsResponseGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListGroupsResponseTypeDef(_ClientListGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **GroupIdentifiers** *(list) --*

        A list of GroupIdentifier objects. Each identifier is an object that contains both the
        GroupName and the GroupArn.
        - *(dict) --*

          The ARN and group name of a group.
          - **GroupName** *(string) --*

            The name of a resource group.
    """


_RequiredClientSearchResourcesResourceQueryTypeDef = TypedDict(
    "_RequiredClientSearchResourcesResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"]},
)
_OptionalClientSearchResourcesResourceQueryTypeDef = TypedDict(
    "_OptionalClientSearchResourcesResourceQueryTypeDef", {"Query": str}, total=False
)


class ClientSearchResourcesResourceQueryTypeDef(
    _RequiredClientSearchResourcesResourceQueryTypeDef,
    _OptionalClientSearchResourcesResourceQueryTypeDef,
):
    """
    The search query, using the same formats that are supported for resource group definition.
    - **Type** *(string) --***[REQUIRED]**

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

        * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
        filters for resource types and tags, as supported by the AWS Tagging API `GetResources
        <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
        operation. If you specify more than one tag key, only resources that match all tag keys, and
        at least one value of each specified tag key, are returned in your query. If you specify
        more than one value for a tag key, a resource matches the filter if it has a tag key value
        that matches *any* of the specified values.
    """


_ClientSearchResourcesResponseQueryErrorsTypeDef = TypedDict(
    "_ClientSearchResourcesResponseQueryErrorsTypeDef",
    {
        "ErrorCode": Literal["CLOUDFORMATION_STACK_INACTIVE", "CLOUDFORMATION_STACK_NOT_EXISTING"],
        "Message": str,
    },
    total=False,
)


class ClientSearchResourcesResponseQueryErrorsTypeDef(
    _ClientSearchResourcesResponseQueryErrorsTypeDef
):
    pass


_ClientSearchResourcesResponseResourceIdentifiersTypeDef = TypedDict(
    "_ClientSearchResourcesResponseResourceIdentifiersTypeDef",
    {"ResourceArn": str, "ResourceType": str},
    total=False,
)


class ClientSearchResourcesResponseResourceIdentifiersTypeDef(
    _ClientSearchResourcesResponseResourceIdentifiersTypeDef
):
    """
    - *(dict) --*

      The ARN of a resource, and its resource type.
      - **ResourceArn** *(string) --*

        The ARN of a resource.
    """


_ClientSearchResourcesResponseTypeDef = TypedDict(
    "_ClientSearchResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[ClientSearchResourcesResponseResourceIdentifiersTypeDef],
        "NextToken": str,
        "QueryErrors": List[ClientSearchResourcesResponseQueryErrorsTypeDef],
    },
    total=False,
)


class ClientSearchResourcesResponseTypeDef(_ClientSearchResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceIdentifiers** *(list) --*

        The ARNs and resource types of resources that are members of the group that you specified.
        - *(dict) --*

          The ARN of a resource, and its resource type.
          - **ResourceArn** *(string) --*

            The ARN of a resource.
    """


_ClientTagResponseTypeDef = TypedDict(
    "_ClientTagResponseTypeDef", {"Arn": str, "Tags": Dict[str, str]}, total=False
)


class ClientTagResponseTypeDef(_ClientTagResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The ARN of the tagged resource.
    """


_ClientUntagResponseTypeDef = TypedDict(
    "_ClientUntagResponseTypeDef", {"Arn": str, "Keys": List[str]}, total=False
)


class ClientUntagResponseTypeDef(_ClientUntagResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The ARN of the resource from which tags have been removed.
    """


_RequiredClientUpdateGroupQueryResourceQueryTypeDef = TypedDict(
    "_RequiredClientUpdateGroupQueryResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"]},
)
_OptionalClientUpdateGroupQueryResourceQueryTypeDef = TypedDict(
    "_OptionalClientUpdateGroupQueryResourceQueryTypeDef", {"Query": str}, total=False
)


class ClientUpdateGroupQueryResourceQueryTypeDef(
    _RequiredClientUpdateGroupQueryResourceQueryTypeDef,
    _OptionalClientUpdateGroupQueryResourceQueryTypeDef,
):
    """
    The resource query that determines which AWS resources are members of the resource group.
    - **Type** *(string) --***[REQUIRED]**

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

        * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
        filters for resource types and tags, as supported by the AWS Tagging API `GetResources
        <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
        operation. If you specify more than one tag key, only resources that match all tag keys, and
        at least one value of each specified tag key, are returned in your query. If you specify
        more than one value for a tag key, a resource matches the filter if it has a tag key value
        that matches *any* of the specified values.
    """


_ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef = TypedDict(
    "_ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"], "Query": str},
    total=False,
)


class ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef(
    _ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef
):
    pass


_ClientUpdateGroupQueryResponseGroupQueryTypeDef = TypedDict(
    "_ClientUpdateGroupQueryResponseGroupQueryTypeDef",
    {
        "GroupName": str,
        "ResourceQuery": ClientUpdateGroupQueryResponseGroupQueryResourceQueryTypeDef,
    },
    total=False,
)


class ClientUpdateGroupQueryResponseGroupQueryTypeDef(
    _ClientUpdateGroupQueryResponseGroupQueryTypeDef
):
    """
    - **GroupQuery** *(dict) --*

      The resource query associated with the resource group after the update.
      - **GroupName** *(string) --*

        The name of a resource group that is associated with a specific resource query.
    """


_ClientUpdateGroupQueryResponseTypeDef = TypedDict(
    "_ClientUpdateGroupQueryResponseTypeDef",
    {"GroupQuery": ClientUpdateGroupQueryResponseGroupQueryTypeDef},
    total=False,
)


class ClientUpdateGroupQueryResponseTypeDef(_ClientUpdateGroupQueryResponseTypeDef):
    """
    - *(dict) --*

      - **GroupQuery** *(dict) --*

        The resource query associated with the resource group after the update.
        - **GroupName** *(string) --*

          The name of a resource group that is associated with a specific resource query.
    """


_ClientUpdateGroupResponseGroupTypeDef = TypedDict(
    "_ClientUpdateGroupResponseGroupTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ClientUpdateGroupResponseGroupTypeDef(_ClientUpdateGroupResponseGroupTypeDef):
    """
    - **Group** *(dict) --*

      The full description of the resource group after it has been updated.
      - **GroupArn** *(string) --*

        The ARN of a resource group.
    """


_ClientUpdateGroupResponseTypeDef = TypedDict(
    "_ClientUpdateGroupResponseTypeDef",
    {"Group": ClientUpdateGroupResponseGroupTypeDef},
    total=False,
)


class ClientUpdateGroupResponseTypeDef(_ClientUpdateGroupResponseTypeDef):
    """
    - *(dict) --*

      - **Group** *(dict) --*

        The full description of the resource group after it has been updated.
        - **GroupArn** *(string) --*

          The ARN of a resource group.
    """


_RequiredListGroupResourcesPaginateFiltersTypeDef = TypedDict(
    "_RequiredListGroupResourcesPaginateFiltersTypeDef", {"Name": str}
)
_OptionalListGroupResourcesPaginateFiltersTypeDef = TypedDict(
    "_OptionalListGroupResourcesPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class ListGroupResourcesPaginateFiltersTypeDef(
    _RequiredListGroupResourcesPaginateFiltersTypeDef,
    _OptionalListGroupResourcesPaginateFiltersTypeDef,
):
    """
    - *(dict) --*

      A filter name and value pair that is used to obtain more specific results from a list of
      resources.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case-sensitive.
    """


_ListGroupResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupResourcesPaginatePaginationConfigTypeDef(
    _ListGroupResourcesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroupResourcesPaginateResponseQueryErrorsTypeDef = TypedDict(
    "_ListGroupResourcesPaginateResponseQueryErrorsTypeDef",
    {
        "ErrorCode": Literal["CLOUDFORMATION_STACK_INACTIVE", "CLOUDFORMATION_STACK_NOT_EXISTING"],
        "Message": str,
    },
    total=False,
)


class ListGroupResourcesPaginateResponseQueryErrorsTypeDef(
    _ListGroupResourcesPaginateResponseQueryErrorsTypeDef
):
    pass


_ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef = TypedDict(
    "_ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef",
    {"ResourceArn": str, "ResourceType": str},
    total=False,
)


class ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef(
    _ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef
):
    """
    - *(dict) --*

      The ARN of a resource, and its resource type.
      - **ResourceArn** *(string) --*

        The ARN of a resource.
    """


_ListGroupResourcesPaginateResponseTypeDef = TypedDict(
    "_ListGroupResourcesPaginateResponseTypeDef",
    {
        "ResourceIdentifiers": List[ListGroupResourcesPaginateResponseResourceIdentifiersTypeDef],
        "QueryErrors": List[ListGroupResourcesPaginateResponseQueryErrorsTypeDef],
    },
    total=False,
)


class ListGroupResourcesPaginateResponseTypeDef(_ListGroupResourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceIdentifiers** *(list) --*

        The ARNs and resource types of resources that are members of the group that you specified.
        - *(dict) --*

          The ARN of a resource, and its resource type.
          - **ResourceArn** *(string) --*

            The ARN of a resource.
    """


_RequiredListGroupsPaginateFiltersTypeDef = TypedDict(
    "_RequiredListGroupsPaginateFiltersTypeDef", {"Name": str}
)
_OptionalListGroupsPaginateFiltersTypeDef = TypedDict(
    "_OptionalListGroupsPaginateFiltersTypeDef", {"Values": List[str]}, total=False
)


class ListGroupsPaginateFiltersTypeDef(
    _RequiredListGroupsPaginateFiltersTypeDef, _OptionalListGroupsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A filter name and value pair that is used to obtain more specific results from a list of
      groups.
      - **Name** *(string) --***[REQUIRED]**

        The name of the filter. Filter names are case-sensitive.
    """


_ListGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGroupsPaginatePaginationConfigTypeDef(_ListGroupsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListGroupsPaginateResponseGroupIdentifiersTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupIdentifiersTypeDef",
    {"GroupName": str, "GroupArn": str},
    total=False,
)


class ListGroupsPaginateResponseGroupIdentifiersTypeDef(
    _ListGroupsPaginateResponseGroupIdentifiersTypeDef
):
    """
    - *(dict) --*

      The ARN and group name of a group.
      - **GroupName** *(string) --*

        The name of a resource group.
    """


_ListGroupsPaginateResponseGroupsTypeDef = TypedDict(
    "_ListGroupsPaginateResponseGroupsTypeDef",
    {"GroupArn": str, "Name": str, "Description": str},
    total=False,
)


class ListGroupsPaginateResponseGroupsTypeDef(_ListGroupsPaginateResponseGroupsTypeDef):
    pass


_ListGroupsPaginateResponseTypeDef = TypedDict(
    "_ListGroupsPaginateResponseTypeDef",
    {
        "GroupIdentifiers": List[ListGroupsPaginateResponseGroupIdentifiersTypeDef],
        "Groups": List[ListGroupsPaginateResponseGroupsTypeDef],
    },
    total=False,
)


class ListGroupsPaginateResponseTypeDef(_ListGroupsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **GroupIdentifiers** *(list) --*

        A list of GroupIdentifier objects. Each identifier is an object that contains both the
        GroupName and the GroupArn.
        - *(dict) --*

          The ARN and group name of a group.
          - **GroupName** *(string) --*

            The name of a resource group.
    """


_SearchResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchResourcesPaginatePaginationConfigTypeDef(
    _SearchResourcesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_RequiredSearchResourcesPaginateResourceQueryTypeDef = TypedDict(
    "_RequiredSearchResourcesPaginateResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"]},
)
_OptionalSearchResourcesPaginateResourceQueryTypeDef = TypedDict(
    "_OptionalSearchResourcesPaginateResourceQueryTypeDef", {"Query": str}, total=False
)


class SearchResourcesPaginateResourceQueryTypeDef(
    _RequiredSearchResourcesPaginateResourceQueryTypeDef,
    _OptionalSearchResourcesPaginateResourceQueryTypeDef,
):
    """
    The search query, using the same formats that are supported for resource group definition.
    - **Type** *(string) --***[REQUIRED]**

      The type of the query. The valid values in this release are ``TAG_FILTERS_1_0`` and
      ``CLOUDFORMATION_STACK_1_0`` .

        * ``TAG_FILTERS_1_0:`` * A JSON syntax that lets you specify a collection of simple tag
        filters for resource types and tags, as supported by the AWS Tagging API `GetResources
        <https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html>`__
        operation. If you specify more than one tag key, only resources that match all tag keys, and
        at least one value of each specified tag key, are returned in your query. If you specify
        more than one value for a tag key, a resource matches the filter if it has a tag key value
        that matches *any* of the specified values.
    """


_SearchResourcesPaginateResponseQueryErrorsTypeDef = TypedDict(
    "_SearchResourcesPaginateResponseQueryErrorsTypeDef",
    {
        "ErrorCode": Literal["CLOUDFORMATION_STACK_INACTIVE", "CLOUDFORMATION_STACK_NOT_EXISTING"],
        "Message": str,
    },
    total=False,
)


class SearchResourcesPaginateResponseQueryErrorsTypeDef(
    _SearchResourcesPaginateResponseQueryErrorsTypeDef
):
    pass


_SearchResourcesPaginateResponseResourceIdentifiersTypeDef = TypedDict(
    "_SearchResourcesPaginateResponseResourceIdentifiersTypeDef",
    {"ResourceArn": str, "ResourceType": str},
    total=False,
)


class SearchResourcesPaginateResponseResourceIdentifiersTypeDef(
    _SearchResourcesPaginateResponseResourceIdentifiersTypeDef
):
    """
    - *(dict) --*

      The ARN of a resource, and its resource type.
      - **ResourceArn** *(string) --*

        The ARN of a resource.
    """


_SearchResourcesPaginateResponseTypeDef = TypedDict(
    "_SearchResourcesPaginateResponseTypeDef",
    {
        "ResourceIdentifiers": List[SearchResourcesPaginateResponseResourceIdentifiersTypeDef],
        "QueryErrors": List[SearchResourcesPaginateResponseQueryErrorsTypeDef],
    },
    total=False,
)


class SearchResourcesPaginateResponseTypeDef(_SearchResourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceIdentifiers** *(list) --*

        The ARNs and resource types of resources that are members of the group that you specified.
        - *(dict) --*

          The ARN of a resource, and its resource type.
          - **ResourceArn** *(string) --*

            The ARN of a resource.
    """
