"Main interface for directconnect service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef",
    "ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef",
    "ClientAllocateConnectionOnInterconnectResponsetagsTypeDef",
    "ClientAllocateConnectionOnInterconnectResponseTypeDef",
    "ClientAllocateHostedConnectionResponsetagsTypeDef",
    "ClientAllocateHostedConnectionResponseTypeDef",
    "ClientAllocateHostedConnectionTagsTypeDef",
    "ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationtagsTypeDef",
    "ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef",
    "ClientAllocatePrivateVirtualInterfaceResponseTypeDef",
    "ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef",
    "ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationtagsTypeDef",
    "ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef",
    "ClientAllocatePublicVirtualInterfaceResponseTypeDef",
    "ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationtagsTypeDef",
    "ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    "ClientAllocateTransitVirtualInterfaceResponseTypeDef",
    "ClientAssociateConnectionWithLagResponsetagsTypeDef",
    "ClientAssociateConnectionWithLagResponseTypeDef",
    "ClientAssociateHostedConnectionResponsetagsTypeDef",
    "ClientAssociateHostedConnectionResponseTypeDef",
    "ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientAssociateVirtualInterfaceResponsetagsTypeDef",
    "ClientAssociateVirtualInterfaceResponseTypeDef",
    "ClientConfirmConnectionResponseTypeDef",
    "ClientConfirmPrivateVirtualInterfaceResponseTypeDef",
    "ClientConfirmPublicVirtualInterfaceResponseTypeDef",
    "ClientConfirmTransitVirtualInterfaceResponseTypeDef",
    "ClientCreateBgpPeerNewBGPPeerTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef",
    "ClientCreateBgpPeerResponsevirtualInterfaceTypeDef",
    "ClientCreateBgpPeerResponseTypeDef",
    "ClientCreateConnectionResponsetagsTypeDef",
    "ClientCreateConnectionResponseTypeDef",
    "ClientCreateConnectionTagsTypeDef",
    "ClientCreateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalRemoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    "ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    "ClientCreateDirectConnectGatewayAssociationResponseTypeDef",
    "ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    "ClientCreateDirectConnectGatewayResponseTypeDef",
    "ClientCreateInterconnectResponsetagsTypeDef",
    "ClientCreateInterconnectResponseTypeDef",
    "ClientCreateInterconnectTagsTypeDef",
    "ClientCreateLagChildConnectionTagsTypeDef",
    "ClientCreateLagResponseconnectionstagsTypeDef",
    "ClientCreateLagResponseconnectionsTypeDef",
    "ClientCreateLagResponsetagsTypeDef",
    "ClientCreateLagResponseTypeDef",
    "ClientCreateLagTagsTypeDef",
    "ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfacetagsTypeDef",
    "ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef",
    "ClientCreatePrivateVirtualInterfaceResponseTypeDef",
    "ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacetagsTypeDef",
    "ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef",
    "ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    "ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    "ClientCreatePublicVirtualInterfaceResponsetagsTypeDef",
    "ClientCreatePublicVirtualInterfaceResponseTypeDef",
    "ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfacetagsTypeDef",
    "ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfaceTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    "ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    "ClientCreateTransitVirtualInterfaceResponseTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef",
    "ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef",
    "ClientDeleteBgpPeerResponseTypeDef",
    "ClientDeleteConnectionResponsetagsTypeDef",
    "ClientDeleteConnectionResponseTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    "ClientDeleteDirectConnectGatewayAssociationResponseTypeDef",
    "ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    "ClientDeleteDirectConnectGatewayResponseTypeDef",
    "ClientDeleteInterconnectResponseTypeDef",
    "ClientDeleteLagResponseconnectionstagsTypeDef",
    "ClientDeleteLagResponseconnectionsTypeDef",
    "ClientDeleteLagResponsetagsTypeDef",
    "ClientDeleteLagResponseTypeDef",
    "ClientDeleteVirtualInterfaceResponseTypeDef",
    "ClientDescribeConnectionLoaResponseloaTypeDef",
    "ClientDescribeConnectionLoaResponseTypeDef",
    "ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef",
    "ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef",
    "ClientDescribeConnectionsOnInterconnectResponseTypeDef",
    "ClientDescribeConnectionsResponseconnectionstagsTypeDef",
    "ClientDescribeConnectionsResponseconnectionsTypeDef",
    "ClientDescribeConnectionsResponseTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef",
    "ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef",
    "ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef",
    "ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef",
    "ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef",
    "ClientDescribeDirectConnectGatewaysResponseTypeDef",
    "ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef",
    "ClientDescribeHostedConnectionsResponseconnectionsTypeDef",
    "ClientDescribeHostedConnectionsResponseTypeDef",
    "ClientDescribeInterconnectLoaResponseloaTypeDef",
    "ClientDescribeInterconnectLoaResponseTypeDef",
    "ClientDescribeInterconnectsResponseinterconnectstagsTypeDef",
    "ClientDescribeInterconnectsResponseinterconnectsTypeDef",
    "ClientDescribeInterconnectsResponseTypeDef",
    "ClientDescribeLagsResponselagsconnectionstagsTypeDef",
    "ClientDescribeLagsResponselagsconnectionsTypeDef",
    "ClientDescribeLagsResponselagstagsTypeDef",
    "ClientDescribeLagsResponselagsTypeDef",
    "ClientDescribeLagsResponseTypeDef",
    "ClientDescribeLoaResponseTypeDef",
    "ClientDescribeLocationsResponselocationsTypeDef",
    "ClientDescribeLocationsResponseTypeDef",
    "ClientDescribeTagsResponseresourceTagstagsTypeDef",
    "ClientDescribeTagsResponseresourceTagsTypeDef",
    "ClientDescribeTagsResponseTypeDef",
    "ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef",
    "ClientDescribeVirtualGatewaysResponseTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef",
    "ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef",
    "ClientDescribeVirtualInterfacesResponseTypeDef",
    "ClientDisassociateConnectionFromLagResponsetagsTypeDef",
    "ClientDisassociateConnectionFromLagResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationRemoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    "ClientUpdateDirectConnectGatewayAssociationResponseTypeDef",
    "ClientUpdateLagResponseconnectionstagsTypeDef",
    "ClientUpdateLagResponseconnectionsTypeDef",
    "ClientUpdateLagResponsetagsTypeDef",
    "ClientUpdateLagResponseTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef",
    "ClientUpdateVirtualInterfaceAttributesResponseTypeDef",
    "DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef",
    "DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef",
    "DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef",
    "DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef",
    "DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef",
    "DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef",
    "DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef",
    "DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef",
    "DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef",
    "DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef",
    "DescribeDirectConnectGatewaysPaginateResponseTypeDef",
)


_ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientAcceptDirectConnectGatewayAssociationProposalOverrideAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    - *(dict) --*

      Information about a route filter prefix that a customer can advertise through Border Gateway
      Protocol (BGP) over a public virtual interface.
      - **cidr** *(string) --*

        The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
        must use /64 or shorter.
    """


_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)


class ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef(
    _ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef
):
    pass


_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "_ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef(
    _ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef
):
    """
    - **directConnectGatewayAssociation** *(dict) --*

      Information about an association between a Direct Connect gateway and a virtual private
      gateway or transit gateway.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef = TypedDict(
    "_ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientAcceptDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)


class ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef(
    _ClientAcceptDirectConnectGatewayAssociationProposalResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAssociation** *(dict) --*

        Information about an association between a Direct Connect gateway and a virtual private
        gateway or transit gateway.
        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.
    """


_ClientAllocateConnectionOnInterconnectResponsetagsTypeDef = TypedDict(
    "_ClientAllocateConnectionOnInterconnectResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocateConnectionOnInterconnectResponsetagsTypeDef(
    _ClientAllocateConnectionOnInterconnectResponsetagsTypeDef
):
    pass


_ClientAllocateConnectionOnInterconnectResponseTypeDef = TypedDict(
    "_ClientAllocateConnectionOnInterconnectResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientAllocateConnectionOnInterconnectResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientAllocateConnectionOnInterconnectResponseTypeDef(
    _ClientAllocateConnectionOnInterconnectResponseTypeDef
):
    """
    - *(dict) --*

      Information about an AWS Direct Connect connection.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the connection.
    """


_ClientAllocateHostedConnectionResponsetagsTypeDef = TypedDict(
    "_ClientAllocateHostedConnectionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientAllocateHostedConnectionResponsetagsTypeDef(
    _ClientAllocateHostedConnectionResponsetagsTypeDef
):
    pass


_ClientAllocateHostedConnectionResponseTypeDef = TypedDict(
    "_ClientAllocateHostedConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientAllocateHostedConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientAllocateHostedConnectionResponseTypeDef(_ClientAllocateHostedConnectionResponseTypeDef):
    """
    - *(dict) --*

      Information about an AWS Direct Connect connection.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the connection.
    """


_RequiredClientAllocateHostedConnectionTagsTypeDef = TypedDict(
    "_RequiredClientAllocateHostedConnectionTagsTypeDef", {"key": str}
)
_OptionalClientAllocateHostedConnectionTagsTypeDef = TypedDict(
    "_OptionalClientAllocateHostedConnectionTagsTypeDef", {"value": str}, total=False
)


class ClientAllocateHostedConnectionTagsTypeDef(
    _RequiredClientAllocateHostedConnectionTagsTypeDef,
    _OptionalClientAllocateHostedConnectionTagsTypeDef,
):
    """
    - *(dict) --*

      Information about a tag.
      - **key** *(string) --***[REQUIRED]**

        The key.
    """


_ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "_ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationtagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationtagsTypeDef(
    _ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationtagsTypeDef
):
    pass


_RequiredClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef",
    {"virtualInterfaceName": str},
)
_OptionalClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef",
    {
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "customerAddress": str,
        "tags": List[
            ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationtagsTypeDef
        ],
    },
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef(
    _RequiredClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef,
    _OptionalClientAllocatePrivateVirtualInterfaceNewPrivateVirtualInterfaceAllocationTypeDef,
):
    """
    Information about the private virtual interface.
    - **virtualInterfaceName** *(string) --***[REQUIRED]**

      The name of the virtual interface assigned by the customer network.
    """


_ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "_ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef(
    _ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef
):
    pass


_ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef(
    _ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef
):
    pass


_ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "_ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef(
    _ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef
):
    pass


_ClientAllocatePrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientAllocatePrivateVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAllocatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientAllocatePrivateVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAllocatePrivateVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)


class ClientAllocatePrivateVirtualInterfaceResponseTypeDef(
    _ClientAllocatePrivateVirtualInterfaceResponseTypeDef
):
    """
    - *(dict) --*

      Information about a virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef(
    _ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef
):
    pass


_ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationtagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationtagsTypeDef(
    _ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationtagsTypeDef
):
    pass


_RequiredClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef",
    {"virtualInterfaceName": str},
)
_OptionalClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef",
    {
        "vlan": int,
        "asn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "routeFilterPrefixes": List[
            ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationrouteFilterPrefixesTypeDef
        ],
        "tags": List[
            ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationtagsTypeDef
        ],
    },
    total=False,
)


class ClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef(
    _RequiredClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef,
    _OptionalClientAllocatePublicVirtualInterfaceNewPublicVirtualInterfaceAllocationTypeDef,
):
    """
    Information about the public virtual interface.
    - **virtualInterfaceName** *(string) --***[REQUIRED]**

      The name of the virtual interface assigned by the customer network.
    """


_ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef(
    _ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef
):
    pass


_ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef(
    _ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef
):
    pass


_ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef(
    _ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef
):
    pass


_ClientAllocatePublicVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientAllocatePublicVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAllocatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientAllocatePublicVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAllocatePublicVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)


class ClientAllocatePublicVirtualInterfaceResponseTypeDef(
    _ClientAllocatePublicVirtualInterfaceResponseTypeDef
):
    """
    - *(dict) --*

      Information about a virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationtagsTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationtagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationtagsTypeDef(
    _ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationtagsTypeDef
):
    pass


_ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "tags": List[
            ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationtagsTypeDef
        ],
    },
    total=False,
)


class ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationTypeDef(
    _ClientAllocateTransitVirtualInterfaceNewTransitVirtualInterfaceAllocationTypeDef
):
    """
    Information about the transit virtual interface.
    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.
    """


_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef(
    _ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef
):
    pass


_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef(
    _ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef
):
    pass


_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef(
    _ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef
):
    pass


_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[
            ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef
        ],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAllocateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef(
    _ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef
):
    """
    - **virtualInterface** *(dict) --*

      Information about a virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_ClientAllocateTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientAllocateTransitVirtualInterfaceResponseTypeDef",
    {"virtualInterface": ClientAllocateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef},
    total=False,
)


class ClientAllocateTransitVirtualInterfaceResponseTypeDef(
    _ClientAllocateTransitVirtualInterfaceResponseTypeDef
):
    """
    - *(dict) --*

      - **virtualInterface** *(dict) --*

        Information about a virtual interface.
        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the virtual interface.
    """


_ClientAssociateConnectionWithLagResponsetagsTypeDef = TypedDict(
    "_ClientAssociateConnectionWithLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientAssociateConnectionWithLagResponsetagsTypeDef(
    _ClientAssociateConnectionWithLagResponsetagsTypeDef
):
    pass


_ClientAssociateConnectionWithLagResponseTypeDef = TypedDict(
    "_ClientAssociateConnectionWithLagResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientAssociateConnectionWithLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientAssociateConnectionWithLagResponseTypeDef(
    _ClientAssociateConnectionWithLagResponseTypeDef
):
    """
    - *(dict) --*

      Information about an AWS Direct Connect connection.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the connection.
    """


_ClientAssociateHostedConnectionResponsetagsTypeDef = TypedDict(
    "_ClientAssociateHostedConnectionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientAssociateHostedConnectionResponsetagsTypeDef(
    _ClientAssociateHostedConnectionResponsetagsTypeDef
):
    pass


_ClientAssociateHostedConnectionResponseTypeDef = TypedDict(
    "_ClientAssociateHostedConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientAssociateHostedConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientAssociateHostedConnectionResponseTypeDef(
    _ClientAssociateHostedConnectionResponseTypeDef
):
    """
    - *(dict) --*

      Information about an AWS Direct Connect connection.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the connection.
    """


_ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "_ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef(
    _ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef
):
    pass


_ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef", {"cidr": str}, total=False
)


class ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef(
    _ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef
):
    pass


_ClientAssociateVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "_ClientAssociateVirtualInterfaceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientAssociateVirtualInterfaceResponsetagsTypeDef(
    _ClientAssociateVirtualInterfaceResponsetagsTypeDef
):
    pass


_ClientAssociateVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientAssociateVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientAssociateVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientAssociateVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientAssociateVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)


class ClientAssociateVirtualInterfaceResponseTypeDef(
    _ClientAssociateVirtualInterfaceResponseTypeDef
):
    """
    - *(dict) --*

      Information about a virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_ClientConfirmConnectionResponseTypeDef = TypedDict(
    "_ClientConfirmConnectionResponseTypeDef",
    {
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)


class ClientConfirmConnectionResponseTypeDef(_ClientConfirmConnectionResponseTypeDef):
    """
    - *(dict) --*

      - **connectionState** *(string) --*

        The state of the connection. The following are the possible values:
        * ``ordering`` : The initial state of a hosted connection provisioned on an interconnect.
        The connection stays in the ordering state until the owner of the hosted connection confirms
        or declines the connection order.
        * ``requested`` : The initial state of a standard connection. The connection stays in the
        requested state until the Letter of Authorization (LOA) is sent to the customer.
        * ``pending`` : The connection has been approved and is being initialized.
        * ``available`` : The network link is up and the connection is ready for use.
        * ``down`` : The network link is down.
        * ``deleting`` : The connection is being deleted.
        * ``deleted`` : The connection has been deleted.
        * ``rejected`` : A hosted connection in the ``ordering`` state enters the ``rejected`` state
        if it is deleted by the customer.
        * ``unknown`` : The state of the connection is not available.
    """


_ClientConfirmPrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientConfirmPrivateVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)


class ClientConfirmPrivateVirtualInterfaceResponseTypeDef(
    _ClientConfirmPrivateVirtualInterfaceResponseTypeDef
):
    """
    - *(dict) --*

      - **virtualInterfaceState** *(string) --*

        The state of the virtual interface. The following are the possible values:
        * ``confirming`` : The creation of the virtual interface is pending confirmation from the
        virtual interface owner. If the owner of the virtual interface is different from the owner
        of the connection on which it is provisioned, then the virtual interface will remain in this
        state until it is confirmed by the virtual interface owner.
        * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
        interface needs validation before the virtual interface can be created.
        * ``pending`` : A virtual interface is in this state from the time that it is created until
        the virtual interface is ready to forward traffic.
        * ``available`` : A virtual interface that is able to forward traffic.
        * ``down`` : A virtual interface that is BGP down.
        * ``deleting`` : A virtual interface is in this state immediately after calling
        DeleteVirtualInterface until it can no longer forward traffic.
        * ``deleted`` : A virtual interface that cannot forward traffic.
        * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
        If a virtual interface in the ``Confirming`` state is deleted by the virtual interface
        owner, the virtual interface enters the ``Rejected`` state.
        * ``unknown`` : The state of the virtual interface is not available.
    """


_ClientConfirmPublicVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientConfirmPublicVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)


class ClientConfirmPublicVirtualInterfaceResponseTypeDef(
    _ClientConfirmPublicVirtualInterfaceResponseTypeDef
):
    """
    - *(dict) --*

      - **virtualInterfaceState** *(string) --*

        The state of the virtual interface. The following are the possible values:
        * ``confirming`` : The creation of the virtual interface is pending confirmation from the
        virtual interface owner. If the owner of the virtual interface is different from the owner
        of the connection on which it is provisioned, then the virtual interface will remain in this
        state until it is confirmed by the virtual interface owner.
        * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
        interface needs validation before the virtual interface can be created.
        * ``pending`` : A virtual interface is in this state from the time that it is created until
        the virtual interface is ready to forward traffic.
        * ``available`` : A virtual interface that is able to forward traffic.
        * ``down`` : A virtual interface that is BGP down.
        * ``deleting`` : A virtual interface is in this state immediately after calling
        DeleteVirtualInterface until it can no longer forward traffic.
        * ``deleted`` : A virtual interface that cannot forward traffic.
        * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
        If a virtual interface in the ``Confirming`` state is deleted by the virtual interface
        owner, the virtual interface enters the ``Rejected`` state.
        * ``unknown`` : The state of the virtual interface is not available.
    """


_ClientConfirmTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientConfirmTransitVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)


class ClientConfirmTransitVirtualInterfaceResponseTypeDef(
    _ClientConfirmTransitVirtualInterfaceResponseTypeDef
):
    """
    - *(dict) --*

      - **virtualInterfaceState** *(string) --*

        The state of the virtual interface. The following are the possible values:
        * ``confirming`` : The creation of the virtual interface is pending confirmation from the
        virtual interface owner. If the owner of the virtual interface is different from the owner
        of the connection on which it is provisioned, then the virtual interface will remain in this
        state until it is confirmed by the virtual interface owner.
        * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
        interface needs validation before the virtual interface can be created.
        * ``pending`` : A virtual interface is in this state from the time that it is created until
        the virtual interface is ready to forward traffic.
        * ``available`` : A virtual interface that is able to forward traffic.
        * ``down`` : A virtual interface that is BGP down.
        * ``deleting`` : A virtual interface is in this state immediately after calling
        DeleteVirtualInterface until it can no longer forward traffic.
        * ``deleted`` : A virtual interface that cannot forward traffic.
        * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
        If a virtual interface in the ``Confirming`` state is deleted by the virtual interface
        owner, the virtual interface enters the ``Rejected`` state.
        * ``unknown`` : The state of the virtual interface is not available.
    """


_ClientCreateBgpPeerNewBGPPeerTypeDef = TypedDict(
    "_ClientCreateBgpPeerNewBGPPeerTypeDef",
    {
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
    },
    total=False,
)


class ClientCreateBgpPeerNewBGPPeerTypeDef(_ClientCreateBgpPeerNewBGPPeerTypeDef):
    """
    Information about the BGP peer.
    - **asn** *(integer) --*

      The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
    """


_ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "_ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef(
    _ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef
):
    pass


_ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "_ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef(
    _ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef
):
    pass


_ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef = TypedDict(
    "_ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef(
    _ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef
):
    pass


_ClientCreateBgpPeerResponsevirtualInterfaceTypeDef = TypedDict(
    "_ClientCreateBgpPeerResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreateBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientCreateBgpPeerResponsevirtualInterfacebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreateBgpPeerResponsevirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientCreateBgpPeerResponsevirtualInterfaceTypeDef(
    _ClientCreateBgpPeerResponsevirtualInterfaceTypeDef
):
    """
    - **virtualInterface** *(dict) --*

      The virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_ClientCreateBgpPeerResponseTypeDef = TypedDict(
    "_ClientCreateBgpPeerResponseTypeDef",
    {"virtualInterface": ClientCreateBgpPeerResponsevirtualInterfaceTypeDef},
    total=False,
)


class ClientCreateBgpPeerResponseTypeDef(_ClientCreateBgpPeerResponseTypeDef):
    """
    - *(dict) --*

      - **virtualInterface** *(dict) --*

        The virtual interface.
        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the virtual interface.
    """


_ClientCreateConnectionResponsetagsTypeDef = TypedDict(
    "_ClientCreateConnectionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateConnectionResponsetagsTypeDef(_ClientCreateConnectionResponsetagsTypeDef):
    pass


_ClientCreateConnectionResponseTypeDef = TypedDict(
    "_ClientCreateConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientCreateConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientCreateConnectionResponseTypeDef(_ClientCreateConnectionResponseTypeDef):
    """
    - *(dict) --*

      Information about an AWS Direct Connect connection.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the connection.
    """


_RequiredClientCreateConnectionTagsTypeDef = TypedDict(
    "_RequiredClientCreateConnectionTagsTypeDef", {"key": str}
)
_OptionalClientCreateConnectionTagsTypeDef = TypedDict(
    "_OptionalClientCreateConnectionTagsTypeDef", {"value": str}, total=False
)


class ClientCreateConnectionTagsTypeDef(
    _RequiredClientCreateConnectionTagsTypeDef, _OptionalClientCreateConnectionTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag.
      - **key** *(string) --***[REQUIRED]**

        The key.
    """


_ClientCreateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    - *(dict) --*

      Information about a route filter prefix that a customer can advertise through Border Gateway
      Protocol (BGP) over a public virtual interface.
      - **cidr** *(string) --*

        The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
        must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayAssociationProposalAddAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalAddAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalAddAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    - *(dict) --*

      Information about a route filter prefix that a customer can advertise through Border Gateway
      Protocol (BGP) over a public virtual interface.
      - **cidr** *(string) --*

        The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
        must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayAssociationProposalRemoveAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalRemoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalRemoveAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalRemoveAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    - *(dict) --*

      Information about a route filter prefix that a customer can advertise through Border Gateway
      Protocol (BGP) over a public virtual interface.
      - **cidr** *(string) --*

        The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
        must use /64 or shorter.
    """


_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef
):
    pass


_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": Literal["requested", "accepted", "deleted"],
        "associatedGateway": ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef,
        "existingAllowedPrefixesToDirectConnectGateway": List[
            ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "requestedAllowedPrefixesToDirectConnectGateway": List[
            ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
    },
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef
):
    """
    - **directConnectGatewayAssociationProposal** *(dict) --*

      Information about the Direct Connect gateway proposal.
      - **proposalId** *(string) --*

        The ID of the association proposal.
    """


_ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef",
    {
        "directConnectGatewayAssociationProposal": ClientCreateDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef
    },
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef(
    _ClientCreateDirectConnectGatewayAssociationProposalResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAssociationProposal** *(dict) --*

        Information about the Direct Connect gateway proposal.
        - **proposalId** *(string) --*

          The ID of the association proposal.
    """


_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef(
    _ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef
):
    pass


_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef(
    _ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
):
    """
    - **directConnectGatewayAssociation** *(dict) --*

      The association to be created.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_ClientCreateDirectConnectGatewayAssociationResponseTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayAssociationResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientCreateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)


class ClientCreateDirectConnectGatewayAssociationResponseTypeDef(
    _ClientCreateDirectConnectGatewayAssociationResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAssociation** *(dict) --*

        The association to be created.
        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.
    """


_ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": Literal["pending", "available", "deleting", "deleted"],
        "stateChangeError": str,
    },
    total=False,
)


class ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef(
    _ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef
):
    """
    - **directConnectGateway** *(dict) --*

      The Direct Connect gateway.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_ClientCreateDirectConnectGatewayResponseTypeDef = TypedDict(
    "_ClientCreateDirectConnectGatewayResponseTypeDef",
    {"directConnectGateway": ClientCreateDirectConnectGatewayResponsedirectConnectGatewayTypeDef},
    total=False,
)


class ClientCreateDirectConnectGatewayResponseTypeDef(
    _ClientCreateDirectConnectGatewayResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGateway** *(dict) --*

        The Direct Connect gateway.
        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.
    """


_ClientCreateInterconnectResponsetagsTypeDef = TypedDict(
    "_ClientCreateInterconnectResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateInterconnectResponsetagsTypeDef(_ClientCreateInterconnectResponsetagsTypeDef):
    pass


_ClientCreateInterconnectResponseTypeDef = TypedDict(
    "_ClientCreateInterconnectResponseTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientCreateInterconnectResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientCreateInterconnectResponseTypeDef(_ClientCreateInterconnectResponseTypeDef):
    """
    - *(dict) --*

      Information about an interconnect.
      - **interconnectId** *(string) --*

        The ID of the interconnect.
    """


_RequiredClientCreateInterconnectTagsTypeDef = TypedDict(
    "_RequiredClientCreateInterconnectTagsTypeDef", {"key": str}
)
_OptionalClientCreateInterconnectTagsTypeDef = TypedDict(
    "_OptionalClientCreateInterconnectTagsTypeDef", {"value": str}, total=False
)


class ClientCreateInterconnectTagsTypeDef(
    _RequiredClientCreateInterconnectTagsTypeDef, _OptionalClientCreateInterconnectTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag.
      - **key** *(string) --***[REQUIRED]**

        The key.
    """


_RequiredClientCreateLagChildConnectionTagsTypeDef = TypedDict(
    "_RequiredClientCreateLagChildConnectionTagsTypeDef", {"key": str}
)
_OptionalClientCreateLagChildConnectionTagsTypeDef = TypedDict(
    "_OptionalClientCreateLagChildConnectionTagsTypeDef", {"value": str}, total=False
)


class ClientCreateLagChildConnectionTagsTypeDef(
    _RequiredClientCreateLagChildConnectionTagsTypeDef,
    _OptionalClientCreateLagChildConnectionTagsTypeDef,
):
    """
    - *(dict) --*

      Information about a tag.
      - **key** *(string) --***[REQUIRED]**

        The key.
    """


_ClientCreateLagResponseconnectionstagsTypeDef = TypedDict(
    "_ClientCreateLagResponseconnectionstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateLagResponseconnectionstagsTypeDef(_ClientCreateLagResponseconnectionstagsTypeDef):
    pass


_ClientCreateLagResponseconnectionsTypeDef = TypedDict(
    "_ClientCreateLagResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientCreateLagResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientCreateLagResponseconnectionsTypeDef(_ClientCreateLagResponseconnectionsTypeDef):
    pass


_ClientCreateLagResponsetagsTypeDef = TypedDict(
    "_ClientCreateLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateLagResponsetagsTypeDef(_ClientCreateLagResponsetagsTypeDef):
    pass


_ClientCreateLagResponseTypeDef = TypedDict(
    "_ClientCreateLagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientCreateLagResponseconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientCreateLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientCreateLagResponseTypeDef(_ClientCreateLagResponseTypeDef):
    """
    - *(dict) --*

      Information about a link aggregation group (LAG).
      - **connectionsBandwidth** *(string) --*

        The individual bandwidth of the physical connections bundled by the LAG. The possible values
        are 1Gbps and 10Gbps.
    """


_RequiredClientCreateLagTagsTypeDef = TypedDict("_RequiredClientCreateLagTagsTypeDef", {"key": str})
_OptionalClientCreateLagTagsTypeDef = TypedDict(
    "_OptionalClientCreateLagTagsTypeDef", {"value": str}, total=False
)


class ClientCreateLagTagsTypeDef(
    _RequiredClientCreateLagTagsTypeDef, _OptionalClientCreateLagTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag.
      - **key** *(string) --***[REQUIRED]**

        The key.
    """


_ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfacetagsTypeDef = TypedDict(
    "_ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfacetagsTypeDef(
    _ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfacetagsTypeDef
):
    pass


_RequiredClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_RequiredClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef",
    {"virtualInterfaceName": str},
)
_OptionalClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_OptionalClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef",
    {
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "tags": List[ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef(
    _RequiredClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef,
    _OptionalClientCreatePrivateVirtualInterfaceNewPrivateVirtualInterfaceTypeDef,
):
    """
    Information about the private virtual interface.
    - **virtualInterfaceName** *(string) --***[REQUIRED]**

      The name of the virtual interface assigned by the customer network.
    """


_ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "_ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef(
    _ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef
):
    pass


_ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef(
    _ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef
):
    pass


_ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "_ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef(
    _ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef
):
    pass


_ClientCreatePrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientCreatePrivateVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreatePrivateVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientCreatePrivateVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreatePrivateVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)


class ClientCreatePrivateVirtualInterfaceResponseTypeDef(
    _ClientCreatePrivateVirtualInterfaceResponseTypeDef
):
    """
    - *(dict) --*

      Information about a virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacerouteFilterPrefixesTypeDef(
    _ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacerouteFilterPrefixesTypeDef
):
    pass


_ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacetagsTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacetagsTypeDef(
    _ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacetagsTypeDef
):
    pass


_RequiredClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef = TypedDict(
    "_RequiredClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef",
    {"virtualInterfaceName": str},
)
_OptionalClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef = TypedDict(
    "_OptionalClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef",
    {
        "vlan": int,
        "asn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "routeFilterPrefixes": List[
            ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "tags": List[ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef(
    _RequiredClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef,
    _OptionalClientCreatePublicVirtualInterfaceNewPublicVirtualInterfaceTypeDef,
):
    """
    Information about the public virtual interface.
    - **virtualInterfaceName** *(string) --***[REQUIRED]**

      The name of the virtual interface assigned by the customer network.
    """


_ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef(
    _ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef
):
    pass


_ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef(
    _ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef
):
    pass


_ClientCreatePublicVirtualInterfaceResponsetagsTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfaceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreatePublicVirtualInterfaceResponsetagsTypeDef(
    _ClientCreatePublicVirtualInterfaceResponsetagsTypeDef
):
    pass


_ClientCreatePublicVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientCreatePublicVirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreatePublicVirtualInterfaceResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientCreatePublicVirtualInterfaceResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreatePublicVirtualInterfaceResponsetagsTypeDef],
    },
    total=False,
)


class ClientCreatePublicVirtualInterfaceResponseTypeDef(
    _ClientCreatePublicVirtualInterfaceResponseTypeDef
):
    """
    - *(dict) --*

      Information about a virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfacetagsTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfacetagsTypeDef(
    _ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfacetagsTypeDef
):
    pass


_ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfaceTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "directConnectGatewayId": str,
        "tags": List[ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfaceTypeDef(
    _ClientCreateTransitVirtualInterfaceNewTransitVirtualInterfaceTypeDef
):
    """
    Information about the transit virtual interface.
    - **virtualInterfaceName** *(string) --*

      The name of the virtual interface assigned by the customer network.
    """


_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef(
    _ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef
):
    pass


_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef(
    _ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef
):
    pass


_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef(
    _ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef
):
    pass


_ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientCreateTransitVirtualInterfaceResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[
            ClientCreateTransitVirtualInterfaceResponsevirtualInterfacebgpPeersTypeDef
        ],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientCreateTransitVirtualInterfaceResponsevirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef(
    _ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef
):
    """
    - **virtualInterface** *(dict) --*

      Information about a virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_ClientCreateTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientCreateTransitVirtualInterfaceResponseTypeDef",
    {"virtualInterface": ClientCreateTransitVirtualInterfaceResponsevirtualInterfaceTypeDef},
    total=False,
)


class ClientCreateTransitVirtualInterfaceResponseTypeDef(
    _ClientCreateTransitVirtualInterfaceResponseTypeDef
):
    """
    - *(dict) --*

      - **virtualInterface** *(dict) --*

        Information about a virtual interface.
        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the virtual interface.
    """


_ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef = TypedDict(
    "_ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef(
    _ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef
):
    pass


_ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef = TypedDict(
    "_ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef(
    _ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef
):
    pass


_ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef = TypedDict(
    "_ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef(
    _ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef
):
    pass


_ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef = TypedDict(
    "_ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientDeleteBgpPeerResponsevirtualInterfacerouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientDeleteBgpPeerResponsevirtualInterfacebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientDeleteBgpPeerResponsevirtualInterfacetagsTypeDef],
    },
    total=False,
)


class ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef(
    _ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef
):
    """
    - **virtualInterface** *(dict) --*

      The virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_ClientDeleteBgpPeerResponseTypeDef = TypedDict(
    "_ClientDeleteBgpPeerResponseTypeDef",
    {"virtualInterface": ClientDeleteBgpPeerResponsevirtualInterfaceTypeDef},
    total=False,
)


class ClientDeleteBgpPeerResponseTypeDef(_ClientDeleteBgpPeerResponseTypeDef):
    """
    - *(dict) --*

      - **virtualInterface** *(dict) --*

        The virtual interface.
        - **ownerAccount** *(string) --*

          The ID of the AWS account that owns the virtual interface.
    """


_ClientDeleteConnectionResponsetagsTypeDef = TypedDict(
    "_ClientDeleteConnectionResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDeleteConnectionResponsetagsTypeDef(_ClientDeleteConnectionResponsetagsTypeDef):
    pass


_ClientDeleteConnectionResponseTypeDef = TypedDict(
    "_ClientDeleteConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDeleteConnectionResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDeleteConnectionResponseTypeDef(_ClientDeleteConnectionResponseTypeDef):
    """
    - *(dict) --*

      Information about an AWS Direct Connect connection.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the connection.
    """


_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef
):
    pass


_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": Literal["requested", "accepted", "deleted"],
        "associatedGateway": ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalassociatedGatewayTypeDef,
        "existingAllowedPrefixesToDirectConnectGateway": List[
            ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalexistingAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "requestedAllowedPrefixesToDirectConnectGateway": List[
            ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef
):
    """
    - **directConnectGatewayAssociationProposal** *(dict) --*

      The ID of the associated gateway.
      - **proposalId** *(string) --*

        The ID of the association proposal.
    """


_ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef",
    {
        "directConnectGatewayAssociationProposal": ClientDeleteDirectConnectGatewayAssociationProposalResponsedirectConnectGatewayAssociationProposalTypeDef
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationProposalResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAssociationProposal** *(dict) --*

        The ID of the associated gateway.
        - **proposalId** *(string) --*

          The ID of the association proposal.
    """


_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef
):
    pass


_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
):
    """
    - **directConnectGatewayAssociation** *(dict) --*

      Information about the deleted association.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_ClientDeleteDirectConnectGatewayAssociationResponseTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayAssociationResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientDeleteDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayAssociationResponseTypeDef(
    _ClientDeleteDirectConnectGatewayAssociationResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAssociation** *(dict) --*

        Information about the deleted association.
        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.
    """


_ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": Literal["pending", "available", "deleting", "deleted"],
        "stateChangeError": str,
    },
    total=False,
)


class ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef(
    _ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef
):
    """
    - **directConnectGateway** *(dict) --*

      The Direct Connect gateway.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_ClientDeleteDirectConnectGatewayResponseTypeDef = TypedDict(
    "_ClientDeleteDirectConnectGatewayResponseTypeDef",
    {"directConnectGateway": ClientDeleteDirectConnectGatewayResponsedirectConnectGatewayTypeDef},
    total=False,
)


class ClientDeleteDirectConnectGatewayResponseTypeDef(
    _ClientDeleteDirectConnectGatewayResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGateway** *(dict) --*

        The Direct Connect gateway.
        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.
    """


_ClientDeleteInterconnectResponseTypeDef = TypedDict(
    "_ClientDeleteInterconnectResponseTypeDef",
    {
        "interconnectState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ]
    },
    total=False,
)


class ClientDeleteInterconnectResponseTypeDef(_ClientDeleteInterconnectResponseTypeDef):
    """
    - *(dict) --*

      - **interconnectState** *(string) --*

        The state of the interconnect. The following are the possible values:
        * ``requested`` : The initial state of an interconnect. The interconnect stays in the
        requested state until the Letter of Authorization (LOA) is sent to the customer.
        * ``pending`` : The interconnect is approved, and is being initialized.
        * ``available`` : The network link is up, and the interconnect is ready for use.
        * ``down`` : The network link is down.
        * ``deleting`` : The interconnect is being deleted.
        * ``deleted`` : The interconnect is deleted.
        * ``unknown`` : The state of the interconnect is not available.
    """


_ClientDeleteLagResponseconnectionstagsTypeDef = TypedDict(
    "_ClientDeleteLagResponseconnectionstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDeleteLagResponseconnectionstagsTypeDef(_ClientDeleteLagResponseconnectionstagsTypeDef):
    pass


_ClientDeleteLagResponseconnectionsTypeDef = TypedDict(
    "_ClientDeleteLagResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDeleteLagResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDeleteLagResponseconnectionsTypeDef(_ClientDeleteLagResponseconnectionsTypeDef):
    pass


_ClientDeleteLagResponsetagsTypeDef = TypedDict(
    "_ClientDeleteLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDeleteLagResponsetagsTypeDef(_ClientDeleteLagResponsetagsTypeDef):
    pass


_ClientDeleteLagResponseTypeDef = TypedDict(
    "_ClientDeleteLagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientDeleteLagResponseconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDeleteLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDeleteLagResponseTypeDef(_ClientDeleteLagResponseTypeDef):
    """
    - *(dict) --*

      Information about a link aggregation group (LAG).
      - **connectionsBandwidth** *(string) --*

        The individual bandwidth of the physical connections bundled by the LAG. The possible values
        are 1Gbps and 10Gbps.
    """


_ClientDeleteVirtualInterfaceResponseTypeDef = TypedDict(
    "_ClientDeleteVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)


class ClientDeleteVirtualInterfaceResponseTypeDef(_ClientDeleteVirtualInterfaceResponseTypeDef):
    """
    - *(dict) --*

      - **virtualInterfaceState** *(string) --*

        The state of the virtual interface. The following are the possible values:
        * ``confirming`` : The creation of the virtual interface is pending confirmation from the
        virtual interface owner. If the owner of the virtual interface is different from the owner
        of the connection on which it is provisioned, then the virtual interface will remain in this
        state until it is confirmed by the virtual interface owner.
        * ``verifying`` : This state only applies to public virtual interfaces. Each public virtual
        interface needs validation before the virtual interface can be created.
        * ``pending`` : A virtual interface is in this state from the time that it is created until
        the virtual interface is ready to forward traffic.
        * ``available`` : A virtual interface that is able to forward traffic.
        * ``down`` : A virtual interface that is BGP down.
        * ``deleting`` : A virtual interface is in this state immediately after calling
        DeleteVirtualInterface until it can no longer forward traffic.
        * ``deleted`` : A virtual interface that cannot forward traffic.
        * ``rejected`` : The virtual interface owner has declined creation of the virtual interface.
        If a virtual interface in the ``Confirming`` state is deleted by the virtual interface
        owner, the virtual interface enters the ``Rejected`` state.
        * ``unknown`` : The state of the virtual interface is not available.
    """


_ClientDescribeConnectionLoaResponseloaTypeDef = TypedDict(
    "_ClientDescribeConnectionLoaResponseloaTypeDef",
    {"loaContent": bytes, "loaContentType": str},
    total=False,
)


class ClientDescribeConnectionLoaResponseloaTypeDef(_ClientDescribeConnectionLoaResponseloaTypeDef):
    """
    - **loa** *(dict) --*

      The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).
      - **loaContent** *(bytes) --*

        The binary contents of the LOA-CFA document.
    """


_ClientDescribeConnectionLoaResponseTypeDef = TypedDict(
    "_ClientDescribeConnectionLoaResponseTypeDef",
    {"loa": ClientDescribeConnectionLoaResponseloaTypeDef},
    total=False,
)


class ClientDescribeConnectionLoaResponseTypeDef(_ClientDescribeConnectionLoaResponseTypeDef):
    """
    - *(dict) --*

      - **loa** *(dict) --*

        The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).
        - **loaContent** *(bytes) --*

          The binary contents of the LOA-CFA document.
    """


_ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef = TypedDict(
    "_ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef(
    _ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef
):
    pass


_ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef = TypedDict(
    "_ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeConnectionsOnInterconnectResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef(
    _ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef
):
    """
    - *(dict) --*

      Information about an AWS Direct Connect connection.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the connection.
    """


_ClientDescribeConnectionsOnInterconnectResponseTypeDef = TypedDict(
    "_ClientDescribeConnectionsOnInterconnectResponseTypeDef",
    {"connections": List[ClientDescribeConnectionsOnInterconnectResponseconnectionsTypeDef]},
    total=False,
)


class ClientDescribeConnectionsOnInterconnectResponseTypeDef(
    _ClientDescribeConnectionsOnInterconnectResponseTypeDef
):
    """
    - *(dict) --*

      - **connections** *(list) --*

        The connections.
        - *(dict) --*

          Information about an AWS Direct Connect connection.
          - **ownerAccount** *(string) --*

            The ID of the AWS account that owns the connection.
    """


_ClientDescribeConnectionsResponseconnectionstagsTypeDef = TypedDict(
    "_ClientDescribeConnectionsResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeConnectionsResponseconnectionstagsTypeDef(
    _ClientDescribeConnectionsResponseconnectionstagsTypeDef
):
    pass


_ClientDescribeConnectionsResponseconnectionsTypeDef = TypedDict(
    "_ClientDescribeConnectionsResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeConnectionsResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeConnectionsResponseconnectionsTypeDef(
    _ClientDescribeConnectionsResponseconnectionsTypeDef
):
    """
    - *(dict) --*

      Information about an AWS Direct Connect connection.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the connection.
    """


_ClientDescribeConnectionsResponseTypeDef = TypedDict(
    "_ClientDescribeConnectionsResponseTypeDef",
    {"connections": List[ClientDescribeConnectionsResponseconnectionsTypeDef]},
    total=False,
)


class ClientDescribeConnectionsResponseTypeDef(_ClientDescribeConnectionsResponseTypeDef):
    """
    - *(dict) --*

      - **connections** *(list) --*

        The connections.
        - *(dict) --*

          Information about an AWS Direct Connect connection.
          - **ownerAccount** *(string) --*

            The ID of the AWS account that owns the connection.
    """


_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef
):
    pass


_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": Literal["requested", "accepted", "deleted"],
        "associatedGateway": ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsassociatedGatewayTypeDef,
        "existingAllowedPrefixesToDirectConnectGateway": List[
            ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsexistingAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "requestedAllowedPrefixesToDirectConnectGateway": List[
            ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsrequestedAllowedPrefixesToDirectConnectGatewayTypeDef
        ],
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef
):
    """
    - *(dict) --*

      Information about the proposal request to attach a virtual private gateway to a Direct Connect
      gateway.
      - **proposalId** *(string) --*

        The ID of the association proposal.
    """


_ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef",
    {
        "directConnectGatewayAssociationProposals": List[
            ClientDescribeDirectConnectGatewayAssociationProposalsResponsedirectConnectGatewayAssociationProposalsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationProposalsResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAssociationProposals** *(list) --*

        Describes the Direct Connect gateway association proposals.
        - *(dict) --*

          Information about the proposal request to attach a virtual private gateway to a Direct
          Connect gateway.
          - **proposalId** *(string) --*

            The ID of the association proposal.
    """


_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef
):
    pass


_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef
):
    """
    - *(dict) --*

      Information about an association between a Direct Connect gateway and a virtual private
      gateway or transit gateway.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef",
    {
        "directConnectGatewayAssociations": List[
            ClientDescribeDirectConnectGatewayAssociationsResponsedirectConnectGatewayAssociationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef(
    _ClientDescribeDirectConnectGatewayAssociationsResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAssociations** *(list) --*

        Information about the associations.
        - *(dict) --*

          Information about an association between a Direct Connect gateway and a virtual private
          gateway or transit gateway.
          - **directConnectGatewayId** *(string) --*

            The ID of the Direct Connect gateway.
    """


_ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef",
    {
        "directConnectGatewayId": str,
        "virtualInterfaceId": str,
        "virtualInterfaceRegion": str,
        "virtualInterfaceOwnerAccount": str,
        "attachmentState": Literal["attaching", "attached", "detaching", "detached"],
        "attachmentType": Literal["TransitVirtualInterface", "PrivateVirtualInterface"],
        "stateChangeError": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef(
    _ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef
):
    """
    - *(dict) --*

      Information about an attachment between a Direct Connect gateway and a virtual interface.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef",
    {
        "directConnectGatewayAttachments": List[
            ClientDescribeDirectConnectGatewayAttachmentsResponsedirectConnectGatewayAttachmentsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef(
    _ClientDescribeDirectConnectGatewayAttachmentsResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAttachments** *(list) --*

        The attachments.
        - *(dict) --*

          Information about an attachment between a Direct Connect gateway and a virtual interface.
          - **directConnectGatewayId** *(string) --*

            The ID of the Direct Connect gateway.
    """


_ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": Literal["pending", "available", "deleting", "deleted"],
        "stateChangeError": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef(
    _ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef
):
    """
    - *(dict) --*

      Information about a Direct Connect gateway, which enables you to connect virtual interfaces
      and virtual private gateway or transit gateways.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_ClientDescribeDirectConnectGatewaysResponseTypeDef = TypedDict(
    "_ClientDescribeDirectConnectGatewaysResponseTypeDef",
    {
        "directConnectGateways": List[
            ClientDescribeDirectConnectGatewaysResponsedirectConnectGatewaysTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeDirectConnectGatewaysResponseTypeDef(
    _ClientDescribeDirectConnectGatewaysResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGateways** *(list) --*

        The Direct Connect gateways.
        - *(dict) --*

          Information about a Direct Connect gateway, which enables you to connect virtual
          interfaces and virtual private gateway or transit gateways.
          - **directConnectGatewayId** *(string) --*

            The ID of the Direct Connect gateway.
    """


_ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef = TypedDict(
    "_ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef(
    _ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef
):
    pass


_ClientDescribeHostedConnectionsResponseconnectionsTypeDef = TypedDict(
    "_ClientDescribeHostedConnectionsResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeHostedConnectionsResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeHostedConnectionsResponseconnectionsTypeDef(
    _ClientDescribeHostedConnectionsResponseconnectionsTypeDef
):
    """
    - *(dict) --*

      Information about an AWS Direct Connect connection.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the connection.
    """


_ClientDescribeHostedConnectionsResponseTypeDef = TypedDict(
    "_ClientDescribeHostedConnectionsResponseTypeDef",
    {"connections": List[ClientDescribeHostedConnectionsResponseconnectionsTypeDef]},
    total=False,
)


class ClientDescribeHostedConnectionsResponseTypeDef(
    _ClientDescribeHostedConnectionsResponseTypeDef
):
    """
    - *(dict) --*

      - **connections** *(list) --*

        The connections.
        - *(dict) --*

          Information about an AWS Direct Connect connection.
          - **ownerAccount** *(string) --*

            The ID of the AWS account that owns the connection.
    """


_ClientDescribeInterconnectLoaResponseloaTypeDef = TypedDict(
    "_ClientDescribeInterconnectLoaResponseloaTypeDef",
    {"loaContent": bytes, "loaContentType": str},
    total=False,
)


class ClientDescribeInterconnectLoaResponseloaTypeDef(
    _ClientDescribeInterconnectLoaResponseloaTypeDef
):
    """
    - **loa** *(dict) --*

      The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).
      - **loaContent** *(bytes) --*

        The binary contents of the LOA-CFA document.
    """


_ClientDescribeInterconnectLoaResponseTypeDef = TypedDict(
    "_ClientDescribeInterconnectLoaResponseTypeDef",
    {"loa": ClientDescribeInterconnectLoaResponseloaTypeDef},
    total=False,
)


class ClientDescribeInterconnectLoaResponseTypeDef(_ClientDescribeInterconnectLoaResponseTypeDef):
    """
    - *(dict) --*

      - **loa** *(dict) --*

        The Letter of Authorization - Connecting Facility Assignment (LOA-CFA).
        - **loaContent** *(bytes) --*

          The binary contents of the LOA-CFA document.
    """


_ClientDescribeInterconnectsResponseinterconnectstagsTypeDef = TypedDict(
    "_ClientDescribeInterconnectsResponseinterconnectstagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeInterconnectsResponseinterconnectstagsTypeDef(
    _ClientDescribeInterconnectsResponseinterconnectstagsTypeDef
):
    pass


_ClientDescribeInterconnectsResponseinterconnectsTypeDef = TypedDict(
    "_ClientDescribeInterconnectsResponseinterconnectsTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeInterconnectsResponseinterconnectstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeInterconnectsResponseinterconnectsTypeDef(
    _ClientDescribeInterconnectsResponseinterconnectsTypeDef
):
    """
    - *(dict) --*

      Information about an interconnect.
      - **interconnectId** *(string) --*

        The ID of the interconnect.
    """


_ClientDescribeInterconnectsResponseTypeDef = TypedDict(
    "_ClientDescribeInterconnectsResponseTypeDef",
    {"interconnects": List[ClientDescribeInterconnectsResponseinterconnectsTypeDef]},
    total=False,
)


class ClientDescribeInterconnectsResponseTypeDef(_ClientDescribeInterconnectsResponseTypeDef):
    """
    - *(dict) --*

      - **interconnects** *(list) --*

        The interconnects.
        - *(dict) --*

          Information about an interconnect.
          - **interconnectId** *(string) --*

            The ID of the interconnect.
    """


_ClientDescribeLagsResponselagsconnectionstagsTypeDef = TypedDict(
    "_ClientDescribeLagsResponselagsconnectionstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDescribeLagsResponselagsconnectionstagsTypeDef(
    _ClientDescribeLagsResponselagsconnectionstagsTypeDef
):
    pass


_ClientDescribeLagsResponselagsconnectionsTypeDef = TypedDict(
    "_ClientDescribeLagsResponselagsconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeLagsResponselagsconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeLagsResponselagsconnectionsTypeDef(
    _ClientDescribeLagsResponselagsconnectionsTypeDef
):
    pass


_ClientDescribeLagsResponselagstagsTypeDef = TypedDict(
    "_ClientDescribeLagsResponselagstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDescribeLagsResponselagstagsTypeDef(_ClientDescribeLagsResponselagstagsTypeDef):
    pass


_ClientDescribeLagsResponselagsTypeDef = TypedDict(
    "_ClientDescribeLagsResponselagsTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientDescribeLagsResponselagsconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDescribeLagsResponselagstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDescribeLagsResponselagsTypeDef(_ClientDescribeLagsResponselagsTypeDef):
    """
    - *(dict) --*

      Information about a link aggregation group (LAG).
      - **connectionsBandwidth** *(string) --*

        The individual bandwidth of the physical connections bundled by the LAG. The possible values
        are 1Gbps and 10Gbps.
    """


_ClientDescribeLagsResponseTypeDef = TypedDict(
    "_ClientDescribeLagsResponseTypeDef",
    {"lags": List[ClientDescribeLagsResponselagsTypeDef]},
    total=False,
)


class ClientDescribeLagsResponseTypeDef(_ClientDescribeLagsResponseTypeDef):
    """
    - *(dict) --*

      - **lags** *(list) --*

        The LAGs.
        - *(dict) --*

          Information about a link aggregation group (LAG).
          - **connectionsBandwidth** *(string) --*

            The individual bandwidth of the physical connections bundled by the LAG. The possible
            values are 1Gbps and 10Gbps.
    """


_ClientDescribeLoaResponseTypeDef = TypedDict(
    "_ClientDescribeLoaResponseTypeDef", {"loaContent": bytes, "loaContentType": str}, total=False
)


class ClientDescribeLoaResponseTypeDef(_ClientDescribeLoaResponseTypeDef):
    """
    - *(dict) --*

      Information about a Letter of Authorization - Connecting Facility Assignment (LOA-CFA) for a
      connection.
      - **loaContent** *(bytes) --*

        The binary contents of the LOA-CFA document.
    """


_ClientDescribeLocationsResponselocationsTypeDef = TypedDict(
    "_ClientDescribeLocationsResponselocationsTypeDef",
    {
        "locationCode": str,
        "locationName": str,
        "region": str,
        "availablePortSpeeds": List[str],
        "availableProviders": List[str],
    },
    total=False,
)


class ClientDescribeLocationsResponselocationsTypeDef(
    _ClientDescribeLocationsResponselocationsTypeDef
):
    """
    - *(dict) --*

      Information about an AWS Direct Connect location.
      - **locationCode** *(string) --*

        The code for the location.
    """


_ClientDescribeLocationsResponseTypeDef = TypedDict(
    "_ClientDescribeLocationsResponseTypeDef",
    {"locations": List[ClientDescribeLocationsResponselocationsTypeDef]},
    total=False,
)


class ClientDescribeLocationsResponseTypeDef(_ClientDescribeLocationsResponseTypeDef):
    """
    - *(dict) --*

      - **locations** *(list) --*

        The locations.
        - *(dict) --*

          Information about an AWS Direct Connect location.
          - **locationCode** *(string) --*

            The code for the location.
    """


_ClientDescribeTagsResponseresourceTagstagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseresourceTagstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientDescribeTagsResponseresourceTagstagsTypeDef(
    _ClientDescribeTagsResponseresourceTagstagsTypeDef
):
    pass


_ClientDescribeTagsResponseresourceTagsTypeDef = TypedDict(
    "_ClientDescribeTagsResponseresourceTagsTypeDef",
    {"resourceArn": str, "tags": List[ClientDescribeTagsResponseresourceTagstagsTypeDef]},
    total=False,
)


class ClientDescribeTagsResponseresourceTagsTypeDef(_ClientDescribeTagsResponseresourceTagsTypeDef):
    """
    - *(dict) --*

      Information about a tag associated with an AWS Direct Connect resource.
      - **resourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource.
    """


_ClientDescribeTagsResponseTypeDef = TypedDict(
    "_ClientDescribeTagsResponseTypeDef",
    {"resourceTags": List[ClientDescribeTagsResponseresourceTagsTypeDef]},
    total=False,
)


class ClientDescribeTagsResponseTypeDef(_ClientDescribeTagsResponseTypeDef):
    """
    - *(dict) --*

      - **resourceTags** *(list) --*

        Information about the tags.
        - *(dict) --*

          Information about a tag associated with an AWS Direct Connect resource.
          - **resourceArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource.
    """


_ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef = TypedDict(
    "_ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef",
    {"virtualGatewayId": str, "virtualGatewayState": str},
    total=False,
)


class ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef(
    _ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef
):
    """
    - *(dict) --*

      Information about a virtual private gateway for a private virtual interface.
      - **virtualGatewayId** *(string) --*

        The ID of the virtual private gateway.
    """


_ClientDescribeVirtualGatewaysResponseTypeDef = TypedDict(
    "_ClientDescribeVirtualGatewaysResponseTypeDef",
    {"virtualGateways": List[ClientDescribeVirtualGatewaysResponsevirtualGatewaysTypeDef]},
    total=False,
)


class ClientDescribeVirtualGatewaysResponseTypeDef(_ClientDescribeVirtualGatewaysResponseTypeDef):
    """
    - *(dict) --*

      - **virtualGateways** *(list) --*

        The virtual private gateways.
        - *(dict) --*

          Information about a virtual private gateway for a private virtual interface.
          - **virtualGatewayId** *(string) --*

            The ID of the virtual private gateway.
    """


_ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef = TypedDict(
    "_ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef(
    _ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef
):
    pass


_ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef = TypedDict(
    "_ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef(
    _ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef
):
    pass


_ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef = TypedDict(
    "_ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef(
    _ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef
):
    pass


_ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef = TypedDict(
    "_ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientDescribeVirtualInterfacesResponsevirtualInterfacesrouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientDescribeVirtualInterfacesResponsevirtualInterfacesbgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientDescribeVirtualInterfacesResponsevirtualInterfacestagsTypeDef],
    },
    total=False,
)


class ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef(
    _ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef
):
    """
    - *(dict) --*

      Information about a virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_ClientDescribeVirtualInterfacesResponseTypeDef = TypedDict(
    "_ClientDescribeVirtualInterfacesResponseTypeDef",
    {"virtualInterfaces": List[ClientDescribeVirtualInterfacesResponsevirtualInterfacesTypeDef]},
    total=False,
)


class ClientDescribeVirtualInterfacesResponseTypeDef(
    _ClientDescribeVirtualInterfacesResponseTypeDef
):
    """
    - *(dict) --*

      - **virtualInterfaces** *(list) --*

        The virtual interfaces
        - *(dict) --*

          Information about a virtual interface.
          - **ownerAccount** *(string) --*

            The ID of the AWS account that owns the virtual interface.
    """


_ClientDisassociateConnectionFromLagResponsetagsTypeDef = TypedDict(
    "_ClientDisassociateConnectionFromLagResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientDisassociateConnectionFromLagResponsetagsTypeDef(
    _ClientDisassociateConnectionFromLagResponsetagsTypeDef
):
    pass


_ClientDisassociateConnectionFromLagResponseTypeDef = TypedDict(
    "_ClientDisassociateConnectionFromLagResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientDisassociateConnectionFromLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientDisassociateConnectionFromLagResponseTypeDef(
    _ClientDisassociateConnectionFromLagResponseTypeDef
):
    """
    - *(dict) --*

      Information about an AWS Direct Connect connection.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the connection.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      Information about a tag.
      - **key** *(string) --***[REQUIRED]**

        The key.
    """


_ClientUpdateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationAddAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    - *(dict) --*

      Information about a route filter prefix that a customer can advertise through Border Gateway
      Protocol (BGP) over a public virtual interface.
      - **cidr** *(string) --*

        The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
        must use /64 or shorter.
    """


_ClientUpdateDirectConnectGatewayAssociationRemoveAllowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationRemoveAllowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationRemoveAllowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationRemoveAllowedPrefixesToDirectConnectGatewayTypeDef
):
    """
    - *(dict) --*

      Information about a route filter prefix that a customer can advertise through Border Gateway
      Protocol (BGP) over a public virtual interface.
      - **cidr** *(string) --*

        The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR
        must use /64 or shorter.
    """


_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef
):
    pass


_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
):
    """
    - **directConnectGatewayAssociation** *(dict) --*

      Information about an association between a Direct Connect gateway and a virtual private
      gateway or transit gateway.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_ClientUpdateDirectConnectGatewayAssociationResponseTypeDef = TypedDict(
    "_ClientUpdateDirectConnectGatewayAssociationResponseTypeDef",
    {
        "directConnectGatewayAssociation": ClientUpdateDirectConnectGatewayAssociationResponsedirectConnectGatewayAssociationTypeDef
    },
    total=False,
)


class ClientUpdateDirectConnectGatewayAssociationResponseTypeDef(
    _ClientUpdateDirectConnectGatewayAssociationResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAssociation** *(dict) --*

        Information about an association between a Direct Connect gateway and a virtual private
        gateway or transit gateway.
        - **directConnectGatewayId** *(string) --*

          The ID of the Direct Connect gateway.
    """


_ClientUpdateLagResponseconnectionstagsTypeDef = TypedDict(
    "_ClientUpdateLagResponseconnectionstagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateLagResponseconnectionstagsTypeDef(_ClientUpdateLagResponseconnectionstagsTypeDef):
    pass


_ClientUpdateLagResponseconnectionsTypeDef = TypedDict(
    "_ClientUpdateLagResponseconnectionsTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientUpdateLagResponseconnectionstagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientUpdateLagResponseconnectionsTypeDef(_ClientUpdateLagResponseconnectionsTypeDef):
    pass


_ClientUpdateLagResponsetagsTypeDef = TypedDict(
    "_ClientUpdateLagResponsetagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientUpdateLagResponsetagsTypeDef(_ClientUpdateLagResponsetagsTypeDef):
    pass


_ClientUpdateLagResponseTypeDef = TypedDict(
    "_ClientUpdateLagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List[ClientUpdateLagResponseconnectionsTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List[ClientUpdateLagResponsetagsTypeDef],
        "providerName": str,
    },
    total=False,
)


class ClientUpdateLagResponseTypeDef(_ClientUpdateLagResponseTypeDef):
    """
    - *(dict) --*

      Information about a link aggregation group (LAG).
      - **connectionsBandwidth** *(string) --*

        The individual bandwidth of the physical connections bundled by the LAG. The possible values
        are 1Gbps and 10Gbps.
    """


_ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef = TypedDict(
    "_ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)


class ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef(
    _ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef
):
    pass


_ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef = TypedDict(
    "_ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef",
    {"cidr": str},
    total=False,
)


class ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef(
    _ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef
):
    pass


_ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef = TypedDict(
    "_ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef(
    _ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef
):
    pass


_ClientUpdateVirtualInterfaceAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateVirtualInterfaceAttributesResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[
            ClientUpdateVirtualInterfaceAttributesResponserouteFilterPrefixesTypeDef
        ],
        "bgpPeers": List[ClientUpdateVirtualInterfaceAttributesResponsebgpPeersTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "tags": List[ClientUpdateVirtualInterfaceAttributesResponsetagsTypeDef],
    },
    total=False,
)


class ClientUpdateVirtualInterfaceAttributesResponseTypeDef(
    _ClientUpdateVirtualInterfaceAttributesResponseTypeDef
):
    """
    - *(dict) --*

      Information about a virtual interface.
      - **ownerAccount** *(string) --*

        The ID of the AWS account that owns the virtual interface.
    """


_DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef(
    _DescribeDirectConnectGatewayAssociationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef",
    {"cidr": str},
    total=False,
)


class DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef(
    _DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef
):
    pass


_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)


class DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef(
    _DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef
):
    pass


_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
        "stateChangeError": str,
        "associatedGateway": DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsassociatedGatewayTypeDef,
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List[
            DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsallowedPrefixesToDirectConnectGatewayTypeDef
        ],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)


class DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef(
    _DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef
):
    """
    - *(dict) --*

      Information about an association between a Direct Connect gateway and a virtual private
      gateway or transit gateway.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef",
    {
        "directConnectGatewayAssociations": List[
            DescribeDirectConnectGatewayAssociationsPaginateResponsedirectConnectGatewayAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef(
    _DescribeDirectConnectGatewayAssociationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAssociations** *(list) --*

        Information about the associations.
        - *(dict) --*

          Information about an association between a Direct Connect gateway and a virtual private
          gateway or transit gateway.
          - **directConnectGatewayId** *(string) --*

            The ID of the Direct Connect gateway.
    """


_DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef(
    _DescribeDirectConnectGatewayAttachmentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef",
    {
        "directConnectGatewayId": str,
        "virtualInterfaceId": str,
        "virtualInterfaceRegion": str,
        "virtualInterfaceOwnerAccount": str,
        "attachmentState": Literal["attaching", "attached", "detaching", "detached"],
        "attachmentType": Literal["TransitVirtualInterface", "PrivateVirtualInterface"],
        "stateChangeError": str,
    },
    total=False,
)


class DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef(
    _DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef
):
    """
    - *(dict) --*

      Information about an attachment between a Direct Connect gateway and a virtual interface.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef = TypedDict(
    "_DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef",
    {
        "directConnectGatewayAttachments": List[
            DescribeDirectConnectGatewayAttachmentsPaginateResponsedirectConnectGatewayAttachmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef(
    _DescribeDirectConnectGatewayAttachmentsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGatewayAttachments** *(list) --*

        The attachments.
        - *(dict) --*

          Information about an attachment between a Direct Connect gateway and a virtual interface.
          - **directConnectGatewayId** *(string) --*

            The ID of the Direct Connect gateway.
    """


_DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef(
    _DescribeDirectConnectGatewaysPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef = TypedDict(
    "_DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": Literal["pending", "available", "deleting", "deleted"],
        "stateChangeError": str,
    },
    total=False,
)


class DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef(
    _DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef
):
    """
    - *(dict) --*

      Information about a Direct Connect gateway, which enables you to connect virtual interfaces
      and virtual private gateway or transit gateways.
      - **directConnectGatewayId** *(string) --*

        The ID of the Direct Connect gateway.
    """


_DescribeDirectConnectGatewaysPaginateResponseTypeDef = TypedDict(
    "_DescribeDirectConnectGatewaysPaginateResponseTypeDef",
    {
        "directConnectGateways": List[
            DescribeDirectConnectGatewaysPaginateResponsedirectConnectGatewaysTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeDirectConnectGatewaysPaginateResponseTypeDef(
    _DescribeDirectConnectGatewaysPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **directConnectGateways** *(list) --*

        The Direct Connect gateways.
        - *(dict) --*

          Information about a Direct Connect gateway, which enables you to connect virtual
          interfaces and virtual private gateway or transit gateways.
          - **directConnectGatewayId** *(string) --*

            The ID of the Direct Connect gateway.
    """
