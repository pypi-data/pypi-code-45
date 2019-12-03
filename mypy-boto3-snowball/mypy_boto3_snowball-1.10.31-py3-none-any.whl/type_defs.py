"Main interface for snowball service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateAddressAddressTypeDef",
    "ClientCreateAddressResponseTypeDef",
    "ClientCreateClusterNotificationTypeDef",
    "ClientCreateClusterResourcesEc2AmiResourcesTypeDef",
    "ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientCreateClusterResourcesLambdaResourcesTypeDef",
    "ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef",
    "ClientCreateClusterResourcesS3ResourcesTypeDef",
    "ClientCreateClusterResourcesTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateJobNotificationTypeDef",
    "ClientCreateJobResourcesEc2AmiResourcesTypeDef",
    "ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientCreateJobResourcesLambdaResourcesTypeDef",
    "ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef",
    "ClientCreateJobResourcesS3ResourcesTypeDef",
    "ClientCreateJobResourcesTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientDescribeAddressResponseAddressTypeDef",
    "ClientDescribeAddressResponseTypeDef",
    "ClientDescribeAddressesResponseAddressesTypeDef",
    "ClientDescribeAddressesResponseTypeDef",
    "ClientDescribeClusterResponseClusterMetadataNotificationTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataResourcesTypeDef",
    "ClientDescribeClusterResponseClusterMetadataTypeDef",
    "ClientDescribeClusterResponseTypeDef",
    "ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef",
    "ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef",
    "ClientDescribeJobResponseJobMetadataNotificationTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataResourcesTypeDef",
    "ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef",
    "ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef",
    "ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef",
    "ClientDescribeJobResponseJobMetadataTypeDef",
    "ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef",
    "ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef",
    "ClientDescribeJobResponseSubJobMetadataNotificationTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataResourcesTypeDef",
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef",
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef",
    "ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef",
    "ClientDescribeJobResponseSubJobMetadataTypeDef",
    "ClientDescribeJobResponseTypeDef",
    "ClientGetJobManifestResponseTypeDef",
    "ClientGetJobUnlockCodeResponseTypeDef",
    "ClientGetSnowballUsageResponseTypeDef",
    "ClientGetSoftwareUpdatesResponseTypeDef",
    "ClientListClusterJobsResponseJobListEntriesTypeDef",
    "ClientListClusterJobsResponseTypeDef",
    "ClientListClustersResponseClusterListEntriesTypeDef",
    "ClientListClustersResponseTypeDef",
    "ClientListCompatibleImagesResponseCompatibleImagesTypeDef",
    "ClientListCompatibleImagesResponseTypeDef",
    "ClientListJobsResponseJobListEntriesTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientUpdateClusterNotificationTypeDef",
    "ClientUpdateClusterResourcesEc2AmiResourcesTypeDef",
    "ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientUpdateClusterResourcesLambdaResourcesTypeDef",
    "ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef",
    "ClientUpdateClusterResourcesS3ResourcesTypeDef",
    "ClientUpdateClusterResourcesTypeDef",
    "ClientUpdateJobNotificationTypeDef",
    "ClientUpdateJobResourcesEc2AmiResourcesTypeDef",
    "ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef",
    "ClientUpdateJobResourcesLambdaResourcesTypeDef",
    "ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef",
    "ClientUpdateJobResourcesS3ResourcesTypeDef",
    "ClientUpdateJobResourcesTypeDef",
    "DescribeAddressesPaginatePaginationConfigTypeDef",
    "DescribeAddressesPaginateResponseAddressesTypeDef",
    "DescribeAddressesPaginateResponseTypeDef",
    "ListClusterJobsPaginatePaginationConfigTypeDef",
    "ListClusterJobsPaginateResponseJobListEntriesTypeDef",
    "ListClusterJobsPaginateResponseTypeDef",
    "ListClustersPaginatePaginationConfigTypeDef",
    "ListClustersPaginateResponseClusterListEntriesTypeDef",
    "ListClustersPaginateResponseTypeDef",
    "ListCompatibleImagesPaginatePaginationConfigTypeDef",
    "ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef",
    "ListCompatibleImagesPaginateResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponseJobListEntriesTypeDef",
    "ListJobsPaginateResponseTypeDef",
)


_ClientCreateAddressAddressTypeDef = TypedDict(
    "_ClientCreateAddressAddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)


class ClientCreateAddressAddressTypeDef(_ClientCreateAddressAddressTypeDef):
    """
    The address that you want the Snowball shipped to.
    - **AddressId** *(string) --*

      The unique ID for an address.
    """


_ClientCreateAddressResponseTypeDef = TypedDict(
    "_ClientCreateAddressResponseTypeDef", {"AddressId": str}, total=False
)


class ClientCreateAddressResponseTypeDef(_ClientCreateAddressResponseTypeDef):
    """
    - *(dict) --*

      - **AddressId** *(string) --*

        The automatically generated ID for a specific address. You'll use this ID when you create a
        job to specify which address you want the Snowball for that job shipped to.
    """


_ClientCreateClusterNotificationTypeDef = TypedDict(
    "_ClientCreateClusterNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)


class ClientCreateClusterNotificationTypeDef(_ClientCreateClusterNotificationTypeDef):
    """
    The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.
    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
      Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
      You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console,
      or by using the `Subscribe <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__
      AWS Simple Notification Service (SNS) API action.
    """


_ClientCreateClusterResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_ClientCreateClusterResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)


class ClientCreateClusterResourcesEc2AmiResourcesTypeDef(
    _ClientCreateClusterResourcesEc2AmiResourcesTypeDef
):
    pass


_ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef
):
    pass


_ClientCreateClusterResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientCreateClusterResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[ClientCreateClusterResourcesLambdaResourcesEventTriggersTypeDef],
    },
    total=False,
)


class ClientCreateClusterResourcesLambdaResourcesTypeDef(
    _ClientCreateClusterResourcesLambdaResourcesTypeDef
):
    pass


_ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef(
    _ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef
):
    pass


_ClientCreateClusterResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientCreateClusterResourcesS3ResourcesTypeDef",
    {"BucketArn": str, "KeyRange": ClientCreateClusterResourcesS3ResourcesKeyRangeTypeDef},
    total=False,
)


class ClientCreateClusterResourcesS3ResourcesTypeDef(
    _ClientCreateClusterResourcesS3ResourcesTypeDef
):
    """
    - *(dict) --*

      Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
      exported from or imported into. For export jobs, this object can have an optional ``KeyRange``
      value. The length of the range is defined at job creation, and has either an inclusive
      ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
      - **BucketArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon S3 bucket.
    """


_ClientCreateClusterResourcesTypeDef = TypedDict(
    "_ClientCreateClusterResourcesTypeDef",
    {
        "S3Resources": List[ClientCreateClusterResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientCreateClusterResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientCreateClusterResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)


class ClientCreateClusterResourcesTypeDef(_ClientCreateClusterResourcesTypeDef):
    """
    The resources associated with the cluster job. These resources include Amazon S3 buckets and
    optional AWS Lambda functions written in the Python language.
    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.
      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
        exported from or imported into. For export jobs, this object can have an optional
        ``KeyRange`` value. The length of the range is defined at job creation, and has either an
        inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
        sorted.
        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.
    """


_ClientCreateClusterResponseTypeDef = TypedDict(
    "_ClientCreateClusterResponseTypeDef", {"ClusterId": str}, total=False
)


class ClientCreateClusterResponseTypeDef(_ClientCreateClusterResponseTypeDef):
    """
    - *(dict) --*

      - **ClusterId** *(string) --*

        The automatically generated ID for a cluster.
    """


_ClientCreateJobNotificationTypeDef = TypedDict(
    "_ClientCreateJobNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)


class ClientCreateJobNotificationTypeDef(_ClientCreateJobNotificationTypeDef):
    """
    Defines the Amazon Simple Notification Service (Amazon SNS) notification settings for this job.
    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
      Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
      You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console,
      or by using the `Subscribe <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__
      AWS Simple Notification Service (SNS) API action.
    """


_ClientCreateJobResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_ClientCreateJobResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)


class ClientCreateJobResourcesEc2AmiResourcesTypeDef(
    _ClientCreateJobResourcesEc2AmiResourcesTypeDef
):
    pass


_ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef
):
    pass


_ClientCreateJobResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientCreateJobResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[ClientCreateJobResourcesLambdaResourcesEventTriggersTypeDef],
    },
    total=False,
)


class ClientCreateJobResourcesLambdaResourcesTypeDef(
    _ClientCreateJobResourcesLambdaResourcesTypeDef
):
    pass


_ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef(
    _ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef
):
    pass


_ClientCreateJobResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientCreateJobResourcesS3ResourcesTypeDef",
    {"BucketArn": str, "KeyRange": ClientCreateJobResourcesS3ResourcesKeyRangeTypeDef},
    total=False,
)


class ClientCreateJobResourcesS3ResourcesTypeDef(_ClientCreateJobResourcesS3ResourcesTypeDef):
    """
    - *(dict) --*

      Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
      exported from or imported into. For export jobs, this object can have an optional ``KeyRange``
      value. The length of the range is defined at job creation, and has either an inclusive
      ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
      - **BucketArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon S3 bucket.
    """


_ClientCreateJobResourcesTypeDef = TypedDict(
    "_ClientCreateJobResourcesTypeDef",
    {
        "S3Resources": List[ClientCreateJobResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientCreateJobResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientCreateJobResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)


class ClientCreateJobResourcesTypeDef(_ClientCreateJobResourcesTypeDef):
    """
    Defines the Amazon S3 buckets associated with this job.
    With ``IMPORT`` jobs, you specify the bucket or buckets that your transferred data will be
    imported into.
    With ``EXPORT`` jobs, you specify the bucket or buckets that your transferred data will be
    exported from. Optionally, you can also specify a ``KeyRange`` value. If you choose to export a
    range, you define the length of the range by providing either an inclusive ``BeginMarker``
    value, an inclusive ``EndMarker`` value, or both. Ranges are UTF-8 binary sorted.
    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.
      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
        exported from or imported into. For export jobs, this object can have an optional
        ``KeyRange`` value. The length of the range is defined at job creation, and has either an
        inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
        sorted.
        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.
    """


_ClientCreateJobResponseTypeDef = TypedDict(
    "_ClientCreateJobResponseTypeDef", {"JobId": str}, total=False
)


class ClientCreateJobResponseTypeDef(_ClientCreateJobResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The automatically generated ID for a job, for example
        ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ClientDescribeAddressResponseAddressTypeDef = TypedDict(
    "_ClientDescribeAddressResponseAddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)


class ClientDescribeAddressResponseAddressTypeDef(_ClientDescribeAddressResponseAddressTypeDef):
    """
    - **Address** *(dict) --*

      The address that you want the Snowball or Snowballs associated with a specific job to be
      shipped to.
      - **AddressId** *(string) --*

        The unique ID for an address.
    """


_ClientDescribeAddressResponseTypeDef = TypedDict(
    "_ClientDescribeAddressResponseTypeDef",
    {"Address": ClientDescribeAddressResponseAddressTypeDef},
    total=False,
)


class ClientDescribeAddressResponseTypeDef(_ClientDescribeAddressResponseTypeDef):
    """
    - *(dict) --*

      - **Address** *(dict) --*

        The address that you want the Snowball or Snowballs associated with a specific job to be
        shipped to.
        - **AddressId** *(string) --*

          The unique ID for an address.
    """


_ClientDescribeAddressesResponseAddressesTypeDef = TypedDict(
    "_ClientDescribeAddressesResponseAddressesTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)


class ClientDescribeAddressesResponseAddressesTypeDef(
    _ClientDescribeAddressesResponseAddressesTypeDef
):
    """
    - *(dict) --*

      The address that you want the Snowball or Snowballs associated with a specific job to be
      shipped to. Addresses are validated at the time of creation. The address you provide must be
      located within the serviceable area of your region. Although no individual elements of the
      ``Address`` are required, if the address is invalid or unsupported, then an exception is
      thrown.
      - **AddressId** *(string) --*

        The unique ID for an address.
    """


_ClientDescribeAddressesResponseTypeDef = TypedDict(
    "_ClientDescribeAddressesResponseTypeDef",
    {"Addresses": List[ClientDescribeAddressesResponseAddressesTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeAddressesResponseTypeDef(_ClientDescribeAddressesResponseTypeDef):
    """
    - *(dict) --*

      - **Addresses** *(list) --*

        The Snowball shipping addresses that were created for this account.
        - *(dict) --*

          The address that you want the Snowball or Snowballs associated with a specific job to be
          shipped to. Addresses are validated at the time of creation. The address you provide must
          be located within the serviceable area of your region. Although no individual elements of
          the ``Address`` are required, if the address is invalid or unsupported, then an exception
          is thrown.
          - **AddressId** *(string) --*

            The unique ID for an address.
    """


_ClientDescribeClusterResponseClusterMetadataNotificationTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataNotificationTypeDef(
    _ClientDescribeClusterResponseClusterMetadataNotificationTypeDef
):
    pass


_ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef
):
    pass


_ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef
):
    pass


_ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef
):
    pass


_ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef
):
    pass


_ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef
):
    pass


_ClientDescribeClusterResponseClusterMetadataResourcesTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataResourcesTypeDef",
    {
        "S3Resources": List[
            ClientDescribeClusterResponseClusterMetadataResourcesS3ResourcesTypeDef
        ],
        "LambdaResources": List[
            ClientDescribeClusterResponseClusterMetadataResourcesLambdaResourcesTypeDef
        ],
        "Ec2AmiResources": List[
            ClientDescribeClusterResponseClusterMetadataResourcesEc2AmiResourcesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataResourcesTypeDef(
    _ClientDescribeClusterResponseClusterMetadataResourcesTypeDef
):
    pass


_ClientDescribeClusterResponseClusterMetadataTypeDef = TypedDict(
    "_ClientDescribeClusterResponseClusterMetadataTypeDef",
    {
        "ClusterId": str,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "ClusterState": Literal["AwaitingQuorum", "Pending", "InUse", "Complete", "Cancelled"],
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Resources": ClientDescribeClusterResponseClusterMetadataResourcesTypeDef,
        "AddressId": str,
        "ShippingOption": Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        "Notification": ClientDescribeClusterResponseClusterMetadataNotificationTypeDef,
        "ForwardingAddressId": str,
    },
    total=False,
)


class ClientDescribeClusterResponseClusterMetadataTypeDef(
    _ClientDescribeClusterResponseClusterMetadataTypeDef
):
    """
    - **ClusterMetadata** *(dict) --*

      Information about a specific cluster, including shipping information, cluster status, and
      other important metadata.
      - **ClusterId** *(string) --*

        The automatically generated ID for a cluster.
    """


_ClientDescribeClusterResponseTypeDef = TypedDict(
    "_ClientDescribeClusterResponseTypeDef",
    {"ClusterMetadata": ClientDescribeClusterResponseClusterMetadataTypeDef},
    total=False,
)


class ClientDescribeClusterResponseTypeDef(_ClientDescribeClusterResponseTypeDef):
    """
    - *(dict) --*

      - **ClusterMetadata** *(dict) --*

        Information about a specific cluster, including shipping information, cluster status, and
        other important metadata.
        - **ClusterId** *(string) --*

          The automatically generated ID for a cluster.
    """


_ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef",
    {"BytesTransferred": int, "ObjectsTransferred": int, "TotalBytes": int, "TotalObjects": int},
    total=False,
)


class ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef(
    _ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef",
    {"JobCompletionReportURI": str, "JobSuccessLogURI": str, "JobFailureLogURI": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef(
    _ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataNotificationTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataNotificationTypeDef(
    _ClientDescribeJobResponseJobMetadataNotificationTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientDescribeJobResponseJobMetadataResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataResourcesTypeDef",
    {
        "S3Resources": List[ClientDescribeJobResponseJobMetadataResourcesS3ResourcesTypeDef],
        "LambdaResources": List[
            ClientDescribeJobResponseJobMetadataResourcesLambdaResourcesTypeDef
        ],
        "Ec2AmiResources": List[
            ClientDescribeJobResponseJobMetadataResourcesEc2AmiResourcesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataResourcesTypeDef(
    _ClientDescribeJobResponseJobMetadataResourcesTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef(
    _ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)


class ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef(
    _ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef",
    {
        "ShippingOption": Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        "InboundShipment": ClientDescribeJobResponseJobMetadataShippingDetailsInboundShipmentTypeDef,
        "OutboundShipment": ClientDescribeJobResponseJobMetadataShippingDetailsOutboundShipmentTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef(
    _ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef
):
    pass


_ClientDescribeJobResponseJobMetadataTypeDef = TypedDict(
    "_ClientDescribeJobResponseJobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Resources": ClientDescribeJobResponseJobMetadataResourcesTypeDef,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": ClientDescribeJobResponseJobMetadataShippingDetailsTypeDef,
        "SnowballCapacityPreference": Literal["T50", "T80", "T100", "T42", "NoPreference"],
        "Notification": ClientDescribeJobResponseJobMetadataNotificationTypeDef,
        "DataTransferProgress": ClientDescribeJobResponseJobMetadataDataTransferProgressTypeDef,
        "JobLogInfo": ClientDescribeJobResponseJobMetadataJobLogInfoTypeDef,
        "ClusterId": str,
        "ForwardingAddressId": str,
    },
    total=False,
)


class ClientDescribeJobResponseJobMetadataTypeDef(_ClientDescribeJobResponseJobMetadataTypeDef):
    """
    - **JobMetadata** *(dict) --*

      Information about a specific job, including shipping information, job status, and other
      important metadata.
      - **JobId** *(string) --*

        The automatically generated ID for a job, for example
        ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef",
    {"BytesTransferred": int, "ObjectsTransferred": int, "TotalBytes": int, "TotalObjects": int},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef(
    _ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef",
    {"JobCompletionReportURI": str, "JobSuccessLogURI": str, "JobFailureLogURI": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef(
    _ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataNotificationTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataNotificationTypeDef(
    _ClientDescribeJobResponseSubJobMetadataNotificationTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[
            ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesEventTriggersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef",
    {
        "BucketArn": str,
        "KeyRange": ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesKeyRangeTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataResourcesTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataResourcesTypeDef",
    {
        "S3Resources": List[ClientDescribeJobResponseSubJobMetadataResourcesS3ResourcesTypeDef],
        "LambdaResources": List[
            ClientDescribeJobResponseSubJobMetadataResourcesLambdaResourcesTypeDef
        ],
        "Ec2AmiResources": List[
            ClientDescribeJobResponseSubJobMetadataResourcesEc2AmiResourcesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataResourcesTypeDef(
    _ClientDescribeJobResponseSubJobMetadataResourcesTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef(
    _ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef",
    {"Status": str, "TrackingNumber": str},
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef(
    _ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef",
    {
        "ShippingOption": Literal["SECOND_DAY", "NEXT_DAY", "EXPRESS", "STANDARD"],
        "InboundShipment": ClientDescribeJobResponseSubJobMetadataShippingDetailsInboundShipmentTypeDef,
        "OutboundShipment": ClientDescribeJobResponseSubJobMetadataShippingDetailsOutboundShipmentTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef(
    _ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef
):
    pass


_ClientDescribeJobResponseSubJobMetadataTypeDef = TypedDict(
    "_ClientDescribeJobResponseSubJobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Resources": ClientDescribeJobResponseSubJobMetadataResourcesTypeDef,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": ClientDescribeJobResponseSubJobMetadataShippingDetailsTypeDef,
        "SnowballCapacityPreference": Literal["T50", "T80", "T100", "T42", "NoPreference"],
        "Notification": ClientDescribeJobResponseSubJobMetadataNotificationTypeDef,
        "DataTransferProgress": ClientDescribeJobResponseSubJobMetadataDataTransferProgressTypeDef,
        "JobLogInfo": ClientDescribeJobResponseSubJobMetadataJobLogInfoTypeDef,
        "ClusterId": str,
        "ForwardingAddressId": str,
    },
    total=False,
)


class ClientDescribeJobResponseSubJobMetadataTypeDef(
    _ClientDescribeJobResponseSubJobMetadataTypeDef
):
    pass


_ClientDescribeJobResponseTypeDef = TypedDict(
    "_ClientDescribeJobResponseTypeDef",
    {
        "JobMetadata": ClientDescribeJobResponseJobMetadataTypeDef,
        "SubJobMetadata": List[ClientDescribeJobResponseSubJobMetadataTypeDef],
    },
    total=False,
)


class ClientDescribeJobResponseTypeDef(_ClientDescribeJobResponseTypeDef):
    """
    - *(dict) --*

      - **JobMetadata** *(dict) --*

        Information about a specific job, including shipping information, job status, and other
        important metadata.
        - **JobId** *(string) --*

          The automatically generated ID for a job, for example
          ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ClientGetJobManifestResponseTypeDef = TypedDict(
    "_ClientGetJobManifestResponseTypeDef", {"ManifestURI": str}, total=False
)


class ClientGetJobManifestResponseTypeDef(_ClientGetJobManifestResponseTypeDef):
    """
    - *(dict) --*

      - **ManifestURI** *(string) --*

        The Amazon S3 presigned URL for the manifest file associated with the specified ``JobId``
        value.
    """


_ClientGetJobUnlockCodeResponseTypeDef = TypedDict(
    "_ClientGetJobUnlockCodeResponseTypeDef", {"UnlockCode": str}, total=False
)


class ClientGetJobUnlockCodeResponseTypeDef(_ClientGetJobUnlockCodeResponseTypeDef):
    """
    - *(dict) --*

      - **UnlockCode** *(string) --*

        The ``UnlockCode`` value for the specified job. The ``UnlockCode`` value can be accessed for
        up to 90 days after the job has been created.
    """


_ClientGetSnowballUsageResponseTypeDef = TypedDict(
    "_ClientGetSnowballUsageResponseTypeDef",
    {"SnowballLimit": int, "SnowballsInUse": int},
    total=False,
)


class ClientGetSnowballUsageResponseTypeDef(_ClientGetSnowballUsageResponseTypeDef):
    """
    - *(dict) --*

      - **SnowballLimit** *(integer) --*

        The service limit for number of Snowballs this account can have at once. The default service
        limit is 1 (one).
    """


_ClientGetSoftwareUpdatesResponseTypeDef = TypedDict(
    "_ClientGetSoftwareUpdatesResponseTypeDef", {"UpdatesURI": str}, total=False
)


class ClientGetSoftwareUpdatesResponseTypeDef(_ClientGetSoftwareUpdatesResponseTypeDef):
    """
    - *(dict) --*

      - **UpdatesURI** *(string) --*

        The Amazon S3 presigned URL for the update file associated with the specified ``JobId``
        value. The software update will be available for 2 days after this request is made. To
        access an update after the 2 days have passed, you'll have to make another call to
        ``GetSoftwareUpdates`` .
    """


_ClientListClusterJobsResponseJobListEntriesTypeDef = TypedDict(
    "_ClientListClusterJobsResponseJobListEntriesTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "IsMaster": bool,
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListClusterJobsResponseJobListEntriesTypeDef(
    _ClientListClusterJobsResponseJobListEntriesTypeDef
):
    """
    - *(dict) --*

      Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
      whether the job is a job part, in the case of an export job.
      - **JobId** *(string) --*

        The automatically generated ID for a job, for example
        ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ClientListClusterJobsResponseTypeDef = TypedDict(
    "_ClientListClusterJobsResponseTypeDef",
    {"JobListEntries": List[ClientListClusterJobsResponseJobListEntriesTypeDef], "NextToken": str},
    total=False,
)


class ClientListClusterJobsResponseTypeDef(_ClientListClusterJobsResponseTypeDef):
    """
    - *(dict) --*

      - **JobListEntries** *(list) --*

        Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
        whether the job is a job part, in the case of export jobs.
        - *(dict) --*

          Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that
          indicates whether the job is a job part, in the case of an export job.
          - **JobId** *(string) --*

            The automatically generated ID for a job, for example
            ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ClientListClustersResponseClusterListEntriesTypeDef = TypedDict(
    "_ClientListClustersResponseClusterListEntriesTypeDef",
    {
        "ClusterId": str,
        "ClusterState": Literal["AwaitingQuorum", "Pending", "InUse", "Complete", "Cancelled"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListClustersResponseClusterListEntriesTypeDef(
    _ClientListClustersResponseClusterListEntriesTypeDef
):
    """
    - *(dict) --*

      Contains a cluster's state, a cluster's ID, and other important information.
      - **ClusterId** *(string) --*

        The 39-character ID for the cluster that you want to list, for example
        ``CID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ClientListClustersResponseTypeDef = TypedDict(
    "_ClientListClustersResponseTypeDef",
    {
        "ClusterListEntries": List[ClientListClustersResponseClusterListEntriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListClustersResponseTypeDef(_ClientListClustersResponseTypeDef):
    """
    - *(dict) --*

      - **ClusterListEntries** *(list) --*

        Each ``ClusterListEntry`` object contains a cluster's state, a cluster's ID, and other
        important status information.
        - *(dict) --*

          Contains a cluster's state, a cluster's ID, and other important information.
          - **ClusterId** *(string) --*

            The 39-character ID for the cluster that you want to list, for example
            ``CID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ClientListCompatibleImagesResponseCompatibleImagesTypeDef = TypedDict(
    "_ClientListCompatibleImagesResponseCompatibleImagesTypeDef",
    {"AmiId": str, "Name": str},
    total=False,
)


class ClientListCompatibleImagesResponseCompatibleImagesTypeDef(
    _ClientListCompatibleImagesResponseCompatibleImagesTypeDef
):
    """
    - *(dict) --*

      A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including the
      ID and name for a Snowball Edge AMI. This AMI is compatible with the device's physical
      hardware requirements, and it should be able to be run in an SBE1 instance on the device.
      - **AmiId** *(string) --*

        The unique identifier for an individual Snowball Edge AMI.
    """


_ClientListCompatibleImagesResponseTypeDef = TypedDict(
    "_ClientListCompatibleImagesResponseTypeDef",
    {
        "CompatibleImages": List[ClientListCompatibleImagesResponseCompatibleImagesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListCompatibleImagesResponseTypeDef(_ClientListCompatibleImagesResponseTypeDef):
    """
    - *(dict) --*

      - **CompatibleImages** *(list) --*

        A JSON-formatted object that describes a compatible AMI, including the ID and name for a
        Snowball Edge AMI.
        - *(dict) --*

          A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including
          the ID and name for a Snowball Edge AMI. This AMI is compatible with the device's physical
          hardware requirements, and it should be able to be run in an SBE1 instance on the device.
          - **AmiId** *(string) --*

            The unique identifier for an individual Snowball Edge AMI.
    """


_ClientListJobsResponseJobListEntriesTypeDef = TypedDict(
    "_ClientListJobsResponseJobListEntriesTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "IsMaster": bool,
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ClientListJobsResponseJobListEntriesTypeDef(_ClientListJobsResponseJobListEntriesTypeDef):
    """
    - *(dict) --*

      Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
      whether the job is a job part, in the case of an export job.
      - **JobId** *(string) --*

        The automatically generated ID for a job, for example
        ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"JobListEntries": List[ClientListJobsResponseJobListEntriesTypeDef], "NextToken": str},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    - *(dict) --*

      - **JobListEntries** *(list) --*

        Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
        whether the job is a job part, in the case of export jobs.
        - *(dict) --*

          Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that
          indicates whether the job is a job part, in the case of an export job.
          - **JobId** *(string) --*

            The automatically generated ID for a job, for example
            ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ClientUpdateClusterNotificationTypeDef = TypedDict(
    "_ClientUpdateClusterNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)


class ClientUpdateClusterNotificationTypeDef(_ClientUpdateClusterNotificationTypeDef):
    """
    The new or updated  Notification object.
    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
      Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
      You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console,
      or by using the `Subscribe <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__
      AWS Simple Notification Service (SNS) API action.
    """


_ClientUpdateClusterResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)


class ClientUpdateClusterResourcesEc2AmiResourcesTypeDef(
    _ClientUpdateClusterResourcesEc2AmiResourcesTypeDef
):
    pass


_ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef
):
    pass


_ClientUpdateClusterResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[ClientUpdateClusterResourcesLambdaResourcesEventTriggersTypeDef],
    },
    total=False,
)


class ClientUpdateClusterResourcesLambdaResourcesTypeDef(
    _ClientUpdateClusterResourcesLambdaResourcesTypeDef
):
    pass


_ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef(
    _ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef
):
    pass


_ClientUpdateClusterResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesS3ResourcesTypeDef",
    {"BucketArn": str, "KeyRange": ClientUpdateClusterResourcesS3ResourcesKeyRangeTypeDef},
    total=False,
)


class ClientUpdateClusterResourcesS3ResourcesTypeDef(
    _ClientUpdateClusterResourcesS3ResourcesTypeDef
):
    """
    - *(dict) --*

      Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
      exported from or imported into. For export jobs, this object can have an optional ``KeyRange``
      value. The length of the range is defined at job creation, and has either an inclusive
      ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
      - **BucketArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon S3 bucket.
    """


_ClientUpdateClusterResourcesTypeDef = TypedDict(
    "_ClientUpdateClusterResourcesTypeDef",
    {
        "S3Resources": List[ClientUpdateClusterResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientUpdateClusterResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientUpdateClusterResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)


class ClientUpdateClusterResourcesTypeDef(_ClientUpdateClusterResourcesTypeDef):
    """
    The updated arrays of  JobResource objects that can include updated  S3Resource objects or
    LambdaResource objects.
    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.
      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
        exported from or imported into. For export jobs, this object can have an optional
        ``KeyRange`` value. The length of the range is defined at job creation, and has either an
        inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
        sorted.
        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.
    """


_ClientUpdateJobNotificationTypeDef = TypedDict(
    "_ClientUpdateJobNotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[
            Literal[
                "New",
                "PreparingAppliance",
                "PreparingShipment",
                "InTransitToCustomer",
                "WithCustomer",
                "InTransitToAWS",
                "WithAWSSortingFacility",
                "WithAWS",
                "InProgress",
                "Complete",
                "Cancelled",
                "Listing",
                "Pending",
            ]
        ],
        "NotifyAll": bool,
    },
    total=False,
)


class ClientUpdateJobNotificationTypeDef(_ClientUpdateJobNotificationTypeDef):
    """
    The new or updated  Notification object.
    - **SnsTopicARN** *(string) --*

      The new SNS ``TopicArn`` that you want to associate with this job. You can create Amazon
      Resource Names (ARNs) for topics by using the `CreateTopic
      <https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html>`__ Amazon SNS API action.
      You can subscribe email addresses to an Amazon SNS topic through the AWS Management Console,
      or by using the `Subscribe <https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html>`__
      AWS Simple Notification Service (SNS) API action.
    """


_ClientUpdateJobResourcesEc2AmiResourcesTypeDef = TypedDict(
    "_ClientUpdateJobResourcesEc2AmiResourcesTypeDef",
    {"AmiId": str, "SnowballAmiId": str},
    total=False,
)


class ClientUpdateJobResourcesEc2AmiResourcesTypeDef(
    _ClientUpdateJobResourcesEc2AmiResourcesTypeDef
):
    pass


_ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef = TypedDict(
    "_ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef",
    {"EventResourceARN": str},
    total=False,
)


class ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef(
    _ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef
):
    pass


_ClientUpdateJobResourcesLambdaResourcesTypeDef = TypedDict(
    "_ClientUpdateJobResourcesLambdaResourcesTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List[ClientUpdateJobResourcesLambdaResourcesEventTriggersTypeDef],
    },
    total=False,
)


class ClientUpdateJobResourcesLambdaResourcesTypeDef(
    _ClientUpdateJobResourcesLambdaResourcesTypeDef
):
    pass


_ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef = TypedDict(
    "_ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef",
    {"BeginMarker": str, "EndMarker": str},
    total=False,
)


class ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef(
    _ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef
):
    pass


_ClientUpdateJobResourcesS3ResourcesTypeDef = TypedDict(
    "_ClientUpdateJobResourcesS3ResourcesTypeDef",
    {"BucketArn": str, "KeyRange": ClientUpdateJobResourcesS3ResourcesKeyRangeTypeDef},
    total=False,
)


class ClientUpdateJobResourcesS3ResourcesTypeDef(_ClientUpdateJobResourcesS3ResourcesTypeDef):
    """
    - *(dict) --*

      Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
      exported from or imported into. For export jobs, this object can have an optional ``KeyRange``
      value. The length of the range is defined at job creation, and has either an inclusive
      ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary sorted.
      - **BucketArn** *(string) --*

        The Amazon Resource Name (ARN) of an Amazon S3 bucket.
    """


_ClientUpdateJobResourcesTypeDef = TypedDict(
    "_ClientUpdateJobResourcesTypeDef",
    {
        "S3Resources": List[ClientUpdateJobResourcesS3ResourcesTypeDef],
        "LambdaResources": List[ClientUpdateJobResourcesLambdaResourcesTypeDef],
        "Ec2AmiResources": List[ClientUpdateJobResourcesEc2AmiResourcesTypeDef],
    },
    total=False,
)


class ClientUpdateJobResourcesTypeDef(_ClientUpdateJobResourcesTypeDef):
    """
    The updated ``JobResource`` object, or the updated  JobResource object.
    - **S3Resources** *(list) --*

      An array of ``S3Resource`` objects.
      - *(dict) --*

        Each ``S3Resource`` object represents an Amazon S3 bucket that your transferred data will be
        exported from or imported into. For export jobs, this object can have an optional
        ``KeyRange`` value. The length of the range is defined at job creation, and has either an
        inclusive ``BeginMarker`` , an inclusive ``EndMarker`` , or both. Ranges are UTF-8 binary
        sorted.
        - **BucketArn** *(string) --*

          The Amazon Resource Name (ARN) of an Amazon S3 bucket.
    """


_DescribeAddressesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAddressesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAddressesPaginatePaginationConfigTypeDef(
    _DescribeAddressesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeAddressesPaginateResponseAddressesTypeDef = TypedDict(
    "_DescribeAddressesPaginateResponseAddressesTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)


class DescribeAddressesPaginateResponseAddressesTypeDef(
    _DescribeAddressesPaginateResponseAddressesTypeDef
):
    """
    - *(dict) --*

      The address that you want the Snowball or Snowballs associated with a specific job to be
      shipped to. Addresses are validated at the time of creation. The address you provide must be
      located within the serviceable area of your region. Although no individual elements of the
      ``Address`` are required, if the address is invalid or unsupported, then an exception is
      thrown.
      - **AddressId** *(string) --*

        The unique ID for an address.
    """


_DescribeAddressesPaginateResponseTypeDef = TypedDict(
    "_DescribeAddressesPaginateResponseTypeDef",
    {"Addresses": List[DescribeAddressesPaginateResponseAddressesTypeDef]},
    total=False,
)


class DescribeAddressesPaginateResponseTypeDef(_DescribeAddressesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **Addresses** *(list) --*

        The Snowball shipping addresses that were created for this account.
        - *(dict) --*

          The address that you want the Snowball or Snowballs associated with a specific job to be
          shipped to. Addresses are validated at the time of creation. The address you provide must
          be located within the serviceable area of your region. Although no individual elements of
          the ``Address`` are required, if the address is invalid or unsupported, then an exception
          is thrown.
          - **AddressId** *(string) --*

            The unique ID for an address.
    """


_ListClusterJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClusterJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListClusterJobsPaginatePaginationConfigTypeDef(
    _ListClusterJobsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListClusterJobsPaginateResponseJobListEntriesTypeDef = TypedDict(
    "_ListClusterJobsPaginateResponseJobListEntriesTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "IsMaster": bool,
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ListClusterJobsPaginateResponseJobListEntriesTypeDef(
    _ListClusterJobsPaginateResponseJobListEntriesTypeDef
):
    """
    - *(dict) --*

      Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
      whether the job is a job part, in the case of an export job.
      - **JobId** *(string) --*

        The automatically generated ID for a job, for example
        ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ListClusterJobsPaginateResponseTypeDef = TypedDict(
    "_ListClusterJobsPaginateResponseTypeDef",
    {"JobListEntries": List[ListClusterJobsPaginateResponseJobListEntriesTypeDef]},
    total=False,
)


class ListClusterJobsPaginateResponseTypeDef(_ListClusterJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **JobListEntries** *(list) --*

        Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
        whether the job is a job part, in the case of export jobs.
        - *(dict) --*

          Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that
          indicates whether the job is a job part, in the case of an export job.
          - **JobId** *(string) --*

            The automatically generated ID for a job, for example
            ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ListClustersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListClustersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListClustersPaginatePaginationConfigTypeDef(_ListClustersPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListClustersPaginateResponseClusterListEntriesTypeDef = TypedDict(
    "_ListClustersPaginateResponseClusterListEntriesTypeDef",
    {
        "ClusterId": str,
        "ClusterState": Literal["AwaitingQuorum", "Pending", "InUse", "Complete", "Cancelled"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ListClustersPaginateResponseClusterListEntriesTypeDef(
    _ListClustersPaginateResponseClusterListEntriesTypeDef
):
    """
    - *(dict) --*

      Contains a cluster's state, a cluster's ID, and other important information.
      - **ClusterId** *(string) --*

        The 39-character ID for the cluster that you want to list, for example
        ``CID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ListClustersPaginateResponseTypeDef = TypedDict(
    "_ListClustersPaginateResponseTypeDef",
    {"ClusterListEntries": List[ListClustersPaginateResponseClusterListEntriesTypeDef]},
    total=False,
)


class ListClustersPaginateResponseTypeDef(_ListClustersPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **ClusterListEntries** *(list) --*

        Each ``ClusterListEntry`` object contains a cluster's state, a cluster's ID, and other
        important status information.
        - *(dict) --*

          Contains a cluster's state, a cluster's ID, and other important information.
          - **ClusterId** *(string) --*

            The 39-character ID for the cluster that you want to list, for example
            ``CID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ListCompatibleImagesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCompatibleImagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCompatibleImagesPaginatePaginationConfigTypeDef(
    _ListCompatibleImagesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef = TypedDict(
    "_ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef",
    {"AmiId": str, "Name": str},
    total=False,
)


class ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef(
    _ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef
):
    """
    - *(dict) --*

      A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including the
      ID and name for a Snowball Edge AMI. This AMI is compatible with the device's physical
      hardware requirements, and it should be able to be run in an SBE1 instance on the device.
      - **AmiId** *(string) --*

        The unique identifier for an individual Snowball Edge AMI.
    """


_ListCompatibleImagesPaginateResponseTypeDef = TypedDict(
    "_ListCompatibleImagesPaginateResponseTypeDef",
    {"CompatibleImages": List[ListCompatibleImagesPaginateResponseCompatibleImagesTypeDef]},
    total=False,
)


class ListCompatibleImagesPaginateResponseTypeDef(_ListCompatibleImagesPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **CompatibleImages** *(list) --*

        A JSON-formatted object that describes a compatible AMI, including the ID and name for a
        Snowball Edge AMI.
        - *(dict) --*

          A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including
          the ID and name for a Snowball Edge AMI. This AMI is compatible with the device's physical
          hardware requirements, and it should be able to be run in an SBE1 instance on the device.
          - **AmiId** *(string) --*

            The unique identifier for an individual Snowball Edge AMI.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobsPaginateResponseJobListEntriesTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobListEntriesTypeDef",
    {
        "JobId": str,
        "JobState": Literal[
            "New",
            "PreparingAppliance",
            "PreparingShipment",
            "InTransitToCustomer",
            "WithCustomer",
            "InTransitToAWS",
            "WithAWSSortingFacility",
            "WithAWS",
            "InProgress",
            "Complete",
            "Cancelled",
            "Listing",
            "Pending",
        ],
        "IsMaster": bool,
        "JobType": Literal["IMPORT", "EXPORT", "LOCAL_USE"],
        "SnowballType": Literal["STANDARD", "EDGE", "EDGE_C", "EDGE_CG"],
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)


class ListJobsPaginateResponseJobListEntriesTypeDef(_ListJobsPaginateResponseJobListEntriesTypeDef):
    """
    - *(dict) --*

      Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
      whether the job is a job part, in the case of an export job.
      - **JobId** *(string) --*

        The automatically generated ID for a job, for example
        ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {"JobListEntries": List[ListJobsPaginateResponseJobListEntriesTypeDef]},
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    - *(dict) --*

      - **JobListEntries** *(list) --*

        Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
        whether the job is a job part, in the case of export jobs.
        - *(dict) --*

          Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that
          indicates whether the job is a job part, in the case of an export job.
          - **JobId** *(string) --*

            The automatically generated ID for a job, for example
            ``JID123e4567-e89b-12d3-a456-426655440000`` .
    """
