"Main interface for servicediscovery service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientCreateHttpNamespaceResponseTypeDef = TypedDict(
    "ClientCreateHttpNamespaceResponseTypeDef", {"OperationId": str}, total=False
)

ClientCreatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "ClientCreatePrivateDnsNamespaceResponseTypeDef", {"OperationId": str}, total=False
)

ClientCreatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "ClientCreatePublicDnsNamespaceResponseTypeDef", {"OperationId": str}, total=False
)

ClientCreateServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "ClientCreateServiceDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)

ClientCreateServiceDnsConfigTypeDef = TypedDict(
    "ClientCreateServiceDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"],
        "DnsRecords": List[ClientCreateServiceDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)

ClientCreateServiceHealthCheckConfigTypeDef = TypedDict(
    "ClientCreateServiceHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)

ClientCreateServiceHealthCheckCustomConfigTypeDef = TypedDict(
    "ClientCreateServiceHealthCheckCustomConfigTypeDef", {"FailureThreshold": int}, total=False
)

ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)

ClientCreateServiceResponseServiceDnsConfigTypeDef = TypedDict(
    "ClientCreateServiceResponseServiceDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"],
        "DnsRecords": List[ClientCreateServiceResponseServiceDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)

ClientCreateServiceResponseServiceHealthCheckConfigTypeDef = TypedDict(
    "ClientCreateServiceResponseServiceHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)

ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef = TypedDict(
    "ClientCreateServiceResponseServiceHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)

ClientCreateServiceResponseServiceTypeDef = TypedDict(
    "ClientCreateServiceResponseServiceTypeDef",
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

ClientCreateServiceResponseTypeDef = TypedDict(
    "ClientCreateServiceResponseTypeDef",
    {"Service": ClientCreateServiceResponseServiceTypeDef},
    total=False,
)

ClientDeleteNamespaceResponseTypeDef = TypedDict(
    "ClientDeleteNamespaceResponseTypeDef", {"OperationId": str}, total=False
)

ClientDeregisterInstanceResponseTypeDef = TypedDict(
    "ClientDeregisterInstanceResponseTypeDef", {"OperationId": str}, total=False
)

ClientDiscoverInstancesResponseInstancesTypeDef = TypedDict(
    "ClientDiscoverInstancesResponseInstancesTypeDef",
    {
        "InstanceId": str,
        "NamespaceName": str,
        "ServiceName": str,
        "HealthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "Attributes": Dict[str, str],
    },
    total=False,
)

ClientDiscoverInstancesResponseTypeDef = TypedDict(
    "ClientDiscoverInstancesResponseTypeDef",
    {"Instances": List[ClientDiscoverInstancesResponseInstancesTypeDef]},
    total=False,
)

ClientGetInstanceResponseInstanceTypeDef = TypedDict(
    "ClientGetInstanceResponseInstanceTypeDef",
    {"Id": str, "CreatorRequestId": str, "Attributes": Dict[str, str]},
    total=False,
)

ClientGetInstanceResponseTypeDef = TypedDict(
    "ClientGetInstanceResponseTypeDef",
    {"Instance": ClientGetInstanceResponseInstanceTypeDef},
    total=False,
)

ClientGetInstancesHealthStatusResponseTypeDef = TypedDict(
    "ClientGetInstancesHealthStatusResponseTypeDef",
    {"Status": Dict[str, Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]], "NextToken": str},
    total=False,
)

ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef = TypedDict(
    "ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef",
    {"HostedZoneId": str},
    total=False,
)

ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef = TypedDict(
    "ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef",
    {"HttpName": str},
    total=False,
)

ClientGetNamespaceResponseNamespacePropertiesTypeDef = TypedDict(
    "ClientGetNamespaceResponseNamespacePropertiesTypeDef",
    {
        "DnsProperties": ClientGetNamespaceResponseNamespacePropertiesDnsPropertiesTypeDef,
        "HttpProperties": ClientGetNamespaceResponseNamespacePropertiesHttpPropertiesTypeDef,
    },
    total=False,
)

ClientGetNamespaceResponseNamespaceTypeDef = TypedDict(
    "ClientGetNamespaceResponseNamespaceTypeDef",
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

ClientGetNamespaceResponseTypeDef = TypedDict(
    "ClientGetNamespaceResponseTypeDef",
    {"Namespace": ClientGetNamespaceResponseNamespaceTypeDef},
    total=False,
)

ClientGetOperationResponseOperationTypeDef = TypedDict(
    "ClientGetOperationResponseOperationTypeDef",
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

ClientGetOperationResponseTypeDef = TypedDict(
    "ClientGetOperationResponseTypeDef",
    {"Operation": ClientGetOperationResponseOperationTypeDef},
    total=False,
)

ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)

ClientGetServiceResponseServiceDnsConfigTypeDef = TypedDict(
    "ClientGetServiceResponseServiceDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"],
        "DnsRecords": List[ClientGetServiceResponseServiceDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)

ClientGetServiceResponseServiceHealthCheckConfigTypeDef = TypedDict(
    "ClientGetServiceResponseServiceHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)

ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef = TypedDict(
    "ClientGetServiceResponseServiceHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)

ClientGetServiceResponseServiceTypeDef = TypedDict(
    "ClientGetServiceResponseServiceTypeDef",
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

ClientGetServiceResponseTypeDef = TypedDict(
    "ClientGetServiceResponseTypeDef",
    {"Service": ClientGetServiceResponseServiceTypeDef},
    total=False,
)

ClientListInstancesResponseInstancesTypeDef = TypedDict(
    "ClientListInstancesResponseInstancesTypeDef",
    {"Id": str, "Attributes": Dict[str, str]},
    total=False,
)

ClientListInstancesResponseTypeDef = TypedDict(
    "ClientListInstancesResponseTypeDef",
    {"Instances": List[ClientListInstancesResponseInstancesTypeDef], "NextToken": str},
    total=False,
)

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
    pass


ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef = TypedDict(
    "ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef",
    {"HostedZoneId": str},
    total=False,
)

ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef = TypedDict(
    "ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef",
    {"HttpName": str},
    total=False,
)

ClientListNamespacesResponseNamespacesPropertiesTypeDef = TypedDict(
    "ClientListNamespacesResponseNamespacesPropertiesTypeDef",
    {
        "DnsProperties": ClientListNamespacesResponseNamespacesPropertiesDnsPropertiesTypeDef,
        "HttpProperties": ClientListNamespacesResponseNamespacesPropertiesHttpPropertiesTypeDef,
    },
    total=False,
)

ClientListNamespacesResponseNamespacesTypeDef = TypedDict(
    "ClientListNamespacesResponseNamespacesTypeDef",
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

ClientListNamespacesResponseTypeDef = TypedDict(
    "ClientListNamespacesResponseTypeDef",
    {"Namespaces": List[ClientListNamespacesResponseNamespacesTypeDef], "NextToken": str},
    total=False,
)

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
    pass


ClientListOperationsResponseOperationsTypeDef = TypedDict(
    "ClientListOperationsResponseOperationsTypeDef",
    {"Id": str, "Status": Literal["SUBMITTED", "PENDING", "SUCCESS", "FAIL"]},
    total=False,
)

ClientListOperationsResponseTypeDef = TypedDict(
    "ClientListOperationsResponseTypeDef",
    {"Operations": List[ClientListOperationsResponseOperationsTypeDef], "NextToken": str},
    total=False,
)

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
    pass


ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef = TypedDict(
    "ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)

ClientListServicesResponseServicesDnsConfigTypeDef = TypedDict(
    "ClientListServicesResponseServicesDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"],
        "DnsRecords": List[ClientListServicesResponseServicesDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)

ClientListServicesResponseServicesHealthCheckConfigTypeDef = TypedDict(
    "ClientListServicesResponseServicesHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)

ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef = TypedDict(
    "ClientListServicesResponseServicesHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)

ClientListServicesResponseServicesTypeDef = TypedDict(
    "ClientListServicesResponseServicesTypeDef",
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

ClientListServicesResponseTypeDef = TypedDict(
    "ClientListServicesResponseTypeDef",
    {"Services": List[ClientListServicesResponseServicesTypeDef], "NextToken": str},
    total=False,
)

ClientRegisterInstanceResponseTypeDef = TypedDict(
    "ClientRegisterInstanceResponseTypeDef", {"OperationId": str}, total=False
)

ClientUpdateServiceResponseTypeDef = TypedDict(
    "ClientUpdateServiceResponseTypeDef", {"OperationId": str}, total=False
)

ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef = TypedDict(
    "ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)

ClientUpdateServiceServiceDnsConfigTypeDef = TypedDict(
    "ClientUpdateServiceServiceDnsConfigTypeDef",
    {"DnsRecords": List[ClientUpdateServiceServiceDnsConfigDnsRecordsTypeDef]},
    total=False,
)

ClientUpdateServiceServiceHealthCheckConfigTypeDef = TypedDict(
    "ClientUpdateServiceServiceHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)

ClientUpdateServiceServiceTypeDef = TypedDict(
    "ClientUpdateServiceServiceTypeDef",
    {
        "Description": str,
        "DnsConfig": ClientUpdateServiceServiceDnsConfigTypeDef,
        "HealthCheckConfig": ClientUpdateServiceServiceHealthCheckConfigTypeDef,
    },
    total=False,
)

ListInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "ListInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListInstancesPaginateResponseInstancesTypeDef = TypedDict(
    "ListInstancesPaginateResponseInstancesTypeDef",
    {"Id": str, "Attributes": Dict[str, str]},
    total=False,
)

ListInstancesPaginateResponseTypeDef = TypedDict(
    "ListInstancesPaginateResponseTypeDef",
    {"Instances": List[ListInstancesPaginateResponseInstancesTypeDef]},
    total=False,
)

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
    pass


ListNamespacesPaginatePaginationConfigTypeDef = TypedDict(
    "ListNamespacesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef = TypedDict(
    "ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef",
    {"HostedZoneId": str},
    total=False,
)

ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef = TypedDict(
    "ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef",
    {"HttpName": str},
    total=False,
)

ListNamespacesPaginateResponseNamespacesPropertiesTypeDef = TypedDict(
    "ListNamespacesPaginateResponseNamespacesPropertiesTypeDef",
    {
        "DnsProperties": ListNamespacesPaginateResponseNamespacesPropertiesDnsPropertiesTypeDef,
        "HttpProperties": ListNamespacesPaginateResponseNamespacesPropertiesHttpPropertiesTypeDef,
    },
    total=False,
)

ListNamespacesPaginateResponseNamespacesTypeDef = TypedDict(
    "ListNamespacesPaginateResponseNamespacesTypeDef",
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

ListNamespacesPaginateResponseTypeDef = TypedDict(
    "ListNamespacesPaginateResponseTypeDef",
    {"Namespaces": List[ListNamespacesPaginateResponseNamespacesTypeDef]},
    total=False,
)

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
    pass


ListOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "ListOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListOperationsPaginateResponseOperationsTypeDef = TypedDict(
    "ListOperationsPaginateResponseOperationsTypeDef",
    {"Id": str, "Status": Literal["SUBMITTED", "PENDING", "SUCCESS", "FAIL"]},
    total=False,
)

ListOperationsPaginateResponseTypeDef = TypedDict(
    "ListOperationsPaginateResponseTypeDef",
    {"Operations": List[ListOperationsPaginateResponseOperationsTypeDef]},
    total=False,
)

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
    pass


ListServicesPaginatePaginationConfigTypeDef = TypedDict(
    "ListServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef = TypedDict(
    "ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef",
    {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int},
    total=False,
)

ListServicesPaginateResponseServicesDnsConfigTypeDef = TypedDict(
    "ListServicesPaginateResponseServicesDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"],
        "DnsRecords": List[ListServicesPaginateResponseServicesDnsConfigDnsRecordsTypeDef],
    },
    total=False,
)

ListServicesPaginateResponseServicesHealthCheckConfigTypeDef = TypedDict(
    "ListServicesPaginateResponseServicesHealthCheckConfigTypeDef",
    {"Type": Literal["HTTP", "HTTPS", "TCP"], "ResourcePath": str, "FailureThreshold": int},
    total=False,
)

ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef = TypedDict(
    "ListServicesPaginateResponseServicesHealthCheckCustomConfigTypeDef",
    {"FailureThreshold": int},
    total=False,
)

ListServicesPaginateResponseServicesTypeDef = TypedDict(
    "ListServicesPaginateResponseServicesTypeDef",
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

ListServicesPaginateResponseTypeDef = TypedDict(
    "ListServicesPaginateResponseTypeDef",
    {"Services": List[ListServicesPaginateResponseServicesTypeDef]},
    total=False,
)
