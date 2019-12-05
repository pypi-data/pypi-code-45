"Main interface for ram service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ram.type_defs import (
    GetResourcePoliciesPaginatePaginationConfigTypeDef,
    GetResourcePoliciesPaginateResponseTypeDef,
    GetResourceShareAssociationsPaginatePaginationConfigTypeDef,
    GetResourceShareAssociationsPaginateResponseTypeDef,
    GetResourceShareInvitationsPaginatePaginationConfigTypeDef,
    GetResourceShareInvitationsPaginateResponseTypeDef,
    GetResourceSharesPaginatePaginationConfigTypeDef,
    GetResourceSharesPaginateResponseTypeDef,
    GetResourceSharesPaginateTagFiltersTypeDef,
    ListPrincipalsPaginatePaginationConfigTypeDef,
    ListPrincipalsPaginateResponseTypeDef,
    ListResourcesPaginatePaginationConfigTypeDef,
    ListResourcesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetResourcePoliciesPaginator",
    "GetResourceShareAssociationsPaginator",
    "GetResourceShareInvitationsPaginator",
    "GetResourceSharesPaginator",
    "ListPrincipalsPaginator",
    "ListResourcesPaginator",
)


class GetResourcePoliciesPaginator(Boto3Paginator):
    """
    Paginator for `get_resource_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceArns: List[str],
        principal: str = None,
        PaginationConfig: GetResourcePoliciesPaginatePaginationConfigTypeDef = None,
    ) -> GetResourcePoliciesPaginateResponseTypeDef:
        """
        [GetResourcePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ram.html#RAM.Paginator.GetResourcePolicies.paginate)
        """


class GetResourceShareAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `get_resource_share_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        associationType: Literal["PRINCIPAL", "RESOURCE"],
        resourceShareArns: List[str] = None,
        resourceArn: str = None,
        principal: str = None,
        associationStatus: Literal[
            "ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"
        ] = None,
        PaginationConfig: GetResourceShareAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> GetResourceShareAssociationsPaginateResponseTypeDef:
        """
        [GetResourceShareAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ram.html#RAM.Paginator.GetResourceShareAssociations.paginate)
        """


class GetResourceShareInvitationsPaginator(Boto3Paginator):
    """
    Paginator for `get_resource_share_invitations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceShareInvitationArns: List[str] = None,
        resourceShareArns: List[str] = None,
        PaginationConfig: GetResourceShareInvitationsPaginatePaginationConfigTypeDef = None,
    ) -> GetResourceShareInvitationsPaginateResponseTypeDef:
        """
        [GetResourceShareInvitations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ram.html#RAM.Paginator.GetResourceShareInvitations.paginate)
        """


class GetResourceSharesPaginator(Boto3Paginator):
    """
    Paginator for `get_resource_shares`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        resourceShareArns: List[str] = None,
        resourceShareStatus: Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"] = None,
        name: str = None,
        tagFilters: List[GetResourceSharesPaginateTagFiltersTypeDef] = None,
        PaginationConfig: GetResourceSharesPaginatePaginationConfigTypeDef = None,
    ) -> GetResourceSharesPaginateResponseTypeDef:
        """
        [GetResourceShares.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ram.html#RAM.Paginator.GetResourceShares.paginate)
        """


class ListPrincipalsPaginator(Boto3Paginator):
    """
    Paginator for `list_principals`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        resourceArn: str = None,
        principals: List[str] = None,
        resourceType: str = None,
        resourceShareArns: List[str] = None,
        PaginationConfig: ListPrincipalsPaginatePaginationConfigTypeDef = None,
    ) -> ListPrincipalsPaginateResponseTypeDef:
        """
        [ListPrincipals.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ram.html#RAM.Paginator.ListPrincipals.paginate)
        """


class ListResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        principal: str = None,
        resourceType: str = None,
        resourceArns: List[str] = None,
        resourceShareArns: List[str] = None,
        PaginationConfig: ListResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListResourcesPaginateResponseTypeDef:
        """
        [ListResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ram.html#RAM.Paginator.ListResources.paginate)
        """
