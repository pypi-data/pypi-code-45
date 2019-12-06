"Main interface for inspector service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_inspector.type_defs import (
    ListAssessmentRunAgentsPaginateFilterTypeDef,
    ListAssessmentRunAgentsPaginatePaginationConfigTypeDef,
    ListAssessmentRunAgentsPaginateResponseTypeDef,
    ListAssessmentRunsPaginateFilterTypeDef,
    ListAssessmentRunsPaginatePaginationConfigTypeDef,
    ListAssessmentRunsPaginateResponseTypeDef,
    ListAssessmentTargetsPaginateFilterTypeDef,
    ListAssessmentTargetsPaginatePaginationConfigTypeDef,
    ListAssessmentTargetsPaginateResponseTypeDef,
    ListAssessmentTemplatesPaginateFilterTypeDef,
    ListAssessmentTemplatesPaginatePaginationConfigTypeDef,
    ListAssessmentTemplatesPaginateResponseTypeDef,
    ListEventSubscriptionsPaginatePaginationConfigTypeDef,
    ListEventSubscriptionsPaginateResponseTypeDef,
    ListExclusionsPaginatePaginationConfigTypeDef,
    ListExclusionsPaginateResponseTypeDef,
    ListFindingsPaginateFilterTypeDef,
    ListFindingsPaginatePaginationConfigTypeDef,
    ListFindingsPaginateResponseTypeDef,
    ListRulesPackagesPaginatePaginationConfigTypeDef,
    ListRulesPackagesPaginateResponseTypeDef,
    PreviewAgentsPaginatePaginationConfigTypeDef,
    PreviewAgentsPaginateResponseTypeDef,
)


__all__ = (
    "ListAssessmentRunAgentsPaginator",
    "ListAssessmentRunsPaginator",
    "ListAssessmentTargetsPaginator",
    "ListAssessmentTemplatesPaginator",
    "ListEventSubscriptionsPaginator",
    "ListExclusionsPaginator",
    "ListFindingsPaginator",
    "ListRulesPackagesPaginator",
    "PreviewAgentsPaginator",
)


class ListAssessmentRunAgentsPaginator(Boto3Paginator):
    """
    Paginator for `list_assessment_run_agents`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        assessmentRunArn: str,
        filter: ListAssessmentRunAgentsPaginateFilterTypeDef = None,
        PaginationConfig: ListAssessmentRunAgentsPaginatePaginationConfigTypeDef = None,
    ) -> ListAssessmentRunAgentsPaginateResponseTypeDef:
        """
        [ListAssessmentRunAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRunAgents.paginate)
        """


class ListAssessmentRunsPaginator(Boto3Paginator):
    """
    Paginator for `list_assessment_runs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        assessmentTemplateArns: List[str] = None,
        filter: ListAssessmentRunsPaginateFilterTypeDef = None,
        PaginationConfig: ListAssessmentRunsPaginatePaginationConfigTypeDef = None,
    ) -> ListAssessmentRunsPaginateResponseTypeDef:
        """
        [ListAssessmentRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRuns.paginate)
        """


class ListAssessmentTargetsPaginator(Boto3Paginator):
    """
    Paginator for `list_assessment_targets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filter: ListAssessmentTargetsPaginateFilterTypeDef = None,
        PaginationConfig: ListAssessmentTargetsPaginatePaginationConfigTypeDef = None,
    ) -> ListAssessmentTargetsPaginateResponseTypeDef:
        """
        [ListAssessmentTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTargets.paginate)
        """


class ListAssessmentTemplatesPaginator(Boto3Paginator):
    """
    Paginator for `list_assessment_templates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        assessmentTargetArns: List[str] = None,
        filter: ListAssessmentTemplatesPaginateFilterTypeDef = None,
        PaginationConfig: ListAssessmentTemplatesPaginatePaginationConfigTypeDef = None,
    ) -> ListAssessmentTemplatesPaginateResponseTypeDef:
        """
        [ListAssessmentTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTemplates.paginate)
        """


class ListEventSubscriptionsPaginator(Boto3Paginator):
    """
    Paginator for `list_event_subscriptions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceArn: str = None,
        PaginationConfig: ListEventSubscriptionsPaginatePaginationConfigTypeDef = None,
    ) -> ListEventSubscriptionsPaginateResponseTypeDef:
        """
        [ListEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListEventSubscriptions.paginate)
        """


class ListExclusionsPaginator(Boto3Paginator):
    """
    Paginator for `list_exclusions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        assessmentRunArn: str,
        PaginationConfig: ListExclusionsPaginatePaginationConfigTypeDef = None,
    ) -> ListExclusionsPaginateResponseTypeDef:
        """
        [ListExclusions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListExclusions.paginate)
        """


class ListFindingsPaginator(Boto3Paginator):
    """
    Paginator for `list_findings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        assessmentRunArns: List[str] = None,
        filter: ListFindingsPaginateFilterTypeDef = None,
        PaginationConfig: ListFindingsPaginatePaginationConfigTypeDef = None,
    ) -> ListFindingsPaginateResponseTypeDef:
        """
        [ListFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListFindings.paginate)
        """


class ListRulesPackagesPaginator(Boto3Paginator):
    """
    Paginator for `list_rules_packages`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListRulesPackagesPaginatePaginationConfigTypeDef = None
    ) -> ListRulesPackagesPaginateResponseTypeDef:
        """
        [ListRulesPackages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.ListRulesPackages.paginate)
        """


class PreviewAgentsPaginator(Boto3Paginator):
    """
    Paginator for `preview_agents`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        previewAgentsArn: str,
        PaginationConfig: PreviewAgentsPaginatePaginationConfigTypeDef = None,
    ) -> PreviewAgentsPaginateResponseTypeDef:
        """
        [PreviewAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/inspector.html#Inspector.Paginator.PreviewAgents.paginate)
        """
