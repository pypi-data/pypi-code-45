"Main interface for waf-regional service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    "ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    "ClientCreateByteMatchSetResponseByteMatchSetTypeDef",
    "ClientCreateByteMatchSetResponseTypeDef",
    "ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    "ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef",
    "ClientCreateGeoMatchSetResponseTypeDef",
    "ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef",
    "ClientCreateIpSetResponseIPSetTypeDef",
    "ClientCreateIpSetResponseTypeDef",
    "ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    "ClientCreateRateBasedRuleResponseRuleTypeDef",
    "ClientCreateRateBasedRuleResponseTypeDef",
    "ClientCreateRateBasedRuleTagsTypeDef",
    "ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    "ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    "ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef",
    "ClientCreateRegexMatchSetResponseTypeDef",
    "ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef",
    "ClientCreateRegexPatternSetResponseTypeDef",
    "ClientCreateRuleGroupResponseRuleGroupTypeDef",
    "ClientCreateRuleGroupResponseTypeDef",
    "ClientCreateRuleGroupTagsTypeDef",
    "ClientCreateRuleResponseRulePredicatesTypeDef",
    "ClientCreateRuleResponseRuleTypeDef",
    "ClientCreateRuleResponseTypeDef",
    "ClientCreateRuleTagsTypeDef",
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    "ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef",
    "ClientCreateSizeConstraintSetResponseTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    "ClientCreateSqlInjectionMatchSetResponseTypeDef",
    "ClientCreateWebAclDefaultActionTypeDef",
    "ClientCreateWebAclResponseWebACLDefaultActionTypeDef",
    "ClientCreateWebAclResponseWebACLRulesActionTypeDef",
    "ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef",
    "ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef",
    "ClientCreateWebAclResponseWebACLRulesTypeDef",
    "ClientCreateWebAclResponseWebACLTypeDef",
    "ClientCreateWebAclResponseTypeDef",
    "ClientCreateWebAclTagsTypeDef",
    "ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    "ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    "ClientCreateXssMatchSetResponseXssMatchSetTypeDef",
    "ClientCreateXssMatchSetResponseTypeDef",
    "ClientDeleteByteMatchSetResponseTypeDef",
    "ClientDeleteGeoMatchSetResponseTypeDef",
    "ClientDeleteIpSetResponseTypeDef",
    "ClientDeleteRateBasedRuleResponseTypeDef",
    "ClientDeleteRegexMatchSetResponseTypeDef",
    "ClientDeleteRegexPatternSetResponseTypeDef",
    "ClientDeleteRuleGroupResponseTypeDef",
    "ClientDeleteRuleResponseTypeDef",
    "ClientDeleteSizeConstraintSetResponseTypeDef",
    "ClientDeleteSqlInjectionMatchSetResponseTypeDef",
    "ClientDeleteWebAclResponseTypeDef",
    "ClientDeleteXssMatchSetResponseTypeDef",
    "ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    "ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    "ClientGetByteMatchSetResponseByteMatchSetTypeDef",
    "ClientGetByteMatchSetResponseTypeDef",
    "ClientGetChangeTokenResponseTypeDef",
    "ClientGetChangeTokenStatusResponseTypeDef",
    "ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    "ClientGetGeoMatchSetResponseGeoMatchSetTypeDef",
    "ClientGetGeoMatchSetResponseTypeDef",
    "ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef",
    "ClientGetIpSetResponseIPSetTypeDef",
    "ClientGetIpSetResponseTypeDef",
    "ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    "ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientGetLoggingConfigurationResponseTypeDef",
    "ClientGetPermissionPolicyResponseTypeDef",
    "ClientGetRateBasedRuleManagedKeysResponseTypeDef",
    "ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    "ClientGetRateBasedRuleResponseRuleTypeDef",
    "ClientGetRateBasedRuleResponseTypeDef",
    "ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    "ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    "ClientGetRegexMatchSetResponseRegexMatchSetTypeDef",
    "ClientGetRegexMatchSetResponseTypeDef",
    "ClientGetRegexPatternSetResponseRegexPatternSetTypeDef",
    "ClientGetRegexPatternSetResponseTypeDef",
    "ClientGetRuleGroupResponseRuleGroupTypeDef",
    "ClientGetRuleGroupResponseTypeDef",
    "ClientGetRuleResponseRulePredicatesTypeDef",
    "ClientGetRuleResponseRuleTypeDef",
    "ClientGetRuleResponseTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef",
    "ClientGetSampledRequestsResponseSampledRequestsTypeDef",
    "ClientGetSampledRequestsResponseTimeWindowTypeDef",
    "ClientGetSampledRequestsResponseTypeDef",
    "ClientGetSampledRequestsTimeWindowTypeDef",
    "ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    "ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    "ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef",
    "ClientGetSizeConstraintSetResponseTypeDef",
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    "ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    "ClientGetSqlInjectionMatchSetResponseTypeDef",
    "ClientGetWebAclForResourceResponseWebACLSummaryTypeDef",
    "ClientGetWebAclForResourceResponseTypeDef",
    "ClientGetWebAclResponseWebACLDefaultActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef",
    "ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef",
    "ClientGetWebAclResponseWebACLRulesTypeDef",
    "ClientGetWebAclResponseWebACLTypeDef",
    "ClientGetWebAclResponseTypeDef",
    "ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    "ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    "ClientGetXssMatchSetResponseXssMatchSetTypeDef",
    "ClientGetXssMatchSetResponseTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef",
    "ClientListActivatedRulesInRuleGroupResponseTypeDef",
    "ClientListByteMatchSetsResponseByteMatchSetsTypeDef",
    "ClientListByteMatchSetsResponseTypeDef",
    "ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef",
    "ClientListGeoMatchSetsResponseTypeDef",
    "ClientListIpSetsResponseIPSetsTypeDef",
    "ClientListIpSetsResponseTypeDef",
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef",
    "ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef",
    "ClientListLoggingConfigurationsResponseTypeDef",
    "ClientListRateBasedRulesResponseRulesTypeDef",
    "ClientListRateBasedRulesResponseTypeDef",
    "ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef",
    "ClientListRegexMatchSetsResponseTypeDef",
    "ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef",
    "ClientListRegexPatternSetsResponseTypeDef",
    "ClientListResourcesForWebAclResponseTypeDef",
    "ClientListRuleGroupsResponseRuleGroupsTypeDef",
    "ClientListRuleGroupsResponseTypeDef",
    "ClientListRulesResponseRulesTypeDef",
    "ClientListRulesResponseTypeDef",
    "ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef",
    "ClientListSizeConstraintSetsResponseTypeDef",
    "ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef",
    "ClientListSqlInjectionMatchSetsResponseTypeDef",
    "ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef",
    "ClientListSubscribedRuleGroupsResponseTypeDef",
    "ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef",
    "ClientListTagsForResourceResponseTagInfoForResourceTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListWebAclsResponseWebACLsTypeDef",
    "ClientListWebAclsResponseTypeDef",
    "ClientListXssMatchSetsResponseXssMatchSetsTypeDef",
    "ClientListXssMatchSetsResponseTypeDef",
    "ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef",
    "ClientPutLoggingConfigurationLoggingConfigurationTypeDef",
    "ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    "ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef",
    "ClientPutLoggingConfigurationResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateByteMatchSetResponseTypeDef",
    "ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef",
    "ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef",
    "ClientUpdateByteMatchSetUpdatesTypeDef",
    "ClientUpdateGeoMatchSetResponseTypeDef",
    "ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef",
    "ClientUpdateGeoMatchSetUpdatesTypeDef",
    "ClientUpdateIpSetResponseTypeDef",
    "ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef",
    "ClientUpdateIpSetUpdatesTypeDef",
    "ClientUpdateRateBasedRuleResponseTypeDef",
    "ClientUpdateRateBasedRuleUpdatesPredicateTypeDef",
    "ClientUpdateRateBasedRuleUpdatesTypeDef",
    "ClientUpdateRegexMatchSetResponseTypeDef",
    "ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef",
    "ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef",
    "ClientUpdateRegexMatchSetUpdatesTypeDef",
    "ClientUpdateRegexPatternSetResponseTypeDef",
    "ClientUpdateRegexPatternSetUpdatesTypeDef",
    "ClientUpdateRuleGroupResponseTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef",
    "ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef",
    "ClientUpdateRuleGroupUpdatesTypeDef",
    "ClientUpdateRuleResponseTypeDef",
    "ClientUpdateRuleUpdatesPredicateTypeDef",
    "ClientUpdateRuleUpdatesTypeDef",
    "ClientUpdateSizeConstraintSetResponseTypeDef",
    "ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef",
    "ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef",
    "ClientUpdateSizeConstraintSetUpdatesTypeDef",
    "ClientUpdateSqlInjectionMatchSetResponseTypeDef",
    "ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef",
    "ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef",
    "ClientUpdateSqlInjectionMatchSetUpdatesTypeDef",
    "ClientUpdateWebAclDefaultActionTypeDef",
    "ClientUpdateWebAclResponseTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef",
    "ClientUpdateWebAclUpdatesActivatedRuleTypeDef",
    "ClientUpdateWebAclUpdatesTypeDef",
    "ClientUpdateXssMatchSetResponseTypeDef",
    "ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef",
    "ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef",
    "ClientUpdateXssMatchSetUpdatesTypeDef",
)


_ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef(
    _ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef
):
    pass


_ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef = TypedDict(
    "_ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef,
        "TargetString": bytes,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)


class ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef(
    _ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef
):
    pass


_ClientCreateByteMatchSetResponseByteMatchSetTypeDef = TypedDict(
    "_ClientCreateByteMatchSetResponseByteMatchSetTypeDef",
    {
        "ByteMatchSetId": str,
        "Name": str,
        "ByteMatchTuples": List[ClientCreateByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef],
    },
    total=False,
)


class ClientCreateByteMatchSetResponseByteMatchSetTypeDef(
    _ClientCreateByteMatchSetResponseByteMatchSetTypeDef
):
    """
    - **ByteMatchSet** *(dict) --*

      A  ByteMatchSet that contains no ``ByteMatchTuple`` objects.
      - **ByteMatchSetId** *(string) --*

        The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
        information about a ``ByteMatchSet`` (see  GetByteMatchSet ), update a ``ByteMatchSet`` (see
        UpdateByteMatchSet ), insert a ``ByteMatchSet`` into a ``Rule`` or delete one from a
        ``Rule`` (see  UpdateRule ), and delete a ``ByteMatchSet`` from AWS WAF (see
        DeleteByteMatchSet ).

          ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .
    """


_ClientCreateByteMatchSetResponseTypeDef = TypedDict(
    "_ClientCreateByteMatchSetResponseTypeDef",
    {"ByteMatchSet": ClientCreateByteMatchSetResponseByteMatchSetTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateByteMatchSetResponseTypeDef(_ClientCreateByteMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **ByteMatchSet** *(dict) --*

        A  ByteMatchSet that contains no ``ByteMatchTuple`` objects.
        - **ByteMatchSetId** *(string) --*

          The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
          information about a ``ByteMatchSet`` (see  GetByteMatchSet ), update a ``ByteMatchSet``
          (see  UpdateByteMatchSet ), insert a ``ByteMatchSet`` into a ``Rule`` or delete one from a
          ``Rule`` (see  UpdateRule ), and delete a ``ByteMatchSet`` from AWS WAF (see
          DeleteByteMatchSet ).

            ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .
    """


_ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef = TypedDict(
    "_ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    {
        "Type": str,
        "Value": Literal[
            "AF",
            "AX",
            "AL",
            "DZ",
            "AS",
            "AD",
            "AO",
            "AI",
            "AQ",
            "AG",
            "AR",
            "AM",
            "AW",
            "AU",
            "AT",
            "AZ",
            "BS",
            "BH",
            "BD",
            "BB",
            "BY",
            "BE",
            "BZ",
            "BJ",
            "BM",
            "BT",
            "BO",
            "BQ",
            "BA",
            "BW",
            "BV",
            "BR",
            "IO",
            "BN",
            "BG",
            "BF",
            "BI",
            "KH",
            "CM",
            "CA",
            "CV",
            "KY",
            "CF",
            "TD",
            "CL",
            "CN",
            "CX",
            "CC",
            "CO",
            "KM",
            "CG",
            "CD",
            "CK",
            "CR",
            "CI",
            "HR",
            "CU",
            "CW",
            "CY",
            "CZ",
            "DK",
            "DJ",
            "DM",
            "DO",
            "EC",
            "EG",
            "SV",
            "GQ",
            "ER",
            "EE",
            "ET",
            "FK",
            "FO",
            "FJ",
            "FI",
            "FR",
            "GF",
            "PF",
            "TF",
            "GA",
            "GM",
            "GE",
            "DE",
            "GH",
            "GI",
            "GR",
            "GL",
            "GD",
            "GP",
            "GU",
            "GT",
            "GG",
            "GN",
            "GW",
            "GY",
            "HT",
            "HM",
            "VA",
            "HN",
            "HK",
            "HU",
            "IS",
            "IN",
            "ID",
            "IR",
            "IQ",
            "IE",
            "IM",
            "IL",
            "IT",
            "JM",
            "JP",
            "JE",
            "JO",
            "KZ",
            "KE",
            "KI",
            "KP",
            "KR",
            "KW",
            "KG",
            "LA",
            "LV",
            "LB",
            "LS",
            "LR",
            "LY",
            "LI",
            "LT",
            "LU",
            "MO",
            "MK",
            "MG",
            "MW",
            "MY",
            "MV",
            "ML",
            "MT",
            "MH",
            "MQ",
            "MR",
            "MU",
            "YT",
            "MX",
            "FM",
            "MD",
            "MC",
            "MN",
            "ME",
            "MS",
            "MA",
            "MZ",
            "MM",
            "NA",
            "NR",
            "NP",
            "NL",
            "NC",
            "NZ",
            "NI",
            "NE",
            "NG",
            "NU",
            "NF",
            "MP",
            "NO",
            "OM",
            "PK",
            "PW",
            "PS",
            "PA",
            "PG",
            "PY",
            "PE",
            "PH",
            "PN",
            "PL",
            "PT",
            "PR",
            "QA",
            "RE",
            "RO",
            "RU",
            "RW",
            "BL",
            "SH",
            "KN",
            "LC",
            "MF",
            "PM",
            "VC",
            "WS",
            "SM",
            "ST",
            "SA",
            "SN",
            "RS",
            "SC",
            "SL",
            "SG",
            "SX",
            "SK",
            "SI",
            "SB",
            "SO",
            "ZA",
            "GS",
            "SS",
            "ES",
            "LK",
            "SD",
            "SR",
            "SJ",
            "SZ",
            "SE",
            "CH",
            "SY",
            "TW",
            "TJ",
            "TZ",
            "TH",
            "TL",
            "TG",
            "TK",
            "TO",
            "TT",
            "TN",
            "TR",
            "TM",
            "TC",
            "TV",
            "UG",
            "UA",
            "AE",
            "GB",
            "US",
            "UM",
            "UY",
            "UZ",
            "VU",
            "VE",
            "VN",
            "VG",
            "VI",
            "WF",
            "EH",
            "YE",
            "ZM",
            "ZW",
        ],
    },
    total=False,
)


class ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef(
    _ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef
):
    pass


_ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef = TypedDict(
    "_ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef",
    {
        "GeoMatchSetId": str,
        "Name": str,
        "GeoMatchConstraints": List[
            ClientCreateGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef
        ],
    },
    total=False,
)


class ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef(
    _ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef
):
    """
    - **GeoMatchSet** *(dict) --*

      The  GeoMatchSet returned in the ``CreateGeoMatchSet`` response. The ``GeoMatchSet`` contains
      no ``GeoMatchConstraints`` .
      - **GeoMatchSetId** *(string) --*

        The ``GeoMatchSetId`` for an ``GeoMatchSet`` . You use ``GeoMatchSetId`` to get information
        about a ``GeoMatchSet`` (see  GeoMatchSet ), update a ``GeoMatchSet`` (see
        UpdateGeoMatchSet ), insert a ``GeoMatchSet`` into a ``Rule`` or delete one from a ``Rule``
        (see  UpdateRule ), and delete a ``GeoMatchSet`` from AWS WAF (see  DeleteGeoMatchSet ).

          ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .
    """


_ClientCreateGeoMatchSetResponseTypeDef = TypedDict(
    "_ClientCreateGeoMatchSetResponseTypeDef",
    {"GeoMatchSet": ClientCreateGeoMatchSetResponseGeoMatchSetTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateGeoMatchSetResponseTypeDef(_ClientCreateGeoMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **GeoMatchSet** *(dict) --*

        The  GeoMatchSet returned in the ``CreateGeoMatchSet`` response. The ``GeoMatchSet``
        contains no ``GeoMatchConstraints`` .
        - **GeoMatchSetId** *(string) --*

          The ``GeoMatchSetId`` for an ``GeoMatchSet`` . You use ``GeoMatchSetId`` to get
          information about a ``GeoMatchSet`` (see  GeoMatchSet ), update a ``GeoMatchSet`` (see
          UpdateGeoMatchSet ), insert a ``GeoMatchSet`` into a ``Rule`` or delete one from a
          ``Rule`` (see  UpdateRule ), and delete a ``GeoMatchSet`` from AWS WAF (see
          DeleteGeoMatchSet ).

            ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .
    """


_ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef = TypedDict(
    "_ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef",
    {"Type": Literal["IPV4", "IPV6"], "Value": str},
    total=False,
)


class ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef(
    _ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef
):
    pass


_ClientCreateIpSetResponseIPSetTypeDef = TypedDict(
    "_ClientCreateIpSetResponseIPSetTypeDef",
    {
        "IPSetId": str,
        "Name": str,
        "IPSetDescriptors": List[ClientCreateIpSetResponseIPSetIPSetDescriptorsTypeDef],
    },
    total=False,
)


class ClientCreateIpSetResponseIPSetTypeDef(_ClientCreateIpSetResponseIPSetTypeDef):
    """
    - **IPSet** *(dict) --*

      The  IPSet returned in the ``CreateIPSet`` response.
      - **IPSetId** *(string) --*

        The ``IPSetId`` for an ``IPSet`` . You use ``IPSetId`` to get information about an ``IPSet``
        (see  GetIPSet ), update an ``IPSet`` (see  UpdateIPSet ), insert an ``IPSet`` into a
        ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``IPSet`` from AWS
        WAF (see  DeleteIPSet ).

          ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .
    """


_ClientCreateIpSetResponseTypeDef = TypedDict(
    "_ClientCreateIpSetResponseTypeDef",
    {"IPSet": ClientCreateIpSetResponseIPSetTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateIpSetResponseTypeDef(_ClientCreateIpSetResponseTypeDef):
    """
    - *(dict) --*

      - **IPSet** *(dict) --*

        The  IPSet returned in the ``CreateIPSet`` response.
        - **IPSetId** *(string) --*

          The ``IPSetId`` for an ``IPSet`` . You use ``IPSetId`` to get information about an
          ``IPSet`` (see  GetIPSet ), update an ``IPSet`` (see  UpdateIPSet ), insert an ``IPSet``
          into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``IPSet``
          from AWS WAF (see  DeleteIPSet ).

            ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .
    """


_ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef = TypedDict(
    "_ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)


class ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef(
    _ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef
):
    pass


_ClientCreateRateBasedRuleResponseRuleTypeDef = TypedDict(
    "_ClientCreateRateBasedRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "MatchPredicates": List[ClientCreateRateBasedRuleResponseRuleMatchPredicatesTypeDef],
        "RateKey": str,
        "RateLimit": int,
    },
    total=False,
)


class ClientCreateRateBasedRuleResponseRuleTypeDef(_ClientCreateRateBasedRuleResponseRuleTypeDef):
    """
    - **Rule** *(dict) --*

      The  RateBasedRule that is returned in the ``CreateRateBasedRule`` response.
      - **RuleId** *(string) --*

        A unique identifier for a ``RateBasedRule`` . You use ``RuleId`` to get more information
        about a ``RateBasedRule`` (see  GetRateBasedRule ), update a ``RateBasedRule`` (see
        UpdateRateBasedRule ), insert a ``RateBasedRule`` into a ``WebACL`` or delete one from a
        ``WebACL`` (see  UpdateWebACL ), or delete a ``RateBasedRule`` from AWS WAF (see
        DeleteRateBasedRule ).
    """


_ClientCreateRateBasedRuleResponseTypeDef = TypedDict(
    "_ClientCreateRateBasedRuleResponseTypeDef",
    {"Rule": ClientCreateRateBasedRuleResponseRuleTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateRateBasedRuleResponseTypeDef(_ClientCreateRateBasedRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Rule** *(dict) --*

        The  RateBasedRule that is returned in the ``CreateRateBasedRule`` response.
        - **RuleId** *(string) --*

          A unique identifier for a ``RateBasedRule`` . You use ``RuleId`` to get more information
          about a ``RateBasedRule`` (see  GetRateBasedRule ), update a ``RateBasedRule`` (see
          UpdateRateBasedRule ), insert a ``RateBasedRule`` into a ``WebACL`` or delete one from a
          ``WebACL`` (see  UpdateWebACL ), or delete a ``RateBasedRule`` from AWS WAF (see
          DeleteRateBasedRule ).
    """


_ClientCreateRateBasedRuleTagsTypeDef = TypedDict(
    "_ClientCreateRateBasedRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRateBasedRuleTagsTypeDef(_ClientCreateRateBasedRuleTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*
      - **Value** *(string) --*
    """


_ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef(
    _ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef
):
    pass


_ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef = TypedDict(
    "_ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "RegexPatternSetId": str,
    },
    total=False,
)


class ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef(
    _ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef
):
    pass


_ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef = TypedDict(
    "_ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
        "RegexMatchTuples": List[
            ClientCreateRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef(
    _ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef
):
    """
    - **RegexMatchSet** *(dict) --*

      A  RegexMatchSet that contains no ``RegexMatchTuple`` objects.
      - **RegexMatchSetId** *(string) --*

        The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
        information about a ``RegexMatchSet`` (see  GetRegexMatchSet ), update a ``RegexMatchSet``
        (see  UpdateRegexMatchSet ), insert a ``RegexMatchSet`` into a ``Rule`` or delete one from a
        ``Rule`` (see  UpdateRule ), and delete a ``RegexMatchSet`` from AWS WAF (see
        DeleteRegexMatchSet ).

          ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .
    """


_ClientCreateRegexMatchSetResponseTypeDef = TypedDict(
    "_ClientCreateRegexMatchSetResponseTypeDef",
    {"RegexMatchSet": ClientCreateRegexMatchSetResponseRegexMatchSetTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateRegexMatchSetResponseTypeDef(_ClientCreateRegexMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **RegexMatchSet** *(dict) --*

        A  RegexMatchSet that contains no ``RegexMatchTuple`` objects.
        - **RegexMatchSetId** *(string) --*

          The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
          information about a ``RegexMatchSet`` (see  GetRegexMatchSet ), update a ``RegexMatchSet``
          (see  UpdateRegexMatchSet ), insert a ``RegexMatchSet`` into a ``Rule`` or delete one from
          a ``Rule`` (see  UpdateRule ), and delete a ``RegexMatchSet`` from AWS WAF (see
          DeleteRegexMatchSet ).

            ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .
    """


_ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef = TypedDict(
    "_ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef",
    {"RegexPatternSetId": str, "Name": str, "RegexPatternStrings": List[str]},
    total=False,
)


class ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef(
    _ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef
):
    """
    - **RegexPatternSet** *(dict) --*

      A  RegexPatternSet that contains no objects.
      - **RegexPatternSetId** *(string) --*

        The identifier for the ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get
        information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
        ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
        WAF.

          ``RegexMatchSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .
    """


_ClientCreateRegexPatternSetResponseTypeDef = TypedDict(
    "_ClientCreateRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": ClientCreateRegexPatternSetResponseRegexPatternSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)


class ClientCreateRegexPatternSetResponseTypeDef(_ClientCreateRegexPatternSetResponseTypeDef):
    """
    - *(dict) --*

      - **RegexPatternSet** *(dict) --*

        A  RegexPatternSet that contains no objects.
        - **RegexPatternSetId** *(string) --*

          The identifier for the ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get
          information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
          ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
          WAF.

            ``RegexMatchSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .
    """


_ClientCreateRuleGroupResponseRuleGroupTypeDef = TypedDict(
    "_ClientCreateRuleGroupResponseRuleGroupTypeDef",
    {"RuleGroupId": str, "Name": str, "MetricName": str},
    total=False,
)


class ClientCreateRuleGroupResponseRuleGroupTypeDef(_ClientCreateRuleGroupResponseRuleGroupTypeDef):
    """
    - **RuleGroup** *(dict) --*

      An empty  RuleGroup .
      - **RuleGroupId** *(string) --*

        A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
        about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup ),
        insert a ``RuleGroup`` into a ``WebACL`` or delete a one from a ``WebACL`` (see
        UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

          ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .
    """


_ClientCreateRuleGroupResponseTypeDef = TypedDict(
    "_ClientCreateRuleGroupResponseTypeDef",
    {"RuleGroup": ClientCreateRuleGroupResponseRuleGroupTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateRuleGroupResponseTypeDef(_ClientCreateRuleGroupResponseTypeDef):
    """
    - *(dict) --*

      - **RuleGroup** *(dict) --*

        An empty  RuleGroup .
        - **RuleGroupId** *(string) --*

          A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
          about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup
          ), insert a ``RuleGroup`` into a ``WebACL`` or delete a one from a ``WebACL`` (see
          UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

            ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .
    """


_ClientCreateRuleGroupTagsTypeDef = TypedDict(
    "_ClientCreateRuleGroupTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRuleGroupTagsTypeDef(_ClientCreateRuleGroupTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*
      - **Value** *(string) --*
    """


_ClientCreateRuleResponseRulePredicatesTypeDef = TypedDict(
    "_ClientCreateRuleResponseRulePredicatesTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)


class ClientCreateRuleResponseRulePredicatesTypeDef(_ClientCreateRuleResponseRulePredicatesTypeDef):
    pass


_ClientCreateRuleResponseRuleTypeDef = TypedDict(
    "_ClientCreateRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "Predicates": List[ClientCreateRuleResponseRulePredicatesTypeDef],
    },
    total=False,
)


class ClientCreateRuleResponseRuleTypeDef(_ClientCreateRuleResponseRuleTypeDef):
    """
    - **Rule** *(dict) --*

      The  Rule returned in the ``CreateRule`` response.
      - **RuleId** *(string) --*

        A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
        ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
        ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from
        AWS WAF (see  DeleteRule ).

          ``RuleId`` is returned by  CreateRule and by  ListRules .
    """


_ClientCreateRuleResponseTypeDef = TypedDict(
    "_ClientCreateRuleResponseTypeDef",
    {"Rule": ClientCreateRuleResponseRuleTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateRuleResponseTypeDef(_ClientCreateRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Rule** *(dict) --*

        The  Rule returned in the ``CreateRule`` response.
        - **RuleId** *(string) --*

          A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
          ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
          ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
          from AWS WAF (see  DeleteRule ).

            ``RuleId`` is returned by  CreateRule and by  ListRules .
    """


_ClientCreateRuleTagsTypeDef = TypedDict(
    "_ClientCreateRuleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateRuleTagsTypeDef(_ClientCreateRuleTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*
      - **Value** *(string) --*
    """


_ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef = TypedDict(
    "_ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef(
    _ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef
):
    pass


_ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef = TypedDict(
    "_ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    {
        "FieldToMatch": ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
    },
    total=False,
)


class ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef(
    _ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef
):
    pass


_ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef = TypedDict(
    "_ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef",
    {
        "SizeConstraintSetId": str,
        "Name": str,
        "SizeConstraints": List[
            ClientCreateSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef
        ],
    },
    total=False,
)


class ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef(
    _ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef
):
    """
    - **SizeConstraintSet** *(dict) --*

      A  SizeConstraintSet that contains no ``SizeConstraint`` objects.
      - **SizeConstraintSetId** *(string) --*

        A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
        information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
        ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into a
        ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
        ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

          ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
          ListSizeConstraintSets .
    """


_ClientCreateSizeConstraintSetResponseTypeDef = TypedDict(
    "_ClientCreateSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": ClientCreateSizeConstraintSetResponseSizeConstraintSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)


class ClientCreateSizeConstraintSetResponseTypeDef(_ClientCreateSizeConstraintSetResponseTypeDef):
    """
    - *(dict) --*

      - **SizeConstraintSet** *(dict) --*

        A  SizeConstraintSet that contains no ``SizeConstraint`` objects.
        - **SizeConstraintSetId** *(string) --*

          A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
          information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
          ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into
          a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
          ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

            ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
            ListSizeConstraintSets .
    """


_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef(
    _ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef
):
    pass


_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef = TypedDict(
    "_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)


class ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef(
    _ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef
):
    pass


_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef = TypedDict(
    "_ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "Name": str,
        "SqlInjectionMatchTuples": List[
            ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef(
    _ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef
):
    """
    - **SqlInjectionMatchSet** *(dict) --*

      A  SqlInjectionMatchSet .
      - **SqlInjectionMatchSetId** *(string) --*

        A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to
        get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a
        ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
        ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ),
        and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

          ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
          ListSqlInjectionMatchSets .
    """


_ClientCreateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "_ClientCreateSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": ClientCreateSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef,
        "ChangeToken": str,
    },
    total=False,
)


class ClientCreateSqlInjectionMatchSetResponseTypeDef(
    _ClientCreateSqlInjectionMatchSetResponseTypeDef
):
    """
    - *(dict) --*

      The response to a ``CreateSqlInjectionMatchSet`` request.
      - **SqlInjectionMatchSet** *(dict) --*

        A  SqlInjectionMatchSet .
        - **SqlInjectionMatchSetId** *(string) --*

          A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to
          get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a
          ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
          ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ),
          and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

            ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
            ListSqlInjectionMatchSets .
    """


_ClientCreateWebAclDefaultActionTypeDef = TypedDict(
    "_ClientCreateWebAclDefaultActionTypeDef", {"Type": Literal["BLOCK", "ALLOW", "COUNT"]}
)


class ClientCreateWebAclDefaultActionTypeDef(_ClientCreateWebAclDefaultActionTypeDef):
    """
    The action that you want AWS WAF to take when a request doesn't match the criteria specified in
    any of the ``Rule`` objects that are associated with the ``WebACL`` .
    - **Type** *(string) --***[REQUIRED]**

      Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` .
      Valid settings include the following:
      * ``ALLOW`` : AWS WAF allows requests
      * ``BLOCK`` : AWS WAF blocks requests
      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in
      the rule. AWS WAF then continues to inspect the web request based on the remaining rules in
      the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` .
    """


_ClientCreateWebAclResponseWebACLDefaultActionTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLDefaultActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)


class ClientCreateWebAclResponseWebACLDefaultActionTypeDef(
    _ClientCreateWebAclResponseWebACLDefaultActionTypeDef
):
    pass


_ClientCreateWebAclResponseWebACLRulesActionTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLRulesActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)


class ClientCreateWebAclResponseWebACLRulesActionTypeDef(
    _ClientCreateWebAclResponseWebACLRulesActionTypeDef
):
    pass


_ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef", {"RuleId": str}, total=False
)


class ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef(
    _ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef
):
    pass


_ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef",
    {"Type": Literal["NONE", "COUNT"]},
    total=False,
)


class ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef(
    _ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef
):
    pass


_ClientCreateWebAclResponseWebACLRulesTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLRulesTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientCreateWebAclResponseWebACLRulesActionTypeDef,
        "OverrideAction": ClientCreateWebAclResponseWebACLRulesOverrideActionTypeDef,
        "Type": Literal["REGULAR", "RATE_BASED", "GROUP"],
        "ExcludedRules": List[ClientCreateWebAclResponseWebACLRulesExcludedRulesTypeDef],
    },
    total=False,
)


class ClientCreateWebAclResponseWebACLRulesTypeDef(_ClientCreateWebAclResponseWebACLRulesTypeDef):
    pass


_ClientCreateWebAclResponseWebACLTypeDef = TypedDict(
    "_ClientCreateWebAclResponseWebACLTypeDef",
    {
        "WebACLId": str,
        "Name": str,
        "MetricName": str,
        "DefaultAction": ClientCreateWebAclResponseWebACLDefaultActionTypeDef,
        "Rules": List[ClientCreateWebAclResponseWebACLRulesTypeDef],
        "WebACLArn": str,
    },
    total=False,
)


class ClientCreateWebAclResponseWebACLTypeDef(_ClientCreateWebAclResponseWebACLTypeDef):
    """
    - **WebACL** *(dict) --*

      The  WebACL returned in the ``CreateWebACL`` response.
      - **WebACLId** *(string) --*

        A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
        ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
        ``WebACL`` from AWS WAF (see  DeleteWebACL ).

          ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .
    """


_ClientCreateWebAclResponseTypeDef = TypedDict(
    "_ClientCreateWebAclResponseTypeDef",
    {"WebACL": ClientCreateWebAclResponseWebACLTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateWebAclResponseTypeDef(_ClientCreateWebAclResponseTypeDef):
    """
    - *(dict) --*

      - **WebACL** *(dict) --*

        The  WebACL returned in the ``CreateWebACL`` response.
        - **WebACLId** *(string) --*

          A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
          ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
          ``WebACL`` from AWS WAF (see  DeleteWebACL ).

            ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .
    """


_ClientCreateWebAclTagsTypeDef = TypedDict(
    "_ClientCreateWebAclTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateWebAclTagsTypeDef(_ClientCreateWebAclTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*
      - **Value** *(string) --*
    """


_ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef(
    _ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef
):
    pass


_ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef = TypedDict(
    "_ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)


class ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef(
    _ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef
):
    pass


_ClientCreateXssMatchSetResponseXssMatchSetTypeDef = TypedDict(
    "_ClientCreateXssMatchSetResponseXssMatchSetTypeDef",
    {
        "XssMatchSetId": str,
        "Name": str,
        "XssMatchTuples": List[ClientCreateXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef],
    },
    total=False,
)


class ClientCreateXssMatchSetResponseXssMatchSetTypeDef(
    _ClientCreateXssMatchSetResponseXssMatchSetTypeDef
):
    """
    - **XssMatchSet** *(dict) --*

      An  XssMatchSet .
      - **XssMatchSetId** *(string) --*

        A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
        about an ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
        UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a ``Rule``
        (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see  DeleteXssMatchSet ).

          ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .
    """


_ClientCreateXssMatchSetResponseTypeDef = TypedDict(
    "_ClientCreateXssMatchSetResponseTypeDef",
    {"XssMatchSet": ClientCreateXssMatchSetResponseXssMatchSetTypeDef, "ChangeToken": str},
    total=False,
)


class ClientCreateXssMatchSetResponseTypeDef(_ClientCreateXssMatchSetResponseTypeDef):
    """
    - *(dict) --*

      The response to a ``CreateXssMatchSet`` request.
      - **XssMatchSet** *(dict) --*

        An  XssMatchSet .
        - **XssMatchSetId** *(string) --*

          A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
          about an ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
          UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a
          ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see
          DeleteXssMatchSet ).

            ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .
    """


_ClientDeleteByteMatchSetResponseTypeDef = TypedDict(
    "_ClientDeleteByteMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteByteMatchSetResponseTypeDef(_ClientDeleteByteMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteByteMatchSet`` request. You can also
        use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteGeoMatchSetResponseTypeDef = TypedDict(
    "_ClientDeleteGeoMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteGeoMatchSetResponseTypeDef(_ClientDeleteGeoMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteGeoMatchSet`` request. You can also
        use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteIpSetResponseTypeDef = TypedDict(
    "_ClientDeleteIpSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteIpSetResponseTypeDef(_ClientDeleteIpSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteIPSet`` request. You can also use
        this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteRateBasedRuleResponseTypeDef = TypedDict(
    "_ClientDeleteRateBasedRuleResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteRateBasedRuleResponseTypeDef(_ClientDeleteRateBasedRuleResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteRateBasedRule`` request. You can
        also use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteRegexMatchSetResponseTypeDef = TypedDict(
    "_ClientDeleteRegexMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteRegexMatchSetResponseTypeDef(_ClientDeleteRegexMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteRegexMatchSet`` request. You can
        also use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteRegexPatternSetResponseTypeDef = TypedDict(
    "_ClientDeleteRegexPatternSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteRegexPatternSetResponseTypeDef(_ClientDeleteRegexPatternSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteRegexPatternSet`` request. You can
        also use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteRuleGroupResponseTypeDef = TypedDict(
    "_ClientDeleteRuleGroupResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteRuleGroupResponseTypeDef(_ClientDeleteRuleGroupResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteRuleGroup`` request. You can also
        use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteRuleResponseTypeDef = TypedDict(
    "_ClientDeleteRuleResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteRuleResponseTypeDef(_ClientDeleteRuleResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteRule`` request. You can also use
        this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteSizeConstraintSetResponseTypeDef = TypedDict(
    "_ClientDeleteSizeConstraintSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteSizeConstraintSetResponseTypeDef(_ClientDeleteSizeConstraintSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteSizeConstraintSet`` request. You can
        also use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "_ClientDeleteSqlInjectionMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteSqlInjectionMatchSetResponseTypeDef(
    _ClientDeleteSqlInjectionMatchSetResponseTypeDef
):
    """
    - *(dict) --*

      The response to a request to delete a  SqlInjectionMatchSet from AWS WAF.
      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteSqlInjectionMatchSet`` request. You
        can also use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteWebAclResponseTypeDef = TypedDict(
    "_ClientDeleteWebAclResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteWebAclResponseTypeDef(_ClientDeleteWebAclResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteWebACL`` request. You can also use
        this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientDeleteXssMatchSetResponseTypeDef = TypedDict(
    "_ClientDeleteXssMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientDeleteXssMatchSetResponseTypeDef(_ClientDeleteXssMatchSetResponseTypeDef):
    """
    - *(dict) --*

      The response to a request to delete an  XssMatchSet from AWS WAF.
      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``DeleteXssMatchSet`` request. You can also
        use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef(
    _ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef
):
    pass


_ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef = TypedDict(
    "_ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesFieldToMatchTypeDef,
        "TargetString": bytes,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)


class ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef(
    _ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef
):
    pass


_ClientGetByteMatchSetResponseByteMatchSetTypeDef = TypedDict(
    "_ClientGetByteMatchSetResponseByteMatchSetTypeDef",
    {
        "ByteMatchSetId": str,
        "Name": str,
        "ByteMatchTuples": List[ClientGetByteMatchSetResponseByteMatchSetByteMatchTuplesTypeDef],
    },
    total=False,
)


class ClientGetByteMatchSetResponseByteMatchSetTypeDef(
    _ClientGetByteMatchSetResponseByteMatchSetTypeDef
):
    """
    - **ByteMatchSet** *(dict) --*

      Information about the  ByteMatchSet that you specified in the ``GetByteMatchSet`` request. For
      more information, see the following topics:
      *  ByteMatchSet : Contains ``ByteMatchSetId`` , ``ByteMatchTuples`` , and ``Name``
      * ``ByteMatchTuples`` : Contains an array of  ByteMatchTuple objects. Each ``ByteMatchTuple``
      object contains  FieldToMatch , ``PositionalConstraint`` , ``TargetString`` , and
      ``TextTransformation``
      *  FieldToMatch : Contains ``Data`` and ``Type``
      - **ByteMatchSetId** *(string) --*

        The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
        information about a ``ByteMatchSet`` (see  GetByteMatchSet ), update a ``ByteMatchSet`` (see
        UpdateByteMatchSet ), insert a ``ByteMatchSet`` into a ``Rule`` or delete one from a
        ``Rule`` (see  UpdateRule ), and delete a ``ByteMatchSet`` from AWS WAF (see
        DeleteByteMatchSet ).

          ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .
    """


_ClientGetByteMatchSetResponseTypeDef = TypedDict(
    "_ClientGetByteMatchSetResponseTypeDef",
    {"ByteMatchSet": ClientGetByteMatchSetResponseByteMatchSetTypeDef},
    total=False,
)


class ClientGetByteMatchSetResponseTypeDef(_ClientGetByteMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **ByteMatchSet** *(dict) --*

        Information about the  ByteMatchSet that you specified in the ``GetByteMatchSet`` request.
        For more information, see the following topics:
        *  ByteMatchSet : Contains ``ByteMatchSetId`` , ``ByteMatchTuples`` , and ``Name``
        * ``ByteMatchTuples`` : Contains an array of  ByteMatchTuple objects. Each
        ``ByteMatchTuple`` object contains  FieldToMatch , ``PositionalConstraint`` ,
        ``TargetString`` , and ``TextTransformation``
        *  FieldToMatch : Contains ``Data`` and ``Type``
        - **ByteMatchSetId** *(string) --*

          The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get
          information about a ``ByteMatchSet`` (see  GetByteMatchSet ), update a ``ByteMatchSet``
          (see  UpdateByteMatchSet ), insert a ``ByteMatchSet`` into a ``Rule`` or delete one from a
          ``Rule`` (see  UpdateRule ), and delete a ``ByteMatchSet`` from AWS WAF (see
          DeleteByteMatchSet ).

            ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .
    """


_ClientGetChangeTokenResponseTypeDef = TypedDict(
    "_ClientGetChangeTokenResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientGetChangeTokenResponseTypeDef(_ClientGetChangeTokenResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used in the request. Use this value in a
        ``GetChangeTokenStatus`` request to get the current status of the request.
    """


_ClientGetChangeTokenStatusResponseTypeDef = TypedDict(
    "_ClientGetChangeTokenStatusResponseTypeDef",
    {"ChangeTokenStatus": Literal["PROVISIONED", "PENDING", "INSYNC"]},
    total=False,
)


class ClientGetChangeTokenStatusResponseTypeDef(_ClientGetChangeTokenStatusResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeTokenStatus** *(string) --*

        The status of the change token.
    """


_ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef = TypedDict(
    "_ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef",
    {
        "Type": str,
        "Value": Literal[
            "AF",
            "AX",
            "AL",
            "DZ",
            "AS",
            "AD",
            "AO",
            "AI",
            "AQ",
            "AG",
            "AR",
            "AM",
            "AW",
            "AU",
            "AT",
            "AZ",
            "BS",
            "BH",
            "BD",
            "BB",
            "BY",
            "BE",
            "BZ",
            "BJ",
            "BM",
            "BT",
            "BO",
            "BQ",
            "BA",
            "BW",
            "BV",
            "BR",
            "IO",
            "BN",
            "BG",
            "BF",
            "BI",
            "KH",
            "CM",
            "CA",
            "CV",
            "KY",
            "CF",
            "TD",
            "CL",
            "CN",
            "CX",
            "CC",
            "CO",
            "KM",
            "CG",
            "CD",
            "CK",
            "CR",
            "CI",
            "HR",
            "CU",
            "CW",
            "CY",
            "CZ",
            "DK",
            "DJ",
            "DM",
            "DO",
            "EC",
            "EG",
            "SV",
            "GQ",
            "ER",
            "EE",
            "ET",
            "FK",
            "FO",
            "FJ",
            "FI",
            "FR",
            "GF",
            "PF",
            "TF",
            "GA",
            "GM",
            "GE",
            "DE",
            "GH",
            "GI",
            "GR",
            "GL",
            "GD",
            "GP",
            "GU",
            "GT",
            "GG",
            "GN",
            "GW",
            "GY",
            "HT",
            "HM",
            "VA",
            "HN",
            "HK",
            "HU",
            "IS",
            "IN",
            "ID",
            "IR",
            "IQ",
            "IE",
            "IM",
            "IL",
            "IT",
            "JM",
            "JP",
            "JE",
            "JO",
            "KZ",
            "KE",
            "KI",
            "KP",
            "KR",
            "KW",
            "KG",
            "LA",
            "LV",
            "LB",
            "LS",
            "LR",
            "LY",
            "LI",
            "LT",
            "LU",
            "MO",
            "MK",
            "MG",
            "MW",
            "MY",
            "MV",
            "ML",
            "MT",
            "MH",
            "MQ",
            "MR",
            "MU",
            "YT",
            "MX",
            "FM",
            "MD",
            "MC",
            "MN",
            "ME",
            "MS",
            "MA",
            "MZ",
            "MM",
            "NA",
            "NR",
            "NP",
            "NL",
            "NC",
            "NZ",
            "NI",
            "NE",
            "NG",
            "NU",
            "NF",
            "MP",
            "NO",
            "OM",
            "PK",
            "PW",
            "PS",
            "PA",
            "PG",
            "PY",
            "PE",
            "PH",
            "PN",
            "PL",
            "PT",
            "PR",
            "QA",
            "RE",
            "RO",
            "RU",
            "RW",
            "BL",
            "SH",
            "KN",
            "LC",
            "MF",
            "PM",
            "VC",
            "WS",
            "SM",
            "ST",
            "SA",
            "SN",
            "RS",
            "SC",
            "SL",
            "SG",
            "SX",
            "SK",
            "SI",
            "SB",
            "SO",
            "ZA",
            "GS",
            "SS",
            "ES",
            "LK",
            "SD",
            "SR",
            "SJ",
            "SZ",
            "SE",
            "CH",
            "SY",
            "TW",
            "TJ",
            "TZ",
            "TH",
            "TL",
            "TG",
            "TK",
            "TO",
            "TT",
            "TN",
            "TR",
            "TM",
            "TC",
            "TV",
            "UG",
            "UA",
            "AE",
            "GB",
            "US",
            "UM",
            "UY",
            "UZ",
            "VU",
            "VE",
            "VN",
            "VG",
            "VI",
            "WF",
            "EH",
            "YE",
            "ZM",
            "ZW",
        ],
    },
    total=False,
)


class ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef(
    _ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef
):
    pass


_ClientGetGeoMatchSetResponseGeoMatchSetTypeDef = TypedDict(
    "_ClientGetGeoMatchSetResponseGeoMatchSetTypeDef",
    {
        "GeoMatchSetId": str,
        "Name": str,
        "GeoMatchConstraints": List[
            ClientGetGeoMatchSetResponseGeoMatchSetGeoMatchConstraintsTypeDef
        ],
    },
    total=False,
)


class ClientGetGeoMatchSetResponseGeoMatchSetTypeDef(
    _ClientGetGeoMatchSetResponseGeoMatchSetTypeDef
):
    """
    - **GeoMatchSet** *(dict) --*

      Information about the  GeoMatchSet that you specified in the ``GetGeoMatchSet`` request. This
      includes the ``Type`` , which for a ``GeoMatchContraint`` is always ``Country`` , as well as
      the ``Value`` , which is the identifier for a specific country.
      - **GeoMatchSetId** *(string) --*

        The ``GeoMatchSetId`` for an ``GeoMatchSet`` . You use ``GeoMatchSetId`` to get information
        about a ``GeoMatchSet`` (see  GeoMatchSet ), update a ``GeoMatchSet`` (see
        UpdateGeoMatchSet ), insert a ``GeoMatchSet`` into a ``Rule`` or delete one from a ``Rule``
        (see  UpdateRule ), and delete a ``GeoMatchSet`` from AWS WAF (see  DeleteGeoMatchSet ).

          ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .
    """


_ClientGetGeoMatchSetResponseTypeDef = TypedDict(
    "_ClientGetGeoMatchSetResponseTypeDef",
    {"GeoMatchSet": ClientGetGeoMatchSetResponseGeoMatchSetTypeDef},
    total=False,
)


class ClientGetGeoMatchSetResponseTypeDef(_ClientGetGeoMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **GeoMatchSet** *(dict) --*

        Information about the  GeoMatchSet that you specified in the ``GetGeoMatchSet`` request.
        This includes the ``Type`` , which for a ``GeoMatchContraint`` is always ``Country`` , as
        well as the ``Value`` , which is the identifier for a specific country.
        - **GeoMatchSetId** *(string) --*

          The ``GeoMatchSetId`` for an ``GeoMatchSet`` . You use ``GeoMatchSetId`` to get
          information about a ``GeoMatchSet`` (see  GeoMatchSet ), update a ``GeoMatchSet`` (see
          UpdateGeoMatchSet ), insert a ``GeoMatchSet`` into a ``Rule`` or delete one from a
          ``Rule`` (see  UpdateRule ), and delete a ``GeoMatchSet`` from AWS WAF (see
          DeleteGeoMatchSet ).

            ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .
    """


_ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef = TypedDict(
    "_ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef",
    {"Type": Literal["IPV4", "IPV6"], "Value": str},
    total=False,
)


class ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef(
    _ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef
):
    pass


_ClientGetIpSetResponseIPSetTypeDef = TypedDict(
    "_ClientGetIpSetResponseIPSetTypeDef",
    {
        "IPSetId": str,
        "Name": str,
        "IPSetDescriptors": List[ClientGetIpSetResponseIPSetIPSetDescriptorsTypeDef],
    },
    total=False,
)


class ClientGetIpSetResponseIPSetTypeDef(_ClientGetIpSetResponseIPSetTypeDef):
    """
    - **IPSet** *(dict) --*

      Information about the  IPSet that you specified in the ``GetIPSet`` request. For more
      information, see the following topics:
      *  IPSet : Contains ``IPSetDescriptors`` , ``IPSetId`` , and ``Name``
      * ``IPSetDescriptors`` : Contains an array of  IPSetDescriptor objects. Each
      ``IPSetDescriptor`` object contains ``Type`` and ``Value``
      - **IPSetId** *(string) --*

        The ``IPSetId`` for an ``IPSet`` . You use ``IPSetId`` to get information about an ``IPSet``
        (see  GetIPSet ), update an ``IPSet`` (see  UpdateIPSet ), insert an ``IPSet`` into a
        ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``IPSet`` from AWS
        WAF (see  DeleteIPSet ).

          ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .
    """


_ClientGetIpSetResponseTypeDef = TypedDict(
    "_ClientGetIpSetResponseTypeDef", {"IPSet": ClientGetIpSetResponseIPSetTypeDef}, total=False
)


class ClientGetIpSetResponseTypeDef(_ClientGetIpSetResponseTypeDef):
    """
    - *(dict) --*

      - **IPSet** *(dict) --*

        Information about the  IPSet that you specified in the ``GetIPSet`` request. For more
        information, see the following topics:
        *  IPSet : Contains ``IPSetDescriptors`` , ``IPSetId`` , and ``Name``
        * ``IPSetDescriptors`` : Contains an array of  IPSetDescriptor objects. Each
        ``IPSetDescriptor`` object contains ``Type`` and ``Value``
        - **IPSetId** *(string) --*

          The ``IPSetId`` for an ``IPSet`` . You use ``IPSetId`` to get information about an
          ``IPSet`` (see  GetIPSet ), update an ``IPSet`` (see  UpdateIPSet ), insert an ``IPSet``
          into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``IPSet``
          from AWS WAF (see  DeleteIPSet ).

            ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .
    """


_ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "_ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef(
    _ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef
):
    pass


_ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "_ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientGetLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef
        ],
    },
    total=False,
)


class ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef(
    _ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef
):
    """
    - **LoggingConfiguration** *(dict) --*

      The  LoggingConfiguration for the specified web ACL.
      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the web ACL that you want to associate with
        ``LogDestinationConfigs`` .
    """


_ClientGetLoggingConfigurationResponseTypeDef = TypedDict(
    "_ClientGetLoggingConfigurationResponseTypeDef",
    {"LoggingConfiguration": ClientGetLoggingConfigurationResponseLoggingConfigurationTypeDef},
    total=False,
)


class ClientGetLoggingConfigurationResponseTypeDef(_ClientGetLoggingConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **LoggingConfiguration** *(dict) --*

        The  LoggingConfiguration for the specified web ACL.
        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the web ACL that you want to associate with
          ``LogDestinationConfigs`` .
    """


_ClientGetPermissionPolicyResponseTypeDef = TypedDict(
    "_ClientGetPermissionPolicyResponseTypeDef", {"Policy": str}, total=False
)


class ClientGetPermissionPolicyResponseTypeDef(_ClientGetPermissionPolicyResponseTypeDef):
    """
    - *(dict) --*

      - **Policy** *(string) --*

        The IAM policy attached to the specified RuleGroup.
    """


_ClientGetRateBasedRuleManagedKeysResponseTypeDef = TypedDict(
    "_ClientGetRateBasedRuleManagedKeysResponseTypeDef",
    {"ManagedKeys": List[str], "NextMarker": str},
    total=False,
)


class ClientGetRateBasedRuleManagedKeysResponseTypeDef(
    _ClientGetRateBasedRuleManagedKeysResponseTypeDef
):
    """
    - *(dict) --*

      - **ManagedKeys** *(list) --*

        An array of IP addresses that currently are blocked by the specified  RateBasedRule .
        - *(string) --*
    """


_ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef = TypedDict(
    "_ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)


class ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef(
    _ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef
):
    pass


_ClientGetRateBasedRuleResponseRuleTypeDef = TypedDict(
    "_ClientGetRateBasedRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "MatchPredicates": List[ClientGetRateBasedRuleResponseRuleMatchPredicatesTypeDef],
        "RateKey": str,
        "RateLimit": int,
    },
    total=False,
)


class ClientGetRateBasedRuleResponseRuleTypeDef(_ClientGetRateBasedRuleResponseRuleTypeDef):
    """
    - **Rule** *(dict) --*

      Information about the  RateBasedRule that you specified in the ``GetRateBasedRule`` request.
      - **RuleId** *(string) --*

        A unique identifier for a ``RateBasedRule`` . You use ``RuleId`` to get more information
        about a ``RateBasedRule`` (see  GetRateBasedRule ), update a ``RateBasedRule`` (see
        UpdateRateBasedRule ), insert a ``RateBasedRule`` into a ``WebACL`` or delete one from a
        ``WebACL`` (see  UpdateWebACL ), or delete a ``RateBasedRule`` from AWS WAF (see
        DeleteRateBasedRule ).
    """


_ClientGetRateBasedRuleResponseTypeDef = TypedDict(
    "_ClientGetRateBasedRuleResponseTypeDef",
    {"Rule": ClientGetRateBasedRuleResponseRuleTypeDef},
    total=False,
)


class ClientGetRateBasedRuleResponseTypeDef(_ClientGetRateBasedRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Rule** *(dict) --*

        Information about the  RateBasedRule that you specified in the ``GetRateBasedRule`` request.
        - **RuleId** *(string) --*

          A unique identifier for a ``RateBasedRule`` . You use ``RuleId`` to get more information
          about a ``RateBasedRule`` (see  GetRateBasedRule ), update a ``RateBasedRule`` (see
          UpdateRateBasedRule ), insert a ``RateBasedRule`` into a ``WebACL`` or delete one from a
          ``WebACL`` (see  UpdateWebACL ), or delete a ``RateBasedRule`` from AWS WAF (see
          DeleteRateBasedRule ).
    """


_ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef(
    _ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef
):
    pass


_ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef = TypedDict(
    "_ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "RegexPatternSetId": str,
    },
    total=False,
)


class ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef(
    _ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef
):
    pass


_ClientGetRegexMatchSetResponseRegexMatchSetTypeDef = TypedDict(
    "_ClientGetRegexMatchSetResponseRegexMatchSetTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
        "RegexMatchTuples": List[
            ClientGetRegexMatchSetResponseRegexMatchSetRegexMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientGetRegexMatchSetResponseRegexMatchSetTypeDef(
    _ClientGetRegexMatchSetResponseRegexMatchSetTypeDef
):
    """
    - **RegexMatchSet** *(dict) --*

      Information about the  RegexMatchSet that you specified in the ``GetRegexMatchSet`` request.
      For more information, see  RegexMatchTuple .
      - **RegexMatchSetId** *(string) --*

        The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
        information about a ``RegexMatchSet`` (see  GetRegexMatchSet ), update a ``RegexMatchSet``
        (see  UpdateRegexMatchSet ), insert a ``RegexMatchSet`` into a ``Rule`` or delete one from a
        ``Rule`` (see  UpdateRule ), and delete a ``RegexMatchSet`` from AWS WAF (see
        DeleteRegexMatchSet ).

          ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .
    """


_ClientGetRegexMatchSetResponseTypeDef = TypedDict(
    "_ClientGetRegexMatchSetResponseTypeDef",
    {"RegexMatchSet": ClientGetRegexMatchSetResponseRegexMatchSetTypeDef},
    total=False,
)


class ClientGetRegexMatchSetResponseTypeDef(_ClientGetRegexMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **RegexMatchSet** *(dict) --*

        Information about the  RegexMatchSet that you specified in the ``GetRegexMatchSet`` request.
        For more information, see  RegexMatchTuple .
        - **RegexMatchSetId** *(string) --*

          The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get
          information about a ``RegexMatchSet`` (see  GetRegexMatchSet ), update a ``RegexMatchSet``
          (see  UpdateRegexMatchSet ), insert a ``RegexMatchSet`` into a ``Rule`` or delete one from
          a ``Rule`` (see  UpdateRule ), and delete a ``RegexMatchSet`` from AWS WAF (see
          DeleteRegexMatchSet ).

            ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .
    """


_ClientGetRegexPatternSetResponseRegexPatternSetTypeDef = TypedDict(
    "_ClientGetRegexPatternSetResponseRegexPatternSetTypeDef",
    {"RegexPatternSetId": str, "Name": str, "RegexPatternStrings": List[str]},
    total=False,
)


class ClientGetRegexPatternSetResponseRegexPatternSetTypeDef(
    _ClientGetRegexPatternSetResponseRegexPatternSetTypeDef
):
    """
    - **RegexPatternSet** *(dict) --*

      Information about the  RegexPatternSet that you specified in the ``GetRegexPatternSet``
      request, including the identifier of the pattern set and the regular expression patterns you
      want AWS WAF to search for.
      - **RegexPatternSetId** *(string) --*

        The identifier for the ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get
        information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
        ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
        WAF.

          ``RegexMatchSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .
    """


_ClientGetRegexPatternSetResponseTypeDef = TypedDict(
    "_ClientGetRegexPatternSetResponseTypeDef",
    {"RegexPatternSet": ClientGetRegexPatternSetResponseRegexPatternSetTypeDef},
    total=False,
)


class ClientGetRegexPatternSetResponseTypeDef(_ClientGetRegexPatternSetResponseTypeDef):
    """
    - *(dict) --*

      - **RegexPatternSet** *(dict) --*

        Information about the  RegexPatternSet that you specified in the ``GetRegexPatternSet``
        request, including the identifier of the pattern set and the regular expression patterns you
        want AWS WAF to search for.
        - **RegexPatternSetId** *(string) --*

          The identifier for the ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get
          information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a
          ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS
          WAF.

            ``RegexMatchSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .
    """


_ClientGetRuleGroupResponseRuleGroupTypeDef = TypedDict(
    "_ClientGetRuleGroupResponseRuleGroupTypeDef",
    {"RuleGroupId": str, "Name": str, "MetricName": str},
    total=False,
)


class ClientGetRuleGroupResponseRuleGroupTypeDef(_ClientGetRuleGroupResponseRuleGroupTypeDef):
    """
    - **RuleGroup** *(dict) --*

      Information about the  RuleGroup that you specified in the ``GetRuleGroup`` request.
      - **RuleGroupId** *(string) --*

        A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
        about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup ),
        insert a ``RuleGroup`` into a ``WebACL`` or delete a one from a ``WebACL`` (see
        UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

          ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .
    """


_ClientGetRuleGroupResponseTypeDef = TypedDict(
    "_ClientGetRuleGroupResponseTypeDef",
    {"RuleGroup": ClientGetRuleGroupResponseRuleGroupTypeDef},
    total=False,
)


class ClientGetRuleGroupResponseTypeDef(_ClientGetRuleGroupResponseTypeDef):
    """
    - *(dict) --*

      - **RuleGroup** *(dict) --*

        Information about the  RuleGroup that you specified in the ``GetRuleGroup`` request.
        - **RuleGroupId** *(string) --*

          A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information
          about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup
          ), insert a ``RuleGroup`` into a ``WebACL`` or delete a one from a ``WebACL`` (see
          UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

            ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .
    """


_ClientGetRuleResponseRulePredicatesTypeDef = TypedDict(
    "_ClientGetRuleResponseRulePredicatesTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)


class ClientGetRuleResponseRulePredicatesTypeDef(_ClientGetRuleResponseRulePredicatesTypeDef):
    pass


_ClientGetRuleResponseRuleTypeDef = TypedDict(
    "_ClientGetRuleResponseRuleTypeDef",
    {
        "RuleId": str,
        "Name": str,
        "MetricName": str,
        "Predicates": List[ClientGetRuleResponseRulePredicatesTypeDef],
    },
    total=False,
)


class ClientGetRuleResponseRuleTypeDef(_ClientGetRuleResponseRuleTypeDef):
    """
    - **Rule** *(dict) --*

      Information about the  Rule that you specified in the ``GetRule`` request. For more
      information, see the following topics:
      *  Rule : Contains ``MetricName`` , ``Name`` , an array of ``Predicate`` objects, and
      ``RuleId``
      *  Predicate : Each ``Predicate`` object contains ``DataId`` , ``Negated`` , and ``Type``
      - **RuleId** *(string) --*

        A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
        ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
        ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from
        AWS WAF (see  DeleteRule ).

          ``RuleId`` is returned by  CreateRule and by  ListRules .
    """


_ClientGetRuleResponseTypeDef = TypedDict(
    "_ClientGetRuleResponseTypeDef", {"Rule": ClientGetRuleResponseRuleTypeDef}, total=False
)


class ClientGetRuleResponseTypeDef(_ClientGetRuleResponseTypeDef):
    """
    - *(dict) --*

      - **Rule** *(dict) --*

        Information about the  Rule that you specified in the ``GetRule`` request. For more
        information, see the following topics:
        *  Rule : Contains ``MetricName`` , ``Name`` , an array of ``Predicate`` objects, and
        ``RuleId``
        *  Predicate : Each ``Predicate`` object contains ``DataId`` , ``Negated`` , and ``Type``
        - **RuleId** *(string) --*

          A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a
          ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a
          ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule``
          from AWS WAF (see  DeleteRule ).

            ``RuleId`` is returned by  CreateRule and by  ListRules .
    """


_ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef = TypedDict(
    "_ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef(
    _ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef
):
    pass


_ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef = TypedDict(
    "_ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef",
    {
        "ClientIP": str,
        "Country": str,
        "URI": str,
        "Method": str,
        "HTTPVersion": str,
        "Headers": List[ClientGetSampledRequestsResponseSampledRequestsRequestHeadersTypeDef],
    },
    total=False,
)


class ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef(
    _ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef
):
    """
    - **Request** *(dict) --*

      A complex type that contains detailed information about the request.
      - **ClientIP** *(string) --*

        The IP address that the request originated from. If the ``WebACL`` is associated with a
        CloudFront distribution, this is the value of one of the following fields in CloudFront
        access logs:
        * ``c-ip`` , if the viewer did not use an HTTP proxy or a load balancer to send the request
        * ``x-forwarded-for`` , if the viewer did use an HTTP proxy or a load balancer to send the
        request
    """


_ClientGetSampledRequestsResponseSampledRequestsTypeDef = TypedDict(
    "_ClientGetSampledRequestsResponseSampledRequestsTypeDef",
    {
        "Request": ClientGetSampledRequestsResponseSampledRequestsRequestTypeDef,
        "Weight": int,
        "Timestamp": datetime,
        "Action": str,
        "RuleWithinRuleGroup": str,
    },
    total=False,
)


class ClientGetSampledRequestsResponseSampledRequestsTypeDef(
    _ClientGetSampledRequestsResponseSampledRequestsTypeDef
):
    """
    - *(dict) --*

      The response from a  GetSampledRequests request includes a ``SampledHTTPRequests`` complex
      type that appears as ``SampledRequests`` in the response syntax. ``SampledHTTPRequests``
      contains one ``SampledHTTPRequest`` object for each web request that is returned by
      ``GetSampledRequests`` .
      - **Request** *(dict) --*

        A complex type that contains detailed information about the request.
        - **ClientIP** *(string) --*

          The IP address that the request originated from. If the ``WebACL`` is associated with a
          CloudFront distribution, this is the value of one of the following fields in CloudFront
          access logs:
          * ``c-ip`` , if the viewer did not use an HTTP proxy or a load balancer to send the
          request
          * ``x-forwarded-for`` , if the viewer did use an HTTP proxy or a load balancer to send the
          request
    """


_ClientGetSampledRequestsResponseTimeWindowTypeDef = TypedDict(
    "_ClientGetSampledRequestsResponseTimeWindowTypeDef",
    {"StartTime": datetime, "EndTime": datetime},
    total=False,
)


class ClientGetSampledRequestsResponseTimeWindowTypeDef(
    _ClientGetSampledRequestsResponseTimeWindowTypeDef
):
    pass


_ClientGetSampledRequestsResponseTypeDef = TypedDict(
    "_ClientGetSampledRequestsResponseTypeDef",
    {
        "SampledRequests": List[ClientGetSampledRequestsResponseSampledRequestsTypeDef],
        "PopulationSize": int,
        "TimeWindow": ClientGetSampledRequestsResponseTimeWindowTypeDef,
    },
    total=False,
)


class ClientGetSampledRequestsResponseTypeDef(_ClientGetSampledRequestsResponseTypeDef):
    """
    - *(dict) --*

      - **SampledRequests** *(list) --*

        A complex type that contains detailed information about each of the requests in the sample.
        - *(dict) --*

          The response from a  GetSampledRequests request includes a ``SampledHTTPRequests`` complex
          type that appears as ``SampledRequests`` in the response syntax. ``SampledHTTPRequests``
          contains one ``SampledHTTPRequest`` object for each web request that is returned by
          ``GetSampledRequests`` .
          - **Request** *(dict) --*

            A complex type that contains detailed information about the request.
            - **ClientIP** *(string) --*

              The IP address that the request originated from. If the ``WebACL`` is associated with
              a CloudFront distribution, this is the value of one of the following fields in
              CloudFront access logs:
              * ``c-ip`` , if the viewer did not use an HTTP proxy or a load balancer to send the
              request
              * ``x-forwarded-for`` , if the viewer did use an HTTP proxy or a load balancer to send
              the request
    """


_RequiredClientGetSampledRequestsTimeWindowTypeDef = TypedDict(
    "_RequiredClientGetSampledRequestsTimeWindowTypeDef", {"StartTime": datetime}
)
_OptionalClientGetSampledRequestsTimeWindowTypeDef = TypedDict(
    "_OptionalClientGetSampledRequestsTimeWindowTypeDef", {"EndTime": datetime}, total=False
)


class ClientGetSampledRequestsTimeWindowTypeDef(
    _RequiredClientGetSampledRequestsTimeWindowTypeDef,
    _OptionalClientGetSampledRequestsTimeWindowTypeDef,
):
    """
    The start date and time and the end date and time of the range for which you want
    ``GetSampledRequests`` to return a sample of requests. Specify the date and time in the
    following format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three
    hours.
    - **StartTime** *(datetime) --***[REQUIRED]**

      The beginning of the time range from which you want ``GetSampledRequests`` to return a sample
      of the requests that your AWS resource received. Specify the date and time in the following
      format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three hours.
    """


_ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef = TypedDict(
    "_ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef(
    _ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef
):
    pass


_ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef = TypedDict(
    "_ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef",
    {
        "FieldToMatch": ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
    },
    total=False,
)


class ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef(
    _ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef
):
    pass


_ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef = TypedDict(
    "_ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef",
    {
        "SizeConstraintSetId": str,
        "Name": str,
        "SizeConstraints": List[
            ClientGetSizeConstraintSetResponseSizeConstraintSetSizeConstraintsTypeDef
        ],
    },
    total=False,
)


class ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef(
    _ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef
):
    """
    - **SizeConstraintSet** *(dict) --*

      Information about the  SizeConstraintSet that you specified in the ``GetSizeConstraintSet``
      request. For more information, see the following topics:
      *  SizeConstraintSet : Contains ``SizeConstraintSetId`` , ``SizeConstraints`` , and ``Name``
      * ``SizeConstraints`` : Contains an array of  SizeConstraint objects. Each ``SizeConstraint``
      object contains  FieldToMatch , ``TextTransformation`` , ``ComparisonOperator`` , and ``Size``
      *  FieldToMatch : Contains ``Data`` and ``Type``
      - **SizeConstraintSetId** *(string) --*

        A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
        information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
        ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into a
        ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
        ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

          ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
          ListSizeConstraintSets .
    """


_ClientGetSizeConstraintSetResponseTypeDef = TypedDict(
    "_ClientGetSizeConstraintSetResponseTypeDef",
    {"SizeConstraintSet": ClientGetSizeConstraintSetResponseSizeConstraintSetTypeDef},
    total=False,
)


class ClientGetSizeConstraintSetResponseTypeDef(_ClientGetSizeConstraintSetResponseTypeDef):
    """
    - *(dict) --*

      - **SizeConstraintSet** *(dict) --*

        Information about the  SizeConstraintSet that you specified in the ``GetSizeConstraintSet``
        request. For more information, see the following topics:
        *  SizeConstraintSet : Contains ``SizeConstraintSetId`` , ``SizeConstraints`` , and ``Name``
        * ``SizeConstraints`` : Contains an array of  SizeConstraint objects. Each
        ``SizeConstraint`` object contains  FieldToMatch , ``TextTransformation`` ,
        ``ComparisonOperator`` , and ``Size``
        *  FieldToMatch : Contains ``Data`` and ``Type``
        - **SizeConstraintSetId** *(string) --*

          A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get
          information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a
          ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into
          a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a
          ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

            ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by
            ListSizeConstraintSets .
    """


_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef(
    _ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef
):
    pass


_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef = TypedDict(
    "_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)


class ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef(
    _ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef
):
    pass


_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef = TypedDict(
    "_ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "Name": str,
        "SqlInjectionMatchTuples": List[
            ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetSqlInjectionMatchTuplesTypeDef
        ],
    },
    total=False,
)


class ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef(
    _ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef
):
    """
    - **SqlInjectionMatchSet** *(dict) --*

      Information about the  SqlInjectionMatchSet that you specified in the
      ``GetSqlInjectionMatchSet`` request. For more information, see the following topics:
      *  SqlInjectionMatchSet : Contains ``Name`` , ``SqlInjectionMatchSetId`` , and an array of
      ``SqlInjectionMatchTuple`` objects
      *  SqlInjectionMatchTuple : Each ``SqlInjectionMatchTuple`` object contains ``FieldToMatch``
      and ``TextTransformation``
      *  FieldToMatch : Contains ``Data`` and ``Type``
      - **SqlInjectionMatchSetId** *(string) --*

        A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to
        get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a
        ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
        ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ),
        and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

          ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
          ListSqlInjectionMatchSets .
    """


_ClientGetSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "_ClientGetSqlInjectionMatchSetResponseTypeDef",
    {"SqlInjectionMatchSet": ClientGetSqlInjectionMatchSetResponseSqlInjectionMatchSetTypeDef},
    total=False,
)


class ClientGetSqlInjectionMatchSetResponseTypeDef(_ClientGetSqlInjectionMatchSetResponseTypeDef):
    """
    - *(dict) --*

      The response to a  GetSqlInjectionMatchSet request.
      - **SqlInjectionMatchSet** *(dict) --*

        Information about the  SqlInjectionMatchSet that you specified in the
        ``GetSqlInjectionMatchSet`` request. For more information, see the following topics:
        *  SqlInjectionMatchSet : Contains ``Name`` , ``SqlInjectionMatchSetId`` , and an array of
        ``SqlInjectionMatchTuple`` objects
        *  SqlInjectionMatchTuple : Each ``SqlInjectionMatchTuple`` object contains ``FieldToMatch``
        and ``TextTransformation``
        *  FieldToMatch : Contains ``Data`` and ``Type``
        - **SqlInjectionMatchSetId** *(string) --*

          A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to
          get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a
          ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a
          ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ),
          and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

            ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by
            ListSqlInjectionMatchSets .
    """


_ClientGetWebAclForResourceResponseWebACLSummaryTypeDef = TypedDict(
    "_ClientGetWebAclForResourceResponseWebACLSummaryTypeDef",
    {"WebACLId": str, "Name": str},
    total=False,
)


class ClientGetWebAclForResourceResponseWebACLSummaryTypeDef(
    _ClientGetWebAclForResourceResponseWebACLSummaryTypeDef
):
    """
    - **WebACLSummary** *(dict) --*

      Information about the web ACL that you specified in the ``GetWebACLForResource`` request. If
      there is no associated resource, a null WebACLSummary is returned.
      - **WebACLId** *(string) --*

        A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
        ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
        ``WebACL`` from AWS WAF (see  DeleteWebACL ).

          ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .
    """


_ClientGetWebAclForResourceResponseTypeDef = TypedDict(
    "_ClientGetWebAclForResourceResponseTypeDef",
    {"WebACLSummary": ClientGetWebAclForResourceResponseWebACLSummaryTypeDef},
    total=False,
)


class ClientGetWebAclForResourceResponseTypeDef(_ClientGetWebAclForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **WebACLSummary** *(dict) --*

        Information about the web ACL that you specified in the ``GetWebACLForResource`` request. If
        there is no associated resource, a null WebACLSummary is returned.
        - **WebACLId** *(string) --*

          A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
          ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
          ``WebACL`` from AWS WAF (see  DeleteWebACL ).

            ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .
    """


_ClientGetWebAclResponseWebACLDefaultActionTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLDefaultActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)


class ClientGetWebAclResponseWebACLDefaultActionTypeDef(
    _ClientGetWebAclResponseWebACLDefaultActionTypeDef
):
    pass


_ClientGetWebAclResponseWebACLRulesActionTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLRulesActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)


class ClientGetWebAclResponseWebACLRulesActionTypeDef(
    _ClientGetWebAclResponseWebACLRulesActionTypeDef
):
    pass


_ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef", {"RuleId": str}, total=False
)


class ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef(
    _ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef
):
    pass


_ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef",
    {"Type": Literal["NONE", "COUNT"]},
    total=False,
)


class ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef(
    _ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef
):
    pass


_ClientGetWebAclResponseWebACLRulesTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLRulesTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientGetWebAclResponseWebACLRulesActionTypeDef,
        "OverrideAction": ClientGetWebAclResponseWebACLRulesOverrideActionTypeDef,
        "Type": Literal["REGULAR", "RATE_BASED", "GROUP"],
        "ExcludedRules": List[ClientGetWebAclResponseWebACLRulesExcludedRulesTypeDef],
    },
    total=False,
)


class ClientGetWebAclResponseWebACLRulesTypeDef(_ClientGetWebAclResponseWebACLRulesTypeDef):
    pass


_ClientGetWebAclResponseWebACLTypeDef = TypedDict(
    "_ClientGetWebAclResponseWebACLTypeDef",
    {
        "WebACLId": str,
        "Name": str,
        "MetricName": str,
        "DefaultAction": ClientGetWebAclResponseWebACLDefaultActionTypeDef,
        "Rules": List[ClientGetWebAclResponseWebACLRulesTypeDef],
        "WebACLArn": str,
    },
    total=False,
)


class ClientGetWebAclResponseWebACLTypeDef(_ClientGetWebAclResponseWebACLTypeDef):
    """
    - **WebACL** *(dict) --*

      Information about the  WebACL that you specified in the ``GetWebACL`` request. For more
      information, see the following topics:
      *  WebACL : Contains ``DefaultAction`` , ``MetricName`` , ``Name`` , an array of ``Rule``
      objects, and ``WebACLId``
      * ``DefaultAction`` (Data type is  WafAction ): Contains ``Type``
      * ``Rules`` : Contains an array of ``ActivatedRule`` objects, which contain ``Action`` ,
      ``Priority`` , and ``RuleId``
      * ``Action`` : Contains ``Type``
      - **WebACLId** *(string) --*

        A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
        ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
        ``WebACL`` from AWS WAF (see  DeleteWebACL ).

          ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .
    """


_ClientGetWebAclResponseTypeDef = TypedDict(
    "_ClientGetWebAclResponseTypeDef", {"WebACL": ClientGetWebAclResponseWebACLTypeDef}, total=False
)


class ClientGetWebAclResponseTypeDef(_ClientGetWebAclResponseTypeDef):
    """
    - *(dict) --*

      - **WebACL** *(dict) --*

        Information about the  WebACL that you specified in the ``GetWebACL`` request. For more
        information, see the following topics:
        *  WebACL : Contains ``DefaultAction`` , ``MetricName`` , ``Name`` , an array of ``Rule``
        objects, and ``WebACLId``
        * ``DefaultAction`` (Data type is  WafAction ): Contains ``Type``
        * ``Rules`` : Contains an array of ``ActivatedRule`` objects, which contain ``Action`` ,
        ``Priority`` , and ``RuleId``
        * ``Action`` : Contains ``Type``
        - **WebACLId** *(string) --*

          A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a
          ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a
          ``WebACL`` from AWS WAF (see  DeleteWebACL ).

            ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .
    """


_ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef = TypedDict(
    "_ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef(
    _ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef
):
    pass


_ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef = TypedDict(
    "_ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef",
    {
        "FieldToMatch": ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)


class ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef(
    _ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef
):
    pass


_ClientGetXssMatchSetResponseXssMatchSetTypeDef = TypedDict(
    "_ClientGetXssMatchSetResponseXssMatchSetTypeDef",
    {
        "XssMatchSetId": str,
        "Name": str,
        "XssMatchTuples": List[ClientGetXssMatchSetResponseXssMatchSetXssMatchTuplesTypeDef],
    },
    total=False,
)


class ClientGetXssMatchSetResponseXssMatchSetTypeDef(
    _ClientGetXssMatchSetResponseXssMatchSetTypeDef
):
    """
    - **XssMatchSet** *(dict) --*

      Information about the  XssMatchSet that you specified in the ``GetXssMatchSet`` request. For
      more information, see the following topics:
      *  XssMatchSet : Contains ``Name`` , ``XssMatchSetId`` , and an array of ``XssMatchTuple``
      objects
      *  XssMatchTuple : Each ``XssMatchTuple`` object contains ``FieldToMatch`` and
      ``TextTransformation``
      *  FieldToMatch : Contains ``Data`` and ``Type``
      - **XssMatchSetId** *(string) --*

        A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
        about an ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
        UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a ``Rule``
        (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see  DeleteXssMatchSet ).

          ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .
    """


_ClientGetXssMatchSetResponseTypeDef = TypedDict(
    "_ClientGetXssMatchSetResponseTypeDef",
    {"XssMatchSet": ClientGetXssMatchSetResponseXssMatchSetTypeDef},
    total=False,
)


class ClientGetXssMatchSetResponseTypeDef(_ClientGetXssMatchSetResponseTypeDef):
    """
    - *(dict) --*

      The response to a  GetXssMatchSet request.
      - **XssMatchSet** *(dict) --*

        Information about the  XssMatchSet that you specified in the ``GetXssMatchSet`` request. For
        more information, see the following topics:
        *  XssMatchSet : Contains ``Name`` , ``XssMatchSetId`` , and an array of ``XssMatchTuple``
        objects
        *  XssMatchTuple : Each ``XssMatchTuple`` object contains ``FieldToMatch`` and
        ``TextTransformation``
        *  FieldToMatch : Contains ``Data`` and ``Type``
        - **XssMatchSetId** *(string) --*

          A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information
          about an ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see
          UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a
          ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see
          DeleteXssMatchSet ).

            ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .
    """


_ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef = TypedDict(
    "_ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)


class ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef(
    _ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef
):
    pass


_ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef = TypedDict(
    "_ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef",
    {"RuleId": str},
    total=False,
)


class ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef(
    _ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef
):
    pass


_ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef = TypedDict(
    "_ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef",
    {"Type": Literal["NONE", "COUNT"]},
    total=False,
)


class ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef(
    _ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef
):
    pass


_ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef = TypedDict(
    "_ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientListActivatedRulesInRuleGroupResponseActivatedRulesActionTypeDef,
        "OverrideAction": ClientListActivatedRulesInRuleGroupResponseActivatedRulesOverrideActionTypeDef,
        "Type": Literal["REGULAR", "RATE_BASED", "GROUP"],
        "ExcludedRules": List[
            ClientListActivatedRulesInRuleGroupResponseActivatedRulesExcludedRulesTypeDef
        ],
    },
    total=False,
)


class ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef(
    _ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef
):
    pass


_ClientListActivatedRulesInRuleGroupResponseTypeDef = TypedDict(
    "_ClientListActivatedRulesInRuleGroupResponseTypeDef",
    {
        "NextMarker": str,
        "ActivatedRules": List[ClientListActivatedRulesInRuleGroupResponseActivatedRulesTypeDef],
    },
    total=False,
)


class ClientListActivatedRulesInRuleGroupResponseTypeDef(
    _ClientListActivatedRulesInRuleGroupResponseTypeDef
):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more ``ActivatedRules`` than the number that you specified for ``Limit`` in the
        request, the response includes a ``NextMarker`` value. To list more ``ActivatedRules`` ,
        submit another ``ListActivatedRulesInRuleGroup`` request, and specify the ``NextMarker``
        value from the response in the ``NextMarker`` value in the next request.
    """


_ClientListByteMatchSetsResponseByteMatchSetsTypeDef = TypedDict(
    "_ClientListByteMatchSetsResponseByteMatchSetsTypeDef",
    {"ByteMatchSetId": str, "Name": str},
    total=False,
)


class ClientListByteMatchSetsResponseByteMatchSetsTypeDef(
    _ClientListByteMatchSetsResponseByteMatchSetsTypeDef
):
    pass


_ClientListByteMatchSetsResponseTypeDef = TypedDict(
    "_ClientListByteMatchSetsResponseTypeDef",
    {"NextMarker": str, "ByteMatchSets": List[ClientListByteMatchSetsResponseByteMatchSetsTypeDef]},
    total=False,
)


class ClientListByteMatchSetsResponseTypeDef(_ClientListByteMatchSetsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more ``ByteMatchSet`` objects than the number that you specified for ``Limit``
        in the request, the response includes a ``NextMarker`` value. To list more ``ByteMatchSet``
        objects, submit another ``ListByteMatchSets`` request, and specify the ``NextMarker`` value
        from the response in the ``NextMarker`` value in the next request.
    """


_ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef = TypedDict(
    "_ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef",
    {"GeoMatchSetId": str, "Name": str},
    total=False,
)


class ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef(
    _ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef
):
    pass


_ClientListGeoMatchSetsResponseTypeDef = TypedDict(
    "_ClientListGeoMatchSetsResponseTypeDef",
    {"NextMarker": str, "GeoMatchSets": List[ClientListGeoMatchSetsResponseGeoMatchSetsTypeDef]},
    total=False,
)


class ClientListGeoMatchSetsResponseTypeDef(_ClientListGeoMatchSetsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more ``GeoMatchSet`` objects than the number that you specified for ``Limit`` in
        the request, the response includes a ``NextMarker`` value. To list more ``GeoMatchSet``
        objects, submit another ``ListGeoMatchSets`` request, and specify the ``NextMarker`` value
        from the response in the ``NextMarker`` value in the next request.
    """


_ClientListIpSetsResponseIPSetsTypeDef = TypedDict(
    "_ClientListIpSetsResponseIPSetsTypeDef", {"IPSetId": str, "Name": str}, total=False
)


class ClientListIpSetsResponseIPSetsTypeDef(_ClientListIpSetsResponseIPSetsTypeDef):
    pass


_ClientListIpSetsResponseTypeDef = TypedDict(
    "_ClientListIpSetsResponseTypeDef",
    {"NextMarker": str, "IPSets": List[ClientListIpSetsResponseIPSetsTypeDef]},
    total=False,
)


class ClientListIpSetsResponseTypeDef(_ClientListIpSetsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        To list more ``IPSet`` objects, submit another ``ListIPSets`` request, and in the next
        request use the ``NextMarker`` response value as the ``NextMarker`` value.
    """


_ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef = TypedDict(
    "_ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef(
    _ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef
):
    pass


_ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef = TypedDict(
    "_ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientListLoggingConfigurationsResponseLoggingConfigurationsRedactedFieldsTypeDef
        ],
    },
    total=False,
)


class ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef(
    _ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef
):
    """
    - *(dict) --*

      The Amazon Kinesis Data Firehose, ``RedactedFields`` information, and the web ACL Amazon
      Resource Name (ARN).
      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the web ACL that you want to associate with
        ``LogDestinationConfigs`` .
    """


_ClientListLoggingConfigurationsResponseTypeDef = TypedDict(
    "_ClientListLoggingConfigurationsResponseTypeDef",
    {
        "LoggingConfigurations": List[
            ClientListLoggingConfigurationsResponseLoggingConfigurationsTypeDef
        ],
        "NextMarker": str,
    },
    total=False,
)


class ClientListLoggingConfigurationsResponseTypeDef(
    _ClientListLoggingConfigurationsResponseTypeDef
):
    """
    - *(dict) --*

      - **LoggingConfigurations** *(list) --*

        An array of  LoggingConfiguration objects.
        - *(dict) --*

          The Amazon Kinesis Data Firehose, ``RedactedFields`` information, and the web ACL Amazon
          Resource Name (ARN).
          - **ResourceArn** *(string) --*

            The Amazon Resource Name (ARN) of the web ACL that you want to associate with
            ``LogDestinationConfigs`` .
    """


_ClientListRateBasedRulesResponseRulesTypeDef = TypedDict(
    "_ClientListRateBasedRulesResponseRulesTypeDef", {"RuleId": str, "Name": str}, total=False
)


class ClientListRateBasedRulesResponseRulesTypeDef(_ClientListRateBasedRulesResponseRulesTypeDef):
    pass


_ClientListRateBasedRulesResponseTypeDef = TypedDict(
    "_ClientListRateBasedRulesResponseTypeDef",
    {"NextMarker": str, "Rules": List[ClientListRateBasedRulesResponseRulesTypeDef]},
    total=False,
)


class ClientListRateBasedRulesResponseTypeDef(_ClientListRateBasedRulesResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more ``Rules`` than the number that you specified for ``Limit`` in the request,
        the response includes a ``NextMarker`` value. To list more ``Rules`` , submit another
        ``ListRateBasedRules`` request, and specify the ``NextMarker`` value from the response in
        the ``NextMarker`` value in the next request.
    """


_ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef = TypedDict(
    "_ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef",
    {"RegexMatchSetId": str, "Name": str},
    total=False,
)


class ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef(
    _ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef
):
    pass


_ClientListRegexMatchSetsResponseTypeDef = TypedDict(
    "_ClientListRegexMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexMatchSets": List[ClientListRegexMatchSetsResponseRegexMatchSetsTypeDef],
    },
    total=False,
)


class ClientListRegexMatchSetsResponseTypeDef(_ClientListRegexMatchSetsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more ``RegexMatchSet`` objects than the number that you specified for ``Limit``
        in the request, the response includes a ``NextMarker`` value. To list more ``RegexMatchSet``
        objects, submit another ``ListRegexMatchSets`` request, and specify the ``NextMarker`` value
        from the response in the ``NextMarker`` value in the next request.
    """


_ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef = TypedDict(
    "_ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef",
    {"RegexPatternSetId": str, "Name": str},
    total=False,
)


class ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef(
    _ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef
):
    pass


_ClientListRegexPatternSetsResponseTypeDef = TypedDict(
    "_ClientListRegexPatternSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexPatternSets": List[ClientListRegexPatternSetsResponseRegexPatternSetsTypeDef],
    },
    total=False,
)


class ClientListRegexPatternSetsResponseTypeDef(_ClientListRegexPatternSetsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more ``RegexPatternSet`` objects than the number that you specified for
        ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more
        ``RegexPatternSet`` objects, submit another ``ListRegexPatternSets`` request, and specify
        the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.
    """


_ClientListResourcesForWebAclResponseTypeDef = TypedDict(
    "_ClientListResourcesForWebAclResponseTypeDef", {"ResourceArns": List[str]}, total=False
)


class ClientListResourcesForWebAclResponseTypeDef(_ClientListResourcesForWebAclResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceArns** *(list) --*

        An array of ARNs (Amazon Resource Names) of the resources associated with the specified web
        ACL. An array with zero elements is returned if there are no resources associated with the
        web ACL.
        - *(string) --*
    """


_ClientListRuleGroupsResponseRuleGroupsTypeDef = TypedDict(
    "_ClientListRuleGroupsResponseRuleGroupsTypeDef", {"RuleGroupId": str, "Name": str}, total=False
)


class ClientListRuleGroupsResponseRuleGroupsTypeDef(_ClientListRuleGroupsResponseRuleGroupsTypeDef):
    pass


_ClientListRuleGroupsResponseTypeDef = TypedDict(
    "_ClientListRuleGroupsResponseTypeDef",
    {"NextMarker": str, "RuleGroups": List[ClientListRuleGroupsResponseRuleGroupsTypeDef]},
    total=False,
)


class ClientListRuleGroupsResponseTypeDef(_ClientListRuleGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more ``RuleGroups`` than the number that you specified for ``Limit`` in the
        request, the response includes a ``NextMarker`` value. To list more ``RuleGroups`` , submit
        another ``ListRuleGroups`` request, and specify the ``NextMarker`` value from the response
        in the ``NextMarker`` value in the next request.
    """


_ClientListRulesResponseRulesTypeDef = TypedDict(
    "_ClientListRulesResponseRulesTypeDef", {"RuleId": str, "Name": str}, total=False
)


class ClientListRulesResponseRulesTypeDef(_ClientListRulesResponseRulesTypeDef):
    pass


_ClientListRulesResponseTypeDef = TypedDict(
    "_ClientListRulesResponseTypeDef",
    {"NextMarker": str, "Rules": List[ClientListRulesResponseRulesTypeDef]},
    total=False,
)


class ClientListRulesResponseTypeDef(_ClientListRulesResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more ``Rules`` than the number that you specified for ``Limit`` in the request,
        the response includes a ``NextMarker`` value. To list more ``Rules`` , submit another
        ``ListRules`` request, and specify the ``NextMarker`` value from the response in the
        ``NextMarker`` value in the next request.
    """


_ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef = TypedDict(
    "_ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef",
    {"SizeConstraintSetId": str, "Name": str},
    total=False,
)


class ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef(
    _ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef
):
    pass


_ClientListSizeConstraintSetsResponseTypeDef = TypedDict(
    "_ClientListSizeConstraintSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SizeConstraintSets": List[ClientListSizeConstraintSetsResponseSizeConstraintSetsTypeDef],
    },
    total=False,
)


class ClientListSizeConstraintSetsResponseTypeDef(_ClientListSizeConstraintSetsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more ``SizeConstraintSet`` objects than the number that you specified for
        ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more
        ``SizeConstraintSet`` objects, submit another ``ListSizeConstraintSets`` request, and
        specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next
        request.
    """


_ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef = TypedDict(
    "_ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef",
    {"SqlInjectionMatchSetId": str, "Name": str},
    total=False,
)


class ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef(
    _ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef
):
    pass


_ClientListSqlInjectionMatchSetsResponseTypeDef = TypedDict(
    "_ClientListSqlInjectionMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SqlInjectionMatchSets": List[
            ClientListSqlInjectionMatchSetsResponseSqlInjectionMatchSetsTypeDef
        ],
    },
    total=False,
)


class ClientListSqlInjectionMatchSetsResponseTypeDef(
    _ClientListSqlInjectionMatchSetsResponseTypeDef
):
    """
    - *(dict) --*

      The response to a  ListSqlInjectionMatchSets request.
      - **NextMarker** *(string) --*

        If you have more  SqlInjectionMatchSet objects than the number that you specified for
        ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more
        ``SqlInjectionMatchSet`` objects, submit another ``ListSqlInjectionMatchSets`` request, and
        specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next
        request.
    """


_ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef = TypedDict(
    "_ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef",
    {"RuleGroupId": str, "Name": str, "MetricName": str},
    total=False,
)


class ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef(
    _ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef
):
    pass


_ClientListSubscribedRuleGroupsResponseTypeDef = TypedDict(
    "_ClientListSubscribedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List[ClientListSubscribedRuleGroupsResponseRuleGroupsTypeDef],
    },
    total=False,
)


class ClientListSubscribedRuleGroupsResponseTypeDef(_ClientListSubscribedRuleGroupsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more objects than the number that you specified for ``Limit`` in the request,
        the response includes a ``NextMarker`` value. To list more objects, submit another
        ``ListSubscribedRuleGroups`` request, and specify the ``NextMarker`` value from the response
        in the ``NextMarker`` value in the next request.
    """


_ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef(
    _ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef
):
    """
    - *(dict) --*

      - **Key** *(string) --*
      - **Value** *(string) --*
    """


_ClientListTagsForResourceResponseTagInfoForResourceTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagInfoForResourceTypeDef",
    {
        "ResourceARN": str,
        "TagList": List[ClientListTagsForResourceResponseTagInfoForResourceTagListTypeDef],
    },
    total=False,
)


class ClientListTagsForResourceResponseTagInfoForResourceTypeDef(
    _ClientListTagsForResourceResponseTagInfoForResourceTypeDef
):
    """
    - **TagInfoForResource** *(dict) --*

      - **ResourceARN** *(string) --*
      - **TagList** *(list) --*

        - *(dict) --*

          - **Key** *(string) --*
          - **Value** *(string) --*
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {
        "NextMarker": str,
        "TagInfoForResource": ClientListTagsForResourceResponseTagInfoForResourceTypeDef,
    },
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*
      - **TagInfoForResource** *(dict) --*

        - **ResourceARN** *(string) --*
        - **TagList** *(list) --*

          - *(dict) --*

            - **Key** *(string) --*
            - **Value** *(string) --*
    """


_ClientListWebAclsResponseWebACLsTypeDef = TypedDict(
    "_ClientListWebAclsResponseWebACLsTypeDef", {"WebACLId": str, "Name": str}, total=False
)


class ClientListWebAclsResponseWebACLsTypeDef(_ClientListWebAclsResponseWebACLsTypeDef):
    pass


_ClientListWebAclsResponseTypeDef = TypedDict(
    "_ClientListWebAclsResponseTypeDef",
    {"NextMarker": str, "WebACLs": List[ClientListWebAclsResponseWebACLsTypeDef]},
    total=False,
)


class ClientListWebAclsResponseTypeDef(_ClientListWebAclsResponseTypeDef):
    """
    - *(dict) --*

      - **NextMarker** *(string) --*

        If you have more ``WebACL`` objects than the number that you specified for ``Limit`` in the
        request, the response includes a ``NextMarker`` value. To list more ``WebACL`` objects,
        submit another ``ListWebACLs`` request, and specify the ``NextMarker`` value from the
        response in the ``NextMarker`` value in the next request.
    """


_ClientListXssMatchSetsResponseXssMatchSetsTypeDef = TypedDict(
    "_ClientListXssMatchSetsResponseXssMatchSetsTypeDef",
    {"XssMatchSetId": str, "Name": str},
    total=False,
)


class ClientListXssMatchSetsResponseXssMatchSetsTypeDef(
    _ClientListXssMatchSetsResponseXssMatchSetsTypeDef
):
    pass


_ClientListXssMatchSetsResponseTypeDef = TypedDict(
    "_ClientListXssMatchSetsResponseTypeDef",
    {"NextMarker": str, "XssMatchSets": List[ClientListXssMatchSetsResponseXssMatchSetsTypeDef]},
    total=False,
)


class ClientListXssMatchSetsResponseTypeDef(_ClientListXssMatchSetsResponseTypeDef):
    """
    - *(dict) --*

      The response to a  ListXssMatchSets request.
      - **NextMarker** *(string) --*

        If you have more  XssMatchSet objects than the number that you specified for ``Limit`` in
        the request, the response includes a ``NextMarker`` value. To list more ``XssMatchSet``
        objects, submit another ``ListXssMatchSets`` request, and specify the ``NextMarker`` value
        from the response in the ``NextMarker`` value in the next request.
    """


_ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "_ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef(
    _ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef
):
    pass


_ClientPutLoggingConfigurationLoggingConfigurationTypeDef = TypedDict(
    "_ClientPutLoggingConfigurationLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientPutLoggingConfigurationLoggingConfigurationRedactedFieldsTypeDef
        ],
    },
    total=False,
)


class ClientPutLoggingConfigurationLoggingConfigurationTypeDef(
    _ClientPutLoggingConfigurationLoggingConfigurationTypeDef
):
    """
    The Amazon Kinesis Data Firehose that contains the inspected traffic information, the redacted
    fields details, and the Amazon Resource Name (ARN) of the web ACL to monitor.
    .. note::

      When specifying ``Type`` in ``RedactedFields`` , you must use one of the following values:
      ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` .
    """


_ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef = TypedDict(
    "_ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef(
    _ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef
):
    pass


_ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef = TypedDict(
    "_ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
        "RedactedFields": List[
            ClientPutLoggingConfigurationResponseLoggingConfigurationRedactedFieldsTypeDef
        ],
    },
    total=False,
)


class ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef(
    _ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef
):
    """
    - **LoggingConfiguration** *(dict) --*

      The  LoggingConfiguration that you submitted in the request.
      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the web ACL that you want to associate with
        ``LogDestinationConfigs`` .
    """


_ClientPutLoggingConfigurationResponseTypeDef = TypedDict(
    "_ClientPutLoggingConfigurationResponseTypeDef",
    {"LoggingConfiguration": ClientPutLoggingConfigurationResponseLoggingConfigurationTypeDef},
    total=False,
)


class ClientPutLoggingConfigurationResponseTypeDef(_ClientPutLoggingConfigurationResponseTypeDef):
    """
    - *(dict) --*

      - **LoggingConfiguration** *(dict) --*

        The  LoggingConfiguration that you submitted in the request.
        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the web ACL that you want to associate with
          ``LogDestinationConfigs`` .
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    - *(dict) --*

      - **Key** *(string) --*
      - **Value** *(string) --*
    """


_ClientUpdateByteMatchSetResponseTypeDef = TypedDict(
    "_ClientUpdateByteMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateByteMatchSetResponseTypeDef(_ClientUpdateByteMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateByteMatchSet`` request. You can also
        use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef = TypedDict(
    "_ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef(
    _ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef
):
    pass


_ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef = TypedDict(
    "_ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateByteMatchSetUpdatesByteMatchTupleFieldToMatchTypeDef,
        "TargetString": bytes,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
    total=False,
)


class ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef(
    _ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef
):
    pass


_RequiredClientUpdateByteMatchSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateByteMatchSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateByteMatchSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateByteMatchSetUpdatesTypeDef",
    {"ByteMatchTuple": ClientUpdateByteMatchSetUpdatesByteMatchTupleTypeDef},
    total=False,
)


class ClientUpdateByteMatchSetUpdatesTypeDef(
    _RequiredClientUpdateByteMatchSetUpdatesTypeDef, _OptionalClientUpdateByteMatchSetUpdatesTypeDef
):
    """
    - *(dict) --*

      In an  UpdateByteMatchSet request, ``ByteMatchSetUpdate`` specifies whether to insert or
      delete a  ByteMatchTuple and includes the settings for the ``ByteMatchTuple`` .
      - **Action** *(string) --***[REQUIRED]**

        Specifies whether to insert or delete a  ByteMatchTuple .
    """


_ClientUpdateGeoMatchSetResponseTypeDef = TypedDict(
    "_ClientUpdateGeoMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateGeoMatchSetResponseTypeDef(_ClientUpdateGeoMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateGeoMatchSet`` request. You can also
        use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef = TypedDict(
    "_ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef",
    {
        "Type": str,
        "Value": Literal[
            "AF",
            "AX",
            "AL",
            "DZ",
            "AS",
            "AD",
            "AO",
            "AI",
            "AQ",
            "AG",
            "AR",
            "AM",
            "AW",
            "AU",
            "AT",
            "AZ",
            "BS",
            "BH",
            "BD",
            "BB",
            "BY",
            "BE",
            "BZ",
            "BJ",
            "BM",
            "BT",
            "BO",
            "BQ",
            "BA",
            "BW",
            "BV",
            "BR",
            "IO",
            "BN",
            "BG",
            "BF",
            "BI",
            "KH",
            "CM",
            "CA",
            "CV",
            "KY",
            "CF",
            "TD",
            "CL",
            "CN",
            "CX",
            "CC",
            "CO",
            "KM",
            "CG",
            "CD",
            "CK",
            "CR",
            "CI",
            "HR",
            "CU",
            "CW",
            "CY",
            "CZ",
            "DK",
            "DJ",
            "DM",
            "DO",
            "EC",
            "EG",
            "SV",
            "GQ",
            "ER",
            "EE",
            "ET",
            "FK",
            "FO",
            "FJ",
            "FI",
            "FR",
            "GF",
            "PF",
            "TF",
            "GA",
            "GM",
            "GE",
            "DE",
            "GH",
            "GI",
            "GR",
            "GL",
            "GD",
            "GP",
            "GU",
            "GT",
            "GG",
            "GN",
            "GW",
            "GY",
            "HT",
            "HM",
            "VA",
            "HN",
            "HK",
            "HU",
            "IS",
            "IN",
            "ID",
            "IR",
            "IQ",
            "IE",
            "IM",
            "IL",
            "IT",
            "JM",
            "JP",
            "JE",
            "JO",
            "KZ",
            "KE",
            "KI",
            "KP",
            "KR",
            "KW",
            "KG",
            "LA",
            "LV",
            "LB",
            "LS",
            "LR",
            "LY",
            "LI",
            "LT",
            "LU",
            "MO",
            "MK",
            "MG",
            "MW",
            "MY",
            "MV",
            "ML",
            "MT",
            "MH",
            "MQ",
            "MR",
            "MU",
            "YT",
            "MX",
            "FM",
            "MD",
            "MC",
            "MN",
            "ME",
            "MS",
            "MA",
            "MZ",
            "MM",
            "NA",
            "NR",
            "NP",
            "NL",
            "NC",
            "NZ",
            "NI",
            "NE",
            "NG",
            "NU",
            "NF",
            "MP",
            "NO",
            "OM",
            "PK",
            "PW",
            "PS",
            "PA",
            "PG",
            "PY",
            "PE",
            "PH",
            "PN",
            "PL",
            "PT",
            "PR",
            "QA",
            "RE",
            "RO",
            "RU",
            "RW",
            "BL",
            "SH",
            "KN",
            "LC",
            "MF",
            "PM",
            "VC",
            "WS",
            "SM",
            "ST",
            "SA",
            "SN",
            "RS",
            "SC",
            "SL",
            "SG",
            "SX",
            "SK",
            "SI",
            "SB",
            "SO",
            "ZA",
            "GS",
            "SS",
            "ES",
            "LK",
            "SD",
            "SR",
            "SJ",
            "SZ",
            "SE",
            "CH",
            "SY",
            "TW",
            "TJ",
            "TZ",
            "TH",
            "TL",
            "TG",
            "TK",
            "TO",
            "TT",
            "TN",
            "TR",
            "TM",
            "TC",
            "TV",
            "UG",
            "UA",
            "AE",
            "GB",
            "US",
            "UM",
            "UY",
            "UZ",
            "VU",
            "VE",
            "VN",
            "VG",
            "VI",
            "WF",
            "EH",
            "YE",
            "ZM",
            "ZW",
        ],
    },
    total=False,
)


class ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef(
    _ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef
):
    pass


_RequiredClientUpdateGeoMatchSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateGeoMatchSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateGeoMatchSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateGeoMatchSetUpdatesTypeDef",
    {"GeoMatchConstraint": ClientUpdateGeoMatchSetUpdatesGeoMatchConstraintTypeDef},
    total=False,
)


class ClientUpdateGeoMatchSetUpdatesTypeDef(
    _RequiredClientUpdateGeoMatchSetUpdatesTypeDef, _OptionalClientUpdateGeoMatchSetUpdatesTypeDef
):
    """
    - *(dict) --*

      Specifies the type of update to perform to an  GeoMatchSet with  UpdateGeoMatchSet .
      - **Action** *(string) --***[REQUIRED]**

        Specifies whether to insert or delete a country with  UpdateGeoMatchSet .
    """


_ClientUpdateIpSetResponseTypeDef = TypedDict(
    "_ClientUpdateIpSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateIpSetResponseTypeDef(_ClientUpdateIpSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateIPSet`` request. You can also use
        this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef = TypedDict(
    "_ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef",
    {"Type": Literal["IPV4", "IPV6"], "Value": str},
    total=False,
)


class ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef(
    _ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef
):
    pass


_RequiredClientUpdateIpSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateIpSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateIpSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateIpSetUpdatesTypeDef",
    {"IPSetDescriptor": ClientUpdateIpSetUpdatesIPSetDescriptorTypeDef},
    total=False,
)


class ClientUpdateIpSetUpdatesTypeDef(
    _RequiredClientUpdateIpSetUpdatesTypeDef, _OptionalClientUpdateIpSetUpdatesTypeDef
):
    """
    - *(dict) --*

      Specifies the type of update to perform to an  IPSet with  UpdateIPSet .
      - **Action** *(string) --***[REQUIRED]**

        Specifies whether to insert or delete an IP address with  UpdateIPSet .
    """


_ClientUpdateRateBasedRuleResponseTypeDef = TypedDict(
    "_ClientUpdateRateBasedRuleResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateRateBasedRuleResponseTypeDef(_ClientUpdateRateBasedRuleResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateRateBasedRule`` request. You can
        also use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateRateBasedRuleUpdatesPredicateTypeDef = TypedDict(
    "_ClientUpdateRateBasedRuleUpdatesPredicateTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)


class ClientUpdateRateBasedRuleUpdatesPredicateTypeDef(
    _ClientUpdateRateBasedRuleUpdatesPredicateTypeDef
):
    pass


_RequiredClientUpdateRateBasedRuleUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateRateBasedRuleUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateRateBasedRuleUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateRateBasedRuleUpdatesTypeDef",
    {"Predicate": ClientUpdateRateBasedRuleUpdatesPredicateTypeDef},
    total=False,
)


class ClientUpdateRateBasedRuleUpdatesTypeDef(
    _RequiredClientUpdateRateBasedRuleUpdatesTypeDef,
    _OptionalClientUpdateRateBasedRuleUpdatesTypeDef,
):
    """
    - *(dict) --*

      Specifies a ``Predicate`` (such as an ``IPSet`` ) and indicates whether you want to add it to
      a ``Rule`` or delete it from a ``Rule`` .
      - **Action** *(string) --***[REQUIRED]**

        Specify ``INSERT`` to add a ``Predicate`` to a ``Rule`` . Use ``DELETE`` to remove a
        ``Predicate`` from a ``Rule`` .
    """


_ClientUpdateRegexMatchSetResponseTypeDef = TypedDict(
    "_ClientUpdateRegexMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateRegexMatchSetResponseTypeDef(_ClientUpdateRegexMatchSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateRegexMatchSet`` request. You can
        also use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef = TypedDict(
    "_ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef(
    _ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef
):
    pass


_ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef = TypedDict(
    "_ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateRegexMatchSetUpdatesRegexMatchTupleFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "RegexPatternSetId": str,
    },
    total=False,
)


class ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef(
    _ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef
):
    pass


_RequiredClientUpdateRegexMatchSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateRegexMatchSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateRegexMatchSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateRegexMatchSetUpdatesTypeDef",
    {"RegexMatchTuple": ClientUpdateRegexMatchSetUpdatesRegexMatchTupleTypeDef},
    total=False,
)


class ClientUpdateRegexMatchSetUpdatesTypeDef(
    _RequiredClientUpdateRegexMatchSetUpdatesTypeDef,
    _OptionalClientUpdateRegexMatchSetUpdatesTypeDef,
):
    """
    - *(dict) --*

      In an  UpdateRegexMatchSet request, ``RegexMatchSetUpdate`` specifies whether to insert or
      delete a  RegexMatchTuple and includes the settings for the ``RegexMatchTuple`` .
      - **Action** *(string) --***[REQUIRED]**

        Specifies whether to insert or delete a  RegexMatchTuple .
    """


_ClientUpdateRegexPatternSetResponseTypeDef = TypedDict(
    "_ClientUpdateRegexPatternSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateRegexPatternSetResponseTypeDef(_ClientUpdateRegexPatternSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateRegexPatternSet`` request. You can
        also use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_RequiredClientUpdateRegexPatternSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateRegexPatternSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateRegexPatternSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateRegexPatternSetUpdatesTypeDef", {"RegexPatternString": str}, total=False
)


class ClientUpdateRegexPatternSetUpdatesTypeDef(
    _RequiredClientUpdateRegexPatternSetUpdatesTypeDef,
    _OptionalClientUpdateRegexPatternSetUpdatesTypeDef,
):
    """
    - *(dict) --*

      In an  UpdateRegexPatternSet request, ``RegexPatternSetUpdate`` specifies whether to insert or
      delete a ``RegexPatternString`` and includes the settings for the ``RegexPatternString`` .
      - **Action** *(string) --***[REQUIRED]**

        Specifies whether to insert or delete a ``RegexPatternString`` .
    """


_ClientUpdateRuleGroupResponseTypeDef = TypedDict(
    "_ClientUpdateRuleGroupResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateRuleGroupResponseTypeDef(_ClientUpdateRuleGroupResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateRuleGroup`` request. You can also
        use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef = TypedDict(
    "_ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)


class ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef(
    _ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef
):
    pass


_ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef = TypedDict(
    "_ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef", {"RuleId": str}, total=False
)


class ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef(
    _ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef
):
    pass


_ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef = TypedDict(
    "_ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef",
    {"Type": Literal["NONE", "COUNT"]},
    total=False,
)


class ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef(
    _ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef
):
    pass


_ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef = TypedDict(
    "_ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientUpdateRuleGroupUpdatesActivatedRuleActionTypeDef,
        "OverrideAction": ClientUpdateRuleGroupUpdatesActivatedRuleOverrideActionTypeDef,
        "Type": Literal["REGULAR", "RATE_BASED", "GROUP"],
        "ExcludedRules": List[ClientUpdateRuleGroupUpdatesActivatedRuleExcludedRulesTypeDef],
    },
    total=False,
)


class ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef(
    _ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef
):
    pass


_ClientUpdateRuleGroupUpdatesTypeDef = TypedDict(
    "_ClientUpdateRuleGroupUpdatesTypeDef",
    {
        "Action": Literal["INSERT", "DELETE"],
        "ActivatedRule": ClientUpdateRuleGroupUpdatesActivatedRuleTypeDef,
    },
    total=False,
)


class ClientUpdateRuleGroupUpdatesTypeDef(_ClientUpdateRuleGroupUpdatesTypeDef):
    pass


_ClientUpdateRuleResponseTypeDef = TypedDict(
    "_ClientUpdateRuleResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateRuleResponseTypeDef(_ClientUpdateRuleResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateRule`` request. You can also use
        this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateRuleUpdatesPredicateTypeDef = TypedDict(
    "_ClientUpdateRuleUpdatesPredicateTypeDef",
    {
        "Negated": bool,
        "Type": Literal[
            "IPMatch",
            "ByteMatch",
            "SqlInjectionMatch",
            "GeoMatch",
            "SizeConstraint",
            "XssMatch",
            "RegexMatch",
        ],
        "DataId": str,
    },
    total=False,
)


class ClientUpdateRuleUpdatesPredicateTypeDef(_ClientUpdateRuleUpdatesPredicateTypeDef):
    pass


_RequiredClientUpdateRuleUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateRuleUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateRuleUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateRuleUpdatesTypeDef",
    {"Predicate": ClientUpdateRuleUpdatesPredicateTypeDef},
    total=False,
)


class ClientUpdateRuleUpdatesTypeDef(
    _RequiredClientUpdateRuleUpdatesTypeDef, _OptionalClientUpdateRuleUpdatesTypeDef
):
    """
    - *(dict) --*

      Specifies a ``Predicate`` (such as an ``IPSet`` ) and indicates whether you want to add it to
      a ``Rule`` or delete it from a ``Rule`` .
      - **Action** *(string) --***[REQUIRED]**

        Specify ``INSERT`` to add a ``Predicate`` to a ``Rule`` . Use ``DELETE`` to remove a
        ``Predicate`` from a ``Rule`` .
    """


_ClientUpdateSizeConstraintSetResponseTypeDef = TypedDict(
    "_ClientUpdateSizeConstraintSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateSizeConstraintSetResponseTypeDef(_ClientUpdateSizeConstraintSetResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateSizeConstraintSet`` request. You can
        also use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef = TypedDict(
    "_ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef(
    _ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef
):
    pass


_ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef = TypedDict(
    "_ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef",
    {
        "FieldToMatch": ClientUpdateSizeConstraintSetUpdatesSizeConstraintFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
    },
    total=False,
)


class ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef(
    _ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef
):
    pass


_RequiredClientUpdateSizeConstraintSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateSizeConstraintSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateSizeConstraintSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateSizeConstraintSetUpdatesTypeDef",
    {"SizeConstraint": ClientUpdateSizeConstraintSetUpdatesSizeConstraintTypeDef},
    total=False,
)


class ClientUpdateSizeConstraintSetUpdatesTypeDef(
    _RequiredClientUpdateSizeConstraintSetUpdatesTypeDef,
    _OptionalClientUpdateSizeConstraintSetUpdatesTypeDef,
):
    """
    - *(dict) --*

      Specifies the part of a web request that you want to inspect the size of and indicates whether
      you want to add the specification to a  SizeConstraintSet or delete it from a
      ``SizeConstraintSet`` .
      - **Action** *(string) --***[REQUIRED]**

        Specify ``INSERT`` to add a  SizeConstraintSetUpdate to a  SizeConstraintSet . Use
        ``DELETE`` to remove a ``SizeConstraintSetUpdate`` from a ``SizeConstraintSet`` .
    """


_ClientUpdateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "_ClientUpdateSqlInjectionMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateSqlInjectionMatchSetResponseTypeDef(
    _ClientUpdateSqlInjectionMatchSetResponseTypeDef
):
    """
    - *(dict) --*

      The response to an  UpdateSqlInjectionMatchSets request.
      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateSqlInjectionMatchSet`` request. You
        can also use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef = TypedDict(
    "_ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef(
    _ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef
):
    pass


_ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef = TypedDict(
    "_ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)


class ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef(
    _ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef
):
    pass


_RequiredClientUpdateSqlInjectionMatchSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateSqlInjectionMatchSetUpdatesTypeDef",
    {"Action": Literal["INSERT", "DELETE"]},
)
_OptionalClientUpdateSqlInjectionMatchSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateSqlInjectionMatchSetUpdatesTypeDef",
    {
        "SqlInjectionMatchTuple": ClientUpdateSqlInjectionMatchSetUpdatesSqlInjectionMatchTupleTypeDef
    },
    total=False,
)


class ClientUpdateSqlInjectionMatchSetUpdatesTypeDef(
    _RequiredClientUpdateSqlInjectionMatchSetUpdatesTypeDef,
    _OptionalClientUpdateSqlInjectionMatchSetUpdatesTypeDef,
):
    """
    - *(dict) --*

      Specifies the part of a web request that you want to inspect for snippets of malicious SQL
      code and indicates whether you want to add the specification to a  SqlInjectionMatchSet or
      delete it from a ``SqlInjectionMatchSet`` .
      - **Action** *(string) --***[REQUIRED]**

        Specify ``INSERT`` to add a  SqlInjectionMatchSetUpdate to a  SqlInjectionMatchSet . Use
        ``DELETE`` to remove a ``SqlInjectionMatchSetUpdate`` from a ``SqlInjectionMatchSet`` .
    """


_ClientUpdateWebAclDefaultActionTypeDef = TypedDict(
    "_ClientUpdateWebAclDefaultActionTypeDef", {"Type": Literal["BLOCK", "ALLOW", "COUNT"]}
)


class ClientUpdateWebAclDefaultActionTypeDef(_ClientUpdateWebAclDefaultActionTypeDef):
    """
    A default action for the web ACL, either ALLOW or BLOCK. AWS WAF performs the default action if
    a request doesn't match the criteria in any of the rules in a web ACL.
    - **Type** *(string) --***[REQUIRED]**

      Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` .
      Valid settings include the following:
      * ``ALLOW`` : AWS WAF allows requests
      * ``BLOCK`` : AWS WAF blocks requests
      * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in
      the rule. AWS WAF then continues to inspect the web request based on the remaining rules in
      the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` .
    """


_ClientUpdateWebAclResponseTypeDef = TypedDict(
    "_ClientUpdateWebAclResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateWebAclResponseTypeDef(_ClientUpdateWebAclResponseTypeDef):
    """
    - *(dict) --*

      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateWebACL`` request. You can also use
        this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef = TypedDict(
    "_ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef",
    {"Type": Literal["BLOCK", "ALLOW", "COUNT"]},
    total=False,
)


class ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef(
    _ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef
):
    pass


_ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef = TypedDict(
    "_ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef", {"RuleId": str}, total=False
)


class ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef(
    _ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef
):
    pass


_ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef = TypedDict(
    "_ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef",
    {"Type": Literal["NONE", "COUNT"]},
    total=False,
)


class ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef(
    _ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef
):
    pass


_ClientUpdateWebAclUpdatesActivatedRuleTypeDef = TypedDict(
    "_ClientUpdateWebAclUpdatesActivatedRuleTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": ClientUpdateWebAclUpdatesActivatedRuleActionTypeDef,
        "OverrideAction": ClientUpdateWebAclUpdatesActivatedRuleOverrideActionTypeDef,
        "Type": Literal["REGULAR", "RATE_BASED", "GROUP"],
        "ExcludedRules": List[ClientUpdateWebAclUpdatesActivatedRuleExcludedRulesTypeDef],
    },
    total=False,
)


class ClientUpdateWebAclUpdatesActivatedRuleTypeDef(_ClientUpdateWebAclUpdatesActivatedRuleTypeDef):
    pass


_RequiredClientUpdateWebAclUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateWebAclUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateWebAclUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateWebAclUpdatesTypeDef",
    {"ActivatedRule": ClientUpdateWebAclUpdatesActivatedRuleTypeDef},
    total=False,
)


class ClientUpdateWebAclUpdatesTypeDef(
    _RequiredClientUpdateWebAclUpdatesTypeDef, _OptionalClientUpdateWebAclUpdatesTypeDef
):
    """
    - *(dict) --*

      Specifies whether to insert a ``Rule`` into or delete a ``Rule`` from a ``WebACL`` .
      - **Action** *(string) --***[REQUIRED]**

        Specifies whether to insert a ``Rule`` into or delete a ``Rule`` from a ``WebACL`` .
    """


_ClientUpdateXssMatchSetResponseTypeDef = TypedDict(
    "_ClientUpdateXssMatchSetResponseTypeDef", {"ChangeToken": str}, total=False
)


class ClientUpdateXssMatchSetResponseTypeDef(_ClientUpdateXssMatchSetResponseTypeDef):
    """
    - *(dict) --*

      The response to an  UpdateXssMatchSets request.
      - **ChangeToken** *(string) --*

        The ``ChangeToken`` that you used to submit the ``UpdateXssMatchSet`` request. You can also
        use this value to query the status of the request. For more information, see
        GetChangeTokenStatus .
    """


_ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef = TypedDict(
    "_ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef",
    {
        "Type": Literal[
            "URI", "QUERY_STRING", "HEADER", "METHOD", "BODY", "SINGLE_QUERY_ARG", "ALL_QUERY_ARGS"
        ],
        "Data": str,
    },
    total=False,
)


class ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef(
    _ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef
):
    pass


_ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef = TypedDict(
    "_ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef",
    {
        "FieldToMatch": ClientUpdateXssMatchSetUpdatesXssMatchTupleFieldToMatchTypeDef,
        "TextTransformation": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
    total=False,
)


class ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef(
    _ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef
):
    pass


_RequiredClientUpdateXssMatchSetUpdatesTypeDef = TypedDict(
    "_RequiredClientUpdateXssMatchSetUpdatesTypeDef", {"Action": Literal["INSERT", "DELETE"]}
)
_OptionalClientUpdateXssMatchSetUpdatesTypeDef = TypedDict(
    "_OptionalClientUpdateXssMatchSetUpdatesTypeDef",
    {"XssMatchTuple": ClientUpdateXssMatchSetUpdatesXssMatchTupleTypeDef},
    total=False,
)


class ClientUpdateXssMatchSetUpdatesTypeDef(
    _RequiredClientUpdateXssMatchSetUpdatesTypeDef, _OptionalClientUpdateXssMatchSetUpdatesTypeDef
):
    """
    - *(dict) --*

      Specifies the part of a web request that you want to inspect for cross-site scripting attacks
      and indicates whether you want to add the specification to an  XssMatchSet or delete it from
      an ``XssMatchSet`` .
      - **Action** *(string) --***[REQUIRED]**

        Specify ``INSERT`` to add an  XssMatchSetUpdate to an  XssMatchSet . Use ``DELETE`` to
        remove an ``XssMatchSetUpdate`` from an ``XssMatchSet`` .
    """
