"Main interface for codedeploy service Paginators"
from __future__ import annotations

import sys
from typing import Dict, List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codedeploy.type_defs import (
    ListApplicationRevisionsPaginatePaginationConfigTypeDef,
    ListApplicationRevisionsPaginateResponseTypeDef,
    ListApplicationsPaginatePaginationConfigTypeDef,
    ListApplicationsPaginateResponseTypeDef,
    ListDeploymentConfigsPaginatePaginationConfigTypeDef,
    ListDeploymentConfigsPaginateResponseTypeDef,
    ListDeploymentGroupsPaginatePaginationConfigTypeDef,
    ListDeploymentGroupsPaginateResponseTypeDef,
    ListDeploymentInstancesPaginatePaginationConfigTypeDef,
    ListDeploymentInstancesPaginateResponseTypeDef,
    ListDeploymentTargetsPaginatePaginationConfigTypeDef,
    ListDeploymentTargetsPaginateResponseTypeDef,
    ListDeploymentsPaginateCreateTimeRangeTypeDef,
    ListDeploymentsPaginatePaginationConfigTypeDef,
    ListDeploymentsPaginateResponseTypeDef,
    ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef,
    ListGitHubAccountTokenNamesPaginateResponseTypeDef,
    ListOnPremisesInstancesPaginatePaginationConfigTypeDef,
    ListOnPremisesInstancesPaginateResponseTypeDef,
    ListOnPremisesInstancesPaginateTagFiltersTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListApplicationRevisionsPaginator",
    "ListApplicationsPaginator",
    "ListDeploymentConfigsPaginator",
    "ListDeploymentGroupsPaginator",
    "ListDeploymentInstancesPaginator",
    "ListDeploymentTargetsPaginator",
    "ListDeploymentsPaginator",
    "ListGitHubAccountTokenNamesPaginator",
    "ListOnPremisesInstancesPaginator",
)


class ListApplicationRevisionsPaginator(Boto3Paginator):
    """
    Paginator for `list_application_revisions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        applicationName: str,
        sortBy: Literal["registerTime", "firstUsedTime", "lastUsedTime"] = None,
        sortOrder: Literal["ascending", "descending"] = None,
        s3Bucket: str = None,
        s3KeyPrefix: str = None,
        deployed: Literal["include", "exclude", "ignore"] = None,
        PaginationConfig: ListApplicationRevisionsPaginatePaginationConfigTypeDef = None,
    ) -> ListApplicationRevisionsPaginateResponseTypeDef:
        """
        [ListApplicationRevisions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions.paginate)
        """


class ListApplicationsPaginator(Boto3Paginator):
    """
    Paginator for `list_applications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListApplicationsPaginatePaginationConfigTypeDef = None
    ) -> ListApplicationsPaginateResponseTypeDef:
        """
        [ListApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications.paginate)
        """


class ListDeploymentConfigsPaginator(Boto3Paginator):
    """
    Paginator for `list_deployment_configs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDeploymentConfigsPaginatePaginationConfigTypeDef = None
    ) -> ListDeploymentConfigsPaginateResponseTypeDef:
        """
        [ListDeploymentConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs.paginate)
        """


class ListDeploymentGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_deployment_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        applicationName: str,
        PaginationConfig: ListDeploymentGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeploymentGroupsPaginateResponseTypeDef:
        """
        [ListDeploymentGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups.paginate)
        """


class ListDeploymentInstancesPaginator(Boto3Paginator):
    """
    Paginator for `list_deployment_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        deploymentId: str,
        instanceStatusFilter: List[
            Literal["Pending", "InProgress", "Succeeded", "Failed", "Skipped", "Unknown", "Ready"]
        ] = None,
        instanceTypeFilter: List[Literal["Blue", "Green"]] = None,
        PaginationConfig: ListDeploymentInstancesPaginatePaginationConfigTypeDef = None,
    ) -> ListDeploymentInstancesPaginateResponseTypeDef:
        """
        [ListDeploymentInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances.paginate)
        """


class ListDeploymentTargetsPaginator(Boto3Paginator):
    """
    Paginator for `list_deployment_targets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        deploymentId: str = None,
        targetFilters: Dict[str, List[str]] = None,
        PaginationConfig: ListDeploymentTargetsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeploymentTargetsPaginateResponseTypeDef:
        """
        [ListDeploymentTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets.paginate)
        """


class ListDeploymentsPaginator(Boto3Paginator):
    """
    Paginator for `list_deployments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        applicationName: str = None,
        deploymentGroupName: str = None,
        includeOnlyStatuses: List[
            Literal["Created", "Queued", "InProgress", "Succeeded", "Failed", "Stopped", "Ready"]
        ] = None,
        createTimeRange: ListDeploymentsPaginateCreateTimeRangeTypeDef = None,
        PaginationConfig: ListDeploymentsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeploymentsPaginateResponseTypeDef:
        """
        [ListDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments.paginate)
        """


class ListGitHubAccountTokenNamesPaginator(Boto3Paginator):
    """
    Paginator for `list_git_hub_account_token_names`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListGitHubAccountTokenNamesPaginatePaginationConfigTypeDef = None
    ) -> ListGitHubAccountTokenNamesPaginateResponseTypeDef:
        """
        [ListGitHubAccountTokenNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames.paginate)
        """


class ListOnPremisesInstancesPaginator(Boto3Paginator):
    """
    Paginator for `list_on_premises_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        registrationStatus: Literal["Registered", "Deregistered"] = None,
        tagFilters: List[ListOnPremisesInstancesPaginateTagFiltersTypeDef] = None,
        PaginationConfig: ListOnPremisesInstancesPaginatePaginationConfigTypeDef = None,
    ) -> ListOnPremisesInstancesPaginateResponseTypeDef:
        """
        [ListOnPremisesInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances.paginate)
        """
