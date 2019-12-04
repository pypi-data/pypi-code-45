"Main interface for cloudformation service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ChangeSetCreateCompleteWaitWaiterConfigTypeDef",
    "ClientCreateChangeSetParametersTypeDef",
    "ClientCreateChangeSetResourcesToImportTypeDef",
    "ClientCreateChangeSetResponseTypeDef",
    "ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    "ClientCreateChangeSetRollbackConfigurationTypeDef",
    "ClientCreateChangeSetTagsTypeDef",
    "ClientCreateStackInstancesOperationPreferencesTypeDef",
    "ClientCreateStackInstancesParameterOverridesTypeDef",
    "ClientCreateStackInstancesResponseTypeDef",
    "ClientCreateStackParametersTypeDef",
    "ClientCreateStackResponseTypeDef",
    "ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    "ClientCreateStackRollbackConfigurationTypeDef",
    "ClientCreateStackSetParametersTypeDef",
    "ClientCreateStackSetResponseTypeDef",
    "ClientCreateStackSetTagsTypeDef",
    "ClientCreateStackTagsTypeDef",
    "ClientDeleteStackInstancesOperationPreferencesTypeDef",
    "ClientDeleteStackInstancesResponseTypeDef",
    "ClientDescribeAccountLimitsResponseAccountLimitsTypeDef",
    "ClientDescribeAccountLimitsResponseTypeDef",
    "ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef",
    "ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef",
    "ClientDescribeChangeSetResponseChangesResourceChangeTypeDef",
    "ClientDescribeChangeSetResponseChangesTypeDef",
    "ClientDescribeChangeSetResponseParametersTypeDef",
    "ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef",
    "ClientDescribeChangeSetResponseRollbackConfigurationTypeDef",
    "ClientDescribeChangeSetResponseTagsTypeDef",
    "ClientDescribeChangeSetResponseTypeDef",
    "ClientDescribeStackDriftDetectionStatusResponseTypeDef",
    "ClientDescribeStackEventsResponseStackEventsTypeDef",
    "ClientDescribeStackEventsResponseTypeDef",
    "ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef",
    "ClientDescribeStackInstanceResponseStackInstanceTypeDef",
    "ClientDescribeStackInstanceResponseTypeDef",
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef",
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef",
    "ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef",
    "ClientDescribeStackResourceDriftsResponseTypeDef",
    "ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef",
    "ClientDescribeStackResourceResponseStackResourceDetailTypeDef",
    "ClientDescribeStackResourceResponseTypeDef",
    "ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef",
    "ClientDescribeStackResourcesResponseStackResourcesTypeDef",
    "ClientDescribeStackResourcesResponseTypeDef",
    "ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef",
    "ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef",
    "ClientDescribeStackSetOperationResponseStackSetOperationTypeDef",
    "ClientDescribeStackSetOperationResponseTypeDef",
    "ClientDescribeStackSetResponseStackSetParametersTypeDef",
    "ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef",
    "ClientDescribeStackSetResponseStackSetTagsTypeDef",
    "ClientDescribeStackSetResponseStackSetTypeDef",
    "ClientDescribeStackSetResponseTypeDef",
    "ClientDescribeStacksResponseStacksDriftInformationTypeDef",
    "ClientDescribeStacksResponseStacksOutputsTypeDef",
    "ClientDescribeStacksResponseStacksParametersTypeDef",
    "ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    "ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef",
    "ClientDescribeStacksResponseStacksTagsTypeDef",
    "ClientDescribeStacksResponseStacksTypeDef",
    "ClientDescribeStacksResponseTypeDef",
    "ClientDescribeTypeRegistrationResponseTypeDef",
    "ClientDescribeTypeResponseLoggingConfigTypeDef",
    "ClientDescribeTypeResponseTypeDef",
    "ClientDetectStackDriftResponseTypeDef",
    "ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef",
    "ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef",
    "ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef",
    "ClientDetectStackResourceDriftResponseTypeDef",
    "ClientDetectStackSetDriftOperationPreferencesTypeDef",
    "ClientDetectStackSetDriftResponseTypeDef",
    "ClientEstimateTemplateCostParametersTypeDef",
    "ClientEstimateTemplateCostResponseTypeDef",
    "ClientGetStackPolicyResponseTypeDef",
    "ClientGetTemplateResponseTypeDef",
    "ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef",
    "ClientGetTemplateSummaryResponseParametersTypeDef",
    "ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef",
    "ClientGetTemplateSummaryResponseTypeDef",
    "ClientListChangeSetsResponseSummariesTypeDef",
    "ClientListChangeSetsResponseTypeDef",
    "ClientListExportsResponseExportsTypeDef",
    "ClientListExportsResponseTypeDef",
    "ClientListImportsResponseTypeDef",
    "ClientListStackInstancesResponseSummariesTypeDef",
    "ClientListStackInstancesResponseTypeDef",
    "ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef",
    "ClientListStackResourcesResponseStackResourceSummariesTypeDef",
    "ClientListStackResourcesResponseTypeDef",
    "ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef",
    "ClientListStackSetOperationResultsResponseSummariesTypeDef",
    "ClientListStackSetOperationResultsResponseTypeDef",
    "ClientListStackSetOperationsResponseSummariesTypeDef",
    "ClientListStackSetOperationsResponseTypeDef",
    "ClientListStackSetsResponseSummariesTypeDef",
    "ClientListStackSetsResponseTypeDef",
    "ClientListStacksResponseStackSummariesDriftInformationTypeDef",
    "ClientListStacksResponseStackSummariesTypeDef",
    "ClientListStacksResponseTypeDef",
    "ClientListTypeRegistrationsResponseTypeDef",
    "ClientListTypeVersionsResponseTypeVersionSummariesTypeDef",
    "ClientListTypeVersionsResponseTypeDef",
    "ClientListTypesResponseTypeSummariesTypeDef",
    "ClientListTypesResponseTypeDef",
    "ClientRegisterTypeLoggingConfigTypeDef",
    "ClientRegisterTypeResponseTypeDef",
    "ClientUpdateStackInstancesOperationPreferencesTypeDef",
    "ClientUpdateStackInstancesParameterOverridesTypeDef",
    "ClientUpdateStackInstancesResponseTypeDef",
    "ClientUpdateStackParametersTypeDef",
    "ClientUpdateStackResponseTypeDef",
    "ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef",
    "ClientUpdateStackRollbackConfigurationTypeDef",
    "ClientUpdateStackSetOperationPreferencesTypeDef",
    "ClientUpdateStackSetParametersTypeDef",
    "ClientUpdateStackSetResponseTypeDef",
    "ClientUpdateStackSetTagsTypeDef",
    "ClientUpdateStackTagsTypeDef",
    "ClientUpdateTerminationProtectionResponseTypeDef",
    "ClientValidateTemplateResponseParametersTypeDef",
    "ClientValidateTemplateResponseTypeDef",
    "DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    "DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef",
    "DescribeAccountLimitsPaginateResponseTypeDef",
    "DescribeChangeSetPaginatePaginationConfigTypeDef",
    "DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef",
    "DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef",
    "DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef",
    "DescribeChangeSetPaginateResponseChangesTypeDef",
    "DescribeChangeSetPaginateResponseParametersTypeDef",
    "DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef",
    "DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef",
    "DescribeChangeSetPaginateResponseTagsTypeDef",
    "DescribeChangeSetPaginateResponseTypeDef",
    "DescribeStackEventsPaginatePaginationConfigTypeDef",
    "DescribeStackEventsPaginateResponseStackEventsTypeDef",
    "DescribeStackEventsPaginateResponseTypeDef",
    "DescribeStacksPaginatePaginationConfigTypeDef",
    "DescribeStacksPaginateResponseStacksDriftInformationTypeDef",
    "DescribeStacksPaginateResponseStacksOutputsTypeDef",
    "DescribeStacksPaginateResponseStacksParametersTypeDef",
    "DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    "DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef",
    "DescribeStacksPaginateResponseStacksTagsTypeDef",
    "DescribeStacksPaginateResponseStacksTypeDef",
    "DescribeStacksPaginateResponseTypeDef",
    "ListChangeSetsPaginatePaginationConfigTypeDef",
    "ListChangeSetsPaginateResponseSummariesTypeDef",
    "ListChangeSetsPaginateResponseTypeDef",
    "ListExportsPaginatePaginationConfigTypeDef",
    "ListExportsPaginateResponseExportsTypeDef",
    "ListExportsPaginateResponseTypeDef",
    "ListImportsPaginatePaginationConfigTypeDef",
    "ListImportsPaginateResponseTypeDef",
    "ListStackInstancesPaginatePaginationConfigTypeDef",
    "ListStackInstancesPaginateResponseSummariesTypeDef",
    "ListStackInstancesPaginateResponseTypeDef",
    "ListStackResourcesPaginatePaginationConfigTypeDef",
    "ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef",
    "ListStackResourcesPaginateResponseStackResourceSummariesTypeDef",
    "ListStackResourcesPaginateResponseTypeDef",
    "ListStackSetOperationResultsPaginatePaginationConfigTypeDef",
    "ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef",
    "ListStackSetOperationResultsPaginateResponseSummariesTypeDef",
    "ListStackSetOperationResultsPaginateResponseTypeDef",
    "ListStackSetOperationsPaginatePaginationConfigTypeDef",
    "ListStackSetOperationsPaginateResponseSummariesTypeDef",
    "ListStackSetOperationsPaginateResponseTypeDef",
    "ListStackSetsPaginatePaginationConfigTypeDef",
    "ListStackSetsPaginateResponseSummariesTypeDef",
    "ListStackSetsPaginateResponseTypeDef",
    "ListStacksPaginatePaginationConfigTypeDef",
    "ListStacksPaginateResponseStackSummariesDriftInformationTypeDef",
    "ListStacksPaginateResponseStackSummariesTypeDef",
    "ListStacksPaginateResponseTypeDef",
    "ServiceResourceCreateStackParametersTypeDef",
    "ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    "ServiceResourceCreateStackRollbackConfigurationTypeDef",
    "ServiceResourceCreateStackTagsTypeDef",
    "StackCreateCompleteWaitWaiterConfigTypeDef",
    "StackDeleteCompleteWaitWaiterConfigTypeDef",
    "StackExistsWaitWaiterConfigTypeDef",
    "StackImportCompleteWaitWaiterConfigTypeDef",
    "StackUpdateCompleteWaitWaiterConfigTypeDef",
    "StackUpdateParametersTypeDef",
    "StackUpdateResponseTypeDef",
    "StackUpdateRollbackConfigurationRollbackTriggersTypeDef",
    "StackUpdateRollbackConfigurationTypeDef",
    "StackUpdateTagsTypeDef",
    "TypeRegistrationCompleteWaitWaiterConfigTypeDef",
)


_ChangeSetCreateCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_ChangeSetCreateCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class ChangeSetCreateCompleteWaitWaiterConfigTypeDef(
    _ChangeSetCreateCompleteWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_ClientCreateChangeSetParametersTypeDef = TypedDict(
    "_ClientCreateChangeSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientCreateChangeSetParametersTypeDef(_ClientCreateChangeSetParametersTypeDef):
    """
    - *(dict) --*

      The Parameter data type.
      - **ParameterKey** *(string) --*

        The key associated with the parameter. If you don't specify a key and value for a particular
        parameter, AWS CloudFormation uses the default value that is specified in your template.
    """


_RequiredClientCreateChangeSetResourcesToImportTypeDef = TypedDict(
    "_RequiredClientCreateChangeSetResourcesToImportTypeDef", {"ResourceType": str}
)
_OptionalClientCreateChangeSetResourcesToImportTypeDef = TypedDict(
    "_OptionalClientCreateChangeSetResourcesToImportTypeDef",
    {"LogicalResourceId": str, "ResourceIdentifier": Dict[str, str]},
    total=False,
)


class ClientCreateChangeSetResourcesToImportTypeDef(
    _RequiredClientCreateChangeSetResourcesToImportTypeDef,
    _OptionalClientCreateChangeSetResourcesToImportTypeDef,
):
    """
    - *(dict) --*

      Describes the target resource of an import operation.
      - **ResourceType** *(string) --***[REQUIRED]**

        The type of resource to import into your stack, such as ``AWS::S3::Bucket`` .
    """


_ClientCreateChangeSetResponseTypeDef = TypedDict(
    "_ClientCreateChangeSetResponseTypeDef", {"Id": str, "StackId": str}, total=False
)


class ClientCreateChangeSetResponseTypeDef(_ClientCreateChangeSetResponseTypeDef):
    """
    - *(dict) --*

      The output for the  CreateChangeSet action.
      - **Id** *(string) --*

        The Amazon Resource Name (ARN) of the change set.
    """


_RequiredClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef,
):
    """
    - *(dict) --*

      A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
      of the alarms you specify goes to ALARM state during the stack operation or within the
      specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.
      - **Arn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the rollback trigger.
        If a specified trigger is missing, the entire stack operation fails and is rolled back.
    """


_ClientCreateChangeSetRollbackConfigurationTypeDef = TypedDict(
    "_ClientCreateChangeSetRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[ClientCreateChangeSetRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ClientCreateChangeSetRollbackConfigurationTypeDef(
    _ClientCreateChangeSetRollbackConfigurationTypeDef
):
    """
    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.
    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.
      By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies
      them to any subsequent update operations for the stack, unless you specify otherwise. If you
      do specify rollback triggers for this parameter, those triggers replace any list of triggers
      previously specified for the stack. This means:
      * To use the rollback triggers previously specified for this stack, if any, don't specify this
      parameter.
      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating the
      stack or during a previous stack update). Any triggers that you don't include in the updated
      list of triggers are no longer applied to the stack.
      * To remove all currently specified triggers, specify an empty list for this parameter.
      If a specified trigger is missing, the entire stack operation fails and is rolled back.
      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
        any of the alarms you specify goes to ALARM state during the stack operation or within the
        specified monitoring period afterwards, CloudFormation rolls back the entire stack
        operation.
        - **Arn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the rollback trigger.
          If a specified trigger is missing, the entire stack operation fails and is rolled back.
    """


_RequiredClientCreateChangeSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateChangeSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateChangeSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateChangeSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateChangeSetTagsTypeDef(
    _RequiredClientCreateChangeSetTagsTypeDef, _OptionalClientCreateChangeSetTagsTypeDef
):
    """
    - *(dict) --*

      The Tag type enables you to specify a key-value pair that can be used to store information
      about an AWS CloudFormation stack.
      - **Key** *(string) --***[REQUIRED]**

        *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
        for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
    """


_ClientCreateStackInstancesOperationPreferencesTypeDef = TypedDict(
    "_ClientCreateStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientCreateStackInstancesOperationPreferencesTypeDef(
    _ClientCreateStackInstancesOperationPreferencesTypeDef
):
    """
    Preferences for how AWS CloudFormation performs this stack set operation.
    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.
      - *(string) --*
    """


_ClientCreateStackInstancesParameterOverridesTypeDef = TypedDict(
    "_ClientCreateStackInstancesParameterOverridesTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientCreateStackInstancesParameterOverridesTypeDef(
    _ClientCreateStackInstancesParameterOverridesTypeDef
):
    pass


_ClientCreateStackInstancesResponseTypeDef = TypedDict(
    "_ClientCreateStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)


class ClientCreateStackInstancesResponseTypeDef(_ClientCreateStackInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        The unique identifier for this stack set operation.
    """


_ClientCreateStackParametersTypeDef = TypedDict(
    "_ClientCreateStackParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientCreateStackParametersTypeDef(_ClientCreateStackParametersTypeDef):
    """
    - *(dict) --*

      The Parameter data type.
      - **ParameterKey** *(string) --*

        The key associated with the parameter. If you don't specify a key and value for a particular
        parameter, AWS CloudFormation uses the default value that is specified in your template.
    """


_ClientCreateStackResponseTypeDef = TypedDict(
    "_ClientCreateStackResponseTypeDef", {"StackId": str}, total=False
)


class ClientCreateStackResponseTypeDef(_ClientCreateStackResponseTypeDef):
    """
    - *(dict) --*

      The output for a  CreateStack action.
      - **StackId** *(string) --*

        Unique identifier of the stack.
    """


_RequiredClientCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredClientCreateStackRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalClientCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalClientCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredClientCreateStackRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalClientCreateStackRollbackConfigurationRollbackTriggersTypeDef,
):
    """
    - *(dict) --*

      A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
      of the alarms you specify goes to ALARM state during the stack operation or within the
      specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.
      - **Arn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the rollback trigger.
        If a specified trigger is missing, the entire stack operation fails and is rolled back.
    """


_ClientCreateStackRollbackConfigurationTypeDef = TypedDict(
    "_ClientCreateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[ClientCreateStackRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ClientCreateStackRollbackConfigurationTypeDef(_ClientCreateStackRollbackConfigurationTypeDef):
    """
    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.
    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.
      By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies
      them to any subsequent update operations for the stack, unless you specify otherwise. If you
      do specify rollback triggers for this parameter, those triggers replace any list of triggers
      previously specified for the stack. This means:
      * To use the rollback triggers previously specified for this stack, if any, don't specify this
      parameter.
      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating the
      stack or during a previous stack update). Any triggers that you don't include in the updated
      list of triggers are no longer applied to the stack.
      * To remove all currently specified triggers, specify an empty list for this parameter.
      If a specified trigger is missing, the entire stack operation fails and is rolled back.
      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
        any of the alarms you specify goes to ALARM state during the stack operation or within the
        specified monitoring period afterwards, CloudFormation rolls back the entire stack
        operation.
        - **Arn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the rollback trigger.
          If a specified trigger is missing, the entire stack operation fails and is rolled back.
    """


_ClientCreateStackSetParametersTypeDef = TypedDict(
    "_ClientCreateStackSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientCreateStackSetParametersTypeDef(_ClientCreateStackSetParametersTypeDef):
    """
    - *(dict) --*

      The Parameter data type.
      - **ParameterKey** *(string) --*

        The key associated with the parameter. If you don't specify a key and value for a particular
        parameter, AWS CloudFormation uses the default value that is specified in your template.
    """


_ClientCreateStackSetResponseTypeDef = TypedDict(
    "_ClientCreateStackSetResponseTypeDef", {"StackSetId": str}, total=False
)


class ClientCreateStackSetResponseTypeDef(_ClientCreateStackSetResponseTypeDef):
    """
    - *(dict) --*

      - **StackSetId** *(string) --*

        The ID of the stack set that you're creating.
    """


_RequiredClientCreateStackSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateStackSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateStackSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateStackSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateStackSetTagsTypeDef(
    _RequiredClientCreateStackSetTagsTypeDef, _OptionalClientCreateStackSetTagsTypeDef
):
    """
    - *(dict) --*

      The Tag type enables you to specify a key-value pair that can be used to store information
      about an AWS CloudFormation stack.
      - **Key** *(string) --***[REQUIRED]**

        *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
        for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
    """


_RequiredClientCreateStackTagsTypeDef = TypedDict(
    "_RequiredClientCreateStackTagsTypeDef", {"Key": str}
)
_OptionalClientCreateStackTagsTypeDef = TypedDict(
    "_OptionalClientCreateStackTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateStackTagsTypeDef(
    _RequiredClientCreateStackTagsTypeDef, _OptionalClientCreateStackTagsTypeDef
):
    """
    - *(dict) --*

      The Tag type enables you to specify a key-value pair that can be used to store information
      about an AWS CloudFormation stack.
      - **Key** *(string) --***[REQUIRED]**

        *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
        for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
    """


_ClientDeleteStackInstancesOperationPreferencesTypeDef = TypedDict(
    "_ClientDeleteStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientDeleteStackInstancesOperationPreferencesTypeDef(
    _ClientDeleteStackInstancesOperationPreferencesTypeDef
):
    """
    Preferences for how AWS CloudFormation performs this stack set operation.
    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.
      - *(string) --*
    """


_ClientDeleteStackInstancesResponseTypeDef = TypedDict(
    "_ClientDeleteStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)


class ClientDeleteStackInstancesResponseTypeDef(_ClientDeleteStackInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        The unique identifier for this stack set operation.
    """


_ClientDescribeAccountLimitsResponseAccountLimitsTypeDef = TypedDict(
    "_ClientDescribeAccountLimitsResponseAccountLimitsTypeDef",
    {"Name": str, "Value": int},
    total=False,
)


class ClientDescribeAccountLimitsResponseAccountLimitsTypeDef(
    _ClientDescribeAccountLimitsResponseAccountLimitsTypeDef
):
    """
    - *(dict) --*

      The AccountLimit data type.
      CloudFormation has the following limits per account:
      * Number of concurrent resources
      * Number of stacks
      * Number of stack outputs
      For more information about these account limits, and other CloudFormation limits, see `AWS
      CloudFormation Limits
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
      in the *AWS CloudFormation User Guide* .
      - **Name** *(string) --*

        The name of the account limit.
        Values: ``ConcurrentResourcesLimit`` | ``StackLimit`` | ``StackOutputsLimit``
    """


_ClientDescribeAccountLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeAccountLimitsResponseTypeDef",
    {
        "AccountLimits": List[ClientDescribeAccountLimitsResponseAccountLimitsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeAccountLimitsResponseTypeDef(_ClientDescribeAccountLimitsResponseTypeDef):
    """
    - *(dict) --*

      The output for the  DescribeAccountLimits action.
      - **AccountLimits** *(list) --*

        An account limit structure that contain a list of AWS CloudFormation account limits and
        their values.
        - *(dict) --*

          The AccountLimit data type.
          CloudFormation has the following limits per account:
          * Number of concurrent resources
          * Number of stacks
          * Number of stack outputs
          For more information about these account limits, and other CloudFormation limits, see `AWS
          CloudFormation Limits
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
          in the *AWS CloudFormation User Guide* .
          - **Name** *(string) --*

            The name of the account limit.
            Values: ``ConcurrentResourcesLimit`` | ``StackLimit`` | ``StackOutputsLimit``
    """


_ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef",
    {
        "Attribute": Literal[
            "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
        ],
        "Name": str,
        "RequiresRecreation": Literal["Never", "Conditionally", "Always"],
    },
    total=False,
)


class ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef(
    _ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef
):
    pass


_ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef",
    {
        "Target": ClientDescribeChangeSetResponseChangesResourceChangeDetailsTargetTypeDef,
        "Evaluation": Literal["Static", "Dynamic"],
        "ChangeSource": Literal[
            "ResourceReference",
            "ParameterReference",
            "ResourceAttribute",
            "DirectModification",
            "Automatic",
        ],
        "CausingEntity": str,
    },
    total=False,
)


class ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef(
    _ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef
):
    pass


_ClientDescribeChangeSetResponseChangesResourceChangeTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseChangesResourceChangeTypeDef",
    {
        "Action": Literal["Add", "Modify", "Remove", "Import"],
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Literal["True", "False", "Conditional"],
        "Scope": List[
            Literal[
                "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
            ]
        ],
        "Details": List[ClientDescribeChangeSetResponseChangesResourceChangeDetailsTypeDef],
    },
    total=False,
)


class ClientDescribeChangeSetResponseChangesResourceChangeTypeDef(
    _ClientDescribeChangeSetResponseChangesResourceChangeTypeDef
):
    pass


_ClientDescribeChangeSetResponseChangesTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseChangesTypeDef",
    {"Type": str, "ResourceChange": ClientDescribeChangeSetResponseChangesResourceChangeTypeDef},
    total=False,
)


class ClientDescribeChangeSetResponseChangesTypeDef(_ClientDescribeChangeSetResponseChangesTypeDef):
    pass


_ClientDescribeChangeSetResponseParametersTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientDescribeChangeSetResponseParametersTypeDef(
    _ClientDescribeChangeSetResponseParametersTypeDef
):
    pass


_ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)


class ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef(
    _ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef
):
    pass


_ClientDescribeChangeSetResponseRollbackConfigurationTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientDescribeChangeSetResponseRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ClientDescribeChangeSetResponseRollbackConfigurationTypeDef(
    _ClientDescribeChangeSetResponseRollbackConfigurationTypeDef
):
    pass


_ClientDescribeChangeSetResponseTagsTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeChangeSetResponseTagsTypeDef(_ClientDescribeChangeSetResponseTagsTypeDef):
    pass


_ClientDescribeChangeSetResponseTypeDef = TypedDict(
    "_ClientDescribeChangeSetResponseTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List[ClientDescribeChangeSetResponseParametersTypeDef],
        "CreationTime": datetime,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": ClientDescribeChangeSetResponseRollbackConfigurationTypeDef,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List[ClientDescribeChangeSetResponseTagsTypeDef],
        "Changes": List[ClientDescribeChangeSetResponseChangesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeChangeSetResponseTypeDef(_ClientDescribeChangeSetResponseTypeDef):
    """
    - *(dict) --*

      The output for the  DescribeChangeSet action.
      - **ChangeSetName** *(string) --*

        The name of the change set.
    """


_ClientDescribeStackDriftDetectionStatusResponseTypeDef = TypedDict(
    "_ClientDescribeStackDriftDetectionStatusResponseTypeDef",
    {
        "StackId": str,
        "StackDriftDetectionId": str,
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "DetectionStatus": Literal[
            "DETECTION_IN_PROGRESS", "DETECTION_FAILED", "DETECTION_COMPLETE"
        ],
        "DetectionStatusReason": str,
        "DriftedStackResourceCount": int,
        "Timestamp": datetime,
    },
    total=False,
)


class ClientDescribeStackDriftDetectionStatusResponseTypeDef(
    _ClientDescribeStackDriftDetectionStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **StackId** *(string) --*

        The ID of the stack.
    """


_ClientDescribeStackEventsResponseStackEventsTypeDef = TypedDict(
    "_ClientDescribeStackEventsResponseStackEventsTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class ClientDescribeStackEventsResponseStackEventsTypeDef(
    _ClientDescribeStackEventsResponseStackEventsTypeDef
):
    """
    - *(dict) --*

      The StackEvent data type.
      - **StackId** *(string) --*

        The unique ID name of the instance of the stack.
    """


_ClientDescribeStackEventsResponseTypeDef = TypedDict(
    "_ClientDescribeStackEventsResponseTypeDef",
    {"StackEvents": List[ClientDescribeStackEventsResponseStackEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeStackEventsResponseTypeDef(_ClientDescribeStackEventsResponseTypeDef):
    """
    - *(dict) --*

      The output for a  DescribeStackEvents action.
      - **StackEvents** *(list) --*

        A list of ``StackEvents`` structures.
        - *(dict) --*

          The StackEvent data type.
          - **StackId** *(string) --*

            The unique ID name of the instance of the stack.
    """


_ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef = TypedDict(
    "_ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef(
    _ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef
):
    pass


_ClientDescribeStackInstanceResponseStackInstanceTypeDef = TypedDict(
    "_ClientDescribeStackInstanceResponseStackInstanceTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "ParameterOverrides": List[
            ClientDescribeStackInstanceResponseStackInstanceParameterOverridesTypeDef
        ],
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StatusReason": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeStackInstanceResponseStackInstanceTypeDef(
    _ClientDescribeStackInstanceResponseStackInstanceTypeDef
):
    """
    - **StackInstance** *(dict) --*

      The stack instance that matches the specified request parameters.
      - **StackSetId** *(string) --*

        The name or unique ID of the stack set that the stack instance is associated with.
    """


_ClientDescribeStackInstanceResponseTypeDef = TypedDict(
    "_ClientDescribeStackInstanceResponseTypeDef",
    {"StackInstance": ClientDescribeStackInstanceResponseStackInstanceTypeDef},
    total=False,
)


class ClientDescribeStackInstanceResponseTypeDef(_ClientDescribeStackInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **StackInstance** *(dict) --*

        The stack instance that matches the specified request parameters.
        - **StackSetId** *(string) --*

          The name or unique ID of the stack set that the stack instance is associated with.
    """


_ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef = TypedDict(
    "_ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef(
    _ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef
):
    pass


_ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef = TypedDict(
    "_ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": Literal["ADD", "REMOVE", "NOT_EQUAL"],
    },
    total=False,
)


class ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef(
    _ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef
):
    pass


_ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef = TypedDict(
    "_ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsPhysicalResourceIdContextTypeDef
        ],
        "ResourceType": str,
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsPropertyDifferencesTypeDef
        ],
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "Timestamp": datetime,
    },
    total=False,
)


class ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef(
    _ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef
):
    """
    - *(dict) --*

      Contains the drift information for a resource that has been checked for drift. This includes
      actual and expected property values for resources in which AWS CloudFormation has detected
      drift. Only resource properties explicitly defined in the stack template are checked for
      drift. For more information, see `Detecting Unregulated Configuration Changes to Stacks and
      Resources
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
      .
      Resources that do not currently support drift detection cannot be checked. For a list of
      resources that support drift detection, see `Resources that Support Drift Detection
      <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
      .
      Use  DetectStackResourceDrift to detect drift on individual resources, or  DetectStackDrift to
      detect drift on all resources in a given stack that support drift detection.
      - **StackId** *(string) --*

        The ID of the stack.
    """


_ClientDescribeStackResourceDriftsResponseTypeDef = TypedDict(
    "_ClientDescribeStackResourceDriftsResponseTypeDef",
    {
        "StackResourceDrifts": List[
            ClientDescribeStackResourceDriftsResponseStackResourceDriftsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeStackResourceDriftsResponseTypeDef(
    _ClientDescribeStackResourceDriftsResponseTypeDef
):
    """
    - *(dict) --*

      - **StackResourceDrifts** *(list) --*

        Drift information for the resources that have been checked for drift in the specified stack.
        This includes actual and expected configuration values for resources where AWS
        CloudFormation detects drift.
        For a given stack, there will be one ``StackResourceDrift`` for each stack resource that has
        been checked for drift. Resources that have not yet been checked for drift are not included.
        Resources that do not currently support drift detection are not checked, and so not
        included. For a list of resources that support drift detection, see `Resources that Support
        Drift Detection
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
        .
        - *(dict) --*

          Contains the drift information for a resource that has been checked for drift. This
          includes actual and expected property values for resources in which AWS CloudFormation has
          detected drift. Only resource properties explicitly defined in the stack template are
          checked for drift. For more information, see `Detecting Unregulated Configuration Changes
          to Stacks and Resources
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__
          .
          Resources that do not currently support drift detection cannot be checked. For a list of
          resources that support drift detection, see `Resources that Support Drift Detection
          <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__
          .
          Use  DetectStackResourceDrift to detect drift on individual resources, or
          DetectStackDrift to detect drift on all resources in a given stack that support drift
          detection.
          - **StackId** *(string) --*

            The ID of the stack.
    """


_ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef = TypedDict(
    "_ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef(
    _ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef
):
    pass


_ClientDescribeStackResourceResponseStackResourceDetailTypeDef = TypedDict(
    "_ClientDescribeStackResourceResponseStackResourceDetailTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "Description": str,
        "Metadata": str,
        "DriftInformation": ClientDescribeStackResourceResponseStackResourceDetailDriftInformationTypeDef,
    },
    total=False,
)


class ClientDescribeStackResourceResponseStackResourceDetailTypeDef(
    _ClientDescribeStackResourceResponseStackResourceDetailTypeDef
):
    """
    - **StackResourceDetail** *(dict) --*

      A ``StackResourceDetail`` structure containing the description of the specified resource in
      the specified stack.
      - **StackName** *(string) --*

        The name associated with the stack.
    """


_ClientDescribeStackResourceResponseTypeDef = TypedDict(
    "_ClientDescribeStackResourceResponseTypeDef",
    {"StackResourceDetail": ClientDescribeStackResourceResponseStackResourceDetailTypeDef},
    total=False,
)


class ClientDescribeStackResourceResponseTypeDef(_ClientDescribeStackResourceResponseTypeDef):
    """
    - *(dict) --*

      The output for a  DescribeStackResource action.
      - **StackResourceDetail** *(dict) --*

        A ``StackResourceDetail`` structure containing the description of the specified resource in
        the specified stack.
        - **StackName** *(string) --*

          The name associated with the stack.
    """


_ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef = TypedDict(
    "_ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef(
    _ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef
):
    pass


_ClientDescribeStackResourcesResponseStackResourcesTypeDef = TypedDict(
    "_ClientDescribeStackResourcesResponseStackResourcesTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "Description": str,
        "DriftInformation": ClientDescribeStackResourcesResponseStackResourcesDriftInformationTypeDef,
    },
    total=False,
)


class ClientDescribeStackResourcesResponseStackResourcesTypeDef(
    _ClientDescribeStackResourcesResponseStackResourcesTypeDef
):
    """
    - *(dict) --*

      The StackResource data type.
      - **StackName** *(string) --*

        The name associated with the stack.
    """


_ClientDescribeStackResourcesResponseTypeDef = TypedDict(
    "_ClientDescribeStackResourcesResponseTypeDef",
    {"StackResources": List[ClientDescribeStackResourcesResponseStackResourcesTypeDef]},
    total=False,
)


class ClientDescribeStackResourcesResponseTypeDef(_ClientDescribeStackResourcesResponseTypeDef):
    """
    - *(dict) --*

      The output for a  DescribeStackResources action.
      - **StackResources** *(list) --*

        A list of ``StackResource`` structures.
        - *(dict) --*

          The StackResource data type.
          - **StackName** *(string) --*

            The name associated with the stack.
    """


_ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef = TypedDict(
    "_ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef(
    _ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef
):
    pass


_ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef = TypedDict(
    "_ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED"],
        "DriftDetectionStatus": Literal[
            "COMPLETED", "FAILED", "PARTIAL_SUCCESS", "IN_PROGRESS", "STOPPED"
        ],
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)


class ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef(
    _ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef
):
    pass


_ClientDescribeStackSetOperationResponseStackSetOperationTypeDef = TypedDict(
    "_ClientDescribeStackSetOperationResponseStackSetOperationTypeDef",
    {
        "OperationId": str,
        "StackSetId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED"],
        "OperationPreferences": ClientDescribeStackSetOperationResponseStackSetOperationOperationPreferencesTypeDef,
        "RetainStacks": bool,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
        "StackSetDriftDetectionDetails": ClientDescribeStackSetOperationResponseStackSetOperationStackSetDriftDetectionDetailsTypeDef,
    },
    total=False,
)


class ClientDescribeStackSetOperationResponseStackSetOperationTypeDef(
    _ClientDescribeStackSetOperationResponseStackSetOperationTypeDef
):
    """
    - **StackSetOperation** *(dict) --*

      The specified stack set operation.
      - **OperationId** *(string) --*

        The unique ID of a stack set operation.
    """


_ClientDescribeStackSetOperationResponseTypeDef = TypedDict(
    "_ClientDescribeStackSetOperationResponseTypeDef",
    {"StackSetOperation": ClientDescribeStackSetOperationResponseStackSetOperationTypeDef},
    total=False,
)


class ClientDescribeStackSetOperationResponseTypeDef(
    _ClientDescribeStackSetOperationResponseTypeDef
):
    """
    - *(dict) --*

      - **StackSetOperation** *(dict) --*

        The specified stack set operation.
        - **OperationId** *(string) --*

          The unique ID of a stack set operation.
    """


_ClientDescribeStackSetResponseStackSetParametersTypeDef = TypedDict(
    "_ClientDescribeStackSetResponseStackSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientDescribeStackSetResponseStackSetParametersTypeDef(
    _ClientDescribeStackSetResponseStackSetParametersTypeDef
):
    pass


_ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef = TypedDict(
    "_ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED"],
        "DriftDetectionStatus": Literal[
            "COMPLETED", "FAILED", "PARTIAL_SUCCESS", "IN_PROGRESS", "STOPPED"
        ],
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)


class ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef(
    _ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef
):
    pass


_ClientDescribeStackSetResponseStackSetTagsTypeDef = TypedDict(
    "_ClientDescribeStackSetResponseStackSetTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeStackSetResponseStackSetTagsTypeDef(
    _ClientDescribeStackSetResponseStackSetTagsTypeDef
):
    pass


_ClientDescribeStackSetResponseStackSetTypeDef = TypedDict(
    "_ClientDescribeStackSetResponseStackSetTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "TemplateBody": str,
        "Parameters": List[ClientDescribeStackSetResponseStackSetParametersTypeDef],
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List[ClientDescribeStackSetResponseStackSetTagsTypeDef],
        "StackSetARN": str,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "StackSetDriftDetectionDetails": ClientDescribeStackSetResponseStackSetStackSetDriftDetectionDetailsTypeDef,
    },
    total=False,
)


class ClientDescribeStackSetResponseStackSetTypeDef(_ClientDescribeStackSetResponseStackSetTypeDef):
    """
    - **StackSet** *(dict) --*

      The specified stack set.
      - **StackSetName** *(string) --*

        The name that's associated with the stack set.
    """


_ClientDescribeStackSetResponseTypeDef = TypedDict(
    "_ClientDescribeStackSetResponseTypeDef",
    {"StackSet": ClientDescribeStackSetResponseStackSetTypeDef},
    total=False,
)


class ClientDescribeStackSetResponseTypeDef(_ClientDescribeStackSetResponseTypeDef):
    """
    - *(dict) --*

      - **StackSet** *(dict) --*

        The specified stack set.
        - **StackSetName** *(string) --*

          The name that's associated with the stack set.
    """


_ClientDescribeStacksResponseStacksDriftInformationTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksDriftInformationTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksDriftInformationTypeDef(
    _ClientDescribeStacksResponseStacksDriftInformationTypeDef
):
    pass


_ClientDescribeStacksResponseStacksOutputsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksOutputsTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str, "ExportName": str},
    total=False,
)


class ClientDescribeStacksResponseStacksOutputsTypeDef(
    _ClientDescribeStacksResponseStacksOutputsTypeDef
):
    pass


_ClientDescribeStacksResponseStacksParametersTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientDescribeStacksResponseStacksParametersTypeDef(
    _ClientDescribeStacksResponseStacksParametersTypeDef
):
    pass


_ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)


class ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef(
    _ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef
):
    pass


_ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ClientDescribeStacksResponseStacksRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef(
    _ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef
):
    pass


_ClientDescribeStacksResponseStacksTagsTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeStacksResponseStacksTagsTypeDef(_ClientDescribeStacksResponseStacksTagsTypeDef):
    pass


_ClientDescribeStacksResponseStacksTypeDef = TypedDict(
    "_ClientDescribeStacksResponseStacksTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List[ClientDescribeStacksResponseStacksParametersTypeDef],
        "CreationTime": datetime,
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": ClientDescribeStacksResponseStacksRollbackConfigurationTypeDef,
        "StackStatus": Literal[
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
        ],
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Outputs": List[ClientDescribeStacksResponseStacksOutputsTypeDef],
        "RoleARN": str,
        "Tags": List[ClientDescribeStacksResponseStacksTagsTypeDef],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ClientDescribeStacksResponseStacksDriftInformationTypeDef,
    },
    total=False,
)


class ClientDescribeStacksResponseStacksTypeDef(_ClientDescribeStacksResponseStacksTypeDef):
    """
    - *(dict) --*

      The Stack data type.
      - **StackId** *(string) --*

        Unique identifier of the stack.
    """


_ClientDescribeStacksResponseTypeDef = TypedDict(
    "_ClientDescribeStacksResponseTypeDef",
    {"Stacks": List[ClientDescribeStacksResponseStacksTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeStacksResponseTypeDef(_ClientDescribeStacksResponseTypeDef):
    """
    - *(dict) --*

      The output for a  DescribeStacks action.
      - **Stacks** *(list) --*

        A list of stack structures.
        - *(dict) --*

          The Stack data type.
          - **StackId** *(string) --*

            Unique identifier of the stack.
    """


_ClientDescribeTypeRegistrationResponseTypeDef = TypedDict(
    "_ClientDescribeTypeRegistrationResponseTypeDef",
    {
        "ProgressStatus": Literal["COMPLETE", "IN_PROGRESS", "FAILED"],
        "Description": str,
        "TypeArn": str,
        "TypeVersionArn": str,
    },
    total=False,
)


class ClientDescribeTypeRegistrationResponseTypeDef(_ClientDescribeTypeRegistrationResponseTypeDef):
    """
    - *(dict) --*

      - **ProgressStatus** *(string) --*

        The current status of the type registration request.
    """


_ClientDescribeTypeResponseLoggingConfigTypeDef = TypedDict(
    "_ClientDescribeTypeResponseLoggingConfigTypeDef",
    {"LogRoleArn": str, "LogGroupName": str},
    total=False,
)


class ClientDescribeTypeResponseLoggingConfigTypeDef(
    _ClientDescribeTypeResponseLoggingConfigTypeDef
):
    pass


_ClientDescribeTypeResponseTypeDef = TypedDict(
    "_ClientDescribeTypeResponseTypeDef",
    {
        "Arn": str,
        "Type": str,
        "TypeName": str,
        "DefaultVersionId": str,
        "Description": str,
        "Schema": str,
        "ProvisioningType": Literal["NON_PROVISIONABLE", "IMMUTABLE", "FULLY_MUTABLE"],
        "DeprecatedStatus": Literal["LIVE", "DEPRECATED"],
        "LoggingConfig": ClientDescribeTypeResponseLoggingConfigTypeDef,
        "ExecutionRoleArn": str,
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
    },
    total=False,
)


class ClientDescribeTypeResponseTypeDef(_ClientDescribeTypeResponseTypeDef):
    """
    - *(dict) --*

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the type.
    """


_ClientDetectStackDriftResponseTypeDef = TypedDict(
    "_ClientDetectStackDriftResponseTypeDef", {"StackDriftDetectionId": str}, total=False
)


class ClientDetectStackDriftResponseTypeDef(_ClientDetectStackDriftResponseTypeDef):
    """
    - *(dict) --*

      - **StackDriftDetectionId** *(string) --*

        The ID of the drift detection results of this operation.
        AWS CloudFormation generates new results, with a new drift detection ID, each time this
        operation is run. However, the number of drift results AWS CloudFormation retains for any
        given stack, and for how long, may vary.
    """


_ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef = TypedDict(
    "_ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef(
    _ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef
):
    pass


_ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef = TypedDict(
    "_ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": Literal["ADD", "REMOVE", "NOT_EQUAL"],
    },
    total=False,
)


class ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef(
    _ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef
):
    pass


_ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef = TypedDict(
    "_ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List[
            ClientDetectStackResourceDriftResponseStackResourceDriftPhysicalResourceIdContextTypeDef
        ],
        "ResourceType": str,
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List[
            ClientDetectStackResourceDriftResponseStackResourceDriftPropertyDifferencesTypeDef
        ],
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "Timestamp": datetime,
    },
    total=False,
)


class ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef(
    _ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef
):
    """
    - **StackResourceDrift** *(dict) --*

      Information about whether the resource's actual configuration has drifted from its expected
      template configuration, including actual and expected property values and any differences
      detected.
      - **StackId** *(string) --*

        The ID of the stack.
    """


_ClientDetectStackResourceDriftResponseTypeDef = TypedDict(
    "_ClientDetectStackResourceDriftResponseTypeDef",
    {"StackResourceDrift": ClientDetectStackResourceDriftResponseStackResourceDriftTypeDef},
    total=False,
)


class ClientDetectStackResourceDriftResponseTypeDef(_ClientDetectStackResourceDriftResponseTypeDef):
    """
    - *(dict) --*

      - **StackResourceDrift** *(dict) --*

        Information about whether the resource's actual configuration has drifted from its expected
        template configuration, including actual and expected property values and any differences
        detected.
        - **StackId** *(string) --*

          The ID of the stack.
    """


_ClientDetectStackSetDriftOperationPreferencesTypeDef = TypedDict(
    "_ClientDetectStackSetDriftOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientDetectStackSetDriftOperationPreferencesTypeDef(
    _ClientDetectStackSetDriftOperationPreferencesTypeDef
):
    """
    The user-specified preferences for how AWS CloudFormation performs a stack set operation.
    For more information on maximum concurrent accounts and failure tolerance, see `Stack set
    operation options
    <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options>`__
    .
    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.
      - *(string) --*
    """


_ClientDetectStackSetDriftResponseTypeDef = TypedDict(
    "_ClientDetectStackSetDriftResponseTypeDef", {"OperationId": str}, total=False
)


class ClientDetectStackSetDriftResponseTypeDef(_ClientDetectStackSetDriftResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        The ID of the drift detection stack set operation.
        you can use this operation id with ``  DescribeStackSetOperation `` to monitor the progress
        of the drift detection operation.
    """


_ClientEstimateTemplateCostParametersTypeDef = TypedDict(
    "_ClientEstimateTemplateCostParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientEstimateTemplateCostParametersTypeDef(_ClientEstimateTemplateCostParametersTypeDef):
    """
    - *(dict) --*

      The Parameter data type.
      - **ParameterKey** *(string) --*

        The key associated with the parameter. If you don't specify a key and value for a particular
        parameter, AWS CloudFormation uses the default value that is specified in your template.
    """


_ClientEstimateTemplateCostResponseTypeDef = TypedDict(
    "_ClientEstimateTemplateCostResponseTypeDef", {"Url": str}, total=False
)


class ClientEstimateTemplateCostResponseTypeDef(_ClientEstimateTemplateCostResponseTypeDef):
    """
    - *(dict) --*

      The output for a  EstimateTemplateCost action.
      - **Url** *(string) --*

        An AWS Simple Monthly Calculator URL with a query string that describes the resources
        required to run the template.
    """


_ClientGetStackPolicyResponseTypeDef = TypedDict(
    "_ClientGetStackPolicyResponseTypeDef", {"StackPolicyBody": str}, total=False
)


class ClientGetStackPolicyResponseTypeDef(_ClientGetStackPolicyResponseTypeDef):
    """
    - *(dict) --*

      The output for the  GetStackPolicy action.
      - **StackPolicyBody** *(string) --*

        Structure containing the stack policy body. (For more information, go to `Prevent Updates to
        Stack Resources
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html>`__
        in the AWS CloudFormation User Guide.)
    """


_ClientGetTemplateResponseTypeDef = TypedDict(
    "_ClientGetTemplateResponseTypeDef",
    {"TemplateBody": Dict[str, Any], "StagesAvailable": List[Literal["Original", "Processed"]]},
    total=False,
)


class ClientGetTemplateResponseTypeDef(_ClientGetTemplateResponseTypeDef):
    """
    - *(dict) --*

      The output for  GetTemplate action.
      - **TemplateBody** (*dict*) --

        Structure containing the template body. (For more information, go to `Template Anatomy
        <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html>`__ in
        the AWS CloudFormation User Guide.)
        AWS CloudFormation returns the same template that was used when the stack was created.
    """


_ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef = TypedDict(
    "_ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef",
    {"AllowedValues": List[str]},
    total=False,
)


class ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef(
    _ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef
):
    pass


_ClientGetTemplateSummaryResponseParametersTypeDef = TypedDict(
    "_ClientGetTemplateSummaryResponseParametersTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "NoEcho": bool,
        "Description": str,
        "ParameterConstraints": ClientGetTemplateSummaryResponseParametersParameterConstraintsTypeDef,
    },
    total=False,
)


class ClientGetTemplateSummaryResponseParametersTypeDef(
    _ClientGetTemplateSummaryResponseParametersTypeDef
):
    """
    - *(dict) --*

      The ParameterDeclaration data type.
      - **ParameterKey** *(string) --*

        The name that is associated with the parameter.
    """


_ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef = TypedDict(
    "_ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef",
    {"ResourceType": str, "LogicalResourceIds": List[str], "ResourceIdentifiers": List[str]},
    total=False,
)


class ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef(
    _ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef
):
    pass


_ClientGetTemplateSummaryResponseTypeDef = TypedDict(
    "_ClientGetTemplateSummaryResponseTypeDef",
    {
        "Parameters": List[ClientGetTemplateSummaryResponseParametersTypeDef],
        "Description": str,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "CapabilitiesReason": str,
        "ResourceTypes": List[str],
        "Version": str,
        "Metadata": str,
        "DeclaredTransforms": List[str],
        "ResourceIdentifierSummaries": List[
            ClientGetTemplateSummaryResponseResourceIdentifierSummariesTypeDef
        ],
    },
    total=False,
)


class ClientGetTemplateSummaryResponseTypeDef(_ClientGetTemplateSummaryResponseTypeDef):
    """
    - *(dict) --*

      The output for the  GetTemplateSummary action.
      - **Parameters** *(list) --*

        A list of parameter declarations that describe various properties for each parameter.
        - *(dict) --*

          The ParameterDeclaration data type.
          - **ParameterKey** *(string) --*

            The name that is associated with the parameter.
    """


_ClientListChangeSetsResponseSummariesTypeDef = TypedDict(
    "_ClientListChangeSetsResponseSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListChangeSetsResponseSummariesTypeDef(_ClientListChangeSetsResponseSummariesTypeDef):
    """
    - *(dict) --*

      The ``ChangeSetSummary`` structure describes a change set, its status, and the stack with
      which it's associated.
      - **StackId** *(string) --*

        The ID of the stack with which the change set is associated.
    """


_ClientListChangeSetsResponseTypeDef = TypedDict(
    "_ClientListChangeSetsResponseTypeDef",
    {"Summaries": List[ClientListChangeSetsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListChangeSetsResponseTypeDef(_ClientListChangeSetsResponseTypeDef):
    """
    - *(dict) --*

      The output for the  ListChangeSets action.
      - **Summaries** *(list) --*

        A list of ``ChangeSetSummary`` structures that provides the ID and status of each change set
        for the specified stack.
        - *(dict) --*

          The ``ChangeSetSummary`` structure describes a change set, its status, and the stack with
          which it's associated.
          - **StackId** *(string) --*

            The ID of the stack with which the change set is associated.
    """


_ClientListExportsResponseExportsTypeDef = TypedDict(
    "_ClientListExportsResponseExportsTypeDef",
    {"ExportingStackId": str, "Name": str, "Value": str},
    total=False,
)


class ClientListExportsResponseExportsTypeDef(_ClientListExportsResponseExportsTypeDef):
    """
    - *(dict) --*

      The ``Export`` structure describes the exported output values for a stack.
      - **ExportingStackId** *(string) --*

        The stack that contains the exported output name and value.
    """


_ClientListExportsResponseTypeDef = TypedDict(
    "_ClientListExportsResponseTypeDef",
    {"Exports": List[ClientListExportsResponseExportsTypeDef], "NextToken": str},
    total=False,
)


class ClientListExportsResponseTypeDef(_ClientListExportsResponseTypeDef):
    """
    - *(dict) --*

      - **Exports** *(list) --*

        The output for the  ListExports action.
        - *(dict) --*

          The ``Export`` structure describes the exported output values for a stack.
          - **ExportingStackId** *(string) --*

            The stack that contains the exported output name and value.
    """


_ClientListImportsResponseTypeDef = TypedDict(
    "_ClientListImportsResponseTypeDef", {"Imports": List[str], "NextToken": str}, total=False
)


class ClientListImportsResponseTypeDef(_ClientListImportsResponseTypeDef):
    """
    - *(dict) --*

      - **Imports** *(list) --*

        A list of stack names that are importing the specified exported output value.
        - *(string) --*
    """


_ClientListStackInstancesResponseSummariesTypeDef = TypedDict(
    "_ClientListStackInstancesResponseSummariesTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StatusReason": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)


class ClientListStackInstancesResponseSummariesTypeDef(
    _ClientListStackInstancesResponseSummariesTypeDef
):
    """
    - *(dict) --*

      The structure that contains summary information about a stack instance.
      - **StackSetId** *(string) --*

        The name or unique ID of the stack set that the stack instance is associated with.
    """


_ClientListStackInstancesResponseTypeDef = TypedDict(
    "_ClientListStackInstancesResponseTypeDef",
    {"Summaries": List[ClientListStackInstancesResponseSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListStackInstancesResponseTypeDef(_ClientListStackInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **Summaries** *(list) --*

        A list of ``StackInstanceSummary`` structures that contain information about the specified
        stack instances.
        - *(dict) --*

          The structure that contains summary information about a stack instance.
          - **StackSetId** *(string) --*

            The name or unique ID of the stack set that the stack instance is associated with.
    """


_ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef = TypedDict(
    "_ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef(
    _ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef
):
    pass


_ClientListStackResourcesResponseStackResourceSummariesTypeDef = TypedDict(
    "_ClientListStackResourcesResponseStackResourceSummariesTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "DriftInformation": ClientListStackResourcesResponseStackResourceSummariesDriftInformationTypeDef,
    },
    total=False,
)


class ClientListStackResourcesResponseStackResourceSummariesTypeDef(
    _ClientListStackResourcesResponseStackResourceSummariesTypeDef
):
    """
    - *(dict) --*

      Contains high-level information about the specified stack resource.
      - **LogicalResourceId** *(string) --*

        The logical name of the resource specified in the template.
    """


_ClientListStackResourcesResponseTypeDef = TypedDict(
    "_ClientListStackResourcesResponseTypeDef",
    {
        "StackResourceSummaries": List[
            ClientListStackResourcesResponseStackResourceSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListStackResourcesResponseTypeDef(_ClientListStackResourcesResponseTypeDef):
    """
    - *(dict) --*

      The output for a  ListStackResources action.
      - **StackResourceSummaries** *(list) --*

        A list of ``StackResourceSummary`` structures.
        - *(dict) --*

          Contains high-level information about the specified stack resource.
          - **LogicalResourceId** *(string) --*

            The logical name of the resource specified in the template.
    """


_ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef = TypedDict(
    "_ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef",
    {"Status": Literal["SUCCEEDED", "FAILED", "SKIPPED"], "StatusReason": str},
    total=False,
)


class ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef(
    _ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef
):
    pass


_ClientListStackSetOperationResultsResponseSummariesTypeDef = TypedDict(
    "_ClientListStackSetOperationResultsResponseSummariesTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StatusReason": str,
        "AccountGateResult": ClientListStackSetOperationResultsResponseSummariesAccountGateResultTypeDef,
    },
    total=False,
)


class ClientListStackSetOperationResultsResponseSummariesTypeDef(
    _ClientListStackSetOperationResultsResponseSummariesTypeDef
):
    """
    - *(dict) --*

      The structure that contains information about a specified operation's results for a given
      account in a given region.
      - **Account** *(string) --*

        The name of the AWS account for this operation result.
    """


_ClientListStackSetOperationResultsResponseTypeDef = TypedDict(
    "_ClientListStackSetOperationResultsResponseTypeDef",
    {
        "Summaries": List[ClientListStackSetOperationResultsResponseSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListStackSetOperationResultsResponseTypeDef(
    _ClientListStackSetOperationResultsResponseTypeDef
):
    """
    - *(dict) --*

      - **Summaries** *(list) --*

        A list of ``StackSetOperationResultSummary`` structures that contain information about the
        specified operation results, for accounts and regions that are included in the operation.
        - *(dict) --*

          The structure that contains information about a specified operation's results for a given
          account in a given region.
          - **Account** *(string) --*

            The name of the AWS account for this operation result.
    """


_ClientListStackSetOperationsResponseSummariesTypeDef = TypedDict(
    "_ClientListStackSetOperationsResponseSummariesTypeDef",
    {
        "OperationId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED"],
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)


class ClientListStackSetOperationsResponseSummariesTypeDef(
    _ClientListStackSetOperationsResponseSummariesTypeDef
):
    """
    - *(dict) --*

      The structures that contain summary information about the specified operation.
      - **OperationId** *(string) --*

        The unique ID of the stack set operation.
    """


_ClientListStackSetOperationsResponseTypeDef = TypedDict(
    "_ClientListStackSetOperationsResponseTypeDef",
    {"Summaries": List[ClientListStackSetOperationsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListStackSetOperationsResponseTypeDef(_ClientListStackSetOperationsResponseTypeDef):
    """
    - *(dict) --*

      - **Summaries** *(list) --*

        A list of ``StackSetOperationSummary`` structures that contain summary information about
        operations for the specified stack set.
        - *(dict) --*

          The structures that contain summary information about the specified operation.
          - **OperationId** *(string) --*

            The unique ID of the stack set operation.
    """


_ClientListStackSetsResponseSummariesTypeDef = TypedDict(
    "_ClientListStackSetsResponseSummariesTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)


class ClientListStackSetsResponseSummariesTypeDef(_ClientListStackSetsResponseSummariesTypeDef):
    """
    - *(dict) --*

      The structures that contain summary information about the specified stack set.
      - **StackSetName** *(string) --*

        The name of the stack set.
    """


_ClientListStackSetsResponseTypeDef = TypedDict(
    "_ClientListStackSetsResponseTypeDef",
    {"Summaries": List[ClientListStackSetsResponseSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListStackSetsResponseTypeDef(_ClientListStackSetsResponseTypeDef):
    """
    - *(dict) --*

      - **Summaries** *(list) --*

        A list of ``StackSetSummary`` structures that contain information about the user's stack
        sets.
        - *(dict) --*

          The structures that contain summary information about the specified stack set.
          - **StackSetName** *(string) --*

            The name of the stack set.
    """


_ClientListStacksResponseStackSummariesDriftInformationTypeDef = TypedDict(
    "_ClientListStacksResponseStackSummariesDriftInformationTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class ClientListStacksResponseStackSummariesDriftInformationTypeDef(
    _ClientListStacksResponseStackSummariesDriftInformationTypeDef
):
    pass


_ClientListStacksResponseStackSummariesTypeDef = TypedDict(
    "_ClientListStacksResponseStackSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "TemplateDescription": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatus": Literal[
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
        ],
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ClientListStacksResponseStackSummariesDriftInformationTypeDef,
    },
    total=False,
)


class ClientListStacksResponseStackSummariesTypeDef(_ClientListStacksResponseStackSummariesTypeDef):
    """
    - *(dict) --*

      The StackSummary Data Type
      - **StackId** *(string) --*

        Unique stack identifier.
    """


_ClientListStacksResponseTypeDef = TypedDict(
    "_ClientListStacksResponseTypeDef",
    {"StackSummaries": List[ClientListStacksResponseStackSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListStacksResponseTypeDef(_ClientListStacksResponseTypeDef):
    """
    - *(dict) --*

      The output for  ListStacks action.
      - **StackSummaries** *(list) --*

        A list of ``StackSummary`` structures containing information about the specified stacks.
        - *(dict) --*

          The StackSummary Data Type
          - **StackId** *(string) --*

            Unique stack identifier.
    """


_ClientListTypeRegistrationsResponseTypeDef = TypedDict(
    "_ClientListTypeRegistrationsResponseTypeDef",
    {"RegistrationTokenList": List[str], "NextToken": str},
    total=False,
)


class ClientListTypeRegistrationsResponseTypeDef(_ClientListTypeRegistrationsResponseTypeDef):
    """
    - *(dict) --*

      - **RegistrationTokenList** *(list) --*

        A list of type registration tokens.
        Use ``  DescribeTypeRegistration `` to return detailed information about a type registration
        request.
        - *(string) --*
    """


_ClientListTypeVersionsResponseTypeVersionSummariesTypeDef = TypedDict(
    "_ClientListTypeVersionsResponseTypeVersionSummariesTypeDef",
    {
        "Type": str,
        "TypeName": str,
        "VersionId": str,
        "Arn": str,
        "TimeCreated": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListTypeVersionsResponseTypeVersionSummariesTypeDef(
    _ClientListTypeVersionsResponseTypeVersionSummariesTypeDef
):
    """
    - *(dict) --*

      Contains summary information about a specific version of a CloudFormation type.
      - **Type** *(string) --*

        The kind of type.
    """


_ClientListTypeVersionsResponseTypeDef = TypedDict(
    "_ClientListTypeVersionsResponseTypeDef",
    {
        "TypeVersionSummaries": List[ClientListTypeVersionsResponseTypeVersionSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTypeVersionsResponseTypeDef(_ClientListTypeVersionsResponseTypeDef):
    """
    - *(dict) --*

      - **TypeVersionSummaries** *(list) --*

        A list of ``TypeVersionSummary`` structures that contain information about the specified
        type's versions.
        - *(dict) --*

          Contains summary information about a specific version of a CloudFormation type.
          - **Type** *(string) --*

            The kind of type.
    """


_ClientListTypesResponseTypeSummariesTypeDef = TypedDict(
    "_ClientListTypesResponseTypeSummariesTypeDef",
    {
        "Type": str,
        "TypeName": str,
        "DefaultVersionId": str,
        "TypeArn": str,
        "LastUpdated": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListTypesResponseTypeSummariesTypeDef(_ClientListTypesResponseTypeSummariesTypeDef):
    """
    - *(dict) --*

      Contains summary information about the specified CloudFormation type.
      - **Type** *(string) --*

        The kind of type.
    """


_ClientListTypesResponseTypeDef = TypedDict(
    "_ClientListTypesResponseTypeDef",
    {"TypeSummaries": List[ClientListTypesResponseTypeSummariesTypeDef], "NextToken": str},
    total=False,
)


class ClientListTypesResponseTypeDef(_ClientListTypesResponseTypeDef):
    """
    - *(dict) --*

      - **TypeSummaries** *(list) --*

        A list of ``TypeSummary`` structures that contain information about the specified types.
        - *(dict) --*

          Contains summary information about the specified CloudFormation type.
          - **Type** *(string) --*

            The kind of type.
    """


_RequiredClientRegisterTypeLoggingConfigTypeDef = TypedDict(
    "_RequiredClientRegisterTypeLoggingConfigTypeDef", {"LogRoleArn": str}
)
_OptionalClientRegisterTypeLoggingConfigTypeDef = TypedDict(
    "_OptionalClientRegisterTypeLoggingConfigTypeDef", {"LogGroupName": str}, total=False
)


class ClientRegisterTypeLoggingConfigTypeDef(
    _RequiredClientRegisterTypeLoggingConfigTypeDef, _OptionalClientRegisterTypeLoggingConfigTypeDef
):
    """
    Specifies logging configuration information for a type.
    - **LogRoleArn** *(string) --***[REQUIRED]**

      The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch
      logs.
    """


_ClientRegisterTypeResponseTypeDef = TypedDict(
    "_ClientRegisterTypeResponseTypeDef", {"RegistrationToken": str}, total=False
)


class ClientRegisterTypeResponseTypeDef(_ClientRegisterTypeResponseTypeDef):
    """
    - *(dict) --*

      - **RegistrationToken** *(string) --*

        The identifier for this registration request.
        Use this registration token when calling ``  DescribeTypeRegistration `` , which returns
        information about the status and IDs of the type registration.
    """


_ClientUpdateStackInstancesOperationPreferencesTypeDef = TypedDict(
    "_ClientUpdateStackInstancesOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientUpdateStackInstancesOperationPreferencesTypeDef(
    _ClientUpdateStackInstancesOperationPreferencesTypeDef
):
    """
    Preferences for how AWS CloudFormation performs this stack set operation.
    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.
      - *(string) --*
    """


_ClientUpdateStackInstancesParameterOverridesTypeDef = TypedDict(
    "_ClientUpdateStackInstancesParameterOverridesTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientUpdateStackInstancesParameterOverridesTypeDef(
    _ClientUpdateStackInstancesParameterOverridesTypeDef
):
    pass


_ClientUpdateStackInstancesResponseTypeDef = TypedDict(
    "_ClientUpdateStackInstancesResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateStackInstancesResponseTypeDef(_ClientUpdateStackInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        The unique identifier for this stack set operation.
    """


_ClientUpdateStackParametersTypeDef = TypedDict(
    "_ClientUpdateStackParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientUpdateStackParametersTypeDef(_ClientUpdateStackParametersTypeDef):
    """
    - *(dict) --*

      The Parameter data type.
      - **ParameterKey** *(string) --*

        The key associated with the parameter. If you don't specify a key and value for a particular
        parameter, AWS CloudFormation uses the default value that is specified in your template.
    """


_ClientUpdateStackResponseTypeDef = TypedDict(
    "_ClientUpdateStackResponseTypeDef", {"StackId": str}, total=False
)


class ClientUpdateStackResponseTypeDef(_ClientUpdateStackResponseTypeDef):
    """
    - *(dict) --*

      The output for an  UpdateStack action.
      - **StackId** *(string) --*

        Unique identifier of the stack.
    """


_RequiredClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef,
):
    """
    - *(dict) --*

      A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
      of the alarms you specify goes to ALARM state during the stack operation or within the
      specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.
      - **Arn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the rollback trigger.
        If a specified trigger is missing, the entire stack operation fails and is rolled back.
    """


_ClientUpdateStackRollbackConfigurationTypeDef = TypedDict(
    "_ClientUpdateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[ClientUpdateStackRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ClientUpdateStackRollbackConfigurationTypeDef(_ClientUpdateStackRollbackConfigurationTypeDef):
    """
    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.
    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.
      By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies
      them to any subsequent update operations for the stack, unless you specify otherwise. If you
      do specify rollback triggers for this parameter, those triggers replace any list of triggers
      previously specified for the stack. This means:
      * To use the rollback triggers previously specified for this stack, if any, don't specify this
      parameter.
      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating the
      stack or during a previous stack update). Any triggers that you don't include in the updated
      list of triggers are no longer applied to the stack.
      * To remove all currently specified triggers, specify an empty list for this parameter.
      If a specified trigger is missing, the entire stack operation fails and is rolled back.
      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
        any of the alarms you specify goes to ALARM state during the stack operation or within the
        specified monitoring period afterwards, CloudFormation rolls back the entire stack
        operation.
        - **Arn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the rollback trigger.
          If a specified trigger is missing, the entire stack operation fails and is rolled back.
    """


_ClientUpdateStackSetOperationPreferencesTypeDef = TypedDict(
    "_ClientUpdateStackSetOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)


class ClientUpdateStackSetOperationPreferencesTypeDef(
    _ClientUpdateStackSetOperationPreferencesTypeDef
):
    """
    Preferences for how AWS CloudFormation performs this stack set operation.
    - **RegionOrder** *(list) --*

      The order of the regions in where you want to perform the stack operation.
      - *(string) --*
    """


_ClientUpdateStackSetParametersTypeDef = TypedDict(
    "_ClientUpdateStackSetParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ClientUpdateStackSetParametersTypeDef(_ClientUpdateStackSetParametersTypeDef):
    """
    - *(dict) --*

      The Parameter data type.
      - **ParameterKey** *(string) --*

        The key associated with the parameter. If you don't specify a key and value for a particular
        parameter, AWS CloudFormation uses the default value that is specified in your template.
    """


_ClientUpdateStackSetResponseTypeDef = TypedDict(
    "_ClientUpdateStackSetResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateStackSetResponseTypeDef(_ClientUpdateStackSetResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        The unique ID for this stack set operation.
    """


_RequiredClientUpdateStackSetTagsTypeDef = TypedDict(
    "_RequiredClientUpdateStackSetTagsTypeDef", {"Key": str}
)
_OptionalClientUpdateStackSetTagsTypeDef = TypedDict(
    "_OptionalClientUpdateStackSetTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdateStackSetTagsTypeDef(
    _RequiredClientUpdateStackSetTagsTypeDef, _OptionalClientUpdateStackSetTagsTypeDef
):
    """
    - *(dict) --*

      The Tag type enables you to specify a key-value pair that can be used to store information
      about an AWS CloudFormation stack.
      - **Key** *(string) --***[REQUIRED]**

        *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
        for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
    """


_RequiredClientUpdateStackTagsTypeDef = TypedDict(
    "_RequiredClientUpdateStackTagsTypeDef", {"Key": str}
)
_OptionalClientUpdateStackTagsTypeDef = TypedDict(
    "_OptionalClientUpdateStackTagsTypeDef", {"Value": str}, total=False
)


class ClientUpdateStackTagsTypeDef(
    _RequiredClientUpdateStackTagsTypeDef, _OptionalClientUpdateStackTagsTypeDef
):
    """
    - *(dict) --*

      The Tag type enables you to specify a key-value pair that can be used to store information
      about an AWS CloudFormation stack.
      - **Key** *(string) --***[REQUIRED]**

        *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
        for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
    """


_ClientUpdateTerminationProtectionResponseTypeDef = TypedDict(
    "_ClientUpdateTerminationProtectionResponseTypeDef", {"StackId": str}, total=False
)


class ClientUpdateTerminationProtectionResponseTypeDef(
    _ClientUpdateTerminationProtectionResponseTypeDef
):
    """
    - *(dict) --*

      - **StackId** *(string) --*

        The unique ID of the stack.
    """


_ClientValidateTemplateResponseParametersTypeDef = TypedDict(
    "_ClientValidateTemplateResponseParametersTypeDef",
    {"ParameterKey": str, "DefaultValue": str, "NoEcho": bool, "Description": str},
    total=False,
)


class ClientValidateTemplateResponseParametersTypeDef(
    _ClientValidateTemplateResponseParametersTypeDef
):
    """
    - *(dict) --*

      The TemplateParameter data type.
      - **ParameterKey** *(string) --*

        The name associated with the parameter.
    """


_ClientValidateTemplateResponseTypeDef = TypedDict(
    "_ClientValidateTemplateResponseTypeDef",
    {
        "Parameters": List[ClientValidateTemplateResponseParametersTypeDef],
        "Description": str,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "CapabilitiesReason": str,
        "DeclaredTransforms": List[str],
    },
    total=False,
)


class ClientValidateTemplateResponseTypeDef(_ClientValidateTemplateResponseTypeDef):
    """
    - *(dict) --*

      The output for  ValidateTemplate action.
      - **Parameters** *(list) --*

        A list of ``TemplateParameter`` structures.
        - *(dict) --*

          The TemplateParameter data type.
          - **ParameterKey** *(string) --*

            The name associated with the parameter.
    """


_DescribeAccountLimitsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeAccountLimitsPaginatePaginationConfigTypeDef(
    _DescribeAccountLimitsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef",
    {"Name": str, "Value": int},
    total=False,
)


class DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef(
    _DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef
):
    """
    - *(dict) --*

      The AccountLimit data type.
      CloudFormation has the following limits per account:
      * Number of concurrent resources
      * Number of stacks
      * Number of stack outputs
      For more information about these account limits, and other CloudFormation limits, see `AWS
      CloudFormation Limits
      <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
      in the *AWS CloudFormation User Guide* .
      - **Name** *(string) --*

        The name of the account limit.
        Values: ``ConcurrentResourcesLimit`` | ``StackLimit`` | ``StackOutputsLimit``
    """


_DescribeAccountLimitsPaginateResponseTypeDef = TypedDict(
    "_DescribeAccountLimitsPaginateResponseTypeDef",
    {"AccountLimits": List[DescribeAccountLimitsPaginateResponseAccountLimitsTypeDef]},
    total=False,
)


class DescribeAccountLimitsPaginateResponseTypeDef(_DescribeAccountLimitsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output for the  DescribeAccountLimits action.
      - **AccountLimits** *(list) --*

        An account limit structure that contain a list of AWS CloudFormation account limits and
        their values.
        - *(dict) --*

          The AccountLimit data type.
          CloudFormation has the following limits per account:
          * Number of concurrent resources
          * Number of stacks
          * Number of stack outputs
          For more information about these account limits, and other CloudFormation limits, see `AWS
          CloudFormation Limits
          <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
          in the *AWS CloudFormation User Guide* .
          - **Name** *(string) --*

            The name of the account limit.
            Values: ``ConcurrentResourcesLimit`` | ``StackLimit`` | ``StackOutputsLimit``
    """


_DescribeChangeSetPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeChangeSetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeChangeSetPaginatePaginationConfigTypeDef(
    _DescribeChangeSetPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef",
    {
        "Attribute": Literal[
            "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
        ],
        "Name": str,
        "RequiresRecreation": Literal["Never", "Conditionally", "Always"],
    },
    total=False,
)


class DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef(
    _DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef
):
    pass


_DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef",
    {
        "Target": DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTargetTypeDef,
        "Evaluation": Literal["Static", "Dynamic"],
        "ChangeSource": Literal[
            "ResourceReference",
            "ParameterReference",
            "ResourceAttribute",
            "DirectModification",
            "Automatic",
        ],
        "CausingEntity": str,
    },
    total=False,
)


class DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef(
    _DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef
):
    pass


_DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef",
    {
        "Action": Literal["Add", "Modify", "Remove", "Import"],
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Literal["True", "False", "Conditional"],
        "Scope": List[
            Literal[
                "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
            ]
        ],
        "Details": List[DescribeChangeSetPaginateResponseChangesResourceChangeDetailsTypeDef],
    },
    total=False,
)


class DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef(
    _DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef
):
    pass


_DescribeChangeSetPaginateResponseChangesTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseChangesTypeDef",
    {"Type": str, "ResourceChange": DescribeChangeSetPaginateResponseChangesResourceChangeTypeDef},
    total=False,
)


class DescribeChangeSetPaginateResponseChangesTypeDef(
    _DescribeChangeSetPaginateResponseChangesTypeDef
):
    pass


_DescribeChangeSetPaginateResponseParametersTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class DescribeChangeSetPaginateResponseParametersTypeDef(
    _DescribeChangeSetPaginateResponseParametersTypeDef
):
    pass


_DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)


class DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef(
    _DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef
):
    pass


_DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            DescribeChangeSetPaginateResponseRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef(
    _DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef
):
    pass


_DescribeChangeSetPaginateResponseTagsTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class DescribeChangeSetPaginateResponseTagsTypeDef(_DescribeChangeSetPaginateResponseTagsTypeDef):
    pass


_DescribeChangeSetPaginateResponseTypeDef = TypedDict(
    "_DescribeChangeSetPaginateResponseTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List[DescribeChangeSetPaginateResponseParametersTypeDef],
        "CreationTime": datetime,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": DescribeChangeSetPaginateResponseRollbackConfigurationTypeDef,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List[DescribeChangeSetPaginateResponseTagsTypeDef],
        "Changes": List[DescribeChangeSetPaginateResponseChangesTypeDef],
    },
    total=False,
)


class DescribeChangeSetPaginateResponseTypeDef(_DescribeChangeSetPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output for the  DescribeChangeSet action.
      - **ChangeSetName** *(string) --*

        The name of the change set.
    """


_DescribeStackEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeStackEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeStackEventsPaginatePaginationConfigTypeDef(
    _DescribeStackEventsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeStackEventsPaginateResponseStackEventsTypeDef = TypedDict(
    "_DescribeStackEventsPaginateResponseStackEventsTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class DescribeStackEventsPaginateResponseStackEventsTypeDef(
    _DescribeStackEventsPaginateResponseStackEventsTypeDef
):
    """
    - *(dict) --*

      The StackEvent data type.
      - **StackId** *(string) --*

        The unique ID name of the instance of the stack.
    """


_DescribeStackEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeStackEventsPaginateResponseTypeDef",
    {"StackEvents": List[DescribeStackEventsPaginateResponseStackEventsTypeDef]},
    total=False,
)


class DescribeStackEventsPaginateResponseTypeDef(_DescribeStackEventsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output for a  DescribeStackEvents action.
      - **StackEvents** *(list) --*

        A list of ``StackEvents`` structures.
        - *(dict) --*

          The StackEvent data type.
          - **StackId** *(string) --*

            The unique ID name of the instance of the stack.
    """


_DescribeStacksPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class DescribeStacksPaginatePaginationConfigTypeDef(_DescribeStacksPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeStacksPaginateResponseStacksDriftInformationTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksDriftInformationTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class DescribeStacksPaginateResponseStacksDriftInformationTypeDef(
    _DescribeStacksPaginateResponseStacksDriftInformationTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksOutputsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksOutputsTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str, "ExportName": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksOutputsTypeDef(
    _DescribeStacksPaginateResponseStacksOutputsTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksParametersTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksParametersTypeDef(
    _DescribeStacksPaginateResponseStacksParametersTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef",
    {"Arn": str, "Type": str},
    total=False,
)


class DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef(
    _DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            DescribeStacksPaginateResponseStacksRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef(
    _DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksTagsTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class DescribeStacksPaginateResponseStacksTagsTypeDef(
    _DescribeStacksPaginateResponseStacksTagsTypeDef
):
    pass


_DescribeStacksPaginateResponseStacksTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseStacksTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List[DescribeStacksPaginateResponseStacksParametersTypeDef],
        "CreationTime": datetime,
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": DescribeStacksPaginateResponseStacksRollbackConfigurationTypeDef,
        "StackStatus": Literal[
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
        ],
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Outputs": List[DescribeStacksPaginateResponseStacksOutputsTypeDef],
        "RoleARN": str,
        "Tags": List[DescribeStacksPaginateResponseStacksTagsTypeDef],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": DescribeStacksPaginateResponseStacksDriftInformationTypeDef,
    },
    total=False,
)


class DescribeStacksPaginateResponseStacksTypeDef(_DescribeStacksPaginateResponseStacksTypeDef):
    """
    - *(dict) --*

      The Stack data type.
      - **StackId** *(string) --*

        Unique identifier of the stack.
    """


_DescribeStacksPaginateResponseTypeDef = TypedDict(
    "_DescribeStacksPaginateResponseTypeDef",
    {"Stacks": List[DescribeStacksPaginateResponseStacksTypeDef]},
    total=False,
)


class DescribeStacksPaginateResponseTypeDef(_DescribeStacksPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output for a  DescribeStacks action.
      - **Stacks** *(list) --*

        A list of stack structures.
        - *(dict) --*

          The Stack data type.
          - **StackId** *(string) --*

            Unique identifier of the stack.
    """


_ListChangeSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListChangeSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListChangeSetsPaginatePaginationConfigTypeDef(_ListChangeSetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListChangeSetsPaginateResponseSummariesTypeDef = TypedDict(
    "_ListChangeSetsPaginateResponseSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
    },
    total=False,
)


class ListChangeSetsPaginateResponseSummariesTypeDef(
    _ListChangeSetsPaginateResponseSummariesTypeDef
):
    """
    - *(dict) --*

      The ``ChangeSetSummary`` structure describes a change set, its status, and the stack with
      which it's associated.
      - **StackId** *(string) --*

        The ID of the stack with which the change set is associated.
    """


_ListChangeSetsPaginateResponseTypeDef = TypedDict(
    "_ListChangeSetsPaginateResponseTypeDef",
    {"Summaries": List[ListChangeSetsPaginateResponseSummariesTypeDef]},
    total=False,
)


class ListChangeSetsPaginateResponseTypeDef(_ListChangeSetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output for the  ListChangeSets action.
      - **Summaries** *(list) --*

        A list of ``ChangeSetSummary`` structures that provides the ID and status of each change set
        for the specified stack.
        - *(dict) --*

          The ``ChangeSetSummary`` structure describes a change set, its status, and the stack with
          which it's associated.
          - **StackId** *(string) --*

            The ID of the stack with which the change set is associated.
    """


_ListExportsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListExportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListExportsPaginatePaginationConfigTypeDef(_ListExportsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListExportsPaginateResponseExportsTypeDef = TypedDict(
    "_ListExportsPaginateResponseExportsTypeDef",
    {"ExportingStackId": str, "Name": str, "Value": str},
    total=False,
)


class ListExportsPaginateResponseExportsTypeDef(_ListExportsPaginateResponseExportsTypeDef):
    """
    - *(dict) --*

      The ``Export`` structure describes the exported output values for a stack.
      - **ExportingStackId** *(string) --*

        The stack that contains the exported output name and value.
    """


_ListExportsPaginateResponseTypeDef = TypedDict(
    "_ListExportsPaginateResponseTypeDef",
    {"Exports": List[ListExportsPaginateResponseExportsTypeDef]},
    total=False,
)


class ListExportsPaginateResponseTypeDef(_ListExportsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Exports** *(list) --*

        The output for the  ListExports action.
        - *(dict) --*

          The ``Export`` structure describes the exported output values for a stack.
          - **ExportingStackId** *(string) --*

            The stack that contains the exported output name and value.
    """


_ListImportsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListImportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListImportsPaginatePaginationConfigTypeDef(_ListImportsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListImportsPaginateResponseTypeDef = TypedDict(
    "_ListImportsPaginateResponseTypeDef", {"Imports": List[str]}, total=False
)


class ListImportsPaginateResponseTypeDef(_ListImportsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Imports** *(list) --*

        A list of stack names that are importing the specified exported output value.
        - *(string) --*
    """


_ListStackInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStackInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStackInstancesPaginatePaginationConfigTypeDef(
    _ListStackInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStackInstancesPaginateResponseSummariesTypeDef = TypedDict(
    "_ListStackInstancesPaginateResponseSummariesTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StatusReason": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)


class ListStackInstancesPaginateResponseSummariesTypeDef(
    _ListStackInstancesPaginateResponseSummariesTypeDef
):
    """
    - *(dict) --*

      The structure that contains summary information about a stack instance.
      - **StackSetId** *(string) --*

        The name or unique ID of the stack set that the stack instance is associated with.
    """


_ListStackInstancesPaginateResponseTypeDef = TypedDict(
    "_ListStackInstancesPaginateResponseTypeDef",
    {"Summaries": List[ListStackInstancesPaginateResponseSummariesTypeDef]},
    total=False,
)


class ListStackInstancesPaginateResponseTypeDef(_ListStackInstancesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Summaries** *(list) --*

        A list of ``StackInstanceSummary`` structures that contain information about the specified
        stack instances.
        - *(dict) --*

          The structure that contains summary information about a stack instance.
          - **StackSetId** *(string) --*

            The name or unique ID of the stack set that the stack instance is associated with.
    """


_ListStackResourcesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStackResourcesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListStackResourcesPaginatePaginationConfigTypeDef(
    _ListStackResourcesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef = TypedDict(
    "_ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef(
    _ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef
):
    pass


_ListStackResourcesPaginateResponseStackResourceSummariesTypeDef = TypedDict(
    "_ListStackResourcesPaginateResponseStackResourceSummariesTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "DriftInformation": ListStackResourcesPaginateResponseStackResourceSummariesDriftInformationTypeDef,
    },
    total=False,
)


class ListStackResourcesPaginateResponseStackResourceSummariesTypeDef(
    _ListStackResourcesPaginateResponseStackResourceSummariesTypeDef
):
    """
    - *(dict) --*

      Contains high-level information about the specified stack resource.
      - **LogicalResourceId** *(string) --*

        The logical name of the resource specified in the template.
    """


_ListStackResourcesPaginateResponseTypeDef = TypedDict(
    "_ListStackResourcesPaginateResponseTypeDef",
    {
        "StackResourceSummaries": List[
            ListStackResourcesPaginateResponseStackResourceSummariesTypeDef
        ]
    },
    total=False,
)


class ListStackResourcesPaginateResponseTypeDef(_ListStackResourcesPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output for a  ListStackResources action.
      - **StackResourceSummaries** *(list) --*

        A list of ``StackResourceSummary`` structures.
        - *(dict) --*

          Contains high-level information about the specified stack resource.
          - **LogicalResourceId** *(string) --*

            The logical name of the resource specified in the template.
    """


_ListStackSetOperationResultsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStackSetOperationResultsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStackSetOperationResultsPaginatePaginationConfigTypeDef(
    _ListStackSetOperationResultsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef = TypedDict(
    "_ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef",
    {"Status": Literal["SUCCEEDED", "FAILED", "SKIPPED"], "StatusReason": str},
    total=False,
)


class ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef(
    _ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef
):
    pass


_ListStackSetOperationResultsPaginateResponseSummariesTypeDef = TypedDict(
    "_ListStackSetOperationResultsPaginateResponseSummariesTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StatusReason": str,
        "AccountGateResult": ListStackSetOperationResultsPaginateResponseSummariesAccountGateResultTypeDef,
    },
    total=False,
)


class ListStackSetOperationResultsPaginateResponseSummariesTypeDef(
    _ListStackSetOperationResultsPaginateResponseSummariesTypeDef
):
    """
    - *(dict) --*

      The structure that contains information about a specified operation's results for a given
      account in a given region.
      - **Account** *(string) --*

        The name of the AWS account for this operation result.
    """


_ListStackSetOperationResultsPaginateResponseTypeDef = TypedDict(
    "_ListStackSetOperationResultsPaginateResponseTypeDef",
    {"Summaries": List[ListStackSetOperationResultsPaginateResponseSummariesTypeDef]},
    total=False,
)


class ListStackSetOperationResultsPaginateResponseTypeDef(
    _ListStackSetOperationResultsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **Summaries** *(list) --*

        A list of ``StackSetOperationResultSummary`` structures that contain information about the
        specified operation results, for accounts and regions that are included in the operation.
        - *(dict) --*

          The structure that contains information about a specified operation's results for a given
          account in a given region.
          - **Account** *(string) --*

            The name of the AWS account for this operation result.
    """


_ListStackSetOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStackSetOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStackSetOperationsPaginatePaginationConfigTypeDef(
    _ListStackSetOperationsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStackSetOperationsPaginateResponseSummariesTypeDef = TypedDict(
    "_ListStackSetOperationsPaginateResponseSummariesTypeDef",
    {
        "OperationId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED"],
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)


class ListStackSetOperationsPaginateResponseSummariesTypeDef(
    _ListStackSetOperationsPaginateResponseSummariesTypeDef
):
    """
    - *(dict) --*

      The structures that contain summary information about the specified operation.
      - **OperationId** *(string) --*

        The unique ID of the stack set operation.
    """


_ListStackSetOperationsPaginateResponseTypeDef = TypedDict(
    "_ListStackSetOperationsPaginateResponseTypeDef",
    {"Summaries": List[ListStackSetOperationsPaginateResponseSummariesTypeDef]},
    total=False,
)


class ListStackSetOperationsPaginateResponseTypeDef(_ListStackSetOperationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Summaries** *(list) --*

        A list of ``StackSetOperationSummary`` structures that contain summary information about
        operations for the specified stack set.
        - *(dict) --*

          The structures that contain summary information about the specified operation.
          - **OperationId** *(string) --*

            The unique ID of the stack set operation.
    """


_ListStackSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStackSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStackSetsPaginatePaginationConfigTypeDef(_ListStackSetsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStackSetsPaginateResponseSummariesTypeDef = TypedDict(
    "_ListStackSetsPaginateResponseSummariesTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)


class ListStackSetsPaginateResponseSummariesTypeDef(_ListStackSetsPaginateResponseSummariesTypeDef):
    """
    - *(dict) --*

      The structures that contain summary information about the specified stack set.
      - **StackSetName** *(string) --*

        The name of the stack set.
    """


_ListStackSetsPaginateResponseTypeDef = TypedDict(
    "_ListStackSetsPaginateResponseTypeDef",
    {"Summaries": List[ListStackSetsPaginateResponseSummariesTypeDef]},
    total=False,
)


class ListStackSetsPaginateResponseTypeDef(_ListStackSetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Summaries** *(list) --*

        A list of ``StackSetSummary`` structures that contain information about the user's stack
        sets.
        - *(dict) --*

          The structures that contain summary information about the specified stack set.
          - **StackSetName** *(string) --*

            The name of the stack set.
    """


_ListStacksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListStacksPaginatePaginationConfigTypeDef(_ListStacksPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListStacksPaginateResponseStackSummariesDriftInformationTypeDef = TypedDict(
    "_ListStacksPaginateResponseStackSummariesDriftInformationTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class ListStacksPaginateResponseStackSummariesDriftInformationTypeDef(
    _ListStacksPaginateResponseStackSummariesDriftInformationTypeDef
):
    pass


_ListStacksPaginateResponseStackSummariesTypeDef = TypedDict(
    "_ListStacksPaginateResponseStackSummariesTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "TemplateDescription": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatus": Literal[
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
        ],
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": ListStacksPaginateResponseStackSummariesDriftInformationTypeDef,
    },
    total=False,
)


class ListStacksPaginateResponseStackSummariesTypeDef(
    _ListStacksPaginateResponseStackSummariesTypeDef
):
    """
    - *(dict) --*

      The StackSummary Data Type
      - **StackId** *(string) --*

        Unique stack identifier.
    """


_ListStacksPaginateResponseTypeDef = TypedDict(
    "_ListStacksPaginateResponseTypeDef",
    {"StackSummaries": List[ListStacksPaginateResponseStackSummariesTypeDef]},
    total=False,
)


class ListStacksPaginateResponseTypeDef(_ListStacksPaginateResponseTypeDef):
    """
    - *(dict) --*

      The output for  ListStacks action.
      - **StackSummaries** *(list) --*

        A list of ``StackSummary`` structures containing information about the specified stacks.
        - *(dict) --*

          The StackSummary Data Type
          - **StackId** *(string) --*

            Unique stack identifier.
    """


_ServiceResourceCreateStackParametersTypeDef = TypedDict(
    "_ServiceResourceCreateStackParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class ServiceResourceCreateStackParametersTypeDef(_ServiceResourceCreateStackParametersTypeDef):
    """
    - *(dict) --*

      The Parameter data type.
      - **ParameterKey** *(string) --*

        The key associated with the parameter. If you don't specify a key and value for a particular
        parameter, AWS CloudFormation uses the default value that is specified in your template.
    """


_RequiredServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef",
    {"Type": str},
    total=False,
)


class ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef,
):
    """
    - *(dict) --*

      A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
      of the alarms you specify goes to ALARM state during the stack operation or within the
      specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.
      - **Arn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the rollback trigger.
        If a specified trigger is missing, the entire stack operation fails and is rolled back.
    """


_ServiceResourceCreateStackRollbackConfigurationTypeDef = TypedDict(
    "_ServiceResourceCreateStackRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[
            ServiceResourceCreateStackRollbackConfigurationRollbackTriggersTypeDef
        ],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class ServiceResourceCreateStackRollbackConfigurationTypeDef(
    _ServiceResourceCreateStackRollbackConfigurationTypeDef
):
    """
    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.
    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.
      By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies
      them to any subsequent update operations for the stack, unless you specify otherwise. If you
      do specify rollback triggers for this parameter, those triggers replace any list of triggers
      previously specified for the stack. This means:
      * To use the rollback triggers previously specified for this stack, if any, don't specify this
      parameter.
      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating the
      stack or during a previous stack update). Any triggers that you don't include in the updated
      list of triggers are no longer applied to the stack.
      * To remove all currently specified triggers, specify an empty list for this parameter.
      If a specified trigger is missing, the entire stack operation fails and is rolled back.
      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
        any of the alarms you specify goes to ALARM state during the stack operation or within the
        specified monitoring period afterwards, CloudFormation rolls back the entire stack
        operation.
        - **Arn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the rollback trigger.
          If a specified trigger is missing, the entire stack operation fails and is rolled back.
    """


_RequiredServiceResourceCreateStackTagsTypeDef = TypedDict(
    "_RequiredServiceResourceCreateStackTagsTypeDef", {"Key": str}
)
_OptionalServiceResourceCreateStackTagsTypeDef = TypedDict(
    "_OptionalServiceResourceCreateStackTagsTypeDef", {"Value": str}, total=False
)


class ServiceResourceCreateStackTagsTypeDef(
    _RequiredServiceResourceCreateStackTagsTypeDef, _OptionalServiceResourceCreateStackTagsTypeDef
):
    """
    - *(dict) --*

      The Tag type enables you to specify a key-value pair that can be used to store information
      about an AWS CloudFormation stack.
      - **Key** *(string) --***[REQUIRED]**

        *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
        for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
    """


_StackCreateCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_StackCreateCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class StackCreateCompleteWaitWaiterConfigTypeDef(_StackCreateCompleteWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_StackDeleteCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_StackDeleteCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class StackDeleteCompleteWaitWaiterConfigTypeDef(_StackDeleteCompleteWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_StackExistsWaitWaiterConfigTypeDef = TypedDict(
    "_StackExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class StackExistsWaitWaiterConfigTypeDef(_StackExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 5
    """


_StackImportCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_StackImportCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class StackImportCompleteWaitWaiterConfigTypeDef(_StackImportCompleteWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_StackUpdateCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_StackUpdateCompleteWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class StackUpdateCompleteWaitWaiterConfigTypeDef(_StackUpdateCompleteWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """


_StackUpdateParametersTypeDef = TypedDict(
    "_StackUpdateParametersTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)


class StackUpdateParametersTypeDef(_StackUpdateParametersTypeDef):
    """
    - *(dict) --*

      The Parameter data type.
      - **ParameterKey** *(string) --*

        The key associated with the parameter. If you don't specify a key and value for a particular
        parameter, AWS CloudFormation uses the default value that is specified in your template.
    """


_StackUpdateResponseTypeDef = TypedDict(
    "_StackUpdateResponseTypeDef", {"StackId": str}, total=False
)


class StackUpdateResponseTypeDef(_StackUpdateResponseTypeDef):
    """
    - *(dict) --*

      The output for an  UpdateStack action.
      - **StackId** *(string) --*

        Unique identifier of the stack.
    """


_RequiredStackUpdateRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_RequiredStackUpdateRollbackConfigurationRollbackTriggersTypeDef", {"Arn": str}
)
_OptionalStackUpdateRollbackConfigurationRollbackTriggersTypeDef = TypedDict(
    "_OptionalStackUpdateRollbackConfigurationRollbackTriggersTypeDef", {"Type": str}, total=False
)


class StackUpdateRollbackConfigurationRollbackTriggersTypeDef(
    _RequiredStackUpdateRollbackConfigurationRollbackTriggersTypeDef,
    _OptionalStackUpdateRollbackConfigurationRollbackTriggersTypeDef,
):
    """
    - *(dict) --*

      A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If any
      of the alarms you specify goes to ALARM state during the stack operation or within the
      specified monitoring period afterwards, CloudFormation rolls back the entire stack operation.
      - **Arn** *(string) --***[REQUIRED]**

        The Amazon Resource Name (ARN) of the rollback trigger.
        If a specified trigger is missing, the entire stack operation fails and is rolled back.
    """


_StackUpdateRollbackConfigurationTypeDef = TypedDict(
    "_StackUpdateRollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List[StackUpdateRollbackConfigurationRollbackTriggersTypeDef],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)


class StackUpdateRollbackConfigurationTypeDef(_StackUpdateRollbackConfigurationTypeDef):
    """
    The rollback triggers for AWS CloudFormation to monitor during stack creation and updating
    operations, and for the specified monitoring period afterwards.
    - **RollbackTriggers** *(list) --*

      The triggers to monitor during stack creation or update actions.
      By default, AWS CloudFormation saves the rollback triggers specified for a stack and applies
      them to any subsequent update operations for the stack, unless you specify otherwise. If you
      do specify rollback triggers for this parameter, those triggers replace any list of triggers
      previously specified for the stack. This means:
      * To use the rollback triggers previously specified for this stack, if any, don't specify this
      parameter.
      * To specify new or updated rollback triggers, you must specify *all* the triggers that you
      want used for this stack, even triggers you've specifed before (for example, when creating the
      stack or during a previous stack update). Any triggers that you don't include in the updated
      list of triggers are no longer applied to the stack.
      * To remove all currently specified triggers, specify an empty list for this parameter.
      If a specified trigger is missing, the entire stack operation fails and is rolled back.
      - *(dict) --*

        A rollback trigger AWS CloudFormation monitors during creation and updating of stacks. If
        any of the alarms you specify goes to ALARM state during the stack operation or within the
        specified monitoring period afterwards, CloudFormation rolls back the entire stack
        operation.
        - **Arn** *(string) --***[REQUIRED]**

          The Amazon Resource Name (ARN) of the rollback trigger.
          If a specified trigger is missing, the entire stack operation fails and is rolled back.
    """


_RequiredStackUpdateTagsTypeDef = TypedDict("_RequiredStackUpdateTagsTypeDef", {"Key": str})
_OptionalStackUpdateTagsTypeDef = TypedDict(
    "_OptionalStackUpdateTagsTypeDef", {"Value": str}, total=False
)


class StackUpdateTagsTypeDef(_RequiredStackUpdateTagsTypeDef, _OptionalStackUpdateTagsTypeDef):
    """
    - *(dict) --*

      The Tag type enables you to specify a key-value pair that can be used to store information
      about an AWS CloudFormation stack.
      - **Key** *(string) --***[REQUIRED]**

        *Required* . A string used to identify this tag. You can specify a maximum of 128 characters
        for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: ``aws:`` .
    """


_TypeRegistrationCompleteWaitWaiterConfigTypeDef = TypedDict(
    "_TypeRegistrationCompleteWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class TypeRegistrationCompleteWaitWaiterConfigTypeDef(
    _TypeRegistrationCompleteWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 30
    """
