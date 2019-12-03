"Main interface for route53domains service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCheckDomainAvailabilityResponseTypeDef",
    "ClientCheckDomainTransferabilityResponseTransferabilityTypeDef",
    "ClientCheckDomainTransferabilityResponseTypeDef",
    "ClientDisableDomainTransferLockResponseTypeDef",
    "ClientEnableDomainTransferLockResponseTypeDef",
    "ClientGetContactReachabilityStatusResponseTypeDef",
    "ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef",
    "ClientGetDomainDetailResponseAdminContactTypeDef",
    "ClientGetDomainDetailResponseNameserversTypeDef",
    "ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef",
    "ClientGetDomainDetailResponseRegistrantContactTypeDef",
    "ClientGetDomainDetailResponseTechContactExtraParamsTypeDef",
    "ClientGetDomainDetailResponseTechContactTypeDef",
    "ClientGetDomainDetailResponseTypeDef",
    "ClientGetDomainSuggestionsResponseSuggestionsListTypeDef",
    "ClientGetDomainSuggestionsResponseTypeDef",
    "ClientGetOperationDetailResponseTypeDef",
    "ClientListDomainsResponseDomainsTypeDef",
    "ClientListDomainsResponseTypeDef",
    "ClientListOperationsResponseOperationsTypeDef",
    "ClientListOperationsResponseTypeDef",
    "ClientListTagsForDomainResponseTagListTypeDef",
    "ClientListTagsForDomainResponseTypeDef",
    "ClientRegisterDomainAdminContactExtraParamsTypeDef",
    "ClientRegisterDomainAdminContactTypeDef",
    "ClientRegisterDomainRegistrantContactExtraParamsTypeDef",
    "ClientRegisterDomainRegistrantContactTypeDef",
    "ClientRegisterDomainResponseTypeDef",
    "ClientRegisterDomainTechContactExtraParamsTypeDef",
    "ClientRegisterDomainTechContactTypeDef",
    "ClientRenewDomainResponseTypeDef",
    "ClientResendContactReachabilityEmailResponseTypeDef",
    "ClientRetrieveDomainAuthCodeResponseTypeDef",
    "ClientTransferDomainAdminContactExtraParamsTypeDef",
    "ClientTransferDomainAdminContactTypeDef",
    "ClientTransferDomainNameserversTypeDef",
    "ClientTransferDomainRegistrantContactExtraParamsTypeDef",
    "ClientTransferDomainRegistrantContactTypeDef",
    "ClientTransferDomainResponseTypeDef",
    "ClientTransferDomainTechContactExtraParamsTypeDef",
    "ClientTransferDomainTechContactTypeDef",
    "ClientUpdateDomainContactAdminContactExtraParamsTypeDef",
    "ClientUpdateDomainContactAdminContactTypeDef",
    "ClientUpdateDomainContactPrivacyResponseTypeDef",
    "ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef",
    "ClientUpdateDomainContactRegistrantContactTypeDef",
    "ClientUpdateDomainContactResponseTypeDef",
    "ClientUpdateDomainContactTechContactExtraParamsTypeDef",
    "ClientUpdateDomainContactTechContactTypeDef",
    "ClientUpdateDomainNameserversNameserversTypeDef",
    "ClientUpdateDomainNameserversResponseTypeDef",
    "ClientUpdateTagsForDomainTagsToUpdateTypeDef",
    "ClientViewBillingResponseBillingRecordsTypeDef",
    "ClientViewBillingResponseTypeDef",
    "ListDomainsPaginatePaginationConfigTypeDef",
    "ListDomainsPaginateResponseDomainsTypeDef",
    "ListDomainsPaginateResponseTypeDef",
    "ListOperationsPaginatePaginationConfigTypeDef",
    "ListOperationsPaginateResponseOperationsTypeDef",
    "ListOperationsPaginateResponseTypeDef",
    "ViewBillingPaginatePaginationConfigTypeDef",
    "ViewBillingPaginateResponseBillingRecordsTypeDef",
    "ViewBillingPaginateResponseTypeDef",
)


_ClientCheckDomainAvailabilityResponseTypeDef = TypedDict(
    "_ClientCheckDomainAvailabilityResponseTypeDef",
    {
        "Availability": Literal[
            "AVAILABLE",
            "AVAILABLE_RESERVED",
            "AVAILABLE_PREORDER",
            "UNAVAILABLE",
            "UNAVAILABLE_PREMIUM",
            "UNAVAILABLE_RESTRICTED",
            "RESERVED",
            "DONT_KNOW",
        ]
    },
    total=False,
)


class ClientCheckDomainAvailabilityResponseTypeDef(_ClientCheckDomainAvailabilityResponseTypeDef):
    """
    - *(dict) --*

      The CheckDomainAvailability response includes the following elements.
      - **Availability** *(string) --*

        Whether the domain name is available for registering.
        .. note::

          You can register only domains designated as ``AVAILABLE`` .
    """


_ClientCheckDomainTransferabilityResponseTransferabilityTypeDef = TypedDict(
    "_ClientCheckDomainTransferabilityResponseTransferabilityTypeDef",
    {"Transferable": Literal["TRANSFERABLE", "UNTRANSFERABLE", "DONT_KNOW"]},
    total=False,
)


class ClientCheckDomainTransferabilityResponseTransferabilityTypeDef(
    _ClientCheckDomainTransferabilityResponseTransferabilityTypeDef
):
    """
    - **Transferability** *(dict) --*

      A complex type that contains information about whether the specified domain can be transferred
      to Amazon Route 53.
      - **Transferable** *(string) --*

        Whether the domain name can be transferred to Amazon Route 53.
        .. note::

          You can transfer only domains that have a value of ``TRANSFERABLE`` for ``Transferable`` .
    """


_ClientCheckDomainTransferabilityResponseTypeDef = TypedDict(
    "_ClientCheckDomainTransferabilityResponseTypeDef",
    {"Transferability": ClientCheckDomainTransferabilityResponseTransferabilityTypeDef},
    total=False,
)


class ClientCheckDomainTransferabilityResponseTypeDef(
    _ClientCheckDomainTransferabilityResponseTypeDef
):
    """
    - *(dict) --*

      The CheckDomainTransferability response includes the following elements.
      - **Transferability** *(dict) --*

        A complex type that contains information about whether the specified domain can be
        transferred to Amazon Route 53.
        - **Transferable** *(string) --*

          Whether the domain name can be transferred to Amazon Route 53.
          .. note::

            You can transfer only domains that have a value of ``TRANSFERABLE`` for ``Transferable``
            .
    """


_ClientDisableDomainTransferLockResponseTypeDef = TypedDict(
    "_ClientDisableDomainTransferLockResponseTypeDef", {"OperationId": str}, total=False
)


class ClientDisableDomainTransferLockResponseTypeDef(
    _ClientDisableDomainTransferLockResponseTypeDef
):
    """
    - *(dict) --*

      The DisableDomainTransferLock response includes the following element.
      - **OperationId** *(string) --*

        Identifier for tracking the progress of the request. To use this ID to query the operation
        status, use  GetOperationDetail .
    """


_ClientEnableDomainTransferLockResponseTypeDef = TypedDict(
    "_ClientEnableDomainTransferLockResponseTypeDef", {"OperationId": str}, total=False
)


class ClientEnableDomainTransferLockResponseTypeDef(_ClientEnableDomainTransferLockResponseTypeDef):
    """
    - *(dict) --*

      The EnableDomainTransferLock response includes the following elements.
      - **OperationId** *(string) --*

        Identifier for tracking the progress of the request. To use this ID to query the operation
        status, use GetOperationDetail.
    """


_ClientGetContactReachabilityStatusResponseTypeDef = TypedDict(
    "_ClientGetContactReachabilityStatusResponseTypeDef",
    {"domainName": str, "status": Literal["PENDING", "DONE", "EXPIRED"]},
    total=False,
)


class ClientGetContactReachabilityStatusResponseTypeDef(
    _ClientGetContactReachabilityStatusResponseTypeDef
):
    """
    - *(dict) --*

      - **domainName** *(string) --*

        The domain name for which you requested the reachability status.
    """


_ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef(
    _ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef
):
    pass


_ClientGetDomainDetailResponseAdminContactTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseAdminContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientGetDomainDetailResponseAdminContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientGetDomainDetailResponseAdminContactTypeDef(
    _ClientGetDomainDetailResponseAdminContactTypeDef
):
    pass


_ClientGetDomainDetailResponseNameserversTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseNameserversTypeDef",
    {"Name": str, "GlueIps": List[str]},
    total=False,
)


class ClientGetDomainDetailResponseNameserversTypeDef(
    _ClientGetDomainDetailResponseNameserversTypeDef
):
    pass


_ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef(
    _ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef
):
    pass


_ClientGetDomainDetailResponseRegistrantContactTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseRegistrantContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientGetDomainDetailResponseRegistrantContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientGetDomainDetailResponseRegistrantContactTypeDef(
    _ClientGetDomainDetailResponseRegistrantContactTypeDef
):
    pass


_ClientGetDomainDetailResponseTechContactExtraParamsTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseTechContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientGetDomainDetailResponseTechContactExtraParamsTypeDef(
    _ClientGetDomainDetailResponseTechContactExtraParamsTypeDef
):
    pass


_ClientGetDomainDetailResponseTechContactTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseTechContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientGetDomainDetailResponseTechContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientGetDomainDetailResponseTechContactTypeDef(
    _ClientGetDomainDetailResponseTechContactTypeDef
):
    pass


_ClientGetDomainDetailResponseTypeDef = TypedDict(
    "_ClientGetDomainDetailResponseTypeDef",
    {
        "DomainName": str,
        "Nameservers": List[ClientGetDomainDetailResponseNameserversTypeDef],
        "AutoRenew": bool,
        "AdminContact": ClientGetDomainDetailResponseAdminContactTypeDef,
        "RegistrantContact": ClientGetDomainDetailResponseRegistrantContactTypeDef,
        "TechContact": ClientGetDomainDetailResponseTechContactTypeDef,
        "AdminPrivacy": bool,
        "RegistrantPrivacy": bool,
        "TechPrivacy": bool,
        "RegistrarName": str,
        "WhoIsServer": str,
        "RegistrarUrl": str,
        "AbuseContactEmail": str,
        "AbuseContactPhone": str,
        "RegistryDomainId": str,
        "CreationDate": datetime,
        "UpdatedDate": datetime,
        "ExpirationDate": datetime,
        "Reseller": str,
        "DnsSec": str,
        "StatusList": List[str],
    },
    total=False,
)


class ClientGetDomainDetailResponseTypeDef(_ClientGetDomainDetailResponseTypeDef):
    """
    - *(dict) --*

      The GetDomainDetail response includes the following elements.
      - **DomainName** *(string) --*

        The name of a domain.
    """


_ClientGetDomainSuggestionsResponseSuggestionsListTypeDef = TypedDict(
    "_ClientGetDomainSuggestionsResponseSuggestionsListTypeDef",
    {"DomainName": str, "Availability": str},
    total=False,
)


class ClientGetDomainSuggestionsResponseSuggestionsListTypeDef(
    _ClientGetDomainSuggestionsResponseSuggestionsListTypeDef
):
    """
    - *(dict) --*

      Information about one suggested domain name.
      - **DomainName** *(string) --*

        A suggested domain name.
    """


_ClientGetDomainSuggestionsResponseTypeDef = TypedDict(
    "_ClientGetDomainSuggestionsResponseTypeDef",
    {"SuggestionsList": List[ClientGetDomainSuggestionsResponseSuggestionsListTypeDef]},
    total=False,
)


class ClientGetDomainSuggestionsResponseTypeDef(_ClientGetDomainSuggestionsResponseTypeDef):
    """
    - *(dict) --*

      - **SuggestionsList** *(list) --*

        A list of possible domain names. If you specified ``true`` for ``OnlyAvailable`` in the
        request, the list contains only domains that are available for registration.
        - *(dict) --*

          Information about one suggested domain name.
          - **DomainName** *(string) --*

            A suggested domain name.
    """


_ClientGetOperationDetailResponseTypeDef = TypedDict(
    "_ClientGetOperationDetailResponseTypeDef",
    {
        "OperationId": str,
        "Status": Literal["SUBMITTED", "IN_PROGRESS", "ERROR", "SUCCESSFUL", "FAILED"],
        "Message": str,
        "DomainName": str,
        "Type": Literal[
            "REGISTER_DOMAIN",
            "DELETE_DOMAIN",
            "TRANSFER_IN_DOMAIN",
            "UPDATE_DOMAIN_CONTACT",
            "UPDATE_NAMESERVER",
            "CHANGE_PRIVACY_PROTECTION",
            "DOMAIN_LOCK",
            "ENABLE_AUTORENEW",
            "DISABLE_AUTORENEW",
            "ADD_DNSSEC",
            "REMOVE_DNSSEC",
            "EXPIRE_DOMAIN",
            "TRANSFER_OUT_DOMAIN",
            "CHANGE_DOMAIN_OWNER",
            "RENEW_DOMAIN",
            "PUSH_DOMAIN",
        ],
        "SubmittedDate": datetime,
    },
    total=False,
)


class ClientGetOperationDetailResponseTypeDef(_ClientGetOperationDetailResponseTypeDef):
    """
    - *(dict) --*

      The GetOperationDetail response includes the following elements.
      - **OperationId** *(string) --*

        The identifier for the operation.
    """


_ClientListDomainsResponseDomainsTypeDef = TypedDict(
    "_ClientListDomainsResponseDomainsTypeDef",
    {"DomainName": str, "AutoRenew": bool, "TransferLock": bool, "Expiry": datetime},
    total=False,
)


class ClientListDomainsResponseDomainsTypeDef(_ClientListDomainsResponseDomainsTypeDef):
    """
    - *(dict) --*

      Summary information about one domain.
      - **DomainName** *(string) --*

        The name of the domain that the summary information applies to.
    """


_ClientListDomainsResponseTypeDef = TypedDict(
    "_ClientListDomainsResponseTypeDef",
    {"Domains": List[ClientListDomainsResponseDomainsTypeDef], "NextPageMarker": str},
    total=False,
)


class ClientListDomainsResponseTypeDef(_ClientListDomainsResponseTypeDef):
    """
    - *(dict) --*

      The ListDomains response includes the following elements.
      - **Domains** *(list) --*

        A summary of domains.
        - *(dict) --*

          Summary information about one domain.
          - **DomainName** *(string) --*

            The name of the domain that the summary information applies to.
    """


_ClientListOperationsResponseOperationsTypeDef = TypedDict(
    "_ClientListOperationsResponseOperationsTypeDef",
    {
        "OperationId": str,
        "Status": Literal["SUBMITTED", "IN_PROGRESS", "ERROR", "SUCCESSFUL", "FAILED"],
        "Type": Literal[
            "REGISTER_DOMAIN",
            "DELETE_DOMAIN",
            "TRANSFER_IN_DOMAIN",
            "UPDATE_DOMAIN_CONTACT",
            "UPDATE_NAMESERVER",
            "CHANGE_PRIVACY_PROTECTION",
            "DOMAIN_LOCK",
            "ENABLE_AUTORENEW",
            "DISABLE_AUTORENEW",
            "ADD_DNSSEC",
            "REMOVE_DNSSEC",
            "EXPIRE_DOMAIN",
            "TRANSFER_OUT_DOMAIN",
            "CHANGE_DOMAIN_OWNER",
            "RENEW_DOMAIN",
            "PUSH_DOMAIN",
        ],
        "SubmittedDate": datetime,
    },
    total=False,
)


class ClientListOperationsResponseOperationsTypeDef(_ClientListOperationsResponseOperationsTypeDef):
    """
    - *(dict) --*

      OperationSummary includes the following elements.
      - **OperationId** *(string) --*

        Identifier returned to track the requested action.
    """


_ClientListOperationsResponseTypeDef = TypedDict(
    "_ClientListOperationsResponseTypeDef",
    {"Operations": List[ClientListOperationsResponseOperationsTypeDef], "NextPageMarker": str},
    total=False,
)


class ClientListOperationsResponseTypeDef(_ClientListOperationsResponseTypeDef):
    """
    - *(dict) --*

      The ListOperations response includes the following elements.
      - **Operations** *(list) --*

        Lists summaries of the operations.
        - *(dict) --*

          OperationSummary includes the following elements.
          - **OperationId** *(string) --*

            Identifier returned to track the requested action.
    """


_ClientListTagsForDomainResponseTagListTypeDef = TypedDict(
    "_ClientListTagsForDomainResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForDomainResponseTagListTypeDef(_ClientListTagsForDomainResponseTagListTypeDef):
    """
    - *(dict) --*

      Each tag includes the following elements.
      - **Key** *(string) --*

        The key (name) of a tag.
        Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"
        Constraints: Each key can be 1-128 characters long.
    """


_ClientListTagsForDomainResponseTypeDef = TypedDict(
    "_ClientListTagsForDomainResponseTypeDef",
    {"TagList": List[ClientListTagsForDomainResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsForDomainResponseTypeDef(_ClientListTagsForDomainResponseTypeDef):
    """
    - *(dict) --*

      The ListTagsForDomain response includes the following elements.
      - **TagList** *(list) --*

        A list of the tags that are associated with the specified domain.
        - *(dict) --*

          Each tag includes the following elements.
          - **Key** *(string) --*

            The key (name) of a tag.
            Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"
            Constraints: Each key can be 1-128 characters long.
    """


_ClientRegisterDomainAdminContactExtraParamsTypeDef = TypedDict(
    "_ClientRegisterDomainAdminContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientRegisterDomainAdminContactExtraParamsTypeDef(
    _ClientRegisterDomainAdminContactExtraParamsTypeDef
):
    pass


_ClientRegisterDomainAdminContactTypeDef = TypedDict(
    "_ClientRegisterDomainAdminContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientRegisterDomainAdminContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientRegisterDomainAdminContactTypeDef(_ClientRegisterDomainAdminContactTypeDef):
    """
    Provides detailed contact information.
    - **FirstName** *(string) --*

      First name of contact.
    """


_ClientRegisterDomainRegistrantContactExtraParamsTypeDef = TypedDict(
    "_ClientRegisterDomainRegistrantContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientRegisterDomainRegistrantContactExtraParamsTypeDef(
    _ClientRegisterDomainRegistrantContactExtraParamsTypeDef
):
    pass


_ClientRegisterDomainRegistrantContactTypeDef = TypedDict(
    "_ClientRegisterDomainRegistrantContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientRegisterDomainRegistrantContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientRegisterDomainRegistrantContactTypeDef(_ClientRegisterDomainRegistrantContactTypeDef):
    """
    Provides detailed contact information.
    - **FirstName** *(string) --*

      First name of contact.
    """


_ClientRegisterDomainResponseTypeDef = TypedDict(
    "_ClientRegisterDomainResponseTypeDef", {"OperationId": str}, total=False
)


class ClientRegisterDomainResponseTypeDef(_ClientRegisterDomainResponseTypeDef):
    """
    - *(dict) --*

      The RegisterDomain response includes the following element.
      - **OperationId** *(string) --*

        Identifier for tracking the progress of the request. To use this ID to query the operation
        status, use  GetOperationDetail .
    """


_ClientRegisterDomainTechContactExtraParamsTypeDef = TypedDict(
    "_ClientRegisterDomainTechContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientRegisterDomainTechContactExtraParamsTypeDef(
    _ClientRegisterDomainTechContactExtraParamsTypeDef
):
    pass


_ClientRegisterDomainTechContactTypeDef = TypedDict(
    "_ClientRegisterDomainTechContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientRegisterDomainTechContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientRegisterDomainTechContactTypeDef(_ClientRegisterDomainTechContactTypeDef):
    """
    Provides detailed contact information.
    - **FirstName** *(string) --*

      First name of contact.
    """


_ClientRenewDomainResponseTypeDef = TypedDict(
    "_ClientRenewDomainResponseTypeDef", {"OperationId": str}, total=False
)


class ClientRenewDomainResponseTypeDef(_ClientRenewDomainResponseTypeDef):
    """
    - *(dict) --*

      - **OperationId** *(string) --*

        The identifier for tracking the progress of the request. To use this ID to query the
        operation status, use  GetOperationDetail .
    """


_ClientResendContactReachabilityEmailResponseTypeDef = TypedDict(
    "_ClientResendContactReachabilityEmailResponseTypeDef",
    {"domainName": str, "emailAddress": str, "isAlreadyVerified": bool},
    total=False,
)


class ClientResendContactReachabilityEmailResponseTypeDef(
    _ClientResendContactReachabilityEmailResponseTypeDef
):
    """
    - *(dict) --*

      - **domainName** *(string) --*

        The domain name for which you requested a confirmation email.
    """


_ClientRetrieveDomainAuthCodeResponseTypeDef = TypedDict(
    "_ClientRetrieveDomainAuthCodeResponseTypeDef", {"AuthCode": str}, total=False
)


class ClientRetrieveDomainAuthCodeResponseTypeDef(_ClientRetrieveDomainAuthCodeResponseTypeDef):
    """
    - *(dict) --*

      The RetrieveDomainAuthCode response includes the following element.
      - **AuthCode** *(string) --*

        The authorization code for the domain.
    """


_ClientTransferDomainAdminContactExtraParamsTypeDef = TypedDict(
    "_ClientTransferDomainAdminContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientTransferDomainAdminContactExtraParamsTypeDef(
    _ClientTransferDomainAdminContactExtraParamsTypeDef
):
    pass


_ClientTransferDomainAdminContactTypeDef = TypedDict(
    "_ClientTransferDomainAdminContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientTransferDomainAdminContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientTransferDomainAdminContactTypeDef(_ClientTransferDomainAdminContactTypeDef):
    """
    Provides detailed contact information.
    - **FirstName** *(string) --*

      First name of contact.
    """


_RequiredClientTransferDomainNameserversTypeDef = TypedDict(
    "_RequiredClientTransferDomainNameserversTypeDef", {"Name": str}
)
_OptionalClientTransferDomainNameserversTypeDef = TypedDict(
    "_OptionalClientTransferDomainNameserversTypeDef", {"GlueIps": List[str]}, total=False
)


class ClientTransferDomainNameserversTypeDef(
    _RequiredClientTransferDomainNameserversTypeDef, _OptionalClientTransferDomainNameserversTypeDef
):
    """
    - *(dict) --*

      Nameserver includes the following elements.
      - **Name** *(string) --***[REQUIRED]**

        The fully qualified host name of the name server.
        Constraint: Maximum 255 characters
    """


_ClientTransferDomainRegistrantContactExtraParamsTypeDef = TypedDict(
    "_ClientTransferDomainRegistrantContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientTransferDomainRegistrantContactExtraParamsTypeDef(
    _ClientTransferDomainRegistrantContactExtraParamsTypeDef
):
    pass


_ClientTransferDomainRegistrantContactTypeDef = TypedDict(
    "_ClientTransferDomainRegistrantContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientTransferDomainRegistrantContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientTransferDomainRegistrantContactTypeDef(_ClientTransferDomainRegistrantContactTypeDef):
    """
    Provides detailed contact information.
    - **FirstName** *(string) --*

      First name of contact.
    """


_ClientTransferDomainResponseTypeDef = TypedDict(
    "_ClientTransferDomainResponseTypeDef", {"OperationId": str}, total=False
)


class ClientTransferDomainResponseTypeDef(_ClientTransferDomainResponseTypeDef):
    """
    - *(dict) --*

      The TranserDomain response includes the following element.
      - **OperationId** *(string) --*

        Identifier for tracking the progress of the request. To use this ID to query the operation
        status, use  GetOperationDetail .
    """


_ClientTransferDomainTechContactExtraParamsTypeDef = TypedDict(
    "_ClientTransferDomainTechContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientTransferDomainTechContactExtraParamsTypeDef(
    _ClientTransferDomainTechContactExtraParamsTypeDef
):
    pass


_ClientTransferDomainTechContactTypeDef = TypedDict(
    "_ClientTransferDomainTechContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientTransferDomainTechContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientTransferDomainTechContactTypeDef(_ClientTransferDomainTechContactTypeDef):
    """
    Provides detailed contact information.
    - **FirstName** *(string) --*

      First name of contact.
    """


_ClientUpdateDomainContactAdminContactExtraParamsTypeDef = TypedDict(
    "_ClientUpdateDomainContactAdminContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientUpdateDomainContactAdminContactExtraParamsTypeDef(
    _ClientUpdateDomainContactAdminContactExtraParamsTypeDef
):
    pass


_ClientUpdateDomainContactAdminContactTypeDef = TypedDict(
    "_ClientUpdateDomainContactAdminContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientUpdateDomainContactAdminContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientUpdateDomainContactAdminContactTypeDef(_ClientUpdateDomainContactAdminContactTypeDef):
    """
    Provides detailed contact information.
    - **FirstName** *(string) --*

      First name of contact.
    """


_ClientUpdateDomainContactPrivacyResponseTypeDef = TypedDict(
    "_ClientUpdateDomainContactPrivacyResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateDomainContactPrivacyResponseTypeDef(
    _ClientUpdateDomainContactPrivacyResponseTypeDef
):
    """
    - *(dict) --*

      The UpdateDomainContactPrivacy response includes the following element.
      - **OperationId** *(string) --*

        Identifier for tracking the progress of the request. To use this ID to query the operation
        status, use GetOperationDetail.
    """


_ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef = TypedDict(
    "_ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef(
    _ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef
):
    pass


_ClientUpdateDomainContactRegistrantContactTypeDef = TypedDict(
    "_ClientUpdateDomainContactRegistrantContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientUpdateDomainContactRegistrantContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientUpdateDomainContactRegistrantContactTypeDef(
    _ClientUpdateDomainContactRegistrantContactTypeDef
):
    """
    Provides detailed contact information.
    - **FirstName** *(string) --*

      First name of contact.
    """


_ClientUpdateDomainContactResponseTypeDef = TypedDict(
    "_ClientUpdateDomainContactResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateDomainContactResponseTypeDef(_ClientUpdateDomainContactResponseTypeDef):
    """
    - *(dict) --*

      The UpdateDomainContact response includes the following element.
      - **OperationId** *(string) --*

        Identifier for tracking the progress of the request. To use this ID to query the operation
        status, use  GetOperationDetail .
    """


_ClientUpdateDomainContactTechContactExtraParamsTypeDef = TypedDict(
    "_ClientUpdateDomainContactTechContactExtraParamsTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
    total=False,
)


class ClientUpdateDomainContactTechContactExtraParamsTypeDef(
    _ClientUpdateDomainContactTechContactExtraParamsTypeDef
):
    pass


_ClientUpdateDomainContactTechContactTypeDef = TypedDict(
    "_ClientUpdateDomainContactTechContactTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List[ClientUpdateDomainContactTechContactExtraParamsTypeDef],
    },
    total=False,
)


class ClientUpdateDomainContactTechContactTypeDef(_ClientUpdateDomainContactTechContactTypeDef):
    """
    Provides detailed contact information.
    - **FirstName** *(string) --*

      First name of contact.
    """


_RequiredClientUpdateDomainNameserversNameserversTypeDef = TypedDict(
    "_RequiredClientUpdateDomainNameserversNameserversTypeDef", {"Name": str}
)
_OptionalClientUpdateDomainNameserversNameserversTypeDef = TypedDict(
    "_OptionalClientUpdateDomainNameserversNameserversTypeDef", {"GlueIps": List[str]}, total=False
)


class ClientUpdateDomainNameserversNameserversTypeDef(
    _RequiredClientUpdateDomainNameserversNameserversTypeDef,
    _OptionalClientUpdateDomainNameserversNameserversTypeDef,
):
    """
    - *(dict) --*

      Nameserver includes the following elements.
      - **Name** *(string) --***[REQUIRED]**

        The fully qualified host name of the name server.
        Constraint: Maximum 255 characters
    """


_ClientUpdateDomainNameserversResponseTypeDef = TypedDict(
    "_ClientUpdateDomainNameserversResponseTypeDef", {"OperationId": str}, total=False
)


class ClientUpdateDomainNameserversResponseTypeDef(_ClientUpdateDomainNameserversResponseTypeDef):
    """
    - *(dict) --*

      The UpdateDomainNameservers response includes the following element.
      - **OperationId** *(string) --*

        Identifier for tracking the progress of the request. To use this ID to query the operation
        status, use  GetOperationDetail .
    """


_ClientUpdateTagsForDomainTagsToUpdateTypeDef = TypedDict(
    "_ClientUpdateTagsForDomainTagsToUpdateTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUpdateTagsForDomainTagsToUpdateTypeDef(_ClientUpdateTagsForDomainTagsToUpdateTypeDef):
    """
    - *(dict) --*

      Each tag includes the following elements.
      - **Key** *(string) --*

        The key (name) of a tag.
        Valid values: A-Z, a-z, 0-9, space, ".:/=+\\-@"
        Constraints: Each key can be 1-128 characters long.
    """


_ClientViewBillingResponseBillingRecordsTypeDef = TypedDict(
    "_ClientViewBillingResponseBillingRecordsTypeDef",
    {
        "DomainName": str,
        "Operation": Literal[
            "REGISTER_DOMAIN",
            "DELETE_DOMAIN",
            "TRANSFER_IN_DOMAIN",
            "UPDATE_DOMAIN_CONTACT",
            "UPDATE_NAMESERVER",
            "CHANGE_PRIVACY_PROTECTION",
            "DOMAIN_LOCK",
            "ENABLE_AUTORENEW",
            "DISABLE_AUTORENEW",
            "ADD_DNSSEC",
            "REMOVE_DNSSEC",
            "EXPIRE_DOMAIN",
            "TRANSFER_OUT_DOMAIN",
            "CHANGE_DOMAIN_OWNER",
            "RENEW_DOMAIN",
            "PUSH_DOMAIN",
        ],
        "InvoiceId": str,
        "BillDate": datetime,
        "Price": float,
    },
    total=False,
)


class ClientViewBillingResponseBillingRecordsTypeDef(
    _ClientViewBillingResponseBillingRecordsTypeDef
):
    pass


_ClientViewBillingResponseTypeDef = TypedDict(
    "_ClientViewBillingResponseTypeDef",
    {"NextPageMarker": str, "BillingRecords": List[ClientViewBillingResponseBillingRecordsTypeDef]},
    total=False,
)


class ClientViewBillingResponseTypeDef(_ClientViewBillingResponseTypeDef):
    """
    - *(dict) --*

      The ViewBilling response includes the following elements.
      - **NextPageMarker** *(string) --*

        If there are more billing records than you specified for ``MaxItems`` in the request, submit
        another request and include the value of ``NextPageMarker`` in the value of ``Marker`` .
    """


_ListDomainsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDomainsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDomainsPaginatePaginationConfigTypeDef(_ListDomainsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDomainsPaginateResponseDomainsTypeDef = TypedDict(
    "_ListDomainsPaginateResponseDomainsTypeDef",
    {"DomainName": str, "AutoRenew": bool, "TransferLock": bool, "Expiry": datetime},
    total=False,
)


class ListDomainsPaginateResponseDomainsTypeDef(_ListDomainsPaginateResponseDomainsTypeDef):
    """
    - *(dict) --*

      Summary information about one domain.
      - **DomainName** *(string) --*

        The name of the domain that the summary information applies to.
    """


_ListDomainsPaginateResponseTypeDef = TypedDict(
    "_ListDomainsPaginateResponseTypeDef",
    {"Domains": List[ListDomainsPaginateResponseDomainsTypeDef], "NextToken": str},
    total=False,
)


class ListDomainsPaginateResponseTypeDef(_ListDomainsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The ListDomains response includes the following elements.
      - **Domains** *(list) --*

        A summary of domains.
        - *(dict) --*

          Summary information about one domain.
          - **DomainName** *(string) --*

            The name of the domain that the summary information applies to.
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
    {
        "OperationId": str,
        "Status": Literal["SUBMITTED", "IN_PROGRESS", "ERROR", "SUCCESSFUL", "FAILED"],
        "Type": Literal[
            "REGISTER_DOMAIN",
            "DELETE_DOMAIN",
            "TRANSFER_IN_DOMAIN",
            "UPDATE_DOMAIN_CONTACT",
            "UPDATE_NAMESERVER",
            "CHANGE_PRIVACY_PROTECTION",
            "DOMAIN_LOCK",
            "ENABLE_AUTORENEW",
            "DISABLE_AUTORENEW",
            "ADD_DNSSEC",
            "REMOVE_DNSSEC",
            "EXPIRE_DOMAIN",
            "TRANSFER_OUT_DOMAIN",
            "CHANGE_DOMAIN_OWNER",
            "RENEW_DOMAIN",
            "PUSH_DOMAIN",
        ],
        "SubmittedDate": datetime,
    },
    total=False,
)


class ListOperationsPaginateResponseOperationsTypeDef(
    _ListOperationsPaginateResponseOperationsTypeDef
):
    """
    - *(dict) --*

      OperationSummary includes the following elements.
      - **OperationId** *(string) --*

        Identifier returned to track the requested action.
    """


_ListOperationsPaginateResponseTypeDef = TypedDict(
    "_ListOperationsPaginateResponseTypeDef",
    {"Operations": List[ListOperationsPaginateResponseOperationsTypeDef], "NextToken": str},
    total=False,
)


class ListOperationsPaginateResponseTypeDef(_ListOperationsPaginateResponseTypeDef):
    """
    - *(dict) --*

      The ListOperations response includes the following elements.
      - **Operations** *(list) --*

        Lists summaries of the operations.
        - *(dict) --*

          OperationSummary includes the following elements.
          - **OperationId** *(string) --*

            Identifier returned to track the requested action.
    """


_ViewBillingPaginatePaginationConfigTypeDef = TypedDict(
    "_ViewBillingPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ViewBillingPaginatePaginationConfigTypeDef(_ViewBillingPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ViewBillingPaginateResponseBillingRecordsTypeDef = TypedDict(
    "_ViewBillingPaginateResponseBillingRecordsTypeDef",
    {
        "DomainName": str,
        "Operation": Literal[
            "REGISTER_DOMAIN",
            "DELETE_DOMAIN",
            "TRANSFER_IN_DOMAIN",
            "UPDATE_DOMAIN_CONTACT",
            "UPDATE_NAMESERVER",
            "CHANGE_PRIVACY_PROTECTION",
            "DOMAIN_LOCK",
            "ENABLE_AUTORENEW",
            "DISABLE_AUTORENEW",
            "ADD_DNSSEC",
            "REMOVE_DNSSEC",
            "EXPIRE_DOMAIN",
            "TRANSFER_OUT_DOMAIN",
            "CHANGE_DOMAIN_OWNER",
            "RENEW_DOMAIN",
            "PUSH_DOMAIN",
        ],
        "InvoiceId": str,
        "BillDate": datetime,
        "Price": float,
    },
    total=False,
)


class ViewBillingPaginateResponseBillingRecordsTypeDef(
    _ViewBillingPaginateResponseBillingRecordsTypeDef
):
    """
    - *(dict) --*

      Information for one billing record.
      - **DomainName** *(string) --*

        The name of the domain that the billing record applies to. If the domain name contains
        characters other than a-z, 0-9, and - (hyphen), such as an internationalized domain name,
        then this value is in Punycode. For more information, see `DNS Domain Name Format
        <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in the
        *Amazon Route 53 Developer Guidezzz* .
    """


_ViewBillingPaginateResponseTypeDef = TypedDict(
    "_ViewBillingPaginateResponseTypeDef",
    {"BillingRecords": List[ViewBillingPaginateResponseBillingRecordsTypeDef], "NextToken": str},
    total=False,
)


class ViewBillingPaginateResponseTypeDef(_ViewBillingPaginateResponseTypeDef):
    """
    - *(dict) --*

      The ViewBilling response includes the following elements.
      - **BillingRecords** *(list) --*

        A summary of billing records.
        - *(dict) --*

          Information for one billing record.
          - **DomainName** *(string) --*

            The name of the domain that the billing record applies to. If the domain name contains
            characters other than a-z, 0-9, and - (hyphen), such as an internationalized domain
            name, then this value is in Punycode. For more information, see `DNS Domain Name Format
            <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in
            the *Amazon Route 53 Developer Guidezzz* .
    """
