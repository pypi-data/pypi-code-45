"Main interface for elbv2 service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_elbv2.type_defs import (
    DescribeAccountLimitsPaginatePaginationConfigTypeDef,
    DescribeAccountLimitsPaginateResponseTypeDef,
    DescribeListenerCertificatesPaginatePaginationConfigTypeDef,
    DescribeListenerCertificatesPaginateResponseTypeDef,
    DescribeListenersPaginatePaginationConfigTypeDef,
    DescribeListenersPaginateResponseTypeDef,
    DescribeLoadBalancersPaginatePaginationConfigTypeDef,
    DescribeLoadBalancersPaginateResponseTypeDef,
    DescribeRulesPaginatePaginationConfigTypeDef,
    DescribeRulesPaginateResponseTypeDef,
    DescribeSSLPoliciesPaginatePaginationConfigTypeDef,
    DescribeSSLPoliciesPaginateResponseTypeDef,
    DescribeTargetGroupsPaginatePaginationConfigTypeDef,
    DescribeTargetGroupsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeAccountLimitsPaginator",
    "DescribeListenerCertificatesPaginator",
    "DescribeListenersPaginator",
    "DescribeLoadBalancersPaginator",
    "DescribeRulesPaginator",
    "DescribeSSLPoliciesPaginator",
    "DescribeTargetGroupsPaginator",
)


class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    Paginator for `describe_account_limits`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeAccountLimitsPaginatePaginationConfigTypeDef = None
    ) -> DescribeAccountLimitsPaginateResponseTypeDef:
        """
        [DescribeAccountLimits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeAccountLimits.paginate)
        """


class DescribeListenerCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `describe_listener_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ListenerArn: str,
        PaginationConfig: DescribeListenerCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeListenerCertificatesPaginateResponseTypeDef:
        """
        [DescribeListenerCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListenerCertificates.paginate)
        """


class DescribeListenersPaginator(Boto3Paginator):
    """
    Paginator for `describe_listeners`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LoadBalancerArn: str = None,
        ListenerArns: List[str] = None,
        PaginationConfig: DescribeListenersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeListenersPaginateResponseTypeDef:
        """
        [DescribeListeners.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeListeners.paginate)
        """


class DescribeLoadBalancersPaginator(Boto3Paginator):
    """
    Paginator for `describe_load_balancers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LoadBalancerArns: List[str] = None,
        Names: List[str] = None,
        PaginationConfig: DescribeLoadBalancersPaginatePaginationConfigTypeDef = None,
    ) -> DescribeLoadBalancersPaginateResponseTypeDef:
        """
        [DescribeLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeLoadBalancers.paginate)
        """


class DescribeRulesPaginator(Boto3Paginator):
    """
    Paginator for `describe_rules`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ListenerArn: str = None,
        RuleArns: List[str] = None,
        PaginationConfig: DescribeRulesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeRulesPaginateResponseTypeDef:
        """
        [DescribeRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeRules.paginate)
        """


class DescribeSSLPoliciesPaginator(Boto3Paginator):
    """
    Paginator for `describe_ssl_policies`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: DescribeSSLPoliciesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSSLPoliciesPaginateResponseTypeDef:
        """
        [DescribeSSLPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeSSLPolicies.paginate)
        """


class DescribeTargetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_target_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LoadBalancerArn: str = None,
        TargetGroupArns: List[str] = None,
        Names: List[str] = None,
        PaginationConfig: DescribeTargetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTargetGroupsPaginateResponseTypeDef:
        """
        [DescribeTargetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/elbv2.html#ElasticLoadBalancingv2.Paginator.DescribeTargetGroups.paginate)
        """
