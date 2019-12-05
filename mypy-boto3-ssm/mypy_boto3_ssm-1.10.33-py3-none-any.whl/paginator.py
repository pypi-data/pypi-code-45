"Main interface for ssm service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ssm.type_defs import (
    DescribeActivationsPaginateFiltersTypeDef,
    DescribeActivationsPaginatePaginationConfigTypeDef,
    DescribeActivationsPaginateResponseTypeDef,
    DescribeAssociationExecutionTargetsPaginateFiltersTypeDef,
    DescribeAssociationExecutionTargetsPaginatePaginationConfigTypeDef,
    DescribeAssociationExecutionTargetsPaginateResponseTypeDef,
    DescribeAssociationExecutionsPaginateFiltersTypeDef,
    DescribeAssociationExecutionsPaginatePaginationConfigTypeDef,
    DescribeAssociationExecutionsPaginateResponseTypeDef,
    DescribeAutomationExecutionsPaginateFiltersTypeDef,
    DescribeAutomationExecutionsPaginatePaginationConfigTypeDef,
    DescribeAutomationExecutionsPaginateResponseTypeDef,
    DescribeAutomationStepExecutionsPaginateFiltersTypeDef,
    DescribeAutomationStepExecutionsPaginatePaginationConfigTypeDef,
    DescribeAutomationStepExecutionsPaginateResponseTypeDef,
    DescribeAvailablePatchesPaginateFiltersTypeDef,
    DescribeAvailablePatchesPaginatePaginationConfigTypeDef,
    DescribeAvailablePatchesPaginateResponseTypeDef,
    DescribeEffectiveInstanceAssociationsPaginatePaginationConfigTypeDef,
    DescribeEffectiveInstanceAssociationsPaginateResponseTypeDef,
    DescribeEffectivePatchesForPatchBaselinePaginatePaginationConfigTypeDef,
    DescribeEffectivePatchesForPatchBaselinePaginateResponseTypeDef,
    DescribeInstanceAssociationsStatusPaginatePaginationConfigTypeDef,
    DescribeInstanceAssociationsStatusPaginateResponseTypeDef,
    DescribeInstanceInformationPaginateFiltersTypeDef,
    DescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef,
    DescribeInstanceInformationPaginatePaginationConfigTypeDef,
    DescribeInstanceInformationPaginateResponseTypeDef,
    DescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef,
    DescribeInstancePatchStatesForPatchGroupPaginatePaginationConfigTypeDef,
    DescribeInstancePatchStatesForPatchGroupPaginateResponseTypeDef,
    DescribeInstancePatchStatesPaginatePaginationConfigTypeDef,
    DescribeInstancePatchStatesPaginateResponseTypeDef,
    DescribeInstancePatchesPaginateFiltersTypeDef,
    DescribeInstancePatchesPaginatePaginationConfigTypeDef,
    DescribeInstancePatchesPaginateResponseTypeDef,
    DescribeInventoryDeletionsPaginatePaginationConfigTypeDef,
    DescribeInventoryDeletionsPaginateResponseTypeDef,
    DescribeMaintenanceWindowExecutionTaskInvocationsPaginateFiltersTypeDef,
    DescribeMaintenanceWindowExecutionTaskInvocationsPaginatePaginationConfigTypeDef,
    DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseTypeDef,
    DescribeMaintenanceWindowExecutionTasksPaginateFiltersTypeDef,
    DescribeMaintenanceWindowExecutionTasksPaginatePaginationConfigTypeDef,
    DescribeMaintenanceWindowExecutionTasksPaginateResponseTypeDef,
    DescribeMaintenanceWindowExecutionsPaginateFiltersTypeDef,
    DescribeMaintenanceWindowExecutionsPaginatePaginationConfigTypeDef,
    DescribeMaintenanceWindowExecutionsPaginateResponseTypeDef,
    DescribeMaintenanceWindowSchedulePaginateFiltersTypeDef,
    DescribeMaintenanceWindowSchedulePaginatePaginationConfigTypeDef,
    DescribeMaintenanceWindowSchedulePaginateResponseTypeDef,
    DescribeMaintenanceWindowSchedulePaginateTargetsTypeDef,
    DescribeMaintenanceWindowTargetsPaginateFiltersTypeDef,
    DescribeMaintenanceWindowTargetsPaginatePaginationConfigTypeDef,
    DescribeMaintenanceWindowTargetsPaginateResponseTypeDef,
    DescribeMaintenanceWindowTasksPaginateFiltersTypeDef,
    DescribeMaintenanceWindowTasksPaginatePaginationConfigTypeDef,
    DescribeMaintenanceWindowTasksPaginateResponseTypeDef,
    DescribeMaintenanceWindowsForTargetPaginatePaginationConfigTypeDef,
    DescribeMaintenanceWindowsForTargetPaginateResponseTypeDef,
    DescribeMaintenanceWindowsForTargetPaginateTargetsTypeDef,
    DescribeMaintenanceWindowsPaginateFiltersTypeDef,
    DescribeMaintenanceWindowsPaginatePaginationConfigTypeDef,
    DescribeMaintenanceWindowsPaginateResponseTypeDef,
    DescribeParametersPaginateFiltersTypeDef,
    DescribeParametersPaginatePaginationConfigTypeDef,
    DescribeParametersPaginateParameterFiltersTypeDef,
    DescribeParametersPaginateResponseTypeDef,
    DescribePatchBaselinesPaginateFiltersTypeDef,
    DescribePatchBaselinesPaginatePaginationConfigTypeDef,
    DescribePatchBaselinesPaginateResponseTypeDef,
    DescribePatchGroupsPaginateFiltersTypeDef,
    DescribePatchGroupsPaginatePaginationConfigTypeDef,
    DescribePatchGroupsPaginateResponseTypeDef,
    DescribeSessionsPaginateFiltersTypeDef,
    DescribeSessionsPaginatePaginationConfigTypeDef,
    DescribeSessionsPaginateResponseTypeDef,
    GetInventoryPaginateAggregatorsTypeDef,
    GetInventoryPaginateFiltersTypeDef,
    GetInventoryPaginatePaginationConfigTypeDef,
    GetInventoryPaginateResponseTypeDef,
    GetInventoryPaginateResultAttributesTypeDef,
    GetInventorySchemaPaginatePaginationConfigTypeDef,
    GetInventorySchemaPaginateResponseTypeDef,
    GetParameterHistoryPaginatePaginationConfigTypeDef,
    GetParameterHistoryPaginateResponseTypeDef,
    GetParametersByPathPaginatePaginationConfigTypeDef,
    GetParametersByPathPaginateParameterFiltersTypeDef,
    GetParametersByPathPaginateResponseTypeDef,
    ListAssociationVersionsPaginatePaginationConfigTypeDef,
    ListAssociationVersionsPaginateResponseTypeDef,
    ListAssociationsPaginateAssociationFilterListTypeDef,
    ListAssociationsPaginatePaginationConfigTypeDef,
    ListAssociationsPaginateResponseTypeDef,
    ListCommandInvocationsPaginateFiltersTypeDef,
    ListCommandInvocationsPaginatePaginationConfigTypeDef,
    ListCommandInvocationsPaginateResponseTypeDef,
    ListCommandsPaginateFiltersTypeDef,
    ListCommandsPaginatePaginationConfigTypeDef,
    ListCommandsPaginateResponseTypeDef,
    ListComplianceItemsPaginateFiltersTypeDef,
    ListComplianceItemsPaginatePaginationConfigTypeDef,
    ListComplianceItemsPaginateResponseTypeDef,
    ListComplianceSummariesPaginateFiltersTypeDef,
    ListComplianceSummariesPaginatePaginationConfigTypeDef,
    ListComplianceSummariesPaginateResponseTypeDef,
    ListDocumentVersionsPaginatePaginationConfigTypeDef,
    ListDocumentVersionsPaginateResponseTypeDef,
    ListDocumentsPaginateDocumentFilterListTypeDef,
    ListDocumentsPaginateFiltersTypeDef,
    ListDocumentsPaginatePaginationConfigTypeDef,
    ListDocumentsPaginateResponseTypeDef,
    ListResourceComplianceSummariesPaginateFiltersTypeDef,
    ListResourceComplianceSummariesPaginatePaginationConfigTypeDef,
    ListResourceComplianceSummariesPaginateResponseTypeDef,
    ListResourceDataSyncPaginatePaginationConfigTypeDef,
    ListResourceDataSyncPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeActivationsPaginator",
    "DescribeAssociationExecutionTargetsPaginator",
    "DescribeAssociationExecutionsPaginator",
    "DescribeAutomationExecutionsPaginator",
    "DescribeAutomationStepExecutionsPaginator",
    "DescribeAvailablePatchesPaginator",
    "DescribeEffectiveInstanceAssociationsPaginator",
    "DescribeEffectivePatchesForPatchBaselinePaginator",
    "DescribeInstanceAssociationsStatusPaginator",
    "DescribeInstanceInformationPaginator",
    "DescribeInstancePatchStatesPaginator",
    "DescribeInstancePatchStatesForPatchGroupPaginator",
    "DescribeInstancePatchesPaginator",
    "DescribeInventoryDeletionsPaginator",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginator",
    "DescribeMaintenanceWindowExecutionTasksPaginator",
    "DescribeMaintenanceWindowExecutionsPaginator",
    "DescribeMaintenanceWindowSchedulePaginator",
    "DescribeMaintenanceWindowTargetsPaginator",
    "DescribeMaintenanceWindowTasksPaginator",
    "DescribeMaintenanceWindowsPaginator",
    "DescribeMaintenanceWindowsForTargetPaginator",
    "DescribeParametersPaginator",
    "DescribePatchBaselinesPaginator",
    "DescribePatchGroupsPaginator",
    "DescribeSessionsPaginator",
    "GetInventoryPaginator",
    "GetInventorySchemaPaginator",
    "GetParameterHistoryPaginator",
    "GetParametersByPathPaginator",
    "ListAssociationVersionsPaginator",
    "ListAssociationsPaginator",
    "ListCommandInvocationsPaginator",
    "ListCommandsPaginator",
    "ListComplianceItemsPaginator",
    "ListComplianceSummariesPaginator",
    "ListDocumentVersionsPaginator",
    "ListDocumentsPaginator",
    "ListResourceComplianceSummariesPaginator",
    "ListResourceDataSyncPaginator",
)


class DescribeActivationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_activations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeActivationsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeActivationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeActivationsPaginateResponseTypeDef:
        """
        [DescribeActivations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeActivations.paginate)
        """


class DescribeAssociationExecutionTargetsPaginator(Boto3Paginator):
    """
    Paginator for `describe_association_execution_targets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: List[DescribeAssociationExecutionTargetsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeAssociationExecutionTargetsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAssociationExecutionTargetsPaginateResponseTypeDef:
        """
        [DescribeAssociationExecutionTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets.paginate)
        """


class DescribeAssociationExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_association_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssociationId: str,
        Filters: List[DescribeAssociationExecutionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeAssociationExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAssociationExecutionsPaginateResponseTypeDef:
        """
        [DescribeAssociationExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions.paginate)
        """


class DescribeAutomationExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_automation_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeAutomationExecutionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeAutomationExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAutomationExecutionsPaginateResponseTypeDef:
        """
        [DescribeAutomationExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions.paginate)
        """


class DescribeAutomationStepExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_automation_step_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AutomationExecutionId: str,
        Filters: List[DescribeAutomationStepExecutionsPaginateFiltersTypeDef] = None,
        ReverseOrder: bool = None,
        PaginationConfig: DescribeAutomationStepExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAutomationStepExecutionsPaginateResponseTypeDef:
        """
        [DescribeAutomationStepExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions.paginate)
        """


class DescribeAvailablePatchesPaginator(Boto3Paginator):
    """
    Paginator for `describe_available_patches`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeAvailablePatchesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeAvailablePatchesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeAvailablePatchesPaginateResponseTypeDef:
        """
        [DescribeAvailablePatches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches.paginate)
        """


class DescribeEffectiveInstanceAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_effective_instance_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: DescribeEffectiveInstanceAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEffectiveInstanceAssociationsPaginateResponseTypeDef:
        """
        [DescribeEffectiveInstanceAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations.paginate)
        """


class DescribeEffectivePatchesForPatchBaselinePaginator(Boto3Paginator):
    """
    Paginator for `describe_effective_patches_for_patch_baseline`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BaselineId: str,
        PaginationConfig: DescribeEffectivePatchesForPatchBaselinePaginatePaginationConfigTypeDef = None,
    ) -> DescribeEffectivePatchesForPatchBaselinePaginateResponseTypeDef:
        """
        [DescribeEffectivePatchesForPatchBaseline.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline.paginate)
        """


class DescribeInstanceAssociationsStatusPaginator(Boto3Paginator):
    """
    Paginator for `describe_instance_associations_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: DescribeInstanceAssociationsStatusPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInstanceAssociationsStatusPaginateResponseTypeDef:
        """
        [DescribeInstanceAssociationsStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus.paginate)
        """


class DescribeInstanceInformationPaginator(Boto3Paginator):
    """
    Paginator for `describe_instance_information`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceInformationFilterList: List[
            DescribeInstanceInformationPaginateInstanceInformationFilterListTypeDef
        ] = None,
        Filters: List[DescribeInstanceInformationPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeInstanceInformationPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInstanceInformationPaginateResponseTypeDef:
        """
        [DescribeInstanceInformation.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation.paginate)
        """


class DescribeInstancePatchStatesPaginator(Boto3Paginator):
    """
    Paginator for `describe_instance_patch_states`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceIds: List[str],
        PaginationConfig: DescribeInstancePatchStatesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInstancePatchStatesPaginateResponseTypeDef:
        """
        [DescribeInstancePatchStates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates.paginate)
        """


class DescribeInstancePatchStatesForPatchGroupPaginator(Boto3Paginator):
    """
    Paginator for `describe_instance_patch_states_for_patch_group`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PatchGroup: str,
        Filters: List[DescribeInstancePatchStatesForPatchGroupPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeInstancePatchStatesForPatchGroupPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInstancePatchStatesForPatchGroupPaginateResponseTypeDef:
        """
        [DescribeInstancePatchStatesForPatchGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup.paginate)
        """


class DescribeInstancePatchesPaginator(Boto3Paginator):
    """
    Paginator for `describe_instance_patches`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        InstanceId: str,
        Filters: List[DescribeInstancePatchesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeInstancePatchesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInstancePatchesPaginateResponseTypeDef:
        """
        [DescribeInstancePatches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches.paginate)
        """


class DescribeInventoryDeletionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_inventory_deletions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DeletionId: str = None,
        PaginationConfig: DescribeInventoryDeletionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeInventoryDeletionsPaginateResponseTypeDef:
        """
        [DescribeInventoryDeletions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions.paginate)
        """


class DescribeMaintenanceWindowExecutionTaskInvocationsPaginator(Boto3Paginator):
    """
    Paginator for `describe_maintenance_window_execution_task_invocations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List[
            DescribeMaintenanceWindowExecutionTaskInvocationsPaginateFiltersTypeDef
        ] = None,
        PaginationConfig: DescribeMaintenanceWindowExecutionTaskInvocationsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMaintenanceWindowExecutionTaskInvocationsPaginateResponseTypeDef:
        """
        [DescribeMaintenanceWindowExecutionTaskInvocations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations.paginate)
        """


class DescribeMaintenanceWindowExecutionTasksPaginator(Boto3Paginator):
    """
    Paginator for `describe_maintenance_window_execution_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowExecutionId: str,
        Filters: List[DescribeMaintenanceWindowExecutionTasksPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeMaintenanceWindowExecutionTasksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMaintenanceWindowExecutionTasksPaginateResponseTypeDef:
        """
        [DescribeMaintenanceWindowExecutionTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks.paginate)
        """


class DescribeMaintenanceWindowExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_maintenance_window_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowId: str,
        Filters: List[DescribeMaintenanceWindowExecutionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeMaintenanceWindowExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMaintenanceWindowExecutionsPaginateResponseTypeDef:
        """
        [DescribeMaintenanceWindowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions.paginate)
        """


class DescribeMaintenanceWindowSchedulePaginator(Boto3Paginator):
    """
    Paginator for `describe_maintenance_window_schedule`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowId: str = None,
        Targets: List[DescribeMaintenanceWindowSchedulePaginateTargetsTypeDef] = None,
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"] = None,
        Filters: List[DescribeMaintenanceWindowSchedulePaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeMaintenanceWindowSchedulePaginatePaginationConfigTypeDef = None,
    ) -> DescribeMaintenanceWindowSchedulePaginateResponseTypeDef:
        """
        [DescribeMaintenanceWindowSchedule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule.paginate)
        """


class DescribeMaintenanceWindowTargetsPaginator(Boto3Paginator):
    """
    Paginator for `describe_maintenance_window_targets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowId: str,
        Filters: List[DescribeMaintenanceWindowTargetsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeMaintenanceWindowTargetsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMaintenanceWindowTargetsPaginateResponseTypeDef:
        """
        [DescribeMaintenanceWindowTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets.paginate)
        """


class DescribeMaintenanceWindowTasksPaginator(Boto3Paginator):
    """
    Paginator for `describe_maintenance_window_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WindowId: str,
        Filters: List[DescribeMaintenanceWindowTasksPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeMaintenanceWindowTasksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMaintenanceWindowTasksPaginateResponseTypeDef:
        """
        [DescribeMaintenanceWindowTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks.paginate)
        """


class DescribeMaintenanceWindowsPaginator(Boto3Paginator):
    """
    Paginator for `describe_maintenance_windows`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeMaintenanceWindowsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeMaintenanceWindowsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMaintenanceWindowsPaginateResponseTypeDef:
        """
        [DescribeMaintenanceWindows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows.paginate)
        """


class DescribeMaintenanceWindowsForTargetPaginator(Boto3Paginator):
    """
    Paginator for `describe_maintenance_windows_for_target`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Targets: List[DescribeMaintenanceWindowsForTargetPaginateTargetsTypeDef],
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"],
        PaginationConfig: DescribeMaintenanceWindowsForTargetPaginatePaginationConfigTypeDef = None,
    ) -> DescribeMaintenanceWindowsForTargetPaginateResponseTypeDef:
        """
        [DescribeMaintenanceWindowsForTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget.paginate)
        """


class DescribeParametersPaginator(Boto3Paginator):
    """
    Paginator for `describe_parameters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeParametersPaginateFiltersTypeDef] = None,
        ParameterFilters: List[DescribeParametersPaginateParameterFiltersTypeDef] = None,
        PaginationConfig: DescribeParametersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeParametersPaginateResponseTypeDef:
        """
        [DescribeParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeParameters.paginate)
        """


class DescribePatchBaselinesPaginator(Boto3Paginator):
    """
    Paginator for `describe_patch_baselines`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribePatchBaselinesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribePatchBaselinesPaginatePaginationConfigTypeDef = None,
    ) -> DescribePatchBaselinesPaginateResponseTypeDef:
        """
        [DescribePatchBaselines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines.paginate)
        """


class DescribePatchGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_patch_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribePatchGroupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribePatchGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribePatchGroupsPaginateResponseTypeDef:
        """
        [DescribePatchGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups.paginate)
        """


class DescribeSessionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_sessions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        State: Literal["Active", "History"],
        Filters: List[DescribeSessionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeSessionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSessionsPaginateResponseTypeDef:
        """
        [DescribeSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.DescribeSessions.paginate)
        """


class GetInventoryPaginator(Boto3Paginator):
    """
    Paginator for `get_inventory`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[GetInventoryPaginateFiltersTypeDef] = None,
        Aggregators: List[GetInventoryPaginateAggregatorsTypeDef] = None,
        ResultAttributes: List[GetInventoryPaginateResultAttributesTypeDef] = None,
        PaginationConfig: GetInventoryPaginatePaginationConfigTypeDef = None,
    ) -> GetInventoryPaginateResponseTypeDef:
        """
        [GetInventory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.GetInventory.paginate)
        """


class GetInventorySchemaPaginator(Boto3Paginator):
    """
    Paginator for `get_inventory_schema`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TypeName: str = None,
        Aggregator: bool = None,
        SubType: bool = None,
        PaginationConfig: GetInventorySchemaPaginatePaginationConfigTypeDef = None,
    ) -> GetInventorySchemaPaginateResponseTypeDef:
        """
        [GetInventorySchema.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.GetInventorySchema.paginate)
        """


class GetParameterHistoryPaginator(Boto3Paginator):
    """
    Paginator for `get_parameter_history`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Name: str,
        WithDecryption: bool = None,
        PaginationConfig: GetParameterHistoryPaginatePaginationConfigTypeDef = None,
    ) -> GetParameterHistoryPaginateResponseTypeDef:
        """
        [GetParameterHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.GetParameterHistory.paginate)
        """


class GetParametersByPathPaginator(Boto3Paginator):
    """
    Paginator for `get_parameters_by_path`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List[GetParametersByPathPaginateParameterFiltersTypeDef] = None,
        WithDecryption: bool = None,
        PaginationConfig: GetParametersByPathPaginatePaginationConfigTypeDef = None,
    ) -> GetParametersByPathPaginateResponseTypeDef:
        """
        [GetParametersByPath.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.GetParametersByPath.paginate)
        """


class ListAssociationVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_association_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssociationId: str,
        PaginationConfig: ListAssociationVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListAssociationVersionsPaginateResponseTypeDef:
        """
        [ListAssociationVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions.paginate)
        """


class ListAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `list_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        AssociationFilterList: List[ListAssociationsPaginateAssociationFilterListTypeDef] = None,
        PaginationConfig: ListAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> ListAssociationsPaginateResponseTypeDef:
        """
        [ListAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.ListAssociations.paginate)
        """


class ListCommandInvocationsPaginator(Boto3Paginator):
    """
    Paginator for `list_command_invocations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List[ListCommandInvocationsPaginateFiltersTypeDef] = None,
        Details: bool = None,
        PaginationConfig: ListCommandInvocationsPaginatePaginationConfigTypeDef = None,
    ) -> ListCommandInvocationsPaginateResponseTypeDef:
        """
        [ListCommandInvocations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations.paginate)
        """


class ListCommandsPaginator(Boto3Paginator):
    """
    Paginator for `list_commands`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List[ListCommandsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListCommandsPaginatePaginationConfigTypeDef = None,
    ) -> ListCommandsPaginateResponseTypeDef:
        """
        [ListCommands.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.ListCommands.paginate)
        """


class ListComplianceItemsPaginator(Boto3Paginator):
    """
    Paginator for `list_compliance_items`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListComplianceItemsPaginateFiltersTypeDef] = None,
        ResourceIds: List[str] = None,
        ResourceTypes: List[str] = None,
        PaginationConfig: ListComplianceItemsPaginatePaginationConfigTypeDef = None,
    ) -> ListComplianceItemsPaginateResponseTypeDef:
        """
        [ListComplianceItems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.ListComplianceItems.paginate)
        """


class ListComplianceSummariesPaginator(Boto3Paginator):
    """
    Paginator for `list_compliance_summaries`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListComplianceSummariesPaginateFiltersTypeDef] = None,
        PaginationConfig: ListComplianceSummariesPaginatePaginationConfigTypeDef = None,
    ) -> ListComplianceSummariesPaginateResponseTypeDef:
        """
        [ListComplianceSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries.paginate)
        """


class ListDocumentVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_document_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Name: str,
        PaginationConfig: ListDocumentVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListDocumentVersionsPaginateResponseTypeDef:
        """
        [ListDocumentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions.paginate)
        """


class ListDocumentsPaginator(Boto3Paginator):
    """
    Paginator for `list_documents`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DocumentFilterList: List[ListDocumentsPaginateDocumentFilterListTypeDef] = None,
        Filters: List[ListDocumentsPaginateFiltersTypeDef] = None,
        PaginationConfig: ListDocumentsPaginatePaginationConfigTypeDef = None,
    ) -> ListDocumentsPaginateResponseTypeDef:
        """
        [ListDocuments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.ListDocuments.paginate)
        """


class ListResourceComplianceSummariesPaginator(Boto3Paginator):
    """
    Paginator for `list_resource_compliance_summaries`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[ListResourceComplianceSummariesPaginateFiltersTypeDef] = None,
        PaginationConfig: ListResourceComplianceSummariesPaginatePaginationConfigTypeDef = None,
    ) -> ListResourceComplianceSummariesPaginateResponseTypeDef:
        """
        [ListResourceComplianceSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries.paginate)
        """


class ListResourceDataSyncPaginator(Boto3Paginator):
    """
    Paginator for `list_resource_data_sync`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SyncType: str = None,
        PaginationConfig: ListResourceDataSyncPaginatePaginationConfigTypeDef = None,
    ) -> ListResourceDataSyncPaginateResponseTypeDef:
        """
        [ListResourceDataSync.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync.paginate)
        """
