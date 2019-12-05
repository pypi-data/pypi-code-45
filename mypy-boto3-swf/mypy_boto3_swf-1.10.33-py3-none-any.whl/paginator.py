"Main interface for swf service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_swf.type_defs import (
    GetWorkflowExecutionHistoryPaginateExecutionTypeDef,
    GetWorkflowExecutionHistoryPaginatePaginationConfigTypeDef,
    GetWorkflowExecutionHistoryPaginateResponseTypeDef,
    ListActivityTypesPaginatePaginationConfigTypeDef,
    ListActivityTypesPaginateResponseTypeDef,
    ListClosedWorkflowExecutionsPaginateCloseStatusFilterTypeDef,
    ListClosedWorkflowExecutionsPaginateCloseTimeFilterTypeDef,
    ListClosedWorkflowExecutionsPaginateExecutionFilterTypeDef,
    ListClosedWorkflowExecutionsPaginatePaginationConfigTypeDef,
    ListClosedWorkflowExecutionsPaginateResponseTypeDef,
    ListClosedWorkflowExecutionsPaginateStartTimeFilterTypeDef,
    ListClosedWorkflowExecutionsPaginateTagFilterTypeDef,
    ListClosedWorkflowExecutionsPaginateTypeFilterTypeDef,
    ListDomainsPaginatePaginationConfigTypeDef,
    ListDomainsPaginateResponseTypeDef,
    ListOpenWorkflowExecutionsPaginateExecutionFilterTypeDef,
    ListOpenWorkflowExecutionsPaginatePaginationConfigTypeDef,
    ListOpenWorkflowExecutionsPaginateResponseTypeDef,
    ListOpenWorkflowExecutionsPaginateStartTimeFilterTypeDef,
    ListOpenWorkflowExecutionsPaginateTagFilterTypeDef,
    ListOpenWorkflowExecutionsPaginateTypeFilterTypeDef,
    ListWorkflowTypesPaginatePaginationConfigTypeDef,
    ListWorkflowTypesPaginateResponseTypeDef,
    PollForDecisionTaskPaginatePaginationConfigTypeDef,
    PollForDecisionTaskPaginateResponseTypeDef,
    PollForDecisionTaskPaginateTaskListTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetWorkflowExecutionHistoryPaginator",
    "ListActivityTypesPaginator",
    "ListClosedWorkflowExecutionsPaginator",
    "ListDomainsPaginator",
    "ListOpenWorkflowExecutionsPaginator",
    "ListWorkflowTypesPaginator",
    "PollForDecisionTaskPaginator",
)


class GetWorkflowExecutionHistoryPaginator(Boto3Paginator):
    """
    Paginator for `get_workflow_execution_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        execution: GetWorkflowExecutionHistoryPaginateExecutionTypeDef,
        reverseOrder: bool = None,
        PaginationConfig: GetWorkflowExecutionHistoryPaginatePaginationConfigTypeDef = None,
    ) -> GetWorkflowExecutionHistoryPaginateResponseTypeDef:
        """
        [GetWorkflowExecutionHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory.paginate)
        """


class ListActivityTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_activity_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: ListActivityTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListActivityTypesPaginateResponseTypeDef:
        """
        [ListActivityTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/swf.html#SWF.Paginator.ListActivityTypes.paginate)
        """


class ListClosedWorkflowExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_closed_workflow_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        startTimeFilter: ListClosedWorkflowExecutionsPaginateStartTimeFilterTypeDef = None,
        closeTimeFilter: ListClosedWorkflowExecutionsPaginateCloseTimeFilterTypeDef = None,
        executionFilter: ListClosedWorkflowExecutionsPaginateExecutionFilterTypeDef = None,
        closeStatusFilter: ListClosedWorkflowExecutionsPaginateCloseStatusFilterTypeDef = None,
        typeFilter: ListClosedWorkflowExecutionsPaginateTypeFilterTypeDef = None,
        tagFilter: ListClosedWorkflowExecutionsPaginateTagFilterTypeDef = None,
        reverseOrder: bool = None,
        PaginationConfig: ListClosedWorkflowExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListClosedWorkflowExecutionsPaginateResponseTypeDef:
        """
        [ListClosedWorkflowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions.paginate)
        """


class ListDomainsPaginator(Boto3Paginator):
    """
    Paginator for `list_domains`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        reverseOrder: bool = None,
        PaginationConfig: ListDomainsPaginatePaginationConfigTypeDef = None,
    ) -> ListDomainsPaginateResponseTypeDef:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/swf.html#SWF.Paginator.ListDomains.paginate)
        """


class ListOpenWorkflowExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_open_workflow_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        startTimeFilter: ListOpenWorkflowExecutionsPaginateStartTimeFilterTypeDef,
        typeFilter: ListOpenWorkflowExecutionsPaginateTypeFilterTypeDef = None,
        tagFilter: ListOpenWorkflowExecutionsPaginateTagFilterTypeDef = None,
        reverseOrder: bool = None,
        executionFilter: ListOpenWorkflowExecutionsPaginateExecutionFilterTypeDef = None,
        PaginationConfig: ListOpenWorkflowExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListOpenWorkflowExecutionsPaginateResponseTypeDef:
        """
        [ListOpenWorkflowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions.paginate)
        """


class ListWorkflowTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_workflow_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        registrationStatus: Literal["REGISTERED", "DEPRECATED"],
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: ListWorkflowTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListWorkflowTypesPaginateResponseTypeDef:
        """
        [ListWorkflowTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes.paginate)
        """


class PollForDecisionTaskPaginator(Boto3Paginator):
    """
    Paginator for `poll_for_decision_task`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domain: str,
        taskList: PollForDecisionTaskPaginateTaskListTypeDef,
        identity: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PollForDecisionTaskPaginatePaginationConfigTypeDef = None,
    ) -> PollForDecisionTaskPaginateResponseTypeDef:
        """
        [PollForDecisionTask.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/swf.html#SWF.Paginator.PollForDecisionTask.paginate)
        """
