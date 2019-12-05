"Main interface for clouddirectory service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_clouddirectory.type_defs import (
    ListAppliedSchemaArnsPaginatePaginationConfigTypeDef,
    ListAppliedSchemaArnsPaginateResponseTypeDef,
    ListAttachedIndicesPaginatePaginationConfigTypeDef,
    ListAttachedIndicesPaginateResponseTypeDef,
    ListAttachedIndicesPaginateTargetReferenceTypeDef,
    ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef,
    ListDevelopmentSchemaArnsPaginateResponseTypeDef,
    ListDirectoriesPaginatePaginationConfigTypeDef,
    ListDirectoriesPaginateResponseTypeDef,
    ListFacetAttributesPaginatePaginationConfigTypeDef,
    ListFacetAttributesPaginateResponseTypeDef,
    ListFacetNamesPaginatePaginationConfigTypeDef,
    ListFacetNamesPaginateResponseTypeDef,
    ListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef,
    ListIncomingTypedLinksPaginateFilterTypedLinkTypeDef,
    ListIncomingTypedLinksPaginateObjectReferenceTypeDef,
    ListIncomingTypedLinksPaginatePaginationConfigTypeDef,
    ListIncomingTypedLinksPaginateResponseTypeDef,
    ListIndexPaginateIndexReferenceTypeDef,
    ListIndexPaginatePaginationConfigTypeDef,
    ListIndexPaginateRangesOnIndexedValuesTypeDef,
    ListIndexPaginateResponseTypeDef,
    ListManagedSchemaArnsPaginatePaginationConfigTypeDef,
    ListManagedSchemaArnsPaginateResponseTypeDef,
    ListObjectAttributesPaginateFacetFilterTypeDef,
    ListObjectAttributesPaginateObjectReferenceTypeDef,
    ListObjectAttributesPaginatePaginationConfigTypeDef,
    ListObjectAttributesPaginateResponseTypeDef,
    ListObjectParentPathsPaginateObjectReferenceTypeDef,
    ListObjectParentPathsPaginatePaginationConfigTypeDef,
    ListObjectParentPathsPaginateResponseTypeDef,
    ListObjectPoliciesPaginateObjectReferenceTypeDef,
    ListObjectPoliciesPaginatePaginationConfigTypeDef,
    ListObjectPoliciesPaginateResponseTypeDef,
    ListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef,
    ListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef,
    ListOutgoingTypedLinksPaginateObjectReferenceTypeDef,
    ListOutgoingTypedLinksPaginatePaginationConfigTypeDef,
    ListOutgoingTypedLinksPaginateResponseTypeDef,
    ListPolicyAttachmentsPaginatePaginationConfigTypeDef,
    ListPolicyAttachmentsPaginatePolicyReferenceTypeDef,
    ListPolicyAttachmentsPaginateResponseTypeDef,
    ListPublishedSchemaArnsPaginatePaginationConfigTypeDef,
    ListPublishedSchemaArnsPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef,
    ListTypedLinkFacetAttributesPaginateResponseTypeDef,
    ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef,
    ListTypedLinkFacetNamesPaginateResponseTypeDef,
    LookupPolicyPaginateObjectReferenceTypeDef,
    LookupPolicyPaginatePaginationConfigTypeDef,
    LookupPolicyPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAppliedSchemaArnsPaginator",
    "ListAttachedIndicesPaginator",
    "ListDevelopmentSchemaArnsPaginator",
    "ListDirectoriesPaginator",
    "ListFacetAttributesPaginator",
    "ListFacetNamesPaginator",
    "ListIncomingTypedLinksPaginator",
    "ListIndexPaginator",
    "ListManagedSchemaArnsPaginator",
    "ListObjectAttributesPaginator",
    "ListObjectParentPathsPaginator",
    "ListObjectPoliciesPaginator",
    "ListOutgoingTypedLinksPaginator",
    "ListPolicyAttachmentsPaginator",
    "ListPublishedSchemaArnsPaginator",
    "ListTagsForResourcePaginator",
    "ListTypedLinkFacetAttributesPaginator",
    "ListTypedLinkFacetNamesPaginator",
    "LookupPolicyPaginator",
)


class ListAppliedSchemaArnsPaginator(Boto3Paginator):
    """
    Paginator for `list_applied_schema_arns`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        SchemaArn: str = None,
        PaginationConfig: ListAppliedSchemaArnsPaginatePaginationConfigTypeDef = None,
    ) -> ListAppliedSchemaArnsPaginateResponseTypeDef:
        """
        [ListAppliedSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAppliedSchemaArns.paginate)
        """


class ListAttachedIndicesPaginator(Boto3Paginator):
    """
    Paginator for `list_attached_indices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        TargetReference: ListAttachedIndicesPaginateTargetReferenceTypeDef,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: ListAttachedIndicesPaginatePaginationConfigTypeDef = None,
    ) -> ListAttachedIndicesPaginateResponseTypeDef:
        """
        [ListAttachedIndices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListAttachedIndices.paginate)
        """


class ListDevelopmentSchemaArnsPaginator(Boto3Paginator):
    """
    Paginator for `list_development_schema_arns`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef = None
    ) -> ListDevelopmentSchemaArnsPaginateResponseTypeDef:
        """
        [ListDevelopmentSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDevelopmentSchemaArns.paginate)
        """


class ListDirectoriesPaginator(Boto3Paginator):
    """
    Paginator for `list_directories`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        state: Literal["ENABLED", "DISABLED", "DELETED"] = None,
        PaginationConfig: ListDirectoriesPaginatePaginationConfigTypeDef = None,
    ) -> ListDirectoriesPaginateResponseTypeDef:
        """
        [ListDirectories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListDirectories.paginate)
        """


class ListFacetAttributesPaginator(Boto3Paginator):
    """
    Paginator for `list_facet_attributes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SchemaArn: str,
        Name: str,
        PaginationConfig: ListFacetAttributesPaginatePaginationConfigTypeDef = None,
    ) -> ListFacetAttributesPaginateResponseTypeDef:
        """
        [ListFacetAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetAttributes.paginate)
        """


class ListFacetNamesPaginator(Boto3Paginator):
    """
    Paginator for `list_facet_names`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, SchemaArn: str, PaginationConfig: ListFacetNamesPaginatePaginationConfigTypeDef = None
    ) -> ListFacetNamesPaginateResponseTypeDef:
        """
        [ListFacetNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListFacetNames.paginate)
        """


class ListIncomingTypedLinksPaginator(Boto3Paginator):
    """
    Paginator for `list_incoming_typed_links`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ListIncomingTypedLinksPaginateObjectReferenceTypeDef,
        FilterAttributeRanges: List[
            ListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef
        ] = None,
        FilterTypedLink: ListIncomingTypedLinksPaginateFilterTypedLinkTypeDef = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: ListIncomingTypedLinksPaginatePaginationConfigTypeDef = None,
    ) -> ListIncomingTypedLinksPaginateResponseTypeDef:
        """
        [ListIncomingTypedLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIncomingTypedLinks.paginate)
        """


class ListIndexPaginator(Boto3Paginator):
    """
    Paginator for `list_index`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        IndexReference: ListIndexPaginateIndexReferenceTypeDef,
        RangesOnIndexedValues: List[ListIndexPaginateRangesOnIndexedValuesTypeDef] = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: ListIndexPaginatePaginationConfigTypeDef = None,
    ) -> ListIndexPaginateResponseTypeDef:
        """
        [ListIndex.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListIndex.paginate)
        """


class ListManagedSchemaArnsPaginator(Boto3Paginator):
    """
    Paginator for `list_managed_schema_arns`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SchemaArn: str = None,
        PaginationConfig: ListManagedSchemaArnsPaginatePaginationConfigTypeDef = None,
    ) -> ListManagedSchemaArnsPaginateResponseTypeDef:
        """
        [ListManagedSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListManagedSchemaArns.paginate)
        """


class ListObjectAttributesPaginator(Boto3Paginator):
    """
    Paginator for `list_object_attributes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ListObjectAttributesPaginateObjectReferenceTypeDef,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        FacetFilter: ListObjectAttributesPaginateFacetFilterTypeDef = None,
        PaginationConfig: ListObjectAttributesPaginatePaginationConfigTypeDef = None,
    ) -> ListObjectAttributesPaginateResponseTypeDef:
        """
        [ListObjectAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectAttributes.paginate)
        """


class ListObjectParentPathsPaginator(Boto3Paginator):
    """
    Paginator for `list_object_parent_paths`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ListObjectParentPathsPaginateObjectReferenceTypeDef,
        PaginationConfig: ListObjectParentPathsPaginatePaginationConfigTypeDef = None,
    ) -> ListObjectParentPathsPaginateResponseTypeDef:
        """
        [ListObjectParentPaths.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectParentPaths.paginate)
        """


class ListObjectPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `list_object_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ListObjectPoliciesPaginateObjectReferenceTypeDef,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: ListObjectPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> ListObjectPoliciesPaginateResponseTypeDef:
        """
        [ListObjectPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListObjectPolicies.paginate)
        """


class ListOutgoingTypedLinksPaginator(Boto3Paginator):
    """
    Paginator for `list_outgoing_typed_links`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: ListOutgoingTypedLinksPaginateObjectReferenceTypeDef,
        FilterAttributeRanges: List[
            ListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef
        ] = None,
        FilterTypedLink: ListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef = None,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: ListOutgoingTypedLinksPaginatePaginationConfigTypeDef = None,
    ) -> ListOutgoingTypedLinksPaginateResponseTypeDef:
        """
        [ListOutgoingTypedLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListOutgoingTypedLinks.paginate)
        """


class ListPolicyAttachmentsPaginator(Boto3Paginator):
    """
    Paginator for `list_policy_attachments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        PolicyReference: ListPolicyAttachmentsPaginatePolicyReferenceTypeDef,
        ConsistencyLevel: Literal["SERIALIZABLE", "EVENTUAL"] = None,
        PaginationConfig: ListPolicyAttachmentsPaginatePaginationConfigTypeDef = None,
    ) -> ListPolicyAttachmentsPaginateResponseTypeDef:
        """
        [ListPolicyAttachments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPolicyAttachments.paginate)
        """


class ListPublishedSchemaArnsPaginator(Boto3Paginator):
    """
    Paginator for `list_published_schema_arns`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SchemaArn: str = None,
        PaginationConfig: ListPublishedSchemaArnsPaginatePaginationConfigTypeDef = None,
    ) -> ListPublishedSchemaArnsPaginateResponseTypeDef:
        """
        [ListPublishedSchemaArns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListPublishedSchemaArns.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTagsForResource.paginate)
        """


class ListTypedLinkFacetAttributesPaginator(Boto3Paginator):
    """
    Paginator for `list_typed_link_facet_attributes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SchemaArn: str,
        Name: str,
        PaginationConfig: ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef = None,
    ) -> ListTypedLinkFacetAttributesPaginateResponseTypeDef:
        """
        [ListTypedLinkFacetAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetAttributes.paginate)
        """


class ListTypedLinkFacetNamesPaginator(Boto3Paginator):
    """
    Paginator for `list_typed_link_facet_names`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SchemaArn: str,
        PaginationConfig: ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef = None,
    ) -> ListTypedLinkFacetNamesPaginateResponseTypeDef:
        """
        [ListTypedLinkFacetNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.ListTypedLinkFacetNames.paginate)
        """


class LookupPolicyPaginator(Boto3Paginator):
    """
    Paginator for `lookup_policy`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: LookupPolicyPaginateObjectReferenceTypeDef,
        PaginationConfig: LookupPolicyPaginatePaginationConfigTypeDef = None,
    ) -> LookupPolicyPaginateResponseTypeDef:
        """
        [LookupPolicy.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/clouddirectory.html#CloudDirectory.Paginator.LookupPolicy.paginate)
        """
