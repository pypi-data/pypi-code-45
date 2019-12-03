"Main interface for codecommit service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef",
    "ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsTypeDef",
    "ClientBatchDescribeMergeConflictsResponseerrorsTypeDef",
    "ClientBatchDescribeMergeConflictsResponseTypeDef",
    "ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseerrorsTypeDef",
    "ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseTypeDef",
    "ClientBatchGetCommitsResponsecommitsauthorTypeDef",
    "ClientBatchGetCommitsResponsecommitscommitterTypeDef",
    "ClientBatchGetCommitsResponsecommitsTypeDef",
    "ClientBatchGetCommitsResponseerrorsTypeDef",
    "ClientBatchGetCommitsResponseTypeDef",
    "ClientBatchGetRepositoriesResponserepositoriesTypeDef",
    "ClientBatchGetRepositoriesResponseTypeDef",
    "ClientCreateApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef",
    "ClientCreateApprovalRuleTemplateResponseTypeDef",
    "ClientCreateCommitDeleteFilesTypeDef",
    "ClientCreateCommitPutFilessourceFileTypeDef",
    "ClientCreateCommitPutFilesTypeDef",
    "ClientCreateCommitResponsefilesAddedTypeDef",
    "ClientCreateCommitResponsefilesDeletedTypeDef",
    "ClientCreateCommitResponsefilesUpdatedTypeDef",
    "ClientCreateCommitResponseTypeDef",
    "ClientCreateCommitSetFileModesTypeDef",
    "ClientCreatePullRequestApprovalRuleResponseapprovalRuleoriginApprovalRuleTemplateTypeDef",
    "ClientCreatePullRequestApprovalRuleResponseapprovalRuleTypeDef",
    "ClientCreatePullRequestApprovalRuleResponseTypeDef",
    "ClientCreatePullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientCreatePullRequestResponsepullRequestapprovalRulesTypeDef",
    "ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef",
    "ClientCreatePullRequestResponsepullRequestTypeDef",
    "ClientCreatePullRequestResponseTypeDef",
    "ClientCreatePullRequestTargetsTypeDef",
    "ClientCreateRepositoryResponserepositoryMetadataTypeDef",
    "ClientCreateRepositoryResponseTypeDef",
    "ClientCreateUnreferencedMergeCommitConflictResolutiondeleteFilesTypeDef",
    "ClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef",
    "ClientCreateUnreferencedMergeCommitConflictResolutionsetFileModesTypeDef",
    "ClientCreateUnreferencedMergeCommitConflictResolutionTypeDef",
    "ClientCreateUnreferencedMergeCommitResponseTypeDef",
    "ClientDeleteApprovalRuleTemplateResponseTypeDef",
    "ClientDeleteBranchResponsedeletedBranchTypeDef",
    "ClientDeleteBranchResponseTypeDef",
    "ClientDeleteCommentContentResponsecommentTypeDef",
    "ClientDeleteCommentContentResponseTypeDef",
    "ClientDeleteFileResponseTypeDef",
    "ClientDeletePullRequestApprovalRuleResponseTypeDef",
    "ClientDeleteRepositoryResponseTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadataTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunksTypeDef",
    "ClientDescribeMergeConflictsResponseTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef",
    "ClientDescribePullRequestEventsResponseTypeDef",
    "ClientEvaluatePullRequestApprovalRulesResponseevaluationTypeDef",
    "ClientEvaluatePullRequestApprovalRulesResponseTypeDef",
    "ClientGetApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef",
    "ClientGetApprovalRuleTemplateResponseTypeDef",
    "ClientGetBlobResponseTypeDef",
    "ClientGetBranchResponsebranchTypeDef",
    "ClientGetBranchResponseTypeDef",
    "ClientGetCommentResponsecommentTypeDef",
    "ClientGetCommentResponseTypeDef",
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef",
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef",
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef",
    "ClientGetCommentsForComparedCommitResponseTypeDef",
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef",
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef",
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef",
    "ClientGetCommentsForPullRequestResponseTypeDef",
    "ClientGetCommitResponsecommitauthorTypeDef",
    "ClientGetCommitResponsecommitcommitterTypeDef",
    "ClientGetCommitResponsecommitTypeDef",
    "ClientGetCommitResponseTypeDef",
    "ClientGetDifferencesResponsedifferencesafterBlobTypeDef",
    "ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef",
    "ClientGetDifferencesResponsedifferencesTypeDef",
    "ClientGetDifferencesResponseTypeDef",
    "ClientGetFileResponseTypeDef",
    "ClientGetFolderResponsefilesTypeDef",
    "ClientGetFolderResponsesubFoldersTypeDef",
    "ClientGetFolderResponsesubModulesTypeDef",
    "ClientGetFolderResponsesymbolicLinksTypeDef",
    "ClientGetFolderResponseTypeDef",
    "ClientGetMergeCommitResponseTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListTypeDef",
    "ClientGetMergeConflictsResponseTypeDef",
    "ClientGetMergeOptionsResponseTypeDef",
    "ClientGetPullRequestApprovalStatesResponseapprovalsTypeDef",
    "ClientGetPullRequestApprovalStatesResponseTypeDef",
    "ClientGetPullRequestOverrideStateResponseTypeDef",
    "ClientGetPullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientGetPullRequestResponsepullRequestapprovalRulesTypeDef",
    "ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef",
    "ClientGetPullRequestResponsepullRequestTypeDef",
    "ClientGetPullRequestResponseTypeDef",
    "ClientGetRepositoryResponserepositoryMetadataTypeDef",
    "ClientGetRepositoryResponseTypeDef",
    "ClientGetRepositoryTriggersResponsetriggersTypeDef",
    "ClientGetRepositoryTriggersResponseTypeDef",
    "ClientListApprovalRuleTemplatesResponseTypeDef",
    "ClientListAssociatedApprovalRuleTemplatesForRepositoryResponseTypeDef",
    "ClientListBranchesResponseTypeDef",
    "ClientListPullRequestsResponseTypeDef",
    "ClientListRepositoriesForApprovalRuleTemplateResponseTypeDef",
    "ClientListRepositoriesResponserepositoriesTypeDef",
    "ClientListRepositoriesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientMergeBranchesByFastForwardResponseTypeDef",
    "ClientMergeBranchesBySquashConflictResolutiondeleteFilesTypeDef",
    "ClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef",
    "ClientMergeBranchesBySquashConflictResolutionsetFileModesTypeDef",
    "ClientMergeBranchesBySquashConflictResolutionTypeDef",
    "ClientMergeBranchesBySquashResponseTypeDef",
    "ClientMergeBranchesByThreeWayConflictResolutiondeleteFilesTypeDef",
    "ClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef",
    "ClientMergeBranchesByThreeWayConflictResolutionsetFileModesTypeDef",
    "ClientMergeBranchesByThreeWayConflictResolutionTypeDef",
    "ClientMergeBranchesByThreeWayResponseTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestTypeDef",
    "ClientMergePullRequestByFastForwardResponseTypeDef",
    "ClientMergePullRequestBySquashConflictResolutiondeleteFilesTypeDef",
    "ClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef",
    "ClientMergePullRequestBySquashConflictResolutionsetFileModesTypeDef",
    "ClientMergePullRequestBySquashConflictResolutionTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestapprovalRulesTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestTypeDef",
    "ClientMergePullRequestBySquashResponseTypeDef",
    "ClientMergePullRequestByThreeWayConflictResolutiondeleteFilesTypeDef",
    "ClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef",
    "ClientMergePullRequestByThreeWayConflictResolutionsetFileModesTypeDef",
    "ClientMergePullRequestByThreeWayConflictResolutionTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestTypeDef",
    "ClientMergePullRequestByThreeWayResponseTypeDef",
    "ClientPostCommentForComparedCommitLocationTypeDef",
    "ClientPostCommentForComparedCommitResponsecommentTypeDef",
    "ClientPostCommentForComparedCommitResponselocationTypeDef",
    "ClientPostCommentForComparedCommitResponseTypeDef",
    "ClientPostCommentForPullRequestLocationTypeDef",
    "ClientPostCommentForPullRequestResponsecommentTypeDef",
    "ClientPostCommentForPullRequestResponselocationTypeDef",
    "ClientPostCommentForPullRequestResponseTypeDef",
    "ClientPostCommentReplyResponsecommentTypeDef",
    "ClientPostCommentReplyResponseTypeDef",
    "ClientPutFileResponseTypeDef",
    "ClientPutRepositoryTriggersResponseTypeDef",
    "ClientPutRepositoryTriggersTriggersTypeDef",
    "ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef",
    "ClientTestRepositoryTriggersResponseTypeDef",
    "ClientTestRepositoryTriggersTriggersTypeDef",
    "ClientUpdateApprovalRuleTemplateContentResponseapprovalRuleTemplateTypeDef",
    "ClientUpdateApprovalRuleTemplateContentResponseTypeDef",
    "ClientUpdateApprovalRuleTemplateDescriptionResponseapprovalRuleTemplateTypeDef",
    "ClientUpdateApprovalRuleTemplateDescriptionResponseTypeDef",
    "ClientUpdateApprovalRuleTemplateNameResponseapprovalRuleTemplateTypeDef",
    "ClientUpdateApprovalRuleTemplateNameResponseTypeDef",
    "ClientUpdateCommentResponsecommentTypeDef",
    "ClientUpdateCommentResponseTypeDef",
    "ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleoriginApprovalRuleTemplateTypeDef",
    "ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleTypeDef",
    "ClientUpdatePullRequestApprovalRuleContentResponseTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef",
    "ClientUpdatePullRequestDescriptionResponseTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestTypeDef",
    "ClientUpdatePullRequestStatusResponseTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestTypeDef",
    "ClientUpdatePullRequestTitleResponseTypeDef",
    "DescribePullRequestEventsPaginatePaginationConfigTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef",
    "DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef",
    "DescribePullRequestEventsPaginateResponseTypeDef",
    "GetCommentsForComparedCommitPaginatePaginationConfigTypeDef",
    "GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef",
    "GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef",
    "GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef",
    "GetCommentsForComparedCommitPaginateResponseTypeDef",
    "GetCommentsForPullRequestPaginatePaginationConfigTypeDef",
    "GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef",
    "GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef",
    "GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef",
    "GetCommentsForPullRequestPaginateResponseTypeDef",
    "GetDifferencesPaginatePaginationConfigTypeDef",
    "GetDifferencesPaginateResponsedifferencesafterBlobTypeDef",
    "GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef",
    "GetDifferencesPaginateResponsedifferencesTypeDef",
    "GetDifferencesPaginateResponseTypeDef",
    "ListBranchesPaginatePaginationConfigTypeDef",
    "ListBranchesPaginateResponseTypeDef",
    "ListPullRequestsPaginatePaginationConfigTypeDef",
    "ListPullRequestsPaginateResponseTypeDef",
    "ListRepositoriesPaginatePaginationConfigTypeDef",
    "ListRepositoriesPaginateResponserepositoriesTypeDef",
    "ListRepositoriesPaginateResponseTypeDef",
)


_ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef = TypedDict(
    "_ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef",
    {"repositoryName": str, "errorCode": str, "errorMessage": str},
    total=False,
)


class ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef(
    _ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef
):
    pass


_ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseTypeDef = TypedDict(
    "_ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseTypeDef",
    {
        "associatedRepositoryNames": List[str],
        "errors": List[
            ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef
        ],
    },
    total=False,
)


class ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseTypeDef(
    _ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseTypeDef
):
    """
    - *(dict) --*

      - **associatedRepositoryNames** *(list) --*

        A list of names of the repositories that have been associated with the template.
        - *(string) --*
    """


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef",
    {
        "source": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "destination": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "base": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef
):
    pass


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef",
    {"source": int, "destination": int, "base": int},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef
):
    pass


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef",
    {"source": bool, "destination": bool, "base": bool},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef
):
    pass


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef",
    {"source": Literal["A", "M", "D"], "destination": Literal["A", "M", "D"]},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef
):
    pass


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef",
    {
        "source": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "destination": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "base": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
    },
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef
):
    pass


_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef",
    {
        "filePath": str,
        "fileSizes": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef,
        "fileModes": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef,
        "objectTypes": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef,
        "numberOfConflicts": int,
        "isBinaryFile": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef,
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef,
    },
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef
):
    """
    - **conflictMetadata** *(dict) --*

      Metadata about a conflict in a merge operation.
      - **filePath** *(string) --*

        The path of the file that contains conflicts.
    """


_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef
):
    pass


_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef
):
    pass


_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef
):
    pass


_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef",
    {
        "isConflict": bool,
        "source": ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef,
        "destination": ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef,
        "base": ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef,
    },
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef
):
    pass


_ClientBatchDescribeMergeConflictsResponseconflictsTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseconflictsTypeDef",
    {
        "conflictMetadata": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef,
        "mergeHunks": List[ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef],
    },
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseconflictsTypeDef(
    _ClientBatchDescribeMergeConflictsResponseconflictsTypeDef
):
    """
    - *(dict) --*

      Information about conflicts in a merge operation.
      - **conflictMetadata** *(dict) --*

        Metadata about a conflict in a merge operation.
        - **filePath** *(string) --*

          The path of the file that contains conflicts.
    """


_ClientBatchDescribeMergeConflictsResponseerrorsTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseerrorsTypeDef",
    {"filePath": str, "exceptionName": str, "message": str},
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseerrorsTypeDef(
    _ClientBatchDescribeMergeConflictsResponseerrorsTypeDef
):
    pass


_ClientBatchDescribeMergeConflictsResponseTypeDef = TypedDict(
    "_ClientBatchDescribeMergeConflictsResponseTypeDef",
    {
        "conflicts": List[ClientBatchDescribeMergeConflictsResponseconflictsTypeDef],
        "nextToken": str,
        "errors": List[ClientBatchDescribeMergeConflictsResponseerrorsTypeDef],
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
    },
    total=False,
)


class ClientBatchDescribeMergeConflictsResponseTypeDef(
    _ClientBatchDescribeMergeConflictsResponseTypeDef
):
    """
    - *(dict) --*

      - **conflicts** *(list) --*

        A list of conflicts for each file, including the conflict metadata and the hunks of the
        differences between the files.
        - *(dict) --*

          Information about conflicts in a merge operation.
          - **conflictMetadata** *(dict) --*

            Metadata about a conflict in a merge operation.
            - **filePath** *(string) --*

              The path of the file that contains conflicts.
    """


_ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseerrorsTypeDef = TypedDict(
    "_ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseerrorsTypeDef",
    {"repositoryName": str, "errorCode": str, "errorMessage": str},
    total=False,
)


class ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseerrorsTypeDef(
    _ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseerrorsTypeDef
):
    pass


_ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseTypeDef = TypedDict(
    "_ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseTypeDef",
    {
        "disassociatedRepositoryNames": List[str],
        "errors": List[
            ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseerrorsTypeDef
        ],
    },
    total=False,
)


class ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseTypeDef(
    _ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseTypeDef
):
    """
    - *(dict) --*

      - **disassociatedRepositoryNames** *(list) --*

        A list of repository names that have had their association with the template removed.
        - *(string) --*
    """


_ClientBatchGetCommitsResponsecommitsauthorTypeDef = TypedDict(
    "_ClientBatchGetCommitsResponsecommitsauthorTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)


class ClientBatchGetCommitsResponsecommitsauthorTypeDef(
    _ClientBatchGetCommitsResponsecommitsauthorTypeDef
):
    pass


_ClientBatchGetCommitsResponsecommitscommitterTypeDef = TypedDict(
    "_ClientBatchGetCommitsResponsecommitscommitterTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)


class ClientBatchGetCommitsResponsecommitscommitterTypeDef(
    _ClientBatchGetCommitsResponsecommitscommitterTypeDef
):
    pass


_ClientBatchGetCommitsResponsecommitsTypeDef = TypedDict(
    "_ClientBatchGetCommitsResponsecommitsTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "parents": List[str],
        "message": str,
        "author": ClientBatchGetCommitsResponsecommitsauthorTypeDef,
        "committer": ClientBatchGetCommitsResponsecommitscommitterTypeDef,
        "additionalData": str,
    },
    total=False,
)


class ClientBatchGetCommitsResponsecommitsTypeDef(_ClientBatchGetCommitsResponsecommitsTypeDef):
    """
    - *(dict) --*

      Returns information about a specific commit.
      - **commitId** *(string) --*

        The full SHA ID of the specified commit.
    """


_ClientBatchGetCommitsResponseerrorsTypeDef = TypedDict(
    "_ClientBatchGetCommitsResponseerrorsTypeDef",
    {"commitId": str, "errorCode": str, "errorMessage": str},
    total=False,
)


class ClientBatchGetCommitsResponseerrorsTypeDef(_ClientBatchGetCommitsResponseerrorsTypeDef):
    pass


_ClientBatchGetCommitsResponseTypeDef = TypedDict(
    "_ClientBatchGetCommitsResponseTypeDef",
    {
        "commits": List[ClientBatchGetCommitsResponsecommitsTypeDef],
        "errors": List[ClientBatchGetCommitsResponseerrorsTypeDef],
    },
    total=False,
)


class ClientBatchGetCommitsResponseTypeDef(_ClientBatchGetCommitsResponseTypeDef):
    """
    - *(dict) --*

      - **commits** *(list) --*

        An array of commit data type objects, each of which contains information about a specified
        commit.
        - *(dict) --*

          Returns information about a specific commit.
          - **commitId** *(string) --*

            The full SHA ID of the specified commit.
    """


_ClientBatchGetRepositoriesResponserepositoriesTypeDef = TypedDict(
    "_ClientBatchGetRepositoriesResponserepositoriesTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)


class ClientBatchGetRepositoriesResponserepositoriesTypeDef(
    _ClientBatchGetRepositoriesResponserepositoriesTypeDef
):
    """
    - *(dict) --*

      Information about a repository.
      - **accountId** *(string) --*

        The ID of the AWS account associated with the repository.
    """


_ClientBatchGetRepositoriesResponseTypeDef = TypedDict(
    "_ClientBatchGetRepositoriesResponseTypeDef",
    {
        "repositories": List[ClientBatchGetRepositoriesResponserepositoriesTypeDef],
        "repositoriesNotFound": List[str],
    },
    total=False,
)


class ClientBatchGetRepositoriesResponseTypeDef(_ClientBatchGetRepositoriesResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a batch get repositories operation.
      - **repositories** *(list) --*

        A list of repositories returned by the batch get repositories operation.
        - *(dict) --*

          Information about a repository.
          - **accountId** *(string) --*

            The ID of the AWS account associated with the repository.
    """


_ClientCreateApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef = TypedDict(
    "_ClientCreateApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)


class ClientCreateApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef(
    _ClientCreateApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef
):
    """
    - **approvalRuleTemplate** *(dict) --*

      The content and structure of the created approval rule template.
      - **approvalRuleTemplateId** *(string) --*

        The system-generated ID of the approval rule template.
    """


_ClientCreateApprovalRuleTemplateResponseTypeDef = TypedDict(
    "_ClientCreateApprovalRuleTemplateResponseTypeDef",
    {"approvalRuleTemplate": ClientCreateApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef},
    total=False,
)


class ClientCreateApprovalRuleTemplateResponseTypeDef(
    _ClientCreateApprovalRuleTemplateResponseTypeDef
):
    """
    - *(dict) --*

      - **approvalRuleTemplate** *(dict) --*

        The content and structure of the created approval rule template.
        - **approvalRuleTemplateId** *(string) --*

          The system-generated ID of the approval rule template.
    """


_ClientCreateCommitDeleteFilesTypeDef = TypedDict(
    "_ClientCreateCommitDeleteFilesTypeDef", {"filePath": str}
)


class ClientCreateCommitDeleteFilesTypeDef(_ClientCreateCommitDeleteFilesTypeDef):
    """
    - *(dict) --*

      A file that is deleted as part of a commit.
      - **filePath** *(string) --***[REQUIRED]**

        The full path of the file to be deleted, including the name of the file.
    """


_ClientCreateCommitPutFilessourceFileTypeDef = TypedDict(
    "_ClientCreateCommitPutFilessourceFileTypeDef", {"filePath": str, "isMove": bool}, total=False
)


class ClientCreateCommitPutFilessourceFileTypeDef(_ClientCreateCommitPutFilessourceFileTypeDef):
    pass


_RequiredClientCreateCommitPutFilesTypeDef = TypedDict(
    "_RequiredClientCreateCommitPutFilesTypeDef", {"filePath": str}
)
_OptionalClientCreateCommitPutFilesTypeDef = TypedDict(
    "_OptionalClientCreateCommitPutFilesTypeDef",
    {
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "fileContent": bytes,
        "sourceFile": ClientCreateCommitPutFilessourceFileTypeDef,
    },
    total=False,
)


class ClientCreateCommitPutFilesTypeDef(
    _RequiredClientCreateCommitPutFilesTypeDef, _OptionalClientCreateCommitPutFilesTypeDef
):
    """
    - *(dict) --*

      Information about a file added or updated as part of a commit.
      - **filePath** *(string) --***[REQUIRED]**

        The full path to the file in the repository, including the name of the file.
    """


_ClientCreateCommitResponsefilesAddedTypeDef = TypedDict(
    "_ClientCreateCommitResponsefilesAddedTypeDef",
    {"absolutePath": str, "blobId": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ClientCreateCommitResponsefilesAddedTypeDef(_ClientCreateCommitResponsefilesAddedTypeDef):
    pass


_ClientCreateCommitResponsefilesDeletedTypeDef = TypedDict(
    "_ClientCreateCommitResponsefilesDeletedTypeDef",
    {"absolutePath": str, "blobId": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ClientCreateCommitResponsefilesDeletedTypeDef(_ClientCreateCommitResponsefilesDeletedTypeDef):
    pass


_ClientCreateCommitResponsefilesUpdatedTypeDef = TypedDict(
    "_ClientCreateCommitResponsefilesUpdatedTypeDef",
    {"absolutePath": str, "blobId": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ClientCreateCommitResponsefilesUpdatedTypeDef(_ClientCreateCommitResponsefilesUpdatedTypeDef):
    pass


_ClientCreateCommitResponseTypeDef = TypedDict(
    "_ClientCreateCommitResponseTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "filesAdded": List[ClientCreateCommitResponsefilesAddedTypeDef],
        "filesUpdated": List[ClientCreateCommitResponsefilesUpdatedTypeDef],
        "filesDeleted": List[ClientCreateCommitResponsefilesDeletedTypeDef],
    },
    total=False,
)


class ClientCreateCommitResponseTypeDef(_ClientCreateCommitResponseTypeDef):
    """
    - *(dict) --*

      - **commitId** *(string) --*

        The full commit ID of the commit that contains your committed file changes.
    """


_RequiredClientCreateCommitSetFileModesTypeDef = TypedDict(
    "_RequiredClientCreateCommitSetFileModesTypeDef", {"filePath": str}
)
_OptionalClientCreateCommitSetFileModesTypeDef = TypedDict(
    "_OptionalClientCreateCommitSetFileModesTypeDef",
    {"fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ClientCreateCommitSetFileModesTypeDef(
    _RequiredClientCreateCommitSetFileModesTypeDef, _OptionalClientCreateCommitSetFileModesTypeDef
):
    """
    - *(dict) --*

      Information about the file mode changes.
      - **filePath** *(string) --***[REQUIRED]**

        The full path to the file, including the name of the file.
    """


_ClientCreatePullRequestApprovalRuleResponseapprovalRuleoriginApprovalRuleTemplateTypeDef = TypedDict(
    "_ClientCreatePullRequestApprovalRuleResponseapprovalRuleoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)


class ClientCreatePullRequestApprovalRuleResponseapprovalRuleoriginApprovalRuleTemplateTypeDef(
    _ClientCreatePullRequestApprovalRuleResponseapprovalRuleoriginApprovalRuleTemplateTypeDef
):
    pass


_ClientCreatePullRequestApprovalRuleResponseapprovalRuleTypeDef = TypedDict(
    "_ClientCreatePullRequestApprovalRuleResponseapprovalRuleTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientCreatePullRequestApprovalRuleResponseapprovalRuleoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)


class ClientCreatePullRequestApprovalRuleResponseapprovalRuleTypeDef(
    _ClientCreatePullRequestApprovalRuleResponseapprovalRuleTypeDef
):
    """
    - **approvalRule** *(dict) --*

      Information about the created approval rule.
      - **approvalRuleId** *(string) --*

        The system-generated ID of the approval rule.
    """


_ClientCreatePullRequestApprovalRuleResponseTypeDef = TypedDict(
    "_ClientCreatePullRequestApprovalRuleResponseTypeDef",
    {"approvalRule": ClientCreatePullRequestApprovalRuleResponseapprovalRuleTypeDef},
    total=False,
)


class ClientCreatePullRequestApprovalRuleResponseTypeDef(
    _ClientCreatePullRequestApprovalRuleResponseTypeDef
):
    """
    - *(dict) --*

      - **approvalRule** *(dict) --*

        Information about the created approval rule.
        - **approvalRuleId** *(string) --*

          The system-generated ID of the approval rule.
    """


_ClientCreatePullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "_ClientCreatePullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)


class ClientCreatePullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef(
    _ClientCreatePullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef
):
    pass


_ClientCreatePullRequestResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "_ClientCreatePullRequestResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientCreatePullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)


class ClientCreatePullRequestResponsepullRequestapprovalRulesTypeDef(
    _ClientCreatePullRequestResponsepullRequestapprovalRulesTypeDef
):
    pass


_ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)


class ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    pass


_ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef(
    _ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef
):
    pass


_ClientCreatePullRequestResponsepullRequestTypeDef = TypedDict(
    "_ClientCreatePullRequestResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[ClientCreatePullRequestResponsepullRequestapprovalRulesTypeDef],
    },
    total=False,
)


class ClientCreatePullRequestResponsepullRequestTypeDef(
    _ClientCreatePullRequestResponsepullRequestTypeDef
):
    """
    - **pullRequest** *(dict) --*

      Information about the newly created pull request.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_ClientCreatePullRequestResponseTypeDef = TypedDict(
    "_ClientCreatePullRequestResponseTypeDef",
    {"pullRequest": ClientCreatePullRequestResponsepullRequestTypeDef},
    total=False,
)


class ClientCreatePullRequestResponseTypeDef(_ClientCreatePullRequestResponseTypeDef):
    """
    - *(dict) --*

      - **pullRequest** *(dict) --*

        Information about the newly created pull request.
        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.
    """


_RequiredClientCreatePullRequestTargetsTypeDef = TypedDict(
    "_RequiredClientCreatePullRequestTargetsTypeDef", {"repositoryName": str}
)
_OptionalClientCreatePullRequestTargetsTypeDef = TypedDict(
    "_OptionalClientCreatePullRequestTargetsTypeDef",
    {"sourceReference": str, "destinationReference": str},
    total=False,
)


class ClientCreatePullRequestTargetsTypeDef(
    _RequiredClientCreatePullRequestTargetsTypeDef, _OptionalClientCreatePullRequestTargetsTypeDef
):
    """
    - *(dict) --*

      Returns information about a target for a pull request.
      - **repositoryName** *(string) --***[REQUIRED]**

        The name of the repository that contains the pull request.
    """


_ClientCreateRepositoryResponserepositoryMetadataTypeDef = TypedDict(
    "_ClientCreateRepositoryResponserepositoryMetadataTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)


class ClientCreateRepositoryResponserepositoryMetadataTypeDef(
    _ClientCreateRepositoryResponserepositoryMetadataTypeDef
):
    """
    - **repositoryMetadata** *(dict) --*

      Information about the newly created repository.
      - **accountId** *(string) --*

        The ID of the AWS account associated with the repository.
    """


_ClientCreateRepositoryResponseTypeDef = TypedDict(
    "_ClientCreateRepositoryResponseTypeDef",
    {"repositoryMetadata": ClientCreateRepositoryResponserepositoryMetadataTypeDef},
    total=False,
)


class ClientCreateRepositoryResponseTypeDef(_ClientCreateRepositoryResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a create repository operation.
      - **repositoryMetadata** *(dict) --*

        Information about the newly created repository.
        - **accountId** *(string) --*

          The ID of the AWS account associated with the repository.
    """


_ClientCreateUnreferencedMergeCommitConflictResolutiondeleteFilesTypeDef = TypedDict(
    "_ClientCreateUnreferencedMergeCommitConflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
    total=False,
)


class ClientCreateUnreferencedMergeCommitConflictResolutiondeleteFilesTypeDef(
    _ClientCreateUnreferencedMergeCommitConflictResolutiondeleteFilesTypeDef
):
    pass


_RequiredClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef",
    {"filePath": str},
)
_OptionalClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef",
    {
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
        "content": bytes,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef(
    _RequiredClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef,
    _OptionalClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef,
):
    """
    - *(dict) --*

      Information about a replacement content entry in the conflict of a merge or pull request
      operation.
      - **filePath** *(string) --***[REQUIRED]**

        The path of the conflicting file.
    """


_ClientCreateUnreferencedMergeCommitConflictResolutionsetFileModesTypeDef = TypedDict(
    "_ClientCreateUnreferencedMergeCommitConflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ClientCreateUnreferencedMergeCommitConflictResolutionsetFileModesTypeDef(
    _ClientCreateUnreferencedMergeCommitConflictResolutionsetFileModesTypeDef
):
    pass


_ClientCreateUnreferencedMergeCommitConflictResolutionTypeDef = TypedDict(
    "_ClientCreateUnreferencedMergeCommitConflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[
            ClientCreateUnreferencedMergeCommitConflictResolutiondeleteFilesTypeDef
        ],
        "setFileModes": List[
            ClientCreateUnreferencedMergeCommitConflictResolutionsetFileModesTypeDef
        ],
    },
    total=False,
)


class ClientCreateUnreferencedMergeCommitConflictResolutionTypeDef(
    _ClientCreateUnreferencedMergeCommitConflictResolutionTypeDef
):
    """
    If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving
    conflicts during a merge.
    - **replaceContents** *(list) --*

      Files to have content replaced as part of the merge conflict resolution.
      - *(dict) --*

        Information about a replacement content entry in the conflict of a merge or pull request
        operation.
        - **filePath** *(string) --***[REQUIRED]**

          The path of the conflicting file.
    """


_ClientCreateUnreferencedMergeCommitResponseTypeDef = TypedDict(
    "_ClientCreateUnreferencedMergeCommitResponseTypeDef",
    {"commitId": str, "treeId": str},
    total=False,
)


class ClientCreateUnreferencedMergeCommitResponseTypeDef(
    _ClientCreateUnreferencedMergeCommitResponseTypeDef
):
    """
    - *(dict) --*

      - **commitId** *(string) --*

        The full commit ID of the commit that contains your merge results.
    """


_ClientDeleteApprovalRuleTemplateResponseTypeDef = TypedDict(
    "_ClientDeleteApprovalRuleTemplateResponseTypeDef", {"approvalRuleTemplateId": str}, total=False
)


class ClientDeleteApprovalRuleTemplateResponseTypeDef(
    _ClientDeleteApprovalRuleTemplateResponseTypeDef
):
    """
    - *(dict) --*

      - **approvalRuleTemplateId** *(string) --*

        The system-generated ID of the deleted approval rule template. If the template has been
        previously deleted, the only response is a 200 OK.
    """


_ClientDeleteBranchResponsedeletedBranchTypeDef = TypedDict(
    "_ClientDeleteBranchResponsedeletedBranchTypeDef",
    {"branchName": str, "commitId": str},
    total=False,
)


class ClientDeleteBranchResponsedeletedBranchTypeDef(
    _ClientDeleteBranchResponsedeletedBranchTypeDef
):
    """
    - **deletedBranch** *(dict) --*

      Information about the branch deleted by the operation, including the branch name and the
      commit ID that was the tip of the branch.
      - **branchName** *(string) --*

        The name of the branch.
    """


_ClientDeleteBranchResponseTypeDef = TypedDict(
    "_ClientDeleteBranchResponseTypeDef",
    {"deletedBranch": ClientDeleteBranchResponsedeletedBranchTypeDef},
    total=False,
)


class ClientDeleteBranchResponseTypeDef(_ClientDeleteBranchResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a delete branch operation.
      - **deletedBranch** *(dict) --*

        Information about the branch deleted by the operation, including the branch name and the
        commit ID that was the tip of the branch.
        - **branchName** *(string) --*

          The name of the branch.
    """


_ClientDeleteCommentContentResponsecommentTypeDef = TypedDict(
    "_ClientDeleteCommentContentResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientDeleteCommentContentResponsecommentTypeDef(
    _ClientDeleteCommentContentResponsecommentTypeDef
):
    """
    - **comment** *(dict) --*

      Information about the comment you just deleted.
      - **commentId** *(string) --*

        The system-generated comment ID.
    """


_ClientDeleteCommentContentResponseTypeDef = TypedDict(
    "_ClientDeleteCommentContentResponseTypeDef",
    {"comment": ClientDeleteCommentContentResponsecommentTypeDef},
    total=False,
)


class ClientDeleteCommentContentResponseTypeDef(_ClientDeleteCommentContentResponseTypeDef):
    """
    - *(dict) --*

      - **comment** *(dict) --*

        Information about the comment you just deleted.
        - **commentId** *(string) --*

          The system-generated comment ID.
    """


_ClientDeleteFileResponseTypeDef = TypedDict(
    "_ClientDeleteFileResponseTypeDef",
    {"commitId": str, "blobId": str, "treeId": str, "filePath": str},
    total=False,
)


class ClientDeleteFileResponseTypeDef(_ClientDeleteFileResponseTypeDef):
    """
    - *(dict) --*

      - **commitId** *(string) --*

        The full commit ID of the commit that contains the change that deletes the file.
    """


_ClientDeletePullRequestApprovalRuleResponseTypeDef = TypedDict(
    "_ClientDeletePullRequestApprovalRuleResponseTypeDef", {"approvalRuleId": str}, total=False
)


class ClientDeletePullRequestApprovalRuleResponseTypeDef(
    _ClientDeletePullRequestApprovalRuleResponseTypeDef
):
    """
    - *(dict) --*

      - **approvalRuleId** *(string) --*

        The ID of the deleted approval rule.
        .. note::

          If the approval rule was deleted in an earlier API call, the response is 200 OK without
          content.
    """


_ClientDeleteRepositoryResponseTypeDef = TypedDict(
    "_ClientDeleteRepositoryResponseTypeDef", {"repositoryId": str}, total=False
)


class ClientDeleteRepositoryResponseTypeDef(_ClientDeleteRepositoryResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a delete repository operation.
      - **repositoryId** *(string) --*

        The ID of the repository that was deleted.
    """


_ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef",
    {
        "source": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "destination": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "base": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef
):
    pass


_ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef",
    {"source": int, "destination": int, "base": int},
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef
):
    pass


_ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef",
    {"source": bool, "destination": bool, "base": bool},
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef
):
    pass


_ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef",
    {"source": Literal["A", "M", "D"], "destination": Literal["A", "M", "D"]},
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef
):
    pass


_ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef",
    {
        "source": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "destination": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "base": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
    },
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef
):
    pass


_ClientDescribeMergeConflictsResponseconflictMetadataTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseconflictMetadataTypeDef",
    {
        "filePath": str,
        "fileSizes": ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef,
        "fileModes": ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef,
        "objectTypes": ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef,
        "numberOfConflicts": int,
        "isBinaryFile": ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef,
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef,
    },
    total=False,
)


class ClientDescribeMergeConflictsResponseconflictMetadataTypeDef(
    _ClientDescribeMergeConflictsResponseconflictMetadataTypeDef
):
    """
    - **conflictMetadata** *(dict) --*

      Contains metadata about the conflicts found in the merge.
      - **filePath** *(string) --*

        The path of the file that contains conflicts.
    """


_ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef(
    _ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef
):
    pass


_ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef(
    _ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef
):
    pass


_ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)


class ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef(
    _ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef
):
    pass


_ClientDescribeMergeConflictsResponsemergeHunksTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponsemergeHunksTypeDef",
    {
        "isConflict": bool,
        "source": ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef,
        "destination": ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef,
        "base": ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef,
    },
    total=False,
)


class ClientDescribeMergeConflictsResponsemergeHunksTypeDef(
    _ClientDescribeMergeConflictsResponsemergeHunksTypeDef
):
    pass


_ClientDescribeMergeConflictsResponseTypeDef = TypedDict(
    "_ClientDescribeMergeConflictsResponseTypeDef",
    {
        "conflictMetadata": ClientDescribeMergeConflictsResponseconflictMetadataTypeDef,
        "mergeHunks": List[ClientDescribeMergeConflictsResponsemergeHunksTypeDef],
        "nextToken": str,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
    },
    total=False,
)


class ClientDescribeMergeConflictsResponseTypeDef(_ClientDescribeMergeConflictsResponseTypeDef):
    """
    - *(dict) --*

      - **conflictMetadata** *(dict) --*

        Contains metadata about the conflicts found in the merge.
        - **filePath** *(string) --*

          The path of the file that contains conflicts.
    """


_ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleEventMetadataTypeDef",
    {"approvalRuleName": str, "approvalRuleId": str, "approvalRuleContent": str},
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleEventMetadataTypeDef
):
    pass


_ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef",
    {"revisionId": str, "overrideStatus": Literal["OVERRIDE", "REVOKE"]},
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef
):
    pass


_ClientDescribePullRequestEventsResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef",
    {"revisionId": str, "approvalStatus": Literal["APPROVE", "REVOKE"]},
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef
):
    pass


_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef",
    {"repositoryName": str, "sourceCommitId": str, "destinationCommitId": str, "mergeBase": str},
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef
):
    pass


_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef
):
    pass


_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "destinationReference": str,
        "mergeMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef,
    },
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef
):
    pass


_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {"repositoryName": str, "beforeCommitId": str, "afterCommitId": str, "mergeBase": str},
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef
):
    pass


_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef",
    {"pullRequestStatus": Literal["OPEN", "CLOSED"]},
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef
):
    pass


_ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef",
    {
        "pullRequestId": str,
        "eventDate": datetime,
        "pullRequestEventType": Literal[
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_STATUS_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
        ],
        "actorArn": str,
        "pullRequestCreatedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef,
        "pullRequestStatusChangedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef,
        "pullRequestSourceReferenceUpdatedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef,
        "pullRequestMergedStateChangedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef,
        "approvalRuleEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleEventMetadataTypeDef,
        "approvalStateChangedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef,
        "approvalRuleOverriddenEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef,
    },
    total=False,
)


class ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef(
    _ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef
):
    """
    - *(dict) --*

      Returns information about a pull request event.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_ClientDescribePullRequestEventsResponseTypeDef = TypedDict(
    "_ClientDescribePullRequestEventsResponseTypeDef",
    {
        "pullRequestEvents": List[ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribePullRequestEventsResponseTypeDef(
    _ClientDescribePullRequestEventsResponseTypeDef
):
    """
    - *(dict) --*

      - **pullRequestEvents** *(list) --*

        Information about the pull request events.
        - *(dict) --*

          Returns information about a pull request event.
          - **pullRequestId** *(string) --*

            The system-generated ID of the pull request.
    """


_ClientEvaluatePullRequestApprovalRulesResponseevaluationTypeDef = TypedDict(
    "_ClientEvaluatePullRequestApprovalRulesResponseevaluationTypeDef",
    {
        "approved": bool,
        "overridden": bool,
        "approvalRulesSatisfied": List[str],
        "approvalRulesNotSatisfied": List[str],
    },
    total=False,
)


class ClientEvaluatePullRequestApprovalRulesResponseevaluationTypeDef(
    _ClientEvaluatePullRequestApprovalRulesResponseevaluationTypeDef
):
    """
    - **evaluation** *(dict) --*

      The result of the evaluation, including the names of the rules whose conditions have been met
      (if any), the names of the rules whose conditions have not been met (if any), whether the pull
      request is in the approved state, and whether the pull request approval rule has been set
      aside by an override.
      - **approved** *(boolean) --*

        Whether the state of the pull request is approved.
    """


_ClientEvaluatePullRequestApprovalRulesResponseTypeDef = TypedDict(
    "_ClientEvaluatePullRequestApprovalRulesResponseTypeDef",
    {"evaluation": ClientEvaluatePullRequestApprovalRulesResponseevaluationTypeDef},
    total=False,
)


class ClientEvaluatePullRequestApprovalRulesResponseTypeDef(
    _ClientEvaluatePullRequestApprovalRulesResponseTypeDef
):
    """
    - *(dict) --*

      - **evaluation** *(dict) --*

        The result of the evaluation, including the names of the rules whose conditions have been
        met (if any), the names of the rules whose conditions have not been met (if any), whether
        the pull request is in the approved state, and whether the pull request approval rule has
        been set aside by an override.
        - **approved** *(boolean) --*

          Whether the state of the pull request is approved.
    """


_ClientGetApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef = TypedDict(
    "_ClientGetApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)


class ClientGetApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef(
    _ClientGetApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef
):
    """
    - **approvalRuleTemplate** *(dict) --*

      The content and structure of the approval rule template.
      - **approvalRuleTemplateId** *(string) --*

        The system-generated ID of the approval rule template.
    """


_ClientGetApprovalRuleTemplateResponseTypeDef = TypedDict(
    "_ClientGetApprovalRuleTemplateResponseTypeDef",
    {"approvalRuleTemplate": ClientGetApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef},
    total=False,
)


class ClientGetApprovalRuleTemplateResponseTypeDef(_ClientGetApprovalRuleTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **approvalRuleTemplate** *(dict) --*

        The content and structure of the approval rule template.
        - **approvalRuleTemplateId** *(string) --*

          The system-generated ID of the approval rule template.
    """


_ClientGetBlobResponseTypeDef = TypedDict(
    "_ClientGetBlobResponseTypeDef", {"content": bytes}, total=False
)


class ClientGetBlobResponseTypeDef(_ClientGetBlobResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a get blob operation.
      - **content** *(bytes) --*

        The content of the blob, usually a file.
    """


_ClientGetBranchResponsebranchTypeDef = TypedDict(
    "_ClientGetBranchResponsebranchTypeDef", {"branchName": str, "commitId": str}, total=False
)


class ClientGetBranchResponsebranchTypeDef(_ClientGetBranchResponsebranchTypeDef):
    """
    - **branch** *(dict) --*

      The name of the branch.
      - **branchName** *(string) --*

        The name of the branch.
    """


_ClientGetBranchResponseTypeDef = TypedDict(
    "_ClientGetBranchResponseTypeDef", {"branch": ClientGetBranchResponsebranchTypeDef}, total=False
)


class ClientGetBranchResponseTypeDef(_ClientGetBranchResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a get branch operation.
      - **branch** *(dict) --*

        The name of the branch.
        - **branchName** *(string) --*

          The name of the branch.
    """


_ClientGetCommentResponsecommentTypeDef = TypedDict(
    "_ClientGetCommentResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientGetCommentResponsecommentTypeDef(_ClientGetCommentResponsecommentTypeDef):
    """
    - **comment** *(dict) --*

      The contents of the comment.
      - **commentId** *(string) --*

        The system-generated comment ID.
    """


_ClientGetCommentResponseTypeDef = TypedDict(
    "_ClientGetCommentResponseTypeDef",
    {"comment": ClientGetCommentResponsecommentTypeDef},
    total=False,
)


class ClientGetCommentResponseTypeDef(_ClientGetCommentResponseTypeDef):
    """
    - *(dict) --*

      - **comment** *(dict) --*

        The contents of the comment.
        - **commentId** *(string) --*

          The system-generated comment ID.
    """


_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef = TypedDict(
    "_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef(
    _ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef
):
    pass


_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef = TypedDict(
    "_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)


class ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef(
    _ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef
):
    pass


_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef = TypedDict(
    "_ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef,
        "comments": List[
            ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef
        ],
    },
    total=False,
)


class ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef(
    _ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef
):
    """
    - *(dict) --*

      Returns information about comments on the comparison between two commits.
      - **repositoryName** *(string) --*

        The name of the repository that contains the compared commits.
    """


_ClientGetCommentsForComparedCommitResponseTypeDef = TypedDict(
    "_ClientGetCommentsForComparedCommitResponseTypeDef",
    {
        "commentsForComparedCommitData": List[
            ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetCommentsForComparedCommitResponseTypeDef(
    _ClientGetCommentsForComparedCommitResponseTypeDef
):
    """
    - *(dict) --*

      - **commentsForComparedCommitData** *(list) --*

        A list of comment objects on the compared commit.
        - *(dict) --*

          Returns information about comments on the comparison between two commits.
          - **repositoryName** *(string) --*

            The name of the repository that contains the compared commits.
    """


_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef = TypedDict(
    "_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef(
    _ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef
):
    pass


_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef = TypedDict(
    "_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)


class ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef(
    _ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef
):
    pass


_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef = TypedDict(
    "_ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef,
        "comments": List[
            ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef
        ],
    },
    total=False,
)


class ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef(
    _ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef
):
    """
    - *(dict) --*

      Returns information about comments on a pull request.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_ClientGetCommentsForPullRequestResponseTypeDef = TypedDict(
    "_ClientGetCommentsForPullRequestResponseTypeDef",
    {
        "commentsForPullRequestData": List[
            ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientGetCommentsForPullRequestResponseTypeDef(
    _ClientGetCommentsForPullRequestResponseTypeDef
):
    """
    - *(dict) --*

      - **commentsForPullRequestData** *(list) --*

        An array of comment objects on the pull request.
        - *(dict) --*

          Returns information about comments on a pull request.
          - **pullRequestId** *(string) --*

            The system-generated ID of the pull request.
    """


_ClientGetCommitResponsecommitauthorTypeDef = TypedDict(
    "_ClientGetCommitResponsecommitauthorTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)


class ClientGetCommitResponsecommitauthorTypeDef(_ClientGetCommitResponsecommitauthorTypeDef):
    pass


_ClientGetCommitResponsecommitcommitterTypeDef = TypedDict(
    "_ClientGetCommitResponsecommitcommitterTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)


class ClientGetCommitResponsecommitcommitterTypeDef(_ClientGetCommitResponsecommitcommitterTypeDef):
    pass


_ClientGetCommitResponsecommitTypeDef = TypedDict(
    "_ClientGetCommitResponsecommitTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "parents": List[str],
        "message": str,
        "author": ClientGetCommitResponsecommitauthorTypeDef,
        "committer": ClientGetCommitResponsecommitcommitterTypeDef,
        "additionalData": str,
    },
    total=False,
)


class ClientGetCommitResponsecommitTypeDef(_ClientGetCommitResponsecommitTypeDef):
    """
    - **commit** *(dict) --*

      A commit data type object that contains information about the specified commit.
      - **commitId** *(string) --*

        The full SHA ID of the specified commit.
    """


_ClientGetCommitResponseTypeDef = TypedDict(
    "_ClientGetCommitResponseTypeDef", {"commit": ClientGetCommitResponsecommitTypeDef}, total=False
)


class ClientGetCommitResponseTypeDef(_ClientGetCommitResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a get commit operation.
      - **commit** *(dict) --*

        A commit data type object that contains information about the specified commit.
        - **commitId** *(string) --*

          The full SHA ID of the specified commit.
    """


_ClientGetDifferencesResponsedifferencesafterBlobTypeDef = TypedDict(
    "_ClientGetDifferencesResponsedifferencesafterBlobTypeDef",
    {"blobId": str, "path": str, "mode": str},
    total=False,
)


class ClientGetDifferencesResponsedifferencesafterBlobTypeDef(
    _ClientGetDifferencesResponsedifferencesafterBlobTypeDef
):
    pass


_ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef = TypedDict(
    "_ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef",
    {"blobId": str, "path": str, "mode": str},
    total=False,
)


class ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef(
    _ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef
):
    """
    - **beforeBlob** *(dict) --*

      Information about a ``beforeBlob`` data type object, including the ID, the file mode
      permission code, and the path.
      - **blobId** *(string) --*

        The full ID of the blob.
    """


_ClientGetDifferencesResponsedifferencesTypeDef = TypedDict(
    "_ClientGetDifferencesResponsedifferencesTypeDef",
    {
        "beforeBlob": ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef,
        "afterBlob": ClientGetDifferencesResponsedifferencesafterBlobTypeDef,
        "changeType": Literal["A", "M", "D"],
    },
    total=False,
)


class ClientGetDifferencesResponsedifferencesTypeDef(
    _ClientGetDifferencesResponsedifferencesTypeDef
):
    """
    - *(dict) --*

      Returns information about a set of differences for a commit specifier.
      - **beforeBlob** *(dict) --*

        Information about a ``beforeBlob`` data type object, including the ID, the file mode
        permission code, and the path.
        - **blobId** *(string) --*

          The full ID of the blob.
    """


_ClientGetDifferencesResponseTypeDef = TypedDict(
    "_ClientGetDifferencesResponseTypeDef",
    {"differences": List[ClientGetDifferencesResponsedifferencesTypeDef], "NextToken": str},
    total=False,
)


class ClientGetDifferencesResponseTypeDef(_ClientGetDifferencesResponseTypeDef):
    """
    - *(dict) --*

      - **differences** *(list) --*

        A data type object that contains information about the differences, including whether the
        difference is added, modified, or deleted (A, D, M).
        - *(dict) --*

          Returns information about a set of differences for a commit specifier.
          - **beforeBlob** *(dict) --*

            Information about a ``beforeBlob`` data type object, including the ID, the file mode
            permission code, and the path.
            - **blobId** *(string) --*

              The full ID of the blob.
    """


_ClientGetFileResponseTypeDef = TypedDict(
    "_ClientGetFileResponseTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "filePath": str,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "fileSize": int,
        "fileContent": bytes,
    },
    total=False,
)


class ClientGetFileResponseTypeDef(_ClientGetFileResponseTypeDef):
    """
    - *(dict) --*

      - **commitId** *(string) --*

        The full commit ID of the commit that contains the content returned by GetFile.
    """


_ClientGetFolderResponsefilesTypeDef = TypedDict(
    "_ClientGetFolderResponsefilesTypeDef",
    {
        "blobId": str,
        "absolutePath": str,
        "relativePath": str,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientGetFolderResponsefilesTypeDef(_ClientGetFolderResponsefilesTypeDef):
    pass


_ClientGetFolderResponsesubFoldersTypeDef = TypedDict(
    "_ClientGetFolderResponsesubFoldersTypeDef",
    {"treeId": str, "absolutePath": str, "relativePath": str},
    total=False,
)


class ClientGetFolderResponsesubFoldersTypeDef(_ClientGetFolderResponsesubFoldersTypeDef):
    pass


_ClientGetFolderResponsesubModulesTypeDef = TypedDict(
    "_ClientGetFolderResponsesubModulesTypeDef",
    {"commitId": str, "absolutePath": str, "relativePath": str},
    total=False,
)


class ClientGetFolderResponsesubModulesTypeDef(_ClientGetFolderResponsesubModulesTypeDef):
    pass


_ClientGetFolderResponsesymbolicLinksTypeDef = TypedDict(
    "_ClientGetFolderResponsesymbolicLinksTypeDef",
    {
        "blobId": str,
        "absolutePath": str,
        "relativePath": str,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientGetFolderResponsesymbolicLinksTypeDef(_ClientGetFolderResponsesymbolicLinksTypeDef):
    pass


_ClientGetFolderResponseTypeDef = TypedDict(
    "_ClientGetFolderResponseTypeDef",
    {
        "commitId": str,
        "folderPath": str,
        "treeId": str,
        "subFolders": List[ClientGetFolderResponsesubFoldersTypeDef],
        "files": List[ClientGetFolderResponsefilesTypeDef],
        "symbolicLinks": List[ClientGetFolderResponsesymbolicLinksTypeDef],
        "subModules": List[ClientGetFolderResponsesubModulesTypeDef],
    },
    total=False,
)


class ClientGetFolderResponseTypeDef(_ClientGetFolderResponseTypeDef):
    """
    - *(dict) --*

      - **commitId** *(string) --*

        The full commit ID used as a reference for the returned version of the folder content.
    """


_ClientGetMergeCommitResponseTypeDef = TypedDict(
    "_ClientGetMergeCommitResponseTypeDef",
    {"sourceCommitId": str, "destinationCommitId": str, "baseCommitId": str, "mergedCommitId": str},
    total=False,
)


class ClientGetMergeCommitResponseTypeDef(_ClientGetMergeCommitResponseTypeDef):
    """
    - *(dict) --*

      - **sourceCommitId** *(string) --*

        The commit ID of the source commit specifier that was used in the merge evaluation.
    """


_ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef",
    {
        "source": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "destination": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "base": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef
):
    pass


_ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef",
    {"source": int, "destination": int, "base": int},
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef
):
    pass


_ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef",
    {"source": bool, "destination": bool, "base": bool},
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef
):
    pass


_ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef",
    {"source": Literal["A", "M", "D"], "destination": Literal["A", "M", "D"]},
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef
):
    pass


_ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef",
    {
        "source": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "destination": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "base": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
    },
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef
):
    pass


_ClientGetMergeConflictsResponseconflictMetadataListTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseconflictMetadataListTypeDef",
    {
        "filePath": str,
        "fileSizes": ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef,
        "fileModes": ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef,
        "objectTypes": ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef,
        "numberOfConflicts": int,
        "isBinaryFile": ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef,
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef,
    },
    total=False,
)


class ClientGetMergeConflictsResponseconflictMetadataListTypeDef(
    _ClientGetMergeConflictsResponseconflictMetadataListTypeDef
):
    pass


_ClientGetMergeConflictsResponseTypeDef = TypedDict(
    "_ClientGetMergeConflictsResponseTypeDef",
    {
        "mergeable": bool,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "conflictMetadataList": List[ClientGetMergeConflictsResponseconflictMetadataListTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetMergeConflictsResponseTypeDef(_ClientGetMergeConflictsResponseTypeDef):
    """
    - *(dict) --*

      - **mergeable** *(boolean) --*

        A Boolean value that indicates whether the code is mergeable by the specified merge option.
    """


_ClientGetMergeOptionsResponseTypeDef = TypedDict(
    "_ClientGetMergeOptionsResponseTypeDef",
    {
        "mergeOptions": List[Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"]],
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
    },
    total=False,
)


class ClientGetMergeOptionsResponseTypeDef(_ClientGetMergeOptionsResponseTypeDef):
    """
    - *(dict) --*

      - **mergeOptions** *(list) --*

        The merge option or strategy used to merge the code.
        - *(string) --*
    """


_ClientGetPullRequestApprovalStatesResponseapprovalsTypeDef = TypedDict(
    "_ClientGetPullRequestApprovalStatesResponseapprovalsTypeDef",
    {"userArn": str, "approvalState": Literal["APPROVE", "REVOKE"]},
    total=False,
)


class ClientGetPullRequestApprovalStatesResponseapprovalsTypeDef(
    _ClientGetPullRequestApprovalStatesResponseapprovalsTypeDef
):
    """
    - *(dict) --*

      Returns information about a specific approval on a pull request.
      - **userArn** *(string) --*

        The Amazon Resource Name (ARN) of the user.
    """


_ClientGetPullRequestApprovalStatesResponseTypeDef = TypedDict(
    "_ClientGetPullRequestApprovalStatesResponseTypeDef",
    {"approvals": List[ClientGetPullRequestApprovalStatesResponseapprovalsTypeDef]},
    total=False,
)


class ClientGetPullRequestApprovalStatesResponseTypeDef(
    _ClientGetPullRequestApprovalStatesResponseTypeDef
):
    """
    - *(dict) --*

      - **approvals** *(list) --*

        Information about users who have approved the pull request.
        - *(dict) --*

          Returns information about a specific approval on a pull request.
          - **userArn** *(string) --*

            The Amazon Resource Name (ARN) of the user.
    """


_ClientGetPullRequestOverrideStateResponseTypeDef = TypedDict(
    "_ClientGetPullRequestOverrideStateResponseTypeDef",
    {"overridden": bool, "overrider": str},
    total=False,
)


class ClientGetPullRequestOverrideStateResponseTypeDef(
    _ClientGetPullRequestOverrideStateResponseTypeDef
):
    """
    - *(dict) --*

      - **overridden** *(boolean) --*

        A Boolean value that indicates whether a pull request has had its rules set aside (TRUE) or
        whether all approval rules still apply (FALSE).
    """


_ClientGetPullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "_ClientGetPullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)


class ClientGetPullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef(
    _ClientGetPullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef
):
    pass


_ClientGetPullRequestResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "_ClientGetPullRequestResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientGetPullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)


class ClientGetPullRequestResponsepullRequestapprovalRulesTypeDef(
    _ClientGetPullRequestResponsepullRequestapprovalRulesTypeDef
):
    pass


_ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)


class ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    pass


_ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef(
    _ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef
):
    pass


_ClientGetPullRequestResponsepullRequestTypeDef = TypedDict(
    "_ClientGetPullRequestResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[ClientGetPullRequestResponsepullRequestapprovalRulesTypeDef],
    },
    total=False,
)


class ClientGetPullRequestResponsepullRequestTypeDef(
    _ClientGetPullRequestResponsepullRequestTypeDef
):
    """
    - **pullRequest** *(dict) --*

      Information about the specified pull request.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_ClientGetPullRequestResponseTypeDef = TypedDict(
    "_ClientGetPullRequestResponseTypeDef",
    {"pullRequest": ClientGetPullRequestResponsepullRequestTypeDef},
    total=False,
)


class ClientGetPullRequestResponseTypeDef(_ClientGetPullRequestResponseTypeDef):
    """
    - *(dict) --*

      - **pullRequest** *(dict) --*

        Information about the specified pull request.
        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.
    """


_ClientGetRepositoryResponserepositoryMetadataTypeDef = TypedDict(
    "_ClientGetRepositoryResponserepositoryMetadataTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)


class ClientGetRepositoryResponserepositoryMetadataTypeDef(
    _ClientGetRepositoryResponserepositoryMetadataTypeDef
):
    """
    - **repositoryMetadata** *(dict) --*

      Information about the repository.
      - **accountId** *(string) --*

        The ID of the AWS account associated with the repository.
    """


_ClientGetRepositoryResponseTypeDef = TypedDict(
    "_ClientGetRepositoryResponseTypeDef",
    {"repositoryMetadata": ClientGetRepositoryResponserepositoryMetadataTypeDef},
    total=False,
)


class ClientGetRepositoryResponseTypeDef(_ClientGetRepositoryResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a get repository operation.
      - **repositoryMetadata** *(dict) --*

        Information about the repository.
        - **accountId** *(string) --*

          The ID of the AWS account associated with the repository.
    """


_ClientGetRepositoryTriggersResponsetriggersTypeDef = TypedDict(
    "_ClientGetRepositoryTriggersResponsetriggersTypeDef",
    {
        "name": str,
        "destinationArn": str,
        "customData": str,
        "branches": List[str],
        "events": List[Literal["all", "updateReference", "createReference", "deleteReference"]],
    },
    total=False,
)


class ClientGetRepositoryTriggersResponsetriggersTypeDef(
    _ClientGetRepositoryTriggersResponsetriggersTypeDef
):
    pass


_ClientGetRepositoryTriggersResponseTypeDef = TypedDict(
    "_ClientGetRepositoryTriggersResponseTypeDef",
    {"configurationId": str, "triggers": List[ClientGetRepositoryTriggersResponsetriggersTypeDef]},
    total=False,
)


class ClientGetRepositoryTriggersResponseTypeDef(_ClientGetRepositoryTriggersResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a get repository triggers operation.
      - **configurationId** *(string) --*

        The system-generated unique ID for the trigger.
    """


_ClientListApprovalRuleTemplatesResponseTypeDef = TypedDict(
    "_ClientListApprovalRuleTemplatesResponseTypeDef",
    {"approvalRuleTemplateNames": List[str], "nextToken": str},
    total=False,
)


class ClientListApprovalRuleTemplatesResponseTypeDef(
    _ClientListApprovalRuleTemplatesResponseTypeDef
):
    """
    - *(dict) --*

      - **approvalRuleTemplateNames** *(list) --*

        The names of all the approval rule templates found in the AWS Region for your AWS account.
        - *(string) --*
    """


_ClientListAssociatedApprovalRuleTemplatesForRepositoryResponseTypeDef = TypedDict(
    "_ClientListAssociatedApprovalRuleTemplatesForRepositoryResponseTypeDef",
    {"approvalRuleTemplateNames": List[str], "nextToken": str},
    total=False,
)


class ClientListAssociatedApprovalRuleTemplatesForRepositoryResponseTypeDef(
    _ClientListAssociatedApprovalRuleTemplatesForRepositoryResponseTypeDef
):
    """
    - *(dict) --*

      - **approvalRuleTemplateNames** *(list) --*

        The names of all approval rule templates associated with the repository.
        - *(string) --*
    """


_ClientListBranchesResponseTypeDef = TypedDict(
    "_ClientListBranchesResponseTypeDef", {"branches": List[str], "nextToken": str}, total=False
)


class ClientListBranchesResponseTypeDef(_ClientListBranchesResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a list branches operation.
      - **branches** *(list) --*

        The list of branch names.
        - *(string) --*
    """


_ClientListPullRequestsResponseTypeDef = TypedDict(
    "_ClientListPullRequestsResponseTypeDef",
    {"pullRequestIds": List[str], "nextToken": str},
    total=False,
)


class ClientListPullRequestsResponseTypeDef(_ClientListPullRequestsResponseTypeDef):
    """
    - *(dict) --*

      - **pullRequestIds** *(list) --*

        The system-generated IDs of the pull requests.
        - *(string) --*
    """


_ClientListRepositoriesForApprovalRuleTemplateResponseTypeDef = TypedDict(
    "_ClientListRepositoriesForApprovalRuleTemplateResponseTypeDef",
    {"repositoryNames": List[str], "nextToken": str},
    total=False,
)


class ClientListRepositoriesForApprovalRuleTemplateResponseTypeDef(
    _ClientListRepositoriesForApprovalRuleTemplateResponseTypeDef
):
    """
    - *(dict) --*

      - **repositoryNames** *(list) --*

        A list of repository names that are associated with the specified approval rule template.
        - *(string) --*
    """


_ClientListRepositoriesResponserepositoriesTypeDef = TypedDict(
    "_ClientListRepositoriesResponserepositoriesTypeDef",
    {"repositoryName": str, "repositoryId": str},
    total=False,
)


class ClientListRepositoriesResponserepositoriesTypeDef(
    _ClientListRepositoriesResponserepositoriesTypeDef
):
    """
    - *(dict) --*

      Information about a repository name and ID.
      - **repositoryName** *(string) --*

        The name associated with the repository.
    """


_ClientListRepositoriesResponseTypeDef = TypedDict(
    "_ClientListRepositoriesResponseTypeDef",
    {"repositories": List[ClientListRepositoriesResponserepositoriesTypeDef], "nextToken": str},
    total=False,
)


class ClientListRepositoriesResponseTypeDef(_ClientListRepositoriesResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a list repositories operation.
      - **repositories** *(list) --*

        Lists the repositories called by the list repositories operation.
        - *(dict) --*

          Information about a repository name and ID.
          - **repositoryName** *(string) --*

            The name associated with the repository.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": Dict[str, str], "nextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        A list of tag key and value pairs associated with the specified resource.
        - *(string) --*

          - *(string) --*
    """


_ClientMergeBranchesByFastForwardResponseTypeDef = TypedDict(
    "_ClientMergeBranchesByFastForwardResponseTypeDef",
    {"commitId": str, "treeId": str},
    total=False,
)


class ClientMergeBranchesByFastForwardResponseTypeDef(
    _ClientMergeBranchesByFastForwardResponseTypeDef
):
    """
    - *(dict) --*

      - **commitId** *(string) --*

        The commit ID of the merge in the destination or target branch.
    """


_ClientMergeBranchesBySquashConflictResolutiondeleteFilesTypeDef = TypedDict(
    "_ClientMergeBranchesBySquashConflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
    total=False,
)


class ClientMergeBranchesBySquashConflictResolutiondeleteFilesTypeDef(
    _ClientMergeBranchesBySquashConflictResolutiondeleteFilesTypeDef
):
    pass


_RequiredClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef",
    {"filePath": str},
)
_OptionalClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef",
    {
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
        "content": bytes,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef,
):
    """
    - *(dict) --*

      Information about a replacement content entry in the conflict of a merge or pull request
      operation.
      - **filePath** *(string) --***[REQUIRED]**

        The path of the conflicting file.
    """


_ClientMergeBranchesBySquashConflictResolutionsetFileModesTypeDef = TypedDict(
    "_ClientMergeBranchesBySquashConflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ClientMergeBranchesBySquashConflictResolutionsetFileModesTypeDef(
    _ClientMergeBranchesBySquashConflictResolutionsetFileModesTypeDef
):
    pass


_ClientMergeBranchesBySquashConflictResolutionTypeDef = TypedDict(
    "_ClientMergeBranchesBySquashConflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[ClientMergeBranchesBySquashConflictResolutiondeleteFilesTypeDef],
        "setFileModes": List[ClientMergeBranchesBySquashConflictResolutionsetFileModesTypeDef],
    },
    total=False,
)


class ClientMergeBranchesBySquashConflictResolutionTypeDef(
    _ClientMergeBranchesBySquashConflictResolutionTypeDef
):
    """
    If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving
    conflicts during a merge.
    - **replaceContents** *(list) --*

      Files to have content replaced as part of the merge conflict resolution.
      - *(dict) --*

        Information about a replacement content entry in the conflict of a merge or pull request
        operation.
        - **filePath** *(string) --***[REQUIRED]**

          The path of the conflicting file.
    """


_ClientMergeBranchesBySquashResponseTypeDef = TypedDict(
    "_ClientMergeBranchesBySquashResponseTypeDef", {"commitId": str, "treeId": str}, total=False
)


class ClientMergeBranchesBySquashResponseTypeDef(_ClientMergeBranchesBySquashResponseTypeDef):
    """
    - *(dict) --*

      - **commitId** *(string) --*

        The commit ID of the merge in the destination or target branch.
    """


_ClientMergeBranchesByThreeWayConflictResolutiondeleteFilesTypeDef = TypedDict(
    "_ClientMergeBranchesByThreeWayConflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
    total=False,
)


class ClientMergeBranchesByThreeWayConflictResolutiondeleteFilesTypeDef(
    _ClientMergeBranchesByThreeWayConflictResolutiondeleteFilesTypeDef
):
    pass


_RequiredClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef",
    {"filePath": str},
)
_OptionalClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef",
    {
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
        "content": bytes,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef,
):
    """
    - *(dict) --*

      Information about a replacement content entry in the conflict of a merge or pull request
      operation.
      - **filePath** *(string) --***[REQUIRED]**

        The path of the conflicting file.
    """


_ClientMergeBranchesByThreeWayConflictResolutionsetFileModesTypeDef = TypedDict(
    "_ClientMergeBranchesByThreeWayConflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ClientMergeBranchesByThreeWayConflictResolutionsetFileModesTypeDef(
    _ClientMergeBranchesByThreeWayConflictResolutionsetFileModesTypeDef
):
    pass


_ClientMergeBranchesByThreeWayConflictResolutionTypeDef = TypedDict(
    "_ClientMergeBranchesByThreeWayConflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[ClientMergeBranchesByThreeWayConflictResolutiondeleteFilesTypeDef],
        "setFileModes": List[ClientMergeBranchesByThreeWayConflictResolutionsetFileModesTypeDef],
    },
    total=False,
)


class ClientMergeBranchesByThreeWayConflictResolutionTypeDef(
    _ClientMergeBranchesByThreeWayConflictResolutionTypeDef
):
    """
    If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving
    conflicts during a merge.
    - **replaceContents** *(list) --*

      Files to have content replaced as part of the merge conflict resolution.
      - *(dict) --*

        Information about a replacement content entry in the conflict of a merge or pull request
        operation.
        - **filePath** *(string) --***[REQUIRED]**

          The path of the conflicting file.
    """


_ClientMergeBranchesByThreeWayResponseTypeDef = TypedDict(
    "_ClientMergeBranchesByThreeWayResponseTypeDef", {"commitId": str, "treeId": str}, total=False
)


class ClientMergeBranchesByThreeWayResponseTypeDef(_ClientMergeBranchesByThreeWayResponseTypeDef):
    """
    - *(dict) --*

      - **commitId** *(string) --*

        The commit ID of the merge in the destination or target branch.
    """


_ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "_ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)


class ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef(
    _ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef
):
    pass


_ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "_ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)


class ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesTypeDef(
    _ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesTypeDef
):
    pass


_ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)


class ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    pass


_ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef(
    _ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef
):
    pass


_ClientMergePullRequestByFastForwardResponsepullRequestTypeDef = TypedDict(
    "_ClientMergePullRequestByFastForwardResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[
            ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesTypeDef
        ],
    },
    total=False,
)


class ClientMergePullRequestByFastForwardResponsepullRequestTypeDef(
    _ClientMergePullRequestByFastForwardResponsepullRequestTypeDef
):
    """
    - **pullRequest** *(dict) --*

      Information about the specified pull request, including the merge.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_ClientMergePullRequestByFastForwardResponseTypeDef = TypedDict(
    "_ClientMergePullRequestByFastForwardResponseTypeDef",
    {"pullRequest": ClientMergePullRequestByFastForwardResponsepullRequestTypeDef},
    total=False,
)


class ClientMergePullRequestByFastForwardResponseTypeDef(
    _ClientMergePullRequestByFastForwardResponseTypeDef
):
    """
    - *(dict) --*

      - **pullRequest** *(dict) --*

        Information about the specified pull request, including the merge.
        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.
    """


_ClientMergePullRequestBySquashConflictResolutiondeleteFilesTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashConflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
    total=False,
)


class ClientMergePullRequestBySquashConflictResolutiondeleteFilesTypeDef(
    _ClientMergePullRequestBySquashConflictResolutiondeleteFilesTypeDef
):
    pass


_RequiredClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef",
    {"filePath": str},
)
_OptionalClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef",
    {
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
        "content": bytes,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef,
):
    """
    - *(dict) --*

      Information about a replacement content entry in the conflict of a merge or pull request
      operation.
      - **filePath** *(string) --***[REQUIRED]**

        The path of the conflicting file.
    """


_ClientMergePullRequestBySquashConflictResolutionsetFileModesTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashConflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ClientMergePullRequestBySquashConflictResolutionsetFileModesTypeDef(
    _ClientMergePullRequestBySquashConflictResolutionsetFileModesTypeDef
):
    pass


_ClientMergePullRequestBySquashConflictResolutionTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashConflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[ClientMergePullRequestBySquashConflictResolutiondeleteFilesTypeDef],
        "setFileModes": List[ClientMergePullRequestBySquashConflictResolutionsetFileModesTypeDef],
    },
    total=False,
)


class ClientMergePullRequestBySquashConflictResolutionTypeDef(
    _ClientMergePullRequestBySquashConflictResolutionTypeDef
):
    """
    If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving
    conflicts during a merge.
    - **replaceContents** *(list) --*

      Files to have content replaced as part of the merge conflict resolution.
      - *(dict) --*

        Information about a replacement content entry in the conflict of a merge or pull request
        operation.
        - **filePath** *(string) --***[REQUIRED]**

          The path of the conflicting file.
    """


_ClientMergePullRequestBySquashResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)


class ClientMergePullRequestBySquashResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef(
    _ClientMergePullRequestBySquashResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef
):
    pass


_ClientMergePullRequestBySquashResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientMergePullRequestBySquashResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)


class ClientMergePullRequestBySquashResponsepullRequestapprovalRulesTypeDef(
    _ClientMergePullRequestBySquashResponsepullRequestapprovalRulesTypeDef
):
    pass


_ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)


class ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    pass


_ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef(
    _ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef
):
    pass


_ClientMergePullRequestBySquashResponsepullRequestTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[
            ClientMergePullRequestBySquashResponsepullRequestapprovalRulesTypeDef
        ],
    },
    total=False,
)


class ClientMergePullRequestBySquashResponsepullRequestTypeDef(
    _ClientMergePullRequestBySquashResponsepullRequestTypeDef
):
    """
    - **pullRequest** *(dict) --*

      Returns information about a pull request.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_ClientMergePullRequestBySquashResponseTypeDef = TypedDict(
    "_ClientMergePullRequestBySquashResponseTypeDef",
    {"pullRequest": ClientMergePullRequestBySquashResponsepullRequestTypeDef},
    total=False,
)


class ClientMergePullRequestBySquashResponseTypeDef(_ClientMergePullRequestBySquashResponseTypeDef):
    """
    - *(dict) --*

      - **pullRequest** *(dict) --*

        Returns information about a pull request.
        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.
    """


_ClientMergePullRequestByThreeWayConflictResolutiondeleteFilesTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayConflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
    total=False,
)


class ClientMergePullRequestByThreeWayConflictResolutiondeleteFilesTypeDef(
    _ClientMergePullRequestByThreeWayConflictResolutiondeleteFilesTypeDef
):
    pass


_RequiredClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef",
    {"filePath": str},
)
_OptionalClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef",
    {
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
        "content": bytes,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef,
):
    """
    - *(dict) --*

      Information about a replacement content entry in the conflict of a merge or pull request
      operation.
      - **filePath** *(string) --***[REQUIRED]**

        The path of the conflicting file.
    """


_ClientMergePullRequestByThreeWayConflictResolutionsetFileModesTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayConflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ClientMergePullRequestByThreeWayConflictResolutionsetFileModesTypeDef(
    _ClientMergePullRequestByThreeWayConflictResolutionsetFileModesTypeDef
):
    pass


_ClientMergePullRequestByThreeWayConflictResolutionTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayConflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[ClientMergePullRequestByThreeWayConflictResolutiondeleteFilesTypeDef],
        "setFileModes": List[ClientMergePullRequestByThreeWayConflictResolutionsetFileModesTypeDef],
    },
    total=False,
)


class ClientMergePullRequestByThreeWayConflictResolutionTypeDef(
    _ClientMergePullRequestByThreeWayConflictResolutionTypeDef
):
    """
    If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving
    conflicts during a merge.
    - **replaceContents** *(list) --*

      Files to have content replaced as part of the merge conflict resolution.
      - *(dict) --*

        Information about a replacement content entry in the conflict of a merge or pull request
        operation.
        - **filePath** *(string) --***[REQUIRED]**

          The path of the conflicting file.
    """


_ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)


class ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef(
    _ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef
):
    pass


_ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)


class ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesTypeDef(
    _ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesTypeDef
):
    pass


_ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)


class ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    pass


_ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef(
    _ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef
):
    pass


_ClientMergePullRequestByThreeWayResponsepullRequestTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[
            ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesTypeDef
        ],
    },
    total=False,
)


class ClientMergePullRequestByThreeWayResponsepullRequestTypeDef(
    _ClientMergePullRequestByThreeWayResponsepullRequestTypeDef
):
    """
    - **pullRequest** *(dict) --*

      Returns information about a pull request.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_ClientMergePullRequestByThreeWayResponseTypeDef = TypedDict(
    "_ClientMergePullRequestByThreeWayResponseTypeDef",
    {"pullRequest": ClientMergePullRequestByThreeWayResponsepullRequestTypeDef},
    total=False,
)


class ClientMergePullRequestByThreeWayResponseTypeDef(
    _ClientMergePullRequestByThreeWayResponseTypeDef
):
    """
    - *(dict) --*

      - **pullRequest** *(dict) --*

        Returns information about a pull request.
        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.
    """


_ClientPostCommentForComparedCommitLocationTypeDef = TypedDict(
    "_ClientPostCommentForComparedCommitLocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)


class ClientPostCommentForComparedCommitLocationTypeDef(
    _ClientPostCommentForComparedCommitLocationTypeDef
):
    """
    The location of the comparison where you want to comment.
    - **filePath** *(string) --*

      The name of the file being compared, including its extension and subdirectory, if any.
    """


_ClientPostCommentForComparedCommitResponsecommentTypeDef = TypedDict(
    "_ClientPostCommentForComparedCommitResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientPostCommentForComparedCommitResponsecommentTypeDef(
    _ClientPostCommentForComparedCommitResponsecommentTypeDef
):
    pass


_ClientPostCommentForComparedCommitResponselocationTypeDef = TypedDict(
    "_ClientPostCommentForComparedCommitResponselocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)


class ClientPostCommentForComparedCommitResponselocationTypeDef(
    _ClientPostCommentForComparedCommitResponselocationTypeDef
):
    pass


_ClientPostCommentForComparedCommitResponseTypeDef = TypedDict(
    "_ClientPostCommentForComparedCommitResponseTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientPostCommentForComparedCommitResponselocationTypeDef,
        "comment": ClientPostCommentForComparedCommitResponsecommentTypeDef,
    },
    total=False,
)


class ClientPostCommentForComparedCommitResponseTypeDef(
    _ClientPostCommentForComparedCommitResponseTypeDef
):
    """
    - *(dict) --*

      - **repositoryName** *(string) --*

        The name of the repository where you posted a comment on the comparison between commits.
    """


_ClientPostCommentForPullRequestLocationTypeDef = TypedDict(
    "_ClientPostCommentForPullRequestLocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)


class ClientPostCommentForPullRequestLocationTypeDef(
    _ClientPostCommentForPullRequestLocationTypeDef
):
    """
    The location of the change where you want to post your comment. If no location is provided, the
    comment is posted as a general comment on the pull request difference between the before commit
    ID and the after commit ID.
    - **filePath** *(string) --*

      The name of the file being compared, including its extension and subdirectory, if any.
    """


_ClientPostCommentForPullRequestResponsecommentTypeDef = TypedDict(
    "_ClientPostCommentForPullRequestResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientPostCommentForPullRequestResponsecommentTypeDef(
    _ClientPostCommentForPullRequestResponsecommentTypeDef
):
    pass


_ClientPostCommentForPullRequestResponselocationTypeDef = TypedDict(
    "_ClientPostCommentForPullRequestResponselocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)


class ClientPostCommentForPullRequestResponselocationTypeDef(
    _ClientPostCommentForPullRequestResponselocationTypeDef
):
    pass


_ClientPostCommentForPullRequestResponseTypeDef = TypedDict(
    "_ClientPostCommentForPullRequestResponseTypeDef",
    {
        "repositoryName": str,
        "pullRequestId": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientPostCommentForPullRequestResponselocationTypeDef,
        "comment": ClientPostCommentForPullRequestResponsecommentTypeDef,
    },
    total=False,
)


class ClientPostCommentForPullRequestResponseTypeDef(
    _ClientPostCommentForPullRequestResponseTypeDef
):
    """
    - *(dict) --*

      - **repositoryName** *(string) --*

        The name of the repository where you posted a comment on a pull request.
    """


_ClientPostCommentReplyResponsecommentTypeDef = TypedDict(
    "_ClientPostCommentReplyResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientPostCommentReplyResponsecommentTypeDef(_ClientPostCommentReplyResponsecommentTypeDef):
    """
    - **comment** *(dict) --*

      Information about the reply to a comment.
      - **commentId** *(string) --*

        The system-generated comment ID.
    """


_ClientPostCommentReplyResponseTypeDef = TypedDict(
    "_ClientPostCommentReplyResponseTypeDef",
    {"comment": ClientPostCommentReplyResponsecommentTypeDef},
    total=False,
)


class ClientPostCommentReplyResponseTypeDef(_ClientPostCommentReplyResponseTypeDef):
    """
    - *(dict) --*

      - **comment** *(dict) --*

        Information about the reply to a comment.
        - **commentId** *(string) --*

          The system-generated comment ID.
    """


_ClientPutFileResponseTypeDef = TypedDict(
    "_ClientPutFileResponseTypeDef", {"commitId": str, "blobId": str, "treeId": str}, total=False
)


class ClientPutFileResponseTypeDef(_ClientPutFileResponseTypeDef):
    """
    - *(dict) --*

      - **commitId** *(string) --*

        The full SHA ID of the commit that contains this file change.
    """


_ClientPutRepositoryTriggersResponseTypeDef = TypedDict(
    "_ClientPutRepositoryTriggersResponseTypeDef", {"configurationId": str}, total=False
)


class ClientPutRepositoryTriggersResponseTypeDef(_ClientPutRepositoryTriggersResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a put repository triggers operation.
      - **configurationId** *(string) --*

        The system-generated unique ID for the create or update operation.
    """


_RequiredClientPutRepositoryTriggersTriggersTypeDef = TypedDict(
    "_RequiredClientPutRepositoryTriggersTriggersTypeDef", {"name": str}
)
_OptionalClientPutRepositoryTriggersTriggersTypeDef = TypedDict(
    "_OptionalClientPutRepositoryTriggersTriggersTypeDef",
    {
        "destinationArn": str,
        "customData": str,
        "branches": List[str],
        "events": List[Literal["all", "updateReference", "createReference", "deleteReference"]],
    },
    total=False,
)


class ClientPutRepositoryTriggersTriggersTypeDef(
    _RequiredClientPutRepositoryTriggersTriggersTypeDef,
    _OptionalClientPutRepositoryTriggersTriggersTypeDef,
):
    """
    - *(dict) --*

      Information about a trigger for a repository.
      - **name** *(string) --***[REQUIRED]**

        The name of the trigger.
    """


_ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef = TypedDict(
    "_ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef",
    {"trigger": str, "failureMessage": str},
    total=False,
)


class ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef(
    _ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef
):
    pass


_ClientTestRepositoryTriggersResponseTypeDef = TypedDict(
    "_ClientTestRepositoryTriggersResponseTypeDef",
    {
        "successfulExecutions": List[str],
        "failedExecutions": List[ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef],
    },
    total=False,
)


class ClientTestRepositoryTriggersResponseTypeDef(_ClientTestRepositoryTriggersResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a test repository triggers operation.
      - **successfulExecutions** *(list) --*

        The list of triggers that were successfully tested. This list provides the names of the
        triggers that were successfully tested, separated by commas.
        - *(string) --*
    """


_RequiredClientTestRepositoryTriggersTriggersTypeDef = TypedDict(
    "_RequiredClientTestRepositoryTriggersTriggersTypeDef", {"name": str}
)
_OptionalClientTestRepositoryTriggersTriggersTypeDef = TypedDict(
    "_OptionalClientTestRepositoryTriggersTriggersTypeDef",
    {
        "destinationArn": str,
        "customData": str,
        "branches": List[str],
        "events": List[Literal["all", "updateReference", "createReference", "deleteReference"]],
    },
    total=False,
)


class ClientTestRepositoryTriggersTriggersTypeDef(
    _RequiredClientTestRepositoryTriggersTriggersTypeDef,
    _OptionalClientTestRepositoryTriggersTriggersTypeDef,
):
    """
    - *(dict) --*

      Information about a trigger for a repository.
      - **name** *(string) --***[REQUIRED]**

        The name of the trigger.
    """


_ClientUpdateApprovalRuleTemplateContentResponseapprovalRuleTemplateTypeDef = TypedDict(
    "_ClientUpdateApprovalRuleTemplateContentResponseapprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)


class ClientUpdateApprovalRuleTemplateContentResponseapprovalRuleTemplateTypeDef(
    _ClientUpdateApprovalRuleTemplateContentResponseapprovalRuleTemplateTypeDef
):
    """
    - **approvalRuleTemplate** *(dict) --*

      Returns information about an approval rule template.
      - **approvalRuleTemplateId** *(string) --*

        The system-generated ID of the approval rule template.
    """


_ClientUpdateApprovalRuleTemplateContentResponseTypeDef = TypedDict(
    "_ClientUpdateApprovalRuleTemplateContentResponseTypeDef",
    {
        "approvalRuleTemplate": ClientUpdateApprovalRuleTemplateContentResponseapprovalRuleTemplateTypeDef
    },
    total=False,
)


class ClientUpdateApprovalRuleTemplateContentResponseTypeDef(
    _ClientUpdateApprovalRuleTemplateContentResponseTypeDef
):
    """
    - *(dict) --*

      - **approvalRuleTemplate** *(dict) --*

        Returns information about an approval rule template.
        - **approvalRuleTemplateId** *(string) --*

          The system-generated ID of the approval rule template.
    """


_ClientUpdateApprovalRuleTemplateDescriptionResponseapprovalRuleTemplateTypeDef = TypedDict(
    "_ClientUpdateApprovalRuleTemplateDescriptionResponseapprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)


class ClientUpdateApprovalRuleTemplateDescriptionResponseapprovalRuleTemplateTypeDef(
    _ClientUpdateApprovalRuleTemplateDescriptionResponseapprovalRuleTemplateTypeDef
):
    """
    - **approvalRuleTemplate** *(dict) --*

      The structure and content of the updated approval rule template.
      - **approvalRuleTemplateId** *(string) --*

        The system-generated ID of the approval rule template.
    """


_ClientUpdateApprovalRuleTemplateDescriptionResponseTypeDef = TypedDict(
    "_ClientUpdateApprovalRuleTemplateDescriptionResponseTypeDef",
    {
        "approvalRuleTemplate": ClientUpdateApprovalRuleTemplateDescriptionResponseapprovalRuleTemplateTypeDef
    },
    total=False,
)


class ClientUpdateApprovalRuleTemplateDescriptionResponseTypeDef(
    _ClientUpdateApprovalRuleTemplateDescriptionResponseTypeDef
):
    """
    - *(dict) --*

      - **approvalRuleTemplate** *(dict) --*

        The structure and content of the updated approval rule template.
        - **approvalRuleTemplateId** *(string) --*

          The system-generated ID of the approval rule template.
    """


_ClientUpdateApprovalRuleTemplateNameResponseapprovalRuleTemplateTypeDef = TypedDict(
    "_ClientUpdateApprovalRuleTemplateNameResponseapprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)


class ClientUpdateApprovalRuleTemplateNameResponseapprovalRuleTemplateTypeDef(
    _ClientUpdateApprovalRuleTemplateNameResponseapprovalRuleTemplateTypeDef
):
    """
    - **approvalRuleTemplate** *(dict) --*

      The structure and content of the updated approval rule template.
      - **approvalRuleTemplateId** *(string) --*

        The system-generated ID of the approval rule template.
    """


_ClientUpdateApprovalRuleTemplateNameResponseTypeDef = TypedDict(
    "_ClientUpdateApprovalRuleTemplateNameResponseTypeDef",
    {
        "approvalRuleTemplate": ClientUpdateApprovalRuleTemplateNameResponseapprovalRuleTemplateTypeDef
    },
    total=False,
)


class ClientUpdateApprovalRuleTemplateNameResponseTypeDef(
    _ClientUpdateApprovalRuleTemplateNameResponseTypeDef
):
    """
    - *(dict) --*

      - **approvalRuleTemplate** *(dict) --*

        The structure and content of the updated approval rule template.
        - **approvalRuleTemplateId** *(string) --*

          The system-generated ID of the approval rule template.
    """


_ClientUpdateCommentResponsecommentTypeDef = TypedDict(
    "_ClientUpdateCommentResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class ClientUpdateCommentResponsecommentTypeDef(_ClientUpdateCommentResponsecommentTypeDef):
    """
    - **comment** *(dict) --*

      Information about the updated comment.
      - **commentId** *(string) --*

        The system-generated comment ID.
    """


_ClientUpdateCommentResponseTypeDef = TypedDict(
    "_ClientUpdateCommentResponseTypeDef",
    {"comment": ClientUpdateCommentResponsecommentTypeDef},
    total=False,
)


class ClientUpdateCommentResponseTypeDef(_ClientUpdateCommentResponseTypeDef):
    """
    - *(dict) --*

      - **comment** *(dict) --*

        Information about the updated comment.
        - **commentId** *(string) --*

          The system-generated comment ID.
    """


_ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleoriginApprovalRuleTemplateTypeDef = TypedDict(
    "_ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)


class ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleoriginApprovalRuleTemplateTypeDef(
    _ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleoriginApprovalRuleTemplateTypeDef
):
    pass


_ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleTypeDef = TypedDict(
    "_ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)


class ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleTypeDef(
    _ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleTypeDef
):
    """
    - **approvalRule** *(dict) --*

      Information about the updated approval rule.
      - **approvalRuleId** *(string) --*

        The system-generated ID of the approval rule.
    """


_ClientUpdatePullRequestApprovalRuleContentResponseTypeDef = TypedDict(
    "_ClientUpdatePullRequestApprovalRuleContentResponseTypeDef",
    {"approvalRule": ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleTypeDef},
    total=False,
)


class ClientUpdatePullRequestApprovalRuleContentResponseTypeDef(
    _ClientUpdatePullRequestApprovalRuleContentResponseTypeDef
):
    """
    - *(dict) --*

      - **approvalRule** *(dict) --*

        Information about the updated approval rule.
        - **approvalRuleId** *(string) --*

          The system-generated ID of the approval rule.
    """


_ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "_ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)


class ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef(
    _ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef
):
    pass


_ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "_ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)


class ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesTypeDef(
    _ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesTypeDef
):
    pass


_ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)


class ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    pass


_ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef(
    _ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef
):
    pass


_ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef = TypedDict(
    "_ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[
            ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesTypeDef
        ],
    },
    total=False,
)


class ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef(
    _ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef
):
    """
    - **pullRequest** *(dict) --*

      Information about the updated pull request.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_ClientUpdatePullRequestDescriptionResponseTypeDef = TypedDict(
    "_ClientUpdatePullRequestDescriptionResponseTypeDef",
    {"pullRequest": ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef},
    total=False,
)


class ClientUpdatePullRequestDescriptionResponseTypeDef(
    _ClientUpdatePullRequestDescriptionResponseTypeDef
):
    """
    - *(dict) --*

      - **pullRequest** *(dict) --*

        Information about the updated pull request.
        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.
    """


_ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "_ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)


class ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef(
    _ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef
):
    pass


_ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "_ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)


class ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesTypeDef(
    _ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesTypeDef
):
    pass


_ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)


class ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    pass


_ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef(
    _ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef
):
    pass


_ClientUpdatePullRequestStatusResponsepullRequestTypeDef = TypedDict(
    "_ClientUpdatePullRequestStatusResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesTypeDef],
    },
    total=False,
)


class ClientUpdatePullRequestStatusResponsepullRequestTypeDef(
    _ClientUpdatePullRequestStatusResponsepullRequestTypeDef
):
    """
    - **pullRequest** *(dict) --*

      Information about the pull request.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_ClientUpdatePullRequestStatusResponseTypeDef = TypedDict(
    "_ClientUpdatePullRequestStatusResponseTypeDef",
    {"pullRequest": ClientUpdatePullRequestStatusResponsepullRequestTypeDef},
    total=False,
)


class ClientUpdatePullRequestStatusResponseTypeDef(_ClientUpdatePullRequestStatusResponseTypeDef):
    """
    - *(dict) --*

      - **pullRequest** *(dict) --*

        Information about the pull request.
        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.
    """


_ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "_ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)


class ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef(
    _ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef
):
    pass


_ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "_ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)


class ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesTypeDef(
    _ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesTypeDef
):
    pass


_ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "_ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)


class ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef(
    _ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef
):
    pass


_ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "_ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)


class ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef(
    _ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef
):
    pass


_ClientUpdatePullRequestTitleResponsepullRequestTypeDef = TypedDict(
    "_ClientUpdatePullRequestTitleResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesTypeDef],
    },
    total=False,
)


class ClientUpdatePullRequestTitleResponsepullRequestTypeDef(
    _ClientUpdatePullRequestTitleResponsepullRequestTypeDef
):
    """
    - **pullRequest** *(dict) --*

      Information about the updated pull request.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_ClientUpdatePullRequestTitleResponseTypeDef = TypedDict(
    "_ClientUpdatePullRequestTitleResponseTypeDef",
    {"pullRequest": ClientUpdatePullRequestTitleResponsepullRequestTypeDef},
    total=False,
)


class ClientUpdatePullRequestTitleResponseTypeDef(_ClientUpdatePullRequestTitleResponseTypeDef):
    """
    - *(dict) --*

      - **pullRequest** *(dict) --*

        Information about the updated pull request.
        - **pullRequestId** *(string) --*

          The system-generated ID of the pull request.
    """


_DescribePullRequestEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribePullRequestEventsPaginatePaginationConfigTypeDef(
    _DescribePullRequestEventsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleEventMetadataTypeDef",
    {"approvalRuleName": str, "approvalRuleId": str, "approvalRuleContent": str},
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleEventMetadataTypeDef
):
    pass


_DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef",
    {"revisionId": str, "overrideStatus": Literal["OVERRIDE", "REVOKE"]},
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef
):
    pass


_DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef",
    {"revisionId": str, "approvalStatus": Literal["APPROVE", "REVOKE"]},
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef
):
    pass


_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef",
    {"repositoryName": str, "sourceCommitId": str, "destinationCommitId": str, "mergeBase": str},
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef
):
    pass


_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef
):
    pass


_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "destinationReference": str,
        "mergeMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef,
    },
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef
):
    pass


_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {"repositoryName": str, "beforeCommitId": str, "afterCommitId": str, "mergeBase": str},
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef
):
    pass


_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef",
    {"pullRequestStatus": Literal["OPEN", "CLOSED"]},
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef
):
    pass


_DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef",
    {
        "pullRequestId": str,
        "eventDate": datetime,
        "pullRequestEventType": Literal[
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_STATUS_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
        ],
        "actorArn": str,
        "pullRequestCreatedEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef,
        "pullRequestStatusChangedEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef,
        "pullRequestSourceReferenceUpdatedEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef,
        "pullRequestMergedStateChangedEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef,
        "approvalRuleEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleEventMetadataTypeDef,
        "approvalStateChangedEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef,
        "approvalRuleOverriddenEventMetadata": DescribePullRequestEventsPaginateResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef,
    },
    total=False,
)


class DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef(
    _DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef
):
    """
    - *(dict) --*

      Returns information about a pull request event.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_DescribePullRequestEventsPaginateResponseTypeDef = TypedDict(
    "_DescribePullRequestEventsPaginateResponseTypeDef",
    {
        "pullRequestEvents": List[
            DescribePullRequestEventsPaginateResponsepullRequestEventsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribePullRequestEventsPaginateResponseTypeDef(
    _DescribePullRequestEventsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **pullRequestEvents** *(list) --*

        Information about the pull request events.
        - *(dict) --*

          Returns information about a pull request event.
          - **pullRequestId** *(string) --*

            The system-generated ID of the pull request.
    """


_GetCommentsForComparedCommitPaginatePaginationConfigTypeDef = TypedDict(
    "_GetCommentsForComparedCommitPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetCommentsForComparedCommitPaginatePaginationConfigTypeDef(
    _GetCommentsForComparedCommitPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef = TypedDict(
    "_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef(
    _GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef
):
    pass


_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef = TypedDict(
    "_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)


class GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef(
    _GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef
):
    pass


_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef = TypedDict(
    "_GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatalocationTypeDef,
        "comments": List[
            GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDatacommentsTypeDef
        ],
    },
    total=False,
)


class GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef(
    _GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef
):
    """
    - *(dict) --*

      Returns information about comments on the comparison between two commits.
      - **repositoryName** *(string) --*

        The name of the repository that contains the compared commits.
    """


_GetCommentsForComparedCommitPaginateResponseTypeDef = TypedDict(
    "_GetCommentsForComparedCommitPaginateResponseTypeDef",
    {
        "commentsForComparedCommitData": List[
            GetCommentsForComparedCommitPaginateResponsecommentsForComparedCommitDataTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetCommentsForComparedCommitPaginateResponseTypeDef(
    _GetCommentsForComparedCommitPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **commentsForComparedCommitData** *(list) --*

        A list of comment objects on the compared commit.
        - *(dict) --*

          Returns information about comments on the comparison between two commits.
          - **repositoryName** *(string) --*

            The name of the repository that contains the compared commits.
    """


_GetCommentsForPullRequestPaginatePaginationConfigTypeDef = TypedDict(
    "_GetCommentsForPullRequestPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetCommentsForPullRequestPaginatePaginationConfigTypeDef(
    _GetCommentsForPullRequestPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef = TypedDict(
    "_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)


class GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef(
    _GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef
):
    pass


_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef = TypedDict(
    "_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)


class GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef(
    _GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef
):
    pass


_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef = TypedDict(
    "_GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatalocationTypeDef,
        "comments": List[
            GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDatacommentsTypeDef
        ],
    },
    total=False,
)


class GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef(
    _GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef
):
    """
    - *(dict) --*

      Returns information about comments on a pull request.
      - **pullRequestId** *(string) --*

        The system-generated ID of the pull request.
    """


_GetCommentsForPullRequestPaginateResponseTypeDef = TypedDict(
    "_GetCommentsForPullRequestPaginateResponseTypeDef",
    {
        "commentsForPullRequestData": List[
            GetCommentsForPullRequestPaginateResponsecommentsForPullRequestDataTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class GetCommentsForPullRequestPaginateResponseTypeDef(
    _GetCommentsForPullRequestPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **commentsForPullRequestData** *(list) --*

        An array of comment objects on the pull request.
        - *(dict) --*

          Returns information about comments on a pull request.
          - **pullRequestId** *(string) --*

            The system-generated ID of the pull request.
    """


_GetDifferencesPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDifferencesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDifferencesPaginatePaginationConfigTypeDef(_GetDifferencesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDifferencesPaginateResponsedifferencesafterBlobTypeDef = TypedDict(
    "_GetDifferencesPaginateResponsedifferencesafterBlobTypeDef",
    {"blobId": str, "path": str, "mode": str},
    total=False,
)


class GetDifferencesPaginateResponsedifferencesafterBlobTypeDef(
    _GetDifferencesPaginateResponsedifferencesafterBlobTypeDef
):
    pass


_GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef = TypedDict(
    "_GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef",
    {"blobId": str, "path": str, "mode": str},
    total=False,
)


class GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef(
    _GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef
):
    """
    - **beforeBlob** *(dict) --*

      Information about a ``beforeBlob`` data type object, including the ID, the file mode
      permission code, and the path.
      - **blobId** *(string) --*

        The full ID of the blob.
    """


_GetDifferencesPaginateResponsedifferencesTypeDef = TypedDict(
    "_GetDifferencesPaginateResponsedifferencesTypeDef",
    {
        "beforeBlob": GetDifferencesPaginateResponsedifferencesbeforeBlobTypeDef,
        "afterBlob": GetDifferencesPaginateResponsedifferencesafterBlobTypeDef,
        "changeType": Literal["A", "M", "D"],
    },
    total=False,
)


class GetDifferencesPaginateResponsedifferencesTypeDef(
    _GetDifferencesPaginateResponsedifferencesTypeDef
):
    """
    - *(dict) --*

      Returns information about a set of differences for a commit specifier.
      - **beforeBlob** *(dict) --*

        Information about a ``beforeBlob`` data type object, including the ID, the file mode
        permission code, and the path.
        - **blobId** *(string) --*

          The full ID of the blob.
    """


_GetDifferencesPaginateResponseTypeDef = TypedDict(
    "_GetDifferencesPaginateResponseTypeDef",
    {"differences": List[GetDifferencesPaginateResponsedifferencesTypeDef]},
    total=False,
)


class GetDifferencesPaginateResponseTypeDef(_GetDifferencesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **differences** *(list) --*

        A data type object that contains information about the differences, including whether the
        difference is added, modified, or deleted (A, D, M).
        - *(dict) --*

          Returns information about a set of differences for a commit specifier.
          - **beforeBlob** *(dict) --*

            Information about a ``beforeBlob`` data type object, including the ID, the file mode
            permission code, and the path.
            - **blobId** *(string) --*

              The full ID of the blob.
    """


_ListBranchesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBranchesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListBranchesPaginatePaginationConfigTypeDef(_ListBranchesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListBranchesPaginateResponseTypeDef = TypedDict(
    "_ListBranchesPaginateResponseTypeDef", {"branches": List[str], "NextToken": str}, total=False
)


class ListBranchesPaginateResponseTypeDef(_ListBranchesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a list branches operation.
      - **branches** *(list) --*

        The list of branch names.
        - *(string) --*
    """


_ListPullRequestsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPullRequestsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPullRequestsPaginatePaginationConfigTypeDef(
    _ListPullRequestsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPullRequestsPaginateResponseTypeDef = TypedDict(
    "_ListPullRequestsPaginateResponseTypeDef",
    {"pullRequestIds": List[str], "NextToken": str},
    total=False,
)


class ListPullRequestsPaginateResponseTypeDef(_ListPullRequestsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **pullRequestIds** *(list) --*

        The system-generated IDs of the pull requests.
        - *(string) --*
    """


_ListRepositoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRepositoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListRepositoriesPaginatePaginationConfigTypeDef(
    _ListRepositoriesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListRepositoriesPaginateResponserepositoriesTypeDef = TypedDict(
    "_ListRepositoriesPaginateResponserepositoriesTypeDef",
    {"repositoryName": str, "repositoryId": str},
    total=False,
)


class ListRepositoriesPaginateResponserepositoriesTypeDef(
    _ListRepositoriesPaginateResponserepositoriesTypeDef
):
    """
    - *(dict) --*

      Information about a repository name and ID.
      - **repositoryName** *(string) --*

        The name associated with the repository.
    """


_ListRepositoriesPaginateResponseTypeDef = TypedDict(
    "_ListRepositoriesPaginateResponseTypeDef",
    {"repositories": List[ListRepositoriesPaginateResponserepositoriesTypeDef], "NextToken": str},
    total=False,
)


class ListRepositoriesPaginateResponseTypeDef(_ListRepositoriesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Represents the output of a list repositories operation.
      - **repositories** *(list) --*

        Lists the repositories called by the list repositories operation.
        - *(dict) --*

          Information about a repository name and ID.
          - **repositoryName** *(string) --*

            The name associated with the repository.
    """
