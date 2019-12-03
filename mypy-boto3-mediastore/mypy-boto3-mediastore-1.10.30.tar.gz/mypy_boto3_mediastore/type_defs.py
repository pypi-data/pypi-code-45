"Main interface for mediastore service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateContainerResponseContainerTypeDef",
    "ClientCreateContainerResponseTypeDef",
    "ClientCreateContainerTagsTypeDef",
    "ClientDescribeContainerResponseContainerTypeDef",
    "ClientDescribeContainerResponseTypeDef",
    "ClientGetContainerPolicyResponseTypeDef",
    "ClientGetCorsPolicyResponseCorsPolicyTypeDef",
    "ClientGetCorsPolicyResponseTypeDef",
    "ClientGetLifecyclePolicyResponseTypeDef",
    "ClientListContainersResponseContainersTypeDef",
    "ClientListContainersResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutCorsPolicyCorsPolicyTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ListContainersPaginatePaginationConfigTypeDef",
    "ListContainersPaginateResponseContainersTypeDef",
    "ListContainersPaginateResponseTypeDef",
)


_ClientCreateContainerResponseContainerTypeDef = TypedDict(
    "_ClientCreateContainerResponseContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": Literal["ACTIVE", "CREATING", "DELETING"],
        "AccessLoggingEnabled": bool,
    },
    total=False,
)


class ClientCreateContainerResponseContainerTypeDef(_ClientCreateContainerResponseContainerTypeDef):
    """
    - **Container** *(dict) --*

      ContainerARN: The Amazon Resource Name (ARN) of the newly created container. The ARN has the
      following format: arn:aws:<region>:<account that owns this container>:container/<name of
      container>. For example: arn:aws:mediastore:us-west-2:111122223333:container/movies
      ContainerName: The container name as specified in the request.
      CreationTime: Unix time stamp.
      Status: The status of container creation or deletion. The status is one of the following:
      ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container, the
      status is ``CREATING`` . When an endpoint is available, the status changes to ``ACTIVE`` .
      The return value does not include the container's endpoint. To make downstream requests, you
      must obtain this value by using  DescribeContainer or  ListContainers .
      - **Endpoint** *(string) --*

        The DNS endpoint of the container. Use the endpoint to identify the specific container when
        sending requests to the data plane. The service assigns this value when the container is
        created. Once the value has been assigned, it does not change.
    """


_ClientCreateContainerResponseTypeDef = TypedDict(
    "_ClientCreateContainerResponseTypeDef",
    {"Container": ClientCreateContainerResponseContainerTypeDef},
    total=False,
)


class ClientCreateContainerResponseTypeDef(_ClientCreateContainerResponseTypeDef):
    """
    - *(dict) --*

      - **Container** *(dict) --*

        ContainerARN: The Amazon Resource Name (ARN) of the newly created container. The ARN has the
        following format: arn:aws:<region>:<account that owns this container>:container/<name of
        container>. For example: arn:aws:mediastore:us-west-2:111122223333:container/movies
        ContainerName: The container name as specified in the request.
        CreationTime: Unix time stamp.
        Status: The status of container creation or deletion. The status is one of the following:
        ``CREATING`` , ``ACTIVE`` , or ``DELETING`` . While the service is creating the container,
        the status is ``CREATING`` . When an endpoint is available, the status changes to ``ACTIVE``
        .
        The return value does not include the container's endpoint. To make downstream requests, you
        must obtain this value by using  DescribeContainer or  ListContainers .
        - **Endpoint** *(string) --*

          The DNS endpoint of the container. Use the endpoint to identify the specific container
          when sending requests to the data plane. The service assigns this value when the container
          is created. Once the value has been assigned, it does not change.
    """


_RequiredClientCreateContainerTagsTypeDef = TypedDict(
    "_RequiredClientCreateContainerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateContainerTagsTypeDef = TypedDict(
    "_OptionalClientCreateContainerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateContainerTagsTypeDef(
    _RequiredClientCreateContainerTagsTypeDef, _OptionalClientCreateContainerTagsTypeDef
):
    """
    - *(dict) --*

      A collection of tags associated with a container. Each tag consists of a key:value pair, which
      can be anything you define. Typically, the tag key represents a category (such as
      "environment") and the tag value represents a specific value within that category (such as
      "test," "development," or "production"). You can add up to 50 tags to each container. For more
      information about tagging, including naming and usage conventions, see `Tagging Resources in
      MediaStore <https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html>`__ .
      - **Key** *(string) --***[REQUIRED]**

        Part of the key:value pair that defines a tag. You can use a tag key to describe a category
        of information, such as "customer." Tag keys are case-sensitive.
    """


_ClientDescribeContainerResponseContainerTypeDef = TypedDict(
    "_ClientDescribeContainerResponseContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": Literal["ACTIVE", "CREATING", "DELETING"],
        "AccessLoggingEnabled": bool,
    },
    total=False,
)


class ClientDescribeContainerResponseContainerTypeDef(
    _ClientDescribeContainerResponseContainerTypeDef
):
    """
    - **Container** *(dict) --*

      The name of the queried container.
      - **Endpoint** *(string) --*

        The DNS endpoint of the container. Use the endpoint to identify the specific container when
        sending requests to the data plane. The service assigns this value when the container is
        created. Once the value has been assigned, it does not change.
    """


_ClientDescribeContainerResponseTypeDef = TypedDict(
    "_ClientDescribeContainerResponseTypeDef",
    {"Container": ClientDescribeContainerResponseContainerTypeDef},
    total=False,
)


class ClientDescribeContainerResponseTypeDef(_ClientDescribeContainerResponseTypeDef):
    """
    - *(dict) --*

      - **Container** *(dict) --*

        The name of the queried container.
        - **Endpoint** *(string) --*

          The DNS endpoint of the container. Use the endpoint to identify the specific container
          when sending requests to the data plane. The service assigns this value when the container
          is created. Once the value has been assigned, it does not change.
    """


_ClientGetContainerPolicyResponseTypeDef = TypedDict(
    "_ClientGetContainerPolicyResponseTypeDef", {"Policy": str}, total=False
)


class ClientGetContainerPolicyResponseTypeDef(_ClientGetContainerPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(string) --*

        The contents of the access policy.
    """


_ClientGetCorsPolicyResponseCorsPolicyTypeDef = TypedDict(
    "_ClientGetCorsPolicyResponseCorsPolicyTypeDef",
    {
        "AllowedOrigins": List[str],
        "AllowedMethods": List[Literal["PUT", "GET", "DELETE", "HEAD"]],
        "AllowedHeaders": List[str],
        "MaxAgeSeconds": int,
        "ExposeHeaders": List[str],
    },
    total=False,
)


class ClientGetCorsPolicyResponseCorsPolicyTypeDef(_ClientGetCorsPolicyResponseCorsPolicyTypeDef):
    """
    - *(dict) --*

      A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule
      applies, the service uses the first applicable rule listed.
      - **AllowedOrigins** *(list) --*

        One or more response headers that you want users to be able to access from their
        applications (for example, from a JavaScript ``XMLHttpRequest`` object).
        Each CORS rule must have at least one ``AllowedOrigins`` element. The string value can
        include only one wildcard character (*), for example, http://*.example.com. Additionally,
        you can specify only one wildcard character to allow cross-origin access for all origins.
        - *(string) --*
    """


_ClientGetCorsPolicyResponseTypeDef = TypedDict(
    "_ClientGetCorsPolicyResponseTypeDef",
    {"CorsPolicy": List[ClientGetCorsPolicyResponseCorsPolicyTypeDef]},
    total=False,
)


class ClientGetCorsPolicyResponseTypeDef(_ClientGetCorsPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **CorsPolicy** *(list) --*

        The CORS policy assigned to the container.
        - *(dict) --*

          A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one
          rule applies, the service uses the first applicable rule listed.
          - **AllowedOrigins** *(list) --*

            One or more response headers that you want users to be able to access from their
            applications (for example, from a JavaScript ``XMLHttpRequest`` object).
            Each CORS rule must have at least one ``AllowedOrigins`` element. The string value can
            include only one wildcard character (*), for example, http://*.example.com.
            Additionally, you can specify only one wildcard character to allow cross-origin access
            for all origins.
            - *(string) --*
    """


_ClientGetLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponseTypeDef", {"LifecyclePolicy": str}, total=False
)


class ClientGetLifecyclePolicyResponseTypeDef(_ClientGetLifecyclePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **LifecyclePolicy** *(string) --*

        The object lifecycle policy that is assigned to the container.
    """


_ClientListContainersResponseContainersTypeDef = TypedDict(
    "_ClientListContainersResponseContainersTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": Literal["ACTIVE", "CREATING", "DELETING"],
        "AccessLoggingEnabled": bool,
    },
    total=False,
)


class ClientListContainersResponseContainersTypeDef(_ClientListContainersResponseContainersTypeDef):
    """
    - *(dict) --*

      This section describes operations that you can perform on an AWS Elemental MediaStore
      container.
      - **Endpoint** *(string) --*

        The DNS endpoint of the container. Use the endpoint to identify the specific container when
        sending requests to the data plane. The service assigns this value when the container is
        created. Once the value has been assigned, it does not change.
    """


_ClientListContainersResponseTypeDef = TypedDict(
    "_ClientListContainersResponseTypeDef",
    {"Containers": List[ClientListContainersResponseContainersTypeDef], "NextToken": str},
    total=False,
)


class ClientListContainersResponseTypeDef(_ClientListContainersResponseTypeDef):
    """
    - *(dict) --*

      - **Containers** *(list) --*

        The names of the containers.
        - *(dict) --*

          This section describes operations that you can perform on an AWS Elemental MediaStore
          container.
          - **Endpoint** *(string) --*

            The DNS endpoint of the container. Use the endpoint to identify the specific container
            when sending requests to the data plane. The service assigns this value when the
            container is created. Once the value has been assigned, it does not change.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      A collection of tags associated with a container. Each tag consists of a key:value pair, which
      can be anything you define. Typically, the tag key represents a category (such as
      "environment") and the tag value represents a specific value within that category (such as
      "test," "development," or "production"). You can add up to 50 tags to each container. For more
      information about tagging, including naming and usage conventions, see `Tagging Resources in
      MediaStore <https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html>`__ .
      - **Key** *(string) --*

        Part of the key:value pair that defines a tag. You can use a tag key to describe a category
        of information, such as "customer." Tag keys are case-sensitive.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        An array of key:value pairs that are assigned to the container.
        - *(dict) --*

          A collection of tags associated with a container. Each tag consists of a key:value pair,
          which can be anything you define. Typically, the tag key represents a category (such as
          "environment") and the tag value represents a specific value within that category (such as
          "test," "development," or "production"). You can add up to 50 tags to each container. For
          more information about tagging, including naming and usage conventions, see `Tagging
          Resources in MediaStore <https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html>`__
          .
          - **Key** *(string) --*

            Part of the key:value pair that defines a tag. You can use a tag key to describe a
            category of information, such as "customer." Tag keys are case-sensitive.
    """


_RequiredClientPutCorsPolicyCorsPolicyTypeDef = TypedDict(
    "_RequiredClientPutCorsPolicyCorsPolicyTypeDef", {"AllowedOrigins": List[str]}
)
_OptionalClientPutCorsPolicyCorsPolicyTypeDef = TypedDict(
    "_OptionalClientPutCorsPolicyCorsPolicyTypeDef",
    {
        "AllowedMethods": List[Literal["PUT", "GET", "DELETE", "HEAD"]],
        "AllowedHeaders": List[str],
        "MaxAgeSeconds": int,
        "ExposeHeaders": List[str],
    },
    total=False,
)


class ClientPutCorsPolicyCorsPolicyTypeDef(
    _RequiredClientPutCorsPolicyCorsPolicyTypeDef, _OptionalClientPutCorsPolicyCorsPolicyTypeDef
):
    """
    - *(dict) --*

      A rule for a CORS policy. You can add up to 100 rules to a CORS policy. If more than one rule
      applies, the service uses the first applicable rule listed.
      - **AllowedOrigins** *(list) --***[REQUIRED]**

        One or more response headers that you want users to be able to access from their
        applications (for example, from a JavaScript ``XMLHttpRequest`` object).
        Each CORS rule must have at least one ``AllowedOrigins`` element. The string value can
        include only one wildcard character (*), for example, http://*.example.com. Additionally,
        you can specify only one wildcard character to allow cross-origin access for all origins.
        - *(string) --*
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      A collection of tags associated with a container. Each tag consists of a key:value pair, which
      can be anything you define. Typically, the tag key represents a category (such as
      "environment") and the tag value represents a specific value within that category (such as
      "test," "development," or "production"). You can add up to 50 tags to each container. For more
      information about tagging, including naming and usage conventions, see `Tagging Resources in
      MediaStore <https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html>`__ .
      - **Key** *(string) --***[REQUIRED]**

        Part of the key:value pair that defines a tag. You can use a tag key to describe a category
        of information, such as "customer." Tag keys are case-sensitive.
    """


_ListContainersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListContainersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListContainersPaginatePaginationConfigTypeDef(_ListContainersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListContainersPaginateResponseContainersTypeDef = TypedDict(
    "_ListContainersPaginateResponseContainersTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": Literal["ACTIVE", "CREATING", "DELETING"],
        "AccessLoggingEnabled": bool,
    },
    total=False,
)


class ListContainersPaginateResponseContainersTypeDef(
    _ListContainersPaginateResponseContainersTypeDef
):
    """
    - *(dict) --*

      This section describes operations that you can perform on an AWS Elemental MediaStore
      container.
      - **Endpoint** *(string) --*

        The DNS endpoint of the container. Use the endpoint to identify the specific container when
        sending requests to the data plane. The service assigns this value when the container is
        created. Once the value has been assigned, it does not change.
    """


_ListContainersPaginateResponseTypeDef = TypedDict(
    "_ListContainersPaginateResponseTypeDef",
    {"Containers": List[ListContainersPaginateResponseContainersTypeDef]},
    total=False,
)


class ListContainersPaginateResponseTypeDef(_ListContainersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Containers** *(list) --*

        The names of the containers.
        - *(dict) --*

          This section describes operations that you can perform on an AWS Elemental MediaStore
          container.
          - **Endpoint** *(string) --*

            The DNS endpoint of the container. Use the endpoint to identify the specific container
            when sending requests to the data plane. The service assigns this value when the
            container is created. Once the value has been assigned, it does not change.
    """
