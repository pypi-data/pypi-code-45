"Main interface for acm service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "CertificateValidatedWaitWaiterConfigTypeDef",
    "ClientAddTagsToCertificateTagsTypeDef",
    "ClientDescribeCertificateResponseCertificateDomainValidationOptionsResourceRecordTypeDef",
    "ClientDescribeCertificateResponseCertificateDomainValidationOptionsTypeDef",
    "ClientDescribeCertificateResponseCertificateExtendedKeyUsagesTypeDef",
    "ClientDescribeCertificateResponseCertificateKeyUsagesTypeDef",
    "ClientDescribeCertificateResponseCertificateOptionsTypeDef",
    "ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsResourceRecordTypeDef",
    "ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsTypeDef",
    "ClientDescribeCertificateResponseCertificateRenewalSummaryTypeDef",
    "ClientDescribeCertificateResponseCertificateTypeDef",
    "ClientDescribeCertificateResponseTypeDef",
    "ClientExportCertificateResponseTypeDef",
    "ClientGetCertificateResponseTypeDef",
    "ClientImportCertificateResponseTypeDef",
    "ClientImportCertificateTagsTypeDef",
    "ClientListCertificatesIncludesTypeDef",
    "ClientListCertificatesResponseCertificateSummaryListTypeDef",
    "ClientListCertificatesResponseTypeDef",
    "ClientListTagsForCertificateResponseTagsTypeDef",
    "ClientListTagsForCertificateResponseTypeDef",
    "ClientRemoveTagsFromCertificateTagsTypeDef",
    "ClientRequestCertificateDomainValidationOptionsTypeDef",
    "ClientRequestCertificateOptionsTypeDef",
    "ClientRequestCertificateResponseTypeDef",
    "ClientRequestCertificateTagsTypeDef",
    "ClientUpdateCertificateOptionsOptionsTypeDef",
    "ListCertificatesPaginateIncludesTypeDef",
    "ListCertificatesPaginatePaginationConfigTypeDef",
    "ListCertificatesPaginateResponseCertificateSummaryListTypeDef",
    "ListCertificatesPaginateResponseTypeDef",
)


_CertificateValidatedWaitWaiterConfigTypeDef = TypedDict(
    "_CertificateValidatedWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class CertificateValidatedWaitWaiterConfigTypeDef(_CertificateValidatedWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 60
    """


_RequiredClientAddTagsToCertificateTagsTypeDef = TypedDict(
    "_RequiredClientAddTagsToCertificateTagsTypeDef", {"Key": str}
)
_OptionalClientAddTagsToCertificateTagsTypeDef = TypedDict(
    "_OptionalClientAddTagsToCertificateTagsTypeDef", {"Value": str}, total=False
)


class ClientAddTagsToCertificateTagsTypeDef(
    _RequiredClientAddTagsToCertificateTagsTypeDef, _OptionalClientAddTagsToCertificateTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair that identifies or specifies metadata about an ACM resource.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientDescribeCertificateResponseCertificateDomainValidationOptionsResourceRecordTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseCertificateDomainValidationOptionsResourceRecordTypeDef",
    {"Name": str, "Type": str, "Value": str},
    total=False,
)


class ClientDescribeCertificateResponseCertificateDomainValidationOptionsResourceRecordTypeDef(
    _ClientDescribeCertificateResponseCertificateDomainValidationOptionsResourceRecordTypeDef
):
    pass


_ClientDescribeCertificateResponseCertificateDomainValidationOptionsTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseCertificateDomainValidationOptionsTypeDef",
    {
        "DomainName": str,
        "ValidationEmails": List[str],
        "ValidationDomain": str,
        "ValidationStatus": Literal["PENDING_VALIDATION", "SUCCESS", "FAILED"],
        "ResourceRecord": ClientDescribeCertificateResponseCertificateDomainValidationOptionsResourceRecordTypeDef,
        "ValidationMethod": Literal["EMAIL", "DNS"],
    },
    total=False,
)


class ClientDescribeCertificateResponseCertificateDomainValidationOptionsTypeDef(
    _ClientDescribeCertificateResponseCertificateDomainValidationOptionsTypeDef
):
    pass


_ClientDescribeCertificateResponseCertificateExtendedKeyUsagesTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseCertificateExtendedKeyUsagesTypeDef",
    {
        "Name": Literal[
            "TLS_WEB_SERVER_AUTHENTICATION",
            "TLS_WEB_CLIENT_AUTHENTICATION",
            "CODE_SIGNING",
            "EMAIL_PROTECTION",
            "TIME_STAMPING",
            "OCSP_SIGNING",
            "IPSEC_END_SYSTEM",
            "IPSEC_TUNNEL",
            "IPSEC_USER",
            "ANY",
            "NONE",
            "CUSTOM",
        ],
        "OID": str,
    },
    total=False,
)


class ClientDescribeCertificateResponseCertificateExtendedKeyUsagesTypeDef(
    _ClientDescribeCertificateResponseCertificateExtendedKeyUsagesTypeDef
):
    pass


_ClientDescribeCertificateResponseCertificateKeyUsagesTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseCertificateKeyUsagesTypeDef",
    {
        "Name": Literal[
            "DIGITAL_SIGNATURE",
            "NON_REPUDIATION",
            "KEY_ENCIPHERMENT",
            "DATA_ENCIPHERMENT",
            "KEY_AGREEMENT",
            "CERTIFICATE_SIGNING",
            "CRL_SIGNING",
            "ENCIPHER_ONLY",
            "DECIPHER_ONLY",
            "ANY",
            "CUSTOM",
        ]
    },
    total=False,
)


class ClientDescribeCertificateResponseCertificateKeyUsagesTypeDef(
    _ClientDescribeCertificateResponseCertificateKeyUsagesTypeDef
):
    pass


_ClientDescribeCertificateResponseCertificateOptionsTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseCertificateOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientDescribeCertificateResponseCertificateOptionsTypeDef(
    _ClientDescribeCertificateResponseCertificateOptionsTypeDef
):
    pass


_ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsResourceRecordTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsResourceRecordTypeDef",
    {"Name": str, "Type": str, "Value": str},
    total=False,
)


class ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsResourceRecordTypeDef(
    _ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsResourceRecordTypeDef
):
    pass


_ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsTypeDef",
    {
        "DomainName": str,
        "ValidationEmails": List[str],
        "ValidationDomain": str,
        "ValidationStatus": Literal["PENDING_VALIDATION", "SUCCESS", "FAILED"],
        "ResourceRecord": ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsResourceRecordTypeDef,
        "ValidationMethod": Literal["EMAIL", "DNS"],
    },
    total=False,
)


class ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsTypeDef(
    _ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsTypeDef
):
    pass


_ClientDescribeCertificateResponseCertificateRenewalSummaryTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseCertificateRenewalSummaryTypeDef",
    {
        "RenewalStatus": Literal["PENDING_AUTO_RENEWAL", "PENDING_VALIDATION", "SUCCESS", "FAILED"],
        "DomainValidationOptions": List[
            ClientDescribeCertificateResponseCertificateRenewalSummaryDomainValidationOptionsTypeDef
        ],
        "RenewalStatusReason": Literal[
            "NO_AVAILABLE_CONTACTS",
            "ADDITIONAL_VERIFICATION_REQUIRED",
            "DOMAIN_NOT_ALLOWED",
            "INVALID_PUBLIC_DOMAIN",
            "DOMAIN_VALIDATION_DENIED",
            "CAA_ERROR",
            "PCA_LIMIT_EXCEEDED",
            "PCA_INVALID_ARN",
            "PCA_INVALID_STATE",
            "PCA_REQUEST_FAILED",
            "PCA_NAME_CONSTRAINTS_VALIDATION",
            "PCA_RESOURCE_NOT_FOUND",
            "PCA_INVALID_ARGS",
            "PCA_INVALID_DURATION",
            "PCA_ACCESS_DENIED",
            "OTHER",
        ],
        "UpdatedAt": datetime,
    },
    total=False,
)


class ClientDescribeCertificateResponseCertificateRenewalSummaryTypeDef(
    _ClientDescribeCertificateResponseCertificateRenewalSummaryTypeDef
):
    pass


_ClientDescribeCertificateResponseCertificateTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseCertificateTypeDef",
    {
        "CertificateArn": str,
        "DomainName": str,
        "SubjectAlternativeNames": List[str],
        "DomainValidationOptions": List[
            ClientDescribeCertificateResponseCertificateDomainValidationOptionsTypeDef
        ],
        "Serial": str,
        "Subject": str,
        "Issuer": str,
        "CreatedAt": datetime,
        "IssuedAt": datetime,
        "ImportedAt": datetime,
        "Status": Literal[
            "PENDING_VALIDATION",
            "ISSUED",
            "INACTIVE",
            "EXPIRED",
            "VALIDATION_TIMED_OUT",
            "REVOKED",
            "FAILED",
        ],
        "RevokedAt": datetime,
        "RevocationReason": Literal[
            "UNSPECIFIED",
            "KEY_COMPROMISE",
            "CA_COMPROMISE",
            "AFFILIATION_CHANGED",
            "SUPERCEDED",
            "CESSATION_OF_OPERATION",
            "CERTIFICATE_HOLD",
            "REMOVE_FROM_CRL",
            "PRIVILEGE_WITHDRAWN",
            "A_A_COMPROMISE",
        ],
        "NotBefore": datetime,
        "NotAfter": datetime,
        "KeyAlgorithm": Literal[
            "RSA_2048", "RSA_1024", "RSA_4096", "EC_prime256v1", "EC_secp384r1", "EC_secp521r1"
        ],
        "SignatureAlgorithm": str,
        "InUseBy": List[str],
        "FailureReason": Literal[
            "NO_AVAILABLE_CONTACTS",
            "ADDITIONAL_VERIFICATION_REQUIRED",
            "DOMAIN_NOT_ALLOWED",
            "INVALID_PUBLIC_DOMAIN",
            "DOMAIN_VALIDATION_DENIED",
            "CAA_ERROR",
            "PCA_LIMIT_EXCEEDED",
            "PCA_INVALID_ARN",
            "PCA_INVALID_STATE",
            "PCA_REQUEST_FAILED",
            "PCA_NAME_CONSTRAINTS_VALIDATION",
            "PCA_RESOURCE_NOT_FOUND",
            "PCA_INVALID_ARGS",
            "PCA_INVALID_DURATION",
            "PCA_ACCESS_DENIED",
            "OTHER",
        ],
        "Type": Literal["IMPORTED", "AMAZON_ISSUED", "PRIVATE"],
        "RenewalSummary": ClientDescribeCertificateResponseCertificateRenewalSummaryTypeDef,
        "KeyUsages": List[ClientDescribeCertificateResponseCertificateKeyUsagesTypeDef],
        "ExtendedKeyUsages": List[
            ClientDescribeCertificateResponseCertificateExtendedKeyUsagesTypeDef
        ],
        "CertificateAuthorityArn": str,
        "RenewalEligibility": Literal["ELIGIBLE", "INELIGIBLE"],
        "Options": ClientDescribeCertificateResponseCertificateOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeCertificateResponseCertificateTypeDef(
    _ClientDescribeCertificateResponseCertificateTypeDef
):
    """
    - **Certificate** *(dict) --*

      Metadata about an ACM certificate.
      - **CertificateArn** *(string) --*

        The Amazon Resource Name (ARN) of the certificate. For more information about ARNs, see
        `Amazon Resource Names (ARNs) and AWS Service Namespaces
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS
        General Reference* .
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

        Metadata about an ACM certificate.
        - **CertificateArn** *(string) --*

          The Amazon Resource Name (ARN) of the certificate. For more information about ARNs, see
          `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
          *AWS General Reference* .
    """


_ClientExportCertificateResponseTypeDef = TypedDict(
    "_ClientExportCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str, "PrivateKey": str},
    total=False,
)


class ClientExportCertificateResponseTypeDef(_ClientExportCertificateResponseTypeDef):
    """
    - *(dict) --*

      - **Certificate** *(string) --*

        The base64 PEM-encoded certificate.
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

        String that contains the ACM certificate represented by the ARN specified at input.
    """


_ClientImportCertificateResponseTypeDef = TypedDict(
    "_ClientImportCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)


class ClientImportCertificateResponseTypeDef(_ClientImportCertificateResponseTypeDef):
    """
    - *(dict) --*

      - **CertificateArn** *(string) --*

        The `Amazon Resource Name (ARN)
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of the
        imported certificate.
    """


_RequiredClientImportCertificateTagsTypeDef = TypedDict(
    "_RequiredClientImportCertificateTagsTypeDef", {"Key": str}
)
_OptionalClientImportCertificateTagsTypeDef = TypedDict(
    "_OptionalClientImportCertificateTagsTypeDef", {"Value": str}, total=False
)


class ClientImportCertificateTagsTypeDef(
    _RequiredClientImportCertificateTagsTypeDef, _OptionalClientImportCertificateTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair that identifies or specifies metadata about an ACM resource.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientListCertificatesIncludesTypeDef = TypedDict(
    "_ClientListCertificatesIncludesTypeDef",
    {
        "extendedKeyUsage": List[
            Literal[
                "TLS_WEB_SERVER_AUTHENTICATION",
                "TLS_WEB_CLIENT_AUTHENTICATION",
                "CODE_SIGNING",
                "EMAIL_PROTECTION",
                "TIME_STAMPING",
                "OCSP_SIGNING",
                "IPSEC_END_SYSTEM",
                "IPSEC_TUNNEL",
                "IPSEC_USER",
                "ANY",
                "NONE",
                "CUSTOM",
            ]
        ],
        "keyUsage": List[
            Literal[
                "DIGITAL_SIGNATURE",
                "NON_REPUDIATION",
                "KEY_ENCIPHERMENT",
                "DATA_ENCIPHERMENT",
                "KEY_AGREEMENT",
                "CERTIFICATE_SIGNING",
                "CRL_SIGNING",
                "ENCIPHER_ONLY",
                "DECIPHER_ONLY",
                "ANY",
                "CUSTOM",
            ]
        ],
        "keyTypes": List[
            Literal[
                "RSA_2048", "RSA_1024", "RSA_4096", "EC_prime256v1", "EC_secp384r1", "EC_secp521r1"
            ]
        ],
    },
    total=False,
)


class ClientListCertificatesIncludesTypeDef(_ClientListCertificatesIncludesTypeDef):
    """
    Filter the certificate list. For more information, see the  Filters structure.
    - **extendedKeyUsage** *(list) --*

      Specify one or more  ExtendedKeyUsage extension values.
      - *(string) --*
    """


_ClientListCertificatesResponseCertificateSummaryListTypeDef = TypedDict(
    "_ClientListCertificatesResponseCertificateSummaryListTypeDef",
    {"CertificateArn": str, "DomainName": str},
    total=False,
)


class ClientListCertificatesResponseCertificateSummaryListTypeDef(
    _ClientListCertificatesResponseCertificateSummaryListTypeDef
):
    pass


_ClientListCertificatesResponseTypeDef = TypedDict(
    "_ClientListCertificatesResponseTypeDef",
    {
        "NextToken": str,
        "CertificateSummaryList": List[ClientListCertificatesResponseCertificateSummaryListTypeDef],
    },
    total=False,
)


class ClientListCertificatesResponseTypeDef(_ClientListCertificatesResponseTypeDef):
    """
    - *(dict) --*

      - **NextToken** *(string) --*

        When the list is truncated, this value is present and contains the value to use for the
        ``NextToken`` parameter in a subsequent pagination request.
    """


_ClientListTagsForCertificateResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForCertificateResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForCertificateResponseTagsTypeDef(
    _ClientListTagsForCertificateResponseTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair that identifies or specifies metadata about an ACM resource.
      - **Key** *(string) --*

        The key of the tag.
    """


_ClientListTagsForCertificateResponseTypeDef = TypedDict(
    "_ClientListTagsForCertificateResponseTypeDef",
    {"Tags": List[ClientListTagsForCertificateResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForCertificateResponseTypeDef(_ClientListTagsForCertificateResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        The key-value pairs that define the applied tags.
        - *(dict) --*

          A key-value pair that identifies or specifies metadata about an ACM resource.
          - **Key** *(string) --*

            The key of the tag.
    """


_RequiredClientRemoveTagsFromCertificateTagsTypeDef = TypedDict(
    "_RequiredClientRemoveTagsFromCertificateTagsTypeDef", {"Key": str}
)
_OptionalClientRemoveTagsFromCertificateTagsTypeDef = TypedDict(
    "_OptionalClientRemoveTagsFromCertificateTagsTypeDef", {"Value": str}, total=False
)


class ClientRemoveTagsFromCertificateTagsTypeDef(
    _RequiredClientRemoveTagsFromCertificateTagsTypeDef,
    _OptionalClientRemoveTagsFromCertificateTagsTypeDef,
):
    """
    - *(dict) --*

      A key-value pair that identifies or specifies metadata about an ACM resource.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_RequiredClientRequestCertificateDomainValidationOptionsTypeDef = TypedDict(
    "_RequiredClientRequestCertificateDomainValidationOptionsTypeDef", {"DomainName": str}
)
_OptionalClientRequestCertificateDomainValidationOptionsTypeDef = TypedDict(
    "_OptionalClientRequestCertificateDomainValidationOptionsTypeDef",
    {"ValidationDomain": str},
    total=False,
)


class ClientRequestCertificateDomainValidationOptionsTypeDef(
    _RequiredClientRequestCertificateDomainValidationOptionsTypeDef,
    _OptionalClientRequestCertificateDomainValidationOptionsTypeDef,
):
    """
    - *(dict) --*

      Contains information about the domain names that you want ACM to use to send you emails that
      enable you to validate domain ownership.
      - **DomainName** *(string) --***[REQUIRED]**

        A fully qualified domain name (FQDN) in the certificate request.
    """


_ClientRequestCertificateOptionsTypeDef = TypedDict(
    "_ClientRequestCertificateOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientRequestCertificateOptionsTypeDef(_ClientRequestCertificateOptionsTypeDef):
    """
    Currently, you can use this parameter to specify whether to add the certificate to a certificate
    transparency log. Certificate transparency makes it possible to detect SSL/TLS certificates that
    have been mistakenly or maliciously issued. Certificates that have not been logged typically
    produce an error message in a browser. For more information, see `Opting Out of Certificate
    Transparency Logging
    <https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency>`__
    .
    - **CertificateTransparencyLoggingPreference** *(string) --*

      You can opt out of certificate transparency logging by specifying the ``DISABLED`` option. Opt
      in by specifying ``ENABLED`` .
    """


_ClientRequestCertificateResponseTypeDef = TypedDict(
    "_ClientRequestCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)


class ClientRequestCertificateResponseTypeDef(_ClientRequestCertificateResponseTypeDef):
    """
    - *(dict) --*

      - **CertificateArn** *(string) --*

        String that contains the ARN of the issued certificate. This must be of the form:

          ``arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012``
    """


_RequiredClientRequestCertificateTagsTypeDef = TypedDict(
    "_RequiredClientRequestCertificateTagsTypeDef", {"Key": str}
)
_OptionalClientRequestCertificateTagsTypeDef = TypedDict(
    "_OptionalClientRequestCertificateTagsTypeDef", {"Value": str}, total=False
)


class ClientRequestCertificateTagsTypeDef(
    _RequiredClientRequestCertificateTagsTypeDef, _OptionalClientRequestCertificateTagsTypeDef
):
    """
    - *(dict) --*

      A key-value pair that identifies or specifies metadata about an ACM resource.
      - **Key** *(string) --***[REQUIRED]**

        The key of the tag.
    """


_ClientUpdateCertificateOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateCertificateOptionsOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class ClientUpdateCertificateOptionsOptionsTypeDef(_ClientUpdateCertificateOptionsOptionsTypeDef):
    """
    Use to update the options for your certificate. Currently, you can specify whether to add your
    certificate to a transparency log. Certificate transparency makes it possible to detect SSL/TLS
    certificates that have been mistakenly or maliciously issued. Certificates that have not been
    logged typically produce an error message in a browser.
    - **CertificateTransparencyLoggingPreference** *(string) --*

      You can opt out of certificate transparency logging by specifying the ``DISABLED`` option. Opt
      in by specifying ``ENABLED`` .
    """


_ListCertificatesPaginateIncludesTypeDef = TypedDict(
    "_ListCertificatesPaginateIncludesTypeDef",
    {
        "extendedKeyUsage": List[
            Literal[
                "TLS_WEB_SERVER_AUTHENTICATION",
                "TLS_WEB_CLIENT_AUTHENTICATION",
                "CODE_SIGNING",
                "EMAIL_PROTECTION",
                "TIME_STAMPING",
                "OCSP_SIGNING",
                "IPSEC_END_SYSTEM",
                "IPSEC_TUNNEL",
                "IPSEC_USER",
                "ANY",
                "NONE",
                "CUSTOM",
            ]
        ],
        "keyUsage": List[
            Literal[
                "DIGITAL_SIGNATURE",
                "NON_REPUDIATION",
                "KEY_ENCIPHERMENT",
                "DATA_ENCIPHERMENT",
                "KEY_AGREEMENT",
                "CERTIFICATE_SIGNING",
                "CRL_SIGNING",
                "ENCIPHER_ONLY",
                "DECIPHER_ONLY",
                "ANY",
                "CUSTOM",
            ]
        ],
        "keyTypes": List[
            Literal[
                "RSA_2048", "RSA_1024", "RSA_4096", "EC_prime256v1", "EC_secp384r1", "EC_secp521r1"
            ]
        ],
    },
    total=False,
)


class ListCertificatesPaginateIncludesTypeDef(_ListCertificatesPaginateIncludesTypeDef):
    """
    Filter the certificate list. For more information, see the  Filters structure.
    - **extendedKeyUsage** *(list) --*

      Specify one or more  ExtendedKeyUsage extension values.
      - *(string) --*
    """


_ListCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCertificatesPaginatePaginationConfigTypeDef(
    _ListCertificatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCertificatesPaginateResponseCertificateSummaryListTypeDef = TypedDict(
    "_ListCertificatesPaginateResponseCertificateSummaryListTypeDef",
    {"CertificateArn": str, "DomainName": str},
    total=False,
)


class ListCertificatesPaginateResponseCertificateSummaryListTypeDef(
    _ListCertificatesPaginateResponseCertificateSummaryListTypeDef
):
    """
    - *(dict) --*

      This structure is returned in the response object of  ListCertificates action.
      - **CertificateArn** *(string) --*

        Amazon Resource Name (ARN) of the certificate. This is of the form:

          ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``
    """


_ListCertificatesPaginateResponseTypeDef = TypedDict(
    "_ListCertificatesPaginateResponseTypeDef",
    {"CertificateSummaryList": List[ListCertificatesPaginateResponseCertificateSummaryListTypeDef]},
    total=False,
)


class ListCertificatesPaginateResponseTypeDef(_ListCertificatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **CertificateSummaryList** *(list) --*

        A list of ACM certificates.
        - *(dict) --*

          This structure is returned in the response object of  ListCertificates action.
          - **CertificateArn** *(string) --*

            Amazon Resource Name (ARN) of the certificate. This is of the form:

              ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``
    """
