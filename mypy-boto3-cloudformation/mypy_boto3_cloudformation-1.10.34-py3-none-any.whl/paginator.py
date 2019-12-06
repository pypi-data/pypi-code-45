"Main interface for cloudformation service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudformation.type_defs import (
    DescribeAccountLimitsPaginatePaginationConfigTypeDef,
    DescribeAccountLimitsPaginateResponseTypeDef,
    DescribeChangeSetPaginatePaginationConfigTypeDef,
    DescribeChangeSetPaginateResponseTypeDef,
    DescribeStackEventsPaginatePaginationConfigTypeDef,
    DescribeStackEventsPaginateResponseTypeDef,
    DescribeStacksPaginatePaginationConfigTypeDef,
    DescribeStacksPaginateResponseTypeDef,
    ListChangeSetsPaginatePaginationConfigTypeDef,
    ListChangeSetsPaginateResponseTypeDef,
    ListExportsPaginatePaginationConfigTypeDef,
    ListExportsPaginateResponseTypeDef,
    ListImportsPaginatePaginationConfigTypeDef,
    ListImportsPaginateResponseTypeDef,
    ListStackInstancesPaginatePaginationConfigTypeDef,
    ListStackInstancesPaginateResponseTypeDef,
    ListStackResourcesPaginatePaginationConfigTypeDef,
    ListStackResourcesPaginateResponseTypeDef,
    ListStackSetOperationResultsPaginatePaginationConfigTypeDef,
    ListStackSetOperationResultsPaginateResponseTypeDef,
    ListStackSetOperationsPaginatePaginationConfigTypeDef,
    ListStackSetOperationsPaginateResponseTypeDef,
    ListStackSetsPaginatePaginationConfigTypeDef,
    ListStackSetsPaginateResponseTypeDef,
    ListStacksPaginatePaginationConfigTypeDef,
    ListStacksPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAccountLimitsPaginator",
    "DescribeChangeSetPaginator",
    "DescribeStackEventsPaginator",
    "DescribeStacksPaginator",
    "ListChangeSetsPaginator",
    "ListExportsPaginator",
    "ListImportsPaginator",
    "ListStackInstancesPaginator",
    "ListStackResourcesPaginator",
    "ListStackSetOperationResultsPaginator",
    "ListStackSetOperationsPaginator",
    "ListStackSetsPaginator",
    "ListStacksPaginator",
)


class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    Paginator for `describe_account_limits`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeAccountLimitsPaginatePaginationConfigTypeDef = None
    ) -> DescribeAccountLimitsPaginateResponseTypeDef:
        """
        [DescribeAccountLimits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits.paginate)
        """


class DescribeChangeSetPaginator(Boto3Paginator):
    """
    Paginator for `describe_change_set`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ChangeSetName: str,
        StackName: str = None,
        PaginationConfig: DescribeChangeSetPaginatePaginationConfigTypeDef = None,
    ) -> DescribeChangeSetPaginateResponseTypeDef:
        """
        [DescribeChangeSet.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet.paginate)
        """


class DescribeStackEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_stack_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackName: str = None,
        PaginationConfig: DescribeStackEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeStackEventsPaginateResponseTypeDef:
        """
        [DescribeStackEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents.paginate)
        """


class DescribeStacksPaginator(Boto3Paginator):
    """
    Paginator for `describe_stacks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackName: str = None,
        PaginationConfig: DescribeStacksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeStacksPaginateResponseTypeDef:
        """
        [DescribeStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks.paginate)
        """


class ListChangeSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_change_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, StackName: str, PaginationConfig: ListChangeSetsPaginatePaginationConfigTypeDef = None
    ) -> ListChangeSetsPaginateResponseTypeDef:
        """
        [ListChangeSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets.paginate)
        """


class ListExportsPaginator(Boto3Paginator):
    """
    Paginator for `list_exports`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListExportsPaginatePaginationConfigTypeDef = None
    ) -> ListExportsPaginateResponseTypeDef:
        """
        [ListExports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports.paginate)
        """


class ListImportsPaginator(Boto3Paginator):
    """
    Paginator for `list_imports`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ExportName: str, PaginationConfig: ListImportsPaginatePaginationConfigTypeDef = None
    ) -> ListImportsPaginateResponseTypeDef:
        """
        [ListImports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports.paginate)
        """


class ListStackInstancesPaginator(Boto3Paginator):
    """
    Paginator for `list_stack_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackSetName: str,
        StackInstanceAccount: str = None,
        StackInstanceRegion: str = None,
        PaginationConfig: ListStackInstancesPaginatePaginationConfigTypeDef = None,
    ) -> ListStackInstancesPaginateResponseTypeDef:
        """
        [ListStackInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances.paginate)
        """


class ListStackResourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_stack_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackName: str,
        PaginationConfig: ListStackResourcesPaginatePaginationConfigTypeDef = None,
    ) -> ListStackResourcesPaginateResponseTypeDef:
        """
        [ListStackResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources.paginate)
        """


class ListStackSetOperationResultsPaginator(Boto3Paginator):
    """
    Paginator for `list_stack_set_operation_results`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackSetName: str,
        OperationId: str,
        PaginationConfig: ListStackSetOperationResultsPaginatePaginationConfigTypeDef = None,
    ) -> ListStackSetOperationResultsPaginateResponseTypeDef:
        """
        [ListStackSetOperationResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults.paginate)
        """


class ListStackSetOperationsPaginator(Boto3Paginator):
    """
    Paginator for `list_stack_set_operations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackSetName: str,
        PaginationConfig: ListStackSetOperationsPaginatePaginationConfigTypeDef = None,
    ) -> ListStackSetOperationsPaginateResponseTypeDef:
        """
        [ListStackSetOperations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations.paginate)
        """


class ListStackSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_stack_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Status: Literal["ACTIVE", "DELETED"] = None,
        PaginationConfig: ListStackSetsPaginatePaginationConfigTypeDef = None,
    ) -> ListStackSetsPaginateResponseTypeDef:
        """
        [ListStackSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets.paginate)
        """


class ListStacksPaginator(Boto3Paginator):
    """
    Paginator for `list_stacks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        StackStatusFilter: List[
            Literal[
                "CREATE_IN_PROGRESS",
                "CREATE_FAILED",
                "CREATE_COMPLETE",
                "ROLLBACK_IN_PROGRESS",
                "ROLLBACK_FAILED",
                "ROLLBACK_COMPLETE",
                "DELETE_IN_PROGRESS",
                "DELETE_FAILED",
                "DELETE_COMPLETE",
                "UPDATE_IN_PROGRESS",
                "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_COMPLETE",
                "UPDATE_ROLLBACK_IN_PROGRESS",
                "UPDATE_ROLLBACK_FAILED",
                "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
                "UPDATE_ROLLBACK_COMPLETE",
                "REVIEW_IN_PROGRESS",
                "IMPORT_IN_PROGRESS",
                "IMPORT_COMPLETE",
                "IMPORT_ROLLBACK_IN_PROGRESS",
                "IMPORT_ROLLBACK_FAILED",
                "IMPORT_ROLLBACK_COMPLETE",
            ]
        ] = None,
        PaginationConfig: ListStacksPaginatePaginationConfigTypeDef = None,
    ) -> ListStacksPaginateResponseTypeDef:
        """
        [ListStacks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks.paginate)
        """
