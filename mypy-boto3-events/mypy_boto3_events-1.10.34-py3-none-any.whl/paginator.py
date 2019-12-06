"Main interface for events service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_events.type_defs import (
    ListRuleNamesByTargetPaginatePaginationConfigTypeDef,
    ListRuleNamesByTargetPaginateResponseTypeDef,
    ListRulesPaginatePaginationConfigTypeDef,
    ListRulesPaginateResponseTypeDef,
    ListTargetsByRulePaginatePaginationConfigTypeDef,
    ListTargetsByRulePaginateResponseTypeDef,
)


__all__ = ("ListRuleNamesByTargetPaginator", "ListRulesPaginator", "ListTargetsByRulePaginator")


class ListRuleNamesByTargetPaginator(Boto3Paginator):
    """
    Paginator for `list_rule_names_by_target`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TargetArn: str,
        EventBusName: str = None,
        PaginationConfig: ListRuleNamesByTargetPaginatePaginationConfigTypeDef = None,
    ) -> ListRuleNamesByTargetPaginateResponseTypeDef:
        """
        [ListRuleNamesByTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/events.html#EventBridge.Paginator.ListRuleNamesByTarget.paginate)
        """


class ListRulesPaginator(Boto3Paginator):
    """
    Paginator for `list_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        NamePrefix: str = None,
        EventBusName: str = None,
        PaginationConfig: ListRulesPaginatePaginationConfigTypeDef = None,
    ) -> ListRulesPaginateResponseTypeDef:
        """
        [ListRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/events.html#EventBridge.Paginator.ListRules.paginate)
        """


class ListTargetsByRulePaginator(Boto3Paginator):
    """
    Paginator for `list_targets_by_rule`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Rule: str,
        EventBusName: str = None,
        PaginationConfig: ListTargetsByRulePaginatePaginationConfigTypeDef = None,
    ) -> ListTargetsByRulePaginateResponseTypeDef:
        """
        [ListTargetsByRule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/events.html#EventBridge.Paginator.ListTargetsByRule.paginate)
        """
