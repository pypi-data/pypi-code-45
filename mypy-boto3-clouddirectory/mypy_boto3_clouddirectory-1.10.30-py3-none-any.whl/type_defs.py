"Main interface for clouddirectory service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddFacetToObjectObjectAttributeListKeyTypeDef",
    "ClientAddFacetToObjectObjectAttributeListValueTypeDef",
    "ClientAddFacetToObjectObjectAttributeListTypeDef",
    "ClientAddFacetToObjectObjectReferenceTypeDef",
    "ClientAddFacetToObjectSchemaFacetTypeDef",
    "ClientApplySchemaResponseTypeDef",
    "ClientAttachObjectChildReferenceTypeDef",
    "ClientAttachObjectParentReferenceTypeDef",
    "ClientAttachObjectResponseTypeDef",
    "ClientAttachPolicyObjectReferenceTypeDef",
    "ClientAttachPolicyPolicyReferenceTypeDef",
    "ClientAttachToIndexIndexReferenceTypeDef",
    "ClientAttachToIndexResponseTypeDef",
    "ClientAttachToIndexTargetReferenceTypeDef",
    "ClientAttachTypedLinkAttributesValueTypeDef",
    "ClientAttachTypedLinkAttributesTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef",
    "ClientAttachTypedLinkResponseTypeDef",
    "ClientAttachTypedLinkSourceObjectReferenceTypeDef",
    "ClientAttachTypedLinkTargetObjectReferenceTypeDef",
    "ClientAttachTypedLinkTypedLinkFacetTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypeDef",
    "ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef",
    "ClientBatchReadOperationsGetObjectAttributesTypeDef",
    "ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetObjectInformationTypeDef",
    "ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef",
    "ClientBatchReadOperationsListAttachedIndicesTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksTypeDef",
    "ClientBatchReadOperationsListIndexIndexReferenceTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef",
    "ClientBatchReadOperationsListIndexTypeDef",
    "ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef",
    "ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectAttributesTypeDef",
    "ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectChildrenTypeDef",
    "ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectParentPathsTypeDef",
    "ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectParentsTypeDef",
    "ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectPoliciesTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksTypeDef",
    "ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef",
    "ClientBatchReadOperationsListPolicyAttachmentsTypeDef",
    "ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef",
    "ClientBatchReadOperationsLookupPolicyTypeDef",
    "ClientBatchReadOperationsTypeDef",
    "ClientBatchReadResponseResponsesExceptionResponseTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseTypeDef",
    "ClientBatchReadResponseResponsesTypeDef",
    "ClientBatchReadResponseTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectTypeDef",
    "ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef",
    "ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef",
    "ClientBatchWriteOperationsAttachObjectTypeDef",
    "ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef",
    "ClientBatchWriteOperationsAttachPolicyTypeDef",
    "ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef",
    "ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef",
    "ClientBatchWriteOperationsAttachToIndexTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkTypeDef",
    "ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef",
    "ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef",
    "ClientBatchWriteOperationsCreateIndexTypeDef",
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef",
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef",
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef",
    "ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef",
    "ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef",
    "ClientBatchWriteOperationsCreateObjectTypeDef",
    "ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDeleteObjectTypeDef",
    "ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef",
    "ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef",
    "ClientBatchWriteOperationsDetachFromIndexTypeDef",
    "ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef",
    "ClientBatchWriteOperationsDetachObjectTypeDef",
    "ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef",
    "ClientBatchWriteOperationsDetachPolicyTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypeDef",
    "ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef",
    "ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef",
    "ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesTypeDef",
    "ClientBatchWriteOperationsTypeDef",
    "ClientBatchWriteResponseResponsesAttachObjectTypeDef",
    "ClientBatchWriteResponseResponsesAttachToIndexTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef",
    "ClientBatchWriteResponseResponsesCreateIndexTypeDef",
    "ClientBatchWriteResponseResponsesCreateObjectTypeDef",
    "ClientBatchWriteResponseResponsesDetachFromIndexTypeDef",
    "ClientBatchWriteResponseResponsesDetachObjectTypeDef",
    "ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef",
    "ClientBatchWriteResponseResponsesTypeDef",
    "ClientBatchWriteResponseTypeDef",
    "ClientCreateDirectoryResponseTypeDef",
    "ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef",
    "ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef",
    "ClientCreateFacetAttributesAttributeDefinitionTypeDef",
    "ClientCreateFacetAttributesAttributeReferenceTypeDef",
    "ClientCreateFacetAttributesTypeDef",
    "ClientCreateIndexOrderedIndexedAttributeListTypeDef",
    "ClientCreateIndexParentReferenceTypeDef",
    "ClientCreateIndexResponseTypeDef",
    "ClientCreateObjectObjectAttributeListKeyTypeDef",
    "ClientCreateObjectObjectAttributeListValueTypeDef",
    "ClientCreateObjectObjectAttributeListTypeDef",
    "ClientCreateObjectParentReferenceTypeDef",
    "ClientCreateObjectResponseTypeDef",
    "ClientCreateObjectSchemaFacetsTypeDef",
    "ClientCreateSchemaResponseTypeDef",
    "ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef",
    "ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef",
    "ClientCreateTypedLinkFacetFacetAttributesTypeDef",
    "ClientCreateTypedLinkFacetFacetTypeDef",
    "ClientDeleteDirectoryResponseTypeDef",
    "ClientDeleteObjectObjectReferenceTypeDef",
    "ClientDeleteSchemaResponseTypeDef",
    "ClientDetachFromIndexIndexReferenceTypeDef",
    "ClientDetachFromIndexResponseTypeDef",
    "ClientDetachFromIndexTargetReferenceTypeDef",
    "ClientDetachObjectParentReferenceTypeDef",
    "ClientDetachObjectResponseTypeDef",
    "ClientDetachPolicyObjectReferenceTypeDef",
    "ClientDetachPolicyPolicyReferenceTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierTypeDef",
    "ClientDisableDirectoryResponseTypeDef",
    "ClientEnableDirectoryResponseTypeDef",
    "ClientGetAppliedSchemaVersionResponseTypeDef",
    "ClientGetDirectoryResponseDirectoryTypeDef",
    "ClientGetDirectoryResponseTypeDef",
    "ClientGetFacetResponseFacetTypeDef",
    "ClientGetFacetResponseTypeDef",
    "ClientGetLinkAttributesResponseAttributesKeyTypeDef",
    "ClientGetLinkAttributesResponseAttributesValueTypeDef",
    "ClientGetLinkAttributesResponseAttributesTypeDef",
    "ClientGetLinkAttributesResponseTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientGetObjectAttributesObjectReferenceTypeDef",
    "ClientGetObjectAttributesResponseAttributesKeyTypeDef",
    "ClientGetObjectAttributesResponseAttributesValueTypeDef",
    "ClientGetObjectAttributesResponseAttributesTypeDef",
    "ClientGetObjectAttributesResponseTypeDef",
    "ClientGetObjectAttributesSchemaFacetTypeDef",
    "ClientGetObjectInformationObjectReferenceTypeDef",
    "ClientGetObjectInformationResponseSchemaFacetsTypeDef",
    "ClientGetObjectInformationResponseTypeDef",
    "ClientGetSchemaAsJsonResponseTypeDef",
    "ClientGetTypedLinkFacetInformationResponseTypeDef",
    "ClientListAppliedSchemaArnsResponseTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsTypeDef",
    "ClientListAttachedIndicesResponseTypeDef",
    "ClientListAttachedIndicesTargetReferenceTypeDef",
    "ClientListDevelopmentSchemaArnsResponseTypeDef",
    "ClientListDirectoriesResponseDirectoriesTypeDef",
    "ClientListDirectoriesResponseTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef",
    "ClientListFacetAttributesResponseAttributesTypeDef",
    "ClientListFacetAttributesResponseTypeDef",
    "ClientListFacetNamesResponseTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesTypeDef",
    "ClientListIncomingTypedLinksFilterTypedLinkTypeDef",
    "ClientListIncomingTypedLinksObjectReferenceTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef",
    "ClientListIncomingTypedLinksResponseTypeDef",
    "ClientListIndexIndexReferenceTypeDef",
    "ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    "ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    "ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    "ClientListIndexRangesOnIndexedValuesRangeTypeDef",
    "ClientListIndexRangesOnIndexedValuesTypeDef",
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef",
    "ClientListIndexResponseIndexAttachmentsTypeDef",
    "ClientListIndexResponseTypeDef",
    "ClientListManagedSchemaArnsResponseTypeDef",
    "ClientListObjectAttributesFacetFilterTypeDef",
    "ClientListObjectAttributesObjectReferenceTypeDef",
    "ClientListObjectAttributesResponseAttributesKeyTypeDef",
    "ClientListObjectAttributesResponseAttributesValueTypeDef",
    "ClientListObjectAttributesResponseAttributesTypeDef",
    "ClientListObjectAttributesResponseTypeDef",
    "ClientListObjectChildrenObjectReferenceTypeDef",
    "ClientListObjectChildrenResponseTypeDef",
    "ClientListObjectParentPathsObjectReferenceTypeDef",
    "ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef",
    "ClientListObjectParentPathsResponseTypeDef",
    "ClientListObjectParentsObjectReferenceTypeDef",
    "ClientListObjectParentsResponseParentLinksTypeDef",
    "ClientListObjectParentsResponseTypeDef",
    "ClientListObjectPoliciesObjectReferenceTypeDef",
    "ClientListObjectPoliciesResponseTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    "ClientListOutgoingTypedLinksFilterTypedLinkTypeDef",
    "ClientListOutgoingTypedLinksObjectReferenceTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef",
    "ClientListOutgoingTypedLinksResponseTypeDef",
    "ClientListPolicyAttachmentsPolicyReferenceTypeDef",
    "ClientListPolicyAttachmentsResponseTypeDef",
    "ClientListPublishedSchemaArnsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef",
    "ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef",
    "ClientListTypedLinkFacetAttributesResponseAttributesTypeDef",
    "ClientListTypedLinkFacetAttributesResponseTypeDef",
    "ClientListTypedLinkFacetNamesResponseTypeDef",
    "ClientLookupPolicyObjectReferenceTypeDef",
    "ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef",
    "ClientLookupPolicyResponsePolicyToPathListTypeDef",
    "ClientLookupPolicyResponseTypeDef",
    "ClientPublishSchemaResponseTypeDef",
    "ClientPutSchemaFromJsonResponseTypeDef",
    "ClientRemoveFacetFromObjectObjectReferenceTypeDef",
    "ClientRemoveFacetFromObjectSchemaFacetTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeTypeDef",
    "ClientUpdateFacetAttributeUpdatesTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesTypeDef",
    "ClientUpdateObjectAttributesObjectReferenceTypeDef",
    "ClientUpdateObjectAttributesResponseTypeDef",
    "ClientUpdateSchemaResponseTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef",
    "ClientUpgradeAppliedSchemaResponseTypeDef",
    "ClientUpgradePublishedSchemaResponseTypeDef",
    "ListAppliedSchemaArnsPaginatePaginationConfigTypeDef",
    "ListAppliedSchemaArnsPaginateResponseTypeDef",
    "ListAttachedIndicesPaginatePaginationConfigTypeDef",
    "ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    "ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef",
    "ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef",
    "ListAttachedIndicesPaginateResponseTypeDef",
    "ListAttachedIndicesPaginateTargetReferenceTypeDef",
    "ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef",
    "ListDevelopmentSchemaArnsPaginateResponseTypeDef",
    "ListDirectoriesPaginatePaginationConfigTypeDef",
    "ListDirectoriesPaginateResponseDirectoriesTypeDef",
    "ListDirectoriesPaginateResponseTypeDef",
    "ListFacetAttributesPaginatePaginationConfigTypeDef",
    "ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef",
    "ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef",
    "ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef",
    "ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef",
    "ListFacetAttributesPaginateResponseAttributesTypeDef",
    "ListFacetAttributesPaginateResponseTypeDef",
    "ListFacetNamesPaginatePaginationConfigTypeDef",
    "ListFacetNamesPaginateResponseTypeDef",
    "ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef",
    "ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef",
    "ListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef",
    "ListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef",
    "ListIncomingTypedLinksPaginateFilterTypedLinkTypeDef",
    "ListIncomingTypedLinksPaginateObjectReferenceTypeDef",
    "ListIncomingTypedLinksPaginatePaginationConfigTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef",
    "ListIncomingTypedLinksPaginateResponseTypeDef",
    "ListIndexPaginateIndexReferenceTypeDef",
    "ListIndexPaginatePaginationConfigTypeDef",
    "ListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef",
    "ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef",
    "ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef",
    "ListIndexPaginateRangesOnIndexedValuesRangeTypeDef",
    "ListIndexPaginateRangesOnIndexedValuesTypeDef",
    "ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    "ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef",
    "ListIndexPaginateResponseIndexAttachmentsTypeDef",
    "ListIndexPaginateResponseTypeDef",
    "ListManagedSchemaArnsPaginatePaginationConfigTypeDef",
    "ListManagedSchemaArnsPaginateResponseTypeDef",
    "ListObjectAttributesPaginateFacetFilterTypeDef",
    "ListObjectAttributesPaginateObjectReferenceTypeDef",
    "ListObjectAttributesPaginatePaginationConfigTypeDef",
    "ListObjectAttributesPaginateResponseAttributesKeyTypeDef",
    "ListObjectAttributesPaginateResponseAttributesValueTypeDef",
    "ListObjectAttributesPaginateResponseAttributesTypeDef",
    "ListObjectAttributesPaginateResponseTypeDef",
    "ListObjectParentPathsPaginateObjectReferenceTypeDef",
    "ListObjectParentPathsPaginatePaginationConfigTypeDef",
    "ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef",
    "ListObjectParentPathsPaginateResponseTypeDef",
    "ListObjectPoliciesPaginateObjectReferenceTypeDef",
    "ListObjectPoliciesPaginatePaginationConfigTypeDef",
    "ListObjectPoliciesPaginateResponseTypeDef",
    "ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef",
    "ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef",
    "ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef",
    "ListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef",
    "ListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef",
    "ListOutgoingTypedLinksPaginateObjectReferenceTypeDef",
    "ListOutgoingTypedLinksPaginatePaginationConfigTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypeDef",
    "ListPolicyAttachmentsPaginatePaginationConfigTypeDef",
    "ListPolicyAttachmentsPaginatePolicyReferenceTypeDef",
    "ListPolicyAttachmentsPaginateResponseTypeDef",
    "ListPublishedSchemaArnsPaginatePaginationConfigTypeDef",
    "ListPublishedSchemaArnsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef",
    "ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef",
    "ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef",
    "ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef",
    "ListTypedLinkFacetAttributesPaginateResponseTypeDef",
    "ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef",
    "ListTypedLinkFacetNamesPaginateResponseTypeDef",
    "LookupPolicyPaginateObjectReferenceTypeDef",
    "LookupPolicyPaginatePaginationConfigTypeDef",
    "LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef",
    "LookupPolicyPaginateResponsePolicyToPathListTypeDef",
    "LookupPolicyPaginateResponseTypeDef",
)


_RequiredClientAddFacetToObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_RequiredClientAddFacetToObjectObjectAttributeListKeyTypeDef", {"SchemaArn": str}
)
_OptionalClientAddFacetToObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_OptionalClientAddFacetToObjectObjectAttributeListKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientAddFacetToObjectObjectAttributeListKeyTypeDef(
    _RequiredClientAddFacetToObjectObjectAttributeListKeyTypeDef,
    _OptionalClientAddFacetToObjectObjectAttributeListKeyTypeDef,
):
    """
    - **Key** *(dict) --***[REQUIRED]**

      The key of the attribute.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientAddFacetToObjectObjectAttributeListValueTypeDef = TypedDict(
    "_ClientAddFacetToObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientAddFacetToObjectObjectAttributeListValueTypeDef(
    _ClientAddFacetToObjectObjectAttributeListValueTypeDef
):
    pass


_RequiredClientAddFacetToObjectObjectAttributeListTypeDef = TypedDict(
    "_RequiredClientAddFacetToObjectObjectAttributeListTypeDef",
    {"Key": ClientAddFacetToObjectObjectAttributeListKeyTypeDef},
)
_OptionalClientAddFacetToObjectObjectAttributeListTypeDef = TypedDict(
    "_OptionalClientAddFacetToObjectObjectAttributeListTypeDef",
    {"Value": ClientAddFacetToObjectObjectAttributeListValueTypeDef},
    total=False,
)


class ClientAddFacetToObjectObjectAttributeListTypeDef(
    _RequiredClientAddFacetToObjectObjectAttributeListTypeDef,
    _OptionalClientAddFacetToObjectObjectAttributeListTypeDef,
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --***[REQUIRED]**

        The key of the attribute.
        - **SchemaArn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientAddFacetToObjectObjectReferenceTypeDef = TypedDict(
    "_ClientAddFacetToObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAddFacetToObjectObjectReferenceTypeDef(_ClientAddFacetToObjectObjectReferenceTypeDef):
    """
    A reference to the object you are adding the specified facet to.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAddFacetToObjectSchemaFacetTypeDef = TypedDict(
    "_ClientAddFacetToObjectSchemaFacetTypeDef", {"SchemaArn": str, "FacetName": str}, total=False
)


class ClientAddFacetToObjectSchemaFacetTypeDef(_ClientAddFacetToObjectSchemaFacetTypeDef):
    """
    Identifiers for the facet that you are adding to the object. See  SchemaFacet for details.
    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place
      Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.
    """


_ClientApplySchemaResponseTypeDef = TypedDict(
    "_ClientApplySchemaResponseTypeDef", {"AppliedSchemaArn": str, "DirectoryArn": str}, total=False
)


class ClientApplySchemaResponseTypeDef(_ClientApplySchemaResponseTypeDef):
    """
    - *(dict) --*

      - **AppliedSchemaArn** *(string) --*

        The applied schema ARN that is associated with the copied schema in the  Directory . You can
        use this ARN to describe the schema information applied on this directory. For more
        information, see  arns .
    """


_ClientAttachObjectChildReferenceTypeDef = TypedDict(
    "_ClientAttachObjectChildReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachObjectChildReferenceTypeDef(_ClientAttachObjectChildReferenceTypeDef):
    """
    The child object reference to be attached to the object.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachObjectParentReferenceTypeDef = TypedDict(
    "_ClientAttachObjectParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachObjectParentReferenceTypeDef(_ClientAttachObjectParentReferenceTypeDef):
    """
    The parent object reference.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachObjectResponseTypeDef = TypedDict(
    "_ClientAttachObjectResponseTypeDef", {"AttachedObjectIdentifier": str}, total=False
)


class ClientAttachObjectResponseTypeDef(_ClientAttachObjectResponseTypeDef):
    """
    - *(dict) --*

      - **AttachedObjectIdentifier** *(string) --*

        The attached ``ObjectIdentifier`` , which is the child ``ObjectIdentifier`` .
    """


_ClientAttachPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientAttachPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachPolicyObjectReferenceTypeDef(_ClientAttachPolicyObjectReferenceTypeDef):
    """
    The reference that identifies the object to which the policy will be attached.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachPolicyPolicyReferenceTypeDef = TypedDict(
    "_ClientAttachPolicyPolicyReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachPolicyPolicyReferenceTypeDef(_ClientAttachPolicyPolicyReferenceTypeDef):
    """
    The reference that is associated with the policy object.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachToIndexIndexReferenceTypeDef = TypedDict(
    "_ClientAttachToIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachToIndexIndexReferenceTypeDef(_ClientAttachToIndexIndexReferenceTypeDef):
    """
    A reference to the index that you are attaching the object to.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachToIndexResponseTypeDef = TypedDict(
    "_ClientAttachToIndexResponseTypeDef", {"AttachedObjectIdentifier": str}, total=False
)


class ClientAttachToIndexResponseTypeDef(_ClientAttachToIndexResponseTypeDef):
    """
    - *(dict) --*

      - **AttachedObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` of the object that was attached to the index.
    """


_ClientAttachToIndexTargetReferenceTypeDef = TypedDict(
    "_ClientAttachToIndexTargetReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachToIndexTargetReferenceTypeDef(_ClientAttachToIndexTargetReferenceTypeDef):
    """
    A reference to the object that you are attaching to the index.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachTypedLinkAttributesValueTypeDef = TypedDict(
    "_ClientAttachTypedLinkAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientAttachTypedLinkAttributesValueTypeDef(_ClientAttachTypedLinkAttributesValueTypeDef):
    pass


_RequiredClientAttachTypedLinkAttributesTypeDef = TypedDict(
    "_RequiredClientAttachTypedLinkAttributesTypeDef", {"AttributeName": str}
)
_OptionalClientAttachTypedLinkAttributesTypeDef = TypedDict(
    "_OptionalClientAttachTypedLinkAttributesTypeDef",
    {"Value": ClientAttachTypedLinkAttributesValueTypeDef},
    total=False,
)


class ClientAttachTypedLinkAttributesTypeDef(
    _RequiredClientAttachTypedLinkAttributesTypeDef, _OptionalClientAttachTypedLinkAttributesTypeDef
):
    """
    - *(dict) --*

      Identifies the attribute name and value for a typed link.
      - **AttributeName** *(string) --***[REQUIRED]**

        The attribute name of the typed link.
    """


_ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    pass


_ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    pass


_ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    pass


_ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    pass


_ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef
):
    """
    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef
):
    """
    - **TypedLinkSpecifier** *(dict) --*

      Returns a typed link specifier as output.
      - **TypedLinkFacet** *(dict) --*

        Identifies the typed link facet that is associated with the typed link.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) that is associated with the schema. For more information,
          see  arns .
    """


_ClientAttachTypedLinkResponseTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypeDef",
    {"TypedLinkSpecifier": ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef},
    total=False,
)


class ClientAttachTypedLinkResponseTypeDef(_ClientAttachTypedLinkResponseTypeDef):
    """
    - *(dict) --*

      - **TypedLinkSpecifier** *(dict) --*

        Returns a typed link specifier as output.
        - **TypedLinkFacet** *(dict) --*

          Identifies the typed link facet that is associated with the typed link.
          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) that is associated with the schema. For more information,
            see  arns .
    """


_ClientAttachTypedLinkSourceObjectReferenceTypeDef = TypedDict(
    "_ClientAttachTypedLinkSourceObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachTypedLinkSourceObjectReferenceTypeDef(
    _ClientAttachTypedLinkSourceObjectReferenceTypeDef
):
    """
    Identifies the source object that the typed link will attach to.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachTypedLinkTargetObjectReferenceTypeDef = TypedDict(
    "_ClientAttachTypedLinkTargetObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachTypedLinkTargetObjectReferenceTypeDef(
    _ClientAttachTypedLinkTargetObjectReferenceTypeDef
):
    """
    Identifies the target object that the typed link will attach to.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientAttachTypedLinkTypedLinkFacetTypeDef = TypedDict(
    "_RequiredClientAttachTypedLinkTypedLinkFacetTypeDef", {"SchemaArn": str}
)
_OptionalClientAttachTypedLinkTypedLinkFacetTypeDef = TypedDict(
    "_OptionalClientAttachTypedLinkTypedLinkFacetTypeDef", {"TypedLinkName": str}, total=False
)


class ClientAttachTypedLinkTypedLinkFacetTypeDef(
    _RequiredClientAttachTypedLinkTypedLinkFacetTypeDef,
    _OptionalClientAttachTypedLinkTypedLinkFacetTypeDef,
):
    """
    Identifies the typed link facet that is associated with the typed link.
    - **SchemaArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .
    """


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    pass


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    pass


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef
):
    pass


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef
):
    pass


_ClientBatchReadOperationsGetLinkAttributesTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef,
        "AttributeNames": List[str],
    },
    total=False,
)


class ClientBatchReadOperationsGetLinkAttributesTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypeDef
):
    pass


_ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef(
    _ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef(
    _ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef
):
    pass


_ClientBatchReadOperationsGetObjectAttributesTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetObjectAttributesTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef,
        "SchemaFacet": ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef,
        "AttributeNames": List[str],
    },
    total=False,
)


class ClientBatchReadOperationsGetObjectAttributesTypeDef(
    _ClientBatchReadOperationsGetObjectAttributesTypeDef
):
    pass


_ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef(
    _ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsGetObjectInformationTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetObjectInformationTypeDef",
    {"ObjectReference": ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef},
    total=False,
)


class ClientBatchReadOperationsGetObjectInformationTypeDef(
    _ClientBatchReadOperationsGetObjectInformationTypeDef
):
    pass


_ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef(
    _ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef
):
    pass


_ClientBatchReadOperationsListAttachedIndicesTypeDef = TypedDict(
    "_ClientBatchReadOperationsListAttachedIndicesTypeDef",
    {
        "TargetReference": ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsListAttachedIndicesTypeDef(
    _ClientBatchReadOperationsListAttachedIndicesTypeDef
):
    pass


_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef
):
    pass


_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef
):
    pass


_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef
):
    pass


_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef",
    {
        "AttributeName": str,
        "Range": ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef
):
    pass


_ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef
):
    pass


_ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsListIncomingTypedLinksTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef,
        "FilterAttributeRanges": List[
            ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef
        ],
        "FilterTypedLink": ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksTypeDef
):
    pass


_ClientBatchReadOperationsListIndexIndexReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchReadOperationsListIndexIndexReferenceTypeDef(
    _ClientBatchReadOperationsListIndexIndexReferenceTypeDef
):
    pass


_ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef(
    _ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef
):
    pass


_ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef(
    _ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef
):
    pass


_ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef(
    _ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef
):
    pass


_ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef(
    _ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef
):
    pass


_ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef",
    {
        "AttributeKey": ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef,
        "Range": ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef(
    _ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef
):
    pass


_ClientBatchReadOperationsListIndexTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexTypeDef",
    {
        "RangesOnIndexedValues": List[
            ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef
        ],
        "IndexReference": ClientBatchReadOperationsListIndexIndexReferenceTypeDef,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadOperationsListIndexTypeDef(_ClientBatchReadOperationsListIndexTypeDef):
    pass


_ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef(
    _ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef
):
    pass


_ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef(
    _ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef
):
    """
    - **ObjectReference** *(dict) --***[REQUIRED]**

      Reference of the object whose attributes need to be listed.
      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to it
        from the directory root. Use the link names from each parent/child link to construct the
        path. Path selectors start with a slash (/) and link names are separated by slashes. For
        more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:
        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share the
        same object identifier
        * */some/path* - Identifies the object based on path
        * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsListObjectAttributesTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListObjectAttributesTypeDef",
    {"ObjectReference": ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef},
)
_OptionalClientBatchReadOperationsListObjectAttributesTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListObjectAttributesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "FacetFilter": ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListObjectAttributesTypeDef(
    _RequiredClientBatchReadOperationsListObjectAttributesTypeDef,
    _OptionalClientBatchReadOperationsListObjectAttributesTypeDef,
):
    """
    - **ListObjectAttributes** *(dict) --*

      Lists all attributes that are associated with an object.
      - **ObjectReference** *(dict) --***[REQUIRED]**

        Reference of the object whose attributes need to be listed.
        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:
          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share the
          same object identifier
          * */some/path* - Identifies the object based on path
          * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef(
    _ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsListObjectChildrenTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectChildrenTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsListObjectChildrenTypeDef(
    _ClientBatchReadOperationsListObjectChildrenTypeDef
):
    pass


_ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef(
    _ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsListObjectParentPathsTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectParentPathsTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsListObjectParentPathsTypeDef(
    _ClientBatchReadOperationsListObjectParentPathsTypeDef
):
    pass


_ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef(
    _ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsListObjectParentsTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectParentsTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsListObjectParentsTypeDef(
    _ClientBatchReadOperationsListObjectParentsTypeDef
):
    pass


_ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef(
    _ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsListObjectPoliciesTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectPoliciesTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsListObjectPoliciesTypeDef(
    _ClientBatchReadOperationsListObjectPoliciesTypeDef
):
    pass


_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef
):
    pass


_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef
):
    pass


_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef
):
    pass


_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    {
        "AttributeName": str,
        "Range": ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef
):
    pass


_ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef
):
    pass


_ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsListOutgoingTypedLinksTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef,
        "FilterAttributeRanges": List[
            ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef
        ],
        "FilterTypedLink": ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksTypeDef
):
    pass


_ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef(
    _ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef
):
    pass


_ClientBatchReadOperationsListPolicyAttachmentsTypeDef = TypedDict(
    "_ClientBatchReadOperationsListPolicyAttachmentsTypeDef",
    {
        "PolicyReference": ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsListPolicyAttachmentsTypeDef(
    _ClientBatchReadOperationsListPolicyAttachmentsTypeDef
):
    pass


_ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef(
    _ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef
):
    pass


_ClientBatchReadOperationsLookupPolicyTypeDef = TypedDict(
    "_ClientBatchReadOperationsLookupPolicyTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsLookupPolicyTypeDef(_ClientBatchReadOperationsLookupPolicyTypeDef):
    pass


_ClientBatchReadOperationsTypeDef = TypedDict(
    "_ClientBatchReadOperationsTypeDef",
    {
        "ListObjectAttributes": ClientBatchReadOperationsListObjectAttributesTypeDef,
        "ListObjectChildren": ClientBatchReadOperationsListObjectChildrenTypeDef,
        "ListAttachedIndices": ClientBatchReadOperationsListAttachedIndicesTypeDef,
        "ListObjectParentPaths": ClientBatchReadOperationsListObjectParentPathsTypeDef,
        "GetObjectInformation": ClientBatchReadOperationsGetObjectInformationTypeDef,
        "GetObjectAttributes": ClientBatchReadOperationsGetObjectAttributesTypeDef,
        "ListObjectParents": ClientBatchReadOperationsListObjectParentsTypeDef,
        "ListObjectPolicies": ClientBatchReadOperationsListObjectPoliciesTypeDef,
        "ListPolicyAttachments": ClientBatchReadOperationsListPolicyAttachmentsTypeDef,
        "LookupPolicy": ClientBatchReadOperationsLookupPolicyTypeDef,
        "ListIndex": ClientBatchReadOperationsListIndexTypeDef,
        "ListOutgoingTypedLinks": ClientBatchReadOperationsListOutgoingTypedLinksTypeDef,
        "ListIncomingTypedLinks": ClientBatchReadOperationsListIncomingTypedLinksTypeDef,
        "GetLinkAttributes": ClientBatchReadOperationsGetLinkAttributesTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsTypeDef(_ClientBatchReadOperationsTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``BatchRead`` operation.
      - **ListObjectAttributes** *(dict) --*

        Lists all attributes that are associated with an object.
        - **ObjectReference** *(dict) --***[REQUIRED]**

          Reference of the object whose attributes need to be listed.
          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:
            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier
            * */some/path* - Identifies the object based on path
            * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadResponseResponsesExceptionResponseTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesExceptionResponseTypeDef",
    {
        "Type": Literal[
            "ValidationException",
            "InvalidArnException",
            "ResourceNotFoundException",
            "InvalidNextTokenException",
            "AccessDeniedException",
            "NotNodeException",
            "FacetValidationException",
            "CannotListParentOfRootException",
            "NotIndexException",
            "NotPolicyException",
            "DirectoryNotEnabledException",
            "LimitExceededException",
            "InternalServiceException",
        ],
        "Message": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesExceptionResponseTypeDef(
    _ClientBatchReadResponseResponsesExceptionResponseTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef",
    {
        "Attributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef
        ]
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef",
    {
        "Attributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef
        ]
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef",
    {
        "SchemaFacets": List[
            ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef",
    {
        "IndexAttachments": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef",
    {
        "LinkSpecifiers": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef",
    {
        "IndexAttachments": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef
):
    """
    - **Key** *(dict) --*

      The key of the attribute.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --*

        The key of the attribute.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef",
    {
        "Attributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef
):
    """
    - **ListObjectAttributes** *(dict) --*

      Lists all attributes that are associated with an object.
      - **Attributes** *(list) --*

        The attributes map that is associated with the object. ``AttributeArn`` is the key;
        attribute value is the value.
        - *(dict) --*

          The combination of an attribute key and an attribute value.
          - **Key** *(dict) --*

            The key of the attribute.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef",
    {"Children": Dict[str, str], "NextToken": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef",
    {"Path": str, "ObjectIdentifiers": List[str]},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef",
    {
        "PathToObjectIdentifiersList": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef",
    {"ObjectIdentifier": str, "LinkName": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef",
    {
        "ParentLinks": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef",
    {"AttachedPolicyIds": List[str], "NextToken": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef",
    {
        "TypedLinkSpecifiers": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef",
    {"ObjectIdentifiers": List[str], "NextToken": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef",
    {"PolicyId": str, "ObjectIdentifier": str, "PolicyType": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef",
    {
        "Path": str,
        "Policies": List[
            ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef
        ],
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef",
    {
        "PolicyToPathList": List[
            ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef
):
    pass


_ClientBatchReadResponseResponsesSuccessfulResponseTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseTypeDef",
    {
        "ListObjectAttributes": ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef,
        "ListObjectChildren": ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef,
        "GetObjectInformation": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef,
        "GetObjectAttributes": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef,
        "ListAttachedIndices": ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef,
        "ListObjectParentPaths": ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef,
        "ListObjectPolicies": ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef,
        "ListPolicyAttachments": ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef,
        "LookupPolicy": ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef,
        "ListIndex": ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef,
        "ListOutgoingTypedLinks": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef,
        "ListIncomingTypedLinks": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef,
        "GetLinkAttributes": ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef,
        "ListObjectParents": ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseTypeDef
):
    """
    - **SuccessfulResponse** *(dict) --*

      Identifies which operation in a batch has succeeded.
      - **ListObjectAttributes** *(dict) --*

        Lists all attributes that are associated with an object.
        - **Attributes** *(list) --*

          The attributes map that is associated with the object. ``AttributeArn`` is the key;
          attribute value is the value.
          - *(dict) --*

            The combination of an attribute key and an attribute value.
            - **Key** *(dict) --*

              The key of the attribute.
              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientBatchReadResponseResponsesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesTypeDef",
    {
        "SuccessfulResponse": ClientBatchReadResponseResponsesSuccessfulResponseTypeDef,
        "ExceptionResponse": ClientBatchReadResponseResponsesExceptionResponseTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesTypeDef(_ClientBatchReadResponseResponsesTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``BatchRead`` response operation.
      - **SuccessfulResponse** *(dict) --*

        Identifies which operation in a batch has succeeded.
        - **ListObjectAttributes** *(dict) --*

          Lists all attributes that are associated with an object.
          - **Attributes** *(list) --*

            The attributes map that is associated with the object. ``AttributeArn`` is the key;
            attribute value is the value.
            - *(dict) --*

              The combination of an attribute key and an attribute value.
              - **Key** *(dict) --*

                The key of the attribute.
                - **SchemaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the schema that contains the facet and
                  attribute.
    """


_ClientBatchReadResponseTypeDef = TypedDict(
    "_ClientBatchReadResponseTypeDef",
    {"Responses": List[ClientBatchReadResponseResponsesTypeDef]},
    total=False,
)


class ClientBatchReadResponseTypeDef(_ClientBatchReadResponseTypeDef):
    """
    - *(dict) --*

      - **Responses** *(list) --*

        A list of all the responses for each batch read.
        - *(dict) --*

          Represents the output of a ``BatchRead`` response operation.
          - **SuccessfulResponse** *(dict) --*

            Identifies which operation in a batch has succeeded.
            - **ListObjectAttributes** *(dict) --*

              Lists all attributes that are associated with an object.
              - **Attributes** *(list) --*

                The attributes map that is associated with the object. ``AttributeArn`` is the key;
                attribute value is the value.
                - *(dict) --*

                  The combination of an attribute key and an attribute value.
                  - **Key** *(dict) --*

                    The key of the attribute.
                    - **SchemaArn** *(string) --*

                      The Amazon Resource Name (ARN) of the schema that contains the facet and
                      attribute.
    """


_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef
):
    pass


_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef
):
    pass


_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef",
    {
        "Key": ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef,
        "Value": ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef
):
    pass


_ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef
):
    pass


_ClientBatchWriteOperationsAddFacetToObjectTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectTypeDef",
    {
        "SchemaFacet": ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef,
        "ObjectAttributeList": List[
            ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef
        ],
        "ObjectReference": ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsAddFacetToObjectTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectTypeDef
):
    pass


_ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef(
    _ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef(
    _ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsAttachObjectTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachObjectTypeDef",
    {
        "ParentReference": ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef,
        "ChildReference": ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef,
        "LinkName": str,
    },
    total=False,
)


class ClientBatchWriteOperationsAttachObjectTypeDef(_ClientBatchWriteOperationsAttachObjectTypeDef):
    pass


_ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef(
    _ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef(
    _ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsAttachPolicyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachPolicyTypeDef",
    {
        "PolicyReference": ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef,
        "ObjectReference": ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsAttachPolicyTypeDef(_ClientBatchWriteOperationsAttachPolicyTypeDef):
    pass


_ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef(
    _ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef(
    _ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsAttachToIndexTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachToIndexTypeDef",
    {
        "IndexReference": ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef,
        "TargetReference": ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsAttachToIndexTypeDef(
    _ClientBatchWriteOperationsAttachToIndexTypeDef
):
    pass


_ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef
):
    pass


_ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef
):
    pass


_ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef
):
    pass


_ClientBatchWriteOperationsAttachTypedLinkTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkTypeDef",
    {
        "SourceObjectReference": ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef,
        "TypedLinkFacet": ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef,
        "Attributes": List[ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef],
    },
    total=False,
)


class ClientBatchWriteOperationsAttachTypedLinkTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkTypeDef
):
    pass


_ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef(
    _ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef
):
    pass


_ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef(
    _ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsCreateIndexTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateIndexTypeDef",
    {
        "OrderedIndexedAttributeList": List[
            ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef
        ],
        "IsUnique": bool,
        "ParentReference": ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)


class ClientBatchWriteOperationsCreateIndexTypeDef(_ClientBatchWriteOperationsCreateIndexTypeDef):
    pass


_ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef(
    _ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef
):
    pass


_ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef(
    _ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef
):
    pass


_ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef",
    {
        "Key": ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef,
        "Value": ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef(
    _ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef
):
    pass


_ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef(
    _ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef(
    _ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef
):
    """
    - *(dict) --*

      A facet.
      - **SchemaArn** *(string) --*

        The ARN of the schema that contains the facet with no minor component. See  arns and
        `In-Place Schema Upgrade
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
        for a description of when to provide minor versions.
    """


_RequiredClientBatchWriteOperationsCreateObjectTypeDef = TypedDict(
    "_RequiredClientBatchWriteOperationsCreateObjectTypeDef",
    {"SchemaFacet": List[ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef]},
)
_OptionalClientBatchWriteOperationsCreateObjectTypeDef = TypedDict(
    "_OptionalClientBatchWriteOperationsCreateObjectTypeDef",
    {
        "ObjectAttributeList": List[
            ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef
        ],
        "ParentReference": ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)


class ClientBatchWriteOperationsCreateObjectTypeDef(
    _RequiredClientBatchWriteOperationsCreateObjectTypeDef,
    _OptionalClientBatchWriteOperationsCreateObjectTypeDef,
):
    """
    - **CreateObject** *(dict) --*

      Creates an object.
      - **SchemaFacet** *(list) --***[REQUIRED]**

        A list of ``FacetArns`` that will be associated with the object. For more information, see
        arns .
        - *(dict) --*

          A facet.
          - **SchemaArn** *(string) --*

            The ARN of the schema that contains the facet with no minor component. See  arns and
            `In-Place Schema Upgrade
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
            for a description of when to provide minor versions.
    """


_ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef(
    _ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsDeleteObjectTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDeleteObjectTypeDef",
    {"ObjectReference": ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef},
    total=False,
)


class ClientBatchWriteOperationsDeleteObjectTypeDef(_ClientBatchWriteOperationsDeleteObjectTypeDef):
    pass


_ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef(
    _ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef(
    _ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsDetachFromIndexTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachFromIndexTypeDef",
    {
        "IndexReference": ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef,
        "TargetReference": ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsDetachFromIndexTypeDef(
    _ClientBatchWriteOperationsDetachFromIndexTypeDef
):
    pass


_ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef(
    _ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsDetachObjectTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachObjectTypeDef",
    {
        "ParentReference": ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)


class ClientBatchWriteOperationsDetachObjectTypeDef(_ClientBatchWriteOperationsDetachObjectTypeDef):
    pass


_ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef(
    _ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef", {"Selector": str}, total=False
)


class ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef(
    _ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsDetachPolicyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachPolicyTypeDef",
    {
        "PolicyReference": ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef,
        "ObjectReference": ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsDetachPolicyTypeDef(_ClientBatchWriteOperationsDetachPolicyTypeDef):
    pass


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    pass


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    pass


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef
):
    pass


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef
):
    pass


_ClientBatchWriteOperationsDetachTypedLinkTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypeDef",
    {"TypedLinkSpecifier": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef},
    total=False,
)


class ClientBatchWriteOperationsDetachTypedLinkTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypeDef
):
    pass


_ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef(
    _ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef(
    _ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef
):
    pass


_ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef = TypedDict(
    "_ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef",
    {
        "SchemaFacet": ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef,
        "ObjectReference": ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef(
    _ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    {
        "AttributeActionType": Literal["CREATE_OR_UPDATE", "DELETE"],
        "AttributeUpdateValue": ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef",
    {
        "AttributeKey": ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef,
        "AttributeAction": ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateLinkAttributesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef,
        "AttributeUpdates": List[
            ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef
        ],
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": Literal["CREATE_OR_UPDATE", "DELETE"],
        "ObjectAttributeUpdateValue": ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef",
    {
        "ObjectAttributeKey": ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef,
        "ObjectAttributeAction": ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef
):
    pass


_ClientBatchWriteOperationsUpdateObjectAttributesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesTypeDef",
    {
        "ObjectReference": ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef,
        "AttributeUpdates": List[
            ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef
        ],
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateObjectAttributesTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesTypeDef
):
    pass


_ClientBatchWriteOperationsTypeDef = TypedDict(
    "_ClientBatchWriteOperationsTypeDef",
    {
        "CreateObject": ClientBatchWriteOperationsCreateObjectTypeDef,
        "AttachObject": ClientBatchWriteOperationsAttachObjectTypeDef,
        "DetachObject": ClientBatchWriteOperationsDetachObjectTypeDef,
        "UpdateObjectAttributes": ClientBatchWriteOperationsUpdateObjectAttributesTypeDef,
        "DeleteObject": ClientBatchWriteOperationsDeleteObjectTypeDef,
        "AddFacetToObject": ClientBatchWriteOperationsAddFacetToObjectTypeDef,
        "RemoveFacetFromObject": ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef,
        "AttachPolicy": ClientBatchWriteOperationsAttachPolicyTypeDef,
        "DetachPolicy": ClientBatchWriteOperationsDetachPolicyTypeDef,
        "CreateIndex": ClientBatchWriteOperationsCreateIndexTypeDef,
        "AttachToIndex": ClientBatchWriteOperationsAttachToIndexTypeDef,
        "DetachFromIndex": ClientBatchWriteOperationsDetachFromIndexTypeDef,
        "AttachTypedLink": ClientBatchWriteOperationsAttachTypedLinkTypeDef,
        "DetachTypedLink": ClientBatchWriteOperationsDetachTypedLinkTypeDef,
        "UpdateLinkAttributes": ClientBatchWriteOperationsUpdateLinkAttributesTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsTypeDef(_ClientBatchWriteOperationsTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``BatchWrite`` operation.
      - **CreateObject** *(dict) --*

        Creates an object.
        - **SchemaFacet** *(list) --***[REQUIRED]**

          A list of ``FacetArns`` that will be associated with the object. For more information, see
          arns .
          - *(dict) --*

            A facet.
            - **SchemaArn** *(string) --*

              The ARN of the schema that contains the facet with no minor component. See  arns and
              `In-Place Schema Upgrade
              <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
              for a description of when to provide minor versions.
    """


_ClientBatchWriteResponseResponsesAttachObjectTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachObjectTypeDef",
    {"attachedObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesAttachObjectTypeDef(
    _ClientBatchWriteResponseResponsesAttachObjectTypeDef
):
    pass


_ClientBatchWriteResponseResponsesAttachToIndexTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachToIndexTypeDef",
    {"AttachedObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesAttachToIndexTypeDef(
    _ClientBatchWriteResponseResponsesAttachToIndexTypeDef
):
    pass


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    pass


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    pass


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    pass


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    pass


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef
):
    pass


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef
):
    pass


_ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef",
    {
        "TypedLinkSpecifier": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef
    },
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef
):
    pass


_ClientBatchWriteResponseResponsesCreateIndexTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesCreateIndexTypeDef", {"ObjectIdentifier": str}, total=False
)


class ClientBatchWriteResponseResponsesCreateIndexTypeDef(
    _ClientBatchWriteResponseResponsesCreateIndexTypeDef
):
    pass


_ClientBatchWriteResponseResponsesCreateObjectTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesCreateObjectTypeDef", {"ObjectIdentifier": str}, total=False
)


class ClientBatchWriteResponseResponsesCreateObjectTypeDef(
    _ClientBatchWriteResponseResponsesCreateObjectTypeDef
):
    """
    - **CreateObject** *(dict) --*

      Creates an object in a  Directory .
      - **ObjectIdentifier** *(string) --*

        The ID that is associated with the object.
    """


_ClientBatchWriteResponseResponsesDetachFromIndexTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesDetachFromIndexTypeDef",
    {"DetachedObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesDetachFromIndexTypeDef(
    _ClientBatchWriteResponseResponsesDetachFromIndexTypeDef
):
    pass


_ClientBatchWriteResponseResponsesDetachObjectTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesDetachObjectTypeDef",
    {"detachedObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesDetachObjectTypeDef(
    _ClientBatchWriteResponseResponsesDetachObjectTypeDef
):
    pass


_ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef",
    {"ObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef(
    _ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef
):
    pass


_ClientBatchWriteResponseResponsesTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesTypeDef",
    {
        "CreateObject": ClientBatchWriteResponseResponsesCreateObjectTypeDef,
        "AttachObject": ClientBatchWriteResponseResponsesAttachObjectTypeDef,
        "DetachObject": ClientBatchWriteResponseResponsesDetachObjectTypeDef,
        "UpdateObjectAttributes": ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef,
        "DeleteObject": Dict[str, Any],
        "AddFacetToObject": Dict[str, Any],
        "RemoveFacetFromObject": Dict[str, Any],
        "AttachPolicy": Dict[str, Any],
        "DetachPolicy": Dict[str, Any],
        "CreateIndex": ClientBatchWriteResponseResponsesCreateIndexTypeDef,
        "AttachToIndex": ClientBatchWriteResponseResponsesAttachToIndexTypeDef,
        "DetachFromIndex": ClientBatchWriteResponseResponsesDetachFromIndexTypeDef,
        "AttachTypedLink": ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef,
        "DetachTypedLink": Dict[str, Any],
        "UpdateLinkAttributes": Dict[str, Any],
    },
    total=False,
)


class ClientBatchWriteResponseResponsesTypeDef(_ClientBatchWriteResponseResponsesTypeDef):
    """
    - *(dict) --*

      Represents the output of a ``BatchWrite`` response operation.
      - **CreateObject** *(dict) --*

        Creates an object in a  Directory .
        - **ObjectIdentifier** *(string) --*

          The ID that is associated with the object.
    """


_ClientBatchWriteResponseTypeDef = TypedDict(
    "_ClientBatchWriteResponseTypeDef",
    {"Responses": List[ClientBatchWriteResponseResponsesTypeDef]},
    total=False,
)


class ClientBatchWriteResponseTypeDef(_ClientBatchWriteResponseTypeDef):
    """
    - *(dict) --*

      - **Responses** *(list) --*

        A list of all the responses for each batch write.
        - *(dict) --*

          Represents the output of a ``BatchWrite`` response operation.
          - **CreateObject** *(dict) --*

            Creates an object in a  Directory .
            - **ObjectIdentifier** *(string) --*

              The ID that is associated with the object.
    """


_ClientCreateDirectoryResponseTypeDef = TypedDict(
    "_ClientCreateDirectoryResponseTypeDef",
    {"DirectoryArn": str, "Name": str, "ObjectIdentifier": str, "AppliedSchemaArn": str},
    total=False,
)


class ClientCreateDirectoryResponseTypeDef(_ClientCreateDirectoryResponseTypeDef):
    """
    - *(dict) --*

      - **DirectoryArn** *(string) --*

        The ARN that is associated with the  Directory . For more information, see  arns .
    """


_ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "_ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef(
    _ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef
):
    pass


_ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef = TypedDict(
    "_ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef(
    _ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef
):
    pass


_ClientCreateFacetAttributesAttributeDefinitionTypeDef = TypedDict(
    "_ClientCreateFacetAttributesAttributeDefinitionTypeDef",
    {
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef],
    },
    total=False,
)


class ClientCreateFacetAttributesAttributeDefinitionTypeDef(
    _ClientCreateFacetAttributesAttributeDefinitionTypeDef
):
    pass


_ClientCreateFacetAttributesAttributeReferenceTypeDef = TypedDict(
    "_ClientCreateFacetAttributesAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
    total=False,
)


class ClientCreateFacetAttributesAttributeReferenceTypeDef(
    _ClientCreateFacetAttributesAttributeReferenceTypeDef
):
    pass


_RequiredClientCreateFacetAttributesTypeDef = TypedDict(
    "_RequiredClientCreateFacetAttributesTypeDef", {"Name": str}
)
_OptionalClientCreateFacetAttributesTypeDef = TypedDict(
    "_OptionalClientCreateFacetAttributesTypeDef",
    {
        "AttributeDefinition": ClientCreateFacetAttributesAttributeDefinitionTypeDef,
        "AttributeReference": ClientCreateFacetAttributesAttributeReferenceTypeDef,
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ClientCreateFacetAttributesTypeDef(
    _RequiredClientCreateFacetAttributesTypeDef, _OptionalClientCreateFacetAttributesTypeDef
):
    """
    - *(dict) --*

      An attribute that is associated with the  Facet .
      - **Name** *(string) --***[REQUIRED]**

        The name of the facet attribute.
    """


_RequiredClientCreateIndexOrderedIndexedAttributeListTypeDef = TypedDict(
    "_RequiredClientCreateIndexOrderedIndexedAttributeListTypeDef", {"SchemaArn": str}
)
_OptionalClientCreateIndexOrderedIndexedAttributeListTypeDef = TypedDict(
    "_OptionalClientCreateIndexOrderedIndexedAttributeListTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientCreateIndexOrderedIndexedAttributeListTypeDef(
    _RequiredClientCreateIndexOrderedIndexedAttributeListTypeDef,
    _OptionalClientCreateIndexOrderedIndexedAttributeListTypeDef,
):
    """
    - *(dict) --*

      A unique identifier for an attribute.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientCreateIndexParentReferenceTypeDef = TypedDict(
    "_ClientCreateIndexParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientCreateIndexParentReferenceTypeDef(_ClientCreateIndexParentReferenceTypeDef):
    """
    A reference to the parent object that contains the index object.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientCreateIndexResponseTypeDef = TypedDict(
    "_ClientCreateIndexResponseTypeDef", {"ObjectIdentifier": str}, total=False
)


class ClientCreateIndexResponseTypeDef(_ClientCreateIndexResponseTypeDef):
    """
    - *(dict) --*

      - **ObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` of the index created by this operation.
    """


_RequiredClientCreateObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_RequiredClientCreateObjectObjectAttributeListKeyTypeDef", {"SchemaArn": str}
)
_OptionalClientCreateObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_OptionalClientCreateObjectObjectAttributeListKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientCreateObjectObjectAttributeListKeyTypeDef(
    _RequiredClientCreateObjectObjectAttributeListKeyTypeDef,
    _OptionalClientCreateObjectObjectAttributeListKeyTypeDef,
):
    """
    - **Key** *(dict) --***[REQUIRED]**

      The key of the attribute.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientCreateObjectObjectAttributeListValueTypeDef = TypedDict(
    "_ClientCreateObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientCreateObjectObjectAttributeListValueTypeDef(
    _ClientCreateObjectObjectAttributeListValueTypeDef
):
    pass


_RequiredClientCreateObjectObjectAttributeListTypeDef = TypedDict(
    "_RequiredClientCreateObjectObjectAttributeListTypeDef",
    {"Key": ClientCreateObjectObjectAttributeListKeyTypeDef},
)
_OptionalClientCreateObjectObjectAttributeListTypeDef = TypedDict(
    "_OptionalClientCreateObjectObjectAttributeListTypeDef",
    {"Value": ClientCreateObjectObjectAttributeListValueTypeDef},
    total=False,
)


class ClientCreateObjectObjectAttributeListTypeDef(
    _RequiredClientCreateObjectObjectAttributeListTypeDef,
    _OptionalClientCreateObjectObjectAttributeListTypeDef,
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --***[REQUIRED]**

        The key of the attribute.
        - **SchemaArn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientCreateObjectParentReferenceTypeDef = TypedDict(
    "_ClientCreateObjectParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientCreateObjectParentReferenceTypeDef(_ClientCreateObjectParentReferenceTypeDef):
    """
    If specified, the parent reference to which this object will be attached.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientCreateObjectResponseTypeDef = TypedDict(
    "_ClientCreateObjectResponseTypeDef", {"ObjectIdentifier": str}, total=False
)


class ClientCreateObjectResponseTypeDef(_ClientCreateObjectResponseTypeDef):
    """
    - *(dict) --*

      - **ObjectIdentifier** *(string) --*

        The identifier that is associated with the object.
    """


_ClientCreateObjectSchemaFacetsTypeDef = TypedDict(
    "_ClientCreateObjectSchemaFacetsTypeDef", {"SchemaArn": str, "FacetName": str}, total=False
)


class ClientCreateObjectSchemaFacetsTypeDef(_ClientCreateObjectSchemaFacetsTypeDef):
    """
    - *(dict) --*

      A facet.
      - **SchemaArn** *(string) --*

        The ARN of the schema that contains the facet with no minor component. See  arns and
        `In-Place Schema Upgrade
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
        for a description of when to provide minor versions.
    """


_ClientCreateSchemaResponseTypeDef = TypedDict(
    "_ClientCreateSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)


class ClientCreateSchemaResponseTypeDef(_ClientCreateSchemaResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef = TypedDict(
    "_ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef(
    _ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef
):
    pass


_ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef = TypedDict(
    "_ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef(
    _ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef
):
    pass


_ClientCreateTypedLinkFacetFacetAttributesTypeDef = TypedDict(
    "_ClientCreateTypedLinkFacetFacetAttributesTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef],
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ClientCreateTypedLinkFacetFacetAttributesTypeDef(
    _ClientCreateTypedLinkFacetFacetAttributesTypeDef
):
    pass


_RequiredClientCreateTypedLinkFacetFacetTypeDef = TypedDict(
    "_RequiredClientCreateTypedLinkFacetFacetTypeDef",
    {"Name": str, "Attributes": List[ClientCreateTypedLinkFacetFacetAttributesTypeDef]},
)
_OptionalClientCreateTypedLinkFacetFacetTypeDef = TypedDict(
    "_OptionalClientCreateTypedLinkFacetFacetTypeDef",
    {"IdentityAttributeOrder": List[str]},
    total=False,
)


class ClientCreateTypedLinkFacetFacetTypeDef(
    _RequiredClientCreateTypedLinkFacetFacetTypeDef, _OptionalClientCreateTypedLinkFacetFacetTypeDef
):
    """
    Facet structure that is associated with the typed link facet.
    - **Name** *(string) --***[REQUIRED]**
    The unique name of the typed link facet.
    - **Attributes** *(list) --***[REQUIRED]**
    A set of key-value pairs associated with the typed link. Typed link attributes are used when you
    have data values that are related to the link itself, and not to one of the two objects being
    linked. Identity attributes also serve to distinguish the link from others of the same type
    between the same objects.
    - *(dict) --*

      A typed link attribute definition.
      - **Name** *(string) --***[REQUIRED]**

        The unique name of the typed link attribute.
    """


_ClientDeleteDirectoryResponseTypeDef = TypedDict(
    "_ClientDeleteDirectoryResponseTypeDef", {"DirectoryArn": str}, total=False
)


class ClientDeleteDirectoryResponseTypeDef(_ClientDeleteDirectoryResponseTypeDef):
    """
    - *(dict) --*

      - **DirectoryArn** *(string) --*

        The ARN of the deleted directory.
    """


_ClientDeleteObjectObjectReferenceTypeDef = TypedDict(
    "_ClientDeleteObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDeleteObjectObjectReferenceTypeDef(_ClientDeleteObjectObjectReferenceTypeDef):
    """
    A reference that identifies the object.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDeleteSchemaResponseTypeDef = TypedDict(
    "_ClientDeleteSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)


class ClientDeleteSchemaResponseTypeDef(_ClientDeleteSchemaResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaArn** *(string) --*

        The input ARN that is returned as part of the response. For more information, see  arns .
    """


_ClientDetachFromIndexIndexReferenceTypeDef = TypedDict(
    "_ClientDetachFromIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDetachFromIndexIndexReferenceTypeDef(_ClientDetachFromIndexIndexReferenceTypeDef):
    """
    A reference to the index object.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachFromIndexResponseTypeDef = TypedDict(
    "_ClientDetachFromIndexResponseTypeDef", {"DetachedObjectIdentifier": str}, total=False
)


class ClientDetachFromIndexResponseTypeDef(_ClientDetachFromIndexResponseTypeDef):
    """
    - *(dict) --*

      - **DetachedObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` of the object that was detached from the index.
    """


_ClientDetachFromIndexTargetReferenceTypeDef = TypedDict(
    "_ClientDetachFromIndexTargetReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDetachFromIndexTargetReferenceTypeDef(_ClientDetachFromIndexTargetReferenceTypeDef):
    """
    A reference to the object being detached from the index.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachObjectParentReferenceTypeDef = TypedDict(
    "_ClientDetachObjectParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDetachObjectParentReferenceTypeDef(_ClientDetachObjectParentReferenceTypeDef):
    """
    The parent reference from which the object with the specified link name is detached.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachObjectResponseTypeDef = TypedDict(
    "_ClientDetachObjectResponseTypeDef", {"DetachedObjectIdentifier": str}, total=False
)


class ClientDetachObjectResponseTypeDef(_ClientDetachObjectResponseTypeDef):
    """
    - *(dict) --*

      - **DetachedObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` that was detached from the object.
    """


_ClientDetachPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientDetachPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDetachPolicyObjectReferenceTypeDef(_ClientDetachPolicyObjectReferenceTypeDef):
    """
    Reference that identifies the object whose policy object will be detached.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachPolicyPolicyReferenceTypeDef = TypedDict(
    "_ClientDetachPolicyPolicyReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDetachPolicyPolicyReferenceTypeDef(_ClientDetachPolicyPolicyReferenceTypeDef):
    """
    Reference that identifies the policy object.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    pass


_ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    pass


_ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    pass


_ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    pass


_RequiredClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_RequiredClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef", {"SchemaArn": str}
)
_OptionalClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_OptionalClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef(
    _RequiredClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
    _OptionalClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
):
    """
    - **TypedLinkFacet** *(dict) --***[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_RequiredClientDetachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "_RequiredClientDetachTypedLinkTypedLinkSpecifierTypeDef",
    {"TypedLinkFacet": ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef},
)
_OptionalClientDetachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "_OptionalClientDetachTypedLinkTypedLinkSpecifierTypeDef",
    {
        "SourceObjectReference": ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierTypeDef(
    _RequiredClientDetachTypedLinkTypedLinkSpecifierTypeDef,
    _OptionalClientDetachTypedLinkTypedLinkSpecifierTypeDef,
):
    """
    Used to accept a typed link specifier as input.
    - **TypedLinkFacet** *(dict) --***[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_ClientDisableDirectoryResponseTypeDef = TypedDict(
    "_ClientDisableDirectoryResponseTypeDef", {"DirectoryArn": str}, total=False
)


class ClientDisableDirectoryResponseTypeDef(_ClientDisableDirectoryResponseTypeDef):
    """
    - *(dict) --*

      - **DirectoryArn** *(string) --*

        The ARN of the directory that has been disabled.
    """


_ClientEnableDirectoryResponseTypeDef = TypedDict(
    "_ClientEnableDirectoryResponseTypeDef", {"DirectoryArn": str}, total=False
)


class ClientEnableDirectoryResponseTypeDef(_ClientEnableDirectoryResponseTypeDef):
    """
    - *(dict) --*

      - **DirectoryArn** *(string) --*

        The ARN of the enabled directory.
    """


_ClientGetAppliedSchemaVersionResponseTypeDef = TypedDict(
    "_ClientGetAppliedSchemaVersionResponseTypeDef", {"AppliedSchemaArn": str}, total=False
)


class ClientGetAppliedSchemaVersionResponseTypeDef(_ClientGetAppliedSchemaVersionResponseTypeDef):
    """
    - *(dict) --*

      - **AppliedSchemaArn** *(string) --*

        Current applied schema ARN, including the minor version in use if one was provided.
    """


_ClientGetDirectoryResponseDirectoryTypeDef = TypedDict(
    "_ClientGetDirectoryResponseDirectoryTypeDef",
    {
        "Name": str,
        "DirectoryArn": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "CreationDateTime": datetime,
    },
    total=False,
)


class ClientGetDirectoryResponseDirectoryTypeDef(_ClientGetDirectoryResponseDirectoryTypeDef):
    """
    - **Directory** *(dict) --*

      Metadata about the directory.
      - **Name** *(string) --*

        The name of the directory.
    """


_ClientGetDirectoryResponseTypeDef = TypedDict(
    "_ClientGetDirectoryResponseTypeDef",
    {"Directory": ClientGetDirectoryResponseDirectoryTypeDef},
    total=False,
)


class ClientGetDirectoryResponseTypeDef(_ClientGetDirectoryResponseTypeDef):
    """
    - *(dict) --*

      - **Directory** *(dict) --*

        Metadata about the directory.
        - **Name** *(string) --*

          The name of the directory.
    """


_ClientGetFacetResponseFacetTypeDef = TypedDict(
    "_ClientGetFacetResponseFacetTypeDef",
    {
        "Name": str,
        "ObjectType": Literal["NODE", "LEAF_NODE", "POLICY", "INDEX"],
        "FacetStyle": Literal["STATIC", "DYNAMIC"],
    },
    total=False,
)


class ClientGetFacetResponseFacetTypeDef(_ClientGetFacetResponseFacetTypeDef):
    """
    - **Facet** *(dict) --*

      The  Facet structure that is associated with the facet.
      - **Name** *(string) --*

        The name of the  Facet .
    """


_ClientGetFacetResponseTypeDef = TypedDict(
    "_ClientGetFacetResponseTypeDef", {"Facet": ClientGetFacetResponseFacetTypeDef}, total=False
)


class ClientGetFacetResponseTypeDef(_ClientGetFacetResponseTypeDef):
    """
    - *(dict) --*

      - **Facet** *(dict) --*

        The  Facet structure that is associated with the facet.
        - **Name** *(string) --*

          The name of the  Facet .
    """


_ClientGetLinkAttributesResponseAttributesKeyTypeDef = TypedDict(
    "_ClientGetLinkAttributesResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientGetLinkAttributesResponseAttributesKeyTypeDef(
    _ClientGetLinkAttributesResponseAttributesKeyTypeDef
):
    """
    - **Key** *(dict) --*

      The key of the attribute.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientGetLinkAttributesResponseAttributesValueTypeDef = TypedDict(
    "_ClientGetLinkAttributesResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientGetLinkAttributesResponseAttributesValueTypeDef(
    _ClientGetLinkAttributesResponseAttributesValueTypeDef
):
    pass


_ClientGetLinkAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientGetLinkAttributesResponseAttributesTypeDef",
    {
        "Key": ClientGetLinkAttributesResponseAttributesKeyTypeDef,
        "Value": ClientGetLinkAttributesResponseAttributesValueTypeDef,
    },
    total=False,
)


class ClientGetLinkAttributesResponseAttributesTypeDef(
    _ClientGetLinkAttributesResponseAttributesTypeDef
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --*

        The key of the attribute.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientGetLinkAttributesResponseTypeDef = TypedDict(
    "_ClientGetLinkAttributesResponseTypeDef",
    {"Attributes": List[ClientGetLinkAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientGetLinkAttributesResponseTypeDef(_ClientGetLinkAttributesResponseTypeDef):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        The attributes that are associated with the typed link.
        - *(dict) --*

          The combination of an attribute key and an attribute value.
          - **Key** *(dict) --*

            The key of the attribute.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    pass


_ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    pass


_ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    pass


_ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    pass


_RequiredClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_RequiredClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef", {"SchemaArn": str}
)
_OptionalClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_OptionalClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef(
    _RequiredClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
    _OptionalClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
):
    """
    - **TypedLinkFacet** *(dict) --***[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_RequiredClientGetLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_RequiredClientGetLinkAttributesTypedLinkSpecifierTypeDef",
    {"TypedLinkFacet": ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef},
)
_OptionalClientGetLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_OptionalClientGetLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "SourceObjectReference": ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierTypeDef(
    _RequiredClientGetLinkAttributesTypedLinkSpecifierTypeDef,
    _OptionalClientGetLinkAttributesTypedLinkSpecifierTypeDef,
):
    """
    Allows a typed link specifier to be accepted as input.
    - **TypedLinkFacet** *(dict) --***[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_ClientGetObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientGetObjectAttributesObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientGetObjectAttributesObjectReferenceTypeDef(
    _ClientGetObjectAttributesObjectReferenceTypeDef
):
    """
    Reference that identifies the object whose attributes will be retrieved.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientGetObjectAttributesResponseAttributesKeyTypeDef = TypedDict(
    "_ClientGetObjectAttributesResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientGetObjectAttributesResponseAttributesKeyTypeDef(
    _ClientGetObjectAttributesResponseAttributesKeyTypeDef
):
    """
    - **Key** *(dict) --*

      The key of the attribute.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientGetObjectAttributesResponseAttributesValueTypeDef = TypedDict(
    "_ClientGetObjectAttributesResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientGetObjectAttributesResponseAttributesValueTypeDef(
    _ClientGetObjectAttributesResponseAttributesValueTypeDef
):
    pass


_ClientGetObjectAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientGetObjectAttributesResponseAttributesTypeDef",
    {
        "Key": ClientGetObjectAttributesResponseAttributesKeyTypeDef,
        "Value": ClientGetObjectAttributesResponseAttributesValueTypeDef,
    },
    total=False,
)


class ClientGetObjectAttributesResponseAttributesTypeDef(
    _ClientGetObjectAttributesResponseAttributesTypeDef
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --*

        The key of the attribute.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientGetObjectAttributesResponseTypeDef = TypedDict(
    "_ClientGetObjectAttributesResponseTypeDef",
    {"Attributes": List[ClientGetObjectAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientGetObjectAttributesResponseTypeDef(_ClientGetObjectAttributesResponseTypeDef):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        The attributes that are associated with the object.
        - *(dict) --*

          The combination of an attribute key and an attribute value.
          - **Key** *(dict) --*

            The key of the attribute.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientGetObjectAttributesSchemaFacetTypeDef = TypedDict(
    "_ClientGetObjectAttributesSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientGetObjectAttributesSchemaFacetTypeDef(_ClientGetObjectAttributesSchemaFacetTypeDef):
    """
    Identifier for the facet whose attributes will be retrieved. See  SchemaFacet for details.
    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place
      Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.
    """


_ClientGetObjectInformationObjectReferenceTypeDef = TypedDict(
    "_ClientGetObjectInformationObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientGetObjectInformationObjectReferenceTypeDef(
    _ClientGetObjectInformationObjectReferenceTypeDef
):
    """
    A reference to the object.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientGetObjectInformationResponseSchemaFacetsTypeDef = TypedDict(
    "_ClientGetObjectInformationResponseSchemaFacetsTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientGetObjectInformationResponseSchemaFacetsTypeDef(
    _ClientGetObjectInformationResponseSchemaFacetsTypeDef
):
    """
    - *(dict) --*

      A facet.
      - **SchemaArn** *(string) --*

        The ARN of the schema that contains the facet with no minor component. See  arns and
        `In-Place Schema Upgrade
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
        for a description of when to provide minor versions.
    """


_ClientGetObjectInformationResponseTypeDef = TypedDict(
    "_ClientGetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List[ClientGetObjectInformationResponseSchemaFacetsTypeDef],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientGetObjectInformationResponseTypeDef(_ClientGetObjectInformationResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaFacets** *(list) --*

        The facets attached to the specified object. Although the response does not include minor
        version information, the most recently applied minor version of each Facet is in effect. See
        GetAppliedSchemaVersion for details.
        - *(dict) --*

          A facet.
          - **SchemaArn** *(string) --*

            The ARN of the schema that contains the facet with no minor component. See  arns and
            `In-Place Schema Upgrade
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
            for a description of when to provide minor versions.
    """


_ClientGetSchemaAsJsonResponseTypeDef = TypedDict(
    "_ClientGetSchemaAsJsonResponseTypeDef", {"Name": str, "Document": str}, total=False
)


class ClientGetSchemaAsJsonResponseTypeDef(_ClientGetSchemaAsJsonResponseTypeDef):
    """
    - *(dict) --*

      - **Name** *(string) --*

        The name of the retrieved schema.
    """


_ClientGetTypedLinkFacetInformationResponseTypeDef = TypedDict(
    "_ClientGetTypedLinkFacetInformationResponseTypeDef",
    {"IdentityAttributeOrder": List[str]},
    total=False,
)


class ClientGetTypedLinkFacetInformationResponseTypeDef(
    _ClientGetTypedLinkFacetInformationResponseTypeDef
):
    """
    - *(dict) --*

      - **IdentityAttributeOrder** *(list) --*

        The order of identity attributes for the facet, from most significant to least significant.
        The ability to filter typed links considers the order that the attributes are defined on the
        typed link facet. When providing ranges to typed link selection, any inexact ranges must be
        specified at the end. Any attributes that do not have a range specified are presumed to
        match the entire range. Filters are interpreted in the order of the attributes on the typed
        link facet, not the order in which they are supplied to any API calls. For more information
        about identity attributes, see `Typed Links
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
        .
        - *(string) --*
    """


_ClientListAppliedSchemaArnsResponseTypeDef = TypedDict(
    "_ClientListAppliedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)


class ClientListAppliedSchemaArnsResponseTypeDef(_ClientListAppliedSchemaArnsResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaArns** *(list) --*

        The ARNs of schemas that are applied to the directory.
        - *(string) --*
    """


_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef
):
    """
    - **Key** *(dict) --*

      The key of the attribute.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef(
    _ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef
):
    pass


_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef(
    _ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --*

        The key of the attribute.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListAttachedIndicesResponseIndexAttachmentsTypeDef = TypedDict(
    "_ClientListAttachedIndicesResponseIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientListAttachedIndicesResponseIndexAttachmentsTypeDef(
    _ClientListAttachedIndicesResponseIndexAttachmentsTypeDef
):
    """
    - *(dict) --*

      Represents an index and an attached object.
      - **IndexedAttributes** *(list) --*

        The indexed attribute values.
        - *(dict) --*

          The combination of an attribute key and an attribute value.
          - **Key** *(dict) --*

            The key of the attribute.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListAttachedIndicesResponseTypeDef = TypedDict(
    "_ClientListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List[ClientListAttachedIndicesResponseIndexAttachmentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListAttachedIndicesResponseTypeDef(_ClientListAttachedIndicesResponseTypeDef):
    """
    - *(dict) --*

      - **IndexAttachments** *(list) --*

        The indices attached to the specified object.
        - *(dict) --*

          Represents an index and an attached object.
          - **IndexedAttributes** *(list) --*

            The indexed attribute values.
            - *(dict) --*

              The combination of an attribute key and an attribute value.
              - **Key** *(dict) --*

                The key of the attribute.
                - **SchemaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the schema that contains the facet and
                  attribute.
    """


_ClientListAttachedIndicesTargetReferenceTypeDef = TypedDict(
    "_ClientListAttachedIndicesTargetReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListAttachedIndicesTargetReferenceTypeDef(
    _ClientListAttachedIndicesTargetReferenceTypeDef
):
    """
    A reference to the object that has indices attached.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListDevelopmentSchemaArnsResponseTypeDef = TypedDict(
    "_ClientListDevelopmentSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)


class ClientListDevelopmentSchemaArnsResponseTypeDef(
    _ClientListDevelopmentSchemaArnsResponseTypeDef
):
    """
    - *(dict) --*

      - **SchemaArns** *(list) --*

        The ARNs of retrieved development schemas.
        - *(string) --*
    """


_ClientListDirectoriesResponseDirectoriesTypeDef = TypedDict(
    "_ClientListDirectoriesResponseDirectoriesTypeDef",
    {
        "Name": str,
        "DirectoryArn": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "CreationDateTime": datetime,
    },
    total=False,
)


class ClientListDirectoriesResponseDirectoriesTypeDef(
    _ClientListDirectoriesResponseDirectoriesTypeDef
):
    """
    - *(dict) --*

      Directory structure that includes the directory name and directory ARN.
      - **Name** *(string) --*

        The name of the directory.
    """


_ClientListDirectoriesResponseTypeDef = TypedDict(
    "_ClientListDirectoriesResponseTypeDef",
    {"Directories": List[ClientListDirectoriesResponseDirectoriesTypeDef], "NextToken": str},
    total=False,
)


class ClientListDirectoriesResponseTypeDef(_ClientListDirectoriesResponseTypeDef):
    """
    - *(dict) --*

      - **Directories** *(list) --*

        Lists all directories that are associated with your account in pagination fashion.
        - *(dict) --*

          Directory structure that includes the directory name and directory ARN.
          - **Name** *(string) --*

            The name of the directory.
    """


_ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef(
    _ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef
):
    pass


_ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef(
    _ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef
):
    pass


_ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef",
    {
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str, ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef
        ],
    },
    total=False,
)


class ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef(
    _ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef
):
    pass


_ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
    total=False,
)


class ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef(
    _ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef
):
    pass


_ClientListFacetAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseAttributesTypeDef",
    {
        "Name": str,
        "AttributeDefinition": ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef,
        "AttributeReference": ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef,
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ClientListFacetAttributesResponseAttributesTypeDef(
    _ClientListFacetAttributesResponseAttributesTypeDef
):
    """
    - *(dict) --*

      An attribute that is associated with the  Facet .
      - **Name** *(string) --*

        The name of the facet attribute.
    """


_ClientListFacetAttributesResponseTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseTypeDef",
    {"Attributes": List[ClientListFacetAttributesResponseAttributesTypeDef], "NextToken": str},
    total=False,
)


class ClientListFacetAttributesResponseTypeDef(_ClientListFacetAttributesResponseTypeDef):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        The attributes attached to the facet.
        - *(dict) --*

          An attribute that is associated with the  Facet .
          - **Name** *(string) --*

            The name of the facet attribute.
    """


_ClientListFacetNamesResponseTypeDef = TypedDict(
    "_ClientListFacetNamesResponseTypeDef", {"FacetNames": List[str], "NextToken": str}, total=False
)


class ClientListFacetNamesResponseTypeDef(_ClientListFacetNamesResponseTypeDef):
    """
    - *(dict) --*

      - **FacetNames** *(list) --*

        The names of facets that exist within the schema.
        - *(string) --*
    """


_ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef(
    _ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef
):
    pass


_ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef(
    _ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef
):
    pass


_ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef(
    _ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef
):
    pass


_ClientListIncomingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksFilterAttributeRangesTypeDef",
    {"AttributeName": str, "Range": ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef},
    total=False,
)


class ClientListIncomingTypedLinksFilterAttributeRangesTypeDef(
    _ClientListIncomingTypedLinksFilterAttributeRangesTypeDef
):
    """
    - *(dict) --*

      Identifies the range of attributes that are used by a specified filter.
      - **AttributeName** *(string) --*

        The unique name of the typed link attribute.
    """


_RequiredClientListIncomingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_RequiredClientListIncomingTypedLinksFilterTypedLinkTypeDef", {"SchemaArn": str}
)
_OptionalClientListIncomingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_OptionalClientListIncomingTypedLinksFilterTypedLinkTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ClientListIncomingTypedLinksFilterTypedLinkTypeDef(
    _RequiredClientListIncomingTypedLinksFilterTypedLinkTypeDef,
    _OptionalClientListIncomingTypedLinksFilterTypedLinkTypeDef,
):
    """
    Filters are interpreted in the order of the attributes on the typed link facet, not the order in
    which they are supplied to any API calls.
    - **SchemaArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .
    """


_ClientListIncomingTypedLinksObjectReferenceTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListIncomingTypedLinksObjectReferenceTypeDef(
    _ClientListIncomingTypedLinksObjectReferenceTypeDef
):
    """
    Reference that identifies the object whose attributes will be listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    pass


_ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef
):
    pass


_ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef
):
    pass


_ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef
):
    pass


_ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef
):
    """
    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef
):
    """
    - *(dict) --*

      Contains all the information that is used to uniquely identify a typed link. The parameters
      discussed in this topic are used to uniquely specify the typed link being operated on. The
      AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one
      as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations
      provide typed link specifiers as output. You can also construct a typed link specifier from
      scratch.
      - **TypedLinkFacet** *(dict) --*

        Identifies the typed link facet that is associated with the typed link.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) that is associated with the schema. For more information,
          see  arns .
    """


_ClientListIncomingTypedLinksResponseTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List[ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListIncomingTypedLinksResponseTypeDef(_ClientListIncomingTypedLinksResponseTypeDef):
    """
    - *(dict) --*

      - **LinkSpecifiers** *(list) --*

        Returns one or more typed link specifiers as output.
        - *(dict) --*

          Contains all the information that is used to uniquely identify a typed link. The
          parameters discussed in this topic are used to uniquely specify the typed link being
          operated on. The  AttachTypedLink API returns a typed link specifier while the
          DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and
          ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can
          also construct a typed link specifier from scratch.
          - **TypedLinkFacet** *(dict) --*

            Identifies the typed link facet that is associated with the typed link.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) that is associated with the schema. For more
              information, see  arns .
    """


_ClientListIndexIndexReferenceTypeDef = TypedDict(
    "_ClientListIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListIndexIndexReferenceTypeDef(_ClientListIndexIndexReferenceTypeDef):
    """
    The reference to the index to list.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "_RequiredClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef", {"SchemaArn": str}
)
_OptionalClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "_OptionalClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef(
    _RequiredClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef,
    _OptionalClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef,
):
    """
    - **AttributeKey** *(dict) --*

      The key of the attribute that the attribute range covers.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef = TypedDict(
    "_ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef(
    _ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef
):
    pass


_ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef = TypedDict(
    "_ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef(
    _ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef
):
    pass


_ClientListIndexRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "_ClientListIndexRangesOnIndexedValuesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientListIndexRangesOnIndexedValuesRangeTypeDef(
    _ClientListIndexRangesOnIndexedValuesRangeTypeDef
):
    pass


_ClientListIndexRangesOnIndexedValuesTypeDef = TypedDict(
    "_ClientListIndexRangesOnIndexedValuesTypeDef",
    {
        "AttributeKey": ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef,
        "Range": ClientListIndexRangesOnIndexedValuesRangeTypeDef,
    },
    total=False,
)


class ClientListIndexRangesOnIndexedValuesTypeDef(_ClientListIndexRangesOnIndexedValuesTypeDef):
    """
    - *(dict) --*

      A range of attributes.
      - **AttributeKey** *(dict) --*

        The key of the attribute that the attribute range covers.
        - **SchemaArn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef
):
    """
    - **Key** *(dict) --*

      The key of the attribute.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef(
    _ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef
):
    pass


_ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef(
    _ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --*

        The key of the attribute.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListIndexResponseIndexAttachmentsTypeDef = TypedDict(
    "_ClientListIndexResponseIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientListIndexResponseIndexAttachmentsTypeDef(
    _ClientListIndexResponseIndexAttachmentsTypeDef
):
    """
    - *(dict) --*

      Represents an index and an attached object.
      - **IndexedAttributes** *(list) --*

        The indexed attribute values.
        - *(dict) --*

          The combination of an attribute key and an attribute value.
          - **Key** *(dict) --*

            The key of the attribute.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListIndexResponseTypeDef = TypedDict(
    "_ClientListIndexResponseTypeDef",
    {"IndexAttachments": List[ClientListIndexResponseIndexAttachmentsTypeDef], "NextToken": str},
    total=False,
)


class ClientListIndexResponseTypeDef(_ClientListIndexResponseTypeDef):
    """
    - *(dict) --*

      - **IndexAttachments** *(list) --*

        The objects and indexed values attached to the index.
        - *(dict) --*

          Represents an index and an attached object.
          - **IndexedAttributes** *(list) --*

            The indexed attribute values.
            - *(dict) --*

              The combination of an attribute key and an attribute value.
              - **Key** *(dict) --*

                The key of the attribute.
                - **SchemaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the schema that contains the facet and
                  attribute.
    """


_ClientListManagedSchemaArnsResponseTypeDef = TypedDict(
    "_ClientListManagedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)


class ClientListManagedSchemaArnsResponseTypeDef(_ClientListManagedSchemaArnsResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaArns** *(list) --*

        The ARNs for all AWS managed schemas.
        - *(string) --*
    """


_ClientListObjectAttributesFacetFilterTypeDef = TypedDict(
    "_ClientListObjectAttributesFacetFilterTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientListObjectAttributesFacetFilterTypeDef(_ClientListObjectAttributesFacetFilterTypeDef):
    """
    Used to filter the list of object attributes that are associated with a certain facet.
    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place
      Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.
    """


_ClientListObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientListObjectAttributesObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListObjectAttributesObjectReferenceTypeDef(
    _ClientListObjectAttributesObjectReferenceTypeDef
):
    """
    The reference that identifies the object whose attributes will be listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListObjectAttributesResponseAttributesKeyTypeDef = TypedDict(
    "_ClientListObjectAttributesResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientListObjectAttributesResponseAttributesKeyTypeDef(
    _ClientListObjectAttributesResponseAttributesKeyTypeDef
):
    """
    - **Key** *(dict) --*

      The key of the attribute.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListObjectAttributesResponseAttributesValueTypeDef = TypedDict(
    "_ClientListObjectAttributesResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListObjectAttributesResponseAttributesValueTypeDef(
    _ClientListObjectAttributesResponseAttributesValueTypeDef
):
    pass


_ClientListObjectAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientListObjectAttributesResponseAttributesTypeDef",
    {
        "Key": ClientListObjectAttributesResponseAttributesKeyTypeDef,
        "Value": ClientListObjectAttributesResponseAttributesValueTypeDef,
    },
    total=False,
)


class ClientListObjectAttributesResponseAttributesTypeDef(
    _ClientListObjectAttributesResponseAttributesTypeDef
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --*

        The key of the attribute.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListObjectAttributesResponseTypeDef = TypedDict(
    "_ClientListObjectAttributesResponseTypeDef",
    {"Attributes": List[ClientListObjectAttributesResponseAttributesTypeDef], "NextToken": str},
    total=False,
)


class ClientListObjectAttributesResponseTypeDef(_ClientListObjectAttributesResponseTypeDef):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        Attributes map that is associated with the object. ``AttributeArn`` is the key, and
        attribute value is the value.
        - *(dict) --*

          The combination of an attribute key and an attribute value.
          - **Key** *(dict) --*

            The key of the attribute.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientListObjectChildrenObjectReferenceTypeDef = TypedDict(
    "_ClientListObjectChildrenObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListObjectChildrenObjectReferenceTypeDef(
    _ClientListObjectChildrenObjectReferenceTypeDef
):
    """
    The reference that identifies the object for which child objects are being listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListObjectChildrenResponseTypeDef = TypedDict(
    "_ClientListObjectChildrenResponseTypeDef",
    {"Children": Dict[str, str], "NextToken": str},
    total=False,
)


class ClientListObjectChildrenResponseTypeDef(_ClientListObjectChildrenResponseTypeDef):
    """
    - *(dict) --*

      - **Children** *(dict) --*

        Children structure, which is a map with key as the ``LinkName`` and ``ObjectIdentifier`` as
        the value.
        - *(string) --*

          - *(string) --*
    """


_ClientListObjectParentPathsObjectReferenceTypeDef = TypedDict(
    "_ClientListObjectParentPathsObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListObjectParentPathsObjectReferenceTypeDef(
    _ClientListObjectParentPathsObjectReferenceTypeDef
):
    """
    The reference that identifies the object whose parent paths are listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef = TypedDict(
    "_ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef",
    {"Path": str, "ObjectIdentifiers": List[str]},
    total=False,
)


class ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef(
    _ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef
):
    """
    - *(dict) --*

      Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.
      - **Path** *(string) --*

        The path that is used to identify the object starting from directory root.
    """


_ClientListObjectParentPathsResponseTypeDef = TypedDict(
    "_ClientListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List[
            ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListObjectParentPathsResponseTypeDef(_ClientListObjectParentPathsResponseTypeDef):
    """
    - *(dict) --*

      - **PathToObjectIdentifiersList** *(list) --*

        Returns the path to the ``ObjectIdentifiers`` that are associated with the directory.
        - *(dict) --*

          Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.
          - **Path** *(string) --*

            The path that is used to identify the object starting from directory root.
    """


_ClientListObjectParentsObjectReferenceTypeDef = TypedDict(
    "_ClientListObjectParentsObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListObjectParentsObjectReferenceTypeDef(_ClientListObjectParentsObjectReferenceTypeDef):
    """
    The reference that identifies the object for which parent objects are being listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListObjectParentsResponseParentLinksTypeDef = TypedDict(
    "_ClientListObjectParentsResponseParentLinksTypeDef",
    {"ObjectIdentifier": str, "LinkName": str},
    total=False,
)


class ClientListObjectParentsResponseParentLinksTypeDef(
    _ClientListObjectParentsResponseParentLinksTypeDef
):
    pass


_ClientListObjectParentsResponseTypeDef = TypedDict(
    "_ClientListObjectParentsResponseTypeDef",
    {
        "Parents": Dict[str, str],
        "NextToken": str,
        "ParentLinks": List[ClientListObjectParentsResponseParentLinksTypeDef],
    },
    total=False,
)


class ClientListObjectParentsResponseTypeDef(_ClientListObjectParentsResponseTypeDef):
    """
    - *(dict) --*

      - **Parents** *(dict) --*

        The parent structure, which is a map with key as the ``ObjectIdentifier`` and LinkName as
        the value.
        - *(string) --*

          - *(string) --*
    """


_ClientListObjectPoliciesObjectReferenceTypeDef = TypedDict(
    "_ClientListObjectPoliciesObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListObjectPoliciesObjectReferenceTypeDef(
    _ClientListObjectPoliciesObjectReferenceTypeDef
):
    """
    Reference that identifies the object for which policies will be listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListObjectPoliciesResponseTypeDef = TypedDict(
    "_ClientListObjectPoliciesResponseTypeDef",
    {"AttachedPolicyIds": List[str], "NextToken": str},
    total=False,
)


class ClientListObjectPoliciesResponseTypeDef(_ClientListObjectPoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **AttachedPolicyIds** *(list) --*

        A list of policy ``ObjectIdentifiers`` , that are attached to the object.
        - *(string) --*
    """


_ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef(
    _ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef
):
    pass


_ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef(
    _ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef
):
    pass


_ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef(
    _ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef
):
    pass


_ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    {"AttributeName": str, "Range": ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef},
    total=False,
)


class ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef(
    _ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef
):
    """
    - *(dict) --*

      Identifies the range of attributes that are used by a specified filter.
      - **AttributeName** *(string) --*

        The unique name of the typed link attribute.
    """


_RequiredClientListOutgoingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_RequiredClientListOutgoingTypedLinksFilterTypedLinkTypeDef", {"SchemaArn": str}
)
_OptionalClientListOutgoingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_OptionalClientListOutgoingTypedLinksFilterTypedLinkTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ClientListOutgoingTypedLinksFilterTypedLinkTypeDef(
    _RequiredClientListOutgoingTypedLinksFilterTypedLinkTypeDef,
    _OptionalClientListOutgoingTypedLinksFilterTypedLinkTypeDef,
):
    """
    Filters are interpreted in the order of the attributes defined on the typed link facet, not the
    order they are supplied to any API calls.
    - **SchemaArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .
    """


_ClientListOutgoingTypedLinksObjectReferenceTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListOutgoingTypedLinksObjectReferenceTypeDef(
    _ClientListOutgoingTypedLinksObjectReferenceTypeDef
):
    """
    A reference that identifies the object whose attributes will be listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    pass


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef
):
    pass


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef
):
    pass


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef
):
    pass


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef
):
    """
    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef
):
    """
    - *(dict) --*

      Contains all the information that is used to uniquely identify a typed link. The parameters
      discussed in this topic are used to uniquely specify the typed link being operated on. The
      AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one
      as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations
      provide typed link specifiers as output. You can also construct a typed link specifier from
      scratch.
      - **TypedLinkFacet** *(dict) --*

        Identifies the typed link facet that is associated with the typed link.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) that is associated with the schema. For more information,
          see  arns .
    """


_ClientListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List[ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypeDef(_ClientListOutgoingTypedLinksResponseTypeDef):
    """
    - *(dict) --*

      - **TypedLinkSpecifiers** *(list) --*

        Returns a typed link specifier as output.
        - *(dict) --*

          Contains all the information that is used to uniquely identify a typed link. The
          parameters discussed in this topic are used to uniquely specify the typed link being
          operated on. The  AttachTypedLink API returns a typed link specifier while the
          DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and
          ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can
          also construct a typed link specifier from scratch.
          - **TypedLinkFacet** *(dict) --*

            Identifies the typed link facet that is associated with the typed link.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) that is associated with the schema. For more
              information, see  arns .
    """


_ClientListPolicyAttachmentsPolicyReferenceTypeDef = TypedDict(
    "_ClientListPolicyAttachmentsPolicyReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListPolicyAttachmentsPolicyReferenceTypeDef(
    _ClientListPolicyAttachmentsPolicyReferenceTypeDef
):
    """
    The reference that identifies the policy object.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListPolicyAttachmentsResponseTypeDef = TypedDict(
    "_ClientListPolicyAttachmentsResponseTypeDef",
    {"ObjectIdentifiers": List[str], "NextToken": str},
    total=False,
)


class ClientListPolicyAttachmentsResponseTypeDef(_ClientListPolicyAttachmentsResponseTypeDef):
    """
    - *(dict) --*

      - **ObjectIdentifiers** *(list) --*

        A list of ``ObjectIdentifiers`` to which the policy is attached.
        - *(string) --*
    """


_ClientListPublishedSchemaArnsResponseTypeDef = TypedDict(
    "_ClientListPublishedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)


class ClientListPublishedSchemaArnsResponseTypeDef(_ClientListPublishedSchemaArnsResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaArns** *(list) --*

        The ARNs of published schemas.
        - *(string) --*
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      The tag structure that contains a tag key and value.
      - **Key** *(string) --*

        The key that is associated with the tag.
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

        A list of tag key value pairs that are associated with the response.
        - *(dict) --*

          The tag structure that contains a tag key and value.
          - **Key** *(string) --*

            The key that is associated with the tag.
    """


_ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef = TypedDict(
    "_ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef(
    _ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef
):
    pass


_ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef = TypedDict(
    "_ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef(
    _ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef
):
    pass


_ClientListTypedLinkFacetAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientListTypedLinkFacetAttributesResponseAttributesTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef],
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ClientListTypedLinkFacetAttributesResponseAttributesTypeDef(
    _ClientListTypedLinkFacetAttributesResponseAttributesTypeDef
):
    """
    - *(dict) --*

      A typed link attribute definition.
      - **Name** *(string) --*

        The unique name of the typed link attribute.
    """


_ClientListTypedLinkFacetAttributesResponseTypeDef = TypedDict(
    "_ClientListTypedLinkFacetAttributesResponseTypeDef",
    {
        "Attributes": List[ClientListTypedLinkFacetAttributesResponseAttributesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTypedLinkFacetAttributesResponseTypeDef(
    _ClientListTypedLinkFacetAttributesResponseTypeDef
):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        An ordered set of attributes associate with the typed link.
        - *(dict) --*

          A typed link attribute definition.
          - **Name** *(string) --*

            The unique name of the typed link attribute.
    """


_ClientListTypedLinkFacetNamesResponseTypeDef = TypedDict(
    "_ClientListTypedLinkFacetNamesResponseTypeDef",
    {"FacetNames": List[str], "NextToken": str},
    total=False,
)


class ClientListTypedLinkFacetNamesResponseTypeDef(_ClientListTypedLinkFacetNamesResponseTypeDef):
    """
    - *(dict) --*

      - **FacetNames** *(list) --*

        The names of typed link facets that exist within the schema.
        - *(string) --*
    """


_ClientLookupPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientLookupPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientLookupPolicyObjectReferenceTypeDef(_ClientLookupPolicyObjectReferenceTypeDef):
    """
    Reference that identifies the object whose policies will be looked up.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef = TypedDict(
    "_ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef",
    {"PolicyId": str, "ObjectIdentifier": str, "PolicyType": str},
    total=False,
)


class ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef(
    _ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef
):
    pass


_ClientLookupPolicyResponsePolicyToPathListTypeDef = TypedDict(
    "_ClientLookupPolicyResponsePolicyToPathListTypeDef",
    {"Path": str, "Policies": List[ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef]},
    total=False,
)


class ClientLookupPolicyResponsePolicyToPathListTypeDef(
    _ClientLookupPolicyResponsePolicyToPathListTypeDef
):
    """
    - *(dict) --*

      Used when a regular object exists in a  Directory and you want to find all of the policies
      that are associated with that object and the parent to that object.
      - **Path** *(string) --*

        The path that is referenced from the root.
    """


_ClientLookupPolicyResponseTypeDef = TypedDict(
    "_ClientLookupPolicyResponseTypeDef",
    {"PolicyToPathList": List[ClientLookupPolicyResponsePolicyToPathListTypeDef], "NextToken": str},
    total=False,
)


class ClientLookupPolicyResponseTypeDef(_ClientLookupPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyToPathList** *(list) --*

        Provides list of path to policies. Policies contain ``PolicyId`` , ``ObjectIdentifier`` ,
        and ``PolicyType`` . For more information, see `Policies
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
        .
        - *(dict) --*

          Used when a regular object exists in a  Directory and you want to find all of the policies
          that are associated with that object and the parent to that object.
          - **Path** *(string) --*

            The path that is referenced from the root.
    """


_ClientPublishSchemaResponseTypeDef = TypedDict(
    "_ClientPublishSchemaResponseTypeDef", {"PublishedSchemaArn": str}, total=False
)


class ClientPublishSchemaResponseTypeDef(_ClientPublishSchemaResponseTypeDef):
    """
    - *(dict) --*

      - **PublishedSchemaArn** *(string) --*

        The ARN that is associated with the published schema. For more information, see  arns .
    """


_ClientPutSchemaFromJsonResponseTypeDef = TypedDict(
    "_ClientPutSchemaFromJsonResponseTypeDef", {"Arn": str}, total=False
)


class ClientPutSchemaFromJsonResponseTypeDef(_ClientPutSchemaFromJsonResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The ARN of the schema to update.
    """


_ClientRemoveFacetFromObjectObjectReferenceTypeDef = TypedDict(
    "_ClientRemoveFacetFromObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientRemoveFacetFromObjectObjectReferenceTypeDef(
    _ClientRemoveFacetFromObjectObjectReferenceTypeDef
):
    """
    A reference to the object to remove the facet from.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientRemoveFacetFromObjectSchemaFacetTypeDef = TypedDict(
    "_ClientRemoveFacetFromObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientRemoveFacetFromObjectSchemaFacetTypeDef(_ClientRemoveFacetFromObjectSchemaFacetTypeDef):
    """
    The facet to remove. See  SchemaFacet for details.
    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place
      Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      The tag structure that contains a tag key and value.
      - **Key** *(string) --*

        The key that is associated with the tag.
    """


_ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "_ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef(
    _ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef
):
    pass


_ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef = TypedDict(
    "_ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef(
    _ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef
):
    pass


_ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef = TypedDict(
    "_ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef",
    {
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str, ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef(
    _ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef
):
    pass


_ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef = TypedDict(
    "_ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
    total=False,
)


class ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef(
    _ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef
):
    pass


_RequiredClientUpdateFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_RequiredClientUpdateFacetAttributeUpdatesAttributeTypeDef", {"Name": str}
)
_OptionalClientUpdateFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_OptionalClientUpdateFacetAttributeUpdatesAttributeTypeDef",
    {
        "AttributeDefinition": ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef,
        "AttributeReference": ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef,
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ClientUpdateFacetAttributeUpdatesAttributeTypeDef(
    _RequiredClientUpdateFacetAttributeUpdatesAttributeTypeDef,
    _OptionalClientUpdateFacetAttributeUpdatesAttributeTypeDef,
):
    """
    - **Attribute** *(dict) --*

      The attribute to update.
      - **Name** *(string) --***[REQUIRED]**

        The name of the facet attribute.
    """


_ClientUpdateFacetAttributeUpdatesTypeDef = TypedDict(
    "_ClientUpdateFacetAttributeUpdatesTypeDef",
    {
        "Attribute": ClientUpdateFacetAttributeUpdatesAttributeTypeDef,
        "Action": Literal["CREATE_OR_UPDATE", "DELETE"],
    },
    total=False,
)


class ClientUpdateFacetAttributeUpdatesTypeDef(_ClientUpdateFacetAttributeUpdatesTypeDef):
    """
    - *(dict) --*

      A structure that contains information used to update an attribute.
      - **Attribute** *(dict) --*

        The attribute to update.
        - **Name** *(string) --***[REQUIRED]**

          The name of the facet attribute.
    """


_ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef(
    _ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef
):
    pass


_ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    {
        "AttributeActionType": Literal["CREATE_OR_UPDATE", "DELETE"],
        "AttributeUpdateValue": ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef,
    },
    total=False,
)


class ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef(
    _ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef
):
    pass


_RequiredClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef = TypedDict(
    "_RequiredClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef", {"SchemaArn": str}
)
_OptionalClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef = TypedDict(
    "_OptionalClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef(
    _RequiredClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef,
    _OptionalClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef,
):
    """
    - **AttributeKey** *(dict) --*

      The key of the attribute being updated.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientUpdateLinkAttributesAttributeUpdatesTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesAttributeUpdatesTypeDef",
    {
        "AttributeKey": ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef,
        "AttributeAction": ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef,
    },
    total=False,
)


class ClientUpdateLinkAttributesAttributeUpdatesTypeDef(
    _ClientUpdateLinkAttributesAttributeUpdatesTypeDef
):
    """
    - *(dict) --*

      Structure that contains attribute update information.
      - **AttributeKey** *(dict) --*

        The key of the attribute being updated.
        - **SchemaArn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    pass


_ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    pass


_ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    pass


_ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    pass


_RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef", {"SchemaArn": str}
)
_OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef(
    _RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
    _OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
):
    """
    - **TypedLinkFacet** *(dict) --***[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    {"TypedLinkFacet": ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef},
)
_OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "SourceObjectReference": ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef(
    _RequiredClientUpdateLinkAttributesTypedLinkSpecifierTypeDef,
    _OptionalClientUpdateLinkAttributesTypedLinkSpecifierTypeDef,
):
    """
    Allows a typed link specifier to be accepted as input.
    - **TypedLinkFacet** *(dict) --***[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef(
    _ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef
):
    pass


_ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": Literal["CREATE_OR_UPDATE", "DELETE"],
        "ObjectAttributeUpdateValue": ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef,
    },
    total=False,
)


class ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef(
    _ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef
):
    pass


_RequiredClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef = TypedDict(
    "_RequiredClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    {"SchemaArn": str},
)
_OptionalClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef = TypedDict(
    "_OptionalClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef(
    _RequiredClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef,
    _OptionalClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef,
):
    """
    - **ObjectAttributeKey** *(dict) --*

      The key of the attribute being updated.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientUpdateObjectAttributesAttributeUpdatesTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesAttributeUpdatesTypeDef",
    {
        "ObjectAttributeKey": ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef,
        "ObjectAttributeAction": ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef,
    },
    total=False,
)


class ClientUpdateObjectAttributesAttributeUpdatesTypeDef(
    _ClientUpdateObjectAttributesAttributeUpdatesTypeDef
):
    """
    - *(dict) --*

      Structure that contains attribute update information.
      - **ObjectAttributeKey** *(dict) --*

        The key of the attribute being updated.
        - **SchemaArn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ClientUpdateObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientUpdateObjectAttributesObjectReferenceTypeDef(
    _ClientUpdateObjectAttributesObjectReferenceTypeDef
):
    """
    The reference that identifies the object.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientUpdateObjectAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesResponseTypeDef", {"ObjectIdentifier": str}, total=False
)


class ClientUpdateObjectAttributesResponseTypeDef(_ClientUpdateObjectAttributesResponseTypeDef):
    """
    - *(dict) --*

      - **ObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` of the updated object.
    """


_ClientUpdateSchemaResponseTypeDef = TypedDict(
    "_ClientUpdateSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)


class ClientUpdateSchemaResponseTypeDef(_ClientUpdateSchemaResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaArn** *(string) --*

        The ARN that is associated with the updated schema. For more information, see  arns .
    """


_ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef = TypedDict(
    "_ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef(
    _ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef
):
    pass


_ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef = TypedDict(
    "_ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef(
    _ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef
):
    pass


_RequiredClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_RequiredClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef", {"Name": str}
)
_OptionalClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_OptionalClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef",
    {
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef],
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef(
    _RequiredClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef,
    _OptionalClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef,
):
    """
    - **Attribute** *(dict) --***[REQUIRED]**

      The attribute to update.
      - **Name** *(string) --***[REQUIRED]**

        The unique name of the typed link attribute.
    """


_RequiredClientUpdateTypedLinkFacetAttributeUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateTypedLinkFacetAttributeUpdatesTypeDef",
    {"Attribute": ClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef},
)
_OptionalClientUpdateTypedLinkFacetAttributeUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateTypedLinkFacetAttributeUpdatesTypeDef",
    {"Action": Literal["CREATE_OR_UPDATE", "DELETE"]},
    total=False,
)


class ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef(
    _RequiredClientUpdateTypedLinkFacetAttributeUpdatesTypeDef,
    _OptionalClientUpdateTypedLinkFacetAttributeUpdatesTypeDef,
):
    """
    - *(dict) --*

      A typed link facet attribute update.
      - **Attribute** *(dict) --***[REQUIRED]**

        The attribute to update.
        - **Name** *(string) --***[REQUIRED]**

          The unique name of the typed link attribute.
    """


_ClientUpgradeAppliedSchemaResponseTypeDef = TypedDict(
    "_ClientUpgradeAppliedSchemaResponseTypeDef",
    {"UpgradedSchemaArn": str, "DirectoryArn": str},
    total=False,
)


class ClientUpgradeAppliedSchemaResponseTypeDef(_ClientUpgradeAppliedSchemaResponseTypeDef):
    """
    - *(dict) --*

      - **UpgradedSchemaArn** *(string) --*

        The ARN of the upgraded schema that is returned as part of the response.
    """


_ClientUpgradePublishedSchemaResponseTypeDef = TypedDict(
    "_ClientUpgradePublishedSchemaResponseTypeDef", {"UpgradedSchemaArn": str}, total=False
)


class ClientUpgradePublishedSchemaResponseTypeDef(_ClientUpgradePublishedSchemaResponseTypeDef):
    """
    - *(dict) --*

      - **UpgradedSchemaArn** *(string) --*

        The ARN of the upgraded schema that is returned as part of the response.
    """


_ListAppliedSchemaArnsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAppliedSchemaArnsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAppliedSchemaArnsPaginatePaginationConfigTypeDef(
    _ListAppliedSchemaArnsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAppliedSchemaArnsPaginateResponseTypeDef = TypedDict(
    "_ListAppliedSchemaArnsPaginateResponseTypeDef", {"SchemaArns": List[str]}, total=False
)


class ListAppliedSchemaArnsPaginateResponseTypeDef(_ListAppliedSchemaArnsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaArns** *(list) --*

        The ARNs of schemas that are applied to the directory.
        - *(string) --*
    """


_ListAttachedIndicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttachedIndicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttachedIndicesPaginatePaginationConfigTypeDef(
    _ListAttachedIndicesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef
):
    """
    - **Key** *(dict) --*

      The key of the attribute.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef(
    _ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef
):
    pass


_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef(
    _ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --*

        The key of the attribute.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef(
    _ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef
):
    """
    - *(dict) --*

      Represents an index and an attached object.
      - **IndexedAttributes** *(list) --*

        The indexed attribute values.
        - *(dict) --*

          The combination of an attribute key and an attribute value.
          - **Key** *(dict) --*

            The key of the attribute.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListAttachedIndicesPaginateResponseTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateResponseTypeDef",
    {"IndexAttachments": List[ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef]},
    total=False,
)


class ListAttachedIndicesPaginateResponseTypeDef(_ListAttachedIndicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **IndexAttachments** *(list) --*

        The indices attached to the specified object.
        - *(dict) --*

          Represents an index and an attached object.
          - **IndexedAttributes** *(list) --*

            The indexed attribute values.
            - *(dict) --*

              The combination of an attribute key and an attribute value.
              - **Key** *(dict) --*

                The key of the attribute.
                - **SchemaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the schema that contains the facet and
                  attribute.
    """


_ListAttachedIndicesPaginateTargetReferenceTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateTargetReferenceTypeDef", {"Selector": str}, total=False
)


class ListAttachedIndicesPaginateTargetReferenceTypeDef(
    _ListAttachedIndicesPaginateTargetReferenceTypeDef
):
    """
    A reference to the object that has indices attached.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef(
    _ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDevelopmentSchemaArnsPaginateResponseTypeDef = TypedDict(
    "_ListDevelopmentSchemaArnsPaginateResponseTypeDef", {"SchemaArns": List[str]}, total=False
)


class ListDevelopmentSchemaArnsPaginateResponseTypeDef(
    _ListDevelopmentSchemaArnsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SchemaArns** *(list) --*

        The ARNs of retrieved development schemas.
        - *(string) --*
    """


_ListDirectoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDirectoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDirectoriesPaginatePaginationConfigTypeDef(
    _ListDirectoriesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDirectoriesPaginateResponseDirectoriesTypeDef = TypedDict(
    "_ListDirectoriesPaginateResponseDirectoriesTypeDef",
    {
        "Name": str,
        "DirectoryArn": str,
        "State": Literal["ENABLED", "DISABLED", "DELETED"],
        "CreationDateTime": datetime,
    },
    total=False,
)


class ListDirectoriesPaginateResponseDirectoriesTypeDef(
    _ListDirectoriesPaginateResponseDirectoriesTypeDef
):
    """
    - *(dict) --*

      Directory structure that includes the directory name and directory ARN.
      - **Name** *(string) --*

        The name of the directory.
    """


_ListDirectoriesPaginateResponseTypeDef = TypedDict(
    "_ListDirectoriesPaginateResponseTypeDef",
    {"Directories": List[ListDirectoriesPaginateResponseDirectoriesTypeDef]},
    total=False,
)


class ListDirectoriesPaginateResponseTypeDef(_ListDirectoriesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Directories** *(list) --*

        Lists all directories that are associated with your account in pagination fashion.
        - *(dict) --*

          Directory structure that includes the directory name and directory ARN.
          - **Name** *(string) --*

            The name of the directory.
    """


_ListFacetAttributesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFacetAttributesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFacetAttributesPaginatePaginationConfigTypeDef(
    _ListFacetAttributesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef(
    _ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef
):
    pass


_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef(
    _ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef
):
    pass


_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef",
    {
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str, ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef
        ],
    },
    total=False,
)


class ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef(
    _ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef
):
    pass


_ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
    total=False,
)


class ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef(
    _ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef
):
    pass


_ListFacetAttributesPaginateResponseAttributesTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseAttributesTypeDef",
    {
        "Name": str,
        "AttributeDefinition": ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef,
        "AttributeReference": ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef,
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ListFacetAttributesPaginateResponseAttributesTypeDef(
    _ListFacetAttributesPaginateResponseAttributesTypeDef
):
    """
    - *(dict) --*

      An attribute that is associated with the  Facet .
      - **Name** *(string) --*

        The name of the facet attribute.
    """


_ListFacetAttributesPaginateResponseTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseTypeDef",
    {"Attributes": List[ListFacetAttributesPaginateResponseAttributesTypeDef]},
    total=False,
)


class ListFacetAttributesPaginateResponseTypeDef(_ListFacetAttributesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        The attributes attached to the facet.
        - *(dict) --*

          An attribute that is associated with the  Facet .
          - **Name** *(string) --*

            The name of the facet attribute.
    """


_ListFacetNamesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFacetNamesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFacetNamesPaginatePaginationConfigTypeDef(_ListFacetNamesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListFacetNamesPaginateResponseTypeDef = TypedDict(
    "_ListFacetNamesPaginateResponseTypeDef", {"FacetNames": List[str]}, total=False
)


class ListFacetNamesPaginateResponseTypeDef(_ListFacetNamesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **FacetNames** *(list) --*

        The names of facets that exist within the schema.
        - *(string) --*
    """


_ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef(
    _ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef
):
    pass


_ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef(
    _ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef
):
    pass


_ListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef(
    _ListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef
):
    pass


_ListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef",
    {
        "AttributeName": str,
        "Range": ListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef(
    _ListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef
):
    """
    - *(dict) --*

      Identifies the range of attributes that are used by a specified filter.
      - **AttributeName** *(string) --*

        The unique name of the typed link attribute.
    """


_RequiredListIncomingTypedLinksPaginateFilterTypedLinkTypeDef = TypedDict(
    "_RequiredListIncomingTypedLinksPaginateFilterTypedLinkTypeDef", {"SchemaArn": str}
)
_OptionalListIncomingTypedLinksPaginateFilterTypedLinkTypeDef = TypedDict(
    "_OptionalListIncomingTypedLinksPaginateFilterTypedLinkTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ListIncomingTypedLinksPaginateFilterTypedLinkTypeDef(
    _RequiredListIncomingTypedLinksPaginateFilterTypedLinkTypeDef,
    _OptionalListIncomingTypedLinksPaginateFilterTypedLinkTypeDef,
):
    """
    Filters are interpreted in the order of the attributes on the typed link facet, not the order in
    which they are supplied to any API calls.
    - **SchemaArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .
    """


_ListIncomingTypedLinksPaginateObjectReferenceTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ListIncomingTypedLinksPaginateObjectReferenceTypeDef(
    _ListIncomingTypedLinksPaginateObjectReferenceTypeDef
):
    """
    Reference that identifies the object whose attributes will be listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListIncomingTypedLinksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIncomingTypedLinksPaginatePaginationConfigTypeDef(
    _ListIncomingTypedLinksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    pass


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef
):
    pass


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef
):
    pass


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef
):
    pass


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef
):
    """
    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef
):
    """
    - *(dict) --*

      Contains all the information that is used to uniquely identify a typed link. The parameters
      discussed in this topic are used to uniquely specify the typed link being operated on. The
      AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one
      as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations
      provide typed link specifiers as output. You can also construct a typed link specifier from
      scratch.
      - **TypedLinkFacet** *(dict) --*

        Identifies the typed link facet that is associated with the typed link.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) that is associated with the schema. For more information,
          see  arns .
    """


_ListIncomingTypedLinksPaginateResponseTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseTypeDef",
    {"LinkSpecifiers": List[ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef]},
    total=False,
)


class ListIncomingTypedLinksPaginateResponseTypeDef(_ListIncomingTypedLinksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **LinkSpecifiers** *(list) --*

        Returns one or more typed link specifiers as output.
        - *(dict) --*

          Contains all the information that is used to uniquely identify a typed link. The
          parameters discussed in this topic are used to uniquely specify the typed link being
          operated on. The  AttachTypedLink API returns a typed link specifier while the
          DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and
          ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can
          also construct a typed link specifier from scratch.
          - **TypedLinkFacet** *(dict) --*

            Identifies the typed link facet that is associated with the typed link.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) that is associated with the schema. For more
              information, see  arns .
    """


_ListIndexPaginateIndexReferenceTypeDef = TypedDict(
    "_ListIndexPaginateIndexReferenceTypeDef", {"Selector": str}, total=False
)


class ListIndexPaginateIndexReferenceTypeDef(_ListIndexPaginateIndexReferenceTypeDef):
    """
    The reference to the index to list.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListIndexPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIndexPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIndexPaginatePaginationConfigTypeDef(_ListIndexPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_RequiredListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "_RequiredListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef", {"SchemaArn": str}
)
_OptionalListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "_OptionalListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef",
    {"FacetName": str, "Name": str},
    total=False,
)


class ListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef(
    _RequiredListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef,
    _OptionalListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef,
):
    """
    - **AttributeKey** *(dict) --*

      The key of the attribute that the attribute range covers.
      - **SchemaArn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef = TypedDict(
    "_ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef(
    _ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef
):
    pass


_ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef = TypedDict(
    "_ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef(
    _ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef
):
    pass


_ListIndexPaginateRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "_ListIndexPaginateRangesOnIndexedValuesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef,
    },
    total=False,
)


class ListIndexPaginateRangesOnIndexedValuesRangeTypeDef(
    _ListIndexPaginateRangesOnIndexedValuesRangeTypeDef
):
    pass


_ListIndexPaginateRangesOnIndexedValuesTypeDef = TypedDict(
    "_ListIndexPaginateRangesOnIndexedValuesTypeDef",
    {
        "AttributeKey": ListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef,
        "Range": ListIndexPaginateRangesOnIndexedValuesRangeTypeDef,
    },
    total=False,
)


class ListIndexPaginateRangesOnIndexedValuesTypeDef(_ListIndexPaginateRangesOnIndexedValuesTypeDef):
    """
    - *(dict) --*

      A range of attributes.
      - **AttributeKey** *(dict) --*

        The key of the attribute that the attribute range covers.
        - **SchemaArn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef
):
    """
    - **Key** *(dict) --*

      The key of the attribute.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef(
    _ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef
):
    pass


_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef(
    _ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --*

        The key of the attribute.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListIndexPaginateResponseIndexAttachmentsTypeDef = TypedDict(
    "_ListIndexPaginateResponseIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ListIndexPaginateResponseIndexAttachmentsTypeDef(
    _ListIndexPaginateResponseIndexAttachmentsTypeDef
):
    """
    - *(dict) --*

      Represents an index and an attached object.
      - **IndexedAttributes** *(list) --*

        The indexed attribute values.
        - *(dict) --*

          The combination of an attribute key and an attribute value.
          - **Key** *(dict) --*

            The key of the attribute.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListIndexPaginateResponseTypeDef = TypedDict(
    "_ListIndexPaginateResponseTypeDef",
    {"IndexAttachments": List[ListIndexPaginateResponseIndexAttachmentsTypeDef]},
    total=False,
)


class ListIndexPaginateResponseTypeDef(_ListIndexPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **IndexAttachments** *(list) --*

        The objects and indexed values attached to the index.
        - *(dict) --*

          Represents an index and an attached object.
          - **IndexedAttributes** *(list) --*

            The indexed attribute values.
            - *(dict) --*

              The combination of an attribute key and an attribute value.
              - **Key** *(dict) --*

                The key of the attribute.
                - **SchemaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the schema that contains the facet and
                  attribute.
    """


_ListManagedSchemaArnsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListManagedSchemaArnsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListManagedSchemaArnsPaginatePaginationConfigTypeDef(
    _ListManagedSchemaArnsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListManagedSchemaArnsPaginateResponseTypeDef = TypedDict(
    "_ListManagedSchemaArnsPaginateResponseTypeDef", {"SchemaArns": List[str]}, total=False
)


class ListManagedSchemaArnsPaginateResponseTypeDef(_ListManagedSchemaArnsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaArns** *(list) --*

        The ARNs for all AWS managed schemas.
        - *(string) --*
    """


_ListObjectAttributesPaginateFacetFilterTypeDef = TypedDict(
    "_ListObjectAttributesPaginateFacetFilterTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ListObjectAttributesPaginateFacetFilterTypeDef(
    _ListObjectAttributesPaginateFacetFilterTypeDef
):
    """
    Used to filter the list of object attributes that are associated with a certain facet.
    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place
      Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.
    """


_ListObjectAttributesPaginateObjectReferenceTypeDef = TypedDict(
    "_ListObjectAttributesPaginateObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ListObjectAttributesPaginateObjectReferenceTypeDef(
    _ListObjectAttributesPaginateObjectReferenceTypeDef
):
    """
    The reference that identifies the object whose attributes will be listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListObjectAttributesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectAttributesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectAttributesPaginatePaginationConfigTypeDef(
    _ListObjectAttributesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListObjectAttributesPaginateResponseAttributesKeyTypeDef = TypedDict(
    "_ListObjectAttributesPaginateResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ListObjectAttributesPaginateResponseAttributesKeyTypeDef(
    _ListObjectAttributesPaginateResponseAttributesKeyTypeDef
):
    """
    - **Key** *(dict) --*

      The key of the attribute.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListObjectAttributesPaginateResponseAttributesValueTypeDef = TypedDict(
    "_ListObjectAttributesPaginateResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListObjectAttributesPaginateResponseAttributesValueTypeDef(
    _ListObjectAttributesPaginateResponseAttributesValueTypeDef
):
    pass


_ListObjectAttributesPaginateResponseAttributesTypeDef = TypedDict(
    "_ListObjectAttributesPaginateResponseAttributesTypeDef",
    {
        "Key": ListObjectAttributesPaginateResponseAttributesKeyTypeDef,
        "Value": ListObjectAttributesPaginateResponseAttributesValueTypeDef,
    },
    total=False,
)


class ListObjectAttributesPaginateResponseAttributesTypeDef(
    _ListObjectAttributesPaginateResponseAttributesTypeDef
):
    """
    - *(dict) --*

      The combination of an attribute key and an attribute value.
      - **Key** *(dict) --*

        The key of the attribute.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListObjectAttributesPaginateResponseTypeDef = TypedDict(
    "_ListObjectAttributesPaginateResponseTypeDef",
    {"Attributes": List[ListObjectAttributesPaginateResponseAttributesTypeDef]},
    total=False,
)


class ListObjectAttributesPaginateResponseTypeDef(_ListObjectAttributesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        Attributes map that is associated with the object. ``AttributeArn`` is the key, and
        attribute value is the value.
        - *(dict) --*

          The combination of an attribute key and an attribute value.
          - **Key** *(dict) --*

            The key of the attribute.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.
    """


_ListObjectParentPathsPaginateObjectReferenceTypeDef = TypedDict(
    "_ListObjectParentPathsPaginateObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ListObjectParentPathsPaginateObjectReferenceTypeDef(
    _ListObjectParentPathsPaginateObjectReferenceTypeDef
):
    """
    The reference that identifies the object whose parent paths are listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListObjectParentPathsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectParentPathsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectParentPathsPaginatePaginationConfigTypeDef(
    _ListObjectParentPathsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef = TypedDict(
    "_ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef",
    {"Path": str, "ObjectIdentifiers": List[str]},
    total=False,
)


class ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef(
    _ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef
):
    """
    - *(dict) --*

      Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.
      - **Path** *(string) --*

        The path that is used to identify the object starting from directory root.
    """


_ListObjectParentPathsPaginateResponseTypeDef = TypedDict(
    "_ListObjectParentPathsPaginateResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List[
            ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef
        ]
    },
    total=False,
)


class ListObjectParentPathsPaginateResponseTypeDef(_ListObjectParentPathsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **PathToObjectIdentifiersList** *(list) --*

        Returns the path to the ``ObjectIdentifiers`` that are associated with the directory.
        - *(dict) --*

          Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.
          - **Path** *(string) --*

            The path that is used to identify the object starting from directory root.
    """


_ListObjectPoliciesPaginateObjectReferenceTypeDef = TypedDict(
    "_ListObjectPoliciesPaginateObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ListObjectPoliciesPaginateObjectReferenceTypeDef(
    _ListObjectPoliciesPaginateObjectReferenceTypeDef
):
    """
    Reference that identifies the object for which policies will be listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListObjectPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectPoliciesPaginatePaginationConfigTypeDef(
    _ListObjectPoliciesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListObjectPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListObjectPoliciesPaginateResponseTypeDef", {"AttachedPolicyIds": List[str]}, total=False
)


class ListObjectPoliciesPaginateResponseTypeDef(_ListObjectPoliciesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **AttachedPolicyIds** *(list) --*

        A list of policy ``ObjectIdentifiers`` , that are attached to the object.
        - *(string) --*
    """


_ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef(
    _ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef
):
    pass


_ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef(
    _ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef
):
    pass


_ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef",
    {
        "StartMode": Literal[
            "FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"
        ],
        "StartValue": ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef,
        "EndMode": Literal["FIRST", "LAST", "LAST_BEFORE_MISSING_VALUES", "INCLUSIVE", "EXCLUSIVE"],
        "EndValue": ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef(
    _ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef
):
    pass


_ListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef",
    {
        "AttributeName": str,
        "Range": ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef(
    _ListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef
):
    """
    - *(dict) --*

      Identifies the range of attributes that are used by a specified filter.
      - **AttributeName** *(string) --*

        The unique name of the typed link attribute.
    """


_RequiredListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef = TypedDict(
    "_RequiredListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef", {"SchemaArn": str}
)
_OptionalListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef = TypedDict(
    "_OptionalListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef",
    {"TypedLinkName": str},
    total=False,
)


class ListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef(
    _RequiredListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef,
    _OptionalListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef,
):
    """
    Filters are interpreted in the order of the attributes defined on the typed link facet, not the
    order they are supplied to any API calls.
    - **SchemaArn** *(string) --***[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .
    """


_ListOutgoingTypedLinksPaginateObjectReferenceTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ListOutgoingTypedLinksPaginateObjectReferenceTypeDef(
    _ListOutgoingTypedLinksPaginateObjectReferenceTypeDef
):
    """
    A reference that identifies the object whose attributes will be listed.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListOutgoingTypedLinksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOutgoingTypedLinksPaginatePaginationConfigTypeDef(
    _ListOutgoingTypedLinksPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    pass


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef
):
    pass


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef
):
    pass


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef
):
    pass


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef
):
    """
    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.
      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .
    """


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef
):
    """
    - *(dict) --*

      Contains all the information that is used to uniquely identify a typed link. The parameters
      discussed in this topic are used to uniquely specify the typed link being operated on. The
      AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts one
      as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations
      provide typed link specifiers as output. You can also construct a typed link specifier from
      scratch.
      - **TypedLinkFacet** *(dict) --*

        Identifies the typed link facet that is associated with the typed link.
        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) that is associated with the schema. For more information,
          see  arns .
    """


_ListOutgoingTypedLinksPaginateResponseTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypeDef",
    {"TypedLinkSpecifiers": List[ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef]},
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypeDef(_ListOutgoingTypedLinksPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TypedLinkSpecifiers** *(list) --*

        Returns a typed link specifier as output.
        - *(dict) --*

          Contains all the information that is used to uniquely identify a typed link. The
          parameters discussed in this topic are used to uniquely specify the typed link being
          operated on. The  AttachTypedLink API returns a typed link specifier while the
          DetachTypedLink API accepts one as input. Similarly, the  ListIncomingTypedLinks and
          ListOutgoingTypedLinks API operations provide typed link specifiers as output. You can
          also construct a typed link specifier from scratch.
          - **TypedLinkFacet** *(dict) --*

            Identifies the typed link facet that is associated with the typed link.
            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) that is associated with the schema. For more
              information, see  arns .
    """


_ListPolicyAttachmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPolicyAttachmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPolicyAttachmentsPaginatePaginationConfigTypeDef(
    _ListPolicyAttachmentsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPolicyAttachmentsPaginatePolicyReferenceTypeDef = TypedDict(
    "_ListPolicyAttachmentsPaginatePolicyReferenceTypeDef", {"Selector": str}, total=False
)


class ListPolicyAttachmentsPaginatePolicyReferenceTypeDef(
    _ListPolicyAttachmentsPaginatePolicyReferenceTypeDef
):
    """
    The reference that identifies the policy object.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListPolicyAttachmentsPaginateResponseTypeDef = TypedDict(
    "_ListPolicyAttachmentsPaginateResponseTypeDef", {"ObjectIdentifiers": List[str]}, total=False
)


class ListPolicyAttachmentsPaginateResponseTypeDef(_ListPolicyAttachmentsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ObjectIdentifiers** *(list) --*

        A list of ``ObjectIdentifiers`` to which the policy is attached.
        - *(string) --*
    """


_ListPublishedSchemaArnsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPublishedSchemaArnsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPublishedSchemaArnsPaginatePaginationConfigTypeDef(
    _ListPublishedSchemaArnsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPublishedSchemaArnsPaginateResponseTypeDef = TypedDict(
    "_ListPublishedSchemaArnsPaginateResponseTypeDef", {"SchemaArns": List[str]}, total=False
)


class ListPublishedSchemaArnsPaginateResponseTypeDef(
    _ListPublishedSchemaArnsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SchemaArns** *(list) --*

        The ARNs of published schemas.
        - *(string) --*
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

      The tag structure that contains a tag key and value.
      - **Key** *(string) --*

        The key that is associated with the tag.
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

        A list of tag key value pairs that are associated with the response.
        - *(dict) --*

          The tag structure that contains a tag key and value.
          - **Key** *(string) --*

            The key that is associated with the tag.
    """


_ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef(
    _ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef = TypedDict(
    "_ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef(
    _ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef
):
    pass


_ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef = TypedDict(
    "_ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef",
    {
        "Type": Literal["BINARY_LENGTH", "NUMBER_COMPARISON", "STRING_FROM_SET", "STRING_LENGTH"],
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef(
    _ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef
):
    pass


_ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef = TypedDict(
    "_ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef",
    {
        "Name": str,
        "Type": Literal["STRING", "BINARY", "BOOLEAN", "NUMBER", "DATETIME", "VARIANT"],
        "DefaultValue": ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef],
        "RequiredBehavior": Literal["REQUIRED_ALWAYS", "NOT_REQUIRED"],
    },
    total=False,
)


class ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef(
    _ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef
):
    """
    - *(dict) --*

      A typed link attribute definition.
      - **Name** *(string) --*

        The unique name of the typed link attribute.
    """


_ListTypedLinkFacetAttributesPaginateResponseTypeDef = TypedDict(
    "_ListTypedLinkFacetAttributesPaginateResponseTypeDef",
    {"Attributes": List[ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef]},
    total=False,
)


class ListTypedLinkFacetAttributesPaginateResponseTypeDef(
    _ListTypedLinkFacetAttributesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Attributes** *(list) --*

        An ordered set of attributes associate with the typed link.
        - *(dict) --*

          A typed link attribute definition.
          - **Name** *(string) --*

            The unique name of the typed link attribute.
    """


_ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef(
    _ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTypedLinkFacetNamesPaginateResponseTypeDef = TypedDict(
    "_ListTypedLinkFacetNamesPaginateResponseTypeDef", {"FacetNames": List[str]}, total=False
)


class ListTypedLinkFacetNamesPaginateResponseTypeDef(
    _ListTypedLinkFacetNamesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **FacetNames** *(list) --*

        The names of typed link facets that exist within the schema.
        - *(string) --*
    """


_LookupPolicyPaginateObjectReferenceTypeDef = TypedDict(
    "_LookupPolicyPaginateObjectReferenceTypeDef", {"Selector": str}, total=False
)


class LookupPolicyPaginateObjectReferenceTypeDef(_LookupPolicyPaginateObjectReferenceTypeDef):
    """
    Reference that identifies the object whose policies will be looked up.
    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:
      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier
      * */some/path* - Identifies the object based on path
      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_LookupPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_LookupPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class LookupPolicyPaginatePaginationConfigTypeDef(_LookupPolicyPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef = TypedDict(
    "_LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef",
    {"PolicyId": str, "ObjectIdentifier": str, "PolicyType": str},
    total=False,
)


class LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef(
    _LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef
):
    pass


_LookupPolicyPaginateResponsePolicyToPathListTypeDef = TypedDict(
    "_LookupPolicyPaginateResponsePolicyToPathListTypeDef",
    {"Path": str, "Policies": List[LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef]},
    total=False,
)


class LookupPolicyPaginateResponsePolicyToPathListTypeDef(
    _LookupPolicyPaginateResponsePolicyToPathListTypeDef
):
    """
    - *(dict) --*

      Used when a regular object exists in a  Directory and you want to find all of the policies
      that are associated with that object and the parent to that object.
      - **Path** *(string) --*

        The path that is referenced from the root.
    """


_LookupPolicyPaginateResponseTypeDef = TypedDict(
    "_LookupPolicyPaginateResponseTypeDef",
    {"PolicyToPathList": List[LookupPolicyPaginateResponsePolicyToPathListTypeDef]},
    total=False,
)


class LookupPolicyPaginateResponseTypeDef(_LookupPolicyPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyToPathList** *(list) --*

        Provides list of path to policies. Policies contain ``PolicyId`` , ``ObjectIdentifier`` ,
        and ``PolicyType`` . For more information, see `Policies
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
        .
        - *(dict) --*

          Used when a regular object exists in a  Directory and you want to find all of the policies
          that are associated with that object and the parent to that object.
          - **Path** *(string) --*

            The path that is referenced from the root.
    """
