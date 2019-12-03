"Main interface for acm-pca service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "AuditReportCreatedWaitWaiterConfigTypeDef",
    "CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef",
    "CertificateIssuedWaitWaiterConfigTypeDef",
    "ClientCreateCertificateAuthorityAuditReportResponseTypeDef",
    "ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef",
    "ClientCreateCertificateAuthorityCertificateAuthorityConfigurationTypeDef",
    "ClientCreateCertificateAuthorityResponseTypeDef",
    "ClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    "ClientCreateCertificateAuthorityRevocationConfigurationTypeDef",
    "ClientCreateCertificateAuthorityTagsTypeDef",
    "ClientDescribeCertificateAuthorityAuditReportResponseTypeDef",
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef",
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef",
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef",
    "ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef",
    "ClientDescribeCertificateAuthorityResponseTypeDef",
    "ClientGetCertificateAuthorityCertificateResponseTypeDef",
    "ClientGetCertificateAuthorityCsrResponseTypeDef",
    "ClientGetCertificateResponseTypeDef",
    "ClientIssueCertificateResponseTypeDef",
    "ClientIssueCertificateValidityTypeDef",
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef",
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef",
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef",
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef",
    "ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef",
    "ClientListCertificateAuthoritiesResponseTypeDef",
    "ClientListPermissionsResponsePermissionsTypeDef",
    "ClientListPermissionsResponseTypeDef",
    "ClientListTagsResponseTagsTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientTagCertificateAuthorityTagsTypeDef",
    "ClientUntagCertificateAuthorityTagsTypeDef",
    "ClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    "ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef",
    "ListCertificateAuthoritiesPaginatePaginationConfigTypeDef",
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef",
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef",
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef",
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef",
    "ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef",
    "ListCertificateAuthoritiesPaginateResponseTypeDef",
    "ListPermissionsPaginatePaginationConfigTypeDef",
    "ListPermissionsPaginateResponsePermissionsTypeDef",
    "ListPermissionsPaginateResponseTypeDef",
    "ListTagsPaginatePaginationConfigTypeDef",
    "ListTagsPaginateResponseTagsTypeDef",
    "ListTagsPaginateResponseTypeDef",
)


_AuditReportCreatedWaitWaiterConfigTypeDef = TypedDict(
    "_AuditReportCreatedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class AuditReportCreatedWaitWaiterConfigTypeDef(_AuditReportCreatedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3
    """


_CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef = TypedDict(
    "_CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef(
    _CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef
):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3
    """


_CertificateIssuedWaitWaiterConfigTypeDef = TypedDict(
    "_CertificateIssuedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class CertificateIssuedWaitWaiterConfigTypeDef(_CertificateIssuedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3
    """


_ClientCreateCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "_ClientCreateCertificateAuthorityAuditReportResponseTypeDef",
    {"AuditReportId": str, "S3Key": str},
    total=False,
)


class ClientCreateCertificateAuthorityAuditReportResponseTypeDef(
    _ClientCreateCertificateAuthorityAuditReportResponseTypeDef
):
    """
    - *(dict) --*

      - **AuditReportId** *(string) --*

        An alphanumeric string that contains a report identifier.
    """


_ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "_ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef",
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


class ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef(
    _ClientCreateCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef
):
    pass


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
    """
    Name and bit size of the private key algorithm, the name of the signing algorithm, and X.500
    certificate subject information.
    - **KeyAlgorithm** *(string) --***[REQUIRED]**

      Type of the public key algorithm and size, in bits, of the key pair that your CA creates when
      it issues a certificate. When you create a subordinate CA, you must use a key algorithm
      supported by the parent CA.
    """


_ClientCreateCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientCreateCertificateAuthorityResponseTypeDef",
    {"CertificateAuthorityArn": str},
    total=False,
)


class ClientCreateCertificateAuthorityResponseTypeDef(
    _ClientCreateCertificateAuthorityResponseTypeDef
):
    """
    - *(dict) --*

      - **CertificateAuthorityArn** *(string) --*

        If successful, the Amazon Resource Name (ARN) of the certificate authority (CA). This is of
        the form:

          ``arn:aws:acm-pca:*region* :*account*
          :certificate-authority/*12345678-1234-1234-1234-123456789012* `` .
    """


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
    """
    - **CrlConfiguration** *(dict) --*

      Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.
      - **Enabled** *(boolean) --***[REQUIRED]**

        Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You
        can use this value to enable certificate revocation for a new CA when you call the
        CreateCertificateAuthority action or for an existing CA when you call the
        UpdateCertificateAuthority action.
    """


_ClientCreateCertificateAuthorityRevocationConfigurationTypeDef = TypedDict(
    "_ClientCreateCertificateAuthorityRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientCreateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)


class ClientCreateCertificateAuthorityRevocationConfigurationTypeDef(
    _ClientCreateCertificateAuthorityRevocationConfigurationTypeDef
):
    """
    Contains a Boolean value that you can use to enable a certification revocation list (CRL) for
    the CA, the name of the S3 bucket to which ACM Private CA will write the CRL, and an optional
    CNAME alias that you can use to hide the name of your bucket in the **CRL Distribution Points**
    extension of your CA certificate. For more information, see the  CrlConfiguration structure.
    - **CrlConfiguration** *(dict) --*

      Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.
      - **Enabled** *(boolean) --***[REQUIRED]**

        Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You
        can use this value to enable certificate revocation for a new CA when you call the
        CreateCertificateAuthority action or for an existing CA when you call the
        UpdateCertificateAuthority action.
    """


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
    """
    - *(dict) --*

      Tags are labels that you can use to identify and organize your private CAs. Each tag consists
      of a key and an optional value. You can associate up to 50 tags with a private CA. To add one
      or more tags to a private CA, call the  TagCertificateAuthority action. To remove a tag, call
      the  UntagCertificateAuthority action.
      - **Key** *(string) --***[REQUIRED]**

        Key (name) of the tag.
    """


_ClientDescribeCertificateAuthorityAuditReportResponseTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityAuditReportResponseTypeDef",
    {
        "AuditReportStatus": Literal["CREATING", "SUCCESS", "FAILED"],
        "S3BucketName": str,
        "S3Key": str,
        "CreatedAt": datetime,
    },
    total=False,
)


class ClientDescribeCertificateAuthorityAuditReportResponseTypeDef(
    _ClientDescribeCertificateAuthorityAuditReportResponseTypeDef
):
    """
    - *(dict) --*

      - **AuditReportStatus** *(string) --*

        Specifies whether report creation is in progress, has succeeded, or has failed.
    """


_ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef",
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


class ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef(
    _ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationSubjectTypeDef
):
    pass


_ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef",
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


class ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef(
    _ClientDescribeCertificateAuthorityResponseCertificateAuthorityCertificateAuthorityConfigurationTypeDef
):
    pass


_ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool, "ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef(
    _ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
):
    pass


_ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)


class ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef(
    _ClientDescribeCertificateAuthorityResponseCertificateAuthorityRevocationConfigurationTypeDef
):
    pass


_ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef",
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


class ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef(
    _ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef
):
    """
    - **CertificateAuthority** *(dict) --*

      A  CertificateAuthority structure that contains information about your private CA.
      - **Arn** *(string) --*

        Amazon Resource Name (ARN) for your private certificate authority (CA). The format is ``
        *12345678-1234-1234-1234-123456789012* `` .
    """


_ClientDescribeCertificateAuthorityResponseTypeDef = TypedDict(
    "_ClientDescribeCertificateAuthorityResponseTypeDef",
    {"CertificateAuthority": ClientDescribeCertificateAuthorityResponseCertificateAuthorityTypeDef},
    total=False,
)


class ClientDescribeCertificateAuthorityResponseTypeDef(
    _ClientDescribeCertificateAuthorityResponseTypeDef
):
    """
    - *(dict) --*

      - **CertificateAuthority** *(dict) --*

        A  CertificateAuthority structure that contains information about your private CA.
        - **Arn** *(string) --*

          Amazon Resource Name (ARN) for your private certificate authority (CA). The format is ``
          *12345678-1234-1234-1234-123456789012* `` .
    """


_ClientGetCertificateAuthorityCertificateResponseTypeDef = TypedDict(
    "_ClientGetCertificateAuthorityCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str},
    total=False,
)


class ClientGetCertificateAuthorityCertificateResponseTypeDef(
    _ClientGetCertificateAuthorityCertificateResponseTypeDef
):
    """
    - *(dict) --*

      - **Certificate** *(string) --*

        Base64-encoded certificate authority (CA) certificate.
    """


_ClientGetCertificateAuthorityCsrResponseTypeDef = TypedDict(
    "_ClientGetCertificateAuthorityCsrResponseTypeDef", {"Csr": str}, total=False
)


class ClientGetCertificateAuthorityCsrResponseTypeDef(
    _ClientGetCertificateAuthorityCsrResponseTypeDef
):
    """
    - *(dict) --*

      - **Csr** *(string) --*

        The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.
    """


_ClientGetCertificateResponseTypeDef = TypedDict(
    "_ClientGetCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str},
    total=False,
)


class ClientGetCertificateResponseTypeDef(_ClientGetCertificateResponseTypeDef):
    """
    - *(dict) --*

      - **Certificate** *(string) --*

        The base64 PEM-encoded certificate specified by the ``CertificateArn`` parameter.
    """


_ClientIssueCertificateResponseTypeDef = TypedDict(
    "_ClientIssueCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)


class ClientIssueCertificateResponseTypeDef(_ClientIssueCertificateResponseTypeDef):
    """
    - *(dict) --*

      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the issued certificate and the certificate serial number.
        This is of the form:

          ``arn:aws:acm-pca:*region* :*account*
          :certificate-authority/*12345678-1234-1234-1234-123456789012*
          /certificate/*286535153982981100925020015808220737245* ``
    """


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
    """
    The type of the validity period.
    - **Value** *(integer) --***[REQUIRED]**

      Time period.
    """


_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef",
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


class ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef(
    _ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef
):
    pass


_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef",
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


class ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef(
    _ClientListCertificateAuthoritiesResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef
):
    pass


_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool, "ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef(
    _ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef
):
    pass


_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)


class ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef(
    _ClientListCertificateAuthoritiesResponseCertificateAuthoritiesRevocationConfigurationTypeDef
):
    pass


_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef",
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


class ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef(
    _ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef
):
    """
    - *(dict) --*

      Contains information about your private certificate authority (CA). Your private CA can issue
      and revoke X.509 digital certificates. Digital certificates verify that the entity named in
      the certificate **Subject** field owns or controls the public key contained in the **Subject
      Public Key Info** field. Call the  CreateCertificateAuthority action to create your private
      CA. You must then call the  GetCertificateAuthorityCertificate action to retrieve a private CA
      certificate signing request (CSR). Sign the CSR with your ACM Private CA-hosted or on-premises
      root or subordinate CA certificate. Call the  ImportCertificateAuthorityCertificate action to
      import the signed certificate into AWS Certificate Manager (ACM).
      - **Arn** *(string) --*

        Amazon Resource Name (ARN) for your private certificate authority (CA). The format is ``
        *12345678-1234-1234-1234-123456789012* `` .
    """


_ClientListCertificateAuthoritiesResponseTypeDef = TypedDict(
    "_ClientListCertificateAuthoritiesResponseTypeDef",
    {
        "CertificateAuthorities": List[
            ClientListCertificateAuthoritiesResponseCertificateAuthoritiesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListCertificateAuthoritiesResponseTypeDef(
    _ClientListCertificateAuthoritiesResponseTypeDef
):
    """
    - *(dict) --*

      - **CertificateAuthorities** *(list) --*

        Summary information about each certificate authority you have created.
        - *(dict) --*

          Contains information about your private certificate authority (CA). Your private CA can
          issue and revoke X.509 digital certificates. Digital certificates verify that the entity
          named in the certificate **Subject** field owns or controls the public key contained in
          the **Subject Public Key Info** field. Call the  CreateCertificateAuthority action to
          create your private CA. You must then call the  GetCertificateAuthorityCertificate action
          to retrieve a private CA certificate signing request (CSR). Sign the CSR with your ACM
          Private CA-hosted or on-premises root or subordinate CA certificate. Call the
          ImportCertificateAuthorityCertificate action to import the signed certificate into AWS
          Certificate Manager (ACM).
          - **Arn** *(string) --*

            Amazon Resource Name (ARN) for your private certificate authority (CA). The format is ``
            *12345678-1234-1234-1234-123456789012* `` .
    """


_ClientListPermissionsResponsePermissionsTypeDef = TypedDict(
    "_ClientListPermissionsResponsePermissionsTypeDef",
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


class ClientListPermissionsResponsePermissionsTypeDef(
    _ClientListPermissionsResponsePermissionsTypeDef
):
    """
    - *(dict) --*

      Permissions designate which private CA actions can be performed by an AWS service or entity.
      In order for ACM to automatically renew private certificates, you must give the ACM service
      principal all available permissions (``IssueCertificate`` , ``GetCertificate`` , and
      ``ListPermissions`` ). Permissions can be assigned with the  CreatePermission action, removed
      with the  DeletePermission action, and listed with the  ListPermissions action.
      - **CertificateAuthorityArn** *(string) --*

        The Amazon Resource Number (ARN) of the private CA from which the permission was issued.
    """


_ClientListPermissionsResponseTypeDef = TypedDict(
    "_ClientListPermissionsResponseTypeDef",
    {"Permissions": List[ClientListPermissionsResponsePermissionsTypeDef], "NextToken": str},
    total=False,
)


class ClientListPermissionsResponseTypeDef(_ClientListPermissionsResponseTypeDef):
    """
    - *(dict) --*

      - **Permissions** *(list) --*

        Summary information about each permission assigned by the specified private CA, including
        the action enabled, the policy provided, and the time of creation.
        - *(dict) --*

          Permissions designate which private CA actions can be performed by an AWS service or
          entity. In order for ACM to automatically renew private certificates, you must give the
          ACM service principal all available permissions (``IssueCertificate`` , ``GetCertificate``
          , and ``ListPermissions`` ). Permissions can be assigned with the  CreatePermission
          action, removed with the  DeletePermission action, and listed with the  ListPermissions
          action.
          - **CertificateAuthorityArn** *(string) --*

            The Amazon Resource Number (ARN) of the private CA from which the permission was issued.
    """


_ClientListTagsResponseTagsTypeDef = TypedDict(
    "_ClientListTagsResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagsTypeDef(_ClientListTagsResponseTagsTypeDef):
    """
    - *(dict) --*

      Tags are labels that you can use to identify and organize your private CAs. Each tag consists
      of a key and an optional value. You can associate up to 50 tags with a private CA. To add one
      or more tags to a private CA, call the  TagCertificateAuthority action. To remove a tag, call
      the  UntagCertificateAuthority action.
      - **Key** *(string) --*

        Key (name) of the tag.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"Tags": List[ClientListTagsResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The tags associated with your private CA.
        - *(dict) --*

          Tags are labels that you can use to identify and organize your private CAs. Each tag
          consists of a key and an optional value. You can associate up to 50 tags with a private
          CA. To add one or more tags to a private CA, call the  TagCertificateAuthority action. To
          remove a tag, call the  UntagCertificateAuthority action.
          - **Key** *(string) --*

            Key (name) of the tag.
    """


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
    """
    - *(dict) --*

      Tags are labels that you can use to identify and organize your private CAs. Each tag consists
      of a key and an optional value. You can associate up to 50 tags with a private CA. To add one
      or more tags to a private CA, call the  TagCertificateAuthority action. To remove a tag, call
      the  UntagCertificateAuthority action.
      - **Key** *(string) --***[REQUIRED]**

        Key (name) of the tag.
    """


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
    """
    - *(dict) --*

      Tags are labels that you can use to identify and organize your private CAs. Each tag consists
      of a key and an optional value. You can associate up to 50 tags with a private CA. To add one
      or more tags to a private CA, call the  TagCertificateAuthority action. To remove a tag, call
      the  UntagCertificateAuthority action.
      - **Key** *(string) --***[REQUIRED]**

        Key (name) of the tag.
    """


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
    """
    - **CrlConfiguration** *(dict) --*

      Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.
      - **Enabled** *(boolean) --***[REQUIRED]**

        Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You
        can use this value to enable certificate revocation for a new CA when you call the
        CreateCertificateAuthority action or for an existing CA when you call the
        UpdateCertificateAuthority action.
    """


_ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef = TypedDict(
    "_ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ClientUpdateCertificateAuthorityRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)


class ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef(
    _ClientUpdateCertificateAuthorityRevocationConfigurationTypeDef
):
    """
    Revocation information for your private CA.
    - **CrlConfiguration** *(dict) --*

      Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.
      - **Enabled** *(boolean) --***[REQUIRED]**

        Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You
        can use this value to enable certificate revocation for a new CA when you call the
        CreateCertificateAuthority action or for an existing CA when you call the
        UpdateCertificateAuthority action.
    """


_ListCertificateAuthoritiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCertificateAuthoritiesPaginatePaginationConfigTypeDef(
    _ListCertificateAuthoritiesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef",
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


class ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef(
    _ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationSubjectTypeDef
):
    pass


_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef",
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


class ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef(
    _ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesCertificateAuthorityConfigurationTypeDef
):
    pass


_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef",
    {"Enabled": bool, "ExpirationInDays": int, "CustomCname": str, "S3BucketName": str},
    total=False,
)


class ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef(
    _ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef
):
    pass


_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef",
    {
        "CrlConfiguration": ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationCrlConfigurationTypeDef
    },
    total=False,
)


class ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef(
    _ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesRevocationConfigurationTypeDef
):
    pass


_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef",
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


class ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef(
    _ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef
):
    """
    - *(dict) --*

      Contains information about your private certificate authority (CA). Your private CA can issue
      and revoke X.509 digital certificates. Digital certificates verify that the entity named in
      the certificate **Subject** field owns or controls the public key contained in the **Subject
      Public Key Info** field. Call the  CreateCertificateAuthority action to create your private
      CA. You must then call the  GetCertificateAuthorityCertificate action to retrieve a private CA
      certificate signing request (CSR). Sign the CSR with your ACM Private CA-hosted or on-premises
      root or subordinate CA certificate. Call the  ImportCertificateAuthorityCertificate action to
      import the signed certificate into AWS Certificate Manager (ACM).
      - **Arn** *(string) --*

        Amazon Resource Name (ARN) for your private certificate authority (CA). The format is ``
        *12345678-1234-1234-1234-123456789012* `` .
    """


_ListCertificateAuthoritiesPaginateResponseTypeDef = TypedDict(
    "_ListCertificateAuthoritiesPaginateResponseTypeDef",
    {
        "CertificateAuthorities": List[
            ListCertificateAuthoritiesPaginateResponseCertificateAuthoritiesTypeDef
        ]
    },
    total=False,
)


class ListCertificateAuthoritiesPaginateResponseTypeDef(
    _ListCertificateAuthoritiesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      - **CertificateAuthorities** *(list) --*

        Summary information about each certificate authority you have created.
        - *(dict) --*

          Contains information about your private certificate authority (CA). Your private CA can
          issue and revoke X.509 digital certificates. Digital certificates verify that the entity
          named in the certificate **Subject** field owns or controls the public key contained in
          the **Subject Public Key Info** field. Call the  CreateCertificateAuthority action to
          create your private CA. You must then call the  GetCertificateAuthorityCertificate action
          to retrieve a private CA certificate signing request (CSR). Sign the CSR with your ACM
          Private CA-hosted or on-premises root or subordinate CA certificate. Call the
          ImportCertificateAuthorityCertificate action to import the signed certificate into AWS
          Certificate Manager (ACM).
          - **Arn** *(string) --*

            Amazon Resource Name (ARN) for your private certificate authority (CA). The format is ``
            *12345678-1234-1234-1234-123456789012* `` .
    """


_ListPermissionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPermissionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPermissionsPaginatePaginationConfigTypeDef(
    _ListPermissionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListPermissionsPaginateResponsePermissionsTypeDef = TypedDict(
    "_ListPermissionsPaginateResponsePermissionsTypeDef",
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


class ListPermissionsPaginateResponsePermissionsTypeDef(
    _ListPermissionsPaginateResponsePermissionsTypeDef
):
    """
    - *(dict) --*

      Permissions designate which private CA actions can be performed by an AWS service or entity.
      In order for ACM to automatically renew private certificates, you must give the ACM service
      principal all available permissions (``IssueCertificate`` , ``GetCertificate`` , and
      ``ListPermissions`` ). Permissions can be assigned with the  CreatePermission action, removed
      with the  DeletePermission action, and listed with the  ListPermissions action.
      - **CertificateAuthorityArn** *(string) --*

        The Amazon Resource Number (ARN) of the private CA from which the permission was issued.
    """


_ListPermissionsPaginateResponseTypeDef = TypedDict(
    "_ListPermissionsPaginateResponseTypeDef",
    {"Permissions": List[ListPermissionsPaginateResponsePermissionsTypeDef]},
    total=False,
)


class ListPermissionsPaginateResponseTypeDef(_ListPermissionsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Permissions** *(list) --*

        Summary information about each permission assigned by the specified private CA, including
        the action enabled, the policy provided, and the time of creation.
        - *(dict) --*

          Permissions designate which private CA actions can be performed by an AWS service or
          entity. In order for ACM to automatically renew private certificates, you must give the
          ACM service principal all available permissions (``IssueCertificate`` , ``GetCertificate``
          , and ``ListPermissions`` ). Permissions can be assigned with the  CreatePermission
          action, removed with the  DeletePermission action, and listed with the  ListPermissions
          action.
          - **CertificateAuthorityArn** *(string) --*

            The Amazon Resource Number (ARN) of the private CA from which the permission was issued.
    """


_ListTagsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsPaginatePaginationConfigTypeDef(_ListTagsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTagsPaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsPaginateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ListTagsPaginateResponseTagsTypeDef(_ListTagsPaginateResponseTagsTypeDef):
    """
    - *(dict) --*

      Tags are labels that you can use to identify and organize your private CAs. Each tag consists
      of a key and an optional value. You can associate up to 50 tags with a private CA. To add one
      or more tags to a private CA, call the  TagCertificateAuthority action. To remove a tag, call
      the  UntagCertificateAuthority action.
      - **Key** *(string) --*

        Key (name) of the tag.
    """


_ListTagsPaginateResponseTypeDef = TypedDict(
    "_ListTagsPaginateResponseTypeDef",
    {"Tags": List[ListTagsPaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsPaginateResponseTypeDef(_ListTagsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The tags associated with your private CA.
        - *(dict) --*

          Tags are labels that you can use to identify and organize your private CAs. Each tag
          consists of a key and an optional value. You can associate up to 50 tags with a private
          CA. To add one or more tags to a private CA, call the  TagCertificateAuthority action. To
          remove a tag, call the  UntagCertificateAuthority action.
          - **Key** *(string) --*

            Key (name) of the tag.
    """
