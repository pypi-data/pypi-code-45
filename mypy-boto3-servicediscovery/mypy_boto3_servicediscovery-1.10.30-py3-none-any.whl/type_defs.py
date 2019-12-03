"Main interface for servicediscovery service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateHttpNamespaceResponseTypeDef",
    "ClientCreatePrivateDnsNamespaceResponseTypeDef",
    "ClientCreatePublicDnsNamespaceResponseTypeDef",
    "ClientCreateServiceDnsConfigDnsRecordsTypeDef",
    "ClientCreateServiceDnsConfigTypeDef",
    "ClientCreateServiceHealthCheckConfigTypeDef",
    "ClientCreateServiceHealthCheckCustomConfigTypeDef",
    "ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef",
    "ClientCreateServiceResponseServiceDnsConfigTypeDef",
    "ClientCreateServiceResponseServiceHealthCheckConfigTypeDef",
    "ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef",
    "ClientCreateServiceResponseServiceTypeDef",
    "ClientCreateServiceResponseTypeDef",
    "ClientDeleteNamespaceResponseTypeDef",
    "ClientDeregisterInstanceResponseTypeDef",
    "ClientDiscoverInstancesResponseInstancesTypeDef",
    "ClientDiscoverInstancesResponseTypeDef",
    "ClientGetInstanceResponseInstanceTypeDef",
    "ClientGetInstanceResponseTypeDef",
    "ClientGetInstancesHealthStatusResponseTypeDef",
    "ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef",
    "ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef",
    "ClientGetNamespaceResponseNamespacePropertiesTypeDef",
    "ClientGetNamespaceResponseNamespaceTypeDef",
    "ClientGetNamespaceResponseTypeDef",
    "ClientGetOperationResponseOperationTypeDef",
    "ClientGetOperationResponseTypeDef",
    "ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef",
    "ClientGetServiceResponseServiceDnsConfigTypeDef",
    "ClientGetServiceResponseServiceHealthCheckConfigTypeDef",
    "ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef",
    "ClientGetServiceResponseServiceTypeDef",
    "ClientGetServiceResponseTypeDef",
    "ClientListInstancesResponseInstancesTypeDef",
    "ClientListInstancesResponseTypeDef",
    "ClientListNamespacesFiltersTypeDef",
    "ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef",
    "ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef",
    "ClientListNamespacesResponseNamespacesPropertiesTypeDef",
    "ClientListNamespacesResponseNamespacesTypeDef",
    "ClientListNamespacesResponseTypeDef",
    "ClientListOperationsFiltersTypeDef",
    "ClientListOperationsResponseOperationsTypeDef",
    "ClientListOperationsResponseTypeDef",
    "ClientListServicesFiltersTypeDef",
    "ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef",
    "ClientListServicesResponseServicesDnsConfigTypeDef",
    "ClientListServicesResponseServicesHealthCheckConfigTypeDef",
    "ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef",
    "ClientListServicesResponseServicesTypeDef",
    "ClientListServicesResponseTypeDef",
    "ClientRegisterInstanceResponseTypeDef",
    "ClientUpdateServiceResponseTypeDef",
    "ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef",
    "ClientUpdateServiceServiceDnsConfigTypeDef",
    "ClientUpdateServiceServiceHealthCheckConfigTypeDef",
    "ClientUpdateServiceServiceTypeDef",
    "ListInstancesPaginatePaginationConfigTypeDef",
    "ListInstancesPaginateResponseInstancesTypeDef",
    "ListInstancesPaginateResponseTypeDef",
    "ListNamespacesPaginateFiltersTypeDef",
    "ListNamespacesPaginatePaginationConfigTypeDef",
    "ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef",
    "ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef",
    "ListNamespacesPaginateResponseNamespacesPropertiesTypeDef",
    "ListNamespacesPaginateResponseNamespacesTypeDef",
    "ListNamespacesPaginateResponseTypeDef",
    "ListOperationsPaginateFiltersTypeDef",
    "ListOperationsPaginatePaginationConfigTypeDef",
    "ListOperationsPaginateResponseOperationsTypeDef",
    "ListOperationsPaginateResponseTypeDef",
    "ListServicesPaginateFiltersTypeDef",
    "ListServicesPaginatePaginationConfigTypeDef",
    "ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef",
    "ListServicesPaginateResponseServicesDnsConfigTypeDef",
    "ListServicesPaginateResponseServicesHealthCheckConfigTypeDef",
    "ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef",
    "ListServicesPaginateResponseServicesTypeDef",
    "ListServicesPaginateResponseTypeDef",
)


_ClientCreateHttpNamespaceResponseTypeDef = TypedDict(
    "_ClientCreateHttpNamespaceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientCreateHttpNamespaceResponseTypeDef(_ClientCreateHttpNamespaceResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        A value that you can use to determine whether the request completed successfully. To get the
        status of the operation, see  GetOperation .
    """


_ClientCreatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "_ClientCreatePrivateDnsNamespaceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientCreatePrivateDnsNamespaceResponseTypeDef(
    _ClientCreatePrivateDnsNamespaceResponseTypeDef
):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        A value that you can use to determine whether the request completed successfully. To get the
        status of the operation, see  GetOperation .
    """


_ClientCreatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "_ClientCreatePublicDnsNamespaceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientCreatePublicDnsNamespaceResponseTypeDef(_ClientCreatePublicDnsNamespaceResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        A value that you can use to determine whether the request completed successfully. To get the
        status of the operation, see  GetOperation .
    """


_ClientCreateServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ClientCreateServiceDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)


class ClientCreateServiceDnsConfigDnsRecordsTypeDef(_ClientCreateServiceDnsConfigDnsRecordsTypeDef):
    pass


_ClientCreateServiceDnsConfigTypeDef = TypedDict(
    "_ClientCreateServiceDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"],
        "DnsRecords": List[ClientCreateServiceDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)


class ClientCreateServiceDnsConfigTypeDef(_ClientCreateServiceDnsConfigTypeDef):
    """
    A complex type that contains information about the Amazon Route 53 records that you want AWS
    Cloud Map to create when you register an instance.
    - **NamespaceId** *(string) --*

      The ID of the namespace to use for DNS configuration.
    """


_ClientCreateServiceHealthCheckConfigTypeDef = TypedDict(
    "_ClientCreateServiceHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ClientCreateServiceHealthCheckConfigTypeDef(_ClientCreateServiceHealthCheckConfigTypeDef):
    """
    *Public DNS namespaces only.* A complex type that contains settings for an optional Route 53
    health check. If you specify settings for a health check, AWS Cloud Map associates the health
    check with all the Route 53 DNS records that you specify in ``DnsConfig`` .
    .. warning::

      If you specify a health check configuration, you can specify either
      ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.
    """


_ClientCreateServiceHealthCheckCustomConfigTypeDef = TypedDict(
    "_ClientCreateServiceHealthCheckCustomConfigTypeDef", {"FailureThreshold": int}, total=False
)


class ClientCreateServiceHealthCheckCustomConfigTypeDef(
    _ClientCreateServiceHealthCheckCustomConfigTypeDef
):
    """
    A complex type that contains information about an optional custom health check.
    .. warning::

      If you specify a health check configuration, you can specify either
      ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.
    """


_ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)


class ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef(
    _ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef
):
    pass


_ClientCreateServiceResponseServiceDnsConfigTypeDef = TypedDict(
    "_ClientCreateServiceResponseServiceDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"],
        "DnsRecords": List[ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)


class ClientCreateServiceResponseServiceDnsConfigTypeDef(
    _ClientCreateServiceResponseServiceDnsConfigTypeDef
):
    pass


_ClientCreateServiceResponseServiceHealthCheckConfigTypeDef = TypedDict(
    "_ClientCreateServiceResponseServiceHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ClientCreateServiceResponseServiceHealthCheckConfigTypeDef(
    _ClientCreateServiceResponseServiceHealthCheckConfigTypeDef
):
    pass


_ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef = TypedDict(
    "_ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)


class ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef(
    _ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef
):
    pass


_ClientCreateServiceResponseServiceTypeDef = TypedDict(
    "_ClientCreateServiceResponseServiceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "NamespaceId": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": ClientCreateServiceResponseServiceDnsConfigTypeDef,
        "HealthCheckConfig": ClientCreateServiceResponseServiceHealthCheckConfigTypeDef,
        "HealthCheckCustomConfig": ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef,
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)


class ClientCreateServiceResponseServiceTypeDef(_ClientCreateServiceResponseServiceTypeDef):
    """
    - **Service** *(dict) --*

      A complex type that contains information about the new service.
      - **Id** *(string) --*

        The ID that AWS Cloud Map assigned to the service when you created it.
    """


_ClientCreateServiceResponseTypeDef = TypedDict(
    "_ClientCreateServiceResponseTypeDef",
    {"Service": ClientCreateServiceResponseServiceTypeDef},
    total=False,
)


class ClientCreateServiceResponseTypeDef(_ClientCreateServiceResponseTypeDef):
    """
    - *(dict) --*

      - **Service** *(dict) --*

        A complex type that contains information about the new service.
        - **Id** *(string) --*

          The ID that AWS Cloud Map assigned to the service when you created it.
    """


_ClientDeleteNamespaceResponseTypeDef = TypedDict(
    "_ClientDeleteNamespaceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientDeleteNamespaceResponseTypeDef(_ClientDeleteNamespaceResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        A value that you can use to determine whether the request completed successfully. To get the
        status of the operation, see  GetOperation .
    """


_ClientDeregisterInstanceResponseTypeDef = TypedDict(
    "_ClientDeregisterInstanceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientDeregisterInstanceResponseTypeDef(_ClientDeregisterInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        A value that you can use to determine whether the request completed successfully. For more
        information, see  GetOperation .
    """


_ClientDiscoverInstancesResponseInstancesTypeDef = TypedDict(
    "_ClientDiscoverInstancesResponseInstancesTypeDef",
    {
        "InstanceId": str,
        "NamespaceName": str,
        "ServiceName": str,
        "HealthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "Attributes": Dict[str, str],
    },
    total=False,
)


class ClientDiscoverInstancesResponseInstancesTypeDef(
    _ClientDiscoverInstancesResponseInstancesTypeDef
):
    """
    - *(dict) --*

      In a response to a  DiscoverInstance request, ``HttpInstanceSummary`` contains information
      about one instance that matches the values that you specified in the request.
      - **InstanceId** *(string) --*

        The ID of an instance that matches the values that you specified in the request.
    """


_ClientDiscoverInstancesResponseTypeDef = TypedDict(
    "_ClientDiscoverInstancesResponseTypeDef",
    {"Instances": List[ClientDiscoverInstancesResponseInstancesTypeDef]},
    total=False,
)


class ClientDiscoverInstancesResponseTypeDef(_ClientDiscoverInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **Instances** *(list) --*

        A complex type that contains one ``HttpInstanceSummary`` for each registered instance.
        - *(dict) --*

          In a response to a  DiscoverInstance request, ``HttpInstanceSummary`` contains information
          about one instance that matches the values that you specified in the request.
          - **InstanceId** *(string) --*

            The ID of an instance that matches the values that you specified in the request.
    """


_ClientGetInstanceResponseInstanceTypeDef = TypedDict(
    "_ClientGetInstanceResponseInstanceTypeDef",
    {"Id": str, "CreatorRequestId": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientGetInstanceResponseInstanceTypeDef(_ClientGetInstanceResponseInstanceTypeDef):
    """
    - **Instance** *(dict) --*

      A complex type that contains information about a specified instance.
      - **Id** *(string) --*

        An identifier that you want to associate with the instance. Note the following:
        * If the service that is specified by ``ServiceId`` includes settings for an SRV record, the
        value of ``InstanceId`` is automatically included as part of the value for the SRV record.
        For more information, see  DnsRecord$Type .
        * You can use this value to update an existing instance.
        * To register a new instance, you must specify a value that is unique among instances that
        you register by using the same service.
        * If you specify an existing ``InstanceId`` and ``ServiceId`` , AWS Cloud Map updates the
        existing DNS records. If there's also an existing health check, AWS Cloud Map deletes the
        old health check and creates a new one.
        .. note::

          The health check isn't deleted immediately, so it will still appear for a while if you
          submit a ``ListHealthChecks`` request, for example.
    """


_ClientGetInstanceResponseTypeDef = TypedDict(
    "_ClientGetInstanceResponseTypeDef",
    {"Instance": ClientGetInstanceResponseInstanceTypeDef},
    total=False,
)


class ClientGetInstanceResponseTypeDef(_ClientGetInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **Instance** *(dict) --*

        A complex type that contains information about a specified instance.
        - **Id** *(string) --*

          An identifier that you want to associate with the instance. Note the following:
          * If the service that is specified by ``ServiceId`` includes settings for an SRV record,
          the value of ``InstanceId`` is automatically included as part of the value for the SRV
          record. For more information, see  DnsRecord$Type .
          * You can use this value to update an existing instance.
          * To register a new instance, you must specify a value that is unique among instances that
          you register by using the same service.
          * If you specify an existing ``InstanceId`` and ``ServiceId`` , AWS Cloud Map updates the
          existing DNS records. If there's also an existing health check, AWS Cloud Map deletes the
          old health check and creates a new one.
          .. note::

            The health check isn't deleted immediately, so it will still appear for a while if you
            submit a ``ListHealthChecks`` request, for example.
    """


_ClientGetInstancesHealthStatusResponseTypeDef = TypedDict(
    "_ClientGetInstancesHealthStatusResponseTypeDef",
    {"Status": Dict[str, Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]], "NextToken": str},
    total=False,
)


class ClientGetInstancesHealthStatusResponseTypeDef(_ClientGetInstancesHealthStatusResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(dict) --*

        A complex type that contains the IDs and the health status of the instances that you
        specified in the ``GetInstancesHealthStatus`` request.
        - *(string) --*

          - *(string) --*
    """


_ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef = TypedDict(
    "_ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef",
    {"HostedZoneId": str},
    total=False,
)


class ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef(
    _ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef
):
    pass


_ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef = TypedDict(
    "_ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef",
    {"HttpName": str},
    total=False,
)


class ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef(
    _ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef
):
    pass


_ClientGetNamespaceResponseNamespacePropertiesTypeDef = TypedDict(
    "_ClientGetNamespaceResponseNamespacePropertiesTypeDef",
    {
        "DnsProperties": ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef,
        "HttpProperties": ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef,
    },
    total=False,
)


class ClientGetNamespaceResponseNamespacePropertiesTypeDef(
    _ClientGetNamespaceResponseNamespacePropertiesTypeDef
):
    pass


_ClientGetNamespaceResponseNamespaceTypeDef = TypedDict(
    "_ClientGetNamespaceResponseNamespaceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": Literal["DNS_PUBLIC", "DNS_PRIVATE", "HTTP"],
        "Description": str,
        "ServiceCount": int,
        "Properties": ClientGetNamespaceResponseNamespacePropertiesTypeDef,
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)


class ClientGetNamespaceResponseNamespaceTypeDef(_ClientGetNamespaceResponseNamespaceTypeDef):
    """
    - **Namespace** *(dict) --*

      A complex type that contains information about the specified namespace.
      - **Id** *(string) --*

        The ID of a namespace.
    """


_ClientGetNamespaceResponseTypeDef = TypedDict(
    "_ClientGetNamespaceResponseTypeDef",
    {"Namespace": ClientGetNamespaceResponseNamespaceTypeDef},
    total=False,
)


class ClientGetNamespaceResponseTypeDef(_ClientGetNamespaceResponseTypeDef):
    """
    - *(dict) --*

      - **Namespace** *(dict) --*

        A complex type that contains information about the specified namespace.
        - **Id** *(string) --*

          The ID of a namespace.
    """


_ClientGetOperationResponseOperationTypeDef = TypedDict(
    "_ClientGetOperationResponseOperationTypeDef",
    {
        "Id": str,
        "Type": Literal[
            "CREATE_NAMESPACE",
            "DELETE_NAMESPACE",
            "UPDATE_SERVICE",
            "REGISTER_INSTANCE",
            "DEREGISTER_INSTANCE",
        ],
        "Status": Literal["SUBMITTED", "PENDING", "SUCCESS", "FAIL"],
        "ErrorMessage": str,
        "ErrorCode": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "Targets": Dict[str, str],
    },
    total=False,
)


class ClientGetOperationResponseOperationTypeDef(_ClientGetOperationResponseOperationTypeDef):
    """
    - **Operation** *(dict) --*

      A complex type that contains information about the operation.
      - **Id** *(string) --*

        The ID of the operation that you want to get information about.
    """


_ClientGetOperationResponseTypeDef = TypedDict(
    "_ClientGetOperationResponseTypeDef",
    {"Operation": ClientGetOperationResponseOperationTypeDef},
    total=False,
)


class ClientGetOperationResponseTypeDef(_ClientGetOperationResponseTypeDef):
    """
    - *(dict) --*

      - **Operation** *(dict) --*

        A complex type that contains information about the operation.
        - **Id** *(string) --*

          The ID of the operation that you want to get information about.
    """


_ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)


class ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef(
    _ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef
):
    pass


_ClientGetServiceResponseServiceDnsConfigTypeDef = TypedDict(
    "_ClientGetServiceResponseServiceDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"],
        "DnsRecords": List[ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)


class ClientGetServiceResponseServiceDnsConfigTypeDef(
    _ClientGetServiceResponseServiceDnsConfigTypeDef
):
    pass


_ClientGetServiceResponseServiceHealthCheckConfigTypeDef = TypedDict(
    "_ClientGetServiceResponseServiceHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ClientGetServiceResponseServiceHealthCheckConfigTypeDef(
    _ClientGetServiceResponseServiceHealthCheckConfigTypeDef
):
    pass


_ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef = TypedDict(
    "_ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)


class ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef(
    _ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef
):
    pass


_ClientGetServiceResponseServiceTypeDef = TypedDict(
    "_ClientGetServiceResponseServiceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "NamespaceId": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": ClientGetServiceResponseServiceDnsConfigTypeDef,
        "HealthCheckConfig": ClientGetServiceResponseServiceHealthCheckConfigTypeDef,
        "HealthCheckCustomConfig": ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef,
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)


class ClientGetServiceResponseServiceTypeDef(_ClientGetServiceResponseServiceTypeDef):
    """
    - **Service** *(dict) --*

      A complex type that contains information about the service.
      - **Id** *(string) --*

        The ID that AWS Cloud Map assigned to the service when you created it.
    """


_ClientGetServiceResponseTypeDef = TypedDict(
    "_ClientGetServiceResponseTypeDef",
    {"Service": ClientGetServiceResponseServiceTypeDef},
    total=False,
)


class ClientGetServiceResponseTypeDef(_ClientGetServiceResponseTypeDef):
    """
    - *(dict) --*

      - **Service** *(dict) --*

        A complex type that contains information about the service.
        - **Id** *(string) --*

          The ID that AWS Cloud Map assigned to the service when you created it.
    """


_ClientListInstancesResponseInstancesTypeDef = TypedDict(
    "_ClientListInstancesResponseInstancesTypeDef",
    {"Id": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientListInstancesResponseInstancesTypeDef(_ClientListInstancesResponseInstancesTypeDef):
    """
    - *(dict) --*

      A complex type that contains information about the instances that you registered by using a
      specified service.
      - **Id** *(string) --*

        The ID for an instance that you created by using a specified service.
    """


_ClientListInstancesResponseTypeDef = TypedDict(
    "_ClientListInstancesResponseTypeDef",
    {"Instances": List[ClientListInstancesResponseInstancesTypeDef], "NextToken": str},
    total=False,
)


class ClientListInstancesResponseTypeDef(_ClientListInstancesResponseTypeDef):
    """
    - *(dict) --*

      - **Instances** *(list) --*

        Summary information about the instances that are associated with the specified service.
        - *(dict) --*

          A complex type that contains information about the instances that you registered by using
          a specified service.
          - **Id** *(string) --*

            The ID for an instance that you created by using a specified service.
    """


_RequiredClientListNamespacesFiltersTypeDef = TypedDict(
    "_RequiredClientListNamespacesFiltersTypeDef", {"Name": str}
)
_OptionalClientListNamespacesFiltersTypeDef = TypedDict(
    "_OptionalClientListNamespacesFiltersTypeDef",
    {"Values": List[str], "Condition": Literal["EQ", "IN", "BETWEEN"]},
    total=False,
)


class ClientListNamespacesFiltersTypeDef(
    _RequiredClientListNamespacesFiltersTypeDef, _OptionalClientListNamespacesFiltersTypeDef
):
    """
    - *(dict) --*

      A complex type that identifies the namespaces that you want to list. You can choose to list
      public or private namespaces.
      - **Name** *(string) --***[REQUIRED]**

        Specify ``TYPE`` .
    """


_ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef = TypedDict(
    "_ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef",
    {"HostedZoneId": str},
    total=False,
)


class ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef(
    _ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef
):
    pass


_ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef = TypedDict(
    "_ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef",
    {"HttpName": str},
    total=False,
)


class ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef(
    _ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef
):
    pass


_ClientListNamespacesResponseNamespacesPropertiesTypeDef = TypedDict(
    "_ClientListNamespacesResponseNamespacesPropertiesTypeDef",
    {
        "DnsProperties": ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef,
        "HttpProperties": ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef,
    },
    total=False,
)


class ClientListNamespacesResponseNamespacesPropertiesTypeDef(
    _ClientListNamespacesResponseNamespacesPropertiesTypeDef
):
    pass


_ClientListNamespacesResponseNamespacesTypeDef = TypedDict(
    "_ClientListNamespacesResponseNamespacesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": Literal["DNS_PUBLIC", "DNS_PRIVATE", "HTTP"],
        "Description": str,
        "ServiceCount": int,
        "Properties": ClientListNamespacesResponseNamespacesPropertiesTypeDef,
        "CreateDate": datetime,
    },
    total=False,
)


class ClientListNamespacesResponseNamespacesTypeDef(_ClientListNamespacesResponseNamespacesTypeDef):
    """
    - *(dict) --*

      A complex type that contains information about a namespace.
      - **Id** *(string) --*

        The ID of the namespace.
    """


_ClientListNamespacesResponseTypeDef = TypedDict(
    "_ClientListNamespacesResponseTypeDef",
    {"Namespaces": List[ClientListNamespacesResponseNamespacesTypeDef], "NextToken": str},
    total=False,
)


class ClientListNamespacesResponseTypeDef(_ClientListNamespacesResponseTypeDef):
    """
    - *(dict) --*

      - **Namespaces** *(list) --*

        An array that contains one ``NamespaceSummary`` object for each namespace that matches the
        specified filter criteria.
        - *(dict) --*

          A complex type that contains information about a namespace.
          - **Id** *(string) --*

            The ID of the namespace.
    """


_RequiredClientListOperationsFiltersTypeDef = TypedDict(
    "_RequiredClientListOperationsFiltersTypeDef",
    {"Name": Literal["NAMESPACE_ID", "SERVICE_ID", "STATUS", "TYPE", "UPDATE_DATE"]},
)
_OptionalClientListOperationsFiltersTypeDef = TypedDict(
    "_OptionalClientListOperationsFiltersTypeDef",
    {"Values": List[str], "Condition": Literal["EQ", "IN", "BETWEEN"]},
    total=False,
)


class ClientListOperationsFiltersTypeDef(
    _RequiredClientListOperationsFiltersTypeDef, _OptionalClientListOperationsFiltersTypeDef
):
    """
    - *(dict) --*

      A complex type that lets you select the operations that you want to list.
      - **Name** *(string) --***[REQUIRED]**

        Specify the operations that you want to get:
        * **NAMESPACE_ID** : Gets operations related to specified namespaces.
        * **SERVICE_ID** : Gets operations related to specified services.
        * **STATUS** : Gets operations based on the status of the operations: ``SUBMITTED`` ,
        ``PENDING`` , ``SUCCEED`` , or ``FAIL`` .
        * **TYPE** : Gets specified types of operation.
        * **UPDATE_DATE** : Gets operations that changed status during a specified date/time range.
    """


_ClientListOperationsResponseOperationsTypeDef = TypedDict(
    "_ClientListOperationsResponseOperationsTypeDef",
    {"Id": str, "Status": Literal["SUBMITTED", "PENDING", "SUCCESS", "FAIL"]},
    total=False,
)


class ClientListOperationsResponseOperationsTypeDef(_ClientListOperationsResponseOperationsTypeDef):
    """
    - *(dict) --*

      A complex type that contains information about an operation that matches the criteria that you
      specified in a  ListOperations request.
      - **Id** *(string) --*

        The ID for an operation.
    """


_ClientListOperationsResponseTypeDef = TypedDict(
    "_ClientListOperationsResponseTypeDef",
    {"Operations": List[ClientListOperationsResponseOperationsTypeDef], "NextToken": str},
    total=False,
)


class ClientListOperationsResponseTypeDef(_ClientListOperationsResponseTypeDef):
    """
    - *(dict) --*

      - **Operations** *(list) --*

        Summary information about the operations that match the specified criteria.
        - *(dict) --*

          A complex type that contains information about an operation that matches the criteria that
          you specified in a  ListOperations request.
          - **Id** *(string) --*

            The ID for an operation.
    """


_RequiredClientListServicesFiltersTypeDef = TypedDict(
    "_RequiredClientListServicesFiltersTypeDef", {"Name": str}
)
_OptionalClientListServicesFiltersTypeDef = TypedDict(
    "_OptionalClientListServicesFiltersTypeDef",
    {"Values": List[str], "Condition": Literal["EQ", "IN", "BETWEEN"]},
    total=False,
)


class ClientListServicesFiltersTypeDef(
    _RequiredClientListServicesFiltersTypeDef, _OptionalClientListServicesFiltersTypeDef
):
    """
    - *(dict) --*

      A complex type that lets you specify the namespaces that you want to list services for.
      - **Name** *(string) --***[REQUIRED]**

        Specify ``NAMESPACE_ID`` .
    """


_ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)


class ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef(
    _ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef
):
    pass


_ClientListServicesResponseServicesDnsConfigTypeDef = TypedDict(
    "_ClientListServicesResponseServicesDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"],
        "DnsRecords": List[ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)


class ClientListServicesResponseServicesDnsConfigTypeDef(
    _ClientListServicesResponseServicesDnsConfigTypeDef
):
    pass


_ClientListServicesResponseServicesHealthCheckConfigTypeDef = TypedDict(
    "_ClientListServicesResponseServicesHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ClientListServicesResponseServicesHealthCheckConfigTypeDef(
    _ClientListServicesResponseServicesHealthCheckConfigTypeDef
):
    pass


_ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef = TypedDict(
    "_ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)


class ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef(
    _ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef
):
    pass


_ClientListServicesResponseServicesTypeDef = TypedDict(
    "_ClientListServicesResponseServicesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": ClientListServicesResponseServicesDnsConfigTypeDef,
        "HealthCheckConfig": ClientListServicesResponseServicesHealthCheckConfigTypeDef,
        "HealthCheckCustomConfig": ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef,
        "CreateDate": datetime,
    },
    total=False,
)


class ClientListServicesResponseServicesTypeDef(_ClientListServicesResponseServicesTypeDef):
    """
    - *(dict) --*

      A complex type that contains information about a specified service.
      - **Id** *(string) --*

        The ID that AWS Cloud Map assigned to the service when you created it.
    """


_ClientListServicesResponseTypeDef = TypedDict(
    "_ClientListServicesResponseTypeDef",
    {"Services": List[ClientListServicesResponseServicesTypeDef], "NextToken": str},
    total=False,
)


class ClientListServicesResponseTypeDef(_ClientListServicesResponseTypeDef):
    """
    - *(dict) --*

      - **Services** *(list) --*

        An array that contains one ``ServiceSummary`` object for each service that matches the
        specified filter criteria.
        - *(dict) --*

          A complex type that contains information about a specified service.
          - **Id** *(string) --*

            The ID that AWS Cloud Map assigned to the service when you created it.
    """


_ClientRegisterInstanceResponseTypeDef = TypedDict(
    "_ClientRegisterInstanceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientRegisterInstanceResponseTypeDef(_ClientRegisterInstanceResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        A value that you can use to determine whether the request completed successfully. To get the
        status of the operation, see  GetOperation .
    """


_ClientUpdateServiceResponseTypeDef = TypedDict(
    "_ClientUpdateServiceResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateServiceResponseTypeDef(_ClientUpdateServiceResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        A value that you can use to determine whether the request completed successfully. To get the
        status of the operation, see  GetOperation .
    """


_ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)


class ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef(
    _ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef
):
    pass


_ClientUpdateServiceServiceDnsConfigTypeDef = TypedDict(
    "_ClientUpdateServiceServiceDnsConfigTypeDef",
    {"DnsRecords": List[ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef]},
    total=False,
)


class ClientUpdateServiceServiceDnsConfigTypeDef(_ClientUpdateServiceServiceDnsConfigTypeDef):
    pass


_ClientUpdateServiceServiceHealthCheckConfigTypeDef = TypedDict(
    "_ClientUpdateServiceServiceHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ClientUpdateServiceServiceHealthCheckConfigTypeDef(
    _ClientUpdateServiceServiceHealthCheckConfigTypeDef
):
    pass


_ClientUpdateServiceServiceTypeDef = TypedDict(
    "_ClientUpdateServiceServiceTypeDef",
    {
        "Description": str,
        "DnsConfig": ClientUpdateServiceServiceDnsConfigTypeDef,
        "HealthCheckConfig": ClientUpdateServiceServiceHealthCheckConfigTypeDef,
    },
    total=False,
)


class ClientUpdateServiceServiceTypeDef(_ClientUpdateServiceServiceTypeDef):
    """
    A complex type that contains the new settings for the service.
    - **Description** *(string) --*

      A description for the service.
    """


_ListInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInstancesPaginatePaginationConfigTypeDef(_ListInstancesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListInstancesPaginateResponseInstancesTypeDef = TypedDict(
    "_ListInstancesPaginateResponseInstancesTypeDef",
    {"Id": str, "Attributes": Dict[str, str]},
    total=False,
)


class ListInstancesPaginateResponseInstancesTypeDef(_ListInstancesPaginateResponseInstancesTypeDef):
    """
    - *(dict) --*

      A complex type that contains information about the instances that you registered by using a
      specified service.
      - **Id** *(string) --*

        The ID for an instance that you created by using a specified service.
    """


_ListInstancesPaginateResponseTypeDef = TypedDict(
    "_ListInstancesPaginateResponseTypeDef",
    {"Instances": List[ListInstancesPaginateResponseInstancesTypeDef]},
    total=False,
)


class ListInstancesPaginateResponseTypeDef(_ListInstancesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Instances** *(list) --*

        Summary information about the instances that are associated with the specified service.
        - *(dict) --*

          A complex type that contains information about the instances that you registered by using
          a specified service.
          - **Id** *(string) --*

            The ID for an instance that you created by using a specified service.
    """


_RequiredListNamespacesPaginateFiltersTypeDef = TypedDict(
    "_RequiredListNamespacesPaginateFiltersTypeDef", {"Name": str}
)
_OptionalListNamespacesPaginateFiltersTypeDef = TypedDict(
    "_OptionalListNamespacesPaginateFiltersTypeDef",
    {"Values": List[str], "Condition": Literal["EQ", "IN", "BETWEEN"]},
    total=False,
)


class ListNamespacesPaginateFiltersTypeDef(
    _RequiredListNamespacesPaginateFiltersTypeDef, _OptionalListNamespacesPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A complex type that identifies the namespaces that you want to list. You can choose to list
      public or private namespaces.
      - **Name** *(string) --***[REQUIRED]**

        Specify ``TYPE`` .
    """


_ListNamespacesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListNamespacesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListNamespacesPaginatePaginationConfigTypeDef(_ListNamespacesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef = TypedDict(
    "_ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef",
    {"HostedZoneId": str},
    total=False,
)


class ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef(
    _ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef
):
    pass


_ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef = TypedDict(
    "_ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef",
    {"HttpName": str},
    total=False,
)


class ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef(
    _ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef
):
    pass


_ListNamespacesPaginateResponseNamespacesPropertiesTypeDef = TypedDict(
    "_ListNamespacesPaginateResponseNamespacesPropertiesTypeDef",
    {
        "DnsProperties": ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef,
        "HttpProperties": ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef,
    },
    total=False,
)


class ListNamespacesPaginateResponseNamespacesPropertiesTypeDef(
    _ListNamespacesPaginateResponseNamespacesPropertiesTypeDef
):
    pass


_ListNamespacesPaginateResponseNamespacesTypeDef = TypedDict(
    "_ListNamespacesPaginateResponseNamespacesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": Literal["DNS_PUBLIC", "DNS_PRIVATE", "HTTP"],
        "Description": str,
        "ServiceCount": int,
        "Properties": ListNamespacesPaginateResponseNamespacesPropertiesTypeDef,
        "CreateDate": datetime,
    },
    total=False,
)


class ListNamespacesPaginateResponseNamespacesTypeDef(
    _ListNamespacesPaginateResponseNamespacesTypeDef
):
    """
    - *(dict) --*

      A complex type that contains information about a namespace.
      - **Id** *(string) --*

        The ID of the namespace.
    """


_ListNamespacesPaginateResponseTypeDef = TypedDict(
    "_ListNamespacesPaginateResponseTypeDef",
    {"Namespaces": List[ListNamespacesPaginateResponseNamespacesTypeDef]},
    total=False,
)


class ListNamespacesPaginateResponseTypeDef(_ListNamespacesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Namespaces** *(list) --*

        An array that contains one ``NamespaceSummary`` object for each namespace that matches the
        specified filter criteria.
        - *(dict) --*

          A complex type that contains information about a namespace.
          - **Id** *(string) --*

            The ID of the namespace.
    """


_RequiredListOperationsPaginateFiltersTypeDef = TypedDict(
    "_RequiredListOperationsPaginateFiltersTypeDef",
    {"Name": Literal["NAMESPACE_ID", "SERVICE_ID", "STATUS", "TYPE", "UPDATE_DATE"]},
)
_OptionalListOperationsPaginateFiltersTypeDef = TypedDict(
    "_OptionalListOperationsPaginateFiltersTypeDef",
    {"Values": List[str], "Condition": Literal["EQ", "IN", "BETWEEN"]},
    total=False,
)


class ListOperationsPaginateFiltersTypeDef(
    _RequiredListOperationsPaginateFiltersTypeDef, _OptionalListOperationsPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A complex type that lets you select the operations that you want to list.
      - **Name** *(string) --***[REQUIRED]**

        Specify the operations that you want to get:
        * **NAMESPACE_ID** : Gets operations related to specified namespaces.
        * **SERVICE_ID** : Gets operations related to specified services.
        * **STATUS** : Gets operations based on the status of the operations: ``SUBMITTED`` ,
        ``PENDING`` , ``SUCCEED`` , or ``FAIL`` .
        * **TYPE** : Gets specified types of operation.
        * **UPDATE_DATE** : Gets operations that changed status during a specified date/time range.
    """


_ListOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOperationsPaginatePaginationConfigTypeDef(_ListOperationsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListOperationsPaginateResponseOperationsTypeDef = TypedDict(
    "_ListOperationsPaginateResponseOperationsTypeDef",
    {"Id": str, "Status": Literal["SUBMITTED", "PENDING", "SUCCESS", "FAIL"]},
    total=False,
)


class ListOperationsPaginateResponseOperationsTypeDef(
    _ListOperationsPaginateResponseOperationsTypeDef
):
    """
    - *(dict) --*

      A complex type that contains information about an operation that matches the criteria that you
      specified in a  ListOperations request.
      - **Id** *(string) --*

        The ID for an operation.
    """


_ListOperationsPaginateResponseTypeDef = TypedDict(
    "_ListOperationsPaginateResponseTypeDef",
    {"Operations": List[ListOperationsPaginateResponseOperationsTypeDef]},
    total=False,
)


class ListOperationsPaginateResponseTypeDef(_ListOperationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Operations** *(list) --*

        Summary information about the operations that match the specified criteria.
        - *(dict) --*

          A complex type that contains information about an operation that matches the criteria that
          you specified in a  ListOperations request.
          - **Id** *(string) --*

            The ID for an operation.
    """


_RequiredListServicesPaginateFiltersTypeDef = TypedDict(
    "_RequiredListServicesPaginateFiltersTypeDef", {"Name": str}
)
_OptionalListServicesPaginateFiltersTypeDef = TypedDict(
    "_OptionalListServicesPaginateFiltersTypeDef",
    {"Values": List[str], "Condition": Literal["EQ", "IN", "BETWEEN"]},
    total=False,
)


class ListServicesPaginateFiltersTypeDef(
    _RequiredListServicesPaginateFiltersTypeDef, _OptionalListServicesPaginateFiltersTypeDef
):
    """
    - *(dict) --*

      A complex type that lets you specify the namespaces that you want to list services for.
      - **Name** *(string) --***[REQUIRED]**

        Specify ``NAMESPACE_ID`` .
    """


_ListServicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServicesPaginatePaginationConfigTypeDef(_ListServicesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)


class ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef(
    _ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef
):
    pass


_ListServicesPaginateResponseServicesDnsConfigTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"],
        "DnsRecords": List[ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)


class ListServicesPaginateResponseServicesDnsConfigTypeDef(
    _ListServicesPaginateResponseServicesDnsConfigTypeDef
):
    pass


_ListServicesPaginateResponseServicesHealthCheckConfigTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)


class ListServicesPaginateResponseServicesHealthCheckConfigTypeDef(
    _ListServicesPaginateResponseServicesHealthCheckConfigTypeDef
):
    pass


_ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)


class ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef(
    _ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef
):
    pass


_ListServicesPaginateResponseServicesTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": ListServicesPaginateResponseServicesDnsConfigTypeDef,
        "HealthCheckConfig": ListServicesPaginateResponseServicesHealthCheckConfigTypeDef,
        "HealthCheckCustomConfig": ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef,
        "CreateDate": datetime,
    },
    total=False,
)


class ListServicesPaginateResponseServicesTypeDef(_ListServicesPaginateResponseServicesTypeDef):
    """
    - *(dict) --*

      A complex type that contains information about a specified service.
      - **Id** *(string) --*

        The ID that AWS Cloud Map assigned to the service when you created it.
    """


_ListServicesPaginateResponseTypeDef = TypedDict(
    "_ListServicesPaginateResponseTypeDef",
    {"Services": List[ListServicesPaginateResponseServicesTypeDef]},
    total=False,
)


class ListServicesPaginateResponseTypeDef(_ListServicesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Services** *(list) --*

        An array that contains one ``ServiceSummary`` object for each service that matches the
        specified filter criteria.
        - *(dict) --*

          A complex type that contains information about a specified service.
          - **Id** *(string) --*

            The ID that AWS Cloud Map assigned to the service when you created it.
    """
