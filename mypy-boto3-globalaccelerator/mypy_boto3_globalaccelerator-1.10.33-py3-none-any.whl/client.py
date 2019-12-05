"Main interface for globalaccelerator service Client"
from __future__ import annotations

import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_globalaccelerator.client as client_scope

# pylint: disable=import-self
import mypy_boto3_globalaccelerator.paginator as paginator_scope
from mypy_boto3_globalaccelerator.type_defs import (
    ClientCreateAcceleratorResponseTypeDef,
    ClientCreateEndpointGroupEndpointConfigurationsTypeDef,
    ClientCreateEndpointGroupResponseTypeDef,
    ClientCreateListenerPortRangesTypeDef,
    ClientCreateListenerResponseTypeDef,
    ClientDescribeAcceleratorAttributesResponseTypeDef,
    ClientDescribeAcceleratorResponseTypeDef,
    ClientDescribeEndpointGroupResponseTypeDef,
    ClientDescribeListenerResponseTypeDef,
    ClientListAcceleratorsResponseTypeDef,
    ClientListEndpointGroupsResponseTypeDef,
    ClientListListenersResponseTypeDef,
    ClientUpdateAcceleratorAttributesResponseTypeDef,
    ClientUpdateAcceleratorResponseTypeDef,
    ClientUpdateEndpointGroupEndpointConfigurationsTypeDef,
    ClientUpdateEndpointGroupResponseTypeDef,
    ClientUpdateListenerPortRangesTypeDef,
    ClientUpdateListenerResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Client",)


class Client(BaseClient):
    """
    [GlobalAccelerator.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client)
    """

    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.can_paginate)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_accelerator(
        self, Name: str, IdempotencyToken: str, IpAddressType: str = None, Enabled: bool = None
    ) -> ClientCreateAcceleratorResponseTypeDef:
        """
        [Client.create_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_accelerator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_endpoint_group(
        self,
        ListenerArn: str,
        EndpointGroupRegion: str,
        IdempotencyToken: str,
        EndpointConfigurations: List[ClientCreateEndpointGroupEndpointConfigurationsTypeDef] = None,
        TrafficDialPercentage: Any = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: Literal["TCP", "HTTP", "HTTPS"] = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
    ) -> ClientCreateEndpointGroupResponseTypeDef:
        """
        [Client.create_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_listener(
        self,
        AcceleratorArn: str,
        PortRanges: List[ClientCreateListenerPortRangesTypeDef],
        Protocol: Literal["TCP", "UDP"],
        IdempotencyToken: str,
        ClientAffinity: Literal["NONE", "SOURCE_IP"] = None,
    ) -> ClientCreateListenerResponseTypeDef:
        """
        [Client.create_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_listener)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_accelerator(self, AcceleratorArn: str) -> None:
        """
        [Client.delete_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_accelerator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_endpoint_group(self, EndpointGroupArn: str) -> None:
        """
        [Client.delete_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_listener(self, ListenerArn: str) -> None:
        """
        [Client.delete_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_listener)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_accelerator(self, AcceleratorArn: str) -> ClientDescribeAcceleratorResponseTypeDef:
        """
        [Client.describe_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_accelerator_attributes(
        self, AcceleratorArn: str
    ) -> ClientDescribeAcceleratorAttributesResponseTypeDef:
        """
        [Client.describe_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_endpoint_group(
        self, EndpointGroupArn: str
    ) -> ClientDescribeEndpointGroupResponseTypeDef:
        """
        [Client.describe_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_listener(self, ListenerArn: str) -> ClientDescribeListenerResponseTypeDef:
        """
        [Client.describe_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_listener)
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
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.generate_presigned_url)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_accelerators(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListAcceleratorsResponseTypeDef:
        """
        [Client.list_accelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_accelerators)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_endpoint_groups(
        self, ListenerArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListEndpointGroupsResponseTypeDef:
        """
        [Client.list_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_endpoint_groups)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_listeners(
        self, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListListenersResponseTypeDef:
        """
        [Client.list_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_listeners)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_accelerator(
        self, AcceleratorArn: str, Name: str = None, IpAddressType: str = None, Enabled: bool = None
    ) -> ClientUpdateAcceleratorResponseTypeDef:
        """
        [Client.update_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_accelerator_attributes(
        self,
        AcceleratorArn: str,
        FlowLogsEnabled: bool = None,
        FlowLogsS3Bucket: str = None,
        FlowLogsS3Prefix: str = None,
    ) -> ClientUpdateAcceleratorAttributesResponseTypeDef:
        """
        [Client.update_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator_attributes)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_endpoint_group(
        self,
        EndpointGroupArn: str,
        EndpointConfigurations: List[ClientUpdateEndpointGroupEndpointConfigurationsTypeDef] = None,
        TrafficDialPercentage: Any = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: Literal["TCP", "HTTP", "HTTPS"] = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
    ) -> ClientUpdateEndpointGroupResponseTypeDef:
        """
        [Client.update_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_endpoint_group)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_listener(
        self,
        ListenerArn: str,
        PortRanges: List[ClientUpdateListenerPortRangesTypeDef] = None,
        Protocol: Literal["TCP", "UDP"] = None,
        ClientAffinity: Literal["NONE", "SOURCE_IP"] = None,
    ) -> ClientUpdateListenerResponseTypeDef:
        """
        [Client.update_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_listener)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_accelerators"]
    ) -> paginator_scope.ListAcceleratorsPaginator:
        """
        [Paginator.ListAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_endpoint_groups"]
    ) -> paginator_scope.ListEndpointGroupsPaginator:
        """
        [Paginator.ListEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_listeners"]
    ) -> paginator_scope.ListListenersPaginator:
        """
        [Paginator.ListListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)
        """


class Exceptions:
    AcceleratorNotDisabledException: Boto3ClientError
    AcceleratorNotFoundException: Boto3ClientError
    AccessDeniedException: Boto3ClientError
    AssociatedEndpointGroupFoundException: Boto3ClientError
    AssociatedListenerFoundException: Boto3ClientError
    ClientError: Boto3ClientError
    EndpointGroupAlreadyExistsException: Boto3ClientError
    EndpointGroupNotFoundException: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidArgumentException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidPortRangeException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ListenerNotFoundException: Boto3ClientError
