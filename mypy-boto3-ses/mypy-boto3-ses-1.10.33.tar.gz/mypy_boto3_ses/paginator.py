"Main interface for ses service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_ses.type_defs import (
    ListConfigurationSetsPaginatePaginationConfigTypeDef,
    ListConfigurationSetsPaginateResponseTypeDef,
    ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef,
    ListCustomVerificationEmailTemplatesPaginateResponseTypeDef,
    ListIdentitiesPaginatePaginationConfigTypeDef,
    ListIdentitiesPaginateResponseTypeDef,
    ListReceiptRuleSetsPaginatePaginationConfigTypeDef,
    ListReceiptRuleSetsPaginateResponseTypeDef,
    ListTemplatesPaginatePaginationConfigTypeDef,
    ListTemplatesPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListConfigurationSetsPaginator",
    "ListCustomVerificationEmailTemplatesPaginator",
    "ListIdentitiesPaginator",
    "ListReceiptRuleSetsPaginator",
    "ListTemplatesPaginator",
)


class ListConfigurationSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_configuration_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListConfigurationSetsPaginatePaginationConfigTypeDef = None
    ) -> ListConfigurationSetsPaginateResponseTypeDef:
        """
        [ListConfigurationSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ses.html#SES.Paginator.ListConfigurationSets.paginate)
        """


class ListCustomVerificationEmailTemplatesPaginator(Boto3Paginator):
    """
    Paginator for `list_custom_verification_email_templates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef = None,
    ) -> ListCustomVerificationEmailTemplatesPaginateResponseTypeDef:
        """
        [ListCustomVerificationEmailTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates.paginate)
        """


class ListIdentitiesPaginator(Boto3Paginator):
    """
    Paginator for `list_identities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        IdentityType: Literal["EmailAddress", "Domain"] = None,
        PaginationConfig: ListIdentitiesPaginatePaginationConfigTypeDef = None,
    ) -> ListIdentitiesPaginateResponseTypeDef:
        """
        [ListIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ses.html#SES.Paginator.ListIdentities.paginate)
        """


class ListReceiptRuleSetsPaginator(Boto3Paginator):
    """
    Paginator for `list_receipt_rule_sets`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListReceiptRuleSetsPaginatePaginationConfigTypeDef = None
    ) -> ListReceiptRuleSetsPaginateResponseTypeDef:
        """
        [ListReceiptRuleSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets.paginate)
        """


class ListTemplatesPaginator(Boto3Paginator):
    """
    Paginator for `list_templates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListTemplatesPaginatePaginationConfigTypeDef = None
    ) -> ListTemplatesPaginateResponseTypeDef:
        """
        [ListTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/ses.html#SES.Paginator.ListTemplates.paginate)
        """
