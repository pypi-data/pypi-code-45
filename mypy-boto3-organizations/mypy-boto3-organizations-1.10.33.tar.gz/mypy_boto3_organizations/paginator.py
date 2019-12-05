"Main interface for organizations service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_organizations.type_defs import (
    ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef,
    ListAWSServiceAccessForOrganizationPaginateResponseTypeDef,
    ListAccountsForParentPaginatePaginationConfigTypeDef,
    ListAccountsForParentPaginateResponseTypeDef,
    ListAccountsPaginatePaginationConfigTypeDef,
    ListAccountsPaginateResponseTypeDef,
    ListChildrenPaginatePaginationConfigTypeDef,
    ListChildrenPaginateResponseTypeDef,
    ListCreateAccountStatusPaginatePaginationConfigTypeDef,
    ListCreateAccountStatusPaginateResponseTypeDef,
    ListHandshakesForAccountPaginateFilterTypeDef,
    ListHandshakesForAccountPaginatePaginationConfigTypeDef,
    ListHandshakesForAccountPaginateResponseTypeDef,
    ListHandshakesForOrganizationPaginateFilterTypeDef,
    ListHandshakesForOrganizationPaginatePaginationConfigTypeDef,
    ListHandshakesForOrganizationPaginateResponseTypeDef,
    ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef,
    ListOrganizationalUnitsForParentPaginateResponseTypeDef,
    ListParentsPaginatePaginationConfigTypeDef,
    ListParentsPaginateResponseTypeDef,
    ListPoliciesForTargetPaginatePaginationConfigTypeDef,
    ListPoliciesForTargetPaginateResponseTypeDef,
    ListPoliciesPaginatePaginationConfigTypeDef,
    ListPoliciesPaginateResponseTypeDef,
    ListRootsPaginatePaginationConfigTypeDef,
    ListRootsPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    ListTargetsForPolicyPaginatePaginationConfigTypeDef,
    ListTargetsForPolicyPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAWSServiceAccessForOrganizationPaginator",
    "ListAccountsPaginator",
    "ListAccountsForParentPaginator",
    "ListChildrenPaginator",
    "ListCreateAccountStatusPaginator",
    "ListHandshakesForAccountPaginator",
    "ListHandshakesForOrganizationPaginator",
    "ListOrganizationalUnitsForParentPaginator",
    "ListParentsPaginator",
    "ListPoliciesPaginator",
    "ListPoliciesForTargetPaginator",
    "ListRootsPaginator",
    "ListTagsForResourcePaginator",
    "ListTargetsForPolicyPaginator",
)


class ListAWSServiceAccessForOrganizationPaginator(Boto3Paginator):
    """
    Paginator for `list_aws_service_access_for_organization`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListAWSServiceAccessForOrganizationPaginatePaginationConfigTypeDef = None,
    ) -> ListAWSServiceAccessForOrganizationPaginateResponseTypeDef:
        """
        [ListAWSServiceAccessForOrganization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListAWSServiceAccessForOrganization.paginate)
        """


class ListAccountsPaginator(Boto3Paginator):
    """
    Paginator for `list_accounts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListAccountsPaginatePaginationConfigTypeDef = None
    ) -> ListAccountsPaginateResponseTypeDef:
        """
        [ListAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListAccounts.paginate)
        """


class ListAccountsForParentPaginator(Boto3Paginator):
    """
    Paginator for `list_accounts_for_parent`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ParentId: str,
        PaginationConfig: ListAccountsForParentPaginatePaginationConfigTypeDef = None,
    ) -> ListAccountsForParentPaginateResponseTypeDef:
        """
        [ListAccountsForParent.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListAccountsForParent.paginate)
        """


class ListChildrenPaginator(Boto3Paginator):
    """
    Paginator for `list_children`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ParentId: str,
        ChildType: Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"],
        PaginationConfig: ListChildrenPaginatePaginationConfigTypeDef = None,
    ) -> ListChildrenPaginateResponseTypeDef:
        """
        [ListChildren.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListChildren.paginate)
        """


class ListCreateAccountStatusPaginator(Boto3Paginator):
    """
    Paginator for `list_create_account_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        States: List[Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"]] = None,
        PaginationConfig: ListCreateAccountStatusPaginatePaginationConfigTypeDef = None,
    ) -> ListCreateAccountStatusPaginateResponseTypeDef:
        """
        [ListCreateAccountStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListCreateAccountStatus.paginate)
        """


class ListHandshakesForAccountPaginator(Boto3Paginator):
    """
    Paginator for `list_handshakes_for_account`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListHandshakesForAccountPaginateFilterTypeDef = None,
        PaginationConfig: ListHandshakesForAccountPaginatePaginationConfigTypeDef = None,
    ) -> ListHandshakesForAccountPaginateResponseTypeDef:
        """
        [ListHandshakesForAccount.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForAccount.paginate)
        """


class ListHandshakesForOrganizationPaginator(Boto3Paginator):
    """
    Paginator for `list_handshakes_for_organization`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListHandshakesForOrganizationPaginateFilterTypeDef = None,
        PaginationConfig: ListHandshakesForOrganizationPaginatePaginationConfigTypeDef = None,
    ) -> ListHandshakesForOrganizationPaginateResponseTypeDef:
        """
        [ListHandshakesForOrganization.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListHandshakesForOrganization.paginate)
        """


class ListOrganizationalUnitsForParentPaginator(Boto3Paginator):
    """
    Paginator for `list_organizational_units_for_parent`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ParentId: str,
        PaginationConfig: ListOrganizationalUnitsForParentPaginatePaginationConfigTypeDef = None,
    ) -> ListOrganizationalUnitsForParentPaginateResponseTypeDef:
        """
        [ListOrganizationalUnitsForParent.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListOrganizationalUnitsForParent.paginate)
        """


class ListParentsPaginator(Boto3Paginator):
    """
    Paginator for `list_parents`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ChildId: str, PaginationConfig: ListParentsPaginatePaginationConfigTypeDef = None
    ) -> ListParentsPaginateResponseTypeDef:
        """
        [ListParents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListParents.paginate)
        """


class ListPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        PaginationConfig: ListPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListPoliciesPaginateResponseTypeDef:
        """
        [ListPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListPolicies.paginate)
        """


class ListPoliciesForTargetPaginator(Boto3Paginator):
    """
    Paginator for `list_policies_for_target`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TargetId: str,
        Filter: Literal["SERVICE_CONTROL_POLICY", "TAG_POLICY"],
        PaginationConfig: ListPoliciesForTargetPaginatePaginationConfigTypeDef = None,
    ) -> ListPoliciesForTargetPaginateResponseTypeDef:
        """
        [ListPoliciesForTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListPoliciesForTarget.paginate)
        """


class ListRootsPaginator(Boto3Paginator):
    """
    Paginator for `list_roots`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListRootsPaginatePaginationConfigTypeDef = None
    ) -> ListRootsPaginateResponseTypeDef:
        """
        [ListRoots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListRoots.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceId: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListTagsForResource.paginate)
        """


class ListTargetsForPolicyPaginator(Boto3Paginator):
    """
    Paginator for `list_targets_for_policy`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PolicyId: str,
        PaginationConfig: ListTargetsForPolicyPaginatePaginationConfigTypeDef = None,
    ) -> ListTargetsForPolicyPaginateResponseTypeDef:
        """
        [ListTargetsForPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/organizations.html#Organizations.Paginator.ListTargetsForPolicy.paginate)
        """
