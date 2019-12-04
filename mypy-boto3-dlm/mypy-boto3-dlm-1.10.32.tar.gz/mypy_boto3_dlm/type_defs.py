"Main interface for dlm service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    "ClientCreateLifecyclePolicyPolicyDetailsTypeDef",
    "ClientCreateLifecyclePolicyResponseTypeDef",
    "ClientGetLifecyclePoliciesResponsePoliciesTypeDef",
    "ClientGetLifecyclePoliciesResponseTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef",
    "ClientGetLifecyclePolicyResponsePolicyTypeDef",
    "ClientGetLifecyclePolicyResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    "ClientUpdateLifecyclePolicyPolicyDetailsTypeDef",
)


_ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef",
    {"ExcludeBootVolume": bool},
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef
):
    pass


_ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Interval": int, "IntervalUnit": str, "Times": List[str]},
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef
):
    pass


_ClientCreateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    {
        "Count": int,
        "Interval": int,
        "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"],
        "AvailabilityZones": List[str],
    },
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef
):
    pass


_ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    {"Count": int, "Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef
):
    pass


_ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef
):
    pass


_ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef
):
    pass


_ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List[ClientCreateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef],
        "VariableTags": List[ClientCreateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef],
        "CreateRule": ClientCreateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
        "RetainRule": ClientCreateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef,
        "FastRestoreRule": ClientCreateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef,
    },
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef
):
    pass


_ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef
):
    pass


_ClientCreateLifecyclePolicyPolicyDetailsTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyPolicyDetailsTypeDef",
    {
        "PolicyType": str,
        "ResourceTypes": List[Literal["VOLUME", "INSTANCE"]],
        "TargetTags": List[ClientCreateLifecyclePolicyPolicyDetailsTargetTagsTypeDef],
        "Schedules": List[ClientCreateLifecyclePolicyPolicyDetailsSchedulesTypeDef],
        "Parameters": ClientCreateLifecyclePolicyPolicyDetailsParametersTypeDef,
    },
    total=False,
)


class ClientCreateLifecyclePolicyPolicyDetailsTypeDef(
    _ClientCreateLifecyclePolicyPolicyDetailsTypeDef
):
    """
    The configuration details of the lifecycle policy.
    - **PolicyType** *(string) --*

      This field determines the valid target resource types and actions a policy can manage. This
      field defaults to EBS_SNAPSHOT_MANAGEMENT if not present.
    """


_ClientCreateLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientCreateLifecyclePolicyResponseTypeDef", {"PolicyId": str}, total=False
)


class ClientCreateLifecyclePolicyResponseTypeDef(_ClientCreateLifecyclePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **PolicyId** *(string) --*

        The identifier of the lifecycle policy.
    """


_ClientGetLifecyclePoliciesResponsePoliciesTypeDef = TypedDict(
    "_ClientGetLifecyclePoliciesResponsePoliciesTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": Literal["ENABLED", "DISABLED", "ERROR"],
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientGetLifecyclePoliciesResponsePoliciesTypeDef(
    _ClientGetLifecyclePoliciesResponsePoliciesTypeDef
):
    """
    - *(dict) --*

      Summary information about a lifecycle policy.
      - **PolicyId** *(string) --*

        The identifier of the lifecycle policy.
    """


_ClientGetLifecyclePoliciesResponseTypeDef = TypedDict(
    "_ClientGetLifecyclePoliciesResponseTypeDef",
    {"Policies": List[ClientGetLifecyclePoliciesResponsePoliciesTypeDef]},
    total=False,
)


class ClientGetLifecyclePoliciesResponseTypeDef(_ClientGetLifecyclePoliciesResponseTypeDef):
    """
    - *(dict) --*

      - **Policies** *(list) --*

        Summary information about the lifecycle policies.
        - *(dict) --*

          Summary information about a lifecycle policy.
          - **PolicyId** *(string) --*

            The identifier of the lifecycle policy.
    """


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef",
    {"ExcludeBootVolume": bool},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef
):
    pass


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Interval": int, "IntervalUnit": str, "Times": List[str]},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef
):
    pass


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    {
        "Count": int,
        "Interval": int,
        "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"],
        "AvailabilityZones": List[str],
    },
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef
):
    pass


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    {"Count": int, "Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef
):
    pass


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef
):
    pass


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef
):
    pass


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List[
            ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTagsToAddTypeDef
        ],
        "VariableTags": List[
            ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesVariableTagsTypeDef
        ],
        "CreateRule": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
        "RetainRule": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesRetainRuleTypeDef,
        "FastRestoreRule": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef,
    },
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef
):
    pass


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef
):
    pass


_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef",
    {
        "PolicyType": str,
        "ResourceTypes": List[Literal["VOLUME", "INSTANCE"]],
        "TargetTags": List[ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTargetTagsTypeDef],
        "Schedules": List[ClientGetLifecyclePolicyResponsePolicyPolicyDetailsSchedulesTypeDef],
        "Parameters": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsParametersTypeDef,
    },
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef(
    _ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef
):
    pass


_ClientGetLifecyclePolicyResponsePolicyTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponsePolicyTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": Literal["ENABLED", "DISABLED", "ERROR"],
        "StatusMessage": str,
        "ExecutionRoleArn": str,
        "DateCreated": datetime,
        "DateModified": datetime,
        "PolicyDetails": ClientGetLifecyclePolicyResponsePolicyPolicyDetailsTypeDef,
        "Tags": Dict[str, str],
        "PolicyArn": str,
    },
    total=False,
)


class ClientGetLifecyclePolicyResponsePolicyTypeDef(_ClientGetLifecyclePolicyResponsePolicyTypeDef):
    """
    - **Policy** *(dict) --*

      Detailed information about the lifecycle policy.
      - **PolicyId** *(string) --*

        The identifier of the lifecycle policy.
    """


_ClientGetLifecyclePolicyResponseTypeDef = TypedDict(
    "_ClientGetLifecyclePolicyResponseTypeDef",
    {"Policy": ClientGetLifecyclePolicyResponsePolicyTypeDef},
    total=False,
)


class ClientGetLifecyclePolicyResponseTypeDef(_ClientGetLifecyclePolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(dict) --*

        Detailed information about the lifecycle policy.
        - **PolicyId** *(string) --*

          The identifier of the lifecycle policy.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(dict) --*

        Information about the tags.
        - *(string) --*

          - *(string) --*
    """


_ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef",
    {"ExcludeBootVolume": bool},
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef
):
    pass


_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef",
    {"Interval": int, "IntervalUnit": str, "Times": List[str]},
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef
):
    pass


_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef",
    {
        "Count": int,
        "Interval": int,
        "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"],
        "AvailabilityZones": List[str],
    },
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef
):
    pass


_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef",
    {"Count": int, "Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef
):
    pass


_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef
):
    pass


_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef
):
    pass


_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List[ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTagsToAddTypeDef],
        "VariableTags": List[ClientUpdateLifecyclePolicyPolicyDetailsSchedulesVariableTagsTypeDef],
        "CreateRule": ClientUpdateLifecyclePolicyPolicyDetailsSchedulesCreateRuleTypeDef,
        "RetainRule": ClientUpdateLifecyclePolicyPolicyDetailsSchedulesRetainRuleTypeDef,
        "FastRestoreRule": ClientUpdateLifecyclePolicyPolicyDetailsSchedulesFastRestoreRuleTypeDef,
    },
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef
):
    pass


_ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef
):
    pass


_ClientUpdateLifecyclePolicyPolicyDetailsTypeDef = TypedDict(
    "_ClientUpdateLifecyclePolicyPolicyDetailsTypeDef",
    {
        "PolicyType": str,
        "ResourceTypes": List[Literal["VOLUME", "INSTANCE"]],
        "TargetTags": List[ClientUpdateLifecyclePolicyPolicyDetailsTargetTagsTypeDef],
        "Schedules": List[ClientUpdateLifecyclePolicyPolicyDetailsSchedulesTypeDef],
        "Parameters": ClientUpdateLifecyclePolicyPolicyDetailsParametersTypeDef,
    },
    total=False,
)


class ClientUpdateLifecyclePolicyPolicyDetailsTypeDef(
    _ClientUpdateLifecyclePolicyPolicyDetailsTypeDef
):
    """
    The configuration of the lifecycle policy. You cannot update the policy type or the resource
    type.
    - **PolicyType** *(string) --*

      This field determines the valid target resource types and actions a policy can manage. This
      field defaults to EBS_SNAPSHOT_MANAGEMENT if not present.
    """
