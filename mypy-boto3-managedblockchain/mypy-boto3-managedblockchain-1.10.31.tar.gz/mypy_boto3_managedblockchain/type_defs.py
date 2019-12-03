"Main interface for managedblockchain service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef",
    "ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef",
    "ClientCreateMemberMemberConfigurationTypeDef",
    "ClientCreateMemberResponseTypeDef",
    "ClientCreateNetworkFrameworkConfigurationFabricTypeDef",
    "ClientCreateNetworkFrameworkConfigurationTypeDef",
    "ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef",
    "ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef",
    "ClientCreateNetworkMemberConfigurationTypeDef",
    "ClientCreateNetworkResponseTypeDef",
    "ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    "ClientCreateNetworkVotingPolicyTypeDef",
    "ClientCreateNodeNodeConfigurationTypeDef",
    "ClientCreateNodeResponseTypeDef",
    "ClientCreateProposalActionsInvitationsTypeDef",
    "ClientCreateProposalActionsRemovalsTypeDef",
    "ClientCreateProposalActionsTypeDef",
    "ClientCreateProposalResponseTypeDef",
    "ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef",
    "ClientGetMemberResponseMemberFrameworkAttributesTypeDef",
    "ClientGetMemberResponseMemberTypeDef",
    "ClientGetMemberResponseTypeDef",
    "ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef",
    "ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef",
    "ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    "ClientGetNetworkResponseNetworkVotingPolicyTypeDef",
    "ClientGetNetworkResponseNetworkTypeDef",
    "ClientGetNetworkResponseTypeDef",
    "ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef",
    "ClientGetNodeResponseNodeFrameworkAttributesTypeDef",
    "ClientGetNodeResponseNodeTypeDef",
    "ClientGetNodeResponseTypeDef",
    "ClientGetProposalResponseProposalActionsInvitationsTypeDef",
    "ClientGetProposalResponseProposalActionsRemovalsTypeDef",
    "ClientGetProposalResponseProposalActionsTypeDef",
    "ClientGetProposalResponseProposalTypeDef",
    "ClientGetProposalResponseTypeDef",
    "ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef",
    "ClientListInvitationsResponseInvitationsTypeDef",
    "ClientListInvitationsResponseTypeDef",
    "ClientListMembersResponseMembersTypeDef",
    "ClientListMembersResponseTypeDef",
    "ClientListNetworksResponseNetworksTypeDef",
    "ClientListNetworksResponseTypeDef",
    "ClientListNodesResponseNodesTypeDef",
    "ClientListNodesResponseTypeDef",
    "ClientListProposalVotesResponseProposalVotesTypeDef",
    "ClientListProposalVotesResponseTypeDef",
    "ClientListProposalsResponseProposalsTypeDef",
    "ClientListProposalsResponseTypeDef",
)


_ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef = TypedDict(
    "_ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef",
    {"AdminUsername": str, "AdminPassword": str},
    total=False,
)


class ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef(
    _ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef
):
    pass


_ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef = TypedDict(
    "_ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef",
    {"Fabric": ClientCreateMemberMemberConfigurationFrameworkConfigurationFabricTypeDef},
    total=False,
)


class ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef(
    _ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef
):
    pass


_RequiredClientCreateMemberMemberConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateMemberMemberConfigurationTypeDef", {"Name": str}
)
_OptionalClientCreateMemberMemberConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateMemberMemberConfigurationTypeDef",
    {
        "Description": str,
        "FrameworkConfiguration": ClientCreateMemberMemberConfigurationFrameworkConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateMemberMemberConfigurationTypeDef(
    _RequiredClientCreateMemberMemberConfigurationTypeDef,
    _OptionalClientCreateMemberMemberConfigurationTypeDef,
):
    """
    Member configuration parameters.
    - **Name** *(string) --***[REQUIRED]**

      The name of the member.
    """


_ClientCreateMemberResponseTypeDef = TypedDict(
    "_ClientCreateMemberResponseTypeDef", {"MemberId": str}, total=False
)


class ClientCreateMemberResponseTypeDef(_ClientCreateMemberResponseTypeDef):
    """
    - *(dict) --*

      - **MemberId** *(string) --*

        The unique identifier of the member.
    """


_ClientCreateNetworkFrameworkConfigurationFabricTypeDef = TypedDict(
    "_ClientCreateNetworkFrameworkConfigurationFabricTypeDef",
    {"Edition": Literal["STARTER", "STANDARD"]},
)


class ClientCreateNetworkFrameworkConfigurationFabricTypeDef(
    _ClientCreateNetworkFrameworkConfigurationFabricTypeDef
):
    """
    - **Fabric** *(dict) --*

      Hyperledger Fabric configuration properties for a Managed Blockchain network that uses
      Hyperledger Fabric.
      - **Edition** *(string) --***[REQUIRED]**

        The edition of Amazon Managed Blockchain that the network uses. For more information, see
        `Amazon Managed Blockchain Pricing <https://aws.amazon.com/managed-blockchain/pricing/>`__ .
    """


_ClientCreateNetworkFrameworkConfigurationTypeDef = TypedDict(
    "_ClientCreateNetworkFrameworkConfigurationTypeDef",
    {"Fabric": ClientCreateNetworkFrameworkConfigurationFabricTypeDef},
    total=False,
)


class ClientCreateNetworkFrameworkConfigurationTypeDef(
    _ClientCreateNetworkFrameworkConfigurationTypeDef
):
    """
    Configuration properties of the blockchain framework relevant to the network configuration.
    - **Fabric** *(dict) --*

      Hyperledger Fabric configuration properties for a Managed Blockchain network that uses
      Hyperledger Fabric.
      - **Edition** *(string) --***[REQUIRED]**

        The edition of Amazon Managed Blockchain that the network uses. For more information, see
        `Amazon Managed Blockchain Pricing <https://aws.amazon.com/managed-blockchain/pricing/>`__ .
    """


_ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef = TypedDict(
    "_ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef",
    {"AdminUsername": str, "AdminPassword": str},
    total=False,
)


class ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef(
    _ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef
):
    pass


_ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef = TypedDict(
    "_ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef",
    {"Fabric": ClientCreateNetworkMemberConfigurationFrameworkConfigurationFabricTypeDef},
    total=False,
)


class ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef(
    _ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef
):
    pass


_RequiredClientCreateNetworkMemberConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateNetworkMemberConfigurationTypeDef", {"Name": str}
)
_OptionalClientCreateNetworkMemberConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateNetworkMemberConfigurationTypeDef",
    {
        "Description": str,
        "FrameworkConfiguration": ClientCreateNetworkMemberConfigurationFrameworkConfigurationTypeDef,
    },
    total=False,
)


class ClientCreateNetworkMemberConfigurationTypeDef(
    _RequiredClientCreateNetworkMemberConfigurationTypeDef,
    _OptionalClientCreateNetworkMemberConfigurationTypeDef,
):
    """
    Configuration properties for the first member within the network.
    - **Name** *(string) --***[REQUIRED]**

      The name of the member.
    """


_ClientCreateNetworkResponseTypeDef = TypedDict(
    "_ClientCreateNetworkResponseTypeDef", {"NetworkId": str, "MemberId": str}, total=False
)


class ClientCreateNetworkResponseTypeDef(_ClientCreateNetworkResponseTypeDef):
    """
    - *(dict) --*

      - **NetworkId** *(string) --*

        The unique identifier for the network.
    """


_ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef = TypedDict(
    "_ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": int,
        "ProposalDurationInHours": int,
        "ThresholdComparator": Literal["GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO"],
    },
    total=False,
)


class ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef(
    _ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef
):
    """
    - **ApprovalThresholdPolicy** *(dict) --*

      Defines the rules for the network for voting on proposals, such as the percentage of ``YES``
      votes required for the proposal to be approved and the duration of the proposal. The policy
      applies to all proposals and is specified when the network is created.
      - **ThresholdPercentage** *(integer) --*

        The percentage of votes among all members that must be ``YES`` for a proposal to be
        approved. For example, a ``ThresholdPercentage`` value of ``50`` indicates 50%. The
        ``ThresholdComparator`` determines the precise comparison. If a ``ThresholdPercentage``
        value of ``50`` is specified on a network with 10 members, along with a
        ``ThresholdComparator`` value of ``GREATER_THAN`` , this indicates that 6 ``YES`` votes are
        required for the proposal to be approved.
    """


_ClientCreateNetworkVotingPolicyTypeDef = TypedDict(
    "_ClientCreateNetworkVotingPolicyTypeDef",
    {"ApprovalThresholdPolicy": ClientCreateNetworkVotingPolicyApprovalThresholdPolicyTypeDef},
    total=False,
)


class ClientCreateNetworkVotingPolicyTypeDef(_ClientCreateNetworkVotingPolicyTypeDef):
    """
    The voting rules used by the network to determine if a proposal is approved.
    - **ApprovalThresholdPolicy** *(dict) --*

      Defines the rules for the network for voting on proposals, such as the percentage of ``YES``
      votes required for the proposal to be approved and the duration of the proposal. The policy
      applies to all proposals and is specified when the network is created.
      - **ThresholdPercentage** *(integer) --*

        The percentage of votes among all members that must be ``YES`` for a proposal to be
        approved. For example, a ``ThresholdPercentage`` value of ``50`` indicates 50%. The
        ``ThresholdComparator`` determines the precise comparison. If a ``ThresholdPercentage``
        value of ``50`` is specified on a network with 10 members, along with a
        ``ThresholdComparator`` value of ``GREATER_THAN`` , this indicates that 6 ``YES`` votes are
        required for the proposal to be approved.
    """


_RequiredClientCreateNodeNodeConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateNodeNodeConfigurationTypeDef", {"InstanceType": str}
)
_OptionalClientCreateNodeNodeConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateNodeNodeConfigurationTypeDef", {"AvailabilityZone": str}, total=False
)


class ClientCreateNodeNodeConfigurationTypeDef(
    _RequiredClientCreateNodeNodeConfigurationTypeDef,
    _OptionalClientCreateNodeNodeConfigurationTypeDef,
):
    """
    The properties of a node configuration.
    - **InstanceType** *(string) --***[REQUIRED]**

      The Amazon Managed Blockchain instance type for the node.
    """


_ClientCreateNodeResponseTypeDef = TypedDict(
    "_ClientCreateNodeResponseTypeDef", {"NodeId": str}, total=False
)


class ClientCreateNodeResponseTypeDef(_ClientCreateNodeResponseTypeDef):
    """
    - *(dict) --*

      - **NodeId** *(string) --*

        The unique identifier of the node.
    """


_ClientCreateProposalActionsInvitationsTypeDef = TypedDict(
    "_ClientCreateProposalActionsInvitationsTypeDef", {"Principal": str}
)


class ClientCreateProposalActionsInvitationsTypeDef(_ClientCreateProposalActionsInvitationsTypeDef):
    """
    - *(dict) --*

      An action to invite a specific AWS account to create a member and join the network. The
      ``InviteAction`` is carried out when a ``Proposal`` is ``APPROVED`` .
      - **Principal** *(string) --***[REQUIRED]**

        The AWS account ID to invite.
    """


_ClientCreateProposalActionsRemovalsTypeDef = TypedDict(
    "_ClientCreateProposalActionsRemovalsTypeDef", {"MemberId": str}, total=False
)


class ClientCreateProposalActionsRemovalsTypeDef(_ClientCreateProposalActionsRemovalsTypeDef):
    pass


_ClientCreateProposalActionsTypeDef = TypedDict(
    "_ClientCreateProposalActionsTypeDef",
    {
        "Invitations": List[ClientCreateProposalActionsInvitationsTypeDef],
        "Removals": List[ClientCreateProposalActionsRemovalsTypeDef],
    },
    total=False,
)


class ClientCreateProposalActionsTypeDef(_ClientCreateProposalActionsTypeDef):
    """
    The type of actions proposed, such as inviting a member or removing a member. The types of
    ``Actions`` in a proposal are mutually exclusive. For example, a proposal with ``Invitations``
    actions cannot also contain ``Removals`` actions.
    - **Invitations** *(list) --*

      The actions to perform for an ``APPROVED`` proposal to invite an AWS account to create a
      member and join the network.
      - *(dict) --*

        An action to invite a specific AWS account to create a member and join the network. The
        ``InviteAction`` is carried out when a ``Proposal`` is ``APPROVED`` .
        - **Principal** *(string) --***[REQUIRED]**

          The AWS account ID to invite.
    """


_ClientCreateProposalResponseTypeDef = TypedDict(
    "_ClientCreateProposalResponseTypeDef", {"ProposalId": str}, total=False
)


class ClientCreateProposalResponseTypeDef(_ClientCreateProposalResponseTypeDef):
    """
    - *(dict) --*

      - **ProposalId** *(string) --*

        The unique identifier of the proposal.
    """


_ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef = TypedDict(
    "_ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef",
    {"AdminUsername": str, "CaEndpoint": str},
    total=False,
)


class ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef(
    _ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef
):
    pass


_ClientGetMemberResponseMemberFrameworkAttributesTypeDef = TypedDict(
    "_ClientGetMemberResponseMemberFrameworkAttributesTypeDef",
    {"Fabric": ClientGetMemberResponseMemberFrameworkAttributesFabricTypeDef},
    total=False,
)


class ClientGetMemberResponseMemberFrameworkAttributesTypeDef(
    _ClientGetMemberResponseMemberFrameworkAttributesTypeDef
):
    pass


_ClientGetMemberResponseMemberTypeDef = TypedDict(
    "_ClientGetMemberResponseMemberTypeDef",
    {
        "NetworkId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "FrameworkAttributes": ClientGetMemberResponseMemberFrameworkAttributesTypeDef,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetMemberResponseMemberTypeDef(_ClientGetMemberResponseMemberTypeDef):
    """
    - **Member** *(dict) --*

      The properties of a member.
      - **NetworkId** *(string) --*

        The unique identifier of the network to which the member belongs.
    """


_ClientGetMemberResponseTypeDef = TypedDict(
    "_ClientGetMemberResponseTypeDef", {"Member": ClientGetMemberResponseMemberTypeDef}, total=False
)


class ClientGetMemberResponseTypeDef(_ClientGetMemberResponseTypeDef):
    """
    - *(dict) --*

      - **Member** *(dict) --*

        The properties of a member.
        - **NetworkId** *(string) --*

          The unique identifier of the network to which the member belongs.
    """


_ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef = TypedDict(
    "_ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef",
    {"OrderingServiceEndpoint": str, "Edition": Literal["STARTER", "STANDARD"]},
    total=False,
)


class ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef(
    _ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef
):
    pass


_ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef = TypedDict(
    "_ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef",
    {"Fabric": ClientGetNetworkResponseNetworkFrameworkAttributesFabricTypeDef},
    total=False,
)


class ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef(
    _ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef
):
    pass


_ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef = TypedDict(
    "_ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": int,
        "ProposalDurationInHours": int,
        "ThresholdComparator": Literal["GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO"],
    },
    total=False,
)


class ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef(
    _ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef
):
    pass


_ClientGetNetworkResponseNetworkVotingPolicyTypeDef = TypedDict(
    "_ClientGetNetworkResponseNetworkVotingPolicyTypeDef",
    {
        "ApprovalThresholdPolicy": ClientGetNetworkResponseNetworkVotingPolicyApprovalThresholdPolicyTypeDef
    },
    total=False,
)


class ClientGetNetworkResponseNetworkVotingPolicyTypeDef(
    _ClientGetNetworkResponseNetworkVotingPolicyTypeDef
):
    pass


_ClientGetNetworkResponseNetworkTypeDef = TypedDict(
    "_ClientGetNetworkResponseNetworkTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": str,
        "FrameworkVersion": str,
        "FrameworkAttributes": ClientGetNetworkResponseNetworkFrameworkAttributesTypeDef,
        "VpcEndpointServiceName": str,
        "VotingPolicy": ClientGetNetworkResponseNetworkVotingPolicyTypeDef,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetNetworkResponseNetworkTypeDef(_ClientGetNetworkResponseNetworkTypeDef):
    """
    - **Network** *(dict) --*

      An object containing network configuration parameters.
      - **Id** *(string) --*

        The unique identifier of the network.
    """


_ClientGetNetworkResponseTypeDef = TypedDict(
    "_ClientGetNetworkResponseTypeDef",
    {"Network": ClientGetNetworkResponseNetworkTypeDef},
    total=False,
)


class ClientGetNetworkResponseTypeDef(_ClientGetNetworkResponseTypeDef):
    """
    - *(dict) --*

      - **Network** *(dict) --*

        An object containing network configuration parameters.
        - **Id** *(string) --*

          The unique identifier of the network.
    """


_ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef = TypedDict(
    "_ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef",
    {"PeerEndpoint": str, "PeerEventEndpoint": str},
    total=False,
)


class ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef(
    _ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef
):
    pass


_ClientGetNodeResponseNodeFrameworkAttributesTypeDef = TypedDict(
    "_ClientGetNodeResponseNodeFrameworkAttributesTypeDef",
    {"Fabric": ClientGetNodeResponseNodeFrameworkAttributesFabricTypeDef},
    total=False,
)


class ClientGetNodeResponseNodeFrameworkAttributesTypeDef(
    _ClientGetNodeResponseNodeFrameworkAttributesTypeDef
):
    pass


_ClientGetNodeResponseNodeTypeDef = TypedDict(
    "_ClientGetNodeResponseNodeTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "Id": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "FrameworkAttributes": ClientGetNodeResponseNodeFrameworkAttributesTypeDef,
        "Status": Literal[
            "CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED", "FAILED"
        ],
        "CreationDate": datetime,
    },
    total=False,
)


class ClientGetNodeResponseNodeTypeDef(_ClientGetNodeResponseNodeTypeDef):
    """
    - **Node** *(dict) --*

      Properties of the node configuration.
      - **NetworkId** *(string) --*

        The unique identifier of the network that the node is in.
    """


_ClientGetNodeResponseTypeDef = TypedDict(
    "_ClientGetNodeResponseTypeDef", {"Node": ClientGetNodeResponseNodeTypeDef}, total=False
)


class ClientGetNodeResponseTypeDef(_ClientGetNodeResponseTypeDef):
    """
    - *(dict) --*

      - **Node** *(dict) --*

        Properties of the node configuration.
        - **NetworkId** *(string) --*

          The unique identifier of the network that the node is in.
    """


_ClientGetProposalResponseProposalActionsInvitationsTypeDef = TypedDict(
    "_ClientGetProposalResponseProposalActionsInvitationsTypeDef", {"Principal": str}, total=False
)


class ClientGetProposalResponseProposalActionsInvitationsTypeDef(
    _ClientGetProposalResponseProposalActionsInvitationsTypeDef
):
    pass


_ClientGetProposalResponseProposalActionsRemovalsTypeDef = TypedDict(
    "_ClientGetProposalResponseProposalActionsRemovalsTypeDef", {"MemberId": str}, total=False
)


class ClientGetProposalResponseProposalActionsRemovalsTypeDef(
    _ClientGetProposalResponseProposalActionsRemovalsTypeDef
):
    pass


_ClientGetProposalResponseProposalActionsTypeDef = TypedDict(
    "_ClientGetProposalResponseProposalActionsTypeDef",
    {
        "Invitations": List[ClientGetProposalResponseProposalActionsInvitationsTypeDef],
        "Removals": List[ClientGetProposalResponseProposalActionsRemovalsTypeDef],
    },
    total=False,
)


class ClientGetProposalResponseProposalActionsTypeDef(
    _ClientGetProposalResponseProposalActionsTypeDef
):
    pass


_ClientGetProposalResponseProposalTypeDef = TypedDict(
    "_ClientGetProposalResponseProposalTypeDef",
    {
        "ProposalId": str,
        "NetworkId": str,
        "Description": str,
        "Actions": ClientGetProposalResponseProposalActionsTypeDef,
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": Literal["IN_PROGRESS", "APPROVED", "REJECTED", "EXPIRED", "ACTION_FAILED"],
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "YesVoteCount": int,
        "NoVoteCount": int,
        "OutstandingVoteCount": int,
    },
    total=False,
)


class ClientGetProposalResponseProposalTypeDef(_ClientGetProposalResponseProposalTypeDef):
    """
    - **Proposal** *(dict) --*

      Information about a proposal.
      - **ProposalId** *(string) --*

        The unique identifier of the proposal.
    """


_ClientGetProposalResponseTypeDef = TypedDict(
    "_ClientGetProposalResponseTypeDef",
    {"Proposal": ClientGetProposalResponseProposalTypeDef},
    total=False,
)


class ClientGetProposalResponseTypeDef(_ClientGetProposalResponseTypeDef):
    """
    - *(dict) --*

      - **Proposal** *(dict) --*

        Information about a proposal.
        - **ProposalId** *(string) --*

          The unique identifier of the proposal.
    """


_ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef = TypedDict(
    "_ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": str,
        "FrameworkVersion": str,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
    },
    total=False,
)


class ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef(
    _ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef
):
    pass


_ClientListInvitationsResponseInvitationsTypeDef = TypedDict(
    "_ClientListInvitationsResponseInvitationsTypeDef",
    {
        "InvitationId": str,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "Status": Literal["PENDING", "ACCEPTED", "ACCEPTING", "REJECTED", "EXPIRED"],
        "NetworkSummary": ClientListInvitationsResponseInvitationsNetworkSummaryTypeDef,
    },
    total=False,
)


class ClientListInvitationsResponseInvitationsTypeDef(
    _ClientListInvitationsResponseInvitationsTypeDef
):
    """
    - *(dict) --*

      An invitation to an AWS account to create a member and join the network.
      - **InvitationId** *(string) --*

        The unique identifier for the invitation.
    """


_ClientListInvitationsResponseTypeDef = TypedDict(
    "_ClientListInvitationsResponseTypeDef",
    {"Invitations": List[ClientListInvitationsResponseInvitationsTypeDef], "NextToken": str},
    total=False,
)


class ClientListInvitationsResponseTypeDef(_ClientListInvitationsResponseTypeDef):
    """
    - *(dict) --*

      - **Invitations** *(list) --*

        The invitations for the network.
        - *(dict) --*

          An invitation to an AWS account to create a member and join the network.
          - **InvitationId** *(string) --*

            The unique identifier for the invitation.
    """


_ClientListMembersResponseMembersTypeDef = TypedDict(
    "_ClientListMembersResponseMembersTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
        "IsOwned": bool,
    },
    total=False,
)


class ClientListMembersResponseMembersTypeDef(_ClientListMembersResponseMembersTypeDef):
    """
    - *(dict) --*

      A summary of configuration properties for a member.
      - **Id** *(string) --*

        The unique identifier of the member.
    """


_ClientListMembersResponseTypeDef = TypedDict(
    "_ClientListMembersResponseTypeDef",
    {"Members": List[ClientListMembersResponseMembersTypeDef], "NextToken": str},
    total=False,
)


class ClientListMembersResponseTypeDef(_ClientListMembersResponseTypeDef):
    """
    - *(dict) --*

      - **Members** *(list) --*

        An array of ``MemberSummary`` objects. Each object contains details about a network member.
        - *(dict) --*

          A summary of configuration properties for a member.
          - **Id** *(string) --*

            The unique identifier of the member.
    """


_ClientListNetworksResponseNetworksTypeDef = TypedDict(
    "_ClientListNetworksResponseNetworksTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": str,
        "FrameworkVersion": str,
        "Status": Literal["CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED"],
        "CreationDate": datetime,
    },
    total=False,
)


class ClientListNetworksResponseNetworksTypeDef(_ClientListNetworksResponseNetworksTypeDef):
    """
    - *(dict) --*

      A summary of network configuration properties.
      - **Id** *(string) --*

        The unique identifier of the network.
    """


_ClientListNetworksResponseTypeDef = TypedDict(
    "_ClientListNetworksResponseTypeDef",
    {"Networks": List[ClientListNetworksResponseNetworksTypeDef], "NextToken": str},
    total=False,
)


class ClientListNetworksResponseTypeDef(_ClientListNetworksResponseTypeDef):
    """
    - *(dict) --*

      - **Networks** *(list) --*

        An array of ``NetworkSummary`` objects that contain configuration properties for each
        network.
        - *(dict) --*

          A summary of network configuration properties.
          - **Id** *(string) --*

            The unique identifier of the network.
    """


_ClientListNodesResponseNodesTypeDef = TypedDict(
    "_ClientListNodesResponseNodesTypeDef",
    {
        "Id": str,
        "Status": Literal[
            "CREATING", "AVAILABLE", "CREATE_FAILED", "DELETING", "DELETED", "FAILED"
        ],
        "CreationDate": datetime,
        "AvailabilityZone": str,
        "InstanceType": str,
    },
    total=False,
)


class ClientListNodesResponseNodesTypeDef(_ClientListNodesResponseNodesTypeDef):
    """
    - *(dict) --*

      A summary of configuration properties for a peer node.
      - **Id** *(string) --*

        The unique identifier of the node.
    """


_ClientListNodesResponseTypeDef = TypedDict(
    "_ClientListNodesResponseTypeDef",
    {"Nodes": List[ClientListNodesResponseNodesTypeDef], "NextToken": str},
    total=False,
)


class ClientListNodesResponseTypeDef(_ClientListNodesResponseTypeDef):
    """
    - *(dict) --*

      - **Nodes** *(list) --*

        An array of ``NodeSummary`` objects that contain configuration properties for each node.
        - *(dict) --*

          A summary of configuration properties for a peer node.
          - **Id** *(string) --*

            The unique identifier of the node.
    """


_ClientListProposalVotesResponseProposalVotesTypeDef = TypedDict(
    "_ClientListProposalVotesResponseProposalVotesTypeDef",
    {"Vote": Literal["YES", "NO"], "MemberName": str, "MemberId": str},
    total=False,
)


class ClientListProposalVotesResponseProposalVotesTypeDef(
    _ClientListProposalVotesResponseProposalVotesTypeDef
):
    """
    - *(dict) --*

      Properties of an individual vote that a member cast for a proposal.
      - **Vote** *(string) --*

        The vote value, either ``YES`` or ``NO`` .
    """


_ClientListProposalVotesResponseTypeDef = TypedDict(
    "_ClientListProposalVotesResponseTypeDef",
    {"ProposalVotes": List[ClientListProposalVotesResponseProposalVotesTypeDef], "NextToken": str},
    total=False,
)


class ClientListProposalVotesResponseTypeDef(_ClientListProposalVotesResponseTypeDef):
    """
    - *(dict) --*

      - **ProposalVotes** *(list) --*

        The listing of votes.
        - *(dict) --*

          Properties of an individual vote that a member cast for a proposal.
          - **Vote** *(string) --*

            The vote value, either ``YES`` or ``NO`` .
    """


_ClientListProposalsResponseProposalsTypeDef = TypedDict(
    "_ClientListProposalsResponseProposalsTypeDef",
    {
        "ProposalId": str,
        "Description": str,
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": Literal["IN_PROGRESS", "APPROVED", "REJECTED", "EXPIRED", "ACTION_FAILED"],
        "CreationDate": datetime,
        "ExpirationDate": datetime,
    },
    total=False,
)


class ClientListProposalsResponseProposalsTypeDef(_ClientListProposalsResponseProposalsTypeDef):
    """
    - *(dict) --*

      Properties of a proposal.
      - **ProposalId** *(string) --*

        The unique identifier of the proposal.
    """


_ClientListProposalsResponseTypeDef = TypedDict(
    "_ClientListProposalsResponseTypeDef",
    {"Proposals": List[ClientListProposalsResponseProposalsTypeDef], "NextToken": str},
    total=False,
)


class ClientListProposalsResponseTypeDef(_ClientListProposalsResponseTypeDef):
    """
    - *(dict) --*

      - **Proposals** *(list) --*

        The summary of each proposal made on the network.
        - *(dict) --*

          Properties of a proposal.
          - **ProposalId** *(string) --*

            The unique identifier of the proposal.
    """
