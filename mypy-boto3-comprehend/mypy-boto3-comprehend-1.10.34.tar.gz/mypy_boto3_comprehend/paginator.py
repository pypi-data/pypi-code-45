"Main interface for comprehend service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_comprehend.type_defs import (
    ListDocumentClassificationJobsPaginateFilterTypeDef,
    ListDocumentClassificationJobsPaginatePaginationConfigTypeDef,
    ListDocumentClassificationJobsPaginateResponseTypeDef,
    ListDocumentClassifiersPaginateFilterTypeDef,
    ListDocumentClassifiersPaginatePaginationConfigTypeDef,
    ListDocumentClassifiersPaginateResponseTypeDef,
    ListDominantLanguageDetectionJobsPaginateFilterTypeDef,
    ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef,
    ListDominantLanguageDetectionJobsPaginateResponseTypeDef,
    ListEntitiesDetectionJobsPaginateFilterTypeDef,
    ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef,
    ListEntitiesDetectionJobsPaginateResponseTypeDef,
    ListEntityRecognizersPaginateFilterTypeDef,
    ListEntityRecognizersPaginatePaginationConfigTypeDef,
    ListEntityRecognizersPaginateResponseTypeDef,
    ListKeyPhrasesDetectionJobsPaginateFilterTypeDef,
    ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef,
    ListKeyPhrasesDetectionJobsPaginateResponseTypeDef,
    ListSentimentDetectionJobsPaginateFilterTypeDef,
    ListSentimentDetectionJobsPaginatePaginationConfigTypeDef,
    ListSentimentDetectionJobsPaginateResponseTypeDef,
    ListTopicsDetectionJobsPaginateFilterTypeDef,
    ListTopicsDetectionJobsPaginatePaginationConfigTypeDef,
    ListTopicsDetectionJobsPaginateResponseTypeDef,
)


__all__ = (
    "ListDocumentClassificationJobsPaginator",
    "ListDocumentClassifiersPaginator",
    "ListDominantLanguageDetectionJobsPaginator",
    "ListEntitiesDetectionJobsPaginator",
    "ListEntityRecognizersPaginator",
    "ListKeyPhrasesDetectionJobsPaginator",
    "ListSentimentDetectionJobsPaginator",
    "ListTopicsDetectionJobsPaginator",
)


class ListDocumentClassificationJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_document_classification_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListDocumentClassificationJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListDocumentClassificationJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListDocumentClassificationJobsPaginateResponseTypeDef:
        """
        [ListDocumentClassificationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs.paginate)
        """


class ListDocumentClassifiersPaginator(Boto3Paginator):
    """
    Paginator for `list_document_classifiers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListDocumentClassifiersPaginateFilterTypeDef = None,
        PaginationConfig: ListDocumentClassifiersPaginatePaginationConfigTypeDef = None,
    ) -> ListDocumentClassifiersPaginateResponseTypeDef:
        """
        [ListDocumentClassifiers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers.paginate)
        """


class ListDominantLanguageDetectionJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_dominant_language_detection_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListDominantLanguageDetectionJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListDominantLanguageDetectionJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListDominantLanguageDetectionJobsPaginateResponseTypeDef:
        """
        [ListDominantLanguageDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs.paginate)
        """


class ListEntitiesDetectionJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_entities_detection_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListEntitiesDetectionJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListEntitiesDetectionJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListEntitiesDetectionJobsPaginateResponseTypeDef:
        """
        [ListEntitiesDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs.paginate)
        """


class ListEntityRecognizersPaginator(Boto3Paginator):
    """
    Paginator for `list_entity_recognizers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListEntityRecognizersPaginateFilterTypeDef = None,
        PaginationConfig: ListEntityRecognizersPaginatePaginationConfigTypeDef = None,
    ) -> ListEntityRecognizersPaginateResponseTypeDef:
        """
        [ListEntityRecognizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers.paginate)
        """


class ListKeyPhrasesDetectionJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_key_phrases_detection_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListKeyPhrasesDetectionJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListKeyPhrasesDetectionJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListKeyPhrasesDetectionJobsPaginateResponseTypeDef:
        """
        [ListKeyPhrasesDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs.paginate)
        """


class ListSentimentDetectionJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_sentiment_detection_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListSentimentDetectionJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListSentimentDetectionJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListSentimentDetectionJobsPaginateResponseTypeDef:
        """
        [ListSentimentDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs.paginate)
        """


class ListTopicsDetectionJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_topics_detection_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filter: ListTopicsDetectionJobsPaginateFilterTypeDef = None,
        PaginationConfig: ListTopicsDetectionJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListTopicsDetectionJobsPaginateResponseTypeDef:
        """
        [ListTopicsDetectionJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs.paginate)
        """
