"Main interface for emr service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_emr.type_defs import (
    ListBootstrapActionsPaginatePaginationConfigTypeDef,
    ListBootstrapActionsPaginateResponseTypeDef,
    ListClustersPaginatePaginationConfigTypeDef,
    ListClustersPaginateResponseTypeDef,
    ListInstanceFleetsPaginatePaginationConfigTypeDef,
    ListInstanceFleetsPaginateResponseTypeDef,
    ListInstanceGroupsPaginatePaginationConfigTypeDef,
    ListInstanceGroupsPaginateResponseTypeDef,
    ListInstancesPaginatePaginationConfigTypeDef,
    ListInstancesPaginateResponseTypeDef,
    ListSecurityConfigurationsPaginatePaginationConfigTypeDef,
    ListSecurityConfigurationsPaginateResponseTypeDef,
    ListStepsPaginatePaginationConfigTypeDef,
    ListStepsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListBootstrapActionsPaginator",
    "ListClustersPaginator",
    "ListInstanceFleetsPaginator",
    "ListInstanceGroupsPaginator",
    "ListInstancesPaginator",
    "ListSecurityConfigurationsPaginator",
    "ListStepsPaginator",
)


class ListBootstrapActionsPaginator(Boto3Paginator):
    """
    Paginator for `list_bootstrap_actions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: ListBootstrapActionsPaginatePaginationConfigTypeDef = None,
    ) -> ListBootstrapActionsPaginateResponseTypeDef:
        """
        [ListBootstrapActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/emr.html#EMR.Paginator.ListBootstrapActions.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    Paginator for `list_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        ClusterStates: List[
            Literal[
                "STARTING",
                "BOOTSTRAPPING",
                "RUNNING",
                "WAITING",
                "TERMINATING",
                "TERMINATED",
                "TERMINATED_WITH_ERRORS",
            ]
        ] = None,
        PaginationConfig: ListClustersPaginatePaginationConfigTypeDef = None,
    ) -> ListClustersPaginateResponseTypeDef:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/emr.html#EMR.Paginator.ListClusters.paginate)
        """


class ListInstanceFleetsPaginator(Boto3Paginator):
    """
    Paginator for `list_instance_fleets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: ListInstanceFleetsPaginatePaginationConfigTypeDef = None,
    ) -> ListInstanceFleetsPaginateResponseTypeDef:
        """
        [ListInstanceFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/emr.html#EMR.Paginator.ListInstanceFleets.paginate)
        """


class ListInstanceGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_instance_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: ListInstanceGroupsPaginatePaginationConfigTypeDef = None,
    ) -> ListInstanceGroupsPaginateResponseTypeDef:
        """
        [ListInstanceGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/emr.html#EMR.Paginator.ListInstanceGroups.paginate)
        """


class ListInstancesPaginator(Boto3Paginator):
    """
    Paginator for `list_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[Literal["MASTER", "CORE", "TASK"]] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: Literal["MASTER", "CORE", "TASK"] = None,
        InstanceStates: List[
            Literal[
                "AWAITING_FULFILLMENT", "PROVISIONING", "BOOTSTRAPPING", "RUNNING", "TERMINATED"
            ]
        ] = None,
        PaginationConfig: ListInstancesPaginatePaginationConfigTypeDef = None,
    ) -> ListInstancesPaginateResponseTypeDef:
        """
        [ListInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/emr.html#EMR.Paginator.ListInstances.paginate)
        """


class ListSecurityConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_security_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSecurityConfigurationsPaginatePaginationConfigTypeDef = None
    ) -> ListSecurityConfigurationsPaginateResponseTypeDef:
        """
        [ListSecurityConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations.paginate)
        """


class ListStepsPaginator(Boto3Paginator):
    """
    Paginator for `list_steps`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterId: str,
        StepStates: List[
            Literal[
                "PENDING",
                "CANCEL_PENDING",
                "RUNNING",
                "COMPLETED",
                "CANCELLED",
                "FAILED",
                "INTERRUPTED",
            ]
        ] = None,
        StepIds: List[str] = None,
        PaginationConfig: ListStepsPaginatePaginationConfigTypeDef = None,
    ) -> ListStepsPaginateResponseTypeDef:
        """
        [ListSteps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/emr.html#EMR.Paginator.ListSteps.paginate)
        """
