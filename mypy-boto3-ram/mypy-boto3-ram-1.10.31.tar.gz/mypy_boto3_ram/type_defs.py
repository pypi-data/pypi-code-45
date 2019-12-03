"Main interface for ram service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    "ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef",
    "ClientAcceptResourceShareInvitationResponseTypeDef",
    "ClientAssociateResourceSharePermissionResponseTypeDef",
    "ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef",
    "ClientAssociateResourceShareResponseTypeDef",
    "ClientCreateResourceShareResponseresourceSharetagsTypeDef",
    "ClientCreateResourceShareResponseresourceShareTypeDef",
    "ClientCreateResourceShareResponseTypeDef",
    "ClientCreateResourceShareTagsTypeDef",
    "ClientDeleteResourceShareResponseTypeDef",
    "ClientDisassociateResourceSharePermissionResponseTypeDef",
    "ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef",
    "ClientDisassociateResourceShareResponseTypeDef",
    "ClientEnableSharingWithAwsOrganizationResponseTypeDef",
    "ClientGetPermissionResponsepermissionTypeDef",
    "ClientGetPermissionResponseTypeDef",
    "ClientGetResourcePoliciesResponseTypeDef",
    "ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef",
    "ClientGetResourceShareAssociationsResponseTypeDef",
    "ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef",
    "ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef",
    "ClientGetResourceShareInvitationsResponseTypeDef",
    "ClientGetResourceSharesResponseresourceSharestagsTypeDef",
    "ClientGetResourceSharesResponseresourceSharesTypeDef",
    "ClientGetResourceSharesResponseTypeDef",
    "ClientGetResourceSharesTagFiltersTypeDef",
    "ClientListPendingInvitationResourcesResponseresourcesTypeDef",
    "ClientListPendingInvitationResourcesResponseTypeDef",
    "ClientListPermissionsResponsepermissionsTypeDef",
    "ClientListPermissionsResponseTypeDef",
    "ClientListPrincipalsResponseprincipalsTypeDef",
    "ClientListPrincipalsResponseTypeDef",
    "ClientListResourceSharePermissionsResponsepermissionsTypeDef",
    "ClientListResourceSharePermissionsResponseTypeDef",
    "ClientListResourcesResponseresourcesTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef",
    "ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    "ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef",
    "ClientRejectResourceShareInvitationResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateResourceShareResponseresourceSharetagsTypeDef",
    "ClientUpdateResourceShareResponseresourceShareTypeDef",
    "ClientUpdateResourceShareResponseTypeDef",
    "GetResourcePoliciesPaginatePaginationConfigTypeDef",
    "GetResourcePoliciesPaginateResponseTypeDef",
    "GetResourceShareAssociationsPaginatePaginationConfigTypeDef",
    "GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef",
    "GetResourceShareAssociationsPaginateResponseTypeDef",
    "GetResourceShareInvitationsPaginatePaginationConfigTypeDef",
    "GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef",
    "GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef",
    "GetResourceShareInvitationsPaginateResponseTypeDef",
    "GetResourceSharesPaginatePaginationConfigTypeDef",
    "GetResourceSharesPaginateResponseresourceSharestagsTypeDef",
    "GetResourceSharesPaginateResponseresourceSharesTypeDef",
    "GetResourceSharesPaginateResponseTypeDef",
    "GetResourceSharesPaginateTagFiltersTypeDef",
    "ListPrincipalsPaginatePaginationConfigTypeDef",
    "ListPrincipalsPaginateResponseprincipalsTypeDef",
    "ListPrincipalsPaginateResponseTypeDef",
    "ListResourcesPaginatePaginationConfigTypeDef",
    "ListResourcesPaginateResponseresourcesTypeDef",
    "ListResourcesPaginateResponseTypeDef",
)


_ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef = TypedDict(
    "_ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef(
    _ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef
):
    pass


_ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef = TypedDict(
    "_ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": Literal["PENDING", "ACCEPTED", "REJECTED", "EXPIRED"],
        "resourceShareAssociations": List[
            ClientAcceptResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)


class ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef(
    _ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef
):
    """
    - **resourceShareInvitation** *(dict) --*

      Information about the invitation.
      - **resourceShareInvitationArn** *(string) --*

        The Amazon Resource Name (ARN) of the invitation.
    """


_ClientAcceptResourceShareInvitationResponseTypeDef = TypedDict(
    "_ClientAcceptResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": ClientAcceptResourceShareInvitationResponseresourceShareInvitationTypeDef,
        "clientToken": str,
    },
    total=False,
)


class ClientAcceptResourceShareInvitationResponseTypeDef(
    _ClientAcceptResourceShareInvitationResponseTypeDef
):
    """
    - *(dict) --*

      - **resourceShareInvitation** *(dict) --*

        Information about the invitation.
        - **resourceShareInvitationArn** *(string) --*

          The Amazon Resource Name (ARN) of the invitation.
    """


_ClientAssociateResourceSharePermissionResponseTypeDef = TypedDict(
    "_ClientAssociateResourceSharePermissionResponseTypeDef",
    {"returnValue": bool, "clientToken": str},
    total=False,
)


class ClientAssociateResourceSharePermissionResponseTypeDef(
    _ClientAssociateResourceSharePermissionResponseTypeDef
):
    """
    - *(dict) --*

      - **returnValue** *(boolean) --*

        Indicates whether the request succeeded.
    """


_ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef = TypedDict(
    "_ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef(
    _ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef
):
    """
    - *(dict) --*

      Describes an association with a resource share.
      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.
    """


_ClientAssociateResourceShareResponseTypeDef = TypedDict(
    "_ClientAssociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List[
            ClientAssociateResourceShareResponseresourceShareAssociationsTypeDef
        ],
        "clientToken": str,
    },
    total=False,
)


class ClientAssociateResourceShareResponseTypeDef(_ClientAssociateResourceShareResponseTypeDef):
    """
    - *(dict) --*

      - **resourceShareAssociations** *(list) --*

        Information about the associations.
        - *(dict) --*

          Describes an association with a resource share.
          - **resourceShareArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource share.
    """


_ClientCreateResourceShareResponseresourceSharetagsTypeDef = TypedDict(
    "_ClientCreateResourceShareResponseresourceSharetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientCreateResourceShareResponseresourceSharetagsTypeDef(
    _ClientCreateResourceShareResponseresourceSharetagsTypeDef
):
    pass


_ClientCreateResourceShareResponseresourceShareTypeDef = TypedDict(
    "_ClientCreateResourceShareResponseresourceShareTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"],
        "statusMessage": str,
        "tags": List[ClientCreateResourceShareResponseresourceSharetagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"],
    },
    total=False,
)


class ClientCreateResourceShareResponseresourceShareTypeDef(
    _ClientCreateResourceShareResponseresourceShareTypeDef
):
    """
    - **resourceShare** *(dict) --*

      Information about the resource share.
      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.
    """


_ClientCreateResourceShareResponseTypeDef = TypedDict(
    "_ClientCreateResourceShareResponseTypeDef",
    {"resourceShare": ClientCreateResourceShareResponseresourceShareTypeDef, "clientToken": str},
    total=False,
)


class ClientCreateResourceShareResponseTypeDef(_ClientCreateResourceShareResponseTypeDef):
    """
    - *(dict) --*

      - **resourceShare** *(dict) --*

        Information about the resource share.
        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.
    """


_ClientCreateResourceShareTagsTypeDef = TypedDict(
    "_ClientCreateResourceShareTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientCreateResourceShareTagsTypeDef(_ClientCreateResourceShareTagsTypeDef):
    """
    - *(dict) --*

      Information about a tag.
      - **key** *(string) --*

        The key of the tag.
    """


_ClientDeleteResourceShareResponseTypeDef = TypedDict(
    "_ClientDeleteResourceShareResponseTypeDef",
    {"returnValue": bool, "clientToken": str},
    total=False,
)


class ClientDeleteResourceShareResponseTypeDef(_ClientDeleteResourceShareResponseTypeDef):
    """
    - *(dict) --*

      - **returnValue** *(boolean) --*

        Indicates whether the request succeeded.
    """


_ClientDisassociateResourceSharePermissionResponseTypeDef = TypedDict(
    "_ClientDisassociateResourceSharePermissionResponseTypeDef",
    {"returnValue": bool, "clientToken": str},
    total=False,
)


class ClientDisassociateResourceSharePermissionResponseTypeDef(
    _ClientDisassociateResourceSharePermissionResponseTypeDef
):
    """
    - *(dict) --*

      - **returnValue** *(boolean) --*

        Indicates whether the request succeeded.
    """


_ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef = TypedDict(
    "_ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef(
    _ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef
):
    """
    - *(dict) --*

      Describes an association with a resource share.
      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.
    """


_ClientDisassociateResourceShareResponseTypeDef = TypedDict(
    "_ClientDisassociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List[
            ClientDisassociateResourceShareResponseresourceShareAssociationsTypeDef
        ],
        "clientToken": str,
    },
    total=False,
)


class ClientDisassociateResourceShareResponseTypeDef(
    _ClientDisassociateResourceShareResponseTypeDef
):
    """
    - *(dict) --*

      - **resourceShareAssociations** *(list) --*

        Information about the associations.
        - *(dict) --*

          Describes an association with a resource share.
          - **resourceShareArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource share.
    """


_ClientEnableSharingWithAwsOrganizationResponseTypeDef = TypedDict(
    "_ClientEnableSharingWithAwsOrganizationResponseTypeDef", {"returnValue": bool}, total=False
)


class ClientEnableSharingWithAwsOrganizationResponseTypeDef(
    _ClientEnableSharingWithAwsOrganizationResponseTypeDef
):
    """
    - *(dict) --*

      - **returnValue** *(boolean) --*

        Indicates whether the request succeeded.
    """


_ClientGetPermissionResponsepermissionTypeDef = TypedDict(
    "_ClientGetPermissionResponsepermissionTypeDef",
    {
        "arn": str,
        "version": str,
        "defaultVersion": bool,
        "name": str,
        "resourceType": str,
        "permission": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ClientGetPermissionResponsepermissionTypeDef(_ClientGetPermissionResponsepermissionTypeDef):
    """
    - **permission** *(dict) --*

      Information about the permission.
      - **arn** *(string) --*

        The ARN of the permission.
    """


_ClientGetPermissionResponseTypeDef = TypedDict(
    "_ClientGetPermissionResponseTypeDef",
    {"permission": ClientGetPermissionResponsepermissionTypeDef},
    total=False,
)


class ClientGetPermissionResponseTypeDef(_ClientGetPermissionResponseTypeDef):
    """
    - *(dict) --*

      - **permission** *(dict) --*

        Information about the permission.
        - **arn** *(string) --*

          The ARN of the permission.
    """


_ClientGetResourcePoliciesResponseTypeDef = TypedDict(
    "_ClientGetResourcePoliciesResponseTypeDef",
    {"policies": List[str], "nextToken": str},
    total=False,
)


class ClientGetResourcePoliciesResponseTypeDef(_ClientGetResourcePoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **policies** *(list) --*

        A key policy document, in JSON format.
        - *(string) --*
    """


_ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef = TypedDict(
    "_ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef(
    _ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef
):
    """
    - *(dict) --*

      Describes an association with a resource share.
      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.
    """


_ClientGetResourceShareAssociationsResponseTypeDef = TypedDict(
    "_ClientGetResourceShareAssociationsResponseTypeDef",
    {
        "resourceShareAssociations": List[
            ClientGetResourceShareAssociationsResponseresourceShareAssociationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetResourceShareAssociationsResponseTypeDef(
    _ClientGetResourceShareAssociationsResponseTypeDef
):
    """
    - *(dict) --*

      - **resourceShareAssociations** *(list) --*

        Information about the associations.
        - *(dict) --*

          Describes an association with a resource share.
          - **resourceShareArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource share.
    """


_ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef = TypedDict(
    "_ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef(
    _ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef
):
    pass


_ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef = TypedDict(
    "_ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": Literal["PENDING", "ACCEPTED", "REJECTED", "EXPIRED"],
        "resourceShareAssociations": List[
            ClientGetResourceShareInvitationsResponseresourceShareInvitationsresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)


class ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef(
    _ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef
):
    """
    - *(dict) --*

      Describes an invitation to join a resource share.
      - **resourceShareInvitationArn** *(string) --*

        The Amazon Resource Name (ARN) of the invitation.
    """


_ClientGetResourceShareInvitationsResponseTypeDef = TypedDict(
    "_ClientGetResourceShareInvitationsResponseTypeDef",
    {
        "resourceShareInvitations": List[
            ClientGetResourceShareInvitationsResponseresourceShareInvitationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetResourceShareInvitationsResponseTypeDef(
    _ClientGetResourceShareInvitationsResponseTypeDef
):
    """
    - *(dict) --*

      - **resourceShareInvitations** *(list) --*

        Information about the invitations.
        - *(dict) --*

          Describes an invitation to join a resource share.
          - **resourceShareInvitationArn** *(string) --*

            The Amazon Resource Name (ARN) of the invitation.
    """


_ClientGetResourceSharesResponseresourceSharestagsTypeDef = TypedDict(
    "_ClientGetResourceSharesResponseresourceSharestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientGetResourceSharesResponseresourceSharestagsTypeDef(
    _ClientGetResourceSharesResponseresourceSharestagsTypeDef
):
    pass


_ClientGetResourceSharesResponseresourceSharesTypeDef = TypedDict(
    "_ClientGetResourceSharesResponseresourceSharesTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"],
        "statusMessage": str,
        "tags": List[ClientGetResourceSharesResponseresourceSharestagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"],
    },
    total=False,
)


class ClientGetResourceSharesResponseresourceSharesTypeDef(
    _ClientGetResourceSharesResponseresourceSharesTypeDef
):
    """
    - *(dict) --*

      Describes a resource share.
      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.
    """


_ClientGetResourceSharesResponseTypeDef = TypedDict(
    "_ClientGetResourceSharesResponseTypeDef",
    {
        "resourceShares": List[ClientGetResourceSharesResponseresourceSharesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetResourceSharesResponseTypeDef(_ClientGetResourceSharesResponseTypeDef):
    """
    - *(dict) --*

      - **resourceShares** *(list) --*

        Information about the resource shares.
        - *(dict) --*

          Describes a resource share.
          - **resourceShareArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource share.
    """


_ClientGetResourceSharesTagFiltersTypeDef = TypedDict(
    "_ClientGetResourceSharesTagFiltersTypeDef",
    {"tagKey": str, "tagValues": List[str]},
    total=False,
)


class ClientGetResourceSharesTagFiltersTypeDef(_ClientGetResourceSharesTagFiltersTypeDef):
    """
    - *(dict) --*

      Used to filter information based on tags.
      - **tagKey** *(string) --*

        The tag key.
    """


_ClientListPendingInvitationResourcesResponseresourcesTypeDef = TypedDict(
    "_ClientListPendingInvitationResourcesResponseresourcesTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "resourceGroupArn": str,
        "status": Literal[
            "AVAILABLE", "ZONAL_RESOURCE_INACCESSIBLE", "LIMIT_EXCEEDED", "UNAVAILABLE", "PENDING"
        ],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ClientListPendingInvitationResourcesResponseresourcesTypeDef(
    _ClientListPendingInvitationResourcesResponseresourcesTypeDef
):
    """
    - *(dict) --*

      Describes a resource associated with a resource share.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the resource.
    """


_ClientListPendingInvitationResourcesResponseTypeDef = TypedDict(
    "_ClientListPendingInvitationResourcesResponseTypeDef",
    {
        "resources": List[ClientListPendingInvitationResourcesResponseresourcesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListPendingInvitationResourcesResponseTypeDef(
    _ClientListPendingInvitationResourcesResponseTypeDef
):
    """
    - *(dict) --*

      - **resources** *(list) --*

        Information about the resources included the resource share.
        - *(dict) --*

          Describes a resource associated with a resource share.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the resource.
    """


_ClientListPermissionsResponsepermissionsTypeDef = TypedDict(
    "_ClientListPermissionsResponsepermissionsTypeDef",
    {
        "arn": str,
        "version": str,
        "defaultVersion": bool,
        "name": str,
        "resourceType": str,
        "status": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ClientListPermissionsResponsepermissionsTypeDef(
    _ClientListPermissionsResponsepermissionsTypeDef
):
    """
    - *(dict) --*

      Information about a permission that is associated with a resource share.
      - **arn** *(string) --*

        The ARN of the permission.
    """


_ClientListPermissionsResponseTypeDef = TypedDict(
    "_ClientListPermissionsResponseTypeDef",
    {"permissions": List[ClientListPermissionsResponsepermissionsTypeDef], "nextToken": str},
    total=False,
)


class ClientListPermissionsResponseTypeDef(_ClientListPermissionsResponseTypeDef):
    """
    - *(dict) --*

      - **permissions** *(list) --*

        Information about the permissions.
        - *(dict) --*

          Information about a permission that is associated with a resource share.
          - **arn** *(string) --*

            The ARN of the permission.
    """


_ClientListPrincipalsResponseprincipalsTypeDef = TypedDict(
    "_ClientListPrincipalsResponseprincipalsTypeDef",
    {
        "id": str,
        "resourceShareArn": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientListPrincipalsResponseprincipalsTypeDef(_ClientListPrincipalsResponseprincipalsTypeDef):
    """
    - *(dict) --*

      Describes a principal for use with AWS Resource Access Manager.
      - **id** *(string) --*

        The ID of the principal.
    """


_ClientListPrincipalsResponseTypeDef = TypedDict(
    "_ClientListPrincipalsResponseTypeDef",
    {"principals": List[ClientListPrincipalsResponseprincipalsTypeDef], "nextToken": str},
    total=False,
)


class ClientListPrincipalsResponseTypeDef(_ClientListPrincipalsResponseTypeDef):
    """
    - *(dict) --*

      - **principals** *(list) --*

        The principals.
        - *(dict) --*

          Describes a principal for use with AWS Resource Access Manager.
          - **id** *(string) --*

            The ID of the principal.
    """


_ClientListResourceSharePermissionsResponsepermissionsTypeDef = TypedDict(
    "_ClientListResourceSharePermissionsResponsepermissionsTypeDef",
    {
        "arn": str,
        "version": str,
        "defaultVersion": bool,
        "name": str,
        "resourceType": str,
        "status": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ClientListResourceSharePermissionsResponsepermissionsTypeDef(
    _ClientListResourceSharePermissionsResponsepermissionsTypeDef
):
    """
    - *(dict) --*

      Information about a permission that is associated with a resource share.
      - **arn** *(string) --*

        The ARN of the permission.
    """


_ClientListResourceSharePermissionsResponseTypeDef = TypedDict(
    "_ClientListResourceSharePermissionsResponseTypeDef",
    {
        "permissions": List[ClientListResourceSharePermissionsResponsepermissionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListResourceSharePermissionsResponseTypeDef(
    _ClientListResourceSharePermissionsResponseTypeDef
):
    """
    - *(dict) --*

      - **permissions** *(list) --*

        The permissions associated with the resource share.
        - *(dict) --*

          Information about a permission that is associated with a resource share.
          - **arn** *(string) --*

            The ARN of the permission.
    """


_ClientListResourcesResponseresourcesTypeDef = TypedDict(
    "_ClientListResourcesResponseresourcesTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "resourceGroupArn": str,
        "status": Literal[
            "AVAILABLE", "ZONAL_RESOURCE_INACCESSIBLE", "LIMIT_EXCEEDED", "UNAVAILABLE", "PENDING"
        ],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ClientListResourcesResponseresourcesTypeDef(_ClientListResourcesResponseresourcesTypeDef):
    """
    - *(dict) --*

      Describes a resource associated with a resource share.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the resource.
    """


_ClientListResourcesResponseTypeDef = TypedDict(
    "_ClientListResourcesResponseTypeDef",
    {"resources": List[ClientListResourcesResponseresourcesTypeDef], "nextToken": str},
    total=False,
)


class ClientListResourcesResponseTypeDef(_ClientListResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **resources** *(list) --*

        Information about the resources.
        - *(dict) --*

          Describes a resource associated with a resource share.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the resource.
    """


_ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef = TypedDict(
    "_ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef",
    {"returnValue": bool},
    total=False,
)


class ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef(
    _ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef
):
    """
    - *(dict) --*

      - **returnValue** *(boolean) --*

        Indicates whether the request succeeded.
    """


_ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef = TypedDict(
    "_ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef(
    _ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef
):
    pass


_ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef = TypedDict(
    "_ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": Literal["PENDING", "ACCEPTED", "REJECTED", "EXPIRED"],
        "resourceShareAssociations": List[
            ClientRejectResourceShareInvitationResponseresourceShareInvitationresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)


class ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef(
    _ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef
):
    """
    - **resourceShareInvitation** *(dict) --*

      Information about the invitation.
      - **resourceShareInvitationArn** *(string) --*

        The Amazon Resource Name (ARN) of the invitation.
    """


_ClientRejectResourceShareInvitationResponseTypeDef = TypedDict(
    "_ClientRejectResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": ClientRejectResourceShareInvitationResponseresourceShareInvitationTypeDef,
        "clientToken": str,
    },
    total=False,
)


class ClientRejectResourceShareInvitationResponseTypeDef(
    _ClientRejectResourceShareInvitationResponseTypeDef
):
    """
    - *(dict) --*

      - **resourceShareInvitation** *(dict) --*

        Information about the invitation.
        - **resourceShareInvitationArn** *(string) --*

          The Amazon Resource Name (ARN) of the invitation.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"key": str, "value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      Information about a tag.
      - **key** *(string) --*

        The key of the tag.
    """


_ClientUpdateResourceShareResponseresourceSharetagsTypeDef = TypedDict(
    "_ClientUpdateResourceShareResponseresourceSharetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientUpdateResourceShareResponseresourceSharetagsTypeDef(
    _ClientUpdateResourceShareResponseresourceSharetagsTypeDef
):
    pass


_ClientUpdateResourceShareResponseresourceShareTypeDef = TypedDict(
    "_ClientUpdateResourceShareResponseresourceShareTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"],
        "statusMessage": str,
        "tags": List[ClientUpdateResourceShareResponseresourceSharetagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"],
    },
    total=False,
)


class ClientUpdateResourceShareResponseresourceShareTypeDef(
    _ClientUpdateResourceShareResponseresourceShareTypeDef
):
    """
    - **resourceShare** *(dict) --*

      Information about the resource share.
      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.
    """


_ClientUpdateResourceShareResponseTypeDef = TypedDict(
    "_ClientUpdateResourceShareResponseTypeDef",
    {"resourceShare": ClientUpdateResourceShareResponseresourceShareTypeDef, "clientToken": str},
    total=False,
)


class ClientUpdateResourceShareResponseTypeDef(_ClientUpdateResourceShareResponseTypeDef):
    """
    - *(dict) --*

      - **resourceShare** *(dict) --*

        Information about the resource share.
        - **resourceShareArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource share.
    """


_GetResourcePoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourcePoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourcePoliciesPaginatePaginationConfigTypeDef(
    _GetResourcePoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetResourcePoliciesPaginateResponseTypeDef = TypedDict(
    "_GetResourcePoliciesPaginateResponseTypeDef",
    {"policies": List[str], "NextToken": str},
    total=False,
)


class GetResourcePoliciesPaginateResponseTypeDef(_GetResourcePoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **policies** *(list) --*

        A key policy document, in JSON format.
        - *(string) --*
    """


_GetResourceShareAssociationsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourceShareAssociationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourceShareAssociationsPaginatePaginationConfigTypeDef(
    _GetResourceShareAssociationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef = TypedDict(
    "_GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef(
    _GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef
):
    """
    - *(dict) --*

      Describes an association with a resource share.
      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.
    """


_GetResourceShareAssociationsPaginateResponseTypeDef = TypedDict(
    "_GetResourceShareAssociationsPaginateResponseTypeDef",
    {
        "resourceShareAssociations": List[
            GetResourceShareAssociationsPaginateResponseresourceShareAssociationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetResourceShareAssociationsPaginateResponseTypeDef(
    _GetResourceShareAssociationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **resourceShareAssociations** *(list) --*

        Information about the associations.
        - *(dict) --*

          Describes an association with a resource share.
          - **resourceShareArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource share.
    """


_GetResourceShareInvitationsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourceShareInvitationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourceShareInvitationsPaginatePaginationConfigTypeDef(
    _GetResourceShareInvitationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef = TypedDict(
    "_GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef",
    {
        "resourceShareArn": str,
        "resourceShareName": str,
        "associatedEntity": str,
        "associationType": Literal["PRINCIPAL", "RESOURCE"],
        "status": Literal["ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef(
    _GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef
):
    pass


_GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef = TypedDict(
    "_GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef",
    {
        "resourceShareInvitationArn": str,
        "resourceShareName": str,
        "resourceShareArn": str,
        "senderAccountId": str,
        "receiverAccountId": str,
        "invitationTimestamp": datetime,
        "status": Literal["PENDING", "ACCEPTED", "REJECTED", "EXPIRED"],
        "resourceShareAssociations": List[
            GetResourceShareInvitationsPaginateResponseresourceShareInvitationsresourceShareAssociationsTypeDef
        ],
    },
    total=False,
)


class GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef(
    _GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef
):
    """
    - *(dict) --*

      Describes an invitation to join a resource share.
      - **resourceShareInvitationArn** *(string) --*

        The Amazon Resource Name (ARN) of the invitation.
    """


_GetResourceShareInvitationsPaginateResponseTypeDef = TypedDict(
    "_GetResourceShareInvitationsPaginateResponseTypeDef",
    {
        "resourceShareInvitations": List[
            GetResourceShareInvitationsPaginateResponseresourceShareInvitationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetResourceShareInvitationsPaginateResponseTypeDef(
    _GetResourceShareInvitationsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **resourceShareInvitations** *(list) --*

        Information about the invitations.
        - *(dict) --*

          Describes an invitation to join a resource share.
          - **resourceShareInvitationArn** *(string) --*

            The Amazon Resource Name (ARN) of the invitation.
    """


_GetResourceSharesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetResourceSharesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetResourceSharesPaginatePaginationConfigTypeDef(
    _GetResourceSharesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetResourceSharesPaginateResponseresourceSharestagsTypeDef = TypedDict(
    "_GetResourceSharesPaginateResponseresourceSharestagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class GetResourceSharesPaginateResponseresourceSharestagsTypeDef(
    _GetResourceSharesPaginateResponseresourceSharestagsTypeDef
):
    pass


_GetResourceSharesPaginateResponseresourceSharesTypeDef = TypedDict(
    "_GetResourceSharesPaginateResponseresourceSharesTypeDef",
    {
        "resourceShareArn": str,
        "name": str,
        "owningAccountId": str,
        "allowExternalPrincipals": bool,
        "status": Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"],
        "statusMessage": str,
        "tags": List[GetResourceSharesPaginateResponseresourceSharestagsTypeDef],
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "featureSet": Literal["CREATED_FROM_POLICY", "PROMOTING_TO_STANDARD", "STANDARD"],
    },
    total=False,
)


class GetResourceSharesPaginateResponseresourceSharesTypeDef(
    _GetResourceSharesPaginateResponseresourceSharesTypeDef
):
    """
    - *(dict) --*

      Describes a resource share.
      - **resourceShareArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource share.
    """


_GetResourceSharesPaginateResponseTypeDef = TypedDict(
    "_GetResourceSharesPaginateResponseTypeDef",
    {
        "resourceShares": List[GetResourceSharesPaginateResponseresourceSharesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetResourceSharesPaginateResponseTypeDef(_GetResourceSharesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **resourceShares** *(list) --*

        Information about the resource shares.
        - *(dict) --*

          Describes a resource share.
          - **resourceShareArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource share.
    """


_GetResourceSharesPaginateTagFiltersTypeDef = TypedDict(
    "_GetResourceSharesPaginateTagFiltersTypeDef",
    {"tagKey": str, "tagValues": List[str]},
    total=False,
)


class GetResourceSharesPaginateTagFiltersTypeDef(_GetResourceSharesPaginateTagFiltersTypeDef):
    """
    - *(dict) --*

      Used to filter information based on tags.
      - **tagKey** *(string) --*

        The tag key.
    """


_ListPrincipalsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPrincipalsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPrincipalsPaginatePaginationConfigTypeDef(_ListPrincipalsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPrincipalsPaginateResponseprincipalsTypeDef = TypedDict(
    "_ListPrincipalsPaginateResponseprincipalsTypeDef",
    {
        "id": str,
        "resourceShareArn": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class ListPrincipalsPaginateResponseprincipalsTypeDef(
    _ListPrincipalsPaginateResponseprincipalsTypeDef
):
    """
    - *(dict) --*

      Describes a principal for use with AWS Resource Access Manager.
      - **id** *(string) --*

        The ID of the principal.
    """


_ListPrincipalsPaginateResponseTypeDef = TypedDict(
    "_ListPrincipalsPaginateResponseTypeDef",
    {"principals": List[ListPrincipalsPaginateResponseprincipalsTypeDef], "NextToken": str},
    total=False,
)


class ListPrincipalsPaginateResponseTypeDef(_ListPrincipalsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **principals** *(list) --*

        The principals.
        - *(dict) --*

          Describes a principal for use with AWS Resource Access Manager.
          - **id** *(string) --*

            The ID of the principal.
    """


_ListResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourcesPaginatePaginationConfigTypeDef(_ListResourcesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListResourcesPaginateResponseresourcesTypeDef = TypedDict(
    "_ListResourcesPaginateResponseresourcesTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "resourceGroupArn": str,
        "status": Literal[
            "AVAILABLE", "ZONAL_RESOURCE_INACCESSIBLE", "LIMIT_EXCEEDED", "UNAVAILABLE", "PENDING"
        ],
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ListResourcesPaginateResponseresourcesTypeDef(_ListResourcesPaginateResponseresourcesTypeDef):
    """
    - *(dict) --*

      Describes a resource associated with a resource share.
      - **arn** *(string) --*

        The Amazon Resource Name (ARN) of the resource.
    """


_ListResourcesPaginateResponseTypeDef = TypedDict(
    "_ListResourcesPaginateResponseTypeDef",
    {"resources": List[ListResourcesPaginateResponseresourcesTypeDef], "NextToken": str},
    total=False,
)


class ListResourcesPaginateResponseTypeDef(_ListResourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **resources** *(list) --*

        Information about the resources.
        - *(dict) --*

          Describes a resource associated with a resource share.
          - **arn** *(string) --*

            The Amazon Resource Name (ARN) of the resource.
    """
