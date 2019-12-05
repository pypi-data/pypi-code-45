"Main interface for acm-pca service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


AuditReportCreatedWaitWaiterConfigTypeDef = TypedDict(
    "AuditReportCreatedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef = TypedDict(
    "CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)

CertificateIssuedWaitWaiterConfigTypeDef = TypedDict(
    "CertificateIssuedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)

ClientCreateCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "ClientCreateCertificateAuthorityAuditReportResponseTypeDef",
    {"AuditReportId": str, "S3Key": str},
    total=False,
)

ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
    },
    total=False,
)

_RequiredClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef",
    {"KeyAlgorithm": Literal["RSA_2048", "RSA_4096", "EC_prime256v1", "EC_secp384r1"]},
)
_OptionalClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef",
    {
        "SigningAlgorithm": Literal[
            "SHA256WITHECDSA",
            "SHA384WITHECDSA",
            "SHA512WITHECDSA",
            "SHA256WITHRSA",
            "SHA384WITHRSA",
            "SHA512WITHRSA",
        ],
        "Subject": ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef,
    },
    total=False,
)


class ClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef(
    _RequiredClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef,
    _OptionalClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef,
):
    pass


ClientCreateCertificateAuthorityResponseTypeDef = TypedDict(
    "ClientCreateCertificateAuthorityResponseTypeDef", {"CertificateAuthorityArn": str}, total=False
)

_RequiredClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool},
)
_OptionalClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class ClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef(
    _RequiredClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef,
    _OptionalClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef,
):
    pass


ClientCreateCertificateAuthorityRevocationConfigurationTypeDef = TypedDict(
    "ClientCreateCertificateAuthorityRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)

_RequiredClientCreateCertificateAuthorityTagsTypeDef = TypedDict(
    "_RequiredClientCreateCertificateAuthorityTagsTypeDef", {"Key": str}
)
_OptionalClientCreateCertificateAuthorityTagsTypeDef = TypedDict(
    "_OptionalClientCreateCertificateAuthorityTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateCertificateAuthorityTagsTypeDef(
    _RequiredClientCreateCertificateAuthorityTagsTypeDef,
    _OptionalClientCreateCertificateAuthorityTagsTypeDef,
):
    pass


ClientDescribeCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "ClientDescribeCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportStatus": Literal["CREATING", "SUCCESS", "FAILED"],
        "S3BucketName": str,
        "S3Key": str,
        "CreatedAt": datetime,
    },
    total=False,
)

ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
    },
    total=False,
)

ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef = TypedDict(
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": Literal["RSA_2048", "RSA_4096", "EC_prime256v1", "EC_secp384r1"],
        "SigningAlgorithm": Literal[
            "SHA256WITHECDSA",
            "SHA384WITHECDSA",
            "SHA512WITHECDSA",
            "SHA256WITHRSA",
            "SHA384WITHRSA",
            "SHA512WITHRSA",
        ],
        "Subject": ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef,
    },
    total=False,
)

ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool, "ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)

ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef = TypedDict(
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)

ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef = TypedDict(
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "LastStateChangeAt": datetime,
        "Type": Literal["ROOT", "SUBORDINATE"],
        "Serial": str,
        "Status": Literal[
            "CREATING", "PENDING_CERTIFICATE", "ACTIVE", "DELETED", "DISABLED", "EXPIRED", "FAILED"
        ],
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": Literal["REQUEST_TIMED_OUT", "UNSUPPORTED_ALGORITHM", "OTHER"],
        "CertificateAuthorityConfiguration": ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef,
        "RevocationConfiguration": ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef,
        "RestorableUntil": datetime,
    },
    total=False,
)

ClientDescribeCertificateAuthorityResponseTypeDef = TypedDict(
    "ClientDescribeCertificateAuthorityResponseTypeDef",
    {"CertificateAuthority": ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef},
    total=False,
)

ClientGetCertificateAuthorityCertificateResponseTypeDef = TypedDict(
    "ClientGetCertificateAuthorityCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str},
    total=False,
)

ClientGetCertificateAuthorityCsrResponseTypeDef = TypedDict(
    "ClientGetCertificateAuthorityCsrResponseTypeDef", {"Csr": str}, total=False
)

ClientGetCertificateResponseTypeDef = TypedDict(
    "ClientGetCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str},
    total=False,
)

ClientIssueCertificateResponseTypeDef = TypedDict(
    "ClientIssueCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)

_RequiredClientIssueCertificateValidityTypeDef = TypedDict(
    "_RequiredClientIssueCertificateValidityTypeDef", {"Value": int}
)
_OptionalClientIssueCertificateValidityTypeDef = TypedDict(
    "_OptionalClientIssueCertificateValidityTypeDef",
    {"Type": Literal["END_DATE", "ABSOLUTE", "DAYS", "MONTHS", "YEARS"]},
    total=False,
)


class ClientIssueCertificateValidityTypeDef(
    _RequiredClientIssueCertificateValidityTypeDef, _OptionalClientIssueCertificateValidityTypeDef
):
    pass


ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
    },
    total=False,
)

ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef = TypedDict(
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": Literal["RSA_2048", "RSA_4096", "EC_prime256v1", "EC_secp384r1"],
        "SigningAlgorithm": Literal[
            "SHA256WITHECDSA",
            "SHA384WITHECDSA",
            "SHA512WITHECDSA",
            "SHA256WITHRSA",
            "SHA384WITHRSA",
            "SHA512WITHRSA",
        ],
        "Subject": ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef,
    },
    total=False,
)

ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool, "ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)

ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef = TypedDict(
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)

ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef = TypedDict(
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "LastStateChangeAt": datetime,
        "Type": Literal["ROOT", "SUBORDINATE"],
        "Serial": str,
        "Status": Literal[
            "CREATING", "PENDING_CERTIFICATE", "ACTIVE", "DELETED", "DISABLED", "EXPIRED", "FAILED"
        ],
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": Literal["REQUEST_TIMED_OUT", "UNSUPPORTED_ALGORITHM", "OTHER"],
        "CertificateAuthorityConfiguration": ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef,
        "RevocationConfiguration": ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef,
        "RestorableUntil": datetime,
    },
    total=False,
)

ClientListCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ClientListCertificateAuthoritiesResponseTypeDef",
    {
        "CertificateAuthorities": List[
            ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListPermissionsResponsePermissionsTypeDef = TypedDict(
    "ClientListPermissionsResponsePermissionsTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CreatedAt": datetime,
        "Principal": str,
        "SourceAccount": str,
        "Actions": List[Literal["IssueCertificate", "GetCertificate", "ListPermissions"]],
        "Policy": str,
    },
    total=False,
)

ClientListPermissionsResponseTypeDef = TypedDict(
    "ClientListPermissionsResponseTypeDef",
    {"Permissions": List[ClientListPermissionsResponsePermissionsTypeDef], "NextToken": str},
    total=False,
)

ClientListTagsResponseTagsTypeDef = TypedDict(
    "ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)

_RequiredClientTagCertificateAuthorityTagsTypeDef = TypedDict(
    "_RequiredClientTagCertificateAuthorityTagsTypeDef", {"Key": str}
)
_OptionalClientTagCertificateAuthorityTagsTypeDef = TypedDict(
    "_OptionalClientTagCertificateAuthorityTagsTypeDef", {"Value": str}, total=False
)


class ClientTagCertificateAuthorityTagsTypeDef(
    _RequiredClientTagCertificateAuthorityTagsTypeDef,
    _OptionalClientTagCertificateAuthorityTagsTypeDef,
):
    pass


_RequiredClientUntagCertificateAuthorityTagsTypeDef = TypedDict(
    "_RequiredClientUntagCertificateAuthorityTagsTypeDef", {"Key": str}
)
_OptionalClientUntagCertificateAuthorityTagsTypeDef = TypedDict(
    "_OptionalClientUntagCertificateAuthorityTagsTypeDef", {"Value": str}, total=False
)


class ClientUntagCertificateAuthorityTagsTypeDef(
    _RequiredClientUntagCertificateAuthorityTagsTypeDef,
    _OptionalClientUntagCertificateAuthorityTagsTypeDef,
):
    pass


_RequiredClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool},
)
_OptionalClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class ClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef(
    _RequiredClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef,
    _OptionalClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef,
):
    pass


ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef = TypedDict(
    "ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)

ListCertificateAuthoritiesPaginatePaginationConfigTypeDef = TypedDict(
    "ListCertificateAuthoritiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
    },
    total=False,
)

ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef = TypedDict(
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": Literal["RSA_2048", "RSA_4096", "EC_prime256v1", "EC_secp384r1"],
        "SigningAlgorithm": Literal[
            "SHA256WITHECDSA",
            "SHA384WITHECDSA",
            "SHA512WITHECDSA",
            "SHA256WITHRSA",
            "SHA384WITHRSA",
            "SHA512WITHRSA",
        ],
        "Subject": ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef,
    },
    total=False,
)

ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool, "ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)

ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef = TypedDict(
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)

ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef = TypedDict(
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "LastStateChangeAt": datetime,
        "Type": Literal["ROOT", "SUBORDINATE"],
        "Serial": str,
        "Status": Literal[
            "CREATING", "PENDING_CERTIFICATE", "ACTIVE", "DELETED", "DISABLED", "EXPIRED", "FAILED"
        ],
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": Literal["REQUEST_TIMED_OUT", "UNSUPPORTED_ALGORITHM", "OTHER"],
        "CertificateAuthorityConfiguration": ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef,
        "RevocationConfiguration": ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef,
        "RestorableUntil": datetime,
    },
    total=False,
)

ListCertificateAuthoritiesPaginateResponseTypeDef = TypedDict(
    "ListCertificateAuthoritiesPaginateResponseTypeDef",
    {
        "CertificateAuthorities": List[
            ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef
        ]
    },
    total=False,
)

ListPermissionsPaginatePaginationConfigTypeDef = TypedDict(
    "ListPermissionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListPermissionsPaginateResponsePermissionsTypeDef = TypedDict(
    "ListPermissionsPaginateResponsePermissionsTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CreatedAt": datetime,
        "Principal": str,
        "SourceAccount": str,
        "Actions": List[Literal["IssueCertificate", "GetCertificate", "ListPermissions"]],
        "Policy": str,
    },
    total=False,
)

ListPermissionsPaginateResponseTypeDef = TypedDict(
    "ListPermissionsPaginateResponseTypeDef",
    {"Permissions": List[ListPermissionsPaginateResponsePermissionsTypeDef]},
    total=False,
)

ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)

ListTagsPaginateResponseTagsTypeDef = TypedDict(
    "ListTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)

ListTagsPaginateResponseTypeDef = TypedDict(
    "ListTagsPaginateResponseTypeDef",
    {"Tags": List[ListTagsPaginateResponseTagsTypeDef]},
    total=False,
)
