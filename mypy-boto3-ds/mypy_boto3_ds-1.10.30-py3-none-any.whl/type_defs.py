"Main interface for ds service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef",
    "ClientAcceptSharedDirectoryResponseTypeDef",
    "ClientAddIpRoutesIpRoutesTypeDef",
    "ClientAddTagsToResourceTagsTypeDef",
    "ClientConnectDirectoryConnectSettingsTypeDef",
    "ClientConnectDirectoryResponseTypeDef",
    "ClientConnectDirectoryTagsTypeDef",
    "ClientCreateAliasResponseTypeDef",
    "ClientCreateComputerComputerAttributesTypeDef",
    "ClientCreateComputerResponseComputerComputerAttributesTypeDef",
    "ClientCreateComputerResponseComputerTypeDef",
    "ClientCreateComputerResponseTypeDef",
    "ClientCreateDirectoryResponseTypeDef",
    "ClientCreateDirectoryTagsTypeDef",
    "ClientCreateDirectoryVpcSettingsTypeDef",
    "ClientCreateMicrosoftAdResponseTypeDef",
    "ClientCreateMicrosoftAdTagsTypeDef",
    "ClientCreateMicrosoftAdVpcSettingsTypeDef",
    "ClientCreateSnapshotResponseTypeDef",
    "ClientCreateTrustResponseTypeDef",
    "ClientDeleteDirectoryResponseTypeDef",
    "ClientDeleteSnapshotResponseTypeDef",
    "ClientDeleteTrustResponseTypeDef",
    "ClientDescribeCertificateResponseCertificateTypeDef",
    "ClientDescribeCertificateResponseTypeDef",
    "ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef",
    "ClientDescribeConditionalForwardersResponseTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef",
    "ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef",
    "ClientDescribeDirectoriesResponseTypeDef",
    "ClientDescribeDomainControllersResponseDomainControllersTypeDef",
    "ClientDescribeDomainControllersResponseTypeDef",
    "ClientDescribeEventTopicsResponseEventTopicsTypeDef",
    "ClientDescribeEventTopicsResponseTypeDef",
    "ClientDescribeLdapsSettingsResponseLDAPSSettingsInfoTypeDef",
    "ClientDescribeLdapsSettingsResponseTypeDef",
    "ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef",
    "ClientDescribeSharedDirectoriesResponseTypeDef",
    "ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    "ClientDescribeSnapshotsResponseTypeDef",
    "ClientDescribeTrustsResponseTrustsTypeDef",
    "ClientDescribeTrustsResponseTypeDef",
    "ClientEnableRadiusRadiusSettingsTypeDef",
    "ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef",
    "ClientGetDirectoryLimitsResponseTypeDef",
    "ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef",
    "ClientGetSnapshotLimitsResponseTypeDef",
    "ClientListCertificatesResponseCertificatesInfoTypeDef",
    "ClientListCertificatesResponseTypeDef",
    "ClientListIpRoutesResponseIpRoutesInfoTypeDef",
    "ClientListIpRoutesResponseTypeDef",
    "ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef",
    "ClientListLogSubscriptionsResponseTypeDef",
    "ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef",
    "ClientListSchemaExtensionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRegisterCertificateResponseTypeDef",
    "ClientRejectSharedDirectoryResponseTypeDef",
    "ClientShareDirectoryResponseTypeDef",
    "ClientShareDirectoryShareTargetTypeDef",
    "ClientStartSchemaExtensionResponseTypeDef",
    "ClientUnshareDirectoryResponseTypeDef",
    "ClientUnshareDirectoryUnshareTargetTypeDef",
    "ClientUpdateRadiusRadiusSettingsTypeDef",
    "ClientUpdateTrustResponseTypeDef",
    "ClientVerifyTrustResponseTypeDef",
    "DescribeDirectoriesPaginatePaginationConfigTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef",
    "DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef",
    "DescribeDirectoriesPaginateResponseTypeDef",
    "DescribeDomainControllersPaginatePaginationConfigTypeDef",
    "DescribeDomainControllersPaginateResponseDomainControllersTypeDef",
    "DescribeDomainControllersPaginateResponseTypeDef",
    "DescribeSharedDirectoriesPaginatePaginationConfigTypeDef",
    "DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef",
    "DescribeSharedDirectoriesPaginateResponseTypeDef",
    "DescribeSnapshotsPaginatePaginationConfigTypeDef",
    "DescribeSnapshotsPaginateResponseSnapshotsTypeDef",
    "DescribeSnapshotsPaginateResponseTypeDef",
    "DescribeTrustsPaginatePaginationConfigTypeDef",
    "DescribeTrustsPaginateResponseTrustsTypeDef",
    "DescribeTrustsPaginateResponseTypeDef",
    "ListIpRoutesPaginatePaginationConfigTypeDef",
    "ListIpRoutesPaginateResponseIpRoutesInfoTypeDef",
    "ListIpRoutesPaginateResponseTypeDef",
    "ListLogSubscriptionsPaginatePaginationConfigTypeDef",
    "ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef",
    "ListLogSubscriptionsPaginateResponseTypeDef",
    "ListSchemaExtensionsPaginatePaginationConfigTypeDef",
    "ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef",
    "ListSchemaExtensionsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
)


_ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef = TypedDict(
    "_ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef(
    _ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef
):
    """
    - **SharedDirectory** *(dict) --*

      The shared directory in the directory consumer account.
      - **OwnerAccountId** *(string) --*

        Identifier of the directory owner account, which contains the directory that has been shared
        to the consumer account.
    """


_ClientAcceptSharedDirectoryResponseTypeDef = TypedDict(
    "_ClientAcceptSharedDirectoryResponseTypeDef",
    {"SharedDirectory": ClientAcceptSharedDirectoryResponseSharedDirectoryTypeDef},
    total=False,
)


class ClientAcceptSharedDirectoryResponseTypeDef(_ClientAcceptSharedDirectoryResponseTypeDef):
    """
    - *(dict) --*

      - **SharedDirectory** *(dict) --*

        The shared directory in the directory consumer account.
        - **OwnerAccountId** *(string) --*

          Identifier of the directory owner account, which contains the directory that has been
          shared to the consumer account.
    """


_ClientAddIpRoutesIpRoutesTypeDef = TypedDict(
    "_ClientAddIpRoutesIpRoutesTypeDef", {"CidrIp": str, "Description": str}, total=False
)


class ClientAddIpRoutesIpRoutesTypeDef(_ClientAddIpRoutesIpRoutesTypeDef):
    """
    - *(dict) --*

      IP address block. This is often the address block of the DNS server used for your on-premises
      domain.
      - **CidrIp** *(string) --*

        IP address block using CIDR format, for example 10.0.0.0/24. This is often the address block
        of the DNS server used for your on-premises domain. For a single IP address use a CIDR
        address block with /32. For example 10.0.0.0/32.
    """


_RequiredClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_RequiredClientAddTagsToResourceTagsTypeDef", {"Key": str}
)
_OptionalClientAddTagsToResourceTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsToResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsToResourceTagsTypeDef(
    _RequiredClientAddTagsToResourceTagsTypeDef, _OptionalClientAddTagsToResourceTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to a directory consisting of a key-value pair.
      - **Key** *(string) --***[REQUIRED]**

        Required name of the tag. The string value can be Unicode characters and cannot be prefixed
        with "aws:". The string can contain only the set of Unicode letters, digits, white-space,
        '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_RequiredClientConnectDirectoryConnectSettingsTypeDef = TypedDict(
    "_RequiredClientConnectDirectoryConnectSettingsTypeDef", {"VpcId": str}
)
_OptionalClientConnectDirectoryConnectSettingsTypeDef = TypedDict(
    "_OptionalClientConnectDirectoryConnectSettingsTypeDef",
    {"SubnetIds": List[str], "CustomerDnsIps": List[str], "CustomerUserName": str},
    total=False,
)


class ClientConnectDirectoryConnectSettingsTypeDef(
    _RequiredClientConnectDirectoryConnectSettingsTypeDef,
    _OptionalClientConnectDirectoryConnectSettingsTypeDef,
):
    """
    A  DirectoryConnectSettings object that contains additional information for the operation.
    - **VpcId** *(string) --***[REQUIRED]**

      The identifier of the VPC in which the AD Connector is created.
    """


_ClientConnectDirectoryResponseTypeDef = TypedDict(
    "_ClientConnectDirectoryResponseTypeDef", {"DirectoryId": str}, total=False
)


class ClientConnectDirectoryResponseTypeDef(_ClientConnectDirectoryResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  ConnectDirectory operation.
      - **DirectoryId** *(string) --*

        The identifier of the new directory.
    """


_RequiredClientConnectDirectoryTagsTypeDef = TypedDict(
    "_RequiredClientConnectDirectoryTagsTypeDef", {"Key": str}
)
_OptionalClientConnectDirectoryTagsTypeDef = TypedDict(
    "_OptionalClientConnectDirectoryTagsTypeDef", {"Value": str}, total=False
)


class ClientConnectDirectoryTagsTypeDef(
    _RequiredClientConnectDirectoryTagsTypeDef, _OptionalClientConnectDirectoryTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to a directory consisting of a key-value pair.
      - **Key** *(string) --***[REQUIRED]**

        Required name of the tag. The string value can be Unicode characters and cannot be prefixed
        with "aws:". The string can contain only the set of Unicode letters, digits, white-space,
        '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientCreateAliasResponseTypeDef = TypedDict(
    "_ClientCreateAliasResponseTypeDef", {"DirectoryId": str, "Alias": str}, total=False
)


class ClientCreateAliasResponseTypeDef(_ClientCreateAliasResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  CreateAlias operation.
      - **DirectoryId** *(string) --*

        The identifier of the directory.
    """


_ClientCreateComputerComputerAttributesTypeDef = TypedDict(
    "_ClientCreateComputerComputerAttributesTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientCreateComputerComputerAttributesTypeDef(_ClientCreateComputerComputerAttributesTypeDef):
    """
    - *(dict) --*

      Represents a named directory attribute.
      - **Name** *(string) --*

        The name of the attribute.
    """


_ClientCreateComputerResponseComputerComputerAttributesTypeDef = TypedDict(
    "_ClientCreateComputerResponseComputerComputerAttributesTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientCreateComputerResponseComputerComputerAttributesTypeDef(
    _ClientCreateComputerResponseComputerComputerAttributesTypeDef
):
    pass


_ClientCreateComputerResponseComputerTypeDef = TypedDict(
    "_ClientCreateComputerResponseComputerTypeDef",
    {
        "ComputerId": str,
        "ComputerName": str,
        "ComputerAttributes": List[ClientCreateComputerResponseComputerComputerAttributesTypeDef],
    },
    total=False,
)


class ClientCreateComputerResponseComputerTypeDef(_ClientCreateComputerResponseComputerTypeDef):
    """
    - **Computer** *(dict) --*

      A  Computer object that represents the computer account.
      - **ComputerId** *(string) --*

        The identifier of the computer.
    """


_ClientCreateComputerResponseTypeDef = TypedDict(
    "_ClientCreateComputerResponseTypeDef",
    {"Computer": ClientCreateComputerResponseComputerTypeDef},
    total=False,
)


class ClientCreateComputerResponseTypeDef(_ClientCreateComputerResponseTypeDef):
    """
    - *(dict) --*

      Contains the results for the  CreateComputer operation.
      - **Computer** *(dict) --*

        A  Computer object that represents the computer account.
        - **ComputerId** *(string) --*

          The identifier of the computer.
    """


_ClientCreateDirectoryResponseTypeDef = TypedDict(
    "_ClientCreateDirectoryResponseTypeDef", {"DirectoryId": str}, total=False
)


class ClientCreateDirectoryResponseTypeDef(_ClientCreateDirectoryResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  CreateDirectory operation.
      - **DirectoryId** *(string) --*

        The identifier of the directory that was created.
    """


_RequiredClientCreateDirectoryTagsTypeDef = TypedDict(
    "_RequiredClientCreateDirectoryTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDirectoryTagsTypeDef = TypedDict(
    "_OptionalClientCreateDirectoryTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDirectoryTagsTypeDef(
    _RequiredClientCreateDirectoryTagsTypeDef, _OptionalClientCreateDirectoryTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to a directory consisting of a key-value pair.
      - **Key** *(string) --***[REQUIRED]**

        Required name of the tag. The string value can be Unicode characters and cannot be prefixed
        with "aws:". The string can contain only the set of Unicode letters, digits, white-space,
        '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_RequiredClientCreateDirectoryVpcSettingsTypeDef = TypedDict(
    "_RequiredClientCreateDirectoryVpcSettingsTypeDef", {"VpcId": str}
)
_OptionalClientCreateDirectoryVpcSettingsTypeDef = TypedDict(
    "_OptionalClientCreateDirectoryVpcSettingsTypeDef", {"SubnetIds": List[str]}, total=False
)


class ClientCreateDirectoryVpcSettingsTypeDef(
    _RequiredClientCreateDirectoryVpcSettingsTypeDef,
    _OptionalClientCreateDirectoryVpcSettingsTypeDef,
):
    """
    A  DirectoryVpcSettings object that contains additional information for the operation.
    - **VpcId** *(string) --***[REQUIRED]**

      The identifier of the VPC in which to create the directory.
    """


_ClientCreateMicrosoftAdResponseTypeDef = TypedDict(
    "_ClientCreateMicrosoftAdResponseTypeDef", {"DirectoryId": str}, total=False
)


class ClientCreateMicrosoftAdResponseTypeDef(_ClientCreateMicrosoftAdResponseTypeDef):
    """
    - *(dict) --*

      Result of a CreateMicrosoftAD request.
      - **DirectoryId** *(string) --*

        The identifier of the directory that was created.
    """


_RequiredClientCreateMicrosoftAdTagsTypeDef = TypedDict(
    "_RequiredClientCreateMicrosoftAdTagsTypeDef", {"Key": str}
)
_OptionalClientCreateMicrosoftAdTagsTypeDef = TypedDict(
    "_OptionalClientCreateMicrosoftAdTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateMicrosoftAdTagsTypeDef(
    _RequiredClientCreateMicrosoftAdTagsTypeDef, _OptionalClientCreateMicrosoftAdTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to a directory consisting of a key-value pair.
      - **Key** *(string) --***[REQUIRED]**

        Required name of the tag. The string value can be Unicode characters and cannot be prefixed
        with "aws:". The string can contain only the set of Unicode letters, digits, white-space,
        '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_RequiredClientCreateMicrosoftAdVpcSettingsTypeDef = TypedDict(
    "_RequiredClientCreateMicrosoftAdVpcSettingsTypeDef", {"VpcId": str}
)
_OptionalClientCreateMicrosoftAdVpcSettingsTypeDef = TypedDict(
    "_OptionalClientCreateMicrosoftAdVpcSettingsTypeDef", {"SubnetIds": List[str]}, total=False
)


class ClientCreateMicrosoftAdVpcSettingsTypeDef(
    _RequiredClientCreateMicrosoftAdVpcSettingsTypeDef,
    _OptionalClientCreateMicrosoftAdVpcSettingsTypeDef,
):
    """
    Contains VPC information for the  CreateDirectory or  CreateMicrosoftAD operation.
    - **VpcId** *(string) --***[REQUIRED]**

      The identifier of the VPC in which to create the directory.
    """


_ClientCreateSnapshotResponseTypeDef = TypedDict(
    "_ClientCreateSnapshotResponseTypeDef", {"SnapshotId": str}, total=False
)


class ClientCreateSnapshotResponseTypeDef(_ClientCreateSnapshotResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  CreateSnapshot operation.
      - **SnapshotId** *(string) --*

        The identifier of the snapshot that was created.
    """


_ClientCreateTrustResponseTypeDef = TypedDict(
    "_ClientCreateTrustResponseTypeDef", {"TrustId": str}, total=False
)


class ClientCreateTrustResponseTypeDef(_ClientCreateTrustResponseTypeDef):
    """
    - *(dict) --*

      The result of a CreateTrust request.
      - **TrustId** *(string) --*

        A unique identifier for the trust relationship that was created.
    """


_ClientDeleteDirectoryResponseTypeDef = TypedDict(
    "_ClientDeleteDirectoryResponseTypeDef", {"DirectoryId": str}, total=False
)


class ClientDeleteDirectoryResponseTypeDef(_ClientDeleteDirectoryResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  DeleteDirectory operation.
      - **DirectoryId** *(string) --*

        The directory identifier.
    """


_ClientDeleteSnapshotResponseTypeDef = TypedDict(
    "_ClientDeleteSnapshotResponseTypeDef", {"SnapshotId": str}, total=False
)


class ClientDeleteSnapshotResponseTypeDef(_ClientDeleteSnapshotResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  DeleteSnapshot operation.
      - **SnapshotId** *(string) --*

        The identifier of the directory snapshot that was deleted.
    """


_ClientDeleteTrustResponseTypeDef = TypedDict(
    "_ClientDeleteTrustResponseTypeDef", {"TrustId": str}, total=False
)


class ClientDeleteTrustResponseTypeDef(_ClientDeleteTrustResponseTypeDef):
    """
    - *(dict) --*

      The result of a DeleteTrust request.
      - **TrustId** *(string) --*

        The Trust ID of the trust relationship that was deleted.
    """


_ClientDescribeCertificateResponseCertificateTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseCertificateTypeDef",
    {
        "CertificateId": str,
        "State": Literal[
            "Registering",
            "Registered",
            "RegisterFailed",
            "Deregistering",
            "Deregistered",
            "DeregisterFailed",
        ],
        "StateReason": str,
        "CommonName": str,
        "RegisteredDateTime": datetime,
        "ExpiryDateTime": datetime,
    },
    total=False,
)


class ClientDescribeCertificateResponseCertificateTypeDef(
    _ClientDescribeCertificateResponseCertificateTypeDef
):
    """
    - **Certificate** *(dict) --*

      Information about the certificate, including registered date time, certificate state, the
      reason for the state, expiration date time, and certificate common name.
      - **CertificateId** *(string) --*

        The identifier of the certificate.
    """


_ClientDescribeCertificateResponseTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseTypeDef",
    {"Certificate": ClientDescribeCertificateResponseCertificateTypeDef},
    total=False,
)


class ClientDescribeCertificateResponseTypeDef(_ClientDescribeCertificateResponseTypeDef):
    """
    - *(dict) --*

      - **Certificate** *(dict) --*

        Information about the certificate, including registered date time, certificate state, the
        reason for the state, expiration date time, and certificate common name.
        - **CertificateId** *(string) --*

          The identifier of the certificate.
    """


_ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef = TypedDict(
    "_ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef",
    {"RemoteDomainName": str, "DnsIpAddrs": List[str], "ReplicationScope": str},
    total=False,
)


class ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef(
    _ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef
):
    """
    - *(dict) --*

      Points to a remote domain with which you are setting up a trust relationship. Conditional
      forwarders are required in order to set up a trust relationship with another domain.
      - **RemoteDomainName** *(string) --*

        The fully qualified domain name (FQDN) of the remote domains pointed to by the conditional
        forwarder.
    """


_ClientDescribeConditionalForwardersResponseTypeDef = TypedDict(
    "_ClientDescribeConditionalForwardersResponseTypeDef",
    {
        "ConditionalForwarders": List[
            ClientDescribeConditionalForwardersResponseConditionalForwardersTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConditionalForwardersResponseTypeDef(
    _ClientDescribeConditionalForwardersResponseTypeDef
):
    """
    - *(dict) --*

      The result of a DescribeConditionalForwarder request.
      - **ConditionalForwarders** *(list) --*

        The list of conditional forwarders that have been created.
        - *(dict) --*

          Points to a remote domain with which you are setting up a trust relationship. Conditional
          forwarders are required in order to set up a trust relationship with another domain.
          - **RemoteDomainName** *(string) --*

            The fully qualified domain name (FQDN) of the remote domains pointed to by the
            conditional forwarder.
    """


_ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerUserName": str,
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
        "ConnectIps": List[str],
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef
):
    pass


_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef
):
    pass


_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupId": str, "AvailabilityZones": List[str]},
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef
):
    pass


_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "AccountId": str,
        "DnsIpAddrs": List[str],
        "VpcSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef,
        "RadiusSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef,
        "RadiusStatus": Literal["Creating", "Completed", "Failed"],
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef
):
    pass


_ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef
):
    pass


_ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupId": str, "AvailabilityZones": List[str]},
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef
):
    pass


_ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef",
    {
        "DirectoryId": str,
        "Name": str,
        "ShortName": str,
        "Size": Literal["Small", "Large"],
        "Edition": Literal["Enterprise", "Standard"],
        "Alias": str,
        "AccessUrl": str,
        "Description": str,
        "DnsIpAddrs": List[str],
        "Stage": Literal[
            "Requested",
            "Creating",
            "Created",
            "Active",
            "Inoperable",
            "Impaired",
            "Restoring",
            "RestoreFailed",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "ShareNotes": str,
        "LaunchTime": datetime,
        "StageLastUpdatedDateTime": datetime,
        "Type": Literal["SimpleAD", "ADConnector", "MicrosoftAD", "SharedMicrosoftAD"],
        "VpcSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsVpcSettingsTypeDef,
        "ConnectSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsConnectSettingsTypeDef,
        "RadiusSettings": ClientDescribeDirectoriesResponseDirectoryDescriptionsRadiusSettingsTypeDef,
        "RadiusStatus": Literal["Creating", "Completed", "Failed"],
        "StageReason": str,
        "SsoEnabled": bool,
        "DesiredNumberOfDomainControllers": int,
        "OwnerDirectoryDescription": ClientDescribeDirectoriesResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef,
    },
    total=False,
)


class ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef(
    _ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef
):
    """
    - *(dict) --*

      Contains information about an AWS Directory Service directory.
      - **DirectoryId** *(string) --*

        The directory identifier.
    """


_ClientDescribeDirectoriesResponseTypeDef = TypedDict(
    "_ClientDescribeDirectoriesResponseTypeDef",
    {
        "DirectoryDescriptions": List[
            ClientDescribeDirectoriesResponseDirectoryDescriptionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeDirectoriesResponseTypeDef(_ClientDescribeDirectoriesResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  DescribeDirectories operation.
      - **DirectoryDescriptions** *(list) --*

        The list of  DirectoryDescription objects that were retrieved.
        It is possible that this list contains less than the number of items specified in the
        ``Limit`` member of the request. This occurs if there are less than the requested number of
        items left to retrieve, or if the limitations of the operation have been exceeded.
        - *(dict) --*

          Contains information about an AWS Directory Service directory.
          - **DirectoryId** *(string) --*

            The directory identifier.
    """


_ClientDescribeDomainControllersResponseDomainControllersTypeDef = TypedDict(
    "_ClientDescribeDomainControllersResponseDomainControllersTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerId": str,
        "DnsIpAddr": str,
        "VpcId": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "Status": Literal[
            "Creating", "Active", "Impaired", "Restoring", "Deleting", "Deleted", "Failed"
        ],
        "StatusReason": str,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeDomainControllersResponseDomainControllersTypeDef(
    _ClientDescribeDomainControllersResponseDomainControllersTypeDef
):
    """
    - *(dict) --*

      Contains information about the domain controllers for a specified directory.
      - **DirectoryId** *(string) --*

        Identifier of the directory where the domain controller resides.
    """


_ClientDescribeDomainControllersResponseTypeDef = TypedDict(
    "_ClientDescribeDomainControllersResponseTypeDef",
    {
        "DomainControllers": List[ClientDescribeDomainControllersResponseDomainControllersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeDomainControllersResponseTypeDef(
    _ClientDescribeDomainControllersResponseTypeDef
):
    """
    - *(dict) --*

      - **DomainControllers** *(list) --*

        List of the  DomainController objects that were retrieved.
        - *(dict) --*

          Contains information about the domain controllers for a specified directory.
          - **DirectoryId** *(string) --*

            Identifier of the directory where the domain controller resides.
    """


_ClientDescribeEventTopicsResponseEventTopicsTypeDef = TypedDict(
    "_ClientDescribeEventTopicsResponseEventTopicsTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
        "TopicArn": str,
        "CreatedDateTime": datetime,
        "Status": Literal["Registered", "Topic not found", "Failed", "Deleted"],
    },
    total=False,
)


class ClientDescribeEventTopicsResponseEventTopicsTypeDef(
    _ClientDescribeEventTopicsResponseEventTopicsTypeDef
):
    """
    - *(dict) --*

      Information about SNS topic and AWS Directory Service directory associations.
      - **DirectoryId** *(string) --*

        The Directory ID of an AWS Directory Service directory that will publish status messages to
        an SNS topic.
    """


_ClientDescribeEventTopicsResponseTypeDef = TypedDict(
    "_ClientDescribeEventTopicsResponseTypeDef",
    {"EventTopics": List[ClientDescribeEventTopicsResponseEventTopicsTypeDef]},
    total=False,
)


class ClientDescribeEventTopicsResponseTypeDef(_ClientDescribeEventTopicsResponseTypeDef):
    """
    - *(dict) --*

      The result of a DescribeEventTopic request.
      - **EventTopics** *(list) --*

        A list of SNS topic names that receive status messages from the specified Directory ID.
        - *(dict) --*

          Information about SNS topic and AWS Directory Service directory associations.
          - **DirectoryId** *(string) --*

            The Directory ID of an AWS Directory Service directory that will publish status messages
            to an SNS topic.
    """


_ClientDescribeLdapsSettingsResponseLDAPSSettingsInfoTypeDef = TypedDict(
    "_ClientDescribeLdapsSettingsResponseLDAPSSettingsInfoTypeDef",
    {
        "LDAPSStatus": Literal["Enabling", "Enabled", "EnableFailed", "Disabled"],
        "LDAPSStatusReason": str,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeLdapsSettingsResponseLDAPSSettingsInfoTypeDef(
    _ClientDescribeLdapsSettingsResponseLDAPSSettingsInfoTypeDef
):
    """
    - *(dict) --*

      Contains general information about the LDAPS settings.
      - **LDAPSStatus** *(string) --*

        The state of the LDAPS settings.
    """


_ClientDescribeLdapsSettingsResponseTypeDef = TypedDict(
    "_ClientDescribeLdapsSettingsResponseTypeDef",
    {
        "LDAPSSettingsInfo": List[ClientDescribeLdapsSettingsResponseLDAPSSettingsInfoTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeLdapsSettingsResponseTypeDef(_ClientDescribeLdapsSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **LDAPSSettingsInfo** *(list) --*

        Information about LDAP security for the specified directory, including status of enablement,
        state last updated date time, and the reason for the state.
        - *(dict) --*

          Contains general information about the LDAPS settings.
          - **LDAPSStatus** *(string) --*

            The state of the LDAPS settings.
    """


_ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef = TypedDict(
    "_ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)


class ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef(
    _ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef
):
    """
    - *(dict) --*

      Details about the shared directory in the directory owner account for which the share request
      in the directory consumer account has been accepted.
      - **OwnerAccountId** *(string) --*

        Identifier of the directory owner account, which contains the directory that has been shared
        to the consumer account.
    """


_ClientDescribeSharedDirectoriesResponseTypeDef = TypedDict(
    "_ClientDescribeSharedDirectoriesResponseTypeDef",
    {
        "SharedDirectories": List[ClientDescribeSharedDirectoriesResponseSharedDirectoriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeSharedDirectoriesResponseTypeDef(
    _ClientDescribeSharedDirectoriesResponseTypeDef
):
    """
    - *(dict) --*

      - **SharedDirectories** *(list) --*

        A list of all shared directories in your account.
        - *(dict) --*

          Details about the shared directory in the directory owner account for which the share
          request in the directory consumer account has been accepted.
          - **OwnerAccountId** *(string) --*

            Identifier of the directory owner account, which contains the directory that has been
            shared to the consumer account.
    """


_ClientDescribeSnapshotsResponseSnapshotsTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseSnapshotsTypeDef",
    {
        "DirectoryId": str,
        "SnapshotId": str,
        "Type": Literal["Auto", "Manual"],
        "Name": str,
        "Status": Literal["Creating", "Completed", "Failed"],
        "StartTime": datetime,
    },
    total=False,
)


class ClientDescribeSnapshotsResponseSnapshotsTypeDef(
    _ClientDescribeSnapshotsResponseSnapshotsTypeDef
):
    """
    - *(dict) --*

      Describes a directory snapshot.
      - **DirectoryId** *(string) --*

        The directory identifier.
    """


_ClientDescribeSnapshotsResponseTypeDef = TypedDict(
    "_ClientDescribeSnapshotsResponseTypeDef",
    {"Snapshots": List[ClientDescribeSnapshotsResponseSnapshotsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeSnapshotsResponseTypeDef(_ClientDescribeSnapshotsResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  DescribeSnapshots operation.
      - **Snapshots** *(list) --*

        The list of  Snapshot objects that were retrieved.
        It is possible that this list contains less than the number of items specified in the
        *Limit* member of the request. This occurs if there are less than the requested number of
        items left to retrieve, or if the limitations of the operation have been exceeded.
        - *(dict) --*

          Describes a directory snapshot.
          - **DirectoryId** *(string) --*

            The directory identifier.
    """


_ClientDescribeTrustsResponseTrustsTypeDef = TypedDict(
    "_ClientDescribeTrustsResponseTrustsTypeDef",
    {
        "DirectoryId": str,
        "TrustId": str,
        "RemoteDomainName": str,
        "TrustType": Literal["Forest", "External"],
        "TrustDirection": Literal["One-Way: Outgoing", "One-Way: Incoming", "Two-Way"],
        "TrustState": Literal[
            "Creating",
            "Created",
            "Verifying",
            "VerifyFailed",
            "Verified",
            "Updating",
            "UpdateFailed",
            "Updated",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
        "StateLastUpdatedDateTime": datetime,
        "TrustStateReason": str,
        "SelectiveAuth": Literal["Enabled", "Disabled"],
    },
    total=False,
)


class ClientDescribeTrustsResponseTrustsTypeDef(_ClientDescribeTrustsResponseTrustsTypeDef):
    """
    - *(dict) --*

      Describes a trust relationship between an AWS Managed Microsoft AD directory and an external
      domain.
      - **DirectoryId** *(string) --*

        The Directory ID of the AWS directory involved in the trust relationship.
    """


_ClientDescribeTrustsResponseTypeDef = TypedDict(
    "_ClientDescribeTrustsResponseTypeDef",
    {"Trusts": List[ClientDescribeTrustsResponseTrustsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeTrustsResponseTypeDef(_ClientDescribeTrustsResponseTypeDef):
    """
    - *(dict) --*

      The result of a DescribeTrust request.
      - **Trusts** *(list) --*

        The list of Trust objects that were retrieved.
        It is possible that this list contains less than the number of items specified in the
        *Limit* member of the request. This occurs if there are less than the requested number of
        items left to retrieve, or if the limitations of the operation have been exceeded.
        - *(dict) --*

          Describes a trust relationship between an AWS Managed Microsoft AD directory and an
          external domain.
          - **DirectoryId** *(string) --*

            The Directory ID of the AWS directory involved in the trust relationship.
    """


_ClientEnableRadiusRadiusSettingsTypeDef = TypedDict(
    "_ClientEnableRadiusRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class ClientEnableRadiusRadiusSettingsTypeDef(_ClientEnableRadiusRadiusSettingsTypeDef):
    """
    A  RadiusSettings object that contains information about the RADIUS server.
    - **RadiusServers** *(list) --*

      An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP
      addresses of your RADIUS server load balancer.
      - *(string) --*
    """


_ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef = TypedDict(
    "_ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef",
    {
        "CloudOnlyDirectoriesLimit": int,
        "CloudOnlyDirectoriesCurrentCount": int,
        "CloudOnlyDirectoriesLimitReached": bool,
        "CloudOnlyMicrosoftADLimit": int,
        "CloudOnlyMicrosoftADCurrentCount": int,
        "CloudOnlyMicrosoftADLimitReached": bool,
        "ConnectedDirectoriesLimit": int,
        "ConnectedDirectoriesCurrentCount": int,
        "ConnectedDirectoriesLimitReached": bool,
    },
    total=False,
)


class ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef(
    _ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef
):
    """
    - **DirectoryLimits** *(dict) --*

      A  DirectoryLimits object that contains the directory limits for the current rRegion.
      - **CloudOnlyDirectoriesLimit** *(integer) --*

        The maximum number of cloud directories allowed in the Region.
    """


_ClientGetDirectoryLimitsResponseTypeDef = TypedDict(
    "_ClientGetDirectoryLimitsResponseTypeDef",
    {"DirectoryLimits": ClientGetDirectoryLimitsResponseDirectoryLimitsTypeDef},
    total=False,
)


class ClientGetDirectoryLimitsResponseTypeDef(_ClientGetDirectoryLimitsResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  GetDirectoryLimits operation.
      - **DirectoryLimits** *(dict) --*

        A  DirectoryLimits object that contains the directory limits for the current rRegion.
        - **CloudOnlyDirectoriesLimit** *(integer) --*

          The maximum number of cloud directories allowed in the Region.
    """


_ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef = TypedDict(
    "_ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef",
    {
        "ManualSnapshotsLimit": int,
        "ManualSnapshotsCurrentCount": int,
        "ManualSnapshotsLimitReached": bool,
    },
    total=False,
)


class ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef(
    _ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef
):
    """
    - **SnapshotLimits** *(dict) --*

      A  SnapshotLimits object that contains the manual snapshot limits for the specified directory.
      - **ManualSnapshotsLimit** *(integer) --*

        The maximum number of manual snapshots allowed.
    """


_ClientGetSnapshotLimitsResponseTypeDef = TypedDict(
    "_ClientGetSnapshotLimitsResponseTypeDef",
    {"SnapshotLimits": ClientGetSnapshotLimitsResponseSnapshotLimitsTypeDef},
    total=False,
)


class ClientGetSnapshotLimitsResponseTypeDef(_ClientGetSnapshotLimitsResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  GetSnapshotLimits operation.
      - **SnapshotLimits** *(dict) --*

        A  SnapshotLimits object that contains the manual snapshot limits for the specified
        directory.
        - **ManualSnapshotsLimit** *(integer) --*

          The maximum number of manual snapshots allowed.
    """


_ClientListCertificatesResponseCertificatesInfoTypeDef = TypedDict(
    "_ClientListCertificatesResponseCertificatesInfoTypeDef",
    {
        "CertificateId": str,
        "CommonName": str,
        "State": Literal[
            "Registering",
            "Registered",
            "RegisterFailed",
            "Deregistering",
            "Deregistered",
            "DeregisterFailed",
        ],
    },
    total=False,
)


class ClientListCertificatesResponseCertificatesInfoTypeDef(
    _ClientListCertificatesResponseCertificatesInfoTypeDef
):
    pass


_ClientListCertificatesResponseTypeDef = TypedDict(
    "_ClientListCertificatesResponseTypeDef",
    {
        "NextToken": str,
        "CertificatesInfo": List[ClientListCertificatesResponseCertificatesInfoTypeDef],
    },
    total=False,
)


class ClientListCertificatesResponseTypeDef(_ClientListCertificatesResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        Indicates whether another page of certificates is available when the number of available
        certificates exceeds the page limit.
    """


_ClientListIpRoutesResponseIpRoutesInfoTypeDef = TypedDict(
    "_ClientListIpRoutesResponseIpRoutesInfoTypeDef",
    {
        "DirectoryId": str,
        "CidrIp": str,
        "IpRouteStatusMsg": Literal[
            "Adding", "Added", "Removing", "Removed", "AddFailed", "RemoveFailed"
        ],
        "AddedDateTime": datetime,
        "IpRouteStatusReason": str,
        "Description": str,
    },
    total=False,
)


class ClientListIpRoutesResponseIpRoutesInfoTypeDef(_ClientListIpRoutesResponseIpRoutesInfoTypeDef):
    """
    - *(dict) --*

      Information about one or more IP address blocks.
      - **DirectoryId** *(string) --*

        Identifier (ID) of the directory associated with the IP addresses.
    """


_ClientListIpRoutesResponseTypeDef = TypedDict(
    "_ClientListIpRoutesResponseTypeDef",
    {"IpRoutesInfo": List[ClientListIpRoutesResponseIpRoutesInfoTypeDef], "NextToken": str},
    total=False,
)


class ClientListIpRoutesResponseTypeDef(_ClientListIpRoutesResponseTypeDef):
    """
    - *(dict) --*

      - **IpRoutesInfo** *(list) --*

        A list of  IpRoute s.
        - *(dict) --*

          Information about one or more IP address blocks.
          - **DirectoryId** *(string) --*

            Identifier (ID) of the directory associated with the IP addresses.
    """


_ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef = TypedDict(
    "_ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef",
    {"DirectoryId": str, "LogGroupName": str, "SubscriptionCreatedDateTime": datetime},
    total=False,
)


class ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef(
    _ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef
):
    """
    - *(dict) --*

      Represents a log subscription, which tracks real-time data from a chosen log group to a
      specified destination.
      - **DirectoryId** *(string) --*

        Identifier (ID) of the directory that you want to associate with the log subscription.
    """


_ClientListLogSubscriptionsResponseTypeDef = TypedDict(
    "_ClientListLogSubscriptionsResponseTypeDef",
    {
        "LogSubscriptions": List[ClientListLogSubscriptionsResponseLogSubscriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListLogSubscriptionsResponseTypeDef(_ClientListLogSubscriptionsResponseTypeDef):
    """
    - *(dict) --*

      - **LogSubscriptions** *(list) --*

        A list of active  LogSubscription objects for calling the AWS account.
        - *(dict) --*

          Represents a log subscription, which tracks real-time data from a chosen log group to a
          specified destination.
          - **DirectoryId** *(string) --*

            Identifier (ID) of the directory that you want to associate with the log subscription.
    """


_ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef = TypedDict(
    "_ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
        "Description": str,
        "SchemaExtensionStatus": Literal[
            "Initializing",
            "CreatingSnapshot",
            "UpdatingSchema",
            "Replicating",
            "CancelInProgress",
            "RollbackInProgress",
            "Cancelled",
            "Failed",
            "Completed",
        ],
        "SchemaExtensionStatusReason": str,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)


class ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef(
    _ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef
):
    """
    - *(dict) --*

      Information about a schema extension.
      - **DirectoryId** *(string) --*

        The identifier of the directory to which the schema extension is applied.
    """


_ClientListSchemaExtensionsResponseTypeDef = TypedDict(
    "_ClientListSchemaExtensionsResponseTypeDef",
    {
        "SchemaExtensionsInfo": List[ClientListSchemaExtensionsResponseSchemaExtensionsInfoTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListSchemaExtensionsResponseTypeDef(_ClientListSchemaExtensionsResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaExtensionsInfo** *(list) --*

        Information about the schema extensions applied to the directory.
        - *(dict) --*

          Information about a schema extension.
          - **DirectoryId** *(string) --*

            The identifier of the directory to which the schema extension is applied.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      Metadata assigned to a directory consisting of a key-value pair.
      - **Key** *(string) --*

        Required name of the tag. The string value can be Unicode characters and cannot be prefixed
        with "aws:". The string can contain only the set of Unicode letters, digits, white-space,
        '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        List of tags returned by the ListTagsForResource operation.
        - *(dict) --*

          Metadata assigned to a directory consisting of a key-value pair.
          - **Key** *(string) --*

            Required name of the tag. The string value can be Unicode characters and cannot be
            prefixed with "aws:". The string can contain only the set of Unicode letters, digits,
            white-space, '_', '.', '/', '=', '+', '-' (Java regex:
            "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ClientRegisterCertificateResponseTypeDef = TypedDict(
    "_ClientRegisterCertificateResponseTypeDef", {"CertificateId": str}, total=False
)


class ClientRegisterCertificateResponseTypeDef(_ClientRegisterCertificateResponseTypeDef):
    """
    - *(dict) --*

      - **CertificateId** *(string) --*

        The identifier of the certificate.
    """


_ClientRejectSharedDirectoryResponseTypeDef = TypedDict(
    "_ClientRejectSharedDirectoryResponseTypeDef", {"SharedDirectoryId": str}, total=False
)


class ClientRejectSharedDirectoryResponseTypeDef(_ClientRejectSharedDirectoryResponseTypeDef):
    """
    - *(dict) --*

      - **SharedDirectoryId** *(string) --*

        Identifier of the shared directory in the directory consumer account.
    """


_ClientShareDirectoryResponseTypeDef = TypedDict(
    "_ClientShareDirectoryResponseTypeDef", {"SharedDirectoryId": str}, total=False
)


class ClientShareDirectoryResponseTypeDef(_ClientShareDirectoryResponseTypeDef):
    """
    - *(dict) --*

      - **SharedDirectoryId** *(string) --*

        Identifier of the directory that is stored in the directory consumer account that is shared
        from the specified directory (``DirectoryId`` ).
    """


_RequiredClientShareDirectoryShareTargetTypeDef = TypedDict(
    "_RequiredClientShareDirectoryShareTargetTypeDef", {"Id": str}
)
_OptionalClientShareDirectoryShareTargetTypeDef = TypedDict(
    "_OptionalClientShareDirectoryShareTargetTypeDef", {"Type": str}, total=False
)


class ClientShareDirectoryShareTargetTypeDef(
    _RequiredClientShareDirectoryShareTargetTypeDef, _OptionalClientShareDirectoryShareTargetTypeDef
):
    """
    Identifier for the directory consumer account with whom the directory is to be shared.
    - **Id** *(string) --***[REQUIRED]**

      Identifier of the directory consumer account.
    """


_ClientStartSchemaExtensionResponseTypeDef = TypedDict(
    "_ClientStartSchemaExtensionResponseTypeDef", {"SchemaExtensionId": str}, total=False
)


class ClientStartSchemaExtensionResponseTypeDef(_ClientStartSchemaExtensionResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaExtensionId** *(string) --*

        The identifier of the schema extension that will be applied.
    """


_ClientUnshareDirectoryResponseTypeDef = TypedDict(
    "_ClientUnshareDirectoryResponseTypeDef", {"SharedDirectoryId": str}, total=False
)


class ClientUnshareDirectoryResponseTypeDef(_ClientUnshareDirectoryResponseTypeDef):
    """
    - *(dict) --*

      - **SharedDirectoryId** *(string) --*

        Identifier of the directory stored in the directory consumer account that is to be unshared
        from the specified directory (``DirectoryId`` ).
    """


_RequiredClientUnshareDirectoryUnshareTargetTypeDef = TypedDict(
    "_RequiredClientUnshareDirectoryUnshareTargetTypeDef", {"Id": str}
)
_OptionalClientUnshareDirectoryUnshareTargetTypeDef = TypedDict(
    "_OptionalClientUnshareDirectoryUnshareTargetTypeDef", {"Type": str}, total=False
)


class ClientUnshareDirectoryUnshareTargetTypeDef(
    _RequiredClientUnshareDirectoryUnshareTargetTypeDef,
    _OptionalClientUnshareDirectoryUnshareTargetTypeDef,
):
    """
    Identifier for the directory consumer account with whom the directory has to be unshared.
    - **Id** *(string) --***[REQUIRED]**

      Identifier of the directory consumer account.
    """


_ClientUpdateRadiusRadiusSettingsTypeDef = TypedDict(
    "_ClientUpdateRadiusRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class ClientUpdateRadiusRadiusSettingsTypeDef(_ClientUpdateRadiusRadiusSettingsTypeDef):
    """
    A  RadiusSettings object that contains information about the RADIUS server.
    - **RadiusServers** *(list) --*

      An array of strings that contains the IP addresses of the RADIUS server endpoints, or the IP
      addresses of your RADIUS server load balancer.
      - *(string) --*
    """


_ClientUpdateTrustResponseTypeDef = TypedDict(
    "_ClientUpdateTrustResponseTypeDef", {"RequestId": str, "TrustId": str}, total=False
)


class ClientUpdateTrustResponseTypeDef(_ClientUpdateTrustResponseTypeDef):
    """
    - *(dict) --*

      - **RequestId** *(string) --*

        The AWS request identifier.
    """


_ClientVerifyTrustResponseTypeDef = TypedDict(
    "_ClientVerifyTrustResponseTypeDef", {"TrustId": str}, total=False
)


class ClientVerifyTrustResponseTypeDef(_ClientVerifyTrustResponseTypeDef):
    """
    - *(dict) --*

      Result of a VerifyTrust request.
      - **TrustId** *(string) --*

        The unique Trust ID of the trust relationship that was verified.
    """


_DescribeDirectoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDirectoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDirectoriesPaginatePaginationConfigTypeDef(
    _DescribeDirectoriesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerUserName": str,
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
        "ConnectIps": List[str],
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef
):
    pass


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef
):
    pass


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupId": str, "AvailabilityZones": List[str]},
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef
):
    pass


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "AccountId": str,
        "DnsIpAddrs": List[str],
        "VpcSettings": DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionVpcSettingsTypeDef,
        "RadiusSettings": DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionRadiusSettingsTypeDef,
        "RadiusStatus": Literal["Creating", "Completed", "Failed"],
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef
):
    pass


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": Literal["PAP", "CHAP", "MS-CHAPv1", "MS-CHAPv2"],
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef
):
    pass


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupId": str, "AvailabilityZones": List[str]},
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef
):
    pass


_DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef",
    {
        "DirectoryId": str,
        "Name": str,
        "ShortName": str,
        "Size": Literal["Small", "Large"],
        "Edition": Literal["Enterprise", "Standard"],
        "Alias": str,
        "AccessUrl": str,
        "Description": str,
        "DnsIpAddrs": List[str],
        "Stage": Literal[
            "Requested",
            "Creating",
            "Created",
            "Active",
            "Inoperable",
            "Impaired",
            "Restoring",
            "RestoreFailed",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "ShareNotes": str,
        "LaunchTime": datetime,
        "StageLastUpdatedDateTime": datetime,
        "Type": Literal["SimpleAD", "ADConnector", "MicrosoftAD", "SharedMicrosoftAD"],
        "VpcSettings": DescribeDirectoriesPaginateResponseDirectoryDescriptionsVpcSettingsTypeDef,
        "ConnectSettings": DescribeDirectoriesPaginateResponseDirectoryDescriptionsConnectSettingsTypeDef,
        "RadiusSettings": DescribeDirectoriesPaginateResponseDirectoryDescriptionsRadiusSettingsTypeDef,
        "RadiusStatus": Literal["Creating", "Completed", "Failed"],
        "StageReason": str,
        "SsoEnabled": bool,
        "DesiredNumberOfDomainControllers": int,
        "OwnerDirectoryDescription": DescribeDirectoriesPaginateResponseDirectoryDescriptionsOwnerDirectoryDescriptionTypeDef,
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef(
    _DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef
):
    """
    - *(dict) --*

      Contains information about an AWS Directory Service directory.
      - **DirectoryId** *(string) --*

        The directory identifier.
    """


_DescribeDirectoriesPaginateResponseTypeDef = TypedDict(
    "_DescribeDirectoriesPaginateResponseTypeDef",
    {
        "DirectoryDescriptions": List[
            DescribeDirectoriesPaginateResponseDirectoryDescriptionsTypeDef
        ]
    },
    total=False,
)


class DescribeDirectoriesPaginateResponseTypeDef(_DescribeDirectoriesPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  DescribeDirectories operation.
      - **DirectoryDescriptions** *(list) --*

        The list of  DirectoryDescription objects that were retrieved.
        It is possible that this list contains less than the number of items specified in the
        ``Limit`` member of the request. This occurs if there are less than the requested number of
        items left to retrieve, or if the limitations of the operation have been exceeded.
        - *(dict) --*

          Contains information about an AWS Directory Service directory.
          - **DirectoryId** *(string) --*

            The directory identifier.
    """


_DescribeDomainControllersPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeDomainControllersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeDomainControllersPaginatePaginationConfigTypeDef(
    _DescribeDomainControllersPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeDomainControllersPaginateResponseDomainControllersTypeDef = TypedDict(
    "_DescribeDomainControllersPaginateResponseDomainControllersTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerId": str,
        "DnsIpAddr": str,
        "VpcId": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "Status": Literal[
            "Creating", "Active", "Impaired", "Restoring", "Deleting", "Deleted", "Failed"
        ],
        "StatusReason": str,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
    },
    total=False,
)


class DescribeDomainControllersPaginateResponseDomainControllersTypeDef(
    _DescribeDomainControllersPaginateResponseDomainControllersTypeDef
):
    """
    - *(dict) --*

      Contains information about the domain controllers for a specified directory.
      - **DirectoryId** *(string) --*

        Identifier of the directory where the domain controller resides.
    """


_DescribeDomainControllersPaginateResponseTypeDef = TypedDict(
    "_DescribeDomainControllersPaginateResponseTypeDef",
    {"DomainControllers": List[DescribeDomainControllersPaginateResponseDomainControllersTypeDef]},
    total=False,
)


class DescribeDomainControllersPaginateResponseTypeDef(
    _DescribeDomainControllersPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **DomainControllers** *(list) --*

        List of the  DomainController objects that were retrieved.
        - *(dict) --*

          Contains information about the domain controllers for a specified directory.
          - **DirectoryId** *(string) --*

            Identifier of the directory where the domain controller resides.
    """


_DescribeSharedDirectoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSharedDirectoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSharedDirectoriesPaginatePaginationConfigTypeDef(
    _DescribeSharedDirectoriesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef = TypedDict(
    "_DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": Literal["ORGANIZATIONS", "HANDSHAKE"],
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": Literal[
            "Shared",
            "PendingAcceptance",
            "Rejected",
            "Rejecting",
            "RejectFailed",
            "Sharing",
            "ShareFailed",
            "Deleted",
            "Deleting",
        ],
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)


class DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef(
    _DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef
):
    """
    - *(dict) --*

      Details about the shared directory in the directory owner account for which the share request
      in the directory consumer account has been accepted.
      - **OwnerAccountId** *(string) --*

        Identifier of the directory owner account, which contains the directory that has been shared
        to the consumer account.
    """


_DescribeSharedDirectoriesPaginateResponseTypeDef = TypedDict(
    "_DescribeSharedDirectoriesPaginateResponseTypeDef",
    {"SharedDirectories": List[DescribeSharedDirectoriesPaginateResponseSharedDirectoriesTypeDef]},
    total=False,
)


class DescribeSharedDirectoriesPaginateResponseTypeDef(
    _DescribeSharedDirectoriesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **SharedDirectories** *(list) --*

        A list of all shared directories in your account.
        - *(dict) --*

          Details about the shared directory in the directory owner account for which the share
          request in the directory consumer account has been accepted.
          - **OwnerAccountId** *(string) --*

            Identifier of the directory owner account, which contains the directory that has been
            shared to the consumer account.
    """


_DescribeSnapshotsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeSnapshotsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeSnapshotsPaginatePaginationConfigTypeDef(
    _DescribeSnapshotsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeSnapshotsPaginateResponseSnapshotsTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseSnapshotsTypeDef",
    {
        "DirectoryId": str,
        "SnapshotId": str,
        "Type": Literal["Auto", "Manual"],
        "Name": str,
        "Status": Literal["Creating", "Completed", "Failed"],
        "StartTime": datetime,
    },
    total=False,
)


class DescribeSnapshotsPaginateResponseSnapshotsTypeDef(
    _DescribeSnapshotsPaginateResponseSnapshotsTypeDef
):
    """
    - *(dict) --*

      Describes a directory snapshot.
      - **DirectoryId** *(string) --*

        The directory identifier.
    """


_DescribeSnapshotsPaginateResponseTypeDef = TypedDict(
    "_DescribeSnapshotsPaginateResponseTypeDef",
    {"Snapshots": List[DescribeSnapshotsPaginateResponseSnapshotsTypeDef]},
    total=False,
)


class DescribeSnapshotsPaginateResponseTypeDef(_DescribeSnapshotsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Contains the results of the  DescribeSnapshots operation.
      - **Snapshots** *(list) --*

        The list of  Snapshot objects that were retrieved.
        It is possible that this list contains less than the number of items specified in the
        *Limit* member of the request. This occurs if there are less than the requested number of
        items left to retrieve, or if the limitations of the operation have been exceeded.
        - *(dict) --*

          Describes a directory snapshot.
          - **DirectoryId** *(string) --*

            The directory identifier.
    """


_DescribeTrustsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeTrustsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeTrustsPaginatePaginationConfigTypeDef(_DescribeTrustsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeTrustsPaginateResponseTrustsTypeDef = TypedDict(
    "_DescribeTrustsPaginateResponseTrustsTypeDef",
    {
        "DirectoryId": str,
        "TrustId": str,
        "RemoteDomainName": str,
        "TrustType": Literal["Forest", "External"],
        "TrustDirection": Literal["One-Way: Outgoing", "One-Way: Incoming", "Two-Way"],
        "TrustState": Literal[
            "Creating",
            "Created",
            "Verifying",
            "VerifyFailed",
            "Verified",
            "Updating",
            "UpdateFailed",
            "Updated",
            "Deleting",
            "Deleted",
            "Failed",
        ],
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
        "StateLastUpdatedDateTime": datetime,
        "TrustStateReason": str,
        "SelectiveAuth": Literal["Enabled", "Disabled"],
    },
    total=False,
)


class DescribeTrustsPaginateResponseTrustsTypeDef(_DescribeTrustsPaginateResponseTrustsTypeDef):
    """
    - *(dict) --*

      Describes a trust relationship between an AWS Managed Microsoft AD directory and an external
      domain.
      - **DirectoryId** *(string) --*

        The Directory ID of the AWS directory involved in the trust relationship.
    """


_DescribeTrustsPaginateResponseTypeDef = TypedDict(
    "_DescribeTrustsPaginateResponseTypeDef",
    {"Trusts": List[DescribeTrustsPaginateResponseTrustsTypeDef]},
    total=False,
)


class DescribeTrustsPaginateResponseTypeDef(_DescribeTrustsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The result of a DescribeTrust request.
      - **Trusts** *(list) --*

        The list of Trust objects that were retrieved.
        It is possible that this list contains less than the number of items specified in the
        *Limit* member of the request. This occurs if there are less than the requested number of
        items left to retrieve, or if the limitations of the operation have been exceeded.
        - *(dict) --*

          Describes a trust relationship between an AWS Managed Microsoft AD directory and an
          external domain.
          - **DirectoryId** *(string) --*

            The Directory ID of the AWS directory involved in the trust relationship.
    """


_ListIpRoutesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIpRoutesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIpRoutesPaginatePaginationConfigTypeDef(_ListIpRoutesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListIpRoutesPaginateResponseIpRoutesInfoTypeDef = TypedDict(
    "_ListIpRoutesPaginateResponseIpRoutesInfoTypeDef",
    {
        "DirectoryId": str,
        "CidrIp": str,
        "IpRouteStatusMsg": Literal[
            "Adding", "Added", "Removing", "Removed", "AddFailed", "RemoveFailed"
        ],
        "AddedDateTime": datetime,
        "IpRouteStatusReason": str,
        "Description": str,
    },
    total=False,
)


class ListIpRoutesPaginateResponseIpRoutesInfoTypeDef(
    _ListIpRoutesPaginateResponseIpRoutesInfoTypeDef
):
    """
    - *(dict) --*

      Information about one or more IP address blocks.
      - **DirectoryId** *(string) --*

        Identifier (ID) of the directory associated with the IP addresses.
    """


_ListIpRoutesPaginateResponseTypeDef = TypedDict(
    "_ListIpRoutesPaginateResponseTypeDef",
    {"IpRoutesInfo": List[ListIpRoutesPaginateResponseIpRoutesInfoTypeDef]},
    total=False,
)


class ListIpRoutesPaginateResponseTypeDef(_ListIpRoutesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **IpRoutesInfo** *(list) --*

        A list of  IpRoute s.
        - *(dict) --*

          Information about one or more IP address blocks.
          - **DirectoryId** *(string) --*

            Identifier (ID) of the directory associated with the IP addresses.
    """


_ListLogSubscriptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLogSubscriptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLogSubscriptionsPaginatePaginationConfigTypeDef(
    _ListLogSubscriptionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef = TypedDict(
    "_ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef",
    {"DirectoryId": str, "LogGroupName": str, "SubscriptionCreatedDateTime": datetime},
    total=False,
)


class ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef(
    _ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef
):
    """
    - *(dict) --*

      Represents a log subscription, which tracks real-time data from a chosen log group to a
      specified destination.
      - **DirectoryId** *(string) --*

        Identifier (ID) of the directory that you want to associate with the log subscription.
    """


_ListLogSubscriptionsPaginateResponseTypeDef = TypedDict(
    "_ListLogSubscriptionsPaginateResponseTypeDef",
    {"LogSubscriptions": List[ListLogSubscriptionsPaginateResponseLogSubscriptionsTypeDef]},
    total=False,
)


class ListLogSubscriptionsPaginateResponseTypeDef(_ListLogSubscriptionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **LogSubscriptions** *(list) --*

        A list of active  LogSubscription objects for calling the AWS account.
        - *(dict) --*

          Represents a log subscription, which tracks real-time data from a chosen log group to a
          specified destination.
          - **DirectoryId** *(string) --*

            Identifier (ID) of the directory that you want to associate with the log subscription.
    """


_ListSchemaExtensionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSchemaExtensionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSchemaExtensionsPaginatePaginationConfigTypeDef(
    _ListSchemaExtensionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef = TypedDict(
    "_ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
        "Description": str,
        "SchemaExtensionStatus": Literal[
            "Initializing",
            "CreatingSnapshot",
            "UpdatingSchema",
            "Replicating",
            "CancelInProgress",
            "RollbackInProgress",
            "Cancelled",
            "Failed",
            "Completed",
        ],
        "SchemaExtensionStatusReason": str,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)


class ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef(
    _ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef
):
    """
    - *(dict) --*

      Information about a schema extension.
      - **DirectoryId** *(string) --*

        The identifier of the directory to which the schema extension is applied.
    """


_ListSchemaExtensionsPaginateResponseTypeDef = TypedDict(
    "_ListSchemaExtensionsPaginateResponseTypeDef",
    {"SchemaExtensionsInfo": List[ListSchemaExtensionsPaginateResponseSchemaExtensionsInfoTypeDef]},
    total=False,
)


class ListSchemaExtensionsPaginateResponseTypeDef(_ListSchemaExtensionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **SchemaExtensionsInfo** *(list) --*

        Information about the schema extensions applied to the directory.
        - *(dict) --*

          Information about a schema extension.
          - **DirectoryId** *(string) --*

            The identifier of the directory to which the schema extension is applied.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    - *(dict) --*

      Metadata assigned to a directory consisting of a key-value pair.
      - **Key** *(string) --*

        Required name of the tag. The string value can be Unicode characters and cannot be prefixed
        with "aws:". The string can contain only the set of Unicode letters, digits, white-space,
        '_', '.', '/', '=', '+', '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(_ListTagsForResourcePaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        List of tags returned by the ListTagsForResource operation.
        - *(dict) --*

          Metadata assigned to a directory consisting of a key-value pair.
          - **Key** *(string) --*

            Required name of the tag. The string value can be Unicode characters and cannot be
            prefixed with "aws:". The string can contain only the set of Unicode letters, digits,
            white-space, '_', '.', '/', '=', '+', '-' (Java regex:
            "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").
    """
