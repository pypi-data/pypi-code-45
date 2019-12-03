"Main interface for worklink service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAssociateWebsiteAuthorizationProviderResponseTypeDef",
    "ClientAssociateWebsiteCertificateAuthorityResponseTypeDef",
    "ClientCreateFleetResponseTypeDef",
    "ClientDescribeAuditStreamConfigurationResponseTypeDef",
    "ClientDescribeCompanyNetworkConfigurationResponseTypeDef",
    "ClientDescribeDevicePolicyConfigurationResponseTypeDef",
    "ClientDescribeDeviceResponseTypeDef",
    "ClientDescribeDomainResponseTypeDef",
    "ClientDescribeFleetMetadataResponseTypeDef",
    "ClientDescribeIdentityProviderConfigurationResponseTypeDef",
    "ClientDescribeWebsiteCertificateAuthorityResponseTypeDef",
    "ClientListDevicesResponseDevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListDomainsResponseDomainsTypeDef",
    "ClientListDomainsResponseTypeDef",
    "ClientListFleetsResponseFleetSummaryListTypeDef",
    "ClientListFleetsResponseTypeDef",
    "ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef",
    "ClientListWebsiteAuthorizationProvidersResponseTypeDef",
    "ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef",
    "ClientListWebsiteCertificateAuthoritiesResponseTypeDef",
)


_ClientAssociateWebsiteAuthorizationProviderResponseTypeDef = TypedDict(
    "_ClientAssociateWebsiteAuthorizationProviderResponseTypeDef",
    {"AuthorizationProviderId": str},
    total=False,
)


class ClientAssociateWebsiteAuthorizationProviderResponseTypeDef(
    _ClientAssociateWebsiteAuthorizationProviderResponseTypeDef
):
    """
    - *(dict) --*

      - **AuthorizationProviderId** *(string) --*

        A unique identifier for the authorization provider.
    """


_ClientAssociateWebsiteCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientAssociateWebsiteCertificateAuthorityResponseTypeDef", {"WebsiteCaId": str}, total=False
)


class ClientAssociateWebsiteCertificateAuthorityResponseTypeDef(
    _ClientAssociateWebsiteCertificateAuthorityResponseTypeDef
):
    """
    - *(dict) --*

      - **WebsiteCaId** *(string) --*

        A unique identifier for the CA.
    """


_ClientCreateFleetResponseTypeDef = TypedDict(
    "_ClientCreateFleetResponseTypeDef", {"FleetArn": str}, total=False
)


class ClientCreateFleetResponseTypeDef(_ClientCreateFleetResponseTypeDef):
    """
    - *(dict) --*

      - **FleetArn** *(string) --*

        The ARN of the fleet.
    """


_ClientDescribeAuditStreamConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeAuditStreamConfigurationResponseTypeDef", {"AuditStreamArn": str}, total=False
)


class ClientDescribeAuditStreamConfigurationResponseTypeDef(
    _ClientDescribeAuditStreamConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **AuditStreamArn** *(string) --*

        The ARN of the Amazon Kinesis data stream that will receive the audit events.
    """


_ClientDescribeCompanyNetworkConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeCompanyNetworkConfigurationResponseTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientDescribeCompanyNetworkConfigurationResponseTypeDef(
    _ClientDescribeCompanyNetworkConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **VpcId** *(string) --*

        The VPC with connectivity to associated websites.
    """


_ClientDescribeDevicePolicyConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeDevicePolicyConfigurationResponseTypeDef",
    {"DeviceCaCertificate": str},
    total=False,
)


class ClientDescribeDevicePolicyConfigurationResponseTypeDef(
    _ClientDescribeDevicePolicyConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **DeviceCaCertificate** *(string) --*

        The certificate chain, including intermediate certificates and the root certificate
        authority certificate used to issue device certificates.
    """


_ClientDescribeDeviceResponseTypeDef = TypedDict(
    "_ClientDescribeDeviceResponseTypeDef",
    {
        "Status": Literal["ACTIVE", "SIGNED_OUT"],
        "Model": str,
        "Manufacturer": str,
        "OperatingSystem": str,
        "OperatingSystemVersion": str,
        "PatchLevel": str,
        "FirstAccessedTime": datetime,
        "LastAccessedTime": datetime,
        "Username": str,
    },
    total=False,
)


class ClientDescribeDeviceResponseTypeDef(_ClientDescribeDeviceResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(string) --*

        The current state of the device.
    """


_ClientDescribeDomainResponseTypeDef = TypedDict(
    "_ClientDescribeDomainResponseTypeDef",
    {
        "DomainName": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "DomainStatus": Literal[
            "PENDING_VALIDATION",
            "ASSOCIATING",
            "ACTIVE",
            "INACTIVE",
            "DISASSOCIATING",
            "DISASSOCIATED",
            "FAILED_TO_ASSOCIATE",
            "FAILED_TO_DISASSOCIATE",
        ],
        "AcmCertificateArn": str,
    },
    total=False,
)


class ClientDescribeDomainResponseTypeDef(_ClientDescribeDomainResponseTypeDef):
    """
    - *(dict) --*

      - **DomainName** *(string) --*

        The name of the domain.
    """


_ClientDescribeFleetMetadataResponseTypeDef = TypedDict(
    "_ClientDescribeFleetMetadataResponseTypeDef",
    {
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "OptimizeForEndUserLocation": bool,
        "CompanyCode": str,
        "FleetStatus": Literal[
            "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED_TO_CREATE", "FAILED_TO_DELETE"
        ],
    },
    total=False,
)


class ClientDescribeFleetMetadataResponseTypeDef(_ClientDescribeFleetMetadataResponseTypeDef):
    """
    - *(dict) --*

      - **CreatedTime** *(datetime) --*

        The time that the fleet was created.
    """


_ClientDescribeIdentityProviderConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeIdentityProviderConfigurationResponseTypeDef",
    {
        "IdentityProviderType": str,
        "ServiceProviderSamlMetadata": str,
        "IdentityProviderSamlMetadata": str,
    },
    total=False,
)


class ClientDescribeIdentityProviderConfigurationResponseTypeDef(
    _ClientDescribeIdentityProviderConfigurationResponseTypeDef
):
    """
    - *(dict) --*

      - **IdentityProviderType** *(string) --*

        The type of identity provider.
    """


_ClientDescribeWebsiteCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientDescribeWebsiteCertificateAuthorityResponseTypeDef",
    {"Certificate": str, "CreatedTime": datetime, "DisplayName": str},
    total=False,
)


class ClientDescribeWebsiteCertificateAuthorityResponseTypeDef(
    _ClientDescribeWebsiteCertificateAuthorityResponseTypeDef
):
    """
    - *(dict) --*

      - **Certificate** *(string) --*

        The root certificate of the certificate authority.
    """


_ClientListDevicesResponseDevicesTypeDef = TypedDict(
    "_ClientListDevicesResponseDevicesTypeDef",
    {"DeviceId": str, "DeviceStatus": Literal["ACTIVE", "SIGNED_OUT"]},
    total=False,
)


class ClientListDevicesResponseDevicesTypeDef(_ClientListDevicesResponseDevicesTypeDef):
    """
    - *(dict) --*

      The summary of devices.
      - **DeviceId** *(string) --*

        The ID of the device.
    """


_ClientListDevicesResponseTypeDef = TypedDict(
    "_ClientListDevicesResponseTypeDef",
    {"Devices": List[ClientListDevicesResponseDevicesTypeDef], "NextToken": str},
    total=False,
)


class ClientListDevicesResponseTypeDef(_ClientListDevicesResponseTypeDef):
    """
    - *(dict) --*

      - **Devices** *(list) --*

        Information about the devices.
        - *(dict) --*

          The summary of devices.
          - **DeviceId** *(string) --*

            The ID of the device.
    """


_ClientListDomainsResponseDomainsTypeDef = TypedDict(
    "_ClientListDomainsResponseDomainsTypeDef",
    {
        "DomainName": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "DomainStatus": Literal[
            "PENDING_VALIDATION",
            "ASSOCIATING",
            "ACTIVE",
            "INACTIVE",
            "DISASSOCIATING",
            "DISASSOCIATED",
            "FAILED_TO_ASSOCIATE",
            "FAILED_TO_DISASSOCIATE",
        ],
    },
    total=False,
)


class ClientListDomainsResponseDomainsTypeDef(_ClientListDomainsResponseDomainsTypeDef):
    """
    - *(dict) --*

      The summary of the domain.
      - **DomainName** *(string) --*

        The name of the domain.
    """


_ClientListDomainsResponseTypeDef = TypedDict(
    "_ClientListDomainsResponseTypeDef",
    {"Domains": List[ClientListDomainsResponseDomainsTypeDef], "NextToken": str},
    total=False,
)


class ClientListDomainsResponseTypeDef(_ClientListDomainsResponseTypeDef):
    """
    - *(dict) --*

      - **Domains** *(list) --*

        Information about the domains.
        - *(dict) --*

          The summary of the domain.
          - **DomainName** *(string) --*

            The name of the domain.
    """


_ClientListFleetsResponseFleetSummaryListTypeDef = TypedDict(
    "_ClientListFleetsResponseFleetSummaryListTypeDef",
    {
        "FleetArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "CompanyCode": str,
        "FleetStatus": Literal[
            "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED_TO_CREATE", "FAILED_TO_DELETE"
        ],
    },
    total=False,
)


class ClientListFleetsResponseFleetSummaryListTypeDef(
    _ClientListFleetsResponseFleetSummaryListTypeDef
):
    """
    - *(dict) --*

      The summary of the fleet.
      - **FleetArn** *(string) --*

        The ARN of the fleet.
    """


_ClientListFleetsResponseTypeDef = TypedDict(
    "_ClientListFleetsResponseTypeDef",
    {"FleetSummaryList": List[ClientListFleetsResponseFleetSummaryListTypeDef], "NextToken": str},
    total=False,
)


class ClientListFleetsResponseTypeDef(_ClientListFleetsResponseTypeDef):
    """
    - *(dict) --*

      - **FleetSummaryList** *(list) --*

        The summary list of the fleets.
        - *(dict) --*

          The summary of the fleet.
          - **FleetArn** *(string) --*

            The ARN of the fleet.
    """


_ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef = TypedDict(
    "_ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef",
    {
        "AuthorizationProviderId": str,
        "AuthorizationProviderType": str,
        "DomainName": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef(
    _ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef
):
    """
    - *(dict) --*

      The summary of the website authorization provider.
      - **AuthorizationProviderId** *(string) --*

        A unique identifier for the authorization provider.
    """


_ClientListWebsiteAuthorizationProvidersResponseTypeDef = TypedDict(
    "_ClientListWebsiteAuthorizationProvidersResponseTypeDef",
    {
        "WebsiteAuthorizationProviders": List[
            ClientListWebsiteAuthorizationProvidersResponseWebsiteAuthorizationProvidersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListWebsiteAuthorizationProvidersResponseTypeDef(
    _ClientListWebsiteAuthorizationProvidersResponseTypeDef
):
    """
    - *(dict) --*

      - **WebsiteAuthorizationProviders** *(list) --*

        The website authorization providers.
        - *(dict) --*

          The summary of the website authorization provider.
          - **AuthorizationProviderId** *(string) --*

            A unique identifier for the authorization provider.
    """


_ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef = TypedDict(
    "_ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef",
    {"WebsiteCaId": str, "CreatedTime": datetime, "DisplayName": str},
    total=False,
)


class ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef(
    _ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef
):
    """
    - *(dict) --*

      The summary of the certificate authority (CA).
      - **WebsiteCaId** *(string) --*

        A unique identifier for the CA.
    """


_ClientListWebsiteCertificateAuthoritiesResponseTypeDef = TypedDict(
    "_ClientListWebsiteCertificateAuthoritiesResponseTypeDef",
    {
        "WebsiteCertificateAuthorities": List[
            ClientListWebsiteCertificateAuthoritiesResponseWebsiteCertificateAuthoritiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListWebsiteCertificateAuthoritiesResponseTypeDef(
    _ClientListWebsiteCertificateAuthoritiesResponseTypeDef
):
    """
    - *(dict) --*

      - **WebsiteCertificateAuthorities** *(list) --*

        Information about the certificates.
        - *(dict) --*

          The summary of the certificate authority (CA).
          - **WebsiteCaId** *(string) --*

            A unique identifier for the CA.
    """
