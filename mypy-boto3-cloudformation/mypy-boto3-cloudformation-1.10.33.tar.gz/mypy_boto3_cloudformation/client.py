"Main interface for cloudformation service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_cloudformation.client as client_scope

# pylint: disable=import-self
import mypy_boto3_cloudformation.paginator as paginator_scope
from mypy_boto3_cloudformation.type_defs import (
    ClientCreateChangeSetParametersTypeDef,
    ClientCreateChangeSetResourcesToImportTypeDef,
    ClientCreateChangeSetResponseTypeDef,
    ClientCreateChangeSetRollbackConfigurationTypeDef,
    ClientCreateChangeSetTagsTypeDef,
    ClientCreateStackInstancesOperationPreferencesTypeDef,
    ClientCreateStackInstancesParameterOverridesTypeDef,
    ClientCreateStackInstancesResponseTypeDef,
    ClientCreateStackParametersTypeDef,
    ClientCreateStackResponseTypeDef,
    ClientCreateStackRollbackConfigurationTypeDef,
    ClientCreateStackSetParametersTypeDef,
    ClientCreateStackSetResponseTypeDef,
    ClientCreateStackSetTagsTypeDef,
    ClientCreateStackTagsTypeDef,
    ClientDeleteStackInstancesOperationPreferencesTypeDef,
    ClientDeleteStackInstancesResponseTypeDef,
    ClientDescribeAccountLimitsResponseTypeDef,
    ClientDescribeChangeSetResponseTypeDef,
    ClientDescribeStackDriftDetectionStatusResponseTypeDef,
    ClientDescribeStackEventsResponseTypeDef,
    ClientDescribeStackInstanceResponseTypeDef,
    ClientDescribeStackResourceDriftsResponseTypeDef,
    ClientDescribeStackResourceResponseTypeDef,
    ClientDescribeStackResourcesResponseTypeDef,
    ClientDescribeStackSetOperationResponseTypeDef,
    ClientDescribeStackSetResponseTypeDef,
    ClientDescribeStacksResponseTypeDef,
    ClientDescribeTypeRegistrationResponseTypeDef,
    ClientDescribeTypeResponseTypeDef,
    ClientDetectStackDriftResponseTypeDef,
    ClientDetectStackResourceDriftResponseTypeDef,
    ClientDetectStackSetDriftOperationPreferencesTypeDef,
    ClientDetectStackSetDriftResponseTypeDef,
    ClientEstimateTemplateCostParametersTypeDef,
    ClientEstimateTemplateCostResponseTypeDef,
    ClientGetStackPolicyResponseTypeDef,
    ClientGetTemplateResponseTypeDef,
    ClientGetTemplateSummaryResponseTypeDef,
    ClientListChangeSetsResponseTypeDef,
    ClientListExportsResponseTypeDef,
    ClientListImportsResponseTypeDef,
    ClientListStackInstancesResponseTypeDef,
    ClientListStackResourcesResponseTypeDef,
    ClientListStackSetOperationResultsResponseTypeDef,
    ClientListStackSetOperationsResponseTypeDef,
    ClientListStackSetsResponseTypeDef,
    ClientListStacksResponseTypeDef,
    ClientListTypeRegistrationsResponseTypeDef,
    ClientListTypeVersionsResponseTypeDef,
    ClientListTypesResponseTypeDef,
    ClientRegisterTypeLoggingConfigTypeDef,
    ClientRegisterTypeResponseTypeDef,
    ClientUpdateStackInstancesOperationPreferencesTypeDef,
    ClientUpdateStackInstancesParameterOverridesTypeDef,
    ClientUpdateStackInstancesResponseTypeDef,
    ClientUpdateStackParametersTypeDef,
    ClientUpdateStackResponseTypeDef,
    ClientUpdateStackRollbackConfigurationTypeDef,
    ClientUpdateStackSetOperationPreferencesTypeDef,
    ClientUpdateStackSetParametersTypeDef,
    ClientUpdateStackSetResponseTypeDef,
    ClientUpdateStackSetTagsTypeDef,
    ClientUpdateStackTagsTypeDef,
    ClientUpdateTerminationProtectionResponseTypeDef,
    ClientValidateTemplateResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_cloudformation.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [CloudFormation.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_update_stack(self, StackName: str, ClientRequestToken: str = None) -> None:
        """
        [Client.cancel_update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.cancel_update_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def continue_update_rollback(
        self,
        StackName: str,
        RoleARN: str = None,
        ResourcesToSkip: List[str] = None,
        ClientRequestToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.continue_update_rollback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.continue_update_rollback)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_change_set(
        self,
        StackName: str,
        ChangeSetName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        Parameters: List[ClientCreateChangeSetParametersTypeDef] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        RollbackConfiguration: ClientCreateChangeSetRollbackConfigurationTypeDef = None,
        NotificationARNs: List[str] = None,
        Tags: List[ClientCreateChangeSetTagsTypeDef] = None,
        ClientToken: str = None,
        Description: str = None,
        ChangeSetType: Literal["CREATE", "UPDATE", "IMPORT"] = None,
        ResourcesToImport: List[ClientCreateChangeSetResourcesToImportTypeDef] = None,
    ) -> ClientCreateChangeSetResponseTypeDef:
        """
        [Client.create_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.create_change_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stack(
        self,
        StackName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List[ClientCreateStackParametersTypeDef] = None,
        DisableRollback: bool = None,
        RollbackConfiguration: ClientCreateStackRollbackConfigurationTypeDef = None,
        TimeoutInMinutes: int = None,
        NotificationARNs: List[str] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        OnFailure: Literal["DO_NOTHING", "ROLLBACK", "DELETE"] = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        Tags: List[ClientCreateStackTagsTypeDef] = None,
        ClientRequestToken: str = None,
        EnableTerminationProtection: bool = None,
    ) -> ClientCreateStackResponseTypeDef:
        """
        [Client.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.create_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stack_instances(
        self,
        StackSetName: str,
        Accounts: List[str],
        Regions: List[str],
        ParameterOverrides: List[ClientCreateStackInstancesParameterOverridesTypeDef] = None,
        OperationPreferences: ClientCreateStackInstancesOperationPreferencesTypeDef = None,
        OperationId: str = None,
    ) -> ClientCreateStackInstancesResponseTypeDef:
        """
        [Client.create_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.create_stack_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stack_set(
        self,
        StackSetName: str,
        Description: str = None,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List[ClientCreateStackSetParametersTypeDef] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        Tags: List[ClientCreateStackSetTagsTypeDef] = None,
        AdministrationRoleARN: str = None,
        ExecutionRoleName: str = None,
        ClientRequestToken: str = None,
    ) -> ClientCreateStackSetResponseTypeDef:
        """
        [Client.create_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.create_stack_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_change_set(self, ChangeSetName: str, StackName: str = None) -> Dict[str, Any]:
        """
        [Client.delete_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.delete_change_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_stack(
        self,
        StackName: str,
        RetainResources: List[str] = None,
        RoleARN: str = None,
        ClientRequestToken: str = None,
    ) -> None:
        """
        [Client.delete_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.delete_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_stack_instances(
        self,
        StackSetName: str,
        Accounts: List[str],
        Regions: List[str],
        RetainStacks: bool,
        OperationPreferences: ClientDeleteStackInstancesOperationPreferencesTypeDef = None,
        OperationId: str = None,
    ) -> ClientDeleteStackInstancesResponseTypeDef:
        """
        [Client.delete_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.delete_stack_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_stack_set(self, StackSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.delete_stack_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_type(
        self, Arn: str = None, Type: str = None, TypeName: str = None, VersionId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.deregister_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.deregister_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_limits(
        self, NextToken: str = None
    ) -> ClientDescribeAccountLimitsResponseTypeDef:
        """
        [Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_account_limits)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_change_set(
        self, ChangeSetName: str, StackName: str = None, NextToken: str = None
    ) -> ClientDescribeChangeSetResponseTypeDef:
        """
        [Client.describe_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_change_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stack_drift_detection_status(
        self, StackDriftDetectionId: str
    ) -> ClientDescribeStackDriftDetectionStatusResponseTypeDef:
        """
        [Client.describe_stack_drift_detection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_drift_detection_status)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stack_events(
        self, StackName: str = None, NextToken: str = None
    ) -> ClientDescribeStackEventsResponseTypeDef:
        """
        [Client.describe_stack_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_events)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stack_instance(
        self, StackSetName: str, StackInstanceAccount: str, StackInstanceRegion: str
    ) -> ClientDescribeStackInstanceResponseTypeDef:
        """
        [Client.describe_stack_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_instance)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stack_resource(
        self, StackName: str, LogicalResourceId: str
    ) -> ClientDescribeStackResourceResponseTypeDef:
        """
        [Client.describe_stack_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stack_resource_drifts(
        self,
        StackName: str,
        StackResourceDriftStatusFilters: List[
            Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"]
        ] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeStackResourceDriftsResponseTypeDef:
        """
        [Client.describe_stack_resource_drifts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resource_drifts)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stack_resources(
        self, StackName: str = None, LogicalResourceId: str = None, PhysicalResourceId: str = None
    ) -> ClientDescribeStackResourcesResponseTypeDef:
        """
        [Client.describe_stack_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stack_set(self, StackSetName: str) -> ClientDescribeStackSetResponseTypeDef:
        """
        [Client.describe_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stack_set_operation(
        self, StackSetName: str, OperationId: str
    ) -> ClientDescribeStackSetOperationResponseTypeDef:
        """
        [Client.describe_stack_set_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_set_operation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stacks(
        self, StackName: str = None, NextToken: str = None
    ) -> ClientDescribeStacksResponseTypeDef:
        """
        [Client.describe_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_stacks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_type(
        self, Type: str = None, TypeName: str = None, Arn: str = None, VersionId: str = None
    ) -> ClientDescribeTypeResponseTypeDef:
        """
        [Client.describe_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_type_registration(
        self, RegistrationToken: str
    ) -> ClientDescribeTypeRegistrationResponseTypeDef:
        """
        [Client.describe_type_registration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.describe_type_registration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_stack_drift(
        self, StackName: str, LogicalResourceIds: List[str] = None
    ) -> ClientDetectStackDriftResponseTypeDef:
        """
        [Client.detect_stack_drift documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_drift)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_stack_resource_drift(
        self, StackName: str, LogicalResourceId: str
    ) -> ClientDetectStackResourceDriftResponseTypeDef:
        """
        [Client.detect_stack_resource_drift documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_resource_drift)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_stack_set_drift(
        self,
        StackSetName: str,
        OperationPreferences: ClientDetectStackSetDriftOperationPreferencesTypeDef = None,
        OperationId: str = None,
    ) -> ClientDetectStackSetDriftResponseTypeDef:
        """
        [Client.detect_stack_set_drift documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_set_drift)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def estimate_template_cost(
        self,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List[ClientEstimateTemplateCostParametersTypeDef] = None,
    ) -> ClientEstimateTemplateCostResponseTypeDef:
        """
        [Client.estimate_template_cost documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.estimate_template_cost)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def execute_change_set(
        self, ChangeSetName: str, StackName: str = None, ClientRequestToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.execute_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.execute_change_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_stack_policy(self, StackName: str) -> ClientGetStackPolicyResponseTypeDef:
        """
        [Client.get_stack_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.get_stack_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_template(
        self,
        StackName: str = None,
        ChangeSetName: str = None,
        TemplateStage: Literal["Original", "Processed"] = None,
    ) -> ClientGetTemplateResponseTypeDef:
        """
        [Client.get_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.get_template)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_template_summary(
        self,
        TemplateBody: str = None,
        TemplateURL: str = None,
        StackName: str = None,
        StackSetName: str = None,
    ) -> ClientGetTemplateSummaryResponseTypeDef:
        """
        [Client.get_template_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.get_template_summary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_change_sets(
        self, StackName: str, NextToken: str = None
    ) -> ClientListChangeSetsResponseTypeDef:
        """
        [Client.list_change_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_change_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_exports(self, NextToken: str = None) -> ClientListExportsResponseTypeDef:
        """
        [Client.list_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_exports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_imports(
        self, ExportName: str, NextToken: str = None
    ) -> ClientListImportsResponseTypeDef:
        """
        [Client.list_imports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_imports)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_stack_instances(
        self,
        StackSetName: str,
        NextToken: str = None,
        MaxResults: int = None,
        StackInstanceAccount: str = None,
        StackInstanceRegion: str = None,
    ) -> ClientListStackInstancesResponseTypeDef:
        """
        [Client.list_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_stack_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_stack_resources(
        self, StackName: str, NextToken: str = None
    ) -> ClientListStackResourcesResponseTypeDef:
        """
        [Client.list_stack_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_stack_resources)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_stack_set_operation_results(
        self, StackSetName: str, OperationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListStackSetOperationResultsResponseTypeDef:
        """
        [Client.list_stack_set_operation_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_stack_set_operation_results)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_stack_set_operations(
        self, StackSetName: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListStackSetOperationsResponseTypeDef:
        """
        [Client.list_stack_set_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_stack_set_operations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_stack_sets(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Status: Literal["ACTIVE", "DELETED"] = None,
    ) -> ClientListStackSetsResponseTypeDef:
        """
        [Client.list_stack_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_stack_sets)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_stacks(
        self,
        NextToken: str = None,
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
    ) -> ClientListStacksResponseTypeDef:
        """
        [Client.list_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_stacks)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_type_registrations(
        self,
        Type: str = None,
        TypeName: str = None,
        TypeArn: str = None,
        RegistrationStatusFilter: Literal["COMPLETE", "IN_PROGRESS", "FAILED"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListTypeRegistrationsResponseTypeDef:
        """
        [Client.list_type_registrations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_type_registrations)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_type_versions(
        self,
        Type: str = None,
        TypeName: str = None,
        Arn: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        DeprecatedStatus: Literal["LIVE", "DEPRECATED"] = None,
    ) -> ClientListTypeVersionsResponseTypeDef:
        """
        [Client.list_type_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_type_versions)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_types(
        self,
        Visibility: Literal["PUBLIC", "PRIVATE"] = None,
        ProvisioningType: Literal["NON_PROVISIONABLE", "IMMUTABLE", "FULLY_MUTABLE"] = None,
        DeprecatedStatus: Literal["LIVE", "DEPRECATED"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListTypesResponseTypeDef:
        """
        [Client.list_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.list_types)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def record_handler_progress(
        self,
        BearerToken: str,
        OperationStatus: Literal["PENDING", "IN_PROGRESS", "SUCCESS", "FAILED"],
        CurrentOperationStatus: Literal["PENDING", "IN_PROGRESS", "SUCCESS", "FAILED"] = None,
        StatusMessage: str = None,
        ErrorCode: Literal[
            "NotUpdatable",
            "InvalidRequest",
            "AccessDenied",
            "InvalidCredentials",
            "AlreadyExists",
            "NotFound",
            "ResourceConflict",
            "Throttling",
            "ServiceLimitExceeded",
            "NotStabilized",
            "GeneralServiceException",
            "ServiceInternalError",
            "NetworkFailure",
            "InternalFailure",
        ] = None,
        ResourceModel: str = None,
        ClientRequestToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.record_handler_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.record_handler_progress)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_type(
        self,
        TypeName: str,
        SchemaHandlerPackage: str,
        Type: str = None,
        LoggingConfig: ClientRegisterTypeLoggingConfigTypeDef = None,
        ExecutionRoleArn: str = None,
        ClientRequestToken: str = None,
    ) -> ClientRegisterTypeResponseTypeDef:
        """
        [Client.register_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.register_type)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_stack_policy(
        self, StackName: str, StackPolicyBody: str = None, StackPolicyURL: str = None
    ) -> None:
        """
        [Client.set_stack_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.set_stack_policy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_type_default_version(
        self, Arn: str = None, Type: str = None, TypeName: str = None, VersionId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.set_type_default_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.set_type_default_version)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def signal_resource(
        self,
        StackName: str,
        LogicalResourceId: str,
        UniqueId: str,
        Status: Literal["SUCCESS", "FAILURE"],
    ) -> None:
        """
        [Client.signal_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.signal_resource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_stack_set_operation(self, StackSetName: str, OperationId: str) -> Dict[str, Any]:
        """
        [Client.stop_stack_set_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.stop_stack_set_operation)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_stack(
        self,
        StackName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        StackPolicyDuringUpdateBody: str = None,
        StackPolicyDuringUpdateURL: str = None,
        Parameters: List[ClientUpdateStackParametersTypeDef] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        RollbackConfiguration: ClientUpdateStackRollbackConfigurationTypeDef = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        NotificationARNs: List[str] = None,
        Tags: List[ClientUpdateStackTagsTypeDef] = None,
        ClientRequestToken: str = None,
    ) -> ClientUpdateStackResponseTypeDef:
        """
        [Client.update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.update_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_stack_instances(
        self,
        StackSetName: str,
        Accounts: List[str],
        Regions: List[str],
        ParameterOverrides: List[ClientUpdateStackInstancesParameterOverridesTypeDef] = None,
        OperationPreferences: ClientUpdateStackInstancesOperationPreferencesTypeDef = None,
        OperationId: str = None,
    ) -> ClientUpdateStackInstancesResponseTypeDef:
        """
        [Client.update_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.update_stack_instances)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_stack_set(
        self,
        StackSetName: str,
        Description: str = None,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        Parameters: List[ClientUpdateStackSetParametersTypeDef] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        Tags: List[ClientUpdateStackSetTagsTypeDef] = None,
        OperationPreferences: ClientUpdateStackSetOperationPreferencesTypeDef = None,
        AdministrationRoleARN: str = None,
        ExecutionRoleName: str = None,
        OperationId: str = None,
        Accounts: List[str] = None,
        Regions: List[str] = None,
    ) -> ClientUpdateStackSetResponseTypeDef:
        """
        [Client.update_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.update_stack_set)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_termination_protection(
        self, EnableTerminationProtection: bool, StackName: str
    ) -> ClientUpdateTerminationProtectionResponseTypeDef:
        """
        [Client.update_termination_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.update_termination_protection)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def validate_template(
        self, TemplateBody: str = None, TemplateURL: str = None
    ) -> ClientValidateTemplateResponseTypeDef:
        """
        [Client.validate_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Client.validate_template)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_account_limits"]
    ) -> paginator_scope.DescribeAccountLimitsPaginator:
        """
        [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_change_set"]
    ) -> paginator_scope.DescribeChangeSetPaginator:
        """
        [Paginator.DescribeChangeSet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_stack_events"]
    ) -> paginator_scope.DescribeStackEventsPaginator:
        """
        [Paginator.DescribeStackEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_stacks"]
    ) -> paginator_scope.DescribeStacksPaginator:
        """
        [Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_change_sets"]
    ) -> paginator_scope.ListChangeSetsPaginator:
        """
        [Paginator.ListChangeSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_exports"]
    ) -> paginator_scope.ListExportsPaginator:
        """
        [Paginator.ListExports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_imports"]
    ) -> paginator_scope.ListImportsPaginator:
        """
        [Paginator.ListImports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_stack_instances"]
    ) -> paginator_scope.ListStackInstancesPaginator:
        """
        [Paginator.ListStackInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_stack_resources"]
    ) -> paginator_scope.ListStackResourcesPaginator:
        """
        [Paginator.ListStackResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_stack_set_operation_results"]
    ) -> paginator_scope.ListStackSetOperationResultsPaginator:
        """
        [Paginator.ListStackSetOperationResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_stack_set_operations"]
    ) -> paginator_scope.ListStackSetOperationsPaginator:
        """
        [Paginator.ListStackSetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_stack_sets"]
    ) -> paginator_scope.ListStackSetsPaginator:
        """
        [Paginator.ListStackSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_stacks"]
    ) -> paginator_scope.ListStacksPaginator:
        """
        [Paginator.ListStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["change_set_create_complete"]
    ) -> waiter_scope.ChangeSetCreateCompleteWaiter:
        """
        [Waiter.ChangeSetCreateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.ChangeSetCreateComplete)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["stack_create_complete"]
    ) -> waiter_scope.StackCreateCompleteWaiter:
        """
        [Waiter.StackCreateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.StackCreateComplete)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["stack_delete_complete"]
    ) -> waiter_scope.StackDeleteCompleteWaiter:
        """
        [Waiter.StackDeleteComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.StackDeleteComplete)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: Literal["stack_exists"]) -> waiter_scope.StackExistsWaiter:
        """
        [Waiter.StackExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.StackExists)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["stack_import_complete"]
    ) -> waiter_scope.StackImportCompleteWaiter:
        """
        [Waiter.StackImportComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.StackImportComplete)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["stack_update_complete"]
    ) -> waiter_scope.StackUpdateCompleteWaiter:
        """
        [Waiter.StackUpdateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.StackUpdateComplete)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["type_registration_complete"]
    ) -> waiter_scope.TypeRegistrationCompleteWaiter:
        """
        [Waiter.TypeRegistrationComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Waiter.TypeRegistrationComplete)
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    CFNRegistryException: Boto3ClientError
    ChangeSetNotFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    CreatedButModifiedException: Boto3ClientError
    InsufficientCapabilitiesException: Boto3ClientError
    InvalidChangeSetStatusException: Boto3ClientError
    InvalidOperationException: Boto3ClientError
    InvalidStateTransitionException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NameAlreadyExistsException: Boto3ClientError
    OperationIdAlreadyExistsException: Boto3ClientError
    OperationInProgressException: Boto3ClientError
    OperationNotFoundException: Boto3ClientError
    OperationStatusCheckFailedException: Boto3ClientError
    StackInstanceNotFoundException: Boto3ClientError
    StackSetNotEmptyException: Boto3ClientError
    StackSetNotFoundException: Boto3ClientError
    StaleRequestException: Boto3ClientError
    TokenAlreadyExistsException: Boto3ClientError
    TypeNotFoundException: Boto3ClientError
