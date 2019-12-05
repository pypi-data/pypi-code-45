"Main interface for cloudformation service ServiceResource"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_cloudformation.service_resource as service_resource_scope
from mypy_boto3_cloudformation.type_defs import (
    ServiceResourceCreateStackParametersTypeDef,
    ServiceResourceCreateStackRollbackConfigurationTypeDef,
    ServiceResourceCreateStackTagsTypeDef,
    StackUpdateParametersTypeDef,
    StackUpdateResponseTypeDef,
    StackUpdateRollbackConfigurationTypeDef,
    StackUpdateTagsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ServiceResource",
    "Event",
    "Stack",
    "StackResource",
    "StackResourceSummary",
    "ServiceResourceStacksCollection",
    "StackEventsCollection",
    "StackResourceSummariesCollection",
)


class ServiceResource(Boto3ServiceResource):
    """
    [CloudFormation.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource)
    """

    stacks: service_resource_scope.ServiceResourceStacksCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Event(self, id: str) -> service_resource_scope.Event:
        """
        [ServiceResource.Event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.Event)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Stack(self, name: str) -> service_resource_scope.Stack:
        """
        [ServiceResource.Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.Stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def StackResource(
        self, stack_name: str, logical_id: str
    ) -> service_resource_scope.StackResource:
        """
        [ServiceResource.StackResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResource)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def StackResourceSummary(
        self, stack_name: str, logical_id: str
    ) -> service_resource_scope.StackResourceSummary:
        """
        [ServiceResource.StackResourceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResourceSummary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stack(
        self,
        StackName: str,
        TemplateBody: str = None,
        TemplateURL: str = None,
        Parameters: List[ServiceResourceCreateStackParametersTypeDef] = None,
        DisableRollback: bool = None,
        RollbackConfiguration: ServiceResourceCreateStackRollbackConfigurationTypeDef = None,
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
        Tags: List[ServiceResourceCreateStackTagsTypeDef] = None,
        ClientRequestToken: str = None,
        EnableTerminationProtection: bool = None,
    ) -> service_resource_scope.Stack:
        """
        [ServiceResource.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.create_stack)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.get_available_subresources)
        """


class Event(Boto3ServiceResource):
    """
    [Event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.Event)
    """

    stack_id: str
    event_id: str
    stack_name: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    timestamp: datetime
    resource_status: str
    resource_status_reason: str
    resource_properties: str
    client_request_token: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass


class Stack(Boto3ServiceResource):
    """
    [Stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.Stack)
    """

    stack_id: str
    stack_name: str
    change_set_id: str
    description: str
    parameters: List[Any]
    creation_time: datetime
    deletion_time: datetime
    last_updated_time: datetime
    rollback_configuration: Dict[str, Any]
    stack_status: str
    stack_status_reason: str
    disable_rollback: bool
    notification_arns: List[Any]
    timeout_in_minutes: int
    capabilities: List[Any]
    outputs: List[Any]
    role_arn: str
    tags: List[Any]
    enable_termination_protection: bool
    parent_id: str
    root_id: str
    drift_information: Dict[str, Any]
    name: str
    events: service_resource_scope.StackEventsCollection
    resource_summaries: service_resource_scope.StackResourceSummariesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def cancel_update(self, ClientRequestToken: str = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(
        self, RetainResources: List[str] = None, RoleARN: str = None, ClientRequestToken: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self,
        TemplateBody: str = None,
        TemplateURL: str = None,
        UsePreviousTemplate: bool = None,
        StackPolicyDuringUpdateBody: str = None,
        StackPolicyDuringUpdateURL: str = None,
        Parameters: List[StackUpdateParametersTypeDef] = None,
        Capabilities: List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ] = None,
        ResourceTypes: List[str] = None,
        RoleARN: str = None,
        RollbackConfiguration: StackUpdateRollbackConfigurationTypeDef = None,
        StackPolicyBody: str = None,
        StackPolicyURL: str = None,
        NotificationARNs: List[str] = None,
        Tags: List[StackUpdateTagsTypeDef] = None,
        ClientRequestToken: str = None,
    ) -> StackUpdateResponseTypeDef:
        pass


class StackResource(Boto3ServiceResource):
    """
    [StackResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResource)
    """

    stack_id: str
    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    description: str
    metadata: str
    drift_information: Dict[str, Any]
    stack_name: str
    logical_id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass


class StackResourceSummary(Boto3ServiceResource):
    """
    [StackResourceSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.StackResourceSummary)
    """

    logical_resource_id: str
    physical_resource_id: str
    resource_type: str
    last_updated_timestamp: datetime
    resource_status: str
    resource_status_reason: str
    drift_information: Dict[str, Any]
    stack_name: str
    logical_id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass


class ServiceResourceStacksCollection(ResourceCollection):
    """
    [ServiceResource.stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.ServiceResource.stacks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Stack]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, StackName: str = None, NextToken: str = None
    ) -> List[service_resource_scope.Stack]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Stack]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Stack]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class StackEventsCollection(ResourceCollection):
    """
    [Stack.events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Stack.events)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Event]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, NextToken: str = None) -> List[service_resource_scope.Event]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Event]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Event]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class StackResourceSummariesCollection(ResourceCollection):
    """
    [Stack.resource_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/cloudformation.html#CloudFormation.Stack.resource_summaries)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.StackResourceSummary]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, NextToken: str = None) -> List[service_resource_scope.StackResourceSummary]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.StackResourceSummary]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.StackResourceSummary]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass
