"Main interface for mediaconvert service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediaconvert.type_defs import (
    DescribeEndpointsPaginatePaginationConfigTypeDef,
    DescribeEndpointsPaginateResponseTypeDef,
    ListJobTemplatesPaginatePaginationConfigTypeDef,
    ListJobTemplatesPaginateResponseTypeDef,
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
    ListPresetsPaginatePaginationConfigTypeDef,
    ListPresetsPaginateResponseTypeDef,
    ListQueuesPaginatePaginationConfigTypeDef,
    ListQueuesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeEndpointsPaginator",
    "ListJobTemplatesPaginator",
    "ListJobsPaginator",
    "ListPresetsPaginator",
    "ListQueuesPaginator",
)


class DescribeEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `describe_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Mode: Literal["DEFAULT", "GET_ONLY"] = None,
        PaginationConfig: DescribeEndpointsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEndpointsPaginateResponseTypeDef:
        """
        [DescribeEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints.paginate)
        """


class ListJobTemplatesPaginator(Boto3Paginator):
    """
    Paginator for `list_job_templates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Category: str = None,
        ListBy: Literal["NAME", "CREATION_DATE", "SYSTEM"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: ListJobTemplatesPaginatePaginationConfigTypeDef = None,
    ) -> ListJobTemplatesPaginateResponseTypeDef:
        """
        [ListJobTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Queue: str = None,
        Status: Literal["SUBMITTED", "PROGRESSING", "COMPLETE", "CANCELED", "ERROR"] = None,
        PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListJobsPaginateResponseTypeDef:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs.paginate)
        """


class ListPresetsPaginator(Boto3Paginator):
    """
    Paginator for `list_presets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Category: str = None,
        ListBy: Literal["NAME", "CREATION_DATE", "SYSTEM"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: ListPresetsPaginatePaginationConfigTypeDef = None,
    ) -> ListPresetsPaginateResponseTypeDef:
        """
        [ListPresets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets.paginate)
        """


class ListQueuesPaginator(Boto3Paginator):
    """
    Paginator for `list_queues`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ListBy: Literal["NAME", "CREATION_DATE"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: ListQueuesPaginatePaginationConfigTypeDef = None,
    ) -> ListQueuesPaginateResponseTypeDef:
        """
        [ListQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues.paginate)
        """
