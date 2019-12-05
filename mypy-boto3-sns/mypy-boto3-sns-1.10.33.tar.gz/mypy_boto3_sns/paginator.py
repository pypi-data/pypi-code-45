"Main interface for sns service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_sns.type_defs import (
    ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef,
    ListEndpointsByPlatformApplicationPaginateResponseTypeDef,
    ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef,
    ListPhoneNumbersOptedOutPaginateResponseTypeDef,
    ListPlatformApplicationsPaginatePaginationConfigTypeDef,
    ListPlatformApplicationsPaginateResponseTypeDef,
    ListSubscriptionsByTopicPaginatePaginationConfigTypeDef,
    ListSubscriptionsByTopicPaginateResponseTypeDef,
    ListSubscriptionsPaginatePaginationConfigTypeDef,
    ListSubscriptionsPaginateResponseTypeDef,
    ListTopicsPaginatePaginationConfigTypeDef,
    ListTopicsPaginateResponseTypeDef,
)


__all__ = (
    "ListEndpointsByPlatformApplicationPaginator",
    "ListPhoneNumbersOptedOutPaginator",
    "ListPlatformApplicationsPaginator",
    "ListSubscriptionsPaginator",
    "ListSubscriptionsByTopicPaginator",
    "ListTopicsPaginator",
)


class ListEndpointsByPlatformApplicationPaginator(Boto3Paginator):
    """
    Paginator for `list_endpoints_by_platform_application`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PlatformApplicationArn: str,
        PaginationConfig: ListEndpointsByPlatformApplicationPaginatePaginationConfigTypeDef = None,
    ) -> ListEndpointsByPlatformApplicationPaginateResponseTypeDef:
        """
        [ListEndpointsByPlatformApplication.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication.paginate)
        """


class ListPhoneNumbersOptedOutPaginator(Boto3Paginator):
    """
    Paginator for `list_phone_numbers_opted_out`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListPhoneNumbersOptedOutPaginatePaginationConfigTypeDef = None
    ) -> ListPhoneNumbersOptedOutPaginateResponseTypeDef:
        """
        [ListPhoneNumbersOptedOut.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut.paginate)
        """


class ListPlatformApplicationsPaginator(Boto3Paginator):
    """
    Paginator for `list_platform_applications`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListPlatformApplicationsPaginatePaginationConfigTypeDef = None
    ) -> ListPlatformApplicationsPaginateResponseTypeDef:
        """
        [ListPlatformApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.Paginator.ListPlatformApplications.paginate)
        """


class ListSubscriptionsPaginator(Boto3Paginator):
    """
    Paginator for `list_subscriptions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSubscriptionsPaginatePaginationConfigTypeDef = None
    ) -> ListSubscriptionsPaginateResponseTypeDef:
        """
        [ListSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.Paginator.ListSubscriptions.paginate)
        """


class ListSubscriptionsByTopicPaginator(Boto3Paginator):
    """
    Paginator for `list_subscriptions_by_topic`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        TopicArn: str,
        PaginationConfig: ListSubscriptionsByTopicPaginatePaginationConfigTypeDef = None,
    ) -> ListSubscriptionsByTopicPaginateResponseTypeDef:
        """
        [ListSubscriptionsByTopic.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic.paginate)
        """


class ListTopicsPaginator(Boto3Paginator):
    """
    Paginator for `list_topics`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListTopicsPaginatePaginationConfigTypeDef = None
    ) -> ListTopicsPaginateResponseTypeDef:
        """
        [ListTopics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/sns.html#SNS.Paginator.ListTopics.paginate)
        """
