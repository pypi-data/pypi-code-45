"Main interface for mturk service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mturk.type_defs import (
    ListAssignmentsForHITPaginatePaginationConfigTypeDef,
    ListAssignmentsForHITPaginateResponseTypeDef,
    ListBonusPaymentsPaginatePaginationConfigTypeDef,
    ListBonusPaymentsPaginateResponseTypeDef,
    ListHITsForQualificationTypePaginatePaginationConfigTypeDef,
    ListHITsForQualificationTypePaginateResponseTypeDef,
    ListHITsPaginatePaginationConfigTypeDef,
    ListHITsPaginateResponseTypeDef,
    ListQualificationRequestsPaginatePaginationConfigTypeDef,
    ListQualificationRequestsPaginateResponseTypeDef,
    ListQualificationTypesPaginatePaginationConfigTypeDef,
    ListQualificationTypesPaginateResponseTypeDef,
    ListReviewableHITsPaginatePaginationConfigTypeDef,
    ListReviewableHITsPaginateResponseTypeDef,
    ListWorkerBlocksPaginatePaginationConfigTypeDef,
    ListWorkerBlocksPaginateResponseTypeDef,
    ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef,
    ListWorkersWithQualificationTypePaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAssignmentsForHITPaginator",
    "ListBonusPaymentsPaginator",
    "ListHITsPaginator",
    "ListHITsForQualificationTypePaginator",
    "ListQualificationRequestsPaginator",
    "ListQualificationTypesPaginator",
    "ListReviewableHITsPaginator",
    "ListWorkerBlocksPaginator",
    "ListWorkersWithQualificationTypePaginator",
)


class ListAssignmentsForHITPaginator(Boto3Paginator):
    """
    Paginator for `list_assignments_for_hit`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HITId: str,
        AssignmentStatuses: List[Literal["Submitted", "Approved", "Rejected"]] = None,
        PaginationConfig: ListAssignmentsForHITPaginatePaginationConfigTypeDef = None,
    ) -> ListAssignmentsForHITPaginateResponseTypeDef:
        """
        [ListAssignmentsForHIT.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT.paginate)
        """


class ListBonusPaymentsPaginator(Boto3Paginator):
    """
    Paginator for `list_bonus_payments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HITId: str = None,
        AssignmentId: str = None,
        PaginationConfig: ListBonusPaymentsPaginatePaginationConfigTypeDef = None,
    ) -> ListBonusPaymentsPaginateResponseTypeDef:
        """
        [ListBonusPayments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments.paginate)
        """


class ListHITsPaginator(Boto3Paginator):
    """
    Paginator for `list_hits`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListHITsPaginatePaginationConfigTypeDef = None
    ) -> ListHITsPaginateResponseTypeDef:
        """
        [ListHITs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mturk.html#MTurk.Paginator.ListHITs.paginate)
        """


class ListHITsForQualificationTypePaginator(Boto3Paginator):
    """
    Paginator for `list_hits_for_qualification_type`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        QualificationTypeId: str,
        PaginationConfig: ListHITsForQualificationTypePaginatePaginationConfigTypeDef = None,
    ) -> ListHITsForQualificationTypePaginateResponseTypeDef:
        """
        [ListHITsForQualificationType.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType.paginate)
        """


class ListQualificationRequestsPaginator(Boto3Paginator):
    """
    Paginator for `list_qualification_requests`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        QualificationTypeId: str = None,
        PaginationConfig: ListQualificationRequestsPaginatePaginationConfigTypeDef = None,
    ) -> ListQualificationRequestsPaginateResponseTypeDef:
        """
        [ListQualificationRequests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests.paginate)
        """


class ListQualificationTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_qualification_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        MustBeRequestable: bool,
        Query: str = None,
        MustBeOwnedByCaller: bool = None,
        PaginationConfig: ListQualificationTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListQualificationTypesPaginateResponseTypeDef:
        """
        [ListQualificationTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes.paginate)
        """


class ListReviewableHITsPaginator(Boto3Paginator):
    """
    Paginator for `list_reviewable_hits`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HITTypeId: str = None,
        Status: Literal["Reviewable", "Reviewing"] = None,
        PaginationConfig: ListReviewableHITsPaginatePaginationConfigTypeDef = None,
    ) -> ListReviewableHITsPaginateResponseTypeDef:
        """
        [ListReviewableHITs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs.paginate)
        """


class ListWorkerBlocksPaginator(Boto3Paginator):
    """
    Paginator for `list_worker_blocks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListWorkerBlocksPaginatePaginationConfigTypeDef = None
    ) -> ListWorkerBlocksPaginateResponseTypeDef:
        """
        [ListWorkerBlocks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks.paginate)
        """


class ListWorkersWithQualificationTypePaginator(Boto3Paginator):
    """
    Paginator for `list_workers_with_qualification_type`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        QualificationTypeId: str,
        Status: Literal["Granted", "Revoked"] = None,
        PaginationConfig: ListWorkersWithQualificationTypePaginatePaginationConfigTypeDef = None,
    ) -> ListWorkersWithQualificationTypePaginateResponseTypeDef:
        """
        [ListWorkersWithQualificationType.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType.paginate)
        """
