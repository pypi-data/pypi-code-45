"Main interface for sns service ServiceResource"
from __future__ import annotations

from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_sns.service_resource as service_resource_scope
from mypy_boto3_sns.type_defs import (
    PlatformEndpointPublishMessageAttributesTypeDef,
    PlatformEndpointPublishResponseTypeDef,
    ServiceResourceCreateTopicTagsTypeDef,
    TopicPublishMessageAttributesTypeDef,
    TopicPublishResponseTypeDef,
)


__all__ = (
    "ServiceResource",
    "PlatformApplication",
    "PlatformEndpoint",
    "Subscription",
    "Topic",
    "ServiceResourcePlatformApplicationsCollection",
    "ServiceResourceSubscriptionsCollection",
    "ServiceResourceTopicsCollection",
    "PlatformApplicationEndpointsCollection",
    "TopicSubscriptionsCollection",
)


class ServiceResource(Boto3ServiceResource):
    """
    [SNS.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource)
    """

    platform_applications: service_resource_scope.ServiceResourcePlatformApplicationsCollection
    subscriptions: service_resource_scope.ServiceResourceSubscriptionsCollection
    topics: service_resource_scope.ServiceResourceTopicsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def PlatformApplication(self, arn: str) -> service_resource_scope.PlatformApplication:
        """
        [ServiceResource.PlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def PlatformEndpoint(self, arn: str) -> service_resource_scope.PlatformEndpoint:
        """
        [ServiceResource.PlatformEndpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Subscription(self, arn: str) -> service_resource_scope.Subscription:
        """
        [ServiceResource.Subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.Subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Topic(self, arn: str) -> service_resource_scope.Topic:
        """
        [ServiceResource.Topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.Topic)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_platform_application(
        self, Name: str, Platform: str, Attributes: Dict[str, str]
    ) -> service_resource_scope.PlatformApplication:
        """
        [ServiceResource.create_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.create_platform_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_topic(
        self,
        Name: str,
        Attributes: Dict[str, str] = None,
        Tags: List[ServiceResourceCreateTopicTagsTypeDef] = None,
    ) -> service_resource_scope.Topic:
        """
        [ServiceResource.create_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.create_topic)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.get_available_subresources)
        """


class PlatformApplication(Boto3ServiceResource):
    """
    [PlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
    """

    attributes: Dict[str, Any]
    arn: str
    endpoints: service_resource_scope.PlatformApplicationEndpointsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_platform_endpoint(
        self, Token: str, CustomUserData: str = None, Attributes: Dict[str, str] = None
    ) -> service_resource_scope.PlatformEndpoint:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
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
    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        pass


class PlatformEndpoint(Boto3ServiceResource):
    """
    [PlatformEndpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
    """

    attributes: Dict[str, Any]
    arn: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def publish(
        self,
        Message: str,
        TopicArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, PlatformEndpointPublishMessageAttributesTypeDef] = None,
    ) -> PlatformEndpointPublishResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        pass


class Subscription(Boto3ServiceResource):
    """
    [Subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.Subscription)
    """

    attributes: Dict[str, Any]
    arn: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
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
    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        pass


class Topic(Boto3ServiceResource):
    """
    [Topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.Topic)
    """

    attributes: Dict[str, Any]
    arn: str
    subscriptions: service_resource_scope.TopicSubscriptionsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_permission(self, Label: str, AWSAccountId: List[str], ActionName: List[str]) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_subscription(
        self, Token: str, AuthenticateOnUnsubscribe: str = None
    ) -> service_resource_scope.Subscription:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def publish(
        self,
        Message: str,
        TargetArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, TopicPublishMessageAttributesTypeDef] = None,
    ) -> TopicPublishResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_permission(self, Label: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def subscribe(
        self,
        Protocol: str,
        Endpoint: str = None,
        Attributes: Dict[str, str] = None,
        ReturnSubscriptionArn: bool = None,
    ) -> service_resource_scope.Subscription:
        pass


class ServiceResourcePlatformApplicationsCollection(ResourceCollection):
    """
    [ServiceResource.platform_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.platform_applications)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.PlatformApplication]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, NextToken: str = None) -> List[service_resource_scope.PlatformApplication]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.PlatformApplication]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.PlatformApplication]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceSubscriptionsCollection(ResourceCollection):
    """
    [ServiceResource.subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.subscriptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Subscription]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, NextToken: str = None) -> List[service_resource_scope.Subscription]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Subscription]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Subscription]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class ServiceResourceTopicsCollection(ResourceCollection):
    """
    [ServiceResource.topics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.ServiceResource.topics)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Topic]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, NextToken: str = None) -> List[service_resource_scope.Topic]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Topic]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Topic]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class PlatformApplicationEndpointsCollection(ResourceCollection):
    """
    [PlatformApplication.endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.PlatformApplication.endpoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.PlatformEndpoint]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, NextToken: str = None) -> List[service_resource_scope.PlatformEndpoint]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.PlatformEndpoint]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.PlatformEndpoint]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass


class TopicSubscriptionsCollection(ResourceCollection):
    """
    [Topic.subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.Topic.subscriptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Subscription]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, NextToken: str = None) -> List[service_resource_scope.Subscription]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Subscription]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Subscription]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        pass
