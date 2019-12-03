"Main interface for route53resolver service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAssociateResolverEndpointIpAddressIpAddressTypeDef",
    "ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    "ClientAssociateResolverEndpointIpAddressResponseTypeDef",
    "ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef",
    "ClientAssociateResolverRuleResponseTypeDef",
    "ClientCreateResolverEndpointIpAddressesTypeDef",
    "ClientCreateResolverEndpointResponseResolverEndpointTypeDef",
    "ClientCreateResolverEndpointResponseTypeDef",
    "ClientCreateResolverEndpointTagsTypeDef",
    "ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientCreateResolverRuleResponseResolverRuleTypeDef",
    "ClientCreateResolverRuleResponseTypeDef",
    "ClientCreateResolverRuleTagsTypeDef",
    "ClientCreateResolverRuleTargetIpsTypeDef",
    "ClientDeleteResolverEndpointResponseResolverEndpointTypeDef",
    "ClientDeleteResolverEndpointResponseTypeDef",
    "ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientDeleteResolverRuleResponseResolverRuleTypeDef",
    "ClientDeleteResolverRuleResponseTypeDef",
    "ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef",
    "ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    "ClientDisassociateResolverEndpointIpAddressResponseTypeDef",
    "ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef",
    "ClientDisassociateResolverRuleResponseTypeDef",
    "ClientGetResolverEndpointResponseResolverEndpointTypeDef",
    "ClientGetResolverEndpointResponseTypeDef",
    "ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef",
    "ClientGetResolverRuleAssociationResponseTypeDef",
    "ClientGetResolverRulePolicyResponseTypeDef",
    "ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientGetResolverRuleResponseResolverRuleTypeDef",
    "ClientGetResolverRuleResponseTypeDef",
    "ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef",
    "ClientListResolverEndpointIpAddressesResponseTypeDef",
    "ClientListResolverEndpointsFiltersTypeDef",
    "ClientListResolverEndpointsResponseResolverEndpointsTypeDef",
    "ClientListResolverEndpointsResponseTypeDef",
    "ClientListResolverRuleAssociationsFiltersTypeDef",
    "ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef",
    "ClientListResolverRuleAssociationsResponseTypeDef",
    "ClientListResolverRulesFiltersTypeDef",
    "ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef",
    "ClientListResolverRulesResponseResolverRulesTypeDef",
    "ClientListResolverRulesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutResolverRulePolicyResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateResolverEndpointResponseResolverEndpointTypeDef",
    "ClientUpdateResolverEndpointResponseTypeDef",
    "ClientUpdateResolverRuleConfigTargetIpsTypeDef",
    "ClientUpdateResolverRuleConfigTypeDef",
    "ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    "ClientUpdateResolverRuleResponseResolverRuleTypeDef",
    "ClientUpdateResolverRuleResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
)


_ClientAssociateResolverEndpointIpAddressIpAddressTypeDef = TypedDict(
    "_ClientAssociateResolverEndpointIpAddressIpAddressTypeDef",
    {"IpId": str, "SubnetId": str, "Ip": str},
    total=False,
)


class ClientAssociateResolverEndpointIpAddressIpAddressTypeDef(
    _ClientAssociateResolverEndpointIpAddressIpAddressTypeDef
):
    """
    Either the IPv4 address that you want to add to a resolver endpoint or a subnet ID. If you
    specify a subnet ID, Resolver chooses an IP address for you from the available IPs in the
    specified subnet.
    - **IpId** *(string) --*

      *Only when removing an IP address from a resolver endpoint* : The ID of the IP address that
      you want to remove. To get this ID, use  GetResolverEndpoint .
    """


_ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef = TypedDict(
    "_ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef(
    _ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef
):
    """
    - **ResolverEndpoint** *(dict) --*

      The response to an ``AssociateResolverEndpointIpAddress`` request.
      - **Id** *(string) --*

        The ID of the resolver endpoint.
    """


_ClientAssociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "_ClientAssociateResolverEndpointIpAddressResponseTypeDef",
    {"ResolverEndpoint": ClientAssociateResolverEndpointIpAddressResponseResolverEndpointTypeDef},
    total=False,
)


class ClientAssociateResolverEndpointIpAddressResponseTypeDef(
    _ClientAssociateResolverEndpointIpAddressResponseTypeDef
):
    """
    - *(dict) --*

      - **ResolverEndpoint** *(dict) --*

        The response to an ``AssociateResolverEndpointIpAddress`` request.
        - **Id** *(string) --*

          The ID of the resolver endpoint.
    """


_ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef = TypedDict(
    "_ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": Literal["CREATING", "COMPLETE", "DELETING", "FAILED", "OVERRIDDEN"],
        "StatusMessage": str,
    },
    total=False,
)


class ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef(
    _ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef
):
    """
    - **ResolverRuleAssociation** *(dict) --*

      Information about the ``AssociateResolverRule`` request, including the status of the request.
      - **Id** *(string) --*

        The ID of the association between a resolver rule and a VPC. Resolver assigns this value
        when you submit an  AssociateResolverRule request.
    """


_ClientAssociateResolverRuleResponseTypeDef = TypedDict(
    "_ClientAssociateResolverRuleResponseTypeDef",
    {"ResolverRuleAssociation": ClientAssociateResolverRuleResponseResolverRuleAssociationTypeDef},
    total=False,
)


class ClientAssociateResolverRuleResponseTypeDef(_ClientAssociateResolverRuleResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverRuleAssociation** *(dict) --*

        Information about the ``AssociateResolverRule`` request, including the status of the
        request.
        - **Id** *(string) --*

          The ID of the association between a resolver rule and a VPC. Resolver assigns this value
          when you submit an  AssociateResolverRule request.
    """


_RequiredClientCreateResolverEndpointIpAddressesTypeDef = TypedDict(
    "_RequiredClientCreateResolverEndpointIpAddressesTypeDef", {"SubnetId": str}
)
_OptionalClientCreateResolverEndpointIpAddressesTypeDef = TypedDict(
    "_OptionalClientCreateResolverEndpointIpAddressesTypeDef", {"Ip": str}, total=False
)


class ClientCreateResolverEndpointIpAddressesTypeDef(
    _RequiredClientCreateResolverEndpointIpAddressesTypeDef,
    _OptionalClientCreateResolverEndpointIpAddressesTypeDef,
):
    """
    - *(dict) --*

      In an  CreateResolverEndpoint request, a subnet and IP address that you want to use for DNS
      queries.
      - **SubnetId** *(string) --***[REQUIRED]**

        The subnet that contains the IP address.
    """


_ClientCreateResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "_ClientCreateResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientCreateResolverEndpointResponseResolverEndpointTypeDef(
    _ClientCreateResolverEndpointResponseResolverEndpointTypeDef
):
    """
    - **ResolverEndpoint** *(dict) --*

      Information about the ``CreateResolverEndpoint`` request, including the status of the request.
      - **Id** *(string) --*

        The ID of the resolver endpoint.
    """


_ClientCreateResolverEndpointResponseTypeDef = TypedDict(
    "_ClientCreateResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientCreateResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)


class ClientCreateResolverEndpointResponseTypeDef(_ClientCreateResolverEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverEndpoint** *(dict) --*

        Information about the ``CreateResolverEndpoint`` request, including the status of the
        request.
        - **Id** *(string) --*

          The ID of the resolver endpoint.
    """


_ClientCreateResolverEndpointTagsTypeDef = TypedDict(
    "_ClientCreateResolverEndpointTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateResolverEndpointTagsTypeDef(_ClientCreateResolverEndpointTagsTypeDef):
    """
    - *(dict) --*

      One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name
      for the tag) and a ``Value`` .
      - **Key** *(string) --*

        The name for the tag. For example, if you want to associate Resolver resources with the
        account IDs of your customers for billing purposes, the value of ``Key`` might be
        ``account-id`` .
    """


_ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "_ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)


class ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef(
    _ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef
):
    pass


_ClientCreateResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "_ClientCreateResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List[ClientCreateResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)


class ClientCreateResolverRuleResponseResolverRuleTypeDef(
    _ClientCreateResolverRuleResponseResolverRuleTypeDef
):
    """
    - **ResolverRule** *(dict) --*

      Information about the ``CreateResolverRule`` request, including the status of the request.
      - **Id** *(string) --*

        The ID that Resolver assigned to the resolver rule when you created it.
    """


_ClientCreateResolverRuleResponseTypeDef = TypedDict(
    "_ClientCreateResolverRuleResponseTypeDef",
    {"ResolverRule": ClientCreateResolverRuleResponseResolverRuleTypeDef},
    total=False,
)


class ClientCreateResolverRuleResponseTypeDef(_ClientCreateResolverRuleResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverRule** *(dict) --*

        Information about the ``CreateResolverRule`` request, including the status of the request.
        - **Id** *(string) --*

          The ID that Resolver assigned to the resolver rule when you created it.
    """


_ClientCreateResolverRuleTagsTypeDef = TypedDict(
    "_ClientCreateResolverRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateResolverRuleTagsTypeDef(_ClientCreateResolverRuleTagsTypeDef):
    """
    - *(dict) --*

      One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name
      for the tag) and a ``Value`` .
      - **Key** *(string) --*

        The name for the tag. For example, if you want to associate Resolver resources with the
        account IDs of your customers for billing purposes, the value of ``Key`` might be
        ``account-id`` .
    """


_RequiredClientCreateResolverRuleTargetIpsTypeDef = TypedDict(
    "_RequiredClientCreateResolverRuleTargetIpsTypeDef", {"Ip": str}
)
_OptionalClientCreateResolverRuleTargetIpsTypeDef = TypedDict(
    "_OptionalClientCreateResolverRuleTargetIpsTypeDef", {"Port": int}, total=False
)


class ClientCreateResolverRuleTargetIpsTypeDef(
    _RequiredClientCreateResolverRuleTargetIpsTypeDef,
    _OptionalClientCreateResolverRuleTargetIpsTypeDef,
):
    """
    - *(dict) --*

      In a  CreateResolverRule request, an array of the IPs that you want to forward DNS queries to.
      - **Ip** *(string) --***[REQUIRED]**

        One IP address that you want to forward DNS queries to. You can specify only IPv4 addresses.
    """


_ClientDeleteResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "_ClientDeleteResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientDeleteResolverEndpointResponseResolverEndpointTypeDef(
    _ClientDeleteResolverEndpointResponseResolverEndpointTypeDef
):
    """
    - **ResolverEndpoint** *(dict) --*

      Information about the ``DeleteResolverEndpoint`` request, including the status of the request.
      - **Id** *(string) --*

        The ID of the resolver endpoint.
    """


_ClientDeleteResolverEndpointResponseTypeDef = TypedDict(
    "_ClientDeleteResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientDeleteResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)


class ClientDeleteResolverEndpointResponseTypeDef(_ClientDeleteResolverEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverEndpoint** *(dict) --*

        Information about the ``DeleteResolverEndpoint`` request, including the status of the
        request.
        - **Id** *(string) --*

          The ID of the resolver endpoint.
    """


_ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "_ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)


class ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef(
    _ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef
):
    pass


_ClientDeleteResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "_ClientDeleteResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List[ClientDeleteResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)


class ClientDeleteResolverRuleResponseResolverRuleTypeDef(
    _ClientDeleteResolverRuleResponseResolverRuleTypeDef
):
    """
    - **ResolverRule** *(dict) --*

      Information about the ``DeleteResolverRule`` request, including the status of the request.
      - **Id** *(string) --*

        The ID that Resolver assigned to the resolver rule when you created it.
    """


_ClientDeleteResolverRuleResponseTypeDef = TypedDict(
    "_ClientDeleteResolverRuleResponseTypeDef",
    {"ResolverRule": ClientDeleteResolverRuleResponseResolverRuleTypeDef},
    total=False,
)


class ClientDeleteResolverRuleResponseTypeDef(_ClientDeleteResolverRuleResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverRule** *(dict) --*

        Information about the ``DeleteResolverRule`` request, including the status of the request.
        - **Id** *(string) --*

          The ID that Resolver assigned to the resolver rule when you created it.
    """


_ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef = TypedDict(
    "_ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef",
    {"IpId": str, "SubnetId": str, "Ip": str},
    total=False,
)


class ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef(
    _ClientDisassociateResolverEndpointIpAddressIpAddressTypeDef
):
    """
    The IPv4 address that you want to remove from a resolver endpoint.
    - **IpId** *(string) --*

      *Only when removing an IP address from a resolver endpoint* : The ID of the IP address that
      you want to remove. To get this ID, use  GetResolverEndpoint .
    """


_ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef = TypedDict(
    "_ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef(
    _ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef
):
    """
    - **ResolverEndpoint** *(dict) --*

      The response to an ``DisassociateResolverEndpointIpAddress`` request.
      - **Id** *(string) --*

        The ID of the resolver endpoint.
    """


_ClientDisassociateResolverEndpointIpAddressResponseTypeDef = TypedDict(
    "_ClientDisassociateResolverEndpointIpAddressResponseTypeDef",
    {
        "ResolverEndpoint": ClientDisassociateResolverEndpointIpAddressResponseResolverEndpointTypeDef
    },
    total=False,
)


class ClientDisassociateResolverEndpointIpAddressResponseTypeDef(
    _ClientDisassociateResolverEndpointIpAddressResponseTypeDef
):
    """
    - *(dict) --*

      - **ResolverEndpoint** *(dict) --*

        The response to an ``DisassociateResolverEndpointIpAddress`` request.
        - **Id** *(string) --*

          The ID of the resolver endpoint.
    """


_ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef = TypedDict(
    "_ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": Literal["CREATING", "COMPLETE", "DELETING", "FAILED", "OVERRIDDEN"],
        "StatusMessage": str,
    },
    total=False,
)


class ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef(
    _ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef
):
    """
    - **ResolverRuleAssociation** *(dict) --*

      Information about the ``DisassociateResolverRule`` request, including the status of the
      request.
      - **Id** *(string) --*

        The ID of the association between a resolver rule and a VPC. Resolver assigns this value
        when you submit an  AssociateResolverRule request.
    """


_ClientDisassociateResolverRuleResponseTypeDef = TypedDict(
    "_ClientDisassociateResolverRuleResponseTypeDef",
    {
        "ResolverRuleAssociation": ClientDisassociateResolverRuleResponseResolverRuleAssociationTypeDef
    },
    total=False,
)


class ClientDisassociateResolverRuleResponseTypeDef(_ClientDisassociateResolverRuleResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverRuleAssociation** *(dict) --*

        Information about the ``DisassociateResolverRule`` request, including the status of the
        request.
        - **Id** *(string) --*

          The ID of the association between a resolver rule and a VPC. Resolver assigns this value
          when you submit an  AssociateResolverRule request.
    """


_ClientGetResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "_ClientGetResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientGetResolverEndpointResponseResolverEndpointTypeDef(
    _ClientGetResolverEndpointResponseResolverEndpointTypeDef
):
    """
    - **ResolverEndpoint** *(dict) --*

      Information about the resolver endpoint that you specified in a ``GetResolverEndpoint``
      request.
      - **Id** *(string) --*

        The ID of the resolver endpoint.
    """


_ClientGetResolverEndpointResponseTypeDef = TypedDict(
    "_ClientGetResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientGetResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)


class ClientGetResolverEndpointResponseTypeDef(_ClientGetResolverEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverEndpoint** *(dict) --*

        Information about the resolver endpoint that you specified in a ``GetResolverEndpoint``
        request.
        - **Id** *(string) --*

          The ID of the resolver endpoint.
    """


_ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef = TypedDict(
    "_ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": Literal["CREATING", "COMPLETE", "DELETING", "FAILED", "OVERRIDDEN"],
        "StatusMessage": str,
    },
    total=False,
)


class ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef(
    _ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef
):
    """
    - **ResolverRuleAssociation** *(dict) --*

      Information about the resolver rule association that you specified in a
      ``GetResolverRuleAssociation`` request.
      - **Id** *(string) --*

        The ID of the association between a resolver rule and a VPC. Resolver assigns this value
        when you submit an  AssociateResolverRule request.
    """


_ClientGetResolverRuleAssociationResponseTypeDef = TypedDict(
    "_ClientGetResolverRuleAssociationResponseTypeDef",
    {
        "ResolverRuleAssociation": ClientGetResolverRuleAssociationResponseResolverRuleAssociationTypeDef
    },
    total=False,
)


class ClientGetResolverRuleAssociationResponseTypeDef(
    _ClientGetResolverRuleAssociationResponseTypeDef
):
    """
    - *(dict) --*

      - **ResolverRuleAssociation** *(dict) --*

        Information about the resolver rule association that you specified in a
        ``GetResolverRuleAssociation`` request.
        - **Id** *(string) --*

          The ID of the association between a resolver rule and a VPC. Resolver assigns this value
          when you submit an  AssociateResolverRule request.
    """


_ClientGetResolverRulePolicyResponseTypeDef = TypedDict(
    "_ClientGetResolverRulePolicyResponseTypeDef", {"ResolverRulePolicy": str}, total=False
)


class ClientGetResolverRulePolicyResponseTypeDef(_ClientGetResolverRulePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverRulePolicy** *(string) --*

        Information about the resolver rule policy that you specified in a ``GetResolverRulePolicy``
        request.
    """


_ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "_ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)


class ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef(
    _ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef
):
    pass


_ClientGetResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "_ClientGetResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List[ClientGetResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)


class ClientGetResolverRuleResponseResolverRuleTypeDef(
    _ClientGetResolverRuleResponseResolverRuleTypeDef
):
    """
    - **ResolverRule** *(dict) --*

      Information about the resolver rule that you specified in a ``GetResolverRule`` request.
      - **Id** *(string) --*

        The ID that Resolver assigned to the resolver rule when you created it.
    """


_ClientGetResolverRuleResponseTypeDef = TypedDict(
    "_ClientGetResolverRuleResponseTypeDef",
    {"ResolverRule": ClientGetResolverRuleResponseResolverRuleTypeDef},
    total=False,
)


class ClientGetResolverRuleResponseTypeDef(_ClientGetResolverRuleResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverRule** *(dict) --*

        Information about the resolver rule that you specified in a ``GetResolverRule`` request.
        - **Id** *(string) --*

          The ID that Resolver assigned to the resolver rule when you created it.
    """


_ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef = TypedDict(
    "_ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef",
    {
        "IpId": str,
        "SubnetId": str,
        "Ip": str,
        "Status": Literal[
            "CREATING",
            "FAILED_CREATION",
            "ATTACHING",
            "ATTACHED",
            "REMAP_DETACHING",
            "REMAP_ATTACHING",
            "DETACHING",
            "FAILED_RESOURCE_GONE",
            "DELETING",
            "DELETE_FAILED_FAS_EXPIRED",
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef(
    _ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef
):
    pass


_ClientListResolverEndpointIpAddressesResponseTypeDef = TypedDict(
    "_ClientListResolverEndpointIpAddressesResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IpAddresses": List[ClientListResolverEndpointIpAddressesResponseIpAddressesTypeDef],
    },
    total=False,
)


class ClientListResolverEndpointIpAddressesResponseTypeDef(
    _ClientListResolverEndpointIpAddressesResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If the specified endpoint has more than ``MaxResults`` IP addresses, you can submit another
        ``ListResolverEndpointIpAddresses`` request to get the next group of IP addresses. In the
        next request, specify the value of ``NextToken`` from the previous response.
    """


_ClientListResolverEndpointsFiltersTypeDef = TypedDict(
    "_ClientListResolverEndpointsFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientListResolverEndpointsFiltersTypeDef(_ClientListResolverEndpointsFiltersTypeDef):
    pass


_ClientListResolverEndpointsResponseResolverEndpointsTypeDef = TypedDict(
    "_ClientListResolverEndpointsResponseResolverEndpointsTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientListResolverEndpointsResponseResolverEndpointsTypeDef(
    _ClientListResolverEndpointsResponseResolverEndpointsTypeDef
):
    pass


_ClientListResolverEndpointsResponseTypeDef = TypedDict(
    "_ClientListResolverEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverEndpoints": List[ClientListResolverEndpointsResponseResolverEndpointsTypeDef],
    },
    total=False,
)


class ClientListResolverEndpointsResponseTypeDef(_ClientListResolverEndpointsResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If more than ``MaxResults`` IP addresses match the specified criteria, you can submit
        another ``ListResolverEndpoint`` request to get the next group of results. In the next
        request, specify the value of ``NextToken`` from the previous response.
    """


_ClientListResolverRuleAssociationsFiltersTypeDef = TypedDict(
    "_ClientListResolverRuleAssociationsFiltersTypeDef",
    {"Name": str, "Values": List[str]},
    total=False,
)


class ClientListResolverRuleAssociationsFiltersTypeDef(
    _ClientListResolverRuleAssociationsFiltersTypeDef
):
    pass


_ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef = TypedDict(
    "_ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef",
    {
        "Id": str,
        "ResolverRuleId": str,
        "Name": str,
        "VPCId": str,
        "Status": Literal["CREATING", "COMPLETE", "DELETING", "FAILED", "OVERRIDDEN"],
        "StatusMessage": str,
    },
    total=False,
)


class ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef(
    _ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef
):
    pass


_ClientListResolverRuleAssociationsResponseTypeDef = TypedDict(
    "_ClientListResolverRuleAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRuleAssociations": List[
            ClientListResolverRuleAssociationsResponseResolverRuleAssociationsTypeDef
        ],
    },
    total=False,
)


class ClientListResolverRuleAssociationsResponseTypeDef(
    _ClientListResolverRuleAssociationsResponseTypeDef
):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If more than ``MaxResults`` rule associations match the specified criteria, you can submit
        another ``ListResolverRuleAssociation`` request to get the next group of results. In the
        next request, specify the value of ``NextToken`` from the previous response.
    """


_ClientListResolverRulesFiltersTypeDef = TypedDict(
    "_ClientListResolverRulesFiltersTypeDef", {"Name": str, "Values": List[str]}, total=False
)


class ClientListResolverRulesFiltersTypeDef(_ClientListResolverRulesFiltersTypeDef):
    pass


_ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef = TypedDict(
    "_ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)


class ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef(
    _ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef
):
    pass


_ClientListResolverRulesResponseResolverRulesTypeDef = TypedDict(
    "_ClientListResolverRulesResponseResolverRulesTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List[ClientListResolverRulesResponseResolverRulesTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)


class ClientListResolverRulesResponseResolverRulesTypeDef(
    _ClientListResolverRulesResponseResolverRulesTypeDef
):
    pass


_ClientListResolverRulesResponseTypeDef = TypedDict(
    "_ClientListResolverRulesResponseTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResolverRules": List[ClientListResolverRulesResponseResolverRulesTypeDef],
    },
    total=False,
)


class ClientListResolverRulesResponseTypeDef(_ClientListResolverRulesResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        If more than ``MaxResults`` resolver rules match the specified criteria, you can submit
        another ``ListResolverRules`` request to get the next group of results. In the next request,
        specify the value of ``NextToken`` from the previous response.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name
      for the tag) and a ``Value`` .
      - **Key** *(string) --*

        The name for the tag. For example, if you want to associate Resolver resources with the
        account IDs of your customers for billing purposes, the value of ``Key`` might be
        ``account-id`` .
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The tags that are associated with the resource that you specified in the
        ``ListTagsForResource`` request.
        - *(dict) --*

          One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a
          name for the tag) and a ``Value`` .
          - **Key** *(string) --*

            The name for the tag. For example, if you want to associate Resolver resources with the
            account IDs of your customers for billing purposes, the value of ``Key`` might be
            ``account-id`` .
    """


_ClientPutResolverRulePolicyResponseTypeDef = TypedDict(
    "_ClientPutResolverRulePolicyResponseTypeDef", {"ReturnValue": bool}, total=False
)


class ClientPutResolverRulePolicyResponseTypeDef(_ClientPutResolverRulePolicyResponseTypeDef):
    """
    - *(dict) --*

      The response to a ``PutResolverRulePolicy`` request.
      - **ReturnValue** *(boolean) --*

        Whether the ``PutResolverRulePolicy`` request was successful.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name
      for the tag) and a ``Value`` .
      - **Key** *(string) --*

        The name for the tag. For example, if you want to associate Resolver resources with the
        account IDs of your customers for billing purposes, the value of ``Key`` might be
        ``account-id`` .
    """


_ClientUpdateResolverEndpointResponseResolverEndpointTypeDef = TypedDict(
    "_ClientUpdateResolverEndpointResponseResolverEndpointTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "Name": str,
        "SecurityGroupIds": List[str],
        "Direction": Literal["INBOUND", "OUTBOUND"],
        "IpAddressCount": int,
        "HostVPCId": str,
        "Status": Literal[
            "CREATING", "OPERATIONAL", "UPDATING", "AUTO_RECOVERING", "ACTION_NEEDED", "DELETING"
        ],
        "StatusMessage": str,
        "CreationTime": str,
        "ModificationTime": str,
    },
    total=False,
)


class ClientUpdateResolverEndpointResponseResolverEndpointTypeDef(
    _ClientUpdateResolverEndpointResponseResolverEndpointTypeDef
):
    """
    - **ResolverEndpoint** *(dict) --*

      The response to an ``UpdateResolverEndpoint`` request.
      - **Id** *(string) --*

        The ID of the resolver endpoint.
    """


_ClientUpdateResolverEndpointResponseTypeDef = TypedDict(
    "_ClientUpdateResolverEndpointResponseTypeDef",
    {"ResolverEndpoint": ClientUpdateResolverEndpointResponseResolverEndpointTypeDef},
    total=False,
)


class ClientUpdateResolverEndpointResponseTypeDef(_ClientUpdateResolverEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverEndpoint** *(dict) --*

        The response to an ``UpdateResolverEndpoint`` request.
        - **Id** *(string) --*

          The ID of the resolver endpoint.
    """


_ClientUpdateResolverRuleConfigTargetIpsTypeDef = TypedDict(
    "_ClientUpdateResolverRuleConfigTargetIpsTypeDef", {"Ip": str, "Port": int}, total=False
)


class ClientUpdateResolverRuleConfigTargetIpsTypeDef(
    _ClientUpdateResolverRuleConfigTargetIpsTypeDef
):
    pass


_ClientUpdateResolverRuleConfigTypeDef = TypedDict(
    "_ClientUpdateResolverRuleConfigTypeDef",
    {
        "Name": str,
        "TargetIps": List[ClientUpdateResolverRuleConfigTargetIpsTypeDef],
        "ResolverEndpointId": str,
    },
    total=False,
)


class ClientUpdateResolverRuleConfigTypeDef(_ClientUpdateResolverRuleConfigTypeDef):
    """
    The new settings for the resolver rule.
    - **Name** *(string) --*

      The new name for the resolver rule. The name that you specify appears in the Resolver
      dashboard in the Route 53 console.
    """


_ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef = TypedDict(
    "_ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef",
    {"Ip": str, "Port": int},
    total=False,
)


class ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef(
    _ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef
):
    pass


_ClientUpdateResolverRuleResponseResolverRuleTypeDef = TypedDict(
    "_ClientUpdateResolverRuleResponseResolverRuleTypeDef",
    {
        "Id": str,
        "CreatorRequestId": str,
        "Arn": str,
        "DomainName": str,
        "Status": Literal["COMPLETE", "DELETING", "UPDATING", "FAILED"],
        "StatusMessage": str,
        "RuleType": Literal["FORWARD", "SYSTEM", "RECURSIVE"],
        "Name": str,
        "TargetIps": List[ClientUpdateResolverRuleResponseResolverRuleTargetIpsTypeDef],
        "ResolverEndpointId": str,
        "OwnerId": str,
        "ShareStatus": Literal["NOT_SHARED", "SHARED_WITH_ME", "SHARED_BY_ME"],
    },
    total=False,
)


class ClientUpdateResolverRuleResponseResolverRuleTypeDef(
    _ClientUpdateResolverRuleResponseResolverRuleTypeDef
):
    """
    - **ResolverRule** *(dict) --*

      The response to an ``UpdateResolverRule`` request.
      - **Id** *(string) --*

        The ID that Resolver assigned to the resolver rule when you created it.
    """


_ClientUpdateResolverRuleResponseTypeDef = TypedDict(
    "_ClientUpdateResolverRuleResponseTypeDef",
    {"ResolverRule": ClientUpdateResolverRuleResponseResolverRuleTypeDef},
    total=False,
)


class ClientUpdateResolverRuleResponseTypeDef(_ClientUpdateResolverRuleResponseTypeDef):
    """
    - *(dict) --*

      - **ResolverRule** *(dict) --*

        The response to an ``UpdateResolverRule`` request.
        - **Id** *(string) --*

          The ID that Resolver assigned to the resolver rule when you created it.
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


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    - *(dict) --*

      One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a name
      for the tag) and a ``Value`` .
      - **Key** *(string) --*

        The name for the tag. For example, if you want to associate Resolver resources with the
        account IDs of your customers for billing purposes, the value of ``Key`` might be
        ``account-id`` .
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(_ListTagsForResourcePaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The tags that are associated with the resource that you specified in the
        ``ListTagsForResource`` request.
        - *(dict) --*

          One tag that you want to add to the specified resource. A tag consists of a ``Key`` (a
          name for the tag) and a ``Value`` .
          - **Key** *(string) --*

            The name for the tag. For example, if you want to associate Resolver resources with the
            account IDs of your customers for billing purposes, the value of ``Key`` might be
            ``account-id`` .
    """
