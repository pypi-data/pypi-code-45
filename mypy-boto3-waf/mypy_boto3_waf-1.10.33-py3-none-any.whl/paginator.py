"Main interface for waf service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_waf.type_defs import (
    GetRateBasedRuleManagedKeysPaginatePaginationConfigTypeDef,
    GetRateBasedRuleManagedKeysPaginateResponseTypeDef,
    ListActivatedRulesInRuleGroupPaginatePaginationConfigTypeDef,
    ListActivatedRulesInRuleGroupPaginateResponseTypeDef,
    ListByteMatchSetsPaginatePaginationConfigTypeDef,
    ListByteMatchSetsPaginateResponseTypeDef,
    ListGeoMatchSetsPaginatePaginationConfigTypeDef,
    ListGeoMatchSetsPaginateResponseTypeDef,
    ListIPSetsPaginatePaginationConfigTypeDef,
    ListIPSetsPaginateResponseTypeDef,
    ListLoggingConfigurationsPaginatePaginationConfigTypeDef,
    ListLoggingConfigurationsPaginateResponseTypeDef,
    ListRateBasedRulesPaginatePaginationConfigTypeDef,
    ListRateBasedRulesPaginateResponseTypeDef,
    ListRegexMatchSetsPaginatePaginationConfigTypeDef,
    ListRegexMatchSetsPaginateResponseTypeDef,
    ListRegexPatternSetsPaginatePaginationConfigTypeDef,
    ListRegexPatternSetsPaginateResponseTypeDef,
    ListRuleGroupsPaginatePaginationConfigTypeDef,
    ListRuleGroupsPaginateResponseTypeDef,
    ListRulesPaginatePaginationConfigTypeDef,
    ListRulesPaginateResponseTypeDef,
    ListSizeConstraintSetsPaginatePaginationConfigTypeDef,
    ListSizeConstraintSetsPaginateResponseTypeDef,
    ListSqlInjectionMatchSetsPaginatePaginationConfigTypeDef,
    ListSqlInjectionMatchSetsPaginateResponseTypeDef,
    ListSubscribedRuleGroupsPaginatePaginationConfigTypeDef,
    ListSubscribedRuleGroupsPaginateResponseTypeDef,
    ListWebACLsPaginatePaginationConfigTypeDef,
    ListWebACLsPaginateResponseTypeDef,
    ListXssMatchSetsPaginatePaginationConfigTypeDef,
    ListXssMatchSetsPaginateResponseTypeDef,
)


__all__ = (
    "GetRateBasedRuleManagedKeysPaginator",
    "ListActivatedRulesInRuleGroupPaginator",
    "ListByteMatchSetsPaginator",
    "ListGeoMatchSetsPaginator",
    "ListIPSetsPaginator",
    "ListLoggingConfigurationsPaginator",
    "ListRateBasedRulesPaginator",
    "ListRegexMatchSetsPaginator",
    "ListRegexPatternSetsPaginator",
    "ListRuleGroupsPaginator",
    "ListRulesPaginator",
    "ListSizeConstraintSetsPaginator",
    "ListSqlInjectionMatchSetsPaginator",
    "ListSubscribedRuleGroupsPaginator",
    "ListWebACLsPaginator",
    "ListXssMatchSetsPaginator",
)


class GetRateBasedRuleManagedKeysPaginator(Boto3Paginator):
    """
    Paginator for `get_rate_based_rule_managed_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RuleId: str,
        PaginationConfig: GetRateBasedRuleManagedKeysPaginatePaginationConfigTypeDef = None,
    ) -> GetRateBasedRuleManagedKeysPaginateResponseTypeDef:
        """
        [GetRateBasedRuleManagedKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.GetRateBasedRuleManagedKeys.paginate)
        """


class ListActivatedRulesInRuleGroupPaginator(Boto3Paginator):
    """
    Paginator for `list_activated_rules_in_rule_group`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RuleGroupId: str = None,
        PaginationConfig: ListActivatedRulesInRuleGroupPaginatePaginationConfigTypeDef = None,
    ) -> ListActivatedRulesInRuleGroupPaginateResponseTypeDef:
        """
        [ListActivatedRulesInRuleGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListActivatedRulesInRuleGroup.paginate)
        """


class ListByteMatchSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_byte_match_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListByteMatchSetsPaginatePaginationConfigTypeDef = None
    ) -> ListByteMatchSetsPaginateResponseTypeDef:
        """
        [ListByteMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListByteMatchSets.paginate)
        """


class ListGeoMatchSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_geo_match_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListGeoMatchSetsPaginatePaginationConfigTypeDef = None
    ) -> ListGeoMatchSetsPaginateResponseTypeDef:
        """
        [ListGeoMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListGeoMatchSets.paginate)
        """


class ListIPSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_ip_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListIPSetsPaginatePaginationConfigTypeDef = None
    ) -> ListIPSetsPaginateResponseTypeDef:
        """
        [ListIPSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListIPSets.paginate)
        """


class ListLoggingConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_logging_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListLoggingConfigurationsPaginatePaginationConfigTypeDef = None
    ) -> ListLoggingConfigurationsPaginateResponseTypeDef:
        """
        [ListLoggingConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListLoggingConfigurations.paginate)
        """


class ListRateBasedRulesPaginator(Boto3Paginator):
    """
    Paginator for `list_rate_based_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListRateBasedRulesPaginatePaginationConfigTypeDef = None
    ) -> ListRateBasedRulesPaginateResponseTypeDef:
        """
        [ListRateBasedRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListRateBasedRules.paginate)
        """


class ListRegexMatchSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_regex_match_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListRegexMatchSetsPaginatePaginationConfigTypeDef = None
    ) -> ListRegexMatchSetsPaginateResponseTypeDef:
        """
        [ListRegexMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListRegexMatchSets.paginate)
        """


class ListRegexPatternSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_regex_pattern_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListRegexPatternSetsPaginatePaginationConfigTypeDef = None
    ) -> ListRegexPatternSetsPaginateResponseTypeDef:
        """
        [ListRegexPatternSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListRegexPatternSets.paginate)
        """


class ListRuleGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_rule_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListRuleGroupsPaginatePaginationConfigTypeDef = None
    ) -> ListRuleGroupsPaginateResponseTypeDef:
        """
        [ListRuleGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListRuleGroups.paginate)
        """


class ListRulesPaginator(Boto3Paginator):
    """
    Paginator for `list_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListRulesPaginatePaginationConfigTypeDef = None
    ) -> ListRulesPaginateResponseTypeDef:
        """
        [ListRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListRules.paginate)
        """


class ListSizeConstraintSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_size_constraint_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSizeConstraintSetsPaginatePaginationConfigTypeDef = None
    ) -> ListSizeConstraintSetsPaginateResponseTypeDef:
        """
        [ListSizeConstraintSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListSizeConstraintSets.paginate)
        """


class ListSqlInjectionMatchSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_sql_injection_match_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSqlInjectionMatchSetsPaginatePaginationConfigTypeDef = None
    ) -> ListSqlInjectionMatchSetsPaginateResponseTypeDef:
        """
        [ListSqlInjectionMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListSqlInjectionMatchSets.paginate)
        """


class ListSubscribedRuleGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_subscribed_rule_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSubscribedRuleGroupsPaginatePaginationConfigTypeDef = None
    ) -> ListSubscribedRuleGroupsPaginateResponseTypeDef:
        """
        [ListSubscribedRuleGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListSubscribedRuleGroups.paginate)
        """


class ListWebACLsPaginator(Boto3Paginator):
    """
    Paginator for `list_web_acls`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListWebACLsPaginatePaginationConfigTypeDef = None
    ) -> ListWebACLsPaginateResponseTypeDef:
        """
        [ListWebACLs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListWebACLs.paginate)
        """


class ListXssMatchSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_xss_match_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListXssMatchSetsPaginatePaginationConfigTypeDef = None
    ) -> ListXssMatchSetsPaginateResponseTypeDef:
        """
        [ListXssMatchSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/waf.html#WAF.Paginator.ListXssMatchSets.paginate)
        """
