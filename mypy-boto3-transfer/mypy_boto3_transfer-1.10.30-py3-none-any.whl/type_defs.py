"Main interface for transfer service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateServerEndpointDetailsTypeDef",
    "ClientCreateServerIdentityProviderDetailsTypeDef",
    "ClientCreateServerResponseTypeDef",
    "ClientCreateServerTagsTypeDef",
    "ClientCreateUserHomeDirectoryMappingsTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientCreateUserTagsTypeDef",
    "ClientDescribeServerResponseServerEndpointDetailsTypeDef",
    "ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef",
    "ClientDescribeServerResponseServerTagsTypeDef",
    "ClientDescribeServerResponseServerTypeDef",
    "ClientDescribeServerResponseTypeDef",
    "ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef",
    "ClientDescribeUserResponseUserSshPublicKeysTypeDef",
    "ClientDescribeUserResponseUserTagsTypeDef",
    "ClientDescribeUserResponseUserTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientImportSshPublicKeyResponseTypeDef",
    "ClientListServersResponseServersTypeDef",
    "ClientListServersResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUsersResponseUsersTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientTestIdentityProviderResponseTypeDef",
    "ClientUpdateServerEndpointDetailsTypeDef",
    "ClientUpdateServerIdentityProviderDetailsTypeDef",
    "ClientUpdateServerResponseTypeDef",
    "ClientUpdateUserHomeDirectoryMappingsTypeDef",
    "ClientUpdateUserResponseTypeDef",
    "ListServersPaginatePaginationConfigTypeDef",
    "ListServersPaginateResponseServersTypeDef",
    "ListServersPaginateResponseTypeDef",
)


_ClientCreateServerEndpointDetailsTypeDef = TypedDict(
    "_ClientCreateServerEndpointDetailsTypeDef", {"VpcEndpointId": str}, total=False
)


class ClientCreateServerEndpointDetailsTypeDef(_ClientCreateServerEndpointDetailsTypeDef):
    """
    The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP
    server. This parameter is required when you specify a value for the ``EndpointType`` parameter.
    - **VpcEndpointId** *(string) --*

      The ID of the VPC endpoint.
    """


_ClientCreateServerIdentityProviderDetailsTypeDef = TypedDict(
    "_ClientCreateServerIdentityProviderDetailsTypeDef",
    {"Url": str, "InvocationRole": str},
    total=False,
)


class ClientCreateServerIdentityProviderDetailsTypeDef(
    _ClientCreateServerIdentityProviderDetailsTypeDef
):
    """
    This parameter is required when the ``IdentityProviderType`` is set to ``API_GATEWAY`` . Accepts
    an array containing all of the information required to call a customer-supplied authentication
    API, including the API Gateway URL. This property is not required when the
    ``IdentityProviderType`` is set to ``SERVICE_MANAGED`` .
    - **Url** *(string) --*

      The ``Url`` parameter provides contains the location of the service endpoint used to
      authenticate users.
    """


_ClientCreateServerResponseTypeDef = TypedDict(
    "_ClientCreateServerResponseTypeDef", {"ServerId": str}, total=False
)


class ClientCreateServerResponseTypeDef(_ClientCreateServerResponseTypeDef):
    """
    - *(dict) --*

      - **ServerId** *(string) --*

        The service-assigned ID of the SFTP server that is created.
    """


_RequiredClientCreateServerTagsTypeDef = TypedDict(
    "_RequiredClientCreateServerTagsTypeDef", {"Key": str}
)
_OptionalClientCreateServerTagsTypeDef = TypedDict(
    "_OptionalClientCreateServerTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateServerTagsTypeDef(
    _RequiredClientCreateServerTagsTypeDef, _OptionalClientCreateServerTagsTypeDef
):
    """
    - *(dict) --*

      Creates a key-value pair for a specific resource. Tags are metadata that you can use to search
      for and group a resource for various purposes. You can apply tags to servers, users, and
      roles. A tag key can take more than one value. For example, to group servers for accounting
      purposes, you might create a tag called ``Group`` and assign the values ``Research`` and
      ``Accounting`` to that group.
      - **Key** *(string) --***[REQUIRED]**

        The name assigned to the tag that you create.
    """


_ClientCreateUserHomeDirectoryMappingsTypeDef = TypedDict(
    "_ClientCreateUserHomeDirectoryMappingsTypeDef", {"Entry": str, "Target": str}, total=False
)


class ClientCreateUserHomeDirectoryMappingsTypeDef(_ClientCreateUserHomeDirectoryMappingsTypeDef):
    pass


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef", {"ServerId": str, "UserName": str}, total=False
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    - *(dict) --*

      - **ServerId** *(string) --*

        The ID of the SFTP server that the user is attached to.
    """


_RequiredClientCreateUserTagsTypeDef = TypedDict(
    "_RequiredClientCreateUserTagsTypeDef", {"Key": str}
)
_OptionalClientCreateUserTagsTypeDef = TypedDict(
    "_OptionalClientCreateUserTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateUserTagsTypeDef(
    _RequiredClientCreateUserTagsTypeDef, _OptionalClientCreateUserTagsTypeDef
):
    """
    - *(dict) --*

      Creates a key-value pair for a specific resource. Tags are metadata that you can use to search
      for and group a resource for various purposes. You can apply tags to servers, users, and
      roles. A tag key can take more than one value. For example, to group servers for accounting
      purposes, you might create a tag called ``Group`` and assign the values ``Research`` and
      ``Accounting`` to that group.
      - **Key** *(string) --***[REQUIRED]**

        The name assigned to the tag that you create.
    """


_ClientDescribeServerResponseServerEndpointDetailsTypeDef = TypedDict(
    "_ClientDescribeServerResponseServerEndpointDetailsTypeDef", {"VpcEndpointId": str}, total=False
)


class ClientDescribeServerResponseServerEndpointDetailsTypeDef(
    _ClientDescribeServerResponseServerEndpointDetailsTypeDef
):
    pass


_ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef = TypedDict(
    "_ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef",
    {"Url": str, "InvocationRole": str},
    total=False,
)


class ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef(
    _ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef
):
    pass


_ClientDescribeServerResponseServerTagsTypeDef = TypedDict(
    "_ClientDescribeServerResponseServerTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeServerResponseServerTagsTypeDef(_ClientDescribeServerResponseServerTagsTypeDef):
    pass


_ClientDescribeServerResponseServerTypeDef = TypedDict(
    "_ClientDescribeServerResponseServerTypeDef",
    {
        "Arn": str,
        "EndpointDetails": ClientDescribeServerResponseServerEndpointDetailsTypeDef,
        "EndpointType": Literal["PUBLIC", "VPC_ENDPOINT"],
        "HostKeyFingerprint": str,
        "IdentityProviderDetails": ClientDescribeServerResponseServerIdentityProviderDetailsTypeDef,
        "IdentityProviderType": Literal["SERVICE_MANAGED", "API_GATEWAY"],
        "LoggingRole": str,
        "ServerId": str,
        "State": Literal[
            "OFFLINE", "ONLINE", "STARTING", "STOPPING", "START_FAILED", "STOP_FAILED"
        ],
        "Tags": List[ClientDescribeServerResponseServerTagsTypeDef],
        "UserCount": int,
    },
    total=False,
)


class ClientDescribeServerResponseServerTypeDef(_ClientDescribeServerResponseServerTypeDef):
    """
    - **Server** *(dict) --*

      An array containing the properties of the server with the ``ServerID`` you specified.
      - **Arn** *(string) --*

        Specifies the unique Amazon Resource Name (ARN) for the server to be described.
    """


_ClientDescribeServerResponseTypeDef = TypedDict(
    "_ClientDescribeServerResponseTypeDef",
    {"Server": ClientDescribeServerResponseServerTypeDef},
    total=False,
)


class ClientDescribeServerResponseTypeDef(_ClientDescribeServerResponseTypeDef):
    """
    - *(dict) --*

      - **Server** *(dict) --*

        An array containing the properties of the server with the ``ServerID`` you specified.
        - **Arn** *(string) --*

          Specifies the unique Amazon Resource Name (ARN) for the server to be described.
    """


_ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef",
    {"Entry": str, "Target": str},
    total=False,
)


class ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef(
    _ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef
):
    pass


_ClientDescribeUserResponseUserSshPublicKeysTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserSshPublicKeysTypeDef",
    {"DateImported": datetime, "SshPublicKeyBody": str, "SshPublicKeyId": str},
    total=False,
)


class ClientDescribeUserResponseUserSshPublicKeysTypeDef(
    _ClientDescribeUserResponseUserSshPublicKeysTypeDef
):
    pass


_ClientDescribeUserResponseUserTagsTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeUserResponseUserTagsTypeDef(_ClientDescribeUserResponseUserTagsTypeDef):
    pass


_ClientDescribeUserResponseUserTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserTypeDef",
    {
        "Arn": str,
        "HomeDirectory": str,
        "HomeDirectoryMappings": List[ClientDescribeUserResponseUserHomeDirectoryMappingsTypeDef],
        "HomeDirectoryType": Literal["PATH", "LOGICAL"],
        "Policy": str,
        "Role": str,
        "SshPublicKeys": List[ClientDescribeUserResponseUserSshPublicKeysTypeDef],
        "Tags": List[ClientDescribeUserResponseUserTagsTypeDef],
        "UserName": str,
    },
    total=False,
)


class ClientDescribeUserResponseUserTypeDef(_ClientDescribeUserResponseUserTypeDef):
    pass


_ClientDescribeUserResponseTypeDef = TypedDict(
    "_ClientDescribeUserResponseTypeDef",
    {"ServerId": str, "User": ClientDescribeUserResponseUserTypeDef},
    total=False,
)


class ClientDescribeUserResponseTypeDef(_ClientDescribeUserResponseTypeDef):
    """
    - *(dict) --*

      - **ServerId** *(string) --*

        A system-assigned unique identifier for an SFTP server that has this user assigned.
    """


_ClientImportSshPublicKeyResponseTypeDef = TypedDict(
    "_ClientImportSshPublicKeyResponseTypeDef",
    {"ServerId": str, "SshPublicKeyId": str, "UserName": str},
    total=False,
)


class ClientImportSshPublicKeyResponseTypeDef(_ClientImportSshPublicKeyResponseTypeDef):
    """
    - *(dict) --*

      This response identifies the user, the server they belong to, and the identifier of the SSH
      public key associated with that user. A user can have more than one key on each server that
      they are associated with.
      - **ServerId** *(string) --*

        A system-assigned unique identifier for an SFTP server.
    """


_ClientListServersResponseServersTypeDef = TypedDict(
    "_ClientListServersResponseServersTypeDef",
    {
        "Arn": str,
        "IdentityProviderType": Literal["SERVICE_MANAGED", "API_GATEWAY"],
        "EndpointType": Literal["PUBLIC", "VPC_ENDPOINT"],
        "LoggingRole": str,
        "ServerId": str,
        "State": Literal[
            "OFFLINE", "ONLINE", "STARTING", "STOPPING", "START_FAILED", "STOP_FAILED"
        ],
        "UserCount": int,
    },
    total=False,
)


class ClientListServersResponseServersTypeDef(_ClientListServersResponseServersTypeDef):
    pass


_ClientListServersResponseTypeDef = TypedDict(
    "_ClientListServersResponseTypeDef",
    {"NextToken": str, "Servers": List[ClientListServersResponseServersTypeDef]},
    total=False,
)


class ClientListServersResponseTypeDef(_ClientListServersResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        When you can get additional results from the ``ListServers`` operation, a ``NextToken``
        parameter is returned in the output. In a following command, you can pass in the
        ``NextToken`` parameter to continue listing additional servers.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    pass


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Arn": str, "NextToken": str, "Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        This value is the ARN you specified to list the tags of.
    """


_ClientListUsersResponseUsersTypeDef = TypedDict(
    "_ClientListUsersResponseUsersTypeDef",
    {
        "Arn": str,
        "HomeDirectory": str,
        "HomeDirectoryType": Literal["PATH", "LOGICAL"],
        "Role": str,
        "SshPublicKeyCount": int,
        "UserName": str,
    },
    total=False,
)


class ClientListUsersResponseUsersTypeDef(_ClientListUsersResponseUsersTypeDef):
    pass


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {"NextToken": str, "ServerId": str, "Users": List[ClientListUsersResponseUsersTypeDef]},
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        When you can get additional results from the ``ListUsers`` call, a ``NextToken`` parameter
        is returned in the output. You can then pass in a subsequent command to the ``NextToken``
        parameter to continue listing additional users.
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

      Creates a key-value pair for a specific resource. Tags are metadata that you can use to search
      for and group a resource for various purposes. You can apply tags to servers, users, and
      roles. A tag key can take more than one value. For example, to group servers for accounting
      purposes, you might create a tag called ``Group`` and assign the values ``Research`` and
      ``Accounting`` to that group.
      - **Key** *(string) --***[REQUIRED]**

        The name assigned to the tag that you create.
    """


_ClientTestIdentityProviderResponseTypeDef = TypedDict(
    "_ClientTestIdentityProviderResponseTypeDef",
    {"Response": str, "StatusCode": int, "Message": str, "Url": str},
    total=False,
)


class ClientTestIdentityProviderResponseTypeDef(_ClientTestIdentityProviderResponseTypeDef):
    """
    - *(dict) --*

      - **Response** *(string) --*

        The response that is returned from your API Gateway.
    """


_ClientUpdateServerEndpointDetailsTypeDef = TypedDict(
    "_ClientUpdateServerEndpointDetailsTypeDef", {"VpcEndpointId": str}, total=False
)


class ClientUpdateServerEndpointDetailsTypeDef(_ClientUpdateServerEndpointDetailsTypeDef):
    """
    The virtual private cloud (VPC) endpoint settings that are configured for your SFTP server. With
    a VPC endpoint, your SFTP server isn't accessible over the public internet.
    - **VpcEndpointId** *(string) --*

      The ID of the VPC endpoint.
    """


_ClientUpdateServerIdentityProviderDetailsTypeDef = TypedDict(
    "_ClientUpdateServerIdentityProviderDetailsTypeDef",
    {"Url": str, "InvocationRole": str},
    total=False,
)


class ClientUpdateServerIdentityProviderDetailsTypeDef(
    _ClientUpdateServerIdentityProviderDetailsTypeDef
):
    """
    This response parameter is an array containing all of the information required to call a
    customer's authentication API method.
    - **Url** *(string) --*

      The ``Url`` parameter provides contains the location of the service endpoint used to
      authenticate users.
    """


_ClientUpdateServerResponseTypeDef = TypedDict(
    "_ClientUpdateServerResponseTypeDef", {"ServerId": str}, total=False
)


class ClientUpdateServerResponseTypeDef(_ClientUpdateServerResponseTypeDef):
    """
    - *(dict) --*

      - **ServerId** *(string) --*

        A system-assigned unique identifier for an SFTP server that the user account is assigned to.
    """


_ClientUpdateUserHomeDirectoryMappingsTypeDef = TypedDict(
    "_ClientUpdateUserHomeDirectoryMappingsTypeDef", {"Entry": str, "Target": str}, total=False
)


class ClientUpdateUserHomeDirectoryMappingsTypeDef(_ClientUpdateUserHomeDirectoryMappingsTypeDef):
    pass


_ClientUpdateUserResponseTypeDef = TypedDict(
    "_ClientUpdateUserResponseTypeDef", {"ServerId": str, "UserName": str}, total=False
)


class ClientUpdateUserResponseTypeDef(_ClientUpdateUserResponseTypeDef):
    """
    - *(dict) --*

      ``UpdateUserResponse`` returns the user name and server identifier for the request to update a
      user's properties.
      - **ServerId** *(string) --*

        A system-assigned unique identifier for an SFTP server instance that the user account is
        assigned to.
    """


_ListServersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServersPaginatePaginationConfigTypeDef(_ListServersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListServersPaginateResponseServersTypeDef = TypedDict(
    "_ListServersPaginateResponseServersTypeDef",
    {
        "Arn": str,
        "IdentityProviderType": Literal["SERVICE_MANAGED", "API_GATEWAY"],
        "EndpointType": Literal["PUBLIC", "VPC_ENDPOINT"],
        "LoggingRole": str,
        "ServerId": str,
        "State": Literal[
            "OFFLINE", "ONLINE", "STARTING", "STOPPING", "START_FAILED", "STOP_FAILED"
        ],
        "UserCount": int,
    },
    total=False,
)


class ListServersPaginateResponseServersTypeDef(_ListServersPaginateResponseServersTypeDef):
    """
    - *(dict) --*

      Returns properties of the server that was specified.
      - **Arn** *(string) --*

        The unique Amazon Resource Name (ARN) for the server to be listed.
    """


_ListServersPaginateResponseTypeDef = TypedDict(
    "_ListServersPaginateResponseTypeDef",
    {"Servers": List[ListServersPaginateResponseServersTypeDef]},
    total=False,
)


class ListServersPaginateResponseTypeDef(_ListServersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Servers** *(list) --*

        An array of servers that were listed.
        - *(dict) --*

          Returns properties of the server that was specified.
          - **Arn** *(string) --*

            The unique Amazon Resource Name (ARN) for the server to be listed.
    """
