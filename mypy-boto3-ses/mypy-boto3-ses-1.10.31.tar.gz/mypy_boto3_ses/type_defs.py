"Main interface for ses service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateConfigurationSetConfigurationSetTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    "ClientCreateReceiptFilterFilterIpFilterTypeDef",
    "ClientCreateReceiptFilterFilterTypeDef",
    "ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsBounceActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsS3ActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsSNSActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsStopActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef",
    "ClientCreateReceiptRuleRuleActionsTypeDef",
    "ClientCreateReceiptRuleRuleTypeDef",
    "ClientCreateTemplateTemplateTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef",
    "ClientDescribeActiveReceiptRuleSetResponseTypeDef",
    "ClientDescribeConfigurationSetResponseConfigurationSetTypeDef",
    "ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef",
    "ClientDescribeConfigurationSetResponseEventDestinationsTypeDef",
    "ClientDescribeConfigurationSetResponseReputationOptionsTypeDef",
    "ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef",
    "ClientDescribeConfigurationSetResponseTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef",
    "ClientDescribeReceiptRuleResponseRuleActionsTypeDef",
    "ClientDescribeReceiptRuleResponseRuleTypeDef",
    "ClientDescribeReceiptRuleResponseTypeDef",
    "ClientDescribeReceiptRuleSetResponseMetadataTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef",
    "ClientDescribeReceiptRuleSetResponseRulesTypeDef",
    "ClientDescribeReceiptRuleSetResponseTypeDef",
    "ClientGetAccountSendingEnabledResponseTypeDef",
    "ClientGetCustomVerificationEmailTemplateResponseTypeDef",
    "ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef",
    "ClientGetIdentityDkimAttributesResponseTypeDef",
    "ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef",
    "ClientGetIdentityMailFromDomainAttributesResponseTypeDef",
    "ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef",
    "ClientGetIdentityNotificationAttributesResponseTypeDef",
    "ClientGetIdentityPoliciesResponseTypeDef",
    "ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef",
    "ClientGetIdentityVerificationAttributesResponseTypeDef",
    "ClientGetSendQuotaResponseTypeDef",
    "ClientGetSendStatisticsResponseSendDataPointsTypeDef",
    "ClientGetSendStatisticsResponseTypeDef",
    "ClientGetTemplateResponseTemplateTypeDef",
    "ClientGetTemplateResponseTypeDef",
    "ClientListConfigurationSetsResponseConfigurationSetsTypeDef",
    "ClientListConfigurationSetsResponseTypeDef",
    "ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef",
    "ClientListCustomVerificationEmailTemplatesResponseTypeDef",
    "ClientListIdentitiesResponseTypeDef",
    "ClientListIdentityPoliciesResponseTypeDef",
    "ClientListReceiptFiltersResponseFiltersIpFilterTypeDef",
    "ClientListReceiptFiltersResponseFiltersTypeDef",
    "ClientListReceiptFiltersResponseTypeDef",
    "ClientListReceiptRuleSetsResponseRuleSetsTypeDef",
    "ClientListReceiptRuleSetsResponseTypeDef",
    "ClientListTemplatesResponseTemplatesMetadataTypeDef",
    "ClientListTemplatesResponseTypeDef",
    "ClientListVerifiedEmailAddressesResponseTypeDef",
    "ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef",
    "ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef",
    "ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef",
    "ClientSendBounceBouncedRecipientInfoListTypeDef",
    "ClientSendBounceMessageDsnExtensionFieldsTypeDef",
    "ClientSendBounceMessageDsnTypeDef",
    "ClientSendBounceResponseTypeDef",
    "ClientSendBulkTemplatedEmailDefaultTagsTypeDef",
    "ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef",
    "ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef",
    "ClientSendBulkTemplatedEmailDestinationsTypeDef",
    "ClientSendBulkTemplatedEmailResponseStatusTypeDef",
    "ClientSendBulkTemplatedEmailResponseTypeDef",
    "ClientSendCustomVerificationEmailResponseTypeDef",
    "ClientSendEmailDestinationTypeDef",
    "ClientSendEmailMessageBodyHtmlTypeDef",
    "ClientSendEmailMessageBodyTextTypeDef",
    "ClientSendEmailMessageBodyTypeDef",
    "ClientSendEmailMessageSubjectTypeDef",
    "ClientSendEmailMessageTypeDef",
    "ClientSendEmailResponseTypeDef",
    "ClientSendEmailTagsTypeDef",
    "ClientSendRawEmailRawMessageTypeDef",
    "ClientSendRawEmailResponseTypeDef",
    "ClientSendRawEmailTagsTypeDef",
    "ClientSendTemplatedEmailDestinationTypeDef",
    "ClientSendTemplatedEmailResponseTypeDef",
    "ClientSendTemplatedEmailTagsTypeDef",
    "ClientTestRenderTemplateResponseTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    "ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsStopActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef",
    "ClientUpdateReceiptRuleRuleActionsTypeDef",
    "ClientUpdateReceiptRuleRuleTypeDef",
    "ClientUpdateTemplateTemplateTypeDef",
    "ClientVerifyDomainDkimResponseTypeDef",
    "ClientVerifyDomainIdentityResponseTypeDef",
    "IdentityExistsWaitWaiterConfigTypeDef",
    "ListConfigurationSetsPaginatePaginationConfigTypeDef",
    "ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef",
    "ListConfigurationSetsPaginateResponseTypeDef",
    "ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef",
    "ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef",
    "ListCustomVerificationEmailTemplatesPaginateResponseTypeDef",
    "ListIdentitiesPaginatePaginationConfigTypeDef",
    "ListIdentitiesPaginateResponseTypeDef",
    "ListReceiptRuleSetsPaginatePaginationConfigTypeDef",
    "ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef",
    "ListReceiptRuleSetsPaginateResponseTypeDef",
    "ListTemplatesPaginatePaginationConfigTypeDef",
    "ListTemplatesPaginateResponseTemplatesMetadataTypeDef",
    "ListTemplatesPaginateResponseTypeDef",
)


_ClientCreateConfigurationSetConfigurationSetTypeDef = TypedDict(
    "_ClientCreateConfigurationSetConfigurationSetTypeDef", {"Name": str}
)


class ClientCreateConfigurationSetConfigurationSetTypeDef(
    _ClientCreateConfigurationSetConfigurationSetTypeDef
):
    """
    A data structure that contains the name of the configuration set.
    - **Name** *(string) --***[REQUIRED]**

      The name of the configuration set. The name must meet the following requirements:
      * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
      * Contain 64 characters or fewer.
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["messageTag", "emailHeader", "linkTag"],
        "DefaultDimensionValue": str,
    },
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef
):
    pass


_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef
):
    pass


_ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"IAMRoleARN": str, "DeliveryStreamARN": str},
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef
):
    pass


_ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    {"TopicARN": str},
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef
):
    pass


_RequiredClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_RequiredClientCreateConfigurationSetEventDestinationEventDestinationTypeDef", {"Name": str}
)
_OptionalClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_OptionalClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "send",
                "reject",
                "bounce",
                "complaint",
                "delivery",
                "open",
                "click",
                "renderingFailure",
            ]
        ],
        "KinesisFirehoseDestination": ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SNSDestination": ClientCreateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef,
    },
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef(
    _RequiredClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
    _OptionalClientCreateConfigurationSetEventDestinationEventDestinationTypeDef,
):
    """
    An object that describes the AWS service that email sending event information will be published
    to.
    - **Name** *(string) --***[REQUIRED]**

      The name of the event destination. The name must:
      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).
      * Contain less than 64 characters.
    """


_ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)


class ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef(
    _ClientCreateConfigurationSetTrackingOptionsTrackingOptionsTypeDef
):
    """
    A domain that is used to redirect email recipients to an Amazon SES-operated domain. This domain
    captures open and click events generated by Amazon SES emails.
    For more information, see `Configuring Custom Domains to Handle Open and Click Tracking
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html>`__
    in the *Amazon SES Developer Guide* .
    - **CustomRedirectDomain** *(string) --*

      The custom subdomain that will be used to redirect email recipients to the Amazon SES event
      tracking domain.
    """


_ClientCreateReceiptFilterFilterIpFilterTypeDef = TypedDict(
    "_ClientCreateReceiptFilterFilterIpFilterTypeDef",
    {"Policy": Literal["Block", "Allow"], "Cidr": str},
    total=False,
)


class ClientCreateReceiptFilterFilterIpFilterTypeDef(
    _ClientCreateReceiptFilterFilterIpFilterTypeDef
):
    pass


_RequiredClientCreateReceiptFilterFilterTypeDef = TypedDict(
    "_RequiredClientCreateReceiptFilterFilterTypeDef", {"Name": str}
)
_OptionalClientCreateReceiptFilterFilterTypeDef = TypedDict(
    "_OptionalClientCreateReceiptFilterFilterTypeDef",
    {"IpFilter": ClientCreateReceiptFilterFilterIpFilterTypeDef},
    total=False,
)


class ClientCreateReceiptFilterFilterTypeDef(
    _RequiredClientCreateReceiptFilterFilterTypeDef, _OptionalClientCreateReceiptFilterFilterTypeDef
):
    """
    A data structure that describes the IP address filter to create, which consists of a name, an IP
    address range, and whether to allow or block mail from it.
    - **Name** *(string) --***[REQUIRED]**

      The name of the IP address filter. The name must:
      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).
      * Start and end with a letter or number.
      * Contain less than 64 characters.
    """


_ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef = TypedDict(
    "_ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef(
    _ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef
):
    pass


_ClientCreateReceiptRuleRuleActionsBounceActionTypeDef = TypedDict(
    "_ClientCreateReceiptRuleRuleActionsBounceActionTypeDef",
    {"TopicArn": str, "SmtpReplyCode": str, "StatusCode": str, "Message": str, "Sender": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsBounceActionTypeDef(
    _ClientCreateReceiptRuleRuleActionsBounceActionTypeDef
):
    pass


_ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef = TypedDict(
    "_ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef(
    _ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef
):
    pass


_ClientCreateReceiptRuleRuleActionsS3ActionTypeDef = TypedDict(
    "_ClientCreateReceiptRuleRuleActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsS3ActionTypeDef(
    _ClientCreateReceiptRuleRuleActionsS3ActionTypeDef
):
    pass


_ClientCreateReceiptRuleRuleActionsSNSActionTypeDef = TypedDict(
    "_ClientCreateReceiptRuleRuleActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": Literal["UTF-8", "Base64"]},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsSNSActionTypeDef(
    _ClientCreateReceiptRuleRuleActionsSNSActionTypeDef
):
    pass


_ClientCreateReceiptRuleRuleActionsStopActionTypeDef = TypedDict(
    "_ClientCreateReceiptRuleRuleActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsStopActionTypeDef(
    _ClientCreateReceiptRuleRuleActionsStopActionTypeDef
):
    pass


_ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef = TypedDict(
    "_ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)


class ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef(
    _ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef
):
    pass


_ClientCreateReceiptRuleRuleActionsTypeDef = TypedDict(
    "_ClientCreateReceiptRuleRuleActionsTypeDef",
    {
        "S3Action": ClientCreateReceiptRuleRuleActionsS3ActionTypeDef,
        "BounceAction": ClientCreateReceiptRuleRuleActionsBounceActionTypeDef,
        "WorkmailAction": ClientCreateReceiptRuleRuleActionsWorkmailActionTypeDef,
        "LambdaAction": ClientCreateReceiptRuleRuleActionsLambdaActionTypeDef,
        "StopAction": ClientCreateReceiptRuleRuleActionsStopActionTypeDef,
        "AddHeaderAction": ClientCreateReceiptRuleRuleActionsAddHeaderActionTypeDef,
        "SNSAction": ClientCreateReceiptRuleRuleActionsSNSActionTypeDef,
    },
    total=False,
)


class ClientCreateReceiptRuleRuleActionsTypeDef(_ClientCreateReceiptRuleRuleActionsTypeDef):
    pass


_RequiredClientCreateReceiptRuleRuleTypeDef = TypedDict(
    "_RequiredClientCreateReceiptRuleRuleTypeDef", {"Name": str}
)
_OptionalClientCreateReceiptRuleRuleTypeDef = TypedDict(
    "_OptionalClientCreateReceiptRuleRuleTypeDef",
    {
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List[ClientCreateReceiptRuleRuleActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientCreateReceiptRuleRuleTypeDef(
    _RequiredClientCreateReceiptRuleRuleTypeDef, _OptionalClientCreateReceiptRuleRuleTypeDef
):
    """
    A data structure that contains the specified rule's name, actions, recipients, domains, enabled
    status, scan status, and TLS policy.
    - **Name** *(string) --***[REQUIRED]**

      The name of the receipt rule. The name must:
      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).
      * Start and end with a letter or number.
      * Contain less than 64 characters.
    """


_RequiredClientCreateTemplateTemplateTypeDef = TypedDict(
    "_RequiredClientCreateTemplateTemplateTypeDef", {"TemplateName": str}
)
_OptionalClientCreateTemplateTemplateTypeDef = TypedDict(
    "_OptionalClientCreateTemplateTemplateTypeDef",
    {"SubjectPart": str, "TextPart": str, "HtmlPart": str},
    total=False,
)


class ClientCreateTemplateTemplateTypeDef(
    _RequiredClientCreateTemplateTemplateTypeDef, _OptionalClientCreateTemplateTemplateTypeDef
):
    """
    The content of the email, composed of a subject line, an HTML part, and a text-only part.
    - **TemplateName** *(string) --***[REQUIRED]**

      The name of the template. You will refer to this name when you send email using the
      ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.
    """


_ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef
):
    """
    - **Metadata** *(dict) --*

      The metadata for the currently active receipt rule set. The metadata consists of the rule set
      name and a timestamp of when the rule set was created.
      - **Name** *(string) --*

        The name of the receipt rule set. The name must:
        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).
        * Start and end with a letter or number.
        * Contain less than 64 characters.
    """


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef
):
    pass


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    {"TopicArn": str, "SmtpReplyCode": str, "StatusCode": str, "Message": str, "Sender": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef
):
    pass


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef
):
    pass


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef
):
    pass


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": Literal["UTF-8", "Base64"]},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef
):
    pass


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef
):
    pass


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef
):
    pass


_ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef",
    {
        "S3Action": ClientDescribeActiveReceiptRuleSetResponseRulesActionsS3ActionTypeDef,
        "BounceAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsBounceActionTypeDef,
        "WorkmailAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef,
        "LambdaAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsLambdaActionTypeDef,
        "StopAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsStopActionTypeDef,
        "AddHeaderAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef,
        "SNSAction": ClientDescribeActiveReceiptRuleSetResponseRulesActionsSNSActionTypeDef,
    },
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef
):
    pass


_ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List[ClientDescribeActiveReceiptRuleSetResponseRulesActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef
):
    pass


_ClientDescribeActiveReceiptRuleSetResponseTypeDef = TypedDict(
    "_ClientDescribeActiveReceiptRuleSetResponseTypeDef",
    {
        "Metadata": ClientDescribeActiveReceiptRuleSetResponseMetadataTypeDef,
        "Rules": List[ClientDescribeActiveReceiptRuleSetResponseRulesTypeDef],
    },
    total=False,
)


class ClientDescribeActiveReceiptRuleSetResponseTypeDef(
    _ClientDescribeActiveReceiptRuleSetResponseTypeDef
):
    """
    - *(dict) --*

      Represents the metadata and receipt rules for the receipt rule set that is currently active.
      - **Metadata** *(dict) --*

        The metadata for the currently active receipt rule set. The metadata consists of the rule
        set name and a timestamp of when the rule set was created.
        - **Name** *(string) --*

          The name of the receipt rule set. The name must:
          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
          dashes (-).
          * Start and end with a letter or number.
          * Contain less than 64 characters.
    """


_ClientDescribeConfigurationSetResponseConfigurationSetTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseConfigurationSetTypeDef", {"Name": str}, total=False
)


class ClientDescribeConfigurationSetResponseConfigurationSetTypeDef(
    _ClientDescribeConfigurationSetResponseConfigurationSetTypeDef
):
    """
    - **ConfigurationSet** *(dict) --*

      The configuration set object associated with the specified configuration set.
      - **Name** *(string) --*

        The name of the configuration set. The name must meet the following requirements:
        * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
        * Contain 64 characters or fewer.
    """


_ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef",
    {"TlsPolicy": Literal["Require", "Optional"]},
    total=False,
)


class ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef(
    _ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef
):
    pass


_ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["messageTag", "emailHeader", "linkTag"],
        "DefaultDimensionValue": str,
    },
    total=False,
)


class ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef(
    _ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef
):
    pass


_ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef(
    _ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef
):
    pass


_ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    {"IAMRoleARN": str, "DeliveryStreamARN": str},
    total=False,
)


class ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef(
    _ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef
):
    pass


_ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef",
    {"TopicARN": str},
    total=False,
)


class ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef(
    _ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef
):
    pass


_ClientDescribeConfigurationSetResponseEventDestinationsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseEventDestinationsTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "send",
                "reject",
                "bounce",
                "complaint",
                "delivery",
                "open",
                "click",
                "renderingFailure",
            ]
        ],
        "KinesisFirehoseDestination": ClientDescribeConfigurationSetResponseEventDestinationsKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientDescribeConfigurationSetResponseEventDestinationsCloudWatchDestinationTypeDef,
        "SNSDestination": ClientDescribeConfigurationSetResponseEventDestinationsSNSDestinationTypeDef,
    },
    total=False,
)


class ClientDescribeConfigurationSetResponseEventDestinationsTypeDef(
    _ClientDescribeConfigurationSetResponseEventDestinationsTypeDef
):
    pass


_ClientDescribeConfigurationSetResponseReputationOptionsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseReputationOptionsTypeDef",
    {"SendingEnabled": bool, "ReputationMetricsEnabled": bool, "LastFreshStart": datetime},
    total=False,
)


class ClientDescribeConfigurationSetResponseReputationOptionsTypeDef(
    _ClientDescribeConfigurationSetResponseReputationOptionsTypeDef
):
    pass


_ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)


class ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef(
    _ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef
):
    pass


_ClientDescribeConfigurationSetResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationSetResponseTypeDef",
    {
        "ConfigurationSet": ClientDescribeConfigurationSetResponseConfigurationSetTypeDef,
        "EventDestinations": List[ClientDescribeConfigurationSetResponseEventDestinationsTypeDef],
        "TrackingOptions": ClientDescribeConfigurationSetResponseTrackingOptionsTypeDef,
        "DeliveryOptions": ClientDescribeConfigurationSetResponseDeliveryOptionsTypeDef,
        "ReputationOptions": ClientDescribeConfigurationSetResponseReputationOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeConfigurationSetResponseTypeDef(_ClientDescribeConfigurationSetResponseTypeDef):
    """
    - *(dict) --*

      Represents the details of a configuration set. Configuration sets enable you to publish email
      sending events. For information about using configuration sets, see the `Amazon SES Developer
      Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__
      .
      - **ConfigurationSet** *(dict) --*

        The configuration set object associated with the specified configuration set.
        - **Name** *(string) --*

          The name of the configuration set. The name must meet the following requirements:
          * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
          * Contain 64 characters or fewer.
    """


_ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef
):
    pass


_ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef",
    {"TopicArn": str, "SmtpReplyCode": str, "StatusCode": str, "Message": str, "Sender": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef
):
    pass


_ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef
):
    pass


_ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef
):
    pass


_ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": Literal["UTF-8", "Base64"]},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef
):
    pass


_ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef
):
    pass


_ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef
):
    pass


_ClientDescribeReceiptRuleResponseRuleActionsTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleActionsTypeDef",
    {
        "S3Action": ClientDescribeReceiptRuleResponseRuleActionsS3ActionTypeDef,
        "BounceAction": ClientDescribeReceiptRuleResponseRuleActionsBounceActionTypeDef,
        "WorkmailAction": ClientDescribeReceiptRuleResponseRuleActionsWorkmailActionTypeDef,
        "LambdaAction": ClientDescribeReceiptRuleResponseRuleActionsLambdaActionTypeDef,
        "StopAction": ClientDescribeReceiptRuleResponseRuleActionsStopActionTypeDef,
        "AddHeaderAction": ClientDescribeReceiptRuleResponseRuleActionsAddHeaderActionTypeDef,
        "SNSAction": ClientDescribeReceiptRuleResponseRuleActionsSNSActionTypeDef,
    },
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleActionsTypeDef(
    _ClientDescribeReceiptRuleResponseRuleActionsTypeDef
):
    pass


_ClientDescribeReceiptRuleResponseRuleTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseRuleTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List[ClientDescribeReceiptRuleResponseRuleActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientDescribeReceiptRuleResponseRuleTypeDef(_ClientDescribeReceiptRuleResponseRuleTypeDef):
    """
    - **Rule** *(dict) --*

      A data structure that contains the specified receipt rule's name, actions, recipients,
      domains, enabled status, scan status, and Transport Layer Security (TLS) policy.
      - **Name** *(string) --*

        The name of the receipt rule. The name must:
        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).
        * Start and end with a letter or number.
        * Contain less than 64 characters.
    """


_ClientDescribeReceiptRuleResponseTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleResponseTypeDef",
    {"Rule": ClientDescribeReceiptRuleResponseRuleTypeDef},
    total=False,
)


class ClientDescribeReceiptRuleResponseTypeDef(_ClientDescribeReceiptRuleResponseTypeDef):
    """
    - *(dict) --*

      Represents the details of a receipt rule.
      - **Rule** *(dict) --*

        A data structure that contains the specified receipt rule's name, actions, recipients,
        domains, enabled status, scan status, and Transport Layer Security (TLS) policy.
        - **Name** *(string) --*

          The name of the receipt rule. The name must:
          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
          dashes (-).
          * Start and end with a letter or number.
          * Contain less than 64 characters.
    """


_ClientDescribeReceiptRuleSetResponseMetadataTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseMetadataTypeDef(
    _ClientDescribeReceiptRuleSetResponseMetadataTypeDef
):
    """
    - **Metadata** *(dict) --*

      The metadata for the receipt rule set, which consists of the rule set name and the timestamp
      of when the rule set was created.
      - **Name** *(string) --*

        The name of the receipt rule set. The name must:
        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).
        * Start and end with a letter or number.
        * Contain less than 64 characters.
    """


_ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef
):
    pass


_ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef",
    {"TopicArn": str, "SmtpReplyCode": str, "StatusCode": str, "Message": str, "Sender": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef
):
    pass


_ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef
):
    pass


_ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef
):
    pass


_ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": Literal["UTF-8", "Base64"]},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef
):
    pass


_ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef
):
    pass


_ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef
):
    pass


_ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef",
    {
        "S3Action": ClientDescribeReceiptRuleSetResponseRulesActionsS3ActionTypeDef,
        "BounceAction": ClientDescribeReceiptRuleSetResponseRulesActionsBounceActionTypeDef,
        "WorkmailAction": ClientDescribeReceiptRuleSetResponseRulesActionsWorkmailActionTypeDef,
        "LambdaAction": ClientDescribeReceiptRuleSetResponseRulesActionsLambdaActionTypeDef,
        "StopAction": ClientDescribeReceiptRuleSetResponseRulesActionsStopActionTypeDef,
        "AddHeaderAction": ClientDescribeReceiptRuleSetResponseRulesActionsAddHeaderActionTypeDef,
        "SNSAction": ClientDescribeReceiptRuleSetResponseRulesActionsSNSActionTypeDef,
    },
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef
):
    pass


_ClientDescribeReceiptRuleSetResponseRulesTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseRulesTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List[ClientDescribeReceiptRuleSetResponseRulesActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientDescribeReceiptRuleSetResponseRulesTypeDef(
    _ClientDescribeReceiptRuleSetResponseRulesTypeDef
):
    pass


_ClientDescribeReceiptRuleSetResponseTypeDef = TypedDict(
    "_ClientDescribeReceiptRuleSetResponseTypeDef",
    {
        "Metadata": ClientDescribeReceiptRuleSetResponseMetadataTypeDef,
        "Rules": List[ClientDescribeReceiptRuleSetResponseRulesTypeDef],
    },
    total=False,
)


class ClientDescribeReceiptRuleSetResponseTypeDef(_ClientDescribeReceiptRuleSetResponseTypeDef):
    """
    - *(dict) --*

      Represents the details of the specified receipt rule set.
      - **Metadata** *(dict) --*

        The metadata for the receipt rule set, which consists of the rule set name and the timestamp
        of when the rule set was created.
        - **Name** *(string) --*

          The name of the receipt rule set. The name must:
          * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
          dashes (-).
          * Start and end with a letter or number.
          * Contain less than 64 characters.
    """


_ClientGetAccountSendingEnabledResponseTypeDef = TypedDict(
    "_ClientGetAccountSendingEnabledResponseTypeDef", {"Enabled": bool}, total=False
)


class ClientGetAccountSendingEnabledResponseTypeDef(_ClientGetAccountSendingEnabledResponseTypeDef):
    """
    - *(dict) --*

      Represents a request to return the email sending status for your Amazon SES account in the
      current AWS Region.
      - **Enabled** *(boolean) --*

        Describes whether email sending is enabled or disabled for your Amazon SES account in the
        current AWS Region.
    """


_ClientGetCustomVerificationEmailTemplateResponseTypeDef = TypedDict(
    "_ClientGetCustomVerificationEmailTemplateResponseTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)


class ClientGetCustomVerificationEmailTemplateResponseTypeDef(
    _ClientGetCustomVerificationEmailTemplateResponseTypeDef
):
    """
    - *(dict) --*

      The content of the custom verification email template.
      - **TemplateName** *(string) --*

        The name of the custom verification email template.
    """


_ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef = TypedDict(
    "_ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef",
    {
        "DkimEnabled": bool,
        "DkimVerificationStatus": Literal[
            "Pending", "Success", "Failed", "TemporaryFailure", "NotStarted"
        ],
        "DkimTokens": List[str],
    },
    total=False,
)


class ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef(
    _ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef
):
    pass


_ClientGetIdentityDkimAttributesResponseTypeDef = TypedDict(
    "_ClientGetIdentityDkimAttributesResponseTypeDef",
    {"DkimAttributes": Dict[str, ClientGetIdentityDkimAttributesResponseDkimAttributesTypeDef]},
    total=False,
)


class ClientGetIdentityDkimAttributesResponseTypeDef(
    _ClientGetIdentityDkimAttributesResponseTypeDef
):
    """
    - *(dict) --*

      Represents the status of Amazon SES Easy DKIM signing for an identity. For domain identities,
      this response also contains the DKIM tokens that are required for Easy DKIM signing, and
      whether Amazon SES successfully verified that these tokens were published.
      - **DkimAttributes** *(dict) --*

        The DKIM attributes for an email address or a domain.
        - *(string) --*

          - *(dict) --*

            Represents the DKIM attributes of a verified email address or a domain.
            - **DkimEnabled** *(boolean) --*

              Is true if DKIM signing is enabled for email sent from the identity. It's false
              otherwise. The default value is true.
    """


_ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef = TypedDict(
    "_ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": Literal["Pending", "Success", "Failed", "TemporaryFailure"],
        "BehaviorOnMXFailure": Literal["UseDefaultValue", "RejectMessage"],
    },
    total=False,
)


class ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef(
    _ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef
):
    pass


_ClientGetIdentityMailFromDomainAttributesResponseTypeDef = TypedDict(
    "_ClientGetIdentityMailFromDomainAttributesResponseTypeDef",
    {
        "MailFromDomainAttributes": Dict[
            str, ClientGetIdentityMailFromDomainAttributesResponseMailFromDomainAttributesTypeDef
        ]
    },
    total=False,
)


class ClientGetIdentityMailFromDomainAttributesResponseTypeDef(
    _ClientGetIdentityMailFromDomainAttributesResponseTypeDef
):
    """
    - *(dict) --*

      Represents the custom MAIL FROM attributes for a list of identities.
      - **MailFromDomainAttributes** *(dict) --*

        A map of identities to custom MAIL FROM attributes.
        - *(string) --*

          - *(dict) --*

            Represents the custom MAIL FROM domain attributes of a verified identity (email address
            or domain).
            - **MailFromDomain** *(string) --*

              The custom MAIL FROM domain that the identity is configured to use.
    """


_ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef = TypedDict(
    "_ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef",
    {
        "BounceTopic": str,
        "ComplaintTopic": str,
        "DeliveryTopic": str,
        "ForwardingEnabled": bool,
        "HeadersInBounceNotificationsEnabled": bool,
        "HeadersInComplaintNotificationsEnabled": bool,
        "HeadersInDeliveryNotificationsEnabled": bool,
    },
    total=False,
)


class ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef(
    _ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef
):
    pass


_ClientGetIdentityNotificationAttributesResponseTypeDef = TypedDict(
    "_ClientGetIdentityNotificationAttributesResponseTypeDef",
    {
        "NotificationAttributes": Dict[
            str, ClientGetIdentityNotificationAttributesResponseNotificationAttributesTypeDef
        ]
    },
    total=False,
)


class ClientGetIdentityNotificationAttributesResponseTypeDef(
    _ClientGetIdentityNotificationAttributesResponseTypeDef
):
    """
    - *(dict) --*

      Represents the notification attributes for a list of identities.
      - **NotificationAttributes** *(dict) --*

        A map of Identity to IdentityNotificationAttributes.
        - *(string) --*

          - *(dict) --*

            Represents the notification attributes of an identity, including whether an identity has
            Amazon Simple Notification Service (Amazon SNS) topics set for bounce, complaint, and/or
            delivery notifications, and whether feedback forwarding is enabled for bounce and
            complaint notifications.
            - **BounceTopic** *(string) --*

              The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish
              bounce notifications.
    """


_ClientGetIdentityPoliciesResponseTypeDef = TypedDict(
    "_ClientGetIdentityPoliciesResponseTypeDef", {"Policies": Dict[str, str]}, total=False
)


class ClientGetIdentityPoliciesResponseTypeDef(_ClientGetIdentityPoliciesResponseTypeDef):
    """
    - *(dict) --*

      Represents the requested sending authorization policies.
      - **Policies** *(dict) --*

        A map of policy names to policies.
        - *(string) --*

          - *(string) --*
    """


_ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef = TypedDict(
    "_ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef",
    {
        "VerificationStatus": Literal[
            "Pending", "Success", "Failed", "TemporaryFailure", "NotStarted"
        ],
        "VerificationToken": str,
    },
    total=False,
)


class ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef(
    _ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef
):
    pass


_ClientGetIdentityVerificationAttributesResponseTypeDef = TypedDict(
    "_ClientGetIdentityVerificationAttributesResponseTypeDef",
    {
        "VerificationAttributes": Dict[
            str, ClientGetIdentityVerificationAttributesResponseVerificationAttributesTypeDef
        ]
    },
    total=False,
)


class ClientGetIdentityVerificationAttributesResponseTypeDef(
    _ClientGetIdentityVerificationAttributesResponseTypeDef
):
    """
    - *(dict) --*

      The Amazon SES verification status of a list of identities. For domain identities, this
      response also contains the verification token.
      - **VerificationAttributes** *(dict) --*

        A map of Identities to IdentityVerificationAttributes objects.
        - *(string) --*

          - *(dict) --*

            Represents the verification attributes of a single identity.
            - **VerificationStatus** *(string) --*

              The verification status of the identity: "Pending", "Success", "Failed", or
              "TemporaryFailure".
    """


_ClientGetSendQuotaResponseTypeDef = TypedDict(
    "_ClientGetSendQuotaResponseTypeDef",
    {"Max24HourSend": float, "MaxSendRate": float, "SentLast24Hours": float},
    total=False,
)


class ClientGetSendQuotaResponseTypeDef(_ClientGetSendQuotaResponseTypeDef):
    """
    - *(dict) --*

      Represents your Amazon SES daily sending quota, maximum send rate, and the number of emails
      you have sent in the last 24 hours.
      - **Max24HourSend** *(float) --*

        The maximum number of emails the user is allowed to send in a 24-hour interval. A value of
        -1 signifies an unlimited quota.
    """


_ClientGetSendStatisticsResponseSendDataPointsTypeDef = TypedDict(
    "_ClientGetSendStatisticsResponseSendDataPointsTypeDef",
    {
        "Timestamp": datetime,
        "DeliveryAttempts": int,
        "Bounces": int,
        "Complaints": int,
        "Rejects": int,
    },
    total=False,
)


class ClientGetSendStatisticsResponseSendDataPointsTypeDef(
    _ClientGetSendStatisticsResponseSendDataPointsTypeDef
):
    """
    - *(dict) --*

      Represents sending statistics data. Each ``SendDataPoint`` contains statistics for a 15-minute
      period of sending activity.
      - **Timestamp** *(datetime) --*

        Time of the data point.
    """


_ClientGetSendStatisticsResponseTypeDef = TypedDict(
    "_ClientGetSendStatisticsResponseTypeDef",
    {"SendDataPoints": List[ClientGetSendStatisticsResponseSendDataPointsTypeDef]},
    total=False,
)


class ClientGetSendStatisticsResponseTypeDef(_ClientGetSendStatisticsResponseTypeDef):
    """
    - *(dict) --*

      Represents a list of data points. This list contains aggregated data from the previous two
      weeks of your sending activity with Amazon SES.
      - **SendDataPoints** *(list) --*

        A list of data points, each of which represents 15 minutes of activity.
        - *(dict) --*

          Represents sending statistics data. Each ``SendDataPoint`` contains statistics for a
          15-minute period of sending activity.
          - **Timestamp** *(datetime) --*

            Time of the data point.
    """


_ClientGetTemplateResponseTemplateTypeDef = TypedDict(
    "_ClientGetTemplateResponseTemplateTypeDef",
    {"TemplateName": str, "SubjectPart": str, "TextPart": str, "HtmlPart": str},
    total=False,
)


class ClientGetTemplateResponseTemplateTypeDef(_ClientGetTemplateResponseTemplateTypeDef):
    """
    - **Template** *(dict) --*

      The content of the email, composed of a subject line, an HTML part, and a text-only part.
      - **TemplateName** *(string) --*

        The name of the template. You will refer to this name when you send email using the
        ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.
    """


_ClientGetTemplateResponseTypeDef = TypedDict(
    "_ClientGetTemplateResponseTypeDef",
    {"Template": ClientGetTemplateResponseTemplateTypeDef},
    total=False,
)


class ClientGetTemplateResponseTypeDef(_ClientGetTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **Template** *(dict) --*

        The content of the email, composed of a subject line, an HTML part, and a text-only part.
        - **TemplateName** *(string) --*

          The name of the template. You will refer to this name when you send email using the
          ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.
    """


_ClientListConfigurationSetsResponseConfigurationSetsTypeDef = TypedDict(
    "_ClientListConfigurationSetsResponseConfigurationSetsTypeDef", {"Name": str}, total=False
)


class ClientListConfigurationSetsResponseConfigurationSetsTypeDef(
    _ClientListConfigurationSetsResponseConfigurationSetsTypeDef
):
    """
    - *(dict) --*

      The name of the configuration set.
      Configuration sets let you create groups of rules that you can apply to the emails you send
      using Amazon SES. For more information about using configuration sets, see `Using Amazon SES
      Configuration Sets
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html>`__ in
      the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/>`__ .
      - **Name** *(string) --*

        The name of the configuration set. The name must meet the following requirements:
        * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
        * Contain 64 characters or fewer.
    """


_ClientListConfigurationSetsResponseTypeDef = TypedDict(
    "_ClientListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List[ClientListConfigurationSetsResponseConfigurationSetsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListConfigurationSetsResponseTypeDef(_ClientListConfigurationSetsResponseTypeDef):
    """
    - *(dict) --*

      A list of configuration sets associated with your AWS account. Configuration sets enable you
      to publish email sending events. For information about using configuration sets, see the
      `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .
      - **ConfigurationSets** *(list) --*

        A list of configuration sets.
        - *(dict) --*

          The name of the configuration set.
          Configuration sets let you create groups of rules that you can apply to the emails you
          send using Amazon SES. For more information about using configuration sets, see `Using
          Amazon SES Configuration Sets
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html>`__
          in the `Amazon SES Developer Guide
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/>`__ .
          - **Name** *(string) --*

            The name of the configuration set. The name must meet the following requirements:
            * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            * Contain 64 characters or fewer.
    """


_ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef = TypedDict(
    "_ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)


class ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef(
    _ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef
):
    """
    - *(dict) --*

      Contains information about a custom verification email template.
      - **TemplateName** *(string) --*

        The name of the custom verification email template.
    """


_ClientListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "_ClientListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List[
            ClientListCustomVerificationEmailTemplatesResponseCustomVerificationEmailTemplatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListCustomVerificationEmailTemplatesResponseTypeDef(
    _ClientListCustomVerificationEmailTemplatesResponseTypeDef
):
    """
    - *(dict) --*

      A paginated list of custom verification email templates.
      - **CustomVerificationEmailTemplates** *(list) --*

        A list of the custom verification email templates that exist in your account.
        - *(dict) --*

          Contains information about a custom verification email template.
          - **TemplateName** *(string) --*

            The name of the custom verification email template.
    """


_ClientListIdentitiesResponseTypeDef = TypedDict(
    "_ClientListIdentitiesResponseTypeDef", {"Identities": List[str], "NextToken": str}, total=False
)


class ClientListIdentitiesResponseTypeDef(_ClientListIdentitiesResponseTypeDef):
    """
    - *(dict) --*

      A list of all identities that you have attempted to verify under your AWS account, regardless
      of verification status.
      - **Identities** *(list) --*

        A list of identities.
        - *(string) --*
    """


_ClientListIdentityPoliciesResponseTypeDef = TypedDict(
    "_ClientListIdentityPoliciesResponseTypeDef", {"PolicyNames": List[str]}, total=False
)


class ClientListIdentityPoliciesResponseTypeDef(_ClientListIdentityPoliciesResponseTypeDef):
    """
    - *(dict) --*

      A list of names of sending authorization policies that apply to an identity.
      - **PolicyNames** *(list) --*

        A list of names of policies that apply to the specified identity.
        - *(string) --*
    """


_ClientListReceiptFiltersResponseFiltersIpFilterTypeDef = TypedDict(
    "_ClientListReceiptFiltersResponseFiltersIpFilterTypeDef",
    {"Policy": Literal["Block", "Allow"], "Cidr": str},
    total=False,
)


class ClientListReceiptFiltersResponseFiltersIpFilterTypeDef(
    _ClientListReceiptFiltersResponseFiltersIpFilterTypeDef
):
    pass


_ClientListReceiptFiltersResponseFiltersTypeDef = TypedDict(
    "_ClientListReceiptFiltersResponseFiltersTypeDef",
    {"Name": str, "IpFilter": ClientListReceiptFiltersResponseFiltersIpFilterTypeDef},
    total=False,
)


class ClientListReceiptFiltersResponseFiltersTypeDef(
    _ClientListReceiptFiltersResponseFiltersTypeDef
):
    """
    - *(dict) --*

      A receipt IP address filter enables you to specify whether to accept or reject mail
      originating from an IP address or range of IP addresses.
      For information about setting up IP address filters, see the `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-ip-filters.html>`__ .
      - **Name** *(string) --*

        The name of the IP address filter. The name must:
        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).
        * Start and end with a letter or number.
        * Contain less than 64 characters.
    """


_ClientListReceiptFiltersResponseTypeDef = TypedDict(
    "_ClientListReceiptFiltersResponseTypeDef",
    {"Filters": List[ClientListReceiptFiltersResponseFiltersTypeDef]},
    total=False,
)


class ClientListReceiptFiltersResponseTypeDef(_ClientListReceiptFiltersResponseTypeDef):
    """
    - *(dict) --*

      A list of IP address filters that exist under your AWS account.
      - **Filters** *(list) --*

        A list of IP address filter data structures, which each consist of a name, an IP address
        range, and whether to allow or block mail from it.
        - *(dict) --*

          A receipt IP address filter enables you to specify whether to accept or reject mail
          originating from an IP address or range of IP addresses.
          For information about setting up IP address filters, see the `Amazon SES Developer Guide
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-ip-filters.html>`__
          .
          - **Name** *(string) --*

            The name of the IP address filter. The name must:
            * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
            or dashes (-).
            * Start and end with a letter or number.
            * Contain less than 64 characters.
    """


_ClientListReceiptRuleSetsResponseRuleSetsTypeDef = TypedDict(
    "_ClientListReceiptRuleSetsResponseRuleSetsTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ClientListReceiptRuleSetsResponseRuleSetsTypeDef(
    _ClientListReceiptRuleSetsResponseRuleSetsTypeDef
):
    """
    - *(dict) --*

      Information about a receipt rule set.
      A receipt rule set is a collection of rules that specify what Amazon SES should do with mail
      it receives on behalf of your account's verified domains.
      For information about setting up receipt rule sets, see the `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__
      .
      - **Name** *(string) --*

        The name of the receipt rule set. The name must:
        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).
        * Start and end with a letter or number.
        * Contain less than 64 characters.
    """


_ClientListReceiptRuleSetsResponseTypeDef = TypedDict(
    "_ClientListReceiptRuleSetsResponseTypeDef",
    {"RuleSets": List[ClientListReceiptRuleSetsResponseRuleSetsTypeDef], "NextToken": str},
    total=False,
)


class ClientListReceiptRuleSetsResponseTypeDef(_ClientListReceiptRuleSetsResponseTypeDef):
    """
    - *(dict) --*

      A list of receipt rule sets that exist under your AWS account.
      - **RuleSets** *(list) --*

        The metadata for the currently active receipt rule set. The metadata consists of the rule
        set name and the timestamp of when the rule set was created.
        - *(dict) --*

          Information about a receipt rule set.
          A receipt rule set is a collection of rules that specify what Amazon SES should do with
          mail it receives on behalf of your account's verified domains.
          For information about setting up receipt rule sets, see the `Amazon SES Developer Guide
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__
          .
          - **Name** *(string) --*

            The name of the receipt rule set. The name must:
            * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
            or dashes (-).
            * Start and end with a letter or number.
            * Contain less than 64 characters.
    """


_ClientListTemplatesResponseTemplatesMetadataTypeDef = TypedDict(
    "_ClientListTemplatesResponseTemplatesMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ClientListTemplatesResponseTemplatesMetadataTypeDef(
    _ClientListTemplatesResponseTemplatesMetadataTypeDef
):
    """
    - *(dict) --*

      Contains information about an email template.
      - **Name** *(string) --*

        The name of the template.
    """


_ClientListTemplatesResponseTypeDef = TypedDict(
    "_ClientListTemplatesResponseTypeDef",
    {
        "TemplatesMetadata": List[ClientListTemplatesResponseTemplatesMetadataTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTemplatesResponseTypeDef(_ClientListTemplatesResponseTypeDef):
    """
    - *(dict) --*

      - **TemplatesMetadata** *(list) --*

        An array the contains the name and creation time stamp for each template in your Amazon SES
        account.
        - *(dict) --*

          Contains information about an email template.
          - **Name** *(string) --*

            The name of the template.
    """


_ClientListVerifiedEmailAddressesResponseTypeDef = TypedDict(
    "_ClientListVerifiedEmailAddressesResponseTypeDef",
    {"VerifiedEmailAddresses": List[str]},
    total=False,
)


class ClientListVerifiedEmailAddressesResponseTypeDef(
    _ClientListVerifiedEmailAddressesResponseTypeDef
):
    """
    - *(dict) --*

      A list of email addresses that you have verified with Amazon SES under your AWS account.
      - **VerifiedEmailAddresses** *(list) --*

        A list of email addresses that have been verified.
        - *(string) --*
    """


_ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef = TypedDict(
    "_ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef",
    {"TlsPolicy": Literal["Require", "Optional"]},
    total=False,
)


class ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef(
    _ClientPutConfigurationSetDeliveryOptionsDeliveryOptionsTypeDef
):
    """
    Specifies whether messages that use the configuration set are required to use Transport Layer
    Security (TLS).
    - **TlsPolicy** *(string) --*

      Specifies whether messages that use the configuration set are required to use Transport Layer
      Security (TLS). If the value is ``Require`` , messages are only delivered if a TLS connection
      can be established. If the value is ``Optional`` , messages can be delivered in plain text if
      a TLS connection can't be established.
    """


_ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef = TypedDict(
    "_ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef(
    _ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef
):
    pass


_ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef = TypedDict(
    "_ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef",
    {
        "FinalRecipient": str,
        "Action": Literal["failed", "delayed", "delivered", "relayed", "expanded"],
        "RemoteMta": str,
        "Status": str,
        "DiagnosticCode": str,
        "LastAttemptDate": datetime,
        "ExtensionFields": List[
            ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsExtensionFieldsTypeDef
        ],
    },
    total=False,
)


class ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef(
    _ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef
):
    pass


_RequiredClientSendBounceBouncedRecipientInfoListTypeDef = TypedDict(
    "_RequiredClientSendBounceBouncedRecipientInfoListTypeDef", {"Recipient": str}
)
_OptionalClientSendBounceBouncedRecipientInfoListTypeDef = TypedDict(
    "_OptionalClientSendBounceBouncedRecipientInfoListTypeDef",
    {
        "RecipientArn": str,
        "BounceType": Literal[
            "DoesNotExist",
            "MessageTooLarge",
            "ExceededQuota",
            "ContentRejected",
            "Undefined",
            "TemporaryFailure",
        ],
        "RecipientDsnFields": ClientSendBounceBouncedRecipientInfoListRecipientDsnFieldsTypeDef,
    },
    total=False,
)


class ClientSendBounceBouncedRecipientInfoListTypeDef(
    _RequiredClientSendBounceBouncedRecipientInfoListTypeDef,
    _OptionalClientSendBounceBouncedRecipientInfoListTypeDef,
):
    """
    - *(dict) --*

      Recipient-related information to include in the Delivery Status Notification (DSN) when an
      email that Amazon SES receives on your behalf bounces.
      For information about receiving email through Amazon SES, see the `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .
      - **Recipient** *(string) --***[REQUIRED]**

        The email address of the recipient of the bounced email.
    """


_ClientSendBounceMessageDsnExtensionFieldsTypeDef = TypedDict(
    "_ClientSendBounceMessageDsnExtensionFieldsTypeDef", {"Name": str, "Value": str}, total=False
)


class ClientSendBounceMessageDsnExtensionFieldsTypeDef(
    _ClientSendBounceMessageDsnExtensionFieldsTypeDef
):
    pass


_RequiredClientSendBounceMessageDsnTypeDef = TypedDict(
    "_RequiredClientSendBounceMessageDsnTypeDef", {"ReportingMta": str}
)
_OptionalClientSendBounceMessageDsnTypeDef = TypedDict(
    "_OptionalClientSendBounceMessageDsnTypeDef",
    {
        "ArrivalDate": datetime,
        "ExtensionFields": List[ClientSendBounceMessageDsnExtensionFieldsTypeDef],
    },
    total=False,
)


class ClientSendBounceMessageDsnTypeDef(
    _RequiredClientSendBounceMessageDsnTypeDef, _OptionalClientSendBounceMessageDsnTypeDef
):
    """
    Message-related DSN fields. If not specified, Amazon SES will choose the values.
    - **ReportingMta** *(string) --***[REQUIRED]**

      The reporting MTA that attempted to deliver the message, formatted as specified in `RFC 3464
      <https://tools.ietf.org/html/rfc3464>`__ (``mta-name-type; mta-name`` ). The default value is
      ``dns; inbound-smtp.[region].amazonaws.com`` .
    """


_ClientSendBounceResponseTypeDef = TypedDict(
    "_ClientSendBounceResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendBounceResponseTypeDef(_ClientSendBounceResponseTypeDef):
    """
    - *(dict) --*

      Represents a unique message ID.
      - **MessageId** *(string) --*

        The message ID of the bounce message.
    """


_RequiredClientSendBulkTemplatedEmailDefaultTagsTypeDef = TypedDict(
    "_RequiredClientSendBulkTemplatedEmailDefaultTagsTypeDef", {"Name": str}
)
_OptionalClientSendBulkTemplatedEmailDefaultTagsTypeDef = TypedDict(
    "_OptionalClientSendBulkTemplatedEmailDefaultTagsTypeDef", {"Value": str}, total=False
)


class ClientSendBulkTemplatedEmailDefaultTagsTypeDef(
    _RequiredClientSendBulkTemplatedEmailDefaultTagsTypeDef,
    _OptionalClientSendBulkTemplatedEmailDefaultTagsTypeDef,
):
    """
    - *(dict) --*

      Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail``
      to apply to an email.
      Message tags, which you use with configuration sets, enable you to publish email sending
      events. For information about using configuration sets, see the `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .
      - **Name** *(string) --***[REQUIRED]**

        The name of the tag. The name must:
        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).
        * Contain less than 256 characters.
    """


_ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef = TypedDict(
    "_ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)


class ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef(
    _ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef
):
    """
    - **Destination** *(dict) --***[REQUIRED]**

      Represents the destination of the message, consisting of To:, CC:, and BCC: fields.
      .. note::

        Amazon SES does not support the SMTPUTF8 extension, as described in `RFC6531
        <https://tools.ietf.org/html/rfc6531>`__ . For this reason, the *local part* of a
        destination email address (the part of the email address that precedes the @ sign) may only
        contain `7-bit ASCII characters <https://en.wikipedia.org/wiki/Email_address#Local-part>`__
        . If the *domain part* of an address (the part after the @ sign) contains non-ASCII
        characters, they must be encoded using Punycode, as described in `RFC3492
        <https://tools.ietf.org/html/rfc3492.html>`__ .
    """


_ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef = TypedDict(
    "_ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef",
    {"Name": str, "Value": str},
    total=False,
)


class ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef(
    _ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef
):
    pass


_RequiredClientSendBulkTemplatedEmailDestinationsTypeDef = TypedDict(
    "_RequiredClientSendBulkTemplatedEmailDestinationsTypeDef",
    {"Destination": ClientSendBulkTemplatedEmailDestinationsDestinationTypeDef},
)
_OptionalClientSendBulkTemplatedEmailDestinationsTypeDef = TypedDict(
    "_OptionalClientSendBulkTemplatedEmailDestinationsTypeDef",
    {
        "ReplacementTags": List[ClientSendBulkTemplatedEmailDestinationsReplacementTagsTypeDef],
        "ReplacementTemplateData": str,
    },
    total=False,
)


class ClientSendBulkTemplatedEmailDestinationsTypeDef(
    _RequiredClientSendBulkTemplatedEmailDestinationsTypeDef,
    _OptionalClientSendBulkTemplatedEmailDestinationsTypeDef,
):
    """
    - *(dict) --*

      An array that contains one or more Destinations, as well as the tags and replacement data
      associated with each of those Destinations.
      - **Destination** *(dict) --***[REQUIRED]**

        Represents the destination of the message, consisting of To:, CC:, and BCC: fields.
        .. note::

          Amazon SES does not support the SMTPUTF8 extension, as described in `RFC6531
          <https://tools.ietf.org/html/rfc6531>`__ . For this reason, the *local part* of a
          destination email address (the part of the email address that precedes the @ sign) may
          only contain `7-bit ASCII characters
          <https://en.wikipedia.org/wiki/Email_address#Local-part>`__ . If the *domain part* of an
          address (the part after the @ sign) contains non-ASCII characters, they must be encoded
          using Punycode, as described in `RFC3492 <https://tools.ietf.org/html/rfc3492.html>`__ .
    """


_ClientSendBulkTemplatedEmailResponseStatusTypeDef = TypedDict(
    "_ClientSendBulkTemplatedEmailResponseStatusTypeDef",
    {
        "Status": Literal[
            "Success",
            "MessageRejected",
            "MailFromDomainNotVerified",
            "ConfigurationSetDoesNotExist",
            "TemplateDoesNotExist",
            "AccountSuspended",
            "AccountThrottled",
            "AccountDailyQuotaExceeded",
            "InvalidSendingPoolName",
            "AccountSendingPaused",
            "ConfigurationSetSendingPaused",
            "InvalidParameterValue",
            "TransientFailure",
            "Failed",
        ],
        "Error": str,
        "MessageId": str,
    },
    total=False,
)


class ClientSendBulkTemplatedEmailResponseStatusTypeDef(
    _ClientSendBulkTemplatedEmailResponseStatusTypeDef
):
    """
    - *(dict) --*

      An object that contains the response from the ``SendBulkTemplatedEmail`` operation.
      - **Status** *(string) --*

        The status of a message sent using the ``SendBulkTemplatedEmail`` operation.
        Possible values for this parameter include:
        * ``Success`` : Amazon SES accepted the message, and will attempt to deliver it to the
        recipients.
        * ``MessageRejected`` : The message was rejected because it contained a virus.
        * ``MailFromDomainNotVerified`` : The sender's email address or domain was not verified.
        * ``ConfigurationSetDoesNotExist`` : The configuration set you specified does not exist.
        * ``TemplateDoesNotExist`` : The template you specified does not exist.
        * ``AccountSuspended`` : Your account has been shut down because of issues related to your
        email sending practices.
        * ``AccountThrottled`` : The number of emails you can send has been reduced because your
        account has exceeded its allocated sending limit.
        * ``AccountDailyQuotaExceeded`` : You have reached or exceeded the maximum number of emails
        you can send from your account in a 24-hour period.
        * ``InvalidSendingPoolName`` : The configuration set you specified refers to an IP pool that
        does not exist.
        * ``AccountSendingPaused`` : Email sending for the Amazon SES account was disabled using the
        UpdateAccountSendingEnabled operation.
        * ``ConfigurationSetSendingPaused`` : Email sending for this configuration set was disabled
        using the  UpdateConfigurationSetSendingEnabled operation.
        * ``InvalidParameterValue`` : One or more of the parameters you specified when calling this
        operation was invalid. See the error message for additional information.
        * ``TransientFailure`` : Amazon SES was unable to process your request because of a
        temporary issue.
        * ``Failed`` : Amazon SES was unable to process your request. See the error message for
        additional information.
    """


_ClientSendBulkTemplatedEmailResponseTypeDef = TypedDict(
    "_ClientSendBulkTemplatedEmailResponseTypeDef",
    {"Status": List[ClientSendBulkTemplatedEmailResponseStatusTypeDef]},
    total=False,
)


class ClientSendBulkTemplatedEmailResponseTypeDef(_ClientSendBulkTemplatedEmailResponseTypeDef):
    """
    - *(dict) --*

      - **Status** *(list) --*

        The unique message identifier returned from the ``SendBulkTemplatedEmail`` action.
        - *(dict) --*

          An object that contains the response from the ``SendBulkTemplatedEmail`` operation.
          - **Status** *(string) --*

            The status of a message sent using the ``SendBulkTemplatedEmail`` operation.
            Possible values for this parameter include:
            * ``Success`` : Amazon SES accepted the message, and will attempt to deliver it to the
            recipients.
            * ``MessageRejected`` : The message was rejected because it contained a virus.
            * ``MailFromDomainNotVerified`` : The sender's email address or domain was not verified.
            * ``ConfigurationSetDoesNotExist`` : The configuration set you specified does not exist.
            * ``TemplateDoesNotExist`` : The template you specified does not exist.
            * ``AccountSuspended`` : Your account has been shut down because of issues related to
            your email sending practices.
            * ``AccountThrottled`` : The number of emails you can send has been reduced because your
            account has exceeded its allocated sending limit.
            * ``AccountDailyQuotaExceeded`` : You have reached or exceeded the maximum number of
            emails you can send from your account in a 24-hour period.
            * ``InvalidSendingPoolName`` : The configuration set you specified refers to an IP pool
            that does not exist.
            * ``AccountSendingPaused`` : Email sending for the Amazon SES account was disabled using
            the  UpdateAccountSendingEnabled operation.
            * ``ConfigurationSetSendingPaused`` : Email sending for this configuration set was
            disabled using the  UpdateConfigurationSetSendingEnabled operation.
            * ``InvalidParameterValue`` : One or more of the parameters you specified when calling
            this operation was invalid. See the error message for additional information.
            * ``TransientFailure`` : Amazon SES was unable to process your request because of a
            temporary issue.
            * ``Failed`` : Amazon SES was unable to process your request. See the error message for
            additional information.
    """


_ClientSendCustomVerificationEmailResponseTypeDef = TypedDict(
    "_ClientSendCustomVerificationEmailResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendCustomVerificationEmailResponseTypeDef(
    _ClientSendCustomVerificationEmailResponseTypeDef
):
    """
    - *(dict) --*

      The response received when attempting to send the custom verification email.
      - **MessageId** *(string) --*

        The unique message identifier returned from the ``SendCustomVerificationEmail`` operation.
    """


_ClientSendEmailDestinationTypeDef = TypedDict(
    "_ClientSendEmailDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)


class ClientSendEmailDestinationTypeDef(_ClientSendEmailDestinationTypeDef):
    """
    The destination for this email, composed of To:, CC:, and BCC: fields.
    - **ToAddresses** *(list) --*

      The recipients to place on the To: line of the message.
      - *(string) --*
    """


_ClientSendEmailMessageBodyHtmlTypeDef = TypedDict(
    "_ClientSendEmailMessageBodyHtmlTypeDef", {"Data": str, "Charset": str}, total=False
)


class ClientSendEmailMessageBodyHtmlTypeDef(_ClientSendEmailMessageBodyHtmlTypeDef):
    pass


_ClientSendEmailMessageBodyTextTypeDef = TypedDict(
    "_ClientSendEmailMessageBodyTextTypeDef", {"Data": str, "Charset": str}, total=False
)


class ClientSendEmailMessageBodyTextTypeDef(_ClientSendEmailMessageBodyTextTypeDef):
    pass


_ClientSendEmailMessageBodyTypeDef = TypedDict(
    "_ClientSendEmailMessageBodyTypeDef",
    {"Text": ClientSendEmailMessageBodyTextTypeDef, "Html": ClientSendEmailMessageBodyHtmlTypeDef},
    total=False,
)


class ClientSendEmailMessageBodyTypeDef(_ClientSendEmailMessageBodyTypeDef):
    pass


_RequiredClientSendEmailMessageSubjectTypeDef = TypedDict(
    "_RequiredClientSendEmailMessageSubjectTypeDef", {"Data": str}
)
_OptionalClientSendEmailMessageSubjectTypeDef = TypedDict(
    "_OptionalClientSendEmailMessageSubjectTypeDef", {"Charset": str}, total=False
)


class ClientSendEmailMessageSubjectTypeDef(
    _RequiredClientSendEmailMessageSubjectTypeDef, _OptionalClientSendEmailMessageSubjectTypeDef
):
    """
    - **Subject** *(dict) --***[REQUIRED]**

      The subject of the message: A short summary of the content, which will appear in the
      recipient's inbox.
      - **Data** *(string) --***[REQUIRED]**

        The textual data of the content.
    """


_RequiredClientSendEmailMessageTypeDef = TypedDict(
    "_RequiredClientSendEmailMessageTypeDef", {"Subject": ClientSendEmailMessageSubjectTypeDef}
)
_OptionalClientSendEmailMessageTypeDef = TypedDict(
    "_OptionalClientSendEmailMessageTypeDef",
    {"Body": ClientSendEmailMessageBodyTypeDef},
    total=False,
)


class ClientSendEmailMessageTypeDef(
    _RequiredClientSendEmailMessageTypeDef, _OptionalClientSendEmailMessageTypeDef
):
    """
    The message to be sent.
    - **Subject** *(dict) --***[REQUIRED]**

      The subject of the message: A short summary of the content, which will appear in the
      recipient's inbox.
      - **Data** *(string) --***[REQUIRED]**

        The textual data of the content.
    """


_ClientSendEmailResponseTypeDef = TypedDict(
    "_ClientSendEmailResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendEmailResponseTypeDef(_ClientSendEmailResponseTypeDef):
    """
    - *(dict) --*

      Represents a unique message ID.
      - **MessageId** *(string) --*

        The unique message identifier returned from the ``SendEmail`` action.
    """


_RequiredClientSendEmailTagsTypeDef = TypedDict(
    "_RequiredClientSendEmailTagsTypeDef", {"Name": str}
)
_OptionalClientSendEmailTagsTypeDef = TypedDict(
    "_OptionalClientSendEmailTagsTypeDef", {"Value": str}, total=False
)


class ClientSendEmailTagsTypeDef(
    _RequiredClientSendEmailTagsTypeDef, _OptionalClientSendEmailTagsTypeDef
):
    """
    - *(dict) --*

      Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail``
      to apply to an email.
      Message tags, which you use with configuration sets, enable you to publish email sending
      events. For information about using configuration sets, see the `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .
      - **Name** *(string) --***[REQUIRED]**

        The name of the tag. The name must:
        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).
        * Contain less than 256 characters.
    """


_ClientSendRawEmailRawMessageTypeDef = TypedDict(
    "_ClientSendRawEmailRawMessageTypeDef", {"Data": bytes}
)


class ClientSendRawEmailRawMessageTypeDef(_ClientSendRawEmailRawMessageTypeDef):
    """
    The raw email message itself. The message has to meet the following criteria:
    * The message has to contain a header and a body, separated by a blank line.
    * All of the required header fields must be present in the message.
    * Each part of a multipart MIME message must be formatted properly.
    * Attachments must be of a content type that Amazon SES supports. For a list on unsupported
    content types, see `Unsupported Attachment Types
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mime-types.html>`__ in the *Amazon SES
    Developer Guide* .
    * The entire message must be base64-encoded.
    * If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII
    character range, we highly recommend that you encode that content. For more information, see
    `Sending Raw Email
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html>`__ in the *Amazon
    SES Developer Guide* .
    * Per `RFC 5321 <https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6>`__ , the maximum length
    of each line of text, including the <CRLF>, must not exceed 1,000 characters.
    - **Data** *(bytes) --***[REQUIRED]**

      The raw data of the message. This data needs to base64-encoded if you are accessing Amazon SES
      directly through the HTTPS interface. If you are accessing Amazon SES using an AWS SDK, the
      SDK takes care of the base 64-encoding for you. In all cases, the client must ensure that the
      message format complies with Internet email standards regarding email header fields, MIME
      types, and MIME encoding.
      The To:, CC:, and BCC: headers in the raw message can contain a group list.
      If you are using ``SendRawEmail`` with sending authorization, you can include X-headers in the
      raw message to specify the "Source," "From," and "Return-Path" addresses. For more
      information, see the documentation for ``SendRawEmail`` .
      .. warning::

        Do not include these X-headers in the DKIM signature, because they are removed by Amazon SES
        before sending the email.
    """


_ClientSendRawEmailResponseTypeDef = TypedDict(
    "_ClientSendRawEmailResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendRawEmailResponseTypeDef(_ClientSendRawEmailResponseTypeDef):
    """
    - *(dict) --*

      Represents a unique message ID.
      - **MessageId** *(string) --*

        The unique message identifier returned from the ``SendRawEmail`` action.
    """


_RequiredClientSendRawEmailTagsTypeDef = TypedDict(
    "_RequiredClientSendRawEmailTagsTypeDef", {"Name": str}
)
_OptionalClientSendRawEmailTagsTypeDef = TypedDict(
    "_OptionalClientSendRawEmailTagsTypeDef", {"Value": str}, total=False
)


class ClientSendRawEmailTagsTypeDef(
    _RequiredClientSendRawEmailTagsTypeDef, _OptionalClientSendRawEmailTagsTypeDef
):
    """
    - *(dict) --*

      Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail``
      to apply to an email.
      Message tags, which you use with configuration sets, enable you to publish email sending
      events. For information about using configuration sets, see the `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .
      - **Name** *(string) --***[REQUIRED]**

        The name of the tag. The name must:
        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).
        * Contain less than 256 characters.
    """


_ClientSendTemplatedEmailDestinationTypeDef = TypedDict(
    "_ClientSendTemplatedEmailDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)


class ClientSendTemplatedEmailDestinationTypeDef(_ClientSendTemplatedEmailDestinationTypeDef):
    """
    The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include
    up to 50 recipients across these three fields.
    - **ToAddresses** *(list) --*

      The recipients to place on the To: line of the message.
      - *(string) --*
    """


_ClientSendTemplatedEmailResponseTypeDef = TypedDict(
    "_ClientSendTemplatedEmailResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendTemplatedEmailResponseTypeDef(_ClientSendTemplatedEmailResponseTypeDef):
    """
    - *(dict) --*

      - **MessageId** *(string) --*

        The unique message identifier returned from the ``SendTemplatedEmail`` action.
    """


_RequiredClientSendTemplatedEmailTagsTypeDef = TypedDict(
    "_RequiredClientSendTemplatedEmailTagsTypeDef", {"Name": str}
)
_OptionalClientSendTemplatedEmailTagsTypeDef = TypedDict(
    "_OptionalClientSendTemplatedEmailTagsTypeDef", {"Value": str}, total=False
)


class ClientSendTemplatedEmailTagsTypeDef(
    _RequiredClientSendTemplatedEmailTagsTypeDef, _OptionalClientSendTemplatedEmailTagsTypeDef
):
    """
    - *(dict) --*

      Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail``
      to apply to an email.
      Message tags, which you use with configuration sets, enable you to publish email sending
      events. For information about using configuration sets, see the `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .
      - **Name** *(string) --***[REQUIRED]**

        The name of the tag. The name must:
        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).
        * Contain less than 256 characters.
    """


_ClientTestRenderTemplateResponseTypeDef = TypedDict(
    "_ClientTestRenderTemplateResponseTypeDef", {"RenderedTemplate": str}, total=False
)


class ClientTestRenderTemplateResponseTypeDef(_ClientTestRenderTemplateResponseTypeDef):
    """
    - *(dict) --*

      - **RenderedTemplate** *(string) --*

        The complete MIME message rendered by applying the data in the TemplateData parameter to the
        template specified in the TemplateName parameter.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["messageTag", "emailHeader", "linkTag"],
        "DefaultDimensionValue": str,
    },
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef
):
    pass


_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef
):
    pass


_ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    {"IAMRoleARN": str, "DeliveryStreamARN": str},
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef
):
    pass


_ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef",
    {"TopicARN": str},
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef
):
    pass


_RequiredClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_RequiredClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef", {"Name": str}
)
_OptionalClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_OptionalClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "send",
                "reject",
                "bounce",
                "complaint",
                "delivery",
                "open",
                "click",
                "renderingFailure",
            ]
        ],
        "KinesisFirehoseDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SNSDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationSNSDestinationTypeDef,
    },
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef(
    _RequiredClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
    _OptionalClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef,
):
    """
    The event destination object that you want to apply to the specified configuration set.
    - **Name** *(string) --***[REQUIRED]**

      The name of the event destination. The name must:
      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).
      * Contain less than 64 characters.
    """


_ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)


class ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef(
    _ClientUpdateConfigurationSetTrackingOptionsTrackingOptionsTypeDef
):
    """
    A domain that is used to redirect email recipients to an Amazon SES-operated domain. This domain
    captures open and click events generated by Amazon SES emails.
    For more information, see `Configuring Custom Domains to Handle Open and Click Tracking
    <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html>`__
    in the *Amazon SES Developer Guide* .
    - **CustomRedirectDomain** *(string) --*

      The custom subdomain that will be used to redirect email recipients to the Amazon SES event
      tracking domain.
    """


_ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef = TypedDict(
    "_ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef",
    {"HeaderName": str, "HeaderValue": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef(
    _ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef
):
    pass


_ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef = TypedDict(
    "_ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef",
    {"TopicArn": str, "SmtpReplyCode": str, "StatusCode": str, "Message": str, "Sender": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef(
    _ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef
):
    pass


_ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef = TypedDict(
    "_ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef",
    {"TopicArn": str, "FunctionArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef(
    _ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef
):
    pass


_ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef = TypedDict(
    "_ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef",
    {"TopicArn": str, "BucketName": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef(
    _ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef
):
    pass


_ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef = TypedDict(
    "_ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef",
    {"TopicArn": str, "Encoding": Literal["UTF-8", "Base64"]},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef(
    _ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef
):
    pass


_ClientUpdateReceiptRuleRuleActionsStopActionTypeDef = TypedDict(
    "_ClientUpdateReceiptRuleRuleActionsStopActionTypeDef",
    {"Scope": str, "TopicArn": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsStopActionTypeDef(
    _ClientUpdateReceiptRuleRuleActionsStopActionTypeDef
):
    pass


_ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef = TypedDict(
    "_ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef",
    {"TopicArn": str, "OrganizationArn": str},
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef(
    _ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef
):
    pass


_ClientUpdateReceiptRuleRuleActionsTypeDef = TypedDict(
    "_ClientUpdateReceiptRuleRuleActionsTypeDef",
    {
        "S3Action": ClientUpdateReceiptRuleRuleActionsS3ActionTypeDef,
        "BounceAction": ClientUpdateReceiptRuleRuleActionsBounceActionTypeDef,
        "WorkmailAction": ClientUpdateReceiptRuleRuleActionsWorkmailActionTypeDef,
        "LambdaAction": ClientUpdateReceiptRuleRuleActionsLambdaActionTypeDef,
        "StopAction": ClientUpdateReceiptRuleRuleActionsStopActionTypeDef,
        "AddHeaderAction": ClientUpdateReceiptRuleRuleActionsAddHeaderActionTypeDef,
        "SNSAction": ClientUpdateReceiptRuleRuleActionsSNSActionTypeDef,
    },
    total=False,
)


class ClientUpdateReceiptRuleRuleActionsTypeDef(_ClientUpdateReceiptRuleRuleActionsTypeDef):
    pass


_RequiredClientUpdateReceiptRuleRuleTypeDef = TypedDict(
    "_RequiredClientUpdateReceiptRuleRuleTypeDef", {"Name": str}
)
_OptionalClientUpdateReceiptRuleRuleTypeDef = TypedDict(
    "_OptionalClientUpdateReceiptRuleRuleTypeDef",
    {
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List[ClientUpdateReceiptRuleRuleActionsTypeDef],
        "ScanEnabled": bool,
    },
    total=False,
)


class ClientUpdateReceiptRuleRuleTypeDef(
    _RequiredClientUpdateReceiptRuleRuleTypeDef, _OptionalClientUpdateReceiptRuleRuleTypeDef
):
    """
    A data structure that contains the updated receipt rule information.
    - **Name** *(string) --***[REQUIRED]**

      The name of the receipt rule. The name must:
      * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
      dashes (-).
      * Start and end with a letter or number.
      * Contain less than 64 characters.
    """


_RequiredClientUpdateTemplateTemplateTypeDef = TypedDict(
    "_RequiredClientUpdateTemplateTemplateTypeDef", {"TemplateName": str}
)
_OptionalClientUpdateTemplateTemplateTypeDef = TypedDict(
    "_OptionalClientUpdateTemplateTemplateTypeDef",
    {"SubjectPart": str, "TextPart": str, "HtmlPart": str},
    total=False,
)


class ClientUpdateTemplateTemplateTypeDef(
    _RequiredClientUpdateTemplateTemplateTypeDef, _OptionalClientUpdateTemplateTemplateTypeDef
):
    """
    The content of the email, composed of a subject line, an HTML part, and a text-only part.
    - **TemplateName** *(string) --***[REQUIRED]**

      The name of the template. You will refer to this name when you send email using the
      ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.
    """


_ClientVerifyDomainDkimResponseTypeDef = TypedDict(
    "_ClientVerifyDomainDkimResponseTypeDef", {"DkimTokens": List[str]}, total=False
)


class ClientVerifyDomainDkimResponseTypeDef(_ClientVerifyDomainDkimResponseTypeDef):
    """
    - *(dict) --*

      Returns CNAME records that you must publish to the DNS server of your domain to set up Easy
      DKIM with Amazon SES.
      - **DkimTokens** *(list) --*

        A set of character strings that represent the domain's identity. If the identity is an email
        address, the tokens represent the domain of that address.
        Using these tokens, you need to create DNS CNAME records that point to DKIM public keys that
        are hosted by Amazon SES. Amazon Web Services eventually detects that you've updated your
        DNS records. This detection process might take up to 72 hours. After successful detection,
        Amazon SES is able to DKIM-sign email originating from that domain. (This only applies to
        domain identities, not email address identities.)
        For more information about creating DNS records using DKIM tokens, see the `Amazon SES
        Developer Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html>`__ .
        - *(string) --*
    """


_ClientVerifyDomainIdentityResponseTypeDef = TypedDict(
    "_ClientVerifyDomainIdentityResponseTypeDef", {"VerificationToken": str}, total=False
)


class ClientVerifyDomainIdentityResponseTypeDef(_ClientVerifyDomainIdentityResponseTypeDef):
    """
    - *(dict) --*

      Returns a TXT record that you must publish to the DNS server of your domain to complete domain
      verification with Amazon SES.
      - **VerificationToken** *(string) --*

        A TXT record that you must place in the DNS settings of the domain to complete domain
        verification with Amazon SES.
        As Amazon SES searches for the TXT record, the domain's verification status is "Pending".
        When Amazon SES detects the record, the domain's verification status changes to "Success".
        If Amazon SES is unable to detect the record within 72 hours, the domain's verification
        status changes to "Failed." In that case, if you still want to verify the domain, you must
        restart the verification process from the beginning.
    """


_IdentityExistsWaitWaiterConfigTypeDef = TypedDict(
    "_IdentityExistsWaitWaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)


class IdentityExistsWaitWaiterConfigTypeDef(_IdentityExistsWaitWaiterConfigTypeDef):
    """
    A dictionary that provides parameters to control waiting behavior.
    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 3
    """


_ListConfigurationSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConfigurationSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConfigurationSetsPaginatePaginationConfigTypeDef(
    _ListConfigurationSetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef = TypedDict(
    "_ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef", {"Name": str}, total=False
)


class ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef(
    _ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef
):
    """
    - *(dict) --*

      The name of the configuration set.
      Configuration sets let you create groups of rules that you can apply to the emails you send
      using Amazon SES. For more information about using configuration sets, see `Using Amazon SES
      Configuration Sets
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html>`__ in
      the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/>`__ .
      - **Name** *(string) --*

        The name of the configuration set. The name must meet the following requirements:
        * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
        * Contain 64 characters or fewer.
    """


_ListConfigurationSetsPaginateResponseTypeDef = TypedDict(
    "_ListConfigurationSetsPaginateResponseTypeDef",
    {"ConfigurationSets": List[ListConfigurationSetsPaginateResponseConfigurationSetsTypeDef]},
    total=False,
)


class ListConfigurationSetsPaginateResponseTypeDef(_ListConfigurationSetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      A list of configuration sets associated with your AWS account. Configuration sets enable you
      to publish email sending events. For information about using configuration sets, see the
      `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .
      - **ConfigurationSets** *(list) --*

        A list of configuration sets.
        - *(dict) --*

          The name of the configuration set.
          Configuration sets let you create groups of rules that you can apply to the emails you
          send using Amazon SES. For more information about using configuration sets, see `Using
          Amazon SES Configuration Sets
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html>`__
          in the `Amazon SES Developer Guide
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/>`__ .
          - **Name** *(string) --*

            The name of the configuration set. The name must meet the following requirements:
            * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            * Contain 64 characters or fewer.
    """


_ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef(
    _ListCustomVerificationEmailTemplatesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef = TypedDict(
    "_ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)


class ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef(
    _ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef
):
    """
    - *(dict) --*

      Contains information about a custom verification email template.
      - **TemplateName** *(string) --*

        The name of the custom verification email template.
    """


_ListCustomVerificationEmailTemplatesPaginateResponseTypeDef = TypedDict(
    "_ListCustomVerificationEmailTemplatesPaginateResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List[
            ListCustomVerificationEmailTemplatesPaginateResponseCustomVerificationEmailTemplatesTypeDef
        ]
    },
    total=False,
)


class ListCustomVerificationEmailTemplatesPaginateResponseTypeDef(
    _ListCustomVerificationEmailTemplatesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      A paginated list of custom verification email templates.
      - **CustomVerificationEmailTemplates** *(list) --*

        A list of the custom verification email templates that exist in your account.
        - *(dict) --*

          Contains information about a custom verification email template.
          - **TemplateName** *(string) --*

            The name of the custom verification email template.
    """


_ListIdentitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIdentitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIdentitiesPaginatePaginationConfigTypeDef(_ListIdentitiesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListIdentitiesPaginateResponseTypeDef = TypedDict(
    "_ListIdentitiesPaginateResponseTypeDef", {"Identities": List[str]}, total=False
)


class ListIdentitiesPaginateResponseTypeDef(_ListIdentitiesPaginateResponseTypeDef):
    """
    - *(dict) --*

      A list of all identities that you have attempted to verify under your AWS account, regardless
      of verification status.
      - **Identities** *(list) --*

        A list of identities.
        - *(string) --*
    """


_ListReceiptRuleSetsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListReceiptRuleSetsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListReceiptRuleSetsPaginatePaginationConfigTypeDef(
    _ListReceiptRuleSetsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef = TypedDict(
    "_ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef(
    _ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef
):
    """
    - *(dict) --*

      Information about a receipt rule set.
      A receipt rule set is a collection of rules that specify what Amazon SES should do with mail
      it receives on behalf of your account's verified domains.
      For information about setting up receipt rule sets, see the `Amazon SES Developer Guide
      <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__
      .
      - **Name** *(string) --*

        The name of the receipt rule set. The name must:
        * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or
        dashes (-).
        * Start and end with a letter or number.
        * Contain less than 64 characters.
    """


_ListReceiptRuleSetsPaginateResponseTypeDef = TypedDict(
    "_ListReceiptRuleSetsPaginateResponseTypeDef",
    {"RuleSets": List[ListReceiptRuleSetsPaginateResponseRuleSetsTypeDef]},
    total=False,
)


class ListReceiptRuleSetsPaginateResponseTypeDef(_ListReceiptRuleSetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      A list of receipt rule sets that exist under your AWS account.
      - **RuleSets** *(list) --*

        The metadata for the currently active receipt rule set. The metadata consists of the rule
        set name and the timestamp of when the rule set was created.
        - *(dict) --*

          Information about a receipt rule set.
          A receipt rule set is a collection of rules that specify what Amazon SES should do with
          mail it receives on behalf of your account's verified domains.
          For information about setting up receipt rule sets, see the `Amazon SES Developer Guide
          <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__
          .
          - **Name** *(string) --*

            The name of the receipt rule set. The name must:
            * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_),
            or dashes (-).
            * Start and end with a letter or number.
            * Contain less than 64 characters.
    """


_ListTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTemplatesPaginatePaginationConfigTypeDef(_ListTemplatesPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListTemplatesPaginateResponseTemplatesMetadataTypeDef = TypedDict(
    "_ListTemplatesPaginateResponseTemplatesMetadataTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)


class ListTemplatesPaginateResponseTemplatesMetadataTypeDef(
    _ListTemplatesPaginateResponseTemplatesMetadataTypeDef
):
    """
    - *(dict) --*

      Contains information about an email template.
      - **Name** *(string) --*

        The name of the template.
    """


_ListTemplatesPaginateResponseTypeDef = TypedDict(
    "_ListTemplatesPaginateResponseTypeDef",
    {"TemplatesMetadata": List[ListTemplatesPaginateResponseTemplatesMetadataTypeDef]},
    total=False,
)


class ListTemplatesPaginateResponseTypeDef(_ListTemplatesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **TemplatesMetadata** *(list) --*

        An array the contains the name and creation time stamp for each template in your Amazon SES
        account.
        - *(dict) --*

          Contains information about an email template.
          - **Name** *(string) --*

            The name of the template.
    """
