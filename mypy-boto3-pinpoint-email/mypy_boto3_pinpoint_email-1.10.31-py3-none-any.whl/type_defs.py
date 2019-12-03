"Main interface for pinpoint-email service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateConfigurationSetDeliveryOptionsTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    "ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    "ClientCreateConfigurationSetReputationOptionsTypeDef",
    "ClientCreateConfigurationSetSendingOptionsTypeDef",
    "ClientCreateConfigurationSetTagsTypeDef",
    "ClientCreateConfigurationSetTrackingOptionsTypeDef",
    "ClientCreateDedicatedIpPoolTagsTypeDef",
    "ClientCreateDeliverabilityTestReportContentRawTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef",
    "ClientCreateDeliverabilityTestReportContentSimpleTypeDef",
    "ClientCreateDeliverabilityTestReportContentTemplateTypeDef",
    "ClientCreateDeliverabilityTestReportContentTypeDef",
    "ClientCreateDeliverabilityTestReportResponseTypeDef",
    "ClientCreateDeliverabilityTestReportTagsTypeDef",
    "ClientCreateEmailIdentityResponseDkimAttributesTypeDef",
    "ClientCreateEmailIdentityResponseTypeDef",
    "ClientCreateEmailIdentityTagsTypeDef",
    "ClientGetAccountResponseSendQuotaTypeDef",
    "ClientGetAccountResponseTypeDef",
    "ClientGetBlacklistReportsResponseBlacklistReportTypeDef",
    "ClientGetBlacklistReportsResponseTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef",
    "ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    "ClientGetConfigurationSetResponseDeliveryOptionsTypeDef",
    "ClientGetConfigurationSetResponseReputationOptionsTypeDef",
    "ClientGetConfigurationSetResponseSendingOptionsTypeDef",
    "ClientGetConfigurationSetResponseTagsTypeDef",
    "ClientGetConfigurationSetResponseTrackingOptionsTypeDef",
    "ClientGetConfigurationSetResponseTypeDef",
    "ClientGetDedicatedIpResponseDedicatedIpTypeDef",
    "ClientGetDedicatedIpResponseTypeDef",
    "ClientGetDedicatedIpsResponseDedicatedIpsTypeDef",
    "ClientGetDedicatedIpsResponseTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef",
    "ClientGetDeliverabilityDashboardOptionsResponseTypeDef",
    "ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef",
    "ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef",
    "ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef",
    "ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef",
    "ClientGetDeliverabilityTestReportResponseTagsTypeDef",
    "ClientGetDeliverabilityTestReportResponseTypeDef",
    "ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef",
    "ClientGetDomainDeliverabilityCampaignResponseTypeDef",
    "ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef",
    "ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef",
    "ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef",
    "ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef",
    "ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef",
    "ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef",
    "ClientGetDomainStatisticsReportResponseTypeDef",
    "ClientGetEmailIdentityResponseDkimAttributesTypeDef",
    "ClientGetEmailIdentityResponseMailFromAttributesTypeDef",
    "ClientGetEmailIdentityResponseTagsTypeDef",
    "ClientGetEmailIdentityResponseTypeDef",
    "ClientListConfigurationSetsResponseTypeDef",
    "ClientListDedicatedIpPoolsResponseTypeDef",
    "ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef",
    "ClientListDeliverabilityTestReportsResponseTypeDef",
    "ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef",
    "ClientListDomainDeliverabilityCampaignsResponseTypeDef",
    "ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef",
    "ClientListEmailIdentitiesResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    "ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef",
    "ClientSendEmailContentRawTypeDef",
    "ClientSendEmailContentSimpleBodyHtmlTypeDef",
    "ClientSendEmailContentSimpleBodyTextTypeDef",
    "ClientSendEmailContentSimpleBodyTypeDef",
    "ClientSendEmailContentSimpleSubjectTypeDef",
    "ClientSendEmailContentSimpleTypeDef",
    "ClientSendEmailContentTemplateTypeDef",
    "ClientSendEmailContentTypeDef",
    "ClientSendEmailDestinationTypeDef",
    "ClientSendEmailEmailTagsTypeDef",
    "ClientSendEmailResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    "ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    "GetDedicatedIpsPaginatePaginationConfigTypeDef",
    "GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef",
    "GetDedicatedIpsPaginateResponseTypeDef",
    "ListConfigurationSetsPaginatePaginationConfigTypeDef",
    "ListConfigurationSetsPaginateResponseTypeDef",
    "ListDedicatedIpPoolsPaginatePaginationConfigTypeDef",
    "ListDedicatedIpPoolsPaginateResponseTypeDef",
    "ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef",
    "ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef",
    "ListDeliverabilityTestReportsPaginateResponseTypeDef",
    "ListEmailIdentitiesPaginatePaginationConfigTypeDef",
    "ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef",
    "ListEmailIdentitiesPaginateResponseTypeDef",
)


_ClientCreateConfigurationSetDeliveryOptionsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetDeliveryOptionsTypeDef",
    {"TlsPolicy": Literal["REQUIRE", "OPTIONAL"], "SendingPoolName": str},
    total=False,
)


class ClientCreateConfigurationSetDeliveryOptionsTypeDef(
    _ClientCreateConfigurationSetDeliveryOptionsTypeDef
):
    """
    An object that defines the dedicated IP pool that is used to send emails that you send using the
    configuration set.
    - **TlsPolicy** *(string) --*

      Specifies whether messages that use the configuration set are required to use Transport Layer
      Security (TLS). If the value is ``Require`` , messages are only delivered if a TLS connection
      can be established. If the value is ``Optional`` , messages can be delivered in plain text if
      a TLS connection can't be established.
    """


_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["MESSAGE_TAG", "EMAIL_HEADER", "LINK_TAG"],
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
    {"IamRoleArn": str, "DeliveryStreamArn": str},
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef
):
    pass


_ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    {"ApplicationArn": str},
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef
):
    pass


_ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef
):
    pass


_ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "SEND",
                "REJECT",
                "BOUNCE",
                "COMPLAINT",
                "DELIVERY",
                "OPEN",
                "CLICK",
                "RENDERING_FAILURE",
            ]
        ],
        "KinesisFirehoseDestination": ClientCreateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientCreateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SnsDestination": ClientCreateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef,
        "PinpointDestination": ClientCreateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef,
    },
    total=False,
)


class ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef(
    _ClientCreateConfigurationSetEventDestinationEventDestinationTypeDef
):
    """
    An object that defines the event destination.
    - **Enabled** *(boolean) --*

      If ``true`` , the event destination is enabled. When the event destination is enabled, the
      specified event types are sent to the destinations in this ``EventDestinationDefinition`` .
      If ``false`` , the event destination is disabled. When the event destination is disabled,
      events aren't sent to the specified destinations.
    """


_ClientCreateConfigurationSetReputationOptionsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetReputationOptionsTypeDef",
    {"ReputationMetricsEnabled": bool, "LastFreshStart": datetime},
    total=False,
)


class ClientCreateConfigurationSetReputationOptionsTypeDef(
    _ClientCreateConfigurationSetReputationOptionsTypeDef
):
    """
    An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails
    that you send that use the configuration set.
    - **ReputationMetricsEnabled** *(boolean) --*

      If ``true`` , tracking of reputation metrics is enabled for the configuration set. If
      ``false`` , tracking of reputation metrics is disabled for the configuration set.
    """


_ClientCreateConfigurationSetSendingOptionsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetSendingOptionsTypeDef", {"SendingEnabled": bool}, total=False
)


class ClientCreateConfigurationSetSendingOptionsTypeDef(
    _ClientCreateConfigurationSetSendingOptionsTypeDef
):
    """
    An object that defines whether or not Amazon Pinpoint can send email that you send using the
    configuration set.
    - **SendingEnabled** *(boolean) --*

      If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending
      is disabled for the configuration set.
    """


_RequiredClientCreateConfigurationSetTagsTypeDef = TypedDict(
    "_RequiredClientCreateConfigurationSetTagsTypeDef", {"Key": str}
)
_OptionalClientCreateConfigurationSetTagsTypeDef = TypedDict(
    "_OptionalClientCreateConfigurationSetTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateConfigurationSetTagsTypeDef(
    _RequiredClientCreateConfigurationSetTagsTypeDef,
    _OptionalClientCreateConfigurationSetTagsTypeDef,
):
    """
    - *(dict) --*

      An object that defines the tags that are associated with a resource. A *tag* is a label that
      you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
      categorize and manage resources in different ways, such as by purpose, owner, environment, or
      other criteria. A resource can have as many as 50 tags.
      Each tag consists of a required *tag key* and an associated *tag value* , both of which you
      define. A tag key is a general label that acts as a category for a more specific tag value. A
      tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
      characters. A tag value can contain as many as 256 characters. The characters can be Unicode
      letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
      additional restrictions apply to tags:
      * Tag keys and values are case sensitive.
      * For each associated resource, each tag key must be unique and it can have only one value.
      * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
      that you define. In addition, you can't edit or remove tag keys or values that use this
      prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
      * You can associate tags with public or shared resources, but the tags are available only for
      your AWS account, not any other accounts that share the resource. In addition, the tags are
      available only for resources that are located in the specified AWS Region for your AWS
      account.
      - **Key** *(string) --***[REQUIRED]**

        One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
        characters. The minimum length is 1 character.
    """


_ClientCreateConfigurationSetTrackingOptionsTypeDef = TypedDict(
    "_ClientCreateConfigurationSetTrackingOptionsTypeDef", {"CustomRedirectDomain": str}
)


class ClientCreateConfigurationSetTrackingOptionsTypeDef(
    _ClientCreateConfigurationSetTrackingOptionsTypeDef
):
    """
    An object that defines the open and click tracking options for emails that you send using the
    configuration set.
    - **CustomRedirectDomain** *(string) --***[REQUIRED]**

      The domain that you want to use for tracking open and click events.
    """


_RequiredClientCreateDedicatedIpPoolTagsTypeDef = TypedDict(
    "_RequiredClientCreateDedicatedIpPoolTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDedicatedIpPoolTagsTypeDef = TypedDict(
    "_OptionalClientCreateDedicatedIpPoolTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDedicatedIpPoolTagsTypeDef(
    _RequiredClientCreateDedicatedIpPoolTagsTypeDef, _OptionalClientCreateDedicatedIpPoolTagsTypeDef
):
    """
    - *(dict) --*

      An object that defines the tags that are associated with a resource. A *tag* is a label that
      you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
      categorize and manage resources in different ways, such as by purpose, owner, environment, or
      other criteria. A resource can have as many as 50 tags.
      Each tag consists of a required *tag key* and an associated *tag value* , both of which you
      define. A tag key is a general label that acts as a category for a more specific tag value. A
      tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
      characters. A tag value can contain as many as 256 characters. The characters can be Unicode
      letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
      additional restrictions apply to tags:
      * Tag keys and values are case sensitive.
      * For each associated resource, each tag key must be unique and it can have only one value.
      * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
      that you define. In addition, you can't edit or remove tag keys or values that use this
      prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
      * You can associate tags with public or shared resources, but the tags are available only for
      your AWS account, not any other accounts that share the resource. In addition, the tags are
      available only for resources that are located in the specified AWS Region for your AWS
      account.
      - **Key** *(string) --***[REQUIRED]**

        One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
        characters. The minimum length is 1 character.
    """


_ClientCreateDeliverabilityTestReportContentRawTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentRawTypeDef", {"Data": bytes}, total=False
)


class ClientCreateDeliverabilityTestReportContentRawTypeDef(
    _ClientCreateDeliverabilityTestReportContentRawTypeDef
):
    pass


_ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef",
    {"Data": str, "Charset": str},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef(
    _ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef
):
    pass


_ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef",
    {"Data": str, "Charset": str},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef(
    _ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef
):
    pass


_ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef",
    {
        "Text": ClientCreateDeliverabilityTestReportContentSimpleBodyTextTypeDef,
        "Html": ClientCreateDeliverabilityTestReportContentSimpleBodyHtmlTypeDef,
    },
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef(
    _ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef
):
    pass


_RequiredClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef = TypedDict(
    "_RequiredClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef", {"Data": str}
)
_OptionalClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef = TypedDict(
    "_OptionalClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef",
    {"Charset": str},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef(
    _RequiredClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef,
    _OptionalClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef,
):
    """
    - **Subject** *(dict) --***[REQUIRED]**

      The subject line of the email. The subject line can only contain 7-bit ASCII characters.
      However, you can specify non-ASCII characters in the subject line by using encoded-word
      syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .
      - **Data** *(string) --***[REQUIRED]**

        The content of the message itself.
    """


_RequiredClientCreateDeliverabilityTestReportContentSimpleTypeDef = TypedDict(
    "_RequiredClientCreateDeliverabilityTestReportContentSimpleTypeDef",
    {"Subject": ClientCreateDeliverabilityTestReportContentSimpleSubjectTypeDef},
)
_OptionalClientCreateDeliverabilityTestReportContentSimpleTypeDef = TypedDict(
    "_OptionalClientCreateDeliverabilityTestReportContentSimpleTypeDef",
    {"Body": ClientCreateDeliverabilityTestReportContentSimpleBodyTypeDef},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentSimpleTypeDef(
    _RequiredClientCreateDeliverabilityTestReportContentSimpleTypeDef,
    _OptionalClientCreateDeliverabilityTestReportContentSimpleTypeDef,
):
    """
    - **Simple** *(dict) --*

      The simple email message. The message consists of a subject and a message body.
      - **Subject** *(dict) --***[REQUIRED]**

        The subject line of the email. The subject line can only contain 7-bit ASCII characters.
        However, you can specify non-ASCII characters in the subject line by using encoded-word
        syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .
        - **Data** *(string) --***[REQUIRED]**

          The content of the message itself.
    """


_ClientCreateDeliverabilityTestReportContentTemplateTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentTemplateTypeDef",
    {"TemplateArn": str, "TemplateData": str},
    total=False,
)


class ClientCreateDeliverabilityTestReportContentTemplateTypeDef(
    _ClientCreateDeliverabilityTestReportContentTemplateTypeDef
):
    pass


_ClientCreateDeliverabilityTestReportContentTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportContentTypeDef",
    {
        "Simple": ClientCreateDeliverabilityTestReportContentSimpleTypeDef,
        "Raw": ClientCreateDeliverabilityTestReportContentRawTypeDef,
        "Template": ClientCreateDeliverabilityTestReportContentTemplateTypeDef,
    },
    total=False,
)


class ClientCreateDeliverabilityTestReportContentTypeDef(
    _ClientCreateDeliverabilityTestReportContentTypeDef
):
    """
    The HTML body of the message that you sent when you performed the predictive inbox placement
    test.
    - **Simple** *(dict) --*

      The simple email message. The message consists of a subject and a message body.
      - **Subject** *(dict) --***[REQUIRED]**

        The subject line of the email. The subject line can only contain 7-bit ASCII characters.
        However, you can specify non-ASCII characters in the subject line by using encoded-word
        syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .
        - **Data** *(string) --***[REQUIRED]**

          The content of the message itself.
    """


_ClientCreateDeliverabilityTestReportResponseTypeDef = TypedDict(
    "_ClientCreateDeliverabilityTestReportResponseTypeDef",
    {"ReportId": str, "DeliverabilityTestStatus": Literal["IN_PROGRESS", "COMPLETED"]},
    total=False,
)


class ClientCreateDeliverabilityTestReportResponseTypeDef(
    _ClientCreateDeliverabilityTestReportResponseTypeDef
):
    """
    - *(dict) --*

      Information about the predictive inbox placement test that you created.
      - **ReportId** *(string) --*

        A unique string that identifies the predictive inbox placement test.
    """


_RequiredClientCreateDeliverabilityTestReportTagsTypeDef = TypedDict(
    "_RequiredClientCreateDeliverabilityTestReportTagsTypeDef", {"Key": str}
)
_OptionalClientCreateDeliverabilityTestReportTagsTypeDef = TypedDict(
    "_OptionalClientCreateDeliverabilityTestReportTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateDeliverabilityTestReportTagsTypeDef(
    _RequiredClientCreateDeliverabilityTestReportTagsTypeDef,
    _OptionalClientCreateDeliverabilityTestReportTagsTypeDef,
):
    """
    - *(dict) --*

      An object that defines the tags that are associated with a resource. A *tag* is a label that
      you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
      categorize and manage resources in different ways, such as by purpose, owner, environment, or
      other criteria. A resource can have as many as 50 tags.
      Each tag consists of a required *tag key* and an associated *tag value* , both of which you
      define. A tag key is a general label that acts as a category for a more specific tag value. A
      tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
      characters. A tag value can contain as many as 256 characters. The characters can be Unicode
      letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
      additional restrictions apply to tags:
      * Tag keys and values are case sensitive.
      * For each associated resource, each tag key must be unique and it can have only one value.
      * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
      that you define. In addition, you can't edit or remove tag keys or values that use this
      prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
      * You can associate tags with public or shared resources, but the tags are available only for
      your AWS account, not any other accounts that share the resource. In addition, the tags are
      available only for resources that are located in the specified AWS Region for your AWS
      account.
      - **Key** *(string) --***[REQUIRED]**

        One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
        characters. The minimum length is 1 character.
    """


_ClientCreateEmailIdentityResponseDkimAttributesTypeDef = TypedDict(
    "_ClientCreateEmailIdentityResponseDkimAttributesTypeDef",
    {
        "SigningEnabled": bool,
        "Status": Literal["PENDING", "SUCCESS", "FAILED", "TEMPORARY_FAILURE", "NOT_STARTED"],
        "Tokens": List[str],
    },
    total=False,
)


class ClientCreateEmailIdentityResponseDkimAttributesTypeDef(
    _ClientCreateEmailIdentityResponseDkimAttributesTypeDef
):
    pass


_ClientCreateEmailIdentityResponseTypeDef = TypedDict(
    "_ClientCreateEmailIdentityResponseTypeDef",
    {
        "IdentityType": Literal["EMAIL_ADDRESS", "DOMAIN", "MANAGED_DOMAIN"],
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": ClientCreateEmailIdentityResponseDkimAttributesTypeDef,
    },
    total=False,
)


class ClientCreateEmailIdentityResponseTypeDef(_ClientCreateEmailIdentityResponseTypeDef):
    """
    - *(dict) --*

      If the email identity is a domain, this object contains tokens that you can use to create a
      set of CNAME records. To sucessfully verify your domain, you have to add these records to the
      DNS configuration for your domain.
      If the email identity is an email address, this object is empty.
      - **IdentityType** *(string) --*

        The email identity type.
    """


_RequiredClientCreateEmailIdentityTagsTypeDef = TypedDict(
    "_RequiredClientCreateEmailIdentityTagsTypeDef", {"Key": str}
)
_OptionalClientCreateEmailIdentityTagsTypeDef = TypedDict(
    "_OptionalClientCreateEmailIdentityTagsTypeDef", {"Value": str}, total=False
)


class ClientCreateEmailIdentityTagsTypeDef(
    _RequiredClientCreateEmailIdentityTagsTypeDef, _OptionalClientCreateEmailIdentityTagsTypeDef
):
    """
    - *(dict) --*

      An object that defines the tags that are associated with a resource. A *tag* is a label that
      you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
      categorize and manage resources in different ways, such as by purpose, owner, environment, or
      other criteria. A resource can have as many as 50 tags.
      Each tag consists of a required *tag key* and an associated *tag value* , both of which you
      define. A tag key is a general label that acts as a category for a more specific tag value. A
      tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
      characters. A tag value can contain as many as 256 characters. The characters can be Unicode
      letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
      additional restrictions apply to tags:
      * Tag keys and values are case sensitive.
      * For each associated resource, each tag key must be unique and it can have only one value.
      * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
      that you define. In addition, you can't edit or remove tag keys or values that use this
      prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
      * You can associate tags with public or shared resources, but the tags are available only for
      your AWS account, not any other accounts that share the resource. In addition, the tags are
      available only for resources that are located in the specified AWS Region for your AWS
      account.
      - **Key** *(string) --***[REQUIRED]**

        One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
        characters. The minimum length is 1 character.
    """


_ClientGetAccountResponseSendQuotaTypeDef = TypedDict(
    "_ClientGetAccountResponseSendQuotaTypeDef",
    {"Max24HourSend": float, "MaxSendRate": float, "SentLast24Hours": float},
    total=False,
)


class ClientGetAccountResponseSendQuotaTypeDef(_ClientGetAccountResponseSendQuotaTypeDef):
    """
    - **SendQuota** *(dict) --*

      An object that contains information about the per-day and per-second sending limits for your
      Amazon Pinpoint account in the current AWS Region.
      - **Max24HourSend** *(float) --*

        The maximum number of emails that you can send in the current AWS Region over a 24-hour
        period. This value is also called your *sending quota* .
    """


_ClientGetAccountResponseTypeDef = TypedDict(
    "_ClientGetAccountResponseTypeDef",
    {
        "SendQuota": ClientGetAccountResponseSendQuotaTypeDef,
        "SendingEnabled": bool,
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
    },
    total=False,
)


class ClientGetAccountResponseTypeDef(_ClientGetAccountResponseTypeDef):
    """
    - *(dict) --*

      A list of details about the email-sending capabilities of your Amazon Pinpoint account in the
      current AWS Region.
      - **SendQuota** *(dict) --*

        An object that contains information about the per-day and per-second sending limits for your
        Amazon Pinpoint account in the current AWS Region.
        - **Max24HourSend** *(float) --*

          The maximum number of emails that you can send in the current AWS Region over a 24-hour
          period. This value is also called your *sending quota* .
    """


_ClientGetBlacklistReportsResponseBlacklistReportTypeDef = TypedDict(
    "_ClientGetBlacklistReportsResponseBlacklistReportTypeDef",
    {"RblName": str, "ListingTime": datetime, "Description": str},
    total=False,
)


class ClientGetBlacklistReportsResponseBlacklistReportTypeDef(
    _ClientGetBlacklistReportsResponseBlacklistReportTypeDef
):
    pass


_ClientGetBlacklistReportsResponseTypeDef = TypedDict(
    "_ClientGetBlacklistReportsResponseTypeDef",
    {"BlacklistReport": Dict[str, List[ClientGetBlacklistReportsResponseBlacklistReportTypeDef]]},
    total=False,
)


class ClientGetBlacklistReportsResponseTypeDef(_ClientGetBlacklistReportsResponseTypeDef):
    """
    - *(dict) --*

      An object that contains information about blacklist events.
      - **BlacklistReport** *(dict) --*

        An object that contains information about a blacklist that one of your dedicated IP
        addresses appears on.
        - *(string) --*

          An IP address that you want to obtain blacklist information for.
          - *(list) --*

            - *(dict) --*

              An object that contains information about a blacklisting event that impacts one of the
              dedicated IP addresses that is associated with your account.
              - **RblName** *(string) --*

                The name of the blacklist that the IP address appears on.
    """


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["MESSAGE_TAG", "EMAIL_HEADER", "LINK_TAG"],
        "DefaultDimensionValue": str,
    },
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef
):
    pass


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List[
            ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationDimensionConfigurationsTypeDef
        ]
    },
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef
):
    pass


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef",
    {"IamRoleArn": str, "DeliveryStreamArn": str},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef
):
    pass


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef",
    {"ApplicationArn": str},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef
):
    pass


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef
):
    pass


_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef",
    {
        "Name": str,
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "SEND",
                "REJECT",
                "BOUNCE",
                "COMPLAINT",
                "DELIVERY",
                "OPEN",
                "CLICK",
                "RENDERING_FAILURE",
            ]
        ],
        "KinesisFirehoseDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsCloudWatchDestinationTypeDef,
        "SnsDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsSnsDestinationTypeDef,
        "PinpointDestination": ClientGetConfigurationSetEventDestinationsResponseEventDestinationsPinpointDestinationTypeDef,
    },
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef
):
    """
    - *(dict) --*

      In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and
      complaints. *Event destinations* are places that you can send information about these events
      to. For example, you can send event data to Amazon SNS to receive notifications when you
      receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to
      Amazon S3 for long-term storage.
      - **Name** *(string) --*

        A name that identifies the event destination.
    """


_ClientGetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "_ClientGetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List[
            ClientGetConfigurationSetEventDestinationsResponseEventDestinationsTypeDef
        ]
    },
    total=False,
)


class ClientGetConfigurationSetEventDestinationsResponseTypeDef(
    _ClientGetConfigurationSetEventDestinationsResponseTypeDef
):
    """
    - *(dict) --*

      Information about an event destination for a configuration set.
      - **EventDestinations** *(list) --*

        An array that includes all of the events destinations that have been configured for the
        configuration set.
        - *(dict) --*

          In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces,
          and complaints. *Event destinations* are places that you can send information about these
          events to. For example, you can send event data to Amazon SNS to receive notifications
          when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to
          stream data to Amazon S3 for long-term storage.
          - **Name** *(string) --*

            A name that identifies the event destination.
    """


_ClientGetConfigurationSetResponseDeliveryOptionsTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseDeliveryOptionsTypeDef",
    {"TlsPolicy": Literal["REQUIRE", "OPTIONAL"], "SendingPoolName": str},
    total=False,
)


class ClientGetConfigurationSetResponseDeliveryOptionsTypeDef(
    _ClientGetConfigurationSetResponseDeliveryOptionsTypeDef
):
    pass


_ClientGetConfigurationSetResponseReputationOptionsTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseReputationOptionsTypeDef",
    {"ReputationMetricsEnabled": bool, "LastFreshStart": datetime},
    total=False,
)


class ClientGetConfigurationSetResponseReputationOptionsTypeDef(
    _ClientGetConfigurationSetResponseReputationOptionsTypeDef
):
    pass


_ClientGetConfigurationSetResponseSendingOptionsTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseSendingOptionsTypeDef", {"SendingEnabled": bool}, total=False
)


class ClientGetConfigurationSetResponseSendingOptionsTypeDef(
    _ClientGetConfigurationSetResponseSendingOptionsTypeDef
):
    pass


_ClientGetConfigurationSetResponseTagsTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetConfigurationSetResponseTagsTypeDef(_ClientGetConfigurationSetResponseTagsTypeDef):
    pass


_ClientGetConfigurationSetResponseTrackingOptionsTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseTrackingOptionsTypeDef",
    {"CustomRedirectDomain": str},
    total=False,
)


class ClientGetConfigurationSetResponseTrackingOptionsTypeDef(
    _ClientGetConfigurationSetResponseTrackingOptionsTypeDef
):
    pass


_ClientGetConfigurationSetResponseTypeDef = TypedDict(
    "_ClientGetConfigurationSetResponseTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": ClientGetConfigurationSetResponseTrackingOptionsTypeDef,
        "DeliveryOptions": ClientGetConfigurationSetResponseDeliveryOptionsTypeDef,
        "ReputationOptions": ClientGetConfigurationSetResponseReputationOptionsTypeDef,
        "SendingOptions": ClientGetConfigurationSetResponseSendingOptionsTypeDef,
        "Tags": List[ClientGetConfigurationSetResponseTagsTypeDef],
    },
    total=False,
)


class ClientGetConfigurationSetResponseTypeDef(_ClientGetConfigurationSetResponseTypeDef):
    """
    - *(dict) --*

      Information about a configuration set.
      - **ConfigurationSetName** *(string) --*

        The name of the configuration set.
    """


_ClientGetDedicatedIpResponseDedicatedIpTypeDef = TypedDict(
    "_ClientGetDedicatedIpResponseDedicatedIpTypeDef",
    {
        "Ip": str,
        "WarmupStatus": Literal["IN_PROGRESS", "DONE"],
        "WarmupPercentage": int,
        "PoolName": str,
    },
    total=False,
)


class ClientGetDedicatedIpResponseDedicatedIpTypeDef(
    _ClientGetDedicatedIpResponseDedicatedIpTypeDef
):
    """
    - **DedicatedIp** *(dict) --*

      An object that contains information about a dedicated IP address.
      - **Ip** *(string) --*

        An IP address that is reserved for use by your Amazon Pinpoint account.
    """


_ClientGetDedicatedIpResponseTypeDef = TypedDict(
    "_ClientGetDedicatedIpResponseTypeDef",
    {"DedicatedIp": ClientGetDedicatedIpResponseDedicatedIpTypeDef},
    total=False,
)


class ClientGetDedicatedIpResponseTypeDef(_ClientGetDedicatedIpResponseTypeDef):
    """
    - *(dict) --*

      Information about a dedicated IP address.
      - **DedicatedIp** *(dict) --*

        An object that contains information about a dedicated IP address.
        - **Ip** *(string) --*

          An IP address that is reserved for use by your Amazon Pinpoint account.
    """


_ClientGetDedicatedIpsResponseDedicatedIpsTypeDef = TypedDict(
    "_ClientGetDedicatedIpsResponseDedicatedIpsTypeDef",
    {
        "Ip": str,
        "WarmupStatus": Literal["IN_PROGRESS", "DONE"],
        "WarmupPercentage": int,
        "PoolName": str,
    },
    total=False,
)


class ClientGetDedicatedIpsResponseDedicatedIpsTypeDef(
    _ClientGetDedicatedIpsResponseDedicatedIpsTypeDef
):
    """
    - *(dict) --*

      Contains information about a dedicated IP address that is associated with your Amazon Pinpoint
      account.
      - **Ip** *(string) --*

        An IP address that is reserved for use by your Amazon Pinpoint account.
    """


_ClientGetDedicatedIpsResponseTypeDef = TypedDict(
    "_ClientGetDedicatedIpsResponseTypeDef",
    {"DedicatedIps": List[ClientGetDedicatedIpsResponseDedicatedIpsTypeDef], "NextToken": str},
    total=False,
)


class ClientGetDedicatedIpsResponseTypeDef(_ClientGetDedicatedIpsResponseTypeDef):
    """
    - *(dict) --*

      Information about the dedicated IP addresses that are associated with your Amazon Pinpoint
      account.
      - **DedicatedIps** *(list) --*

        A list of dedicated IP addresses that are reserved for use by your Amazon Pinpoint account.
        - *(dict) --*

          Contains information about a dedicated IP address that is associated with your Amazon
          Pinpoint account.
          - **Ip** *(string) --*

            An IP address that is reserved for use by your Amazon Pinpoint account.
    """


_ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef = TypedDict(
    "_ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    {"Global": bool, "TrackedIsps": List[str]},
    total=False,
)


class ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef(
    _ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef
):
    pass


_ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef = TypedDict(
    "_ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsInboxPlacementTrackingOptionTypeDef,
    },
    total=False,
)


class ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef(
    _ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef
):
    pass


_ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef = TypedDict(
    "_ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    {"Global": bool, "TrackedIsps": List[str]},
    total=False,
)


class ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef(
    _ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef
):
    pass


_ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef = TypedDict(
    "_ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsInboxPlacementTrackingOptionTypeDef,
    },
    total=False,
)


class ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef(
    _ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef
):
    pass


_ClientGetDeliverabilityDashboardOptionsResponseTypeDef = TypedDict(
    "_ClientGetDeliverabilityDashboardOptionsResponseTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscriptionExpiryDate": datetime,
        "AccountStatus": Literal["ACTIVE", "PENDING_EXPIRATION", "DISABLED"],
        "ActiveSubscribedDomains": List[
            ClientGetDeliverabilityDashboardOptionsResponseActiveSubscribedDomainsTypeDef
        ],
        "PendingExpirationSubscribedDomains": List[
            ClientGetDeliverabilityDashboardOptionsResponsePendingExpirationSubscribedDomainsTypeDef
        ],
    },
    total=False,
)


class ClientGetDeliverabilityDashboardOptionsResponseTypeDef(
    _ClientGetDeliverabilityDashboardOptionsResponseTypeDef
):
    """
    - *(dict) --*

      An object that shows the status of the Deliverability dashboard for your Amazon Pinpoint
      account.
      - **DashboardEnabled** *(boolean) --*

        Specifies whether the Deliverability dashboard is enabled for your Amazon Pinpoint account.
        If this value is ``true`` , the dashboard is enabled.
    """


_ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": Literal["IN_PROGRESS", "COMPLETED"],
    },
    total=False,
)


class ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef(
    _ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef
):
    """
    - **DeliverabilityTestReport** *(dict) --*

      An object that contains the results of the predictive inbox placement test.
      - **ReportId** *(string) --*

        A unique string that identifies the predictive inbox placement test.
    """


_ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef",
    {
        "InboxPercentage": float,
        "SpamPercentage": float,
        "MissingPercentage": float,
        "SpfPercentage": float,
        "DkimPercentage": float,
    },
    total=False,
)


class ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef(
    _ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef
):
    pass


_ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef",
    {
        "IspName": str,
        "PlacementStatistics": ClientGetDeliverabilityTestReportResponseIspPlacementsPlacementStatisticsTypeDef,
    },
    total=False,
)


class ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef(
    _ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef
):
    pass


_ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef",
    {
        "InboxPercentage": float,
        "SpamPercentage": float,
        "MissingPercentage": float,
        "SpfPercentage": float,
        "DkimPercentage": float,
    },
    total=False,
)


class ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef(
    _ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef
):
    pass


_ClientGetDeliverabilityTestReportResponseTagsTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetDeliverabilityTestReportResponseTagsTypeDef(
    _ClientGetDeliverabilityTestReportResponseTagsTypeDef
):
    pass


_ClientGetDeliverabilityTestReportResponseTypeDef = TypedDict(
    "_ClientGetDeliverabilityTestReportResponseTypeDef",
    {
        "DeliverabilityTestReport": ClientGetDeliverabilityTestReportResponseDeliverabilityTestReportTypeDef,
        "OverallPlacement": ClientGetDeliverabilityTestReportResponseOverallPlacementTypeDef,
        "IspPlacements": List[ClientGetDeliverabilityTestReportResponseIspPlacementsTypeDef],
        "Message": str,
        "Tags": List[ClientGetDeliverabilityTestReportResponseTagsTypeDef],
    },
    total=False,
)


class ClientGetDeliverabilityTestReportResponseTypeDef(
    _ClientGetDeliverabilityTestReportResponseTypeDef
):
    """
    - *(dict) --*

      The results of the predictive inbox placement test.
      - **DeliverabilityTestReport** *(dict) --*

        An object that contains the results of the predictive inbox placement test.
        - **ReportId** *(string) --*

          A unique string that identifies the predictive inbox placement test.
    """


_ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef = TypedDict(
    "_ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef",
    {
        "CampaignId": str,
        "ImageUrl": str,
        "Subject": str,
        "FromAddress": str,
        "SendingIps": List[str],
        "FirstSeenDateTime": datetime,
        "LastSeenDateTime": datetime,
        "InboxCount": int,
        "SpamCount": int,
        "ReadRate": float,
        "DeleteRate": float,
        "ReadDeleteRate": float,
        "ProjectedVolume": int,
        "Esps": List[str],
    },
    total=False,
)


class ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef(
    _ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef
):
    """
    - **DomainDeliverabilityCampaign** *(dict) --*

      An object that contains the deliverability data for the campaign.
      - **CampaignId** *(string) --*

        The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns
        this identifier to a campaign. This value is not the same as the campaign identifier that
        Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon Pinpoint
        API or the Amazon Pinpoint console.
    """


_ClientGetDomainDeliverabilityCampaignResponseTypeDef = TypedDict(
    "_ClientGetDomainDeliverabilityCampaignResponseTypeDef",
    {
        "DomainDeliverabilityCampaign": ClientGetDomainDeliverabilityCampaignResponseDomainDeliverabilityCampaignTypeDef
    },
    total=False,
)


class ClientGetDomainDeliverabilityCampaignResponseTypeDef(
    _ClientGetDomainDeliverabilityCampaignResponseTypeDef
):
    """
    - *(dict) --*

      An object that contains all the deliverability data for a specific campaign. This data is
      available for a campaign only if the campaign sent email by using a domain that the
      Deliverability dashboard is enabled for (``PutDeliverabilityDashboardOption`` operation).
      - **DomainDeliverabilityCampaign** *(dict) --*

        An object that contains the deliverability data for the campaign.
        - **CampaignId** *(string) --*

          The unique identifier for the campaign. Amazon Pinpoint automatically generates and
          assigns this identifier to a campaign. This value is not the same as the campaign
          identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using
          the Amazon Pinpoint API or the Amazon Pinpoint console.
    """


_ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef",
    {
        "IspName": str,
        "InboxRawCount": int,
        "SpamRawCount": int,
        "InboxPercentage": float,
        "SpamPercentage": float,
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef(
    _ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef
):
    pass


_ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef",
    {"InboxRawCount": int, "SpamRawCount": int, "ProjectedInbox": int, "ProjectedSpam": int},
    total=False,
)


class ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef(
    _ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef
):
    pass


_ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef",
    {
        "StartDate": datetime,
        "VolumeStatistics": ClientGetDomainStatisticsReportResponseDailyVolumesVolumeStatisticsTypeDef,
        "DomainIspPlacements": List[
            ClientGetDomainStatisticsReportResponseDailyVolumesDomainIspPlacementsTypeDef
        ],
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef(
    _ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef
):
    pass


_ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef",
    {
        "IspName": str,
        "InboxRawCount": int,
        "SpamRawCount": int,
        "InboxPercentage": float,
        "SpamPercentage": float,
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef(
    _ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef
):
    pass


_ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef",
    {"InboxRawCount": int, "SpamRawCount": int, "ProjectedInbox": int, "ProjectedSpam": int},
    total=False,
)


class ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef(
    _ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef
):
    """
    - **VolumeStatistics** *(dict) --*

      An object that contains information about the numbers of messages that arrived in recipients'
      inboxes and junk mail folders.
      - **InboxRawCount** *(integer) --*

        The total number of emails that arrived in recipients' inboxes.
    """


_ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef",
    {
        "VolumeStatistics": ClientGetDomainStatisticsReportResponseOverallVolumeVolumeStatisticsTypeDef,
        "ReadRatePercent": float,
        "DomainIspPlacements": List[
            ClientGetDomainStatisticsReportResponseOverallVolumeDomainIspPlacementsTypeDef
        ],
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef(
    _ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef
):
    """
    - **OverallVolume** *(dict) --*

      An object that contains deliverability metrics for the domain that you specified. The data in
      this object is a summary of all of the data that was collected from the ``StartDate`` to the
      ``EndDate`` .
      - **VolumeStatistics** *(dict) --*

        An object that contains information about the numbers of messages that arrived in
        recipients' inboxes and junk mail folders.
        - **InboxRawCount** *(integer) --*

          The total number of emails that arrived in recipients' inboxes.
    """


_ClientGetDomainStatisticsReportResponseTypeDef = TypedDict(
    "_ClientGetDomainStatisticsReportResponseTypeDef",
    {
        "OverallVolume": ClientGetDomainStatisticsReportResponseOverallVolumeTypeDef,
        "DailyVolumes": List[ClientGetDomainStatisticsReportResponseDailyVolumesTypeDef],
    },
    total=False,
)


class ClientGetDomainStatisticsReportResponseTypeDef(
    _ClientGetDomainStatisticsReportResponseTypeDef
):
    """
    - *(dict) --*

      An object that includes statistics that are related to the domain that you specified.
      - **OverallVolume** *(dict) --*

        An object that contains deliverability metrics for the domain that you specified. The data
        in this object is a summary of all of the data that was collected from the ``StartDate`` to
        the ``EndDate`` .
        - **VolumeStatistics** *(dict) --*

          An object that contains information about the numbers of messages that arrived in
          recipients' inboxes and junk mail folders.
          - **InboxRawCount** *(integer) --*

            The total number of emails that arrived in recipients' inboxes.
    """


_ClientGetEmailIdentityResponseDkimAttributesTypeDef = TypedDict(
    "_ClientGetEmailIdentityResponseDkimAttributesTypeDef",
    {
        "SigningEnabled": bool,
        "Status": Literal["PENDING", "SUCCESS", "FAILED", "TEMPORARY_FAILURE", "NOT_STARTED"],
        "Tokens": List[str],
    },
    total=False,
)


class ClientGetEmailIdentityResponseDkimAttributesTypeDef(
    _ClientGetEmailIdentityResponseDkimAttributesTypeDef
):
    pass


_ClientGetEmailIdentityResponseMailFromAttributesTypeDef = TypedDict(
    "_ClientGetEmailIdentityResponseMailFromAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": Literal["PENDING", "SUCCESS", "FAILED", "TEMPORARY_FAILURE"],
        "BehaviorOnMxFailure": Literal["USE_DEFAULT_VALUE", "REJECT_MESSAGE"],
    },
    total=False,
)


class ClientGetEmailIdentityResponseMailFromAttributesTypeDef(
    _ClientGetEmailIdentityResponseMailFromAttributesTypeDef
):
    pass


_ClientGetEmailIdentityResponseTagsTypeDef = TypedDict(
    "_ClientGetEmailIdentityResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetEmailIdentityResponseTagsTypeDef(_ClientGetEmailIdentityResponseTagsTypeDef):
    pass


_ClientGetEmailIdentityResponseTypeDef = TypedDict(
    "_ClientGetEmailIdentityResponseTypeDef",
    {
        "IdentityType": Literal["EMAIL_ADDRESS", "DOMAIN", "MANAGED_DOMAIN"],
        "FeedbackForwardingStatus": bool,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": ClientGetEmailIdentityResponseDkimAttributesTypeDef,
        "MailFromAttributes": ClientGetEmailIdentityResponseMailFromAttributesTypeDef,
        "Tags": List[ClientGetEmailIdentityResponseTagsTypeDef],
    },
    total=False,
)


class ClientGetEmailIdentityResponseTypeDef(_ClientGetEmailIdentityResponseTypeDef):
    """
    - *(dict) --*

      Details about an email identity.
      - **IdentityType** *(string) --*

        The email identity type.
    """


_ClientListConfigurationSetsResponseTypeDef = TypedDict(
    "_ClientListConfigurationSetsResponseTypeDef",
    {"ConfigurationSets": List[str], "NextToken": str},
    total=False,
)


class ClientListConfigurationSetsResponseTypeDef(_ClientListConfigurationSetsResponseTypeDef):
    """
    - *(dict) --*

      A list of configuration sets in your Amazon Pinpoint account in the current AWS Region.
      - **ConfigurationSets** *(list) --*

        An array that contains all of the configuration sets in your Amazon Pinpoint account in the
        current AWS Region.
        - *(string) --*

          The name of a configuration set.
          In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the
          emails you send. You apply a configuration set to an email by including a reference to the
          configuration set in the headers of the email. When you apply a configuration set to an
          email, all of the rules in that configuration set are applied to the email.
    """


_ClientListDedicatedIpPoolsResponseTypeDef = TypedDict(
    "_ClientListDedicatedIpPoolsResponseTypeDef",
    {"DedicatedIpPools": List[str], "NextToken": str},
    total=False,
)


class ClientListDedicatedIpPoolsResponseTypeDef(_ClientListDedicatedIpPoolsResponseTypeDef):
    """
    - *(dict) --*

      A list of dedicated IP pools.
      - **DedicatedIpPools** *(list) --*

        A list of all of the dedicated IP pools that are associated with your Amazon Pinpoint
        account.
        - *(string) --*

          The name of a dedicated IP pool.
    """


_ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef = TypedDict(
    "_ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": Literal["IN_PROGRESS", "COMPLETED"],
    },
    total=False,
)


class ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef(
    _ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef
):
    """
    - *(dict) --*

      An object that contains metadata related to a predictive inbox placement test.
      - **ReportId** *(string) --*

        A unique string that identifies the predictive inbox placement test.
    """


_ClientListDeliverabilityTestReportsResponseTypeDef = TypedDict(
    "_ClientListDeliverabilityTestReportsResponseTypeDef",
    {
        "DeliverabilityTestReports": List[
            ClientListDeliverabilityTestReportsResponseDeliverabilityTestReportsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListDeliverabilityTestReportsResponseTypeDef(
    _ClientListDeliverabilityTestReportsResponseTypeDef
):
    """
    - *(dict) --*

      A list of the predictive inbox placement test reports that are available for your account,
      regardless of whether or not those tests are complete.
      - **DeliverabilityTestReports** *(list) --*

        An object that contains a lists of predictive inbox placement tests that you've performed.
        - *(dict) --*

          An object that contains metadata related to a predictive inbox placement test.
          - **ReportId** *(string) --*

            A unique string that identifies the predictive inbox placement test.
    """


_ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef = TypedDict(
    "_ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef",
    {
        "CampaignId": str,
        "ImageUrl": str,
        "Subject": str,
        "FromAddress": str,
        "SendingIps": List[str],
        "FirstSeenDateTime": datetime,
        "LastSeenDateTime": datetime,
        "InboxCount": int,
        "SpamCount": int,
        "ReadRate": float,
        "DeleteRate": float,
        "ReadDeleteRate": float,
        "ProjectedVolume": int,
        "Esps": List[str],
    },
    total=False,
)


class ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef(
    _ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef
):
    """
    - *(dict) --*

      An object that contains the deliverability data for a specific campaign. This data is
      available for a campaign only if the campaign sent email by using a domain that the
      Deliverability dashboard is enabled for (``PutDeliverabilityDashboardOption`` operation).
      - **CampaignId** *(string) --*

        The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns
        this identifier to a campaign. This value is not the same as the campaign identifier that
        Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon Pinpoint
        API or the Amazon Pinpoint console.
    """


_ClientListDomainDeliverabilityCampaignsResponseTypeDef = TypedDict(
    "_ClientListDomainDeliverabilityCampaignsResponseTypeDef",
    {
        "DomainDeliverabilityCampaigns": List[
            ClientListDomainDeliverabilityCampaignsResponseDomainDeliverabilityCampaignsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListDomainDeliverabilityCampaignsResponseTypeDef(
    _ClientListDomainDeliverabilityCampaignsResponseTypeDef
):
    """
    - *(dict) --*

      An array of objects that provide deliverability data for all the campaigns that used a
      specific domain to send email during a specified time range. This data is available for a
      domain only if you enabled the Deliverability dashboard (``PutDeliverabilityDashboardOption``
      operation) for the domain.
      - **DomainDeliverabilityCampaigns** *(list) --*

        An array of responses, one for each campaign that used the domain to send email during the
        specified time range.
        - *(dict) --*

          An object that contains the deliverability data for a specific campaign. This data is
          available for a campaign only if the campaign sent email by using a domain that the
          Deliverability dashboard is enabled for (``PutDeliverabilityDashboardOption`` operation).
          - **CampaignId** *(string) --*

            The unique identifier for the campaign. Amazon Pinpoint automatically generates and
            assigns this identifier to a campaign. This value is not the same as the campaign
            identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using
            the Amazon Pinpoint API or the Amazon Pinpoint console.
    """


_ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef = TypedDict(
    "_ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef",
    {
        "IdentityType": Literal["EMAIL_ADDRESS", "DOMAIN", "MANAGED_DOMAIN"],
        "IdentityName": str,
        "SendingEnabled": bool,
    },
    total=False,
)


class ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef(
    _ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef
):
    """
    - *(dict) --*

      Information about an email identity.
      - **IdentityType** *(string) --*

        The email identity type. The identity type can be one of the following:
        * ``EMAIL_ADDRESS`` – The identity is an email address.
        * ``DOMAIN`` – The identity is a domain.
        * ``MANAGED_DOMAIN`` – The identity is a domain that is managed by AWS.
    """


_ClientListEmailIdentitiesResponseTypeDef = TypedDict(
    "_ClientListEmailIdentitiesResponseTypeDef",
    {
        "EmailIdentities": List[ClientListEmailIdentitiesResponseEmailIdentitiesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListEmailIdentitiesResponseTypeDef(_ClientListEmailIdentitiesResponseTypeDef):
    """
    - *(dict) --*

      A list of all of the identities that you've attempted to verify for use with Amazon Pinpoint,
      regardless of whether or not those identities were successfully verified.
      - **EmailIdentities** *(list) --*

        An array that includes all of the identities associated with your Amazon Pinpoint account.
        - *(dict) --*

          Information about an email identity.
          - **IdentityType** *(string) --*

            The email identity type. The identity type can be one of the following:
            * ``EMAIL_ADDRESS`` – The identity is an email address.
            * ``DOMAIN`` – The identity is a domain.
            * ``MANAGED_DOMAIN`` – The identity is a domain that is managed by AWS.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsForResourceResponseTagsTypeDef(_ClientListTagsForResourceResponseTagsTypeDef):
    """
    - *(dict) --*

      An object that defines the tags that are associated with a resource. A *tag* is a label that
      you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
      categorize and manage resources in different ways, such as by purpose, owner, environment, or
      other criteria. A resource can have as many as 50 tags.
      Each tag consists of a required *tag key* and an associated *tag value* , both of which you
      define. A tag key is a general label that acts as a category for a more specific tag value. A
      tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
      characters. A tag value can contain as many as 256 characters. The characters can be Unicode
      letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
      additional restrictions apply to tags:
      * Tag keys and values are case sensitive.
      * For each associated resource, each tag key must be unique and it can have only one value.
      * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
      that you define. In addition, you can't edit or remove tag keys or values that use this
      prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
      * You can associate tags with public or shared resources, but the tags are available only for
      your AWS account, not any other accounts that share the resource. In addition, the tags are
      available only for resources that are located in the specified AWS Region for your AWS
      account.
      - **Key** *(string) --*

        One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
        characters. The minimum length is 1 character.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **Tags** *(list) --*

        An array that lists all the tags that are associated with the resource. Each tag consists of
        a required tag key (``Key`` ) and an associated tag value (``Value`` )
        - *(dict) --*

          An object that defines the tags that are associated with a resource. A *tag* is a label
          that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help
          you categorize and manage resources in different ways, such as by purpose, owner,
          environment, or other criteria. A resource can have as many as 50 tags.
          Each tag consists of a required *tag key* and an associated *tag value* , both of which
          you define. A tag key is a general label that acts as a category for a more specific tag
          value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as
          128 characters. A tag value can contain as many as 256 characters. The characters can be
          Unicode letters, digits, white space, or one of the following symbols: _ . : / =
               + -. The
          following additional restrictions apply to tags:
          * Tag keys and values are case sensitive.
          * For each associated resource, each tag key must be unique and it can have only one
          value.
          * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or
          values that you define. In addition, you can't edit or remove tag keys or values that use
          this prefix. Tags that use this prefix don’t count against the limit of 50 tags per
          resource.
          * You can associate tags with public or shared resources, but the tags are available only
          for your AWS account, not any other accounts that share the resource. In addition, the
          tags are available only for resources that are located in the specified AWS Region for
          your AWS account.
          - **Key** *(string) --*

            One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
            characters. The minimum length is 1 character.
    """


_ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef = TypedDict(
    "_ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef",
    {"Global": bool, "TrackedIsps": List[str]},
    total=False,
)


class ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef(
    _ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef
):
    pass


_ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef = TypedDict(
    "_ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": ClientPutDeliverabilityDashboardOptionSubscribedDomainsInboxPlacementTrackingOptionTypeDef,
    },
    total=False,
)


class ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef(
    _ClientPutDeliverabilityDashboardOptionSubscribedDomainsTypeDef
):
    """
    - *(dict) --*

      An object that contains information about the Deliverability dashboard subscription for a
      verified domain that you use to send email and currently has an active Deliverability
      dashboard subscription. If a Deliverability dashboard subscription is active for a domain, you
      gain access to reputation, inbox placement, and other metrics for the domain.
      - **Domain** *(string) --*

        A verified domain that’s associated with your AWS account and currently has an active
        Deliverability dashboard subscription.
    """


_ClientSendEmailContentRawTypeDef = TypedDict(
    "_ClientSendEmailContentRawTypeDef", {"Data": bytes}, total=False
)


class ClientSendEmailContentRawTypeDef(_ClientSendEmailContentRawTypeDef):
    pass


_ClientSendEmailContentSimpleBodyHtmlTypeDef = TypedDict(
    "_ClientSendEmailContentSimpleBodyHtmlTypeDef", {"Data": str, "Charset": str}, total=False
)


class ClientSendEmailContentSimpleBodyHtmlTypeDef(_ClientSendEmailContentSimpleBodyHtmlTypeDef):
    pass


_ClientSendEmailContentSimpleBodyTextTypeDef = TypedDict(
    "_ClientSendEmailContentSimpleBodyTextTypeDef", {"Data": str, "Charset": str}, total=False
)


class ClientSendEmailContentSimpleBodyTextTypeDef(_ClientSendEmailContentSimpleBodyTextTypeDef):
    pass


_ClientSendEmailContentSimpleBodyTypeDef = TypedDict(
    "_ClientSendEmailContentSimpleBodyTypeDef",
    {
        "Text": ClientSendEmailContentSimpleBodyTextTypeDef,
        "Html": ClientSendEmailContentSimpleBodyHtmlTypeDef,
    },
    total=False,
)


class ClientSendEmailContentSimpleBodyTypeDef(_ClientSendEmailContentSimpleBodyTypeDef):
    pass


_RequiredClientSendEmailContentSimpleSubjectTypeDef = TypedDict(
    "_RequiredClientSendEmailContentSimpleSubjectTypeDef", {"Data": str}
)
_OptionalClientSendEmailContentSimpleSubjectTypeDef = TypedDict(
    "_OptionalClientSendEmailContentSimpleSubjectTypeDef", {"Charset": str}, total=False
)


class ClientSendEmailContentSimpleSubjectTypeDef(
    _RequiredClientSendEmailContentSimpleSubjectTypeDef,
    _OptionalClientSendEmailContentSimpleSubjectTypeDef,
):
    """
    - **Subject** *(dict) --***[REQUIRED]**

      The subject line of the email. The subject line can only contain 7-bit ASCII characters.
      However, you can specify non-ASCII characters in the subject line by using encoded-word
      syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .
      - **Data** *(string) --***[REQUIRED]**

        The content of the message itself.
    """


_RequiredClientSendEmailContentSimpleTypeDef = TypedDict(
    "_RequiredClientSendEmailContentSimpleTypeDef",
    {"Subject": ClientSendEmailContentSimpleSubjectTypeDef},
)
_OptionalClientSendEmailContentSimpleTypeDef = TypedDict(
    "_OptionalClientSendEmailContentSimpleTypeDef",
    {"Body": ClientSendEmailContentSimpleBodyTypeDef},
    total=False,
)


class ClientSendEmailContentSimpleTypeDef(
    _RequiredClientSendEmailContentSimpleTypeDef, _OptionalClientSendEmailContentSimpleTypeDef
):
    """
    - **Simple** *(dict) --*

      The simple email message. The message consists of a subject and a message body.
      - **Subject** *(dict) --***[REQUIRED]**

        The subject line of the email. The subject line can only contain 7-bit ASCII characters.
        However, you can specify non-ASCII characters in the subject line by using encoded-word
        syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .
        - **Data** *(string) --***[REQUIRED]**

          The content of the message itself.
    """


_ClientSendEmailContentTemplateTypeDef = TypedDict(
    "_ClientSendEmailContentTemplateTypeDef", {"TemplateArn": str, "TemplateData": str}, total=False
)


class ClientSendEmailContentTemplateTypeDef(_ClientSendEmailContentTemplateTypeDef):
    pass


_ClientSendEmailContentTypeDef = TypedDict(
    "_ClientSendEmailContentTypeDef",
    {
        "Simple": ClientSendEmailContentSimpleTypeDef,
        "Raw": ClientSendEmailContentRawTypeDef,
        "Template": ClientSendEmailContentTemplateTypeDef,
    },
    total=False,
)


class ClientSendEmailContentTypeDef(_ClientSendEmailContentTypeDef):
    """
    An object that contains the body of the message. You can send either a Simple message or a Raw
    message.
    - **Simple** *(dict) --*

      The simple email message. The message consists of a subject and a message body.
      - **Subject** *(dict) --***[REQUIRED]**

        The subject line of the email. The subject line can only contain 7-bit ASCII characters.
        However, you can specify non-ASCII characters in the subject line by using encoded-word
        syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ .
        - **Data** *(string) --***[REQUIRED]**

          The content of the message itself.
    """


_ClientSendEmailDestinationTypeDef = TypedDict(
    "_ClientSendEmailDestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)


class ClientSendEmailDestinationTypeDef(_ClientSendEmailDestinationTypeDef):
    """
    An object that contains the recipients of the email message.
    - **ToAddresses** *(list) --*

      An array that contains the email addresses of the "To" recipients for the email.
      - *(string) --*
    """


_RequiredClientSendEmailEmailTagsTypeDef = TypedDict(
    "_RequiredClientSendEmailEmailTagsTypeDef", {"Name": str}
)
_OptionalClientSendEmailEmailTagsTypeDef = TypedDict(
    "_OptionalClientSendEmailEmailTagsTypeDef", {"Value": str}, total=False
)


class ClientSendEmailEmailTagsTypeDef(
    _RequiredClientSendEmailEmailTagsTypeDef, _OptionalClientSendEmailEmailTagsTypeDef
):
    """
    - *(dict) --*

      Contains the name and value of a tag that you apply to an email. You can use message tags when
      you publish email sending events.
      - **Name** *(string) --***[REQUIRED]**

        The name of the message tag. The message tag name has to meet the following criteria:
        * It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes
        (-).
        * It can contain no more than 256 characters.
    """


_ClientSendEmailResponseTypeDef = TypedDict(
    "_ClientSendEmailResponseTypeDef", {"MessageId": str}, total=False
)


class ClientSendEmailResponseTypeDef(_ClientSendEmailResponseTypeDef):
    """
    - *(dict) --*

      A unique message ID that you receive when Amazon Pinpoint accepts an email for sending.
      - **MessageId** *(string) --*

        A unique identifier for the message that is generated when Amazon Pinpoint accepts the
        message.
        .. note::

          It is possible for Amazon Pinpoint to accept a message without sending it. This can happen
          when the message you're trying to send has an attachment doesn't pass a virus check, or
          when you send a templated email that contains invalid personalization content, for
          example.
    """


_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    """
    - *(dict) --*

      An object that defines the tags that are associated with a resource. A *tag* is a label that
      you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you
      categorize and manage resources in different ways, such as by purpose, owner, environment, or
      other criteria. A resource can have as many as 50 tags.
      Each tag consists of a required *tag key* and an associated *tag value* , both of which you
      define. A tag key is a general label that acts as a category for a more specific tag value. A
      tag value acts as a descriptor within a tag key. A tag key can contain as many as 128
      characters. A tag value can contain as many as 256 characters. The characters can be Unicode
      letters, digits, white space, or one of the following symbols: _ . : / = + -. The following
      additional restrictions apply to tags:
      * Tag keys and values are case sensitive.
      * For each associated resource, each tag key must be unique and it can have only one value.
      * The ``aws:`` prefix is reserved for use by AWS; you can’t use it in any tag keys or values
      that you define. In addition, you can't edit or remove tag keys or values that use this
      prefix. Tags that use this prefix don’t count against the limit of 50 tags per resource.
      * You can associate tags with public or shared resources, but the tags are available only for
      your AWS account, not any other accounts that share the resource. In addition, the tags are
      available only for resources that are located in the specified AWS Region for your AWS
      account.
      - **Key** *(string) --***[REQUIRED]**

        One part of a key-value pair that defines a tag. The maximum length of a tag key is 128
        characters. The minimum length is 1 character.
    """


_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationDimensionConfigurationsTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["MESSAGE_TAG", "EMAIL_HEADER", "LINK_TAG"],
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
    {"IamRoleArn": str, "DeliveryStreamArn": str},
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef
):
    pass


_ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef",
    {"ApplicationArn": str},
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef
):
    pass


_ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef",
    {"TopicArn": str},
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef
):
    pass


_ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef = TypedDict(
    "_ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "SEND",
                "REJECT",
                "BOUNCE",
                "COMPLAINT",
                "DELIVERY",
                "OPEN",
                "CLICK",
                "RENDERING_FAILURE",
            ]
        ],
        "KinesisFirehoseDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationKinesisFirehoseDestinationTypeDef,
        "CloudWatchDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationCloudWatchDestinationTypeDef,
        "SnsDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationSnsDestinationTypeDef,
        "PinpointDestination": ClientUpdateConfigurationSetEventDestinationEventDestinationPinpointDestinationTypeDef,
    },
    total=False,
)


class ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef(
    _ClientUpdateConfigurationSetEventDestinationEventDestinationTypeDef
):
    """
    An object that defines the event destination.
    - **Enabled** *(boolean) --*

      If ``true`` , the event destination is enabled. When the event destination is enabled, the
      specified event types are sent to the destinations in this ``EventDestinationDefinition`` .
      If ``false`` , the event destination is disabled. When the event destination is disabled,
      events aren't sent to the specified destinations.
    """


_GetDedicatedIpsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetDedicatedIpsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetDedicatedIpsPaginatePaginationConfigTypeDef(
    _GetDedicatedIpsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef = TypedDict(
    "_GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef",
    {
        "Ip": str,
        "WarmupStatus": Literal["IN_PROGRESS", "DONE"],
        "WarmupPercentage": int,
        "PoolName": str,
    },
    total=False,
)


class GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef(
    _GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef
):
    """
    - *(dict) --*

      Contains information about a dedicated IP address that is associated with your Amazon Pinpoint
      account.
      - **Ip** *(string) --*

        An IP address that is reserved for use by your Amazon Pinpoint account.
    """


_GetDedicatedIpsPaginateResponseTypeDef = TypedDict(
    "_GetDedicatedIpsPaginateResponseTypeDef",
    {"DedicatedIps": List[GetDedicatedIpsPaginateResponseDedicatedIpsTypeDef]},
    total=False,
)


class GetDedicatedIpsPaginateResponseTypeDef(_GetDedicatedIpsPaginateResponseTypeDef):
    """
    - *(dict) --*

      Information about the dedicated IP addresses that are associated with your Amazon Pinpoint
      account.
      - **DedicatedIps** *(list) --*

        A list of dedicated IP addresses that are reserved for use by your Amazon Pinpoint account.
        - *(dict) --*

          Contains information about a dedicated IP address that is associated with your Amazon
          Pinpoint account.
          - **Ip** *(string) --*

            An IP address that is reserved for use by your Amazon Pinpoint account.
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


_ListConfigurationSetsPaginateResponseTypeDef = TypedDict(
    "_ListConfigurationSetsPaginateResponseTypeDef", {"ConfigurationSets": List[str]}, total=False
)


class ListConfigurationSetsPaginateResponseTypeDef(_ListConfigurationSetsPaginateResponseTypeDef):
    """
    - *(dict) --*

      A list of configuration sets in your Amazon Pinpoint account in the current AWS Region.
      - **ConfigurationSets** *(list) --*

        An array that contains all of the configuration sets in your Amazon Pinpoint account in the
        current AWS Region.
        - *(string) --*

          The name of a configuration set.
          In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the
          emails you send. You apply a configuration set to an email by including a reference to the
          configuration set in the headers of the email. When you apply a configuration set to an
          email, all of the rules in that configuration set are applied to the email.
    """


_ListDedicatedIpPoolsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDedicatedIpPoolsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDedicatedIpPoolsPaginatePaginationConfigTypeDef(
    _ListDedicatedIpPoolsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDedicatedIpPoolsPaginateResponseTypeDef = TypedDict(
    "_ListDedicatedIpPoolsPaginateResponseTypeDef", {"DedicatedIpPools": List[str]}, total=False
)


class ListDedicatedIpPoolsPaginateResponseTypeDef(_ListDedicatedIpPoolsPaginateResponseTypeDef):
    """
    - *(dict) --*

      A list of dedicated IP pools.
      - **DedicatedIpPools** *(list) --*

        A list of all of the dedicated IP pools that are associated with your Amazon Pinpoint
        account.
        - *(string) --*

          The name of a dedicated IP pool.
    """


_ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef(
    _ListDeliverabilityTestReportsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef = TypedDict(
    "_ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": Literal["IN_PROGRESS", "COMPLETED"],
    },
    total=False,
)


class ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef(
    _ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef
):
    """
    - *(dict) --*

      An object that contains metadata related to a predictive inbox placement test.
      - **ReportId** *(string) --*

        A unique string that identifies the predictive inbox placement test.
    """


_ListDeliverabilityTestReportsPaginateResponseTypeDef = TypedDict(
    "_ListDeliverabilityTestReportsPaginateResponseTypeDef",
    {
        "DeliverabilityTestReports": List[
            ListDeliverabilityTestReportsPaginateResponseDeliverabilityTestReportsTypeDef
        ]
    },
    total=False,
)


class ListDeliverabilityTestReportsPaginateResponseTypeDef(
    _ListDeliverabilityTestReportsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      A list of the predictive inbox placement test reports that are available for your account,
      regardless of whether or not those tests are complete.
      - **DeliverabilityTestReports** *(list) --*

        An object that contains a lists of predictive inbox placement tests that you've performed.
        - *(dict) --*

          An object that contains metadata related to a predictive inbox placement test.
          - **ReportId** *(string) --*

            A unique string that identifies the predictive inbox placement test.
    """


_ListEmailIdentitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEmailIdentitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEmailIdentitiesPaginatePaginationConfigTypeDef(
    _ListEmailIdentitiesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef = TypedDict(
    "_ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef",
    {
        "IdentityType": Literal["EMAIL_ADDRESS", "DOMAIN", "MANAGED_DOMAIN"],
        "IdentityName": str,
        "SendingEnabled": bool,
    },
    total=False,
)


class ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef(
    _ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef
):
    """
    - *(dict) --*

      Information about an email identity.
      - **IdentityType** *(string) --*

        The email identity type. The identity type can be one of the following:
        * ``EMAIL_ADDRESS`` – The identity is an email address.
        * ``DOMAIN`` – The identity is a domain.
        * ``MANAGED_DOMAIN`` – The identity is a domain that is managed by AWS.
    """


_ListEmailIdentitiesPaginateResponseTypeDef = TypedDict(
    "_ListEmailIdentitiesPaginateResponseTypeDef",
    {"EmailIdentities": List[ListEmailIdentitiesPaginateResponseEmailIdentitiesTypeDef]},
    total=False,
)


class ListEmailIdentitiesPaginateResponseTypeDef(_ListEmailIdentitiesPaginateResponseTypeDef):
    """
    - *(dict) --*

      A list of all of the identities that you've attempted to verify for use with Amazon Pinpoint,
      regardless of whether or not those identities were successfully verified.
      - **EmailIdentities** *(list) --*

        An array that includes all of the identities associated with your Amazon Pinpoint account.
        - *(dict) --*

          Information about an email identity.
          - **IdentityType** *(string) --*

            The email identity type. The identity type can be one of the following:
            * ``EMAIL_ADDRESS`` – The identity is an email address.
            * ``DOMAIN`` – The identity is a domain.
            * ``MANAGED_DOMAIN`` – The identity is a domain that is managed by AWS.
    """
