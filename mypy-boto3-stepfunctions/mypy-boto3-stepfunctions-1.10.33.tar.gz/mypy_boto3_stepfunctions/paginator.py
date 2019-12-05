"Main interface for stepfunctions service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_stepfunctions.type_defs import (
    GetExecutionHistoryPaginatePaginationConfigTypeDef,
    GetExecutionHistoryPaginateResponseTypeDef,
    ListActivitiesPaginatePaginationConfigTypeDef,
    ListActivitiesPaginateResponseTypeDef,
    ListExecutionsPaginatePaginationConfigTypeDef,
    ListExecutionsPaginateResponseTypeDef,
    ListStateMachinesPaginatePaginationConfigTypeDef,
    ListStateMachinesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetExecutionHistoryPaginator",
    "ListActivitiesPaginator",
    "ListExecutionsPaginator",
    "ListStateMachinesPaginator",
)


class GetExecutionHistoryPaginator(Boto3Paginator):
    """
    Paginator for `get_execution_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        executionArn: str,
        reverseOrder: bool = None,
        PaginationConfig: GetExecutionHistoryPaginatePaginationConfigTypeDef = None,
    ) -> GetExecutionHistoryPaginateResponseTypeDef:
        """
        [GetExecutionHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory.paginate)
        """


class ListActivitiesPaginator(Boto3Paginator):
    """
    Paginator for `list_activities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListActivitiesPaginatePaginationConfigTypeDef = None
    ) -> ListActivitiesPaginateResponseTypeDef:
        """
        [ListActivities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/stepfunctions.html#SFN.Paginator.ListActivities.paginate)
        """


class ListExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        stateMachineArn: str,
        statusFilter: Literal["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"] = None,
        PaginationConfig: ListExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListExecutionsPaginateResponseTypeDef:
        """
        [ListExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions.paginate)
        """


class ListStateMachinesPaginator(Boto3Paginator):
    """
    Paginator for `list_state_machines`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListStateMachinesPaginatePaginationConfigTypeDef = None
    ) -> ListStateMachinesPaginateResponseTypeDef:
        """
        [ListStateMachines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines.paginate)
        """
