"Main interface for es service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAddTagsTagListTypeDef",
    "ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    "ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "ClientCreateElasticsearchDomainCognitoOptionsTypeDef",
    "ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef",
    "ClientCreateElasticsearchDomainEBSOptionsTypeDef",
    "ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef",
    "ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef",
    "ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    "ClientCreateElasticsearchDomainResponseDomainStatusTypeDef",
    "ClientCreateElasticsearchDomainResponseTypeDef",
    "ClientCreateElasticsearchDomainSnapshotOptionsTypeDef",
    "ClientCreateElasticsearchDomainVPCOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    "ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef",
    "ClientDeleteElasticsearchDomainResponseTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef",
    "ClientDescribeElasticsearchDomainConfigResponseTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    "ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef",
    "ClientDescribeElasticsearchDomainResponseTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef",
    "ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef",
    "ClientDescribeElasticsearchDomainsResponseTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef",
    "ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef",
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef",
    "ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    "ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef",
    "ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef",
    "ClientDescribeReservedElasticsearchInstancesResponseTypeDef",
    "ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef",
    "ClientGetCompatibleElasticsearchVersionsResponseTypeDef",
    "ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef",
    "ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef",
    "ClientGetUpgradeHistoryResponseTypeDef",
    "ClientGetUpgradeStatusResponseTypeDef",
    "ClientListDomainNamesResponseDomainNamesTypeDef",
    "ClientListDomainNamesResponseTypeDef",
    "ClientListElasticsearchInstanceTypesResponseTypeDef",
    "ClientListElasticsearchVersionsResponseTypeDef",
    "ClientListTagsResponseTagListTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    "ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    "ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef",
    "ClientUpdateElasticsearchDomainConfigResponseTypeDef",
    "ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef",
    "ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef",
    "ClientUpgradeElasticsearchDomainResponseTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef",
    "DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef",
    "DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef",
    "DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef",
    "DescribeReservedElasticsearchInstancesPaginateResponseTypeDef",
    "GetUpgradeHistoryPaginatePaginationConfigTypeDef",
    "GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef",
    "GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef",
    "GetUpgradeHistoryPaginateResponseTypeDef",
    "ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef",
    "ListElasticsearchInstanceTypesPaginateResponseTypeDef",
    "ListElasticsearchVersionsPaginatePaginationConfigTypeDef",
    "ListElasticsearchVersionsPaginateResponseTypeDef",
)


_RequiredClientAddTagsTagListTypeDef = TypedDict(
    "_RequiredClientAddTagsTagListTypeDef", {"Key": str}
)
_OptionalClientAddTagsTagListTypeDef = TypedDict(
    "_OptionalClientAddTagsTagListTypeDef", {"Value": str}, total=False
)


class ClientAddTagsTagListTypeDef(
    _RequiredClientAddTagsTagListTypeDef, _OptionalClientAddTagsTagListTypeDef
):
    """
    - *(dict) --*

      Specifies a key value pair for a resource tag.
      - **Key** *(string) --***[REQUIRED]**

        Specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
        Elasticsearch domain to which they are attached.
    """


_ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef(
    _ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef
):
    """
    - **ServiceSoftwareOptions** *(dict) --*

      The current status of the Elasticsearch service software update.
      - **CurrentVersion** *(string) --*

        The current service software version that is present on the domain.
    """


_ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "_ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": ClientCancelElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef
    },
    total=False,
)


class ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef(
    _ClientCancelElasticsearchServiceSoftwareUpdateResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``CancelElasticsearchServiceSoftwareUpdate`` operation. Contains the status of
      the update.
      - **ServiceSoftwareOptions** *(dict) --*

        The current status of the Elasticsearch service software update.
        - **CurrentVersion** *(string) --*

          The current service software version that is present on the domain.
    """


_ClientCreateElasticsearchDomainCognitoOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientCreateElasticsearchDomainCognitoOptionsTypeDef(
    _ClientCreateElasticsearchDomainCognitoOptionsTypeDef
):
    """
    Options to specify the Cognito user and identity pools for Kibana authentication. For more
    information, see `Amazon Cognito Authentication for Kibana
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
    .
    - **Enabled** *(boolean) --*

      Specifies the option to enable Cognito for Kibana authentication.
    """


_ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef(
    _ClientCreateElasticsearchDomainDomainEndpointOptionsTypeDef
):
    """
    Options to specify configuration that will be applied to the domain endpoint.
    - **EnforceHTTPS** *(boolean) --*

      Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.
    """


_ClientCreateElasticsearchDomainEBSOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)


class ClientCreateElasticsearchDomainEBSOptionsTypeDef(
    _ClientCreateElasticsearchDomainEBSOptionsTypeDef
):
    """
    Options to enable, disable and specify the type and size of EBS storage volumes.
    - **EBSEnabled** *(boolean) --*

      Specifies whether EBS-based storage is enabled.
    """


_ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    pass


_ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientCreateElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef(
    _ClientCreateElasticsearchDomainElasticsearchClusterConfigTypeDef
):
    """
    Configuration options for an Elasticsearch domain. Specifies the instance type and number of
    instances in the domain cluster.
    - **InstanceType** *(string) --*

      The instance type for an Elasticsearch cluster.
    """


_ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef(
    _ClientCreateElasticsearchDomainEncryptionAtRestOptionsTypeDef
):
    """
    Specifies the Encryption At Rest Options.
    - **Enabled** *(boolean) --*

      Specifies the option to enable Encryption At Rest.
    """


_ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef(
    _ClientCreateElasticsearchDomainLogPublishingOptionsTypeDef
):
    pass


_ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef(
    _ClientCreateElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef
):
    """
    Specifies the NodeToNodeEncryptionOptions.
    - **Enabled** *(boolean) --*

      Specify true to enable node-to-node encryption.
    """


_ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef
):
    pass


_ClientCreateElasticsearchDomainResponseDomainStatusTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientCreateElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientCreateElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientCreateElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef,
        "VPCOptions": ClientCreateElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef,
        "CognitoOptions": ClientCreateElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientCreateElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientCreateElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str, ClientCreateElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
        ],
        "ServiceSoftwareOptions": ClientCreateElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientCreateElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientCreateElasticsearchDomainResponseDomainStatusTypeDef(
    _ClientCreateElasticsearchDomainResponseDomainStatusTypeDef
):
    """
    - **DomainStatus** *(dict) --*

      The status of the newly created Elasticsearch domain.
      - **DomainId** *(string) --*

        The unique identifier for the specified Elasticsearch domain.
    """


_ClientCreateElasticsearchDomainResponseTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainResponseTypeDef",
    {"DomainStatus": ClientCreateElasticsearchDomainResponseDomainStatusTypeDef},
    total=False,
)


class ClientCreateElasticsearchDomainResponseTypeDef(
    _ClientCreateElasticsearchDomainResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``CreateElasticsearchDomain`` operation. Contains the status of the newly
      created Elasticsearch domain.
      - **DomainStatus** *(dict) --*

        The status of the newly created Elasticsearch domain.
        - **DomainId** *(string) --*

          The unique identifier for the specified Elasticsearch domain.
    """


_ClientCreateElasticsearchDomainSnapshotOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientCreateElasticsearchDomainSnapshotOptionsTypeDef(
    _ClientCreateElasticsearchDomainSnapshotOptionsTypeDef
):
    """
    Option to set time, in UTC format, of the daily automated snapshot. Default value is 0 hours.
    - **AutomatedSnapshotStartHour** *(integer) --*

      Specifies the time, in UTC format, when the service takes a daily automated snapshot of the
      specified Elasticsearch domain. Default value is ``0`` hours.
    """


_ClientCreateElasticsearchDomainVPCOptionsTypeDef = TypedDict(
    "_ClientCreateElasticsearchDomainVPCOptionsTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientCreateElasticsearchDomainVPCOptionsTypeDef(
    _ClientCreateElasticsearchDomainVPCOptionsTypeDef
):
    """
    Options to specify the subnets and security groups for VPC endpoint. For more information, see
    `Creating a VPC
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc>`__
    in *VPC Endpoints for Amazon Elasticsearch Service Domains*
    - **SubnetIds** *(list) --*

      Specifies the subnets for VPC endpoint.
      - *(string) --*
    """


_ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef
):
    pass


_ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientDeleteElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDeleteElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientDeleteElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef,
        "VPCOptions": ClientDeleteElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef,
        "CognitoOptions": ClientDeleteElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDeleteElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDeleteElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str, ClientDeleteElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
        ],
        "ServiceSoftwareOptions": ClientDeleteElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientDeleteElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef(
    _ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef
):
    """
    - **DomainStatus** *(dict) --*

      The status of the Elasticsearch domain being deleted.
      - **DomainId** *(string) --*

        The unique identifier for the specified Elasticsearch domain.
    """


_ClientDeleteElasticsearchDomainResponseTypeDef = TypedDict(
    "_ClientDeleteElasticsearchDomainResponseTypeDef",
    {"DomainStatus": ClientDeleteElasticsearchDomainResponseDomainStatusTypeDef},
    total=False,
)


class ClientDeleteElasticsearchDomainResponseTypeDef(
    _ClientDeleteElasticsearchDomainResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``DeleteElasticsearchDomain`` request. Contains the status of the pending
      deletion, or no status if the domain and all of its resources have been deleted.
      - **DomainStatus** *(dict) --*

        The status of the Elasticsearch domain being deleted.
        - **DomainId** *(string) --*

          The unique identifier for the specified Elasticsearch domain.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    {
        "Options": Dict[str, str],
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    {
        "Options": str,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef
):
    """
    - **ElasticsearchVersion** *(dict) --*

      String of format X.Y to specify version for the Elasticsearch domain.
      - **Options** *(string) --*

        Specifies the Elasticsearch version for the specified Elasticsearch domain.
    """


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    {
        "Options": Dict[
            str,
            ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef,
        ],
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    {
        "Options": ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef,
        "Status": ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef",
    {
        "ElasticsearchVersion": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef,
        "ElasticsearchClusterConfig": ClientDescribeElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef,
        "AccessPolicies": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef,
        "SnapshotOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef,
        "VPCOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef,
        "CognitoOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef,
        "LogPublishingOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef,
        "DomainEndpointOptions": ClientDescribeElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef
):
    """
    - **DomainConfig** *(dict) --*

      The configuration information of the domain requested in the
      ``DescribeElasticsearchDomainConfig`` request.
      - **ElasticsearchVersion** *(dict) --*

        String of format X.Y to specify version for the Elasticsearch domain.
        - **Options** *(string) --*

          Specifies the Elasticsearch version for the specified Elasticsearch domain.
    """


_ClientDescribeElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainConfigResponseTypeDef",
    {"DomainConfig": ClientDescribeElasticsearchDomainConfigResponseDomainConfigTypeDef},
    total=False,
)


class ClientDescribeElasticsearchDomainConfigResponseTypeDef(
    _ClientDescribeElasticsearchDomainConfigResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``DescribeElasticsearchDomainConfig`` request. Contains the configuration
      information of the requested domain.
      - **DomainConfig** *(dict) --*

        The configuration information of the domain requested in the
        ``DescribeElasticsearchDomainConfig`` request.
        - **ElasticsearchVersion** *(dict) --*

          String of format X.Y to specify version for the Elasticsearch domain.
          - **Options** *(string) --*

            Specifies the Elasticsearch version for the specified Elasticsearch domain.
    """


_ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientDescribeElasticsearchDomainResponseDomainStatusElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDescribeElasticsearchDomainResponseDomainStatusEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientDescribeElasticsearchDomainResponseDomainStatusSnapshotOptionsTypeDef,
        "VPCOptions": ClientDescribeElasticsearchDomainResponseDomainStatusVPCOptionsTypeDef,
        "CognitoOptions": ClientDescribeElasticsearchDomainResponseDomainStatusCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDescribeElasticsearchDomainResponseDomainStatusEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDescribeElasticsearchDomainResponseDomainStatusNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str, ClientDescribeElasticsearchDomainResponseDomainStatusLogPublishingOptionsTypeDef
        ],
        "ServiceSoftwareOptions": ClientDescribeElasticsearchDomainResponseDomainStatusServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientDescribeElasticsearchDomainResponseDomainStatusDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef(
    _ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef
):
    """
    - **DomainStatus** *(dict) --*

      The current status of the Elasticsearch domain.
      - **DomainId** *(string) --*

        The unique identifier for the specified Elasticsearch domain.
    """


_ClientDescribeElasticsearchDomainResponseTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainResponseTypeDef",
    {"DomainStatus": ClientDescribeElasticsearchDomainResponseDomainStatusTypeDef},
    total=False,
)


class ClientDescribeElasticsearchDomainResponseTypeDef(
    _ClientDescribeElasticsearchDomainResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``DescribeElasticsearchDomain`` request. Contains the status of the domain
      specified in the request.
      - **DomainStatus** *(dict) --*

        The current status of the Elasticsearch domain.
        - **DomainId** *(string) --*

          The unique identifier for the specified Elasticsearch domain.
    """


_ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef
):
    pass


_ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": ClientDescribeElasticsearchDomainsResponseDomainStatusListElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListEBSOptionsTypeDef,
        "AccessPolicies": str,
        "SnapshotOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListSnapshotOptionsTypeDef,
        "VPCOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListVPCOptionsTypeDef,
        "CognitoOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[
            str,
            ClientDescribeElasticsearchDomainsResponseDomainStatusListLogPublishingOptionsTypeDef,
        ],
        "ServiceSoftwareOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListServiceSoftwareOptionsTypeDef,
        "DomainEndpointOptions": ClientDescribeElasticsearchDomainsResponseDomainStatusListDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef(
    _ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef
):
    """
    - *(dict) --*

      The current status of an Elasticsearch domain.
      - **DomainId** *(string) --*

        The unique identifier for the specified Elasticsearch domain.
    """


_ClientDescribeElasticsearchDomainsResponseTypeDef = TypedDict(
    "_ClientDescribeElasticsearchDomainsResponseTypeDef",
    {"DomainStatusList": List[ClientDescribeElasticsearchDomainsResponseDomainStatusListTypeDef]},
    total=False,
)


class ClientDescribeElasticsearchDomainsResponseTypeDef(
    _ClientDescribeElasticsearchDomainsResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``DescribeElasticsearchDomains`` request. Contains the status of the specified
      domains or all domains owned by the account.
      - **DomainStatusList** *(list) --*

        The status of the domains requested in the ``DescribeElasticsearchDomains`` request.
        - *(dict) --*

          The current status of an Elasticsearch domain.
          - **DomainId** *(string) --*

            The unique identifier for the specified Elasticsearch domain.
    """


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef",
    {"LimitName": str, "LimitValues": List[str]},
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef
):
    pass


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef",
    {"MinimumInstanceCount": int, "MaximumInstanceCount": int},
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef
):
    pass


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef",
    {
        "InstanceCountLimits": ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsInstanceCountLimitsTypeDef
    },
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef
):
    pass


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef",
    {"LimitName": str, "LimitValues": List[str]},
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef
):
    pass


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef",
    {
        "StorageTypeName": str,
        "StorageSubTypeName": str,
        "StorageTypeLimits": List[
            ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesStorageTypeLimitsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef
):
    pass


_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef",
    {
        "StorageTypes": List[
            ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleStorageTypesTypeDef
        ],
        "InstanceLimits": ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleInstanceLimitsTypeDef,
        "AdditionalLimits": List[
            ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleAdditionalLimitsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef
):
    pass


_ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    {
        "LimitsByRole": Dict[
            str, ClientDescribeElasticsearchInstanceTypeLimitsResponseLimitsByRoleTypeDef
        ]
    },
    total=False,
)


class ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef(
    _ClientDescribeElasticsearchInstanceTypeLimitsResponseTypeDef
):
    """
    - *(dict) --*

      Container for the parameters received from ``  DescribeElasticsearchInstanceTypeLimits ``
      operation.
      - **LimitsByRole** *(dict) --*

        Map of Role of the Instance and Limits that are applicable. Role performed by given Instance
        in Elasticsearch can be one of the following:
        * Data: If the given InstanceType is used as Data node
        * Master: If the given InstanceType is used as Master node
        - *(string) --*

          - *(dict) --*

            Limits for given InstanceType and for each of it's role. Limits contains following ``
            StorageTypes, ``  ``  InstanceLimits `` and ``  AdditionalLimits ``
            - **StorageTypes** *(list) --*

              StorageType represents the list of storage related types and attributes that are
              available for given InstanceType.
              - *(dict) --*

                StorageTypes represents the list of storage related types and their attributes that
                are available for given InstanceType.
                - **StorageTypeName** *(string) --*

                  Type of the storage. List of available storage options:
                  * instance
                  Inbuilt storage available for the given Instance
                  * ebs
                  Elastic block storage that would be attached to the given Instance
    """


_ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef(
    _ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef
):
    pass


_ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": Literal["ALL_UPFRONT", "PARTIAL_UPFRONT", "NO_UPFRONT"],
        "RecurringCharges": List[
            ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef(
    _ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef
):
    pass


_ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstanceOfferings": List[
            ClientDescribeReservedElasticsearchInstanceOfferingsResponseReservedElasticsearchInstanceOfferingsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef(
    _ClientDescribeReservedElasticsearchInstanceOfferingsResponseTypeDef
):
    """
    - *(dict) --*

      Container for results from ``DescribeReservedElasticsearchInstanceOfferings``
      - **NextToken** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef(
    _ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef
):
    pass


_ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef",
    {
        "ReservationName": str,
        "ReservedElasticsearchInstanceId": str,
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ElasticsearchInstanceCount": int,
        "State": str,
        "PaymentOption": Literal["ALL_UPFRONT", "PARTIAL_UPFRONT", "NO_UPFRONT"],
        "RecurringCharges": List[
            ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesRecurringChargesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef(
    _ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef
):
    pass


_ClientDescribeReservedElasticsearchInstancesResponseTypeDef = TypedDict(
    "_ClientDescribeReservedElasticsearchInstancesResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstances": List[
            ClientDescribeReservedElasticsearchInstancesResponseReservedElasticsearchInstancesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeReservedElasticsearchInstancesResponseTypeDef(
    _ClientDescribeReservedElasticsearchInstancesResponseTypeDef
):
    """
    - *(dict) --*

      Container for results from ``DescribeReservedElasticsearchInstances``
      - **NextToken** *(string) --*

        Provides an identifier to allow retrieval of paginated results.
    """


_ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef = TypedDict(
    "_ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef",
    {"SourceVersion": str, "TargetVersions": List[str]},
    total=False,
)


class ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef(
    _ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef
):
    """
    - *(dict) --*

      A map from an ``  ElasticsearchVersion `` to a list of compatible ``  ElasticsearchVersion ``
      s to which the domain can be upgraded.
      - **SourceVersion** *(string) --*

        The current version of Elasticsearch on which a domain is.
    """


_ClientGetCompatibleElasticsearchVersionsResponseTypeDef = TypedDict(
    "_ClientGetCompatibleElasticsearchVersionsResponseTypeDef",
    {
        "CompatibleElasticsearchVersions": List[
            ClientGetCompatibleElasticsearchVersionsResponseCompatibleElasticsearchVersionsTypeDef
        ]
    },
    total=False,
)


class ClientGetCompatibleElasticsearchVersionsResponseTypeDef(
    _ClientGetCompatibleElasticsearchVersionsResponseTypeDef
):
    """
    - *(dict) --*

      Container for response returned by ``  GetCompatibleElasticsearchVersions `` operation.
      - **CompatibleElasticsearchVersions** *(list) --*

        A map of compatible Elasticsearch versions returned as part of the ``
        GetCompatibleElasticsearchVersions `` operation.
        - *(dict) --*

          A map from an ``  ElasticsearchVersion `` to a list of compatible ``  ElasticsearchVersion
          `` s to which the domain can be upgraded.
          - **SourceVersion** *(string) --*

            The current version of Elasticsearch on which a domain is.
    """


_ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef = TypedDict(
    "_ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef",
    {
        "UpgradeStep": Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"],
        "UpgradeStepStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "Issues": List[str],
        "ProgressPercent": float,
    },
    total=False,
)


class ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef(
    _ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef
):
    pass


_ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef = TypedDict(
    "_ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef",
    {
        "UpgradeName": str,
        "StartTimestamp": datetime,
        "UpgradeStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "StepsList": List[ClientGetUpgradeHistoryResponseUpgradeHistoriesStepsListTypeDef],
    },
    total=False,
)


class ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef(
    _ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef
):
    """
    - *(dict) --*

      History of the last 10 Upgrades and Upgrade Eligibility Checks.
      - **UpgradeName** *(string) --*

        A string that describes the update briefly
    """


_ClientGetUpgradeHistoryResponseTypeDef = TypedDict(
    "_ClientGetUpgradeHistoryResponseTypeDef",
    {
        "UpgradeHistories": List[ClientGetUpgradeHistoryResponseUpgradeHistoriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetUpgradeHistoryResponseTypeDef(_ClientGetUpgradeHistoryResponseTypeDef):
    """
    - *(dict) --*

      Container for response returned by ``  GetUpgradeHistory `` operation.
      - **UpgradeHistories** *(list) --*

        A list of ``  UpgradeHistory `` objects corresponding to each Upgrade or Upgrade Eligibility
        Check performed on a domain returned as part of ``  GetUpgradeHistoryResponse `` object.
        - *(dict) --*

          History of the last 10 Upgrades and Upgrade Eligibility Checks.
          - **UpgradeName** *(string) --*

            A string that describes the update briefly
    """


_ClientGetUpgradeStatusResponseTypeDef = TypedDict(
    "_ClientGetUpgradeStatusResponseTypeDef",
    {
        "UpgradeStep": Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"],
        "StepStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "UpgradeName": str,
    },
    total=False,
)


class ClientGetUpgradeStatusResponseTypeDef(_ClientGetUpgradeStatusResponseTypeDef):
    """
    - *(dict) --*

      Container for response returned by ``  GetUpgradeStatus `` operation.
      - **UpgradeStep** *(string) --*

        Represents one of 3 steps that an Upgrade or Upgrade Eligibility Check does through:
        * PreUpgradeCheck
        * Snapshot
        * Upgrade
    """


_ClientListDomainNamesResponseDomainNamesTypeDef = TypedDict(
    "_ClientListDomainNamesResponseDomainNamesTypeDef", {"DomainName": str}, total=False
)


class ClientListDomainNamesResponseDomainNamesTypeDef(
    _ClientListDomainNamesResponseDomainNamesTypeDef
):
    """
    - *(dict) --*

      - **DomainName** *(string) --*

        Specifies the ``DomainName`` .
    """


_ClientListDomainNamesResponseTypeDef = TypedDict(
    "_ClientListDomainNamesResponseTypeDef",
    {"DomainNames": List[ClientListDomainNamesResponseDomainNamesTypeDef]},
    total=False,
)


class ClientListDomainNamesResponseTypeDef(_ClientListDomainNamesResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``ListDomainNames`` operation. Contains the names of all Elasticsearch domains
      owned by this account.
      - **DomainNames** *(list) --*

        List of Elasticsearch domain names.
        - *(dict) --*

          - **DomainName** *(string) --*

            Specifies the ``DomainName`` .
    """


_ClientListElasticsearchInstanceTypesResponseTypeDef = TypedDict(
    "_ClientListElasticsearchInstanceTypesResponseTypeDef",
    {
        "ElasticsearchInstanceTypes": List[
            Literal[
                "m3.medium.elasticsearch",
                "m3.large.elasticsearch",
                "m3.xlarge.elasticsearch",
                "m3.2xlarge.elasticsearch",
                "m4.large.elasticsearch",
                "m4.xlarge.elasticsearch",
                "m4.2xlarge.elasticsearch",
                "m4.4xlarge.elasticsearch",
                "m4.10xlarge.elasticsearch",
                "m5.large.elasticsearch",
                "m5.xlarge.elasticsearch",
                "m5.2xlarge.elasticsearch",
                "m5.4xlarge.elasticsearch",
                "m5.12xlarge.elasticsearch",
                "r5.large.elasticsearch",
                "r5.xlarge.elasticsearch",
                "r5.2xlarge.elasticsearch",
                "r5.4xlarge.elasticsearch",
                "r5.12xlarge.elasticsearch",
                "c5.large.elasticsearch",
                "c5.xlarge.elasticsearch",
                "c5.2xlarge.elasticsearch",
                "c5.4xlarge.elasticsearch",
                "c5.9xlarge.elasticsearch",
                "c5.18xlarge.elasticsearch",
                "t2.micro.elasticsearch",
                "t2.small.elasticsearch",
                "t2.medium.elasticsearch",
                "r3.large.elasticsearch",
                "r3.xlarge.elasticsearch",
                "r3.2xlarge.elasticsearch",
                "r3.4xlarge.elasticsearch",
                "r3.8xlarge.elasticsearch",
                "i2.xlarge.elasticsearch",
                "i2.2xlarge.elasticsearch",
                "d2.xlarge.elasticsearch",
                "d2.2xlarge.elasticsearch",
                "d2.4xlarge.elasticsearch",
                "d2.8xlarge.elasticsearch",
                "c4.large.elasticsearch",
                "c4.xlarge.elasticsearch",
                "c4.2xlarge.elasticsearch",
                "c4.4xlarge.elasticsearch",
                "c4.8xlarge.elasticsearch",
                "r4.large.elasticsearch",
                "r4.xlarge.elasticsearch",
                "r4.2xlarge.elasticsearch",
                "r4.4xlarge.elasticsearch",
                "r4.8xlarge.elasticsearch",
                "r4.16xlarge.elasticsearch",
                "i3.large.elasticsearch",
                "i3.xlarge.elasticsearch",
                "i3.2xlarge.elasticsearch",
                "i3.4xlarge.elasticsearch",
                "i3.8xlarge.elasticsearch",
                "i3.16xlarge.elasticsearch",
            ]
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListElasticsearchInstanceTypesResponseTypeDef(
    _ClientListElasticsearchInstanceTypesResponseTypeDef
):
    """
    - *(dict) --*

      Container for the parameters returned by ``  ListElasticsearchInstanceTypes `` operation.
      - **ElasticsearchInstanceTypes** *(list) --*

        List of instance types supported by Amazon Elasticsearch service for given ``
        ElasticsearchVersion ``
        - *(string) --*
    """


_ClientListElasticsearchVersionsResponseTypeDef = TypedDict(
    "_ClientListElasticsearchVersionsResponseTypeDef",
    {"ElasticsearchVersions": List[str], "NextToken": str},
    total=False,
)


class ClientListElasticsearchVersionsResponseTypeDef(
    _ClientListElasticsearchVersionsResponseTypeDef
):
    """
    - *(dict) --*

      Container for the parameters for response received from ``  ListElasticsearchVersions ``
      operation.
      - **ElasticsearchVersions** *(list) --*

        List of supported elastic search versions.
        - *(string) --*
    """


_ClientListTagsResponseTagListTypeDef = TypedDict(
    "_ClientListTagsResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientListTagsResponseTagListTypeDef(_ClientListTagsResponseTagListTypeDef):
    """
    - *(dict) --*

      Specifies a key value pair for a resource tag.
      - **Key** *(string) --*

        Specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
        Elasticsearch domain to which they are attached.
    """


_ClientListTagsResponseTypeDef = TypedDict(
    "_ClientListTagsResponseTypeDef",
    {"TagList": List[ClientListTagsResponseTagListTypeDef]},
    total=False,
)


class ClientListTagsResponseTypeDef(_ClientListTagsResponseTypeDef):
    """
    - *(dict) --*

      The result of a ``ListTags`` operation. Contains tags for all requested Elasticsearch domains.
      - **TagList** *(list) --*

        List of ``Tag`` for the requested Elasticsearch domain.
        - *(dict) --*

          Specifies a key value pair for a resource tag.
          - **Key** *(string) --*

            Specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the
            Elasticsearch domain to which they are attached.
    """


_ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef = TypedDict(
    "_ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    {"ReservedElasticsearchInstanceId": str, "ReservationName": str},
    total=False,
)


class ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef(
    _ClientPurchaseReservedElasticsearchInstanceOfferingResponseTypeDef
):
    """
    - *(dict) --*

      Represents the output of a ``PurchaseReservedElasticsearchInstanceOffering`` operation.
      - **ReservedElasticsearchInstanceId** *(string) --*

        Details of the reserved Elasticsearch instance which was purchased.
    """


_ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef = TypedDict(
    "_ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": Literal[
            "PENDING_UPDATE", "IN_PROGRESS", "COMPLETED", "NOT_ELIGIBLE", "ELIGIBLE"
        ],
        "Description": str,
        "AutomatedUpdateDate": datetime,
    },
    total=False,
)


class ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef(
    _ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef
):
    """
    - **ServiceSoftwareOptions** *(dict) --*

      The current status of the Elasticsearch service software update.
      - **CurrentVersion** *(string) --*

        The current service software version that is present on the domain.
    """


_ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "_ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {
        "ServiceSoftwareOptions": ClientStartElasticsearchServiceSoftwareUpdateResponseServiceSoftwareOptionsTypeDef
    },
    total=False,
)


class ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef(
    _ClientStartElasticsearchServiceSoftwareUpdateResponseTypeDef
):
    """
    - *(dict) --*

      The result of a ``StartElasticsearchServiceSoftwareUpdate`` operation. Contains the status of
      the update.
      - **ServiceSoftwareOptions** *(dict) --*

        The current status of the Elasticsearch service software update.
        - **CurrentVersion** *(string) --*

          The current service software version that is present on the domain.
    """


_ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigCognitoOptionsTypeDef
):
    """
    Options to specify the Cognito user and identity pools for Kibana authentication. For more
    information, see `Amazon Cognito Authentication for Kibana
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html>`__
    .
    - **Enabled** *(boolean) --*

      Specifies the option to enable Cognito for Kibana authentication.
    """


_ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigDomainEndpointOptionsTypeDef
):
    """
    Options to specify configuration that will be applied to the domain endpoint.
    - **EnforceHTTPS** *(boolean) --*

      Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.
    """


_ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigEBSOptionsTypeDef
):
    """
    Specify the type and size of the EBS volume that you want to use.
    - **EBSEnabled** *(boolean) --*

      Specifies whether EBS-based storage is enabled.
    """


_ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef(
    _ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef(
    _ClientUpdateElasticsearchDomainConfigElasticsearchClusterConfigTypeDef
):
    """
    The type and number of instances to instantiate for the domain cluster.
    - **InstanceType** *(string) --*

      The instance type for an Elasticsearch cluster.
    """


_ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigLogPublishingOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef",
    {
        "Options": str,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef",
    {
        "Options": Dict[str, str],
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"],
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": Literal["standard", "gp2", "io1"],
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef",
    {"AvailabilityZoneCount": int},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef",
    {
        "InstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsZoneAwarenessConfigTypeDef,
        "DedicatedMasterType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "DedicatedMasterCount": int,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef",
    {
        "Options": str,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef
):
    """
    - **ElasticsearchVersion** *(dict) --*

      String of format X.Y to specify version for the Elasticsearch domain.
      - **Options** *(string) --*

        Specifies the Elasticsearch version for the specified Elasticsearch domain.
    """


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef",
    {"Enabled": bool, "KmsKeyId": str},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef",
    {"CloudWatchLogsLogGroupArn": str, "Enabled": bool},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef",
    {
        "Options": Dict[
            str,
            ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsOptionsTypeDef,
        ],
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "UpdateVersion": int,
        "State": Literal["RequiresIndexDocuments", "Processing", "Active"],
        "PendingDeletion": bool,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef",
    {
        "Options": ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsOptionsTypeDef,
        "Status": ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsStatusTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef
):
    pass


_ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef",
    {
        "ElasticsearchVersion": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchVersionTypeDef,
        "ElasticsearchClusterConfig": ClientUpdateElasticsearchDomainConfigResponseDomainConfigElasticsearchClusterConfigTypeDef,
        "EBSOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEBSOptionsTypeDef,
        "AccessPolicies": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAccessPoliciesTypeDef,
        "SnapshotOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigSnapshotOptionsTypeDef,
        "VPCOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigVPCOptionsTypeDef,
        "CognitoOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigCognitoOptionsTypeDef,
        "EncryptionAtRestOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigEncryptionAtRestOptionsTypeDef,
        "NodeToNodeEncryptionOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigNodeToNodeEncryptionOptionsTypeDef,
        "AdvancedOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigAdvancedOptionsTypeDef,
        "LogPublishingOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigLogPublishingOptionsTypeDef,
        "DomainEndpointOptions": ClientUpdateElasticsearchDomainConfigResponseDomainConfigDomainEndpointOptionsTypeDef,
    },
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef
):
    """
    - **DomainConfig** *(dict) --*

      The status of the updated Elasticsearch domain.
      - **ElasticsearchVersion** *(dict) --*

        String of format X.Y to specify version for the Elasticsearch domain.
        - **Options** *(string) --*

          Specifies the Elasticsearch version for the specified Elasticsearch domain.
    """


_ClientUpdateElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigResponseTypeDef",
    {"DomainConfig": ClientUpdateElasticsearchDomainConfigResponseDomainConfigTypeDef},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigResponseTypeDef(
    _ClientUpdateElasticsearchDomainConfigResponseTypeDef
):
    """
    - *(dict) --*

      The result of an ``UpdateElasticsearchDomain`` request. Contains the status of the
      Elasticsearch domain being updated.
      - **DomainConfig** *(dict) --*

        The status of the updated Elasticsearch domain.
        - **ElasticsearchVersion** *(dict) --*

          String of format X.Y to specify version for the Elasticsearch domain.
          - **Options** *(string) --*

            Specifies the Elasticsearch version for the specified Elasticsearch domain.
    """


_ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef",
    {"AutomatedSnapshotStartHour": int},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigSnapshotOptionsTypeDef
):
    """
    Option to set the time, in UTC format, for the daily automated snapshot. Default value is ``0``
    hours.
    - **AutomatedSnapshotStartHour** *(integer) --*

      Specifies the time, in UTC format, when the service takes a daily automated snapshot of the
      specified Elasticsearch domain. Default value is ``0`` hours.
    """


_ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef = TypedDict(
    "_ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef(
    _ClientUpdateElasticsearchDomainConfigVPCOptionsTypeDef
):
    """
    Options to specify the subnets and security groups for VPC endpoint. For more information, see
    `Creating a VPC
    <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc>`__
    in *VPC Endpoints for Amazon Elasticsearch Service Domains*
    - **SubnetIds** *(list) --*

      Specifies the subnets for VPC endpoint.
      - *(string) --*
    """


_ClientUpgradeElasticsearchDomainResponseTypeDef = TypedDict(
    "_ClientUpgradeElasticsearchDomainResponseTypeDef",
    {"DomainName": str, "TargetVersion": str, "PerformCheckOnly": bool},
    total=False,
)


class ClientUpgradeElasticsearchDomainResponseTypeDef(
    _ClientUpgradeElasticsearchDomainResponseTypeDef
):
    """
    - *(dict) --*

      Container for response returned by ``  UpgradeElasticsearchDomain `` operation.
      - **DomainName** *(string) --*

        The name of an Elasticsearch domain. Domain names are unique across the domains owned by an
        account within an AWS region. Domain names start with a letter or number and can contain the
        following characters: a-z (lowercase), 0-9, and - (hyphen).
    """


_DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef(
    _DescribeReservedElasticsearchInstanceOfferingsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef(
    _DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef
):
    pass


_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": Literal["ALL_UPFRONT", "PARTIAL_UPFRONT", "NO_UPFRONT"],
        "RecurringCharges": List[
            DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsRecurringChargesTypeDef
        ],
    },
    total=False,
)


class DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef(
    _DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef
):
    """
    - *(dict) --*

      Details of a reserved Elasticsearch instance offering.
      - **ReservedElasticsearchInstanceOfferingId** *(string) --*

        The Elasticsearch reserved instance offering identifier.
    """


_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef",
    {
        "ReservedElasticsearchInstanceOfferings": List[
            DescribeReservedElasticsearchInstanceOfferingsPaginateResponseReservedElasticsearchInstanceOfferingsTypeDef
        ]
    },
    total=False,
)


class DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef(
    _DescribeReservedElasticsearchInstanceOfferingsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Container for results from ``DescribeReservedElasticsearchInstanceOfferings``
      - **ReservedElasticsearchInstanceOfferings** *(list) --*

        List of reserved Elasticsearch instance offerings
        - *(dict) --*

          Details of a reserved Elasticsearch instance offering.
          - **ReservedElasticsearchInstanceOfferingId** *(string) --*

            The Elasticsearch reserved instance offering identifier.
    """


_DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef(
    _DescribeReservedElasticsearchInstancesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)


class DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef(
    _DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef
):
    pass


_DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef",
    {
        "ReservationName": str,
        "ReservedElasticsearchInstanceId": str,
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": Literal[
            "m3.medium.elasticsearch",
            "m3.large.elasticsearch",
            "m3.xlarge.elasticsearch",
            "m3.2xlarge.elasticsearch",
            "m4.large.elasticsearch",
            "m4.xlarge.elasticsearch",
            "m4.2xlarge.elasticsearch",
            "m4.4xlarge.elasticsearch",
            "m4.10xlarge.elasticsearch",
            "m5.large.elasticsearch",
            "m5.xlarge.elasticsearch",
            "m5.2xlarge.elasticsearch",
            "m5.4xlarge.elasticsearch",
            "m5.12xlarge.elasticsearch",
            "r5.large.elasticsearch",
            "r5.xlarge.elasticsearch",
            "r5.2xlarge.elasticsearch",
            "r5.4xlarge.elasticsearch",
            "r5.12xlarge.elasticsearch",
            "c5.large.elasticsearch",
            "c5.xlarge.elasticsearch",
            "c5.2xlarge.elasticsearch",
            "c5.4xlarge.elasticsearch",
            "c5.9xlarge.elasticsearch",
            "c5.18xlarge.elasticsearch",
            "t2.micro.elasticsearch",
            "t2.small.elasticsearch",
            "t2.medium.elasticsearch",
            "r3.large.elasticsearch",
            "r3.xlarge.elasticsearch",
            "r3.2xlarge.elasticsearch",
            "r3.4xlarge.elasticsearch",
            "r3.8xlarge.elasticsearch",
            "i2.xlarge.elasticsearch",
            "i2.2xlarge.elasticsearch",
            "d2.xlarge.elasticsearch",
            "d2.2xlarge.elasticsearch",
            "d2.4xlarge.elasticsearch",
            "d2.8xlarge.elasticsearch",
            "c4.large.elasticsearch",
            "c4.xlarge.elasticsearch",
            "c4.2xlarge.elasticsearch",
            "c4.4xlarge.elasticsearch",
            "c4.8xlarge.elasticsearch",
            "r4.large.elasticsearch",
            "r4.xlarge.elasticsearch",
            "r4.2xlarge.elasticsearch",
            "r4.4xlarge.elasticsearch",
            "r4.8xlarge.elasticsearch",
            "r4.16xlarge.elasticsearch",
            "i3.large.elasticsearch",
            "i3.xlarge.elasticsearch",
            "i3.2xlarge.elasticsearch",
            "i3.4xlarge.elasticsearch",
            "i3.8xlarge.elasticsearch",
            "i3.16xlarge.elasticsearch",
        ],
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ElasticsearchInstanceCount": int,
        "State": str,
        "PaymentOption": Literal["ALL_UPFRONT", "PARTIAL_UPFRONT", "NO_UPFRONT"],
        "RecurringCharges": List[
            DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesRecurringChargesTypeDef
        ],
    },
    total=False,
)


class DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef(
    _DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef
):
    """
    - *(dict) --*

      Details of a reserved Elasticsearch instance.
      - **ReservationName** *(string) --*

        The customer-specified identifier to track this reservation.
    """


_DescribeReservedElasticsearchInstancesPaginateResponseTypeDef = TypedDict(
    "_DescribeReservedElasticsearchInstancesPaginateResponseTypeDef",
    {
        "ReservedElasticsearchInstances": List[
            DescribeReservedElasticsearchInstancesPaginateResponseReservedElasticsearchInstancesTypeDef
        ]
    },
    total=False,
)


class DescribeReservedElasticsearchInstancesPaginateResponseTypeDef(
    _DescribeReservedElasticsearchInstancesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Container for results from ``DescribeReservedElasticsearchInstances``
      - **ReservedElasticsearchInstances** *(list) --*

        List of reserved Elasticsearch instances.
        - *(dict) --*

          Details of a reserved Elasticsearch instance.
          - **ReservationName** *(string) --*

            The customer-specified identifier to track this reservation.
    """


_GetUpgradeHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_GetUpgradeHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetUpgradeHistoryPaginatePaginationConfigTypeDef(
    _GetUpgradeHistoryPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef = TypedDict(
    "_GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef",
    {
        "UpgradeStep": Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"],
        "UpgradeStepStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "Issues": List[str],
        "ProgressPercent": float,
    },
    total=False,
)


class GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef(
    _GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef
):
    pass


_GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef = TypedDict(
    "_GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef",
    {
        "UpgradeName": str,
        "StartTimestamp": datetime,
        "UpgradeStatus": Literal["IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES", "FAILED"],
        "StepsList": List[GetUpgradeHistoryPaginateResponseUpgradeHistoriesStepsListTypeDef],
    },
    total=False,
)


class GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef(
    _GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef
):
    """
    - *(dict) --*

      History of the last 10 Upgrades and Upgrade Eligibility Checks.
      - **UpgradeName** *(string) --*

        A string that describes the update briefly
    """


_GetUpgradeHistoryPaginateResponseTypeDef = TypedDict(
    "_GetUpgradeHistoryPaginateResponseTypeDef",
    {"UpgradeHistories": List[GetUpgradeHistoryPaginateResponseUpgradeHistoriesTypeDef]},
    total=False,
)


class GetUpgradeHistoryPaginateResponseTypeDef(_GetUpgradeHistoryPaginateResponseTypeDef):
    """
    - *(dict) --*

      Container for response returned by ``  GetUpgradeHistory `` operation.
      - **UpgradeHistories** *(list) --*

        A list of ``  UpgradeHistory `` objects corresponding to each Upgrade or Upgrade Eligibility
        Check performed on a domain returned as part of ``  GetUpgradeHistoryResponse `` object.
        - *(dict) --*

          History of the last 10 Upgrades and Upgrade Eligibility Checks.
          - **UpgradeName** *(string) --*

            A string that describes the update briefly
    """


_ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef(
    _ListElasticsearchInstanceTypesPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListElasticsearchInstanceTypesPaginateResponseTypeDef = TypedDict(
    "_ListElasticsearchInstanceTypesPaginateResponseTypeDef",
    {
        "ElasticsearchInstanceTypes": List[
            Literal[
                "m3.medium.elasticsearch",
                "m3.large.elasticsearch",
                "m3.xlarge.elasticsearch",
                "m3.2xlarge.elasticsearch",
                "m4.large.elasticsearch",
                "m4.xlarge.elasticsearch",
                "m4.2xlarge.elasticsearch",
                "m4.4xlarge.elasticsearch",
                "m4.10xlarge.elasticsearch",
                "m5.large.elasticsearch",
                "m5.xlarge.elasticsearch",
                "m5.2xlarge.elasticsearch",
                "m5.4xlarge.elasticsearch",
                "m5.12xlarge.elasticsearch",
                "r5.large.elasticsearch",
                "r5.xlarge.elasticsearch",
                "r5.2xlarge.elasticsearch",
                "r5.4xlarge.elasticsearch",
                "r5.12xlarge.elasticsearch",
                "c5.large.elasticsearch",
                "c5.xlarge.elasticsearch",
                "c5.2xlarge.elasticsearch",
                "c5.4xlarge.elasticsearch",
                "c5.9xlarge.elasticsearch",
                "c5.18xlarge.elasticsearch",
                "t2.micro.elasticsearch",
                "t2.small.elasticsearch",
                "t2.medium.elasticsearch",
                "r3.large.elasticsearch",
                "r3.xlarge.elasticsearch",
                "r3.2xlarge.elasticsearch",
                "r3.4xlarge.elasticsearch",
                "r3.8xlarge.elasticsearch",
                "i2.xlarge.elasticsearch",
                "i2.2xlarge.elasticsearch",
                "d2.xlarge.elasticsearch",
                "d2.2xlarge.elasticsearch",
                "d2.4xlarge.elasticsearch",
                "d2.8xlarge.elasticsearch",
                "c4.large.elasticsearch",
                "c4.xlarge.elasticsearch",
                "c4.2xlarge.elasticsearch",
                "c4.4xlarge.elasticsearch",
                "c4.8xlarge.elasticsearch",
                "r4.large.elasticsearch",
                "r4.xlarge.elasticsearch",
                "r4.2xlarge.elasticsearch",
                "r4.4xlarge.elasticsearch",
                "r4.8xlarge.elasticsearch",
                "r4.16xlarge.elasticsearch",
                "i3.large.elasticsearch",
                "i3.xlarge.elasticsearch",
                "i3.2xlarge.elasticsearch",
                "i3.4xlarge.elasticsearch",
                "i3.8xlarge.elasticsearch",
                "i3.16xlarge.elasticsearch",
            ]
        ]
    },
    total=False,
)


class ListElasticsearchInstanceTypesPaginateResponseTypeDef(
    _ListElasticsearchInstanceTypesPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Container for the parameters returned by ``  ListElasticsearchInstanceTypes `` operation.
      - **ElasticsearchInstanceTypes** *(list) --*

        List of instance types supported by Amazon Elasticsearch service for given ``
        ElasticsearchVersion ``
        - *(string) --*
    """


_ListElasticsearchVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListElasticsearchVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListElasticsearchVersionsPaginatePaginationConfigTypeDef(
    _ListElasticsearchVersionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListElasticsearchVersionsPaginateResponseTypeDef = TypedDict(
    "_ListElasticsearchVersionsPaginateResponseTypeDef",
    {"ElasticsearchVersions": List[str]},
    total=False,
)


class ListElasticsearchVersionsPaginateResponseTypeDef(
    _ListElasticsearchVersionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      Container for the parameters for response received from ``  ListElasticsearchVersions ``
      operation.
      - **ElasticsearchVersions** *(list) --*

        List of supported elastic search versions.
        - *(string) --*
    """
