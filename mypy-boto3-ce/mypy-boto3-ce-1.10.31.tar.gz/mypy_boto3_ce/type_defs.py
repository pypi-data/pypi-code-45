"Main interface for ce service type defs"
from __future__ import annotations

from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateCostCategoryDefinitionResponseTypeDef",
    "ClientCreateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef",
    "ClientCreateCostCategoryDefinitionRulesRuleDimensionsTypeDef",
    "ClientCreateCostCategoryDefinitionRulesRuleTagsTypeDef",
    "ClientCreateCostCategoryDefinitionRulesRuleTypeDef",
    "ClientCreateCostCategoryDefinitionRulesTypeDef",
    "ClientDeleteCostCategoryDefinitionResponseTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleCostCategoriesTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleDimensionsTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTagsTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseCostCategoryTypeDef",
    "ClientDescribeCostCategoryDefinitionResponseTypeDef",
    "ClientGetCostAndUsageFilterCostCategoriesTypeDef",
    "ClientGetCostAndUsageFilterDimensionsTypeDef",
    "ClientGetCostAndUsageFilterTagsTypeDef",
    "ClientGetCostAndUsageFilterTypeDef",
    "ClientGetCostAndUsageGroupByTypeDef",
    "ClientGetCostAndUsageResponseGroupDefinitionsTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef",
    "ClientGetCostAndUsageResponseResultsByTimeTypeDef",
    "ClientGetCostAndUsageResponseTypeDef",
    "ClientGetCostAndUsageTimePeriodTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterCostCategoriesTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterTagsTypeDef",
    "ClientGetCostAndUsageWithResourcesFilterTypeDef",
    "ClientGetCostAndUsageWithResourcesGroupByTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef",
    "ClientGetCostAndUsageWithResourcesResponseTypeDef",
    "ClientGetCostAndUsageWithResourcesTimePeriodTypeDef",
    "ClientGetCostForecastFilterCostCategoriesTypeDef",
    "ClientGetCostForecastFilterDimensionsTypeDef",
    "ClientGetCostForecastFilterTagsTypeDef",
    "ClientGetCostForecastFilterTypeDef",
    "ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    "ClientGetCostForecastResponseForecastResultsByTimeTypeDef",
    "ClientGetCostForecastResponseTotalTypeDef",
    "ClientGetCostForecastResponseTypeDef",
    "ClientGetCostForecastTimePeriodTypeDef",
    "ClientGetDimensionValuesResponseDimensionValuesTypeDef",
    "ClientGetDimensionValuesResponseTypeDef",
    "ClientGetDimensionValuesTimePeriodTypeDef",
    "ClientGetReservationCoverageFilterCostCategoriesTypeDef",
    "ClientGetReservationCoverageFilterDimensionsTypeDef",
    "ClientGetReservationCoverageFilterTagsTypeDef",
    "ClientGetReservationCoverageFilterTypeDef",
    "ClientGetReservationCoverageGroupByTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef",
    "ClientGetReservationCoverageResponseCoveragesByTimeTypeDef",
    "ClientGetReservationCoverageResponseTotalCoverageCostTypeDef",
    "ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef",
    "ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef",
    "ClientGetReservationCoverageResponseTotalTypeDef",
    "ClientGetReservationCoverageResponseTypeDef",
    "ClientGetReservationCoverageTimePeriodTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef",
    "ClientGetReservationPurchaseRecommendationResponseTypeDef",
    "ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef",
    "ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef",
    "ClientGetReservationUtilizationFilterCostCategoriesTypeDef",
    "ClientGetReservationUtilizationFilterDimensionsTypeDef",
    "ClientGetReservationUtilizationFilterTagsTypeDef",
    "ClientGetReservationUtilizationFilterTypeDef",
    "ClientGetReservationUtilizationGroupByTypeDef",
    "ClientGetReservationUtilizationResponseTotalTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef",
    "ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef",
    "ClientGetReservationUtilizationResponseTypeDef",
    "ClientGetReservationUtilizationTimePeriodTypeDef",
    "ClientGetRightsizingRecommendationFilterCostCategoriesTypeDef",
    "ClientGetRightsizingRecommendationFilterDimensionsTypeDef",
    "ClientGetRightsizingRecommendationFilterTagsTypeDef",
    "ClientGetRightsizingRecommendationFilterTypeDef",
    "ClientGetRightsizingRecommendationResponseMetadataTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef",
    "ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef",
    "ClientGetRightsizingRecommendationResponseSummaryTypeDef",
    "ClientGetRightsizingRecommendationResponseTypeDef",
    "ClientGetSavingsPlansCoverageFilterCostCategoriesTypeDef",
    "ClientGetSavingsPlansCoverageFilterDimensionsTypeDef",
    "ClientGetSavingsPlansCoverageFilterTagsTypeDef",
    "ClientGetSavingsPlansCoverageFilterTypeDef",
    "ClientGetSavingsPlansCoverageGroupByTypeDef",
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef",
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef",
    "ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef",
    "ClientGetSavingsPlansCoverageResponseTypeDef",
    "ClientGetSavingsPlansCoverageTimePeriodTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef",
    "ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterCostCategoriesTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsFilterTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsResponseTypeDef",
    "ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef",
    "ClientGetSavingsPlansUtilizationFilterCostCategoriesTypeDef",
    "ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef",
    "ClientGetSavingsPlansUtilizationFilterTagsTypeDef",
    "ClientGetSavingsPlansUtilizationFilterTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTotalTypeDef",
    "ClientGetSavingsPlansUtilizationResponseTypeDef",
    "ClientGetSavingsPlansUtilizationTimePeriodTypeDef",
    "ClientGetTagsResponseTypeDef",
    "ClientGetTagsTimePeriodTypeDef",
    "ClientGetUsageForecastFilterCostCategoriesTypeDef",
    "ClientGetUsageForecastFilterDimensionsTypeDef",
    "ClientGetUsageForecastFilterTagsTypeDef",
    "ClientGetUsageForecastFilterTypeDef",
    "ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    "ClientGetUsageForecastResponseForecastResultsByTimeTypeDef",
    "ClientGetUsageForecastResponseTotalTypeDef",
    "ClientGetUsageForecastResponseTypeDef",
    "ClientGetUsageForecastTimePeriodTypeDef",
    "ClientListCostCategoryDefinitionsResponseCostCategoryReferencesTypeDef",
    "ClientListCostCategoryDefinitionsResponseTypeDef",
    "ClientUpdateCostCategoryDefinitionResponseTypeDef",
    "ClientUpdateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef",
    "ClientUpdateCostCategoryDefinitionRulesRuleDimensionsTypeDef",
    "ClientUpdateCostCategoryDefinitionRulesRuleTagsTypeDef",
    "ClientUpdateCostCategoryDefinitionRulesRuleTypeDef",
    "ClientUpdateCostCategoryDefinitionRulesTypeDef",
)


_ClientCreateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "_ClientCreateCostCategoryDefinitionResponseTypeDef",
    {"CostCategoryArn": str, "EffectiveStart": str},
    total=False,
)


class ClientCreateCostCategoryDefinitionResponseTypeDef(
    _ClientCreateCostCategoryDefinitionResponseTypeDef
):
    """
    - *(dict) --*

      - **CostCategoryArn** *(string) --*

        The unique identifier for your newly created Cost Category.
    """


_ClientCreateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef = TypedDict(
    "_ClientCreateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef(
    _ClientCreateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef
):
    pass


_ClientCreateCostCategoryDefinitionRulesRuleDimensionsTypeDef = TypedDict(
    "_ClientCreateCostCategoryDefinitionRulesRuleDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientCreateCostCategoryDefinitionRulesRuleDimensionsTypeDef(
    _ClientCreateCostCategoryDefinitionRulesRuleDimensionsTypeDef
):
    pass


_ClientCreateCostCategoryDefinitionRulesRuleTagsTypeDef = TypedDict(
    "_ClientCreateCostCategoryDefinitionRulesRuleTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientCreateCostCategoryDefinitionRulesRuleTagsTypeDef(
    _ClientCreateCostCategoryDefinitionRulesRuleTagsTypeDef
):
    pass


_ClientCreateCostCategoryDefinitionRulesRuleTypeDef = TypedDict(
    "_ClientCreateCostCategoryDefinitionRulesRuleTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientCreateCostCategoryDefinitionRulesRuleDimensionsTypeDef,
        "Tags": ClientCreateCostCategoryDefinitionRulesRuleTagsTypeDef,
        "CostCategories": ClientCreateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef,
    },
    total=False,
)


class ClientCreateCostCategoryDefinitionRulesRuleTypeDef(
    _ClientCreateCostCategoryDefinitionRulesRuleTypeDef
):
    pass


_ClientCreateCostCategoryDefinitionRulesTypeDef = TypedDict(
    "_ClientCreateCostCategoryDefinitionRulesTypeDef",
    {"Value": str, "Rule": ClientCreateCostCategoryDefinitionRulesRuleTypeDef},
    total=False,
)


class ClientCreateCostCategoryDefinitionRulesTypeDef(
    _ClientCreateCostCategoryDefinitionRulesTypeDef
):
    """
    - *(dict) --*

      .. warning::

        * **Cost Category is in preview release for AWS Billing and Cost Management and is subject
        to change. Your use of Cost Categories is subject to the Beta Service Participation terms of
        the `AWS Service Terms <https://aws.amazon.com/service-terms/>`__ (Section 1.10).** *
    """


_ClientDeleteCostCategoryDefinitionResponseTypeDef = TypedDict(
    "_ClientDeleteCostCategoryDefinitionResponseTypeDef",
    {"CostCategoryArn": str, "EffectiveEnd": str},
    total=False,
)


class ClientDeleteCostCategoryDefinitionResponseTypeDef(
    _ClientDeleteCostCategoryDefinitionResponseTypeDef
):
    """
    - *(dict) --*

      - **CostCategoryArn** *(string) --*

        The unique identifier for your Cost Category.
    """


_ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleCostCategoriesTypeDef = TypedDict(
    "_ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleCostCategoriesTypeDef(
    _ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleCostCategoriesTypeDef
):
    pass


_ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleDimensionsTypeDef = TypedDict(
    "_ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleDimensionsTypeDef(
    _ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleDimensionsTypeDef
):
    pass


_ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTagsTypeDef = TypedDict(
    "_ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTagsTypeDef(
    _ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTagsTypeDef
):
    pass


_ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTypeDef = TypedDict(
    "_ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleDimensionsTypeDef,
        "Tags": ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTagsTypeDef,
        "CostCategories": ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleCostCategoriesTypeDef,
    },
    total=False,
)


class ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTypeDef(
    _ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTypeDef
):
    pass


_ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesTypeDef = TypedDict(
    "_ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesTypeDef",
    {
        "Value": str,
        "Rule": ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesRuleTypeDef,
    },
    total=False,
)


class ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesTypeDef(
    _ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesTypeDef
):
    pass


_ClientDescribeCostCategoryDefinitionResponseCostCategoryTypeDef = TypedDict(
    "_ClientDescribeCostCategoryDefinitionResponseCostCategoryTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "EffectiveEnd": str,
        "Name": str,
        "RuleVersion": str,
        "Rules": List[ClientDescribeCostCategoryDefinitionResponseCostCategoryRulesTypeDef],
    },
    total=False,
)


class ClientDescribeCostCategoryDefinitionResponseCostCategoryTypeDef(
    _ClientDescribeCostCategoryDefinitionResponseCostCategoryTypeDef
):
    """
    - **CostCategory** *(dict) --*

      .. warning::

        * **Cost Category is in preview release for AWS Billing and Cost Management and is subject
        to change. Your use of Cost Categories is subject to the Beta Service Participation terms of
        the `AWS Service Terms <https://aws.amazon.com/service-terms/>`__ (Section 1.10).** *
    """


_ClientDescribeCostCategoryDefinitionResponseTypeDef = TypedDict(
    "_ClientDescribeCostCategoryDefinitionResponseTypeDef",
    {"CostCategory": ClientDescribeCostCategoryDefinitionResponseCostCategoryTypeDef},
    total=False,
)


class ClientDescribeCostCategoryDefinitionResponseTypeDef(
    _ClientDescribeCostCategoryDefinitionResponseTypeDef
):
    """
    - *(dict) --*

      - **CostCategory** *(dict) --*

        .. warning::

          * **Cost Category is in preview release for AWS Billing and Cost Management and is subject
          to change. Your use of Cost Categories is subject to the Beta Service Participation terms
          of the `AWS Service Terms <https://aws.amazon.com/service-terms/>`__ (Section 1.10).** *
    """


_ClientGetCostAndUsageFilterCostCategoriesTypeDef = TypedDict(
    "_ClientGetCostAndUsageFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetCostAndUsageFilterCostCategoriesTypeDef(
    _ClientGetCostAndUsageFilterCostCategoriesTypeDef
):
    pass


_ClientGetCostAndUsageFilterDimensionsTypeDef = TypedDict(
    "_ClientGetCostAndUsageFilterDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetCostAndUsageFilterDimensionsTypeDef(_ClientGetCostAndUsageFilterDimensionsTypeDef):
    pass


_ClientGetCostAndUsageFilterTagsTypeDef = TypedDict(
    "_ClientGetCostAndUsageFilterTagsTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientGetCostAndUsageFilterTagsTypeDef(_ClientGetCostAndUsageFilterTagsTypeDef):
    pass


_ClientGetCostAndUsageFilterTypeDef = TypedDict(
    "_ClientGetCostAndUsageFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetCostAndUsageFilterDimensionsTypeDef,
        "Tags": ClientGetCostAndUsageFilterTagsTypeDef,
        "CostCategories": ClientGetCostAndUsageFilterCostCategoriesTypeDef,
    },
    total=False,
)


class ClientGetCostAndUsageFilterTypeDef(_ClientGetCostAndUsageFilterTypeDef):
    """
    Filters AWS costs by different dimensions. For example, you can specify ``SERVICE`` and
    ``LINKED_ACCOUNT`` and get the costs that are associated with that account's usage of that
    service. You can nest ``Expression`` objects to define any combination of dimension filters. For
    more information, see `Expression
    <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__ .
    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.
      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:
        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==
            us-west-1``
        . The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION",
        "Values": [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd
        together to retrieve cost or usage data. You can create ``Expression`` and
        ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple
        lines.
        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more
        ``Expression`` objects. This allows you to filter on more advanced options. For example, you
        can filter on ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type ==
             Type1)) AND
        (USAGE_TYPE !=
             DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [
        {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }},
        {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key":
        "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }``
        .. note::

          Because each ``Expression`` can have only one operator, the service returns an error if
          more than one is specified. The following example shows an ``Expression`` object that
          creates an error.
          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``
    """


_ClientGetCostAndUsageGroupByTypeDef = TypedDict(
    "_ClientGetCostAndUsageGroupByTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)


class ClientGetCostAndUsageGroupByTypeDef(_ClientGetCostAndUsageGroupByTypeDef):
    """
    - *(dict) --*

      Represents a group when you specify a group by criteria or in the response to a query with a
      specific grouping.
      - **Type** *(string) --*

        The string that represents the type of group.
    """


_ClientGetCostAndUsageResponseGroupDefinitionsTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseGroupDefinitionsTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)


class ClientGetCostAndUsageResponseGroupDefinitionsTypeDef(
    _ClientGetCostAndUsageResponseGroupDefinitionsTypeDef
):
    pass


_ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef(
    _ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef
):
    pass


_ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef",
    {
        "Keys": List[str],
        "Metrics": Dict[str, ClientGetCostAndUsageResponseResultsByTimeGroupsMetricsTypeDef],
    },
    total=False,
)


class ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef(
    _ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef
):
    pass


_ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef(
    _ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef
):
    pass


_ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef(
    _ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef
):
    pass


_ClientGetCostAndUsageResponseResultsByTimeTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetCostAndUsageResponseResultsByTimeTimePeriodTypeDef,
        "Total": Dict[str, ClientGetCostAndUsageResponseResultsByTimeTotalTypeDef],
        "Groups": List[ClientGetCostAndUsageResponseResultsByTimeGroupsTypeDef],
        "Estimated": bool,
    },
    total=False,
)


class ClientGetCostAndUsageResponseResultsByTimeTypeDef(
    _ClientGetCostAndUsageResponseResultsByTimeTypeDef
):
    pass


_ClientGetCostAndUsageResponseTypeDef = TypedDict(
    "_ClientGetCostAndUsageResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List[ClientGetCostAndUsageResponseGroupDefinitionsTypeDef],
        "ResultsByTime": List[ClientGetCostAndUsageResponseResultsByTimeTypeDef],
    },
    total=False,
)


class ClientGetCostAndUsageResponseTypeDef(_ClientGetCostAndUsageResponseTypeDef):
    """
    - *(dict) --*

      - **NextPageToken** *(string) --*

        The token for the next set of retrievable results. AWS provides the token when the response
        from a previous call has more results than the maximum page size.
    """


_RequiredClientGetCostAndUsageTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetCostAndUsageTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetCostAndUsageTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetCostAndUsageTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetCostAndUsageTimePeriodTypeDef(
    _RequiredClientGetCostAndUsageTimePeriodTypeDef, _OptionalClientGetCostAndUsageTimePeriodTypeDef
):
    """
    Sets the start and end dates for retrieving AWS costs. The start date is inclusive, but the end
    date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01`` ,
    then the cost and usage data is retrieved from ``2017-01-01`` up to and including ``2017-04-30``
    but not including ``2017-05-01`` .
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientGetCostAndUsageWithResourcesFilterCostCategoriesTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetCostAndUsageWithResourcesFilterCostCategoriesTypeDef(
    _ClientGetCostAndUsageWithResourcesFilterCostCategoriesTypeDef
):
    pass


_ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef(
    _ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef
):
    pass


_ClientGetCostAndUsageWithResourcesFilterTagsTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetCostAndUsageWithResourcesFilterTagsTypeDef(
    _ClientGetCostAndUsageWithResourcesFilterTagsTypeDef
):
    pass


_ClientGetCostAndUsageWithResourcesFilterTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetCostAndUsageWithResourcesFilterDimensionsTypeDef,
        "Tags": ClientGetCostAndUsageWithResourcesFilterTagsTypeDef,
        "CostCategories": ClientGetCostAndUsageWithResourcesFilterCostCategoriesTypeDef,
    },
    total=False,
)


class ClientGetCostAndUsageWithResourcesFilterTypeDef(
    _ClientGetCostAndUsageWithResourcesFilterTypeDef
):
    """
    Filters Amazon Web Services costs by different dimensions. For example, you can specify
    ``SERVICE`` and ``LINKED_ACCOUNT`` and get the costs that are associated with that account's
    usage of that service. You can nest ``Expression`` objects to define any combination of
    dimension filters. For more information, see `Expression
    <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__ .
    The ``GetCostAndUsageWithResources`` operation requires that you either group by or filter by a
    ``ResourceId`` .
    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.
      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:
        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==
            us-west-1``
        . The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION",
        "Values": [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd
        together to retrieve cost or usage data. You can create ``Expression`` and
        ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple
        lines.
        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more
        ``Expression`` objects. This allows you to filter on more advanced options. For example, you
        can filter on ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type ==
             Type1)) AND
        (USAGE_TYPE !=
             DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [
        {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }},
        {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key":
        "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }``
        .. note::

          Because each ``Expression`` can have only one operator, the service returns an error if
          more than one is specified. The following example shows an ``Expression`` object that
          creates an error.
          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``
    """


_ClientGetCostAndUsageWithResourcesGroupByTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesGroupByTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)


class ClientGetCostAndUsageWithResourcesGroupByTypeDef(
    _ClientGetCostAndUsageWithResourcesGroupByTypeDef
):
    """
    - *(dict) --*

      Represents a group when you specify a group by criteria or in the response to a query with a
      specific grouping.
      - **Type** *(string) --*

        The string that represents the type of group.
    """


_ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef
):
    pass


_ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef
):
    pass


_ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef",
    {
        "Keys": List[str],
        "Metrics": Dict[
            str, ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsMetricsTypeDef
        ],
    },
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef
):
    pass


_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef
):
    pass


_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef",
    {"Amount": str, "Unit": str},
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef
):
    pass


_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetCostAndUsageWithResourcesResponseResultsByTimeTimePeriodTypeDef,
        "Total": Dict[str, ClientGetCostAndUsageWithResourcesResponseResultsByTimeTotalTypeDef],
        "Groups": List[ClientGetCostAndUsageWithResourcesResponseResultsByTimeGroupsTypeDef],
        "Estimated": bool,
    },
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef
):
    pass


_ClientGetCostAndUsageWithResourcesResponseTypeDef = TypedDict(
    "_ClientGetCostAndUsageWithResourcesResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List[ClientGetCostAndUsageWithResourcesResponseGroupDefinitionsTypeDef],
        "ResultsByTime": List[ClientGetCostAndUsageWithResourcesResponseResultsByTimeTypeDef],
    },
    total=False,
)


class ClientGetCostAndUsageWithResourcesResponseTypeDef(
    _ClientGetCostAndUsageWithResourcesResponseTypeDef
):
    """
    - *(dict) --*

      - **NextPageToken** *(string) --*

        The token for the next set of retrievable results. AWS provides the token when the response
        from a previous call has more results than the maximum page size.
    """


_RequiredClientGetCostAndUsageWithResourcesTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetCostAndUsageWithResourcesTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetCostAndUsageWithResourcesTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetCostAndUsageWithResourcesTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetCostAndUsageWithResourcesTimePeriodTypeDef(
    _RequiredClientGetCostAndUsageWithResourcesTimePeriodTypeDef,
    _OptionalClientGetCostAndUsageWithResourcesTimePeriodTypeDef,
):
    """
    Sets the start and end dates for retrieving Amazon Web Services costs. The range must be within
    the last 14 days (the start date cannot be earlier than 14 days ago). The start date is
    inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and
    ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to
    and including ``2017-04-30`` but not including ``2017-05-01`` .
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientGetCostForecastFilterCostCategoriesTypeDef = TypedDict(
    "_ClientGetCostForecastFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetCostForecastFilterCostCategoriesTypeDef(
    _ClientGetCostForecastFilterCostCategoriesTypeDef
):
    pass


_ClientGetCostForecastFilterDimensionsTypeDef = TypedDict(
    "_ClientGetCostForecastFilterDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetCostForecastFilterDimensionsTypeDef(_ClientGetCostForecastFilterDimensionsTypeDef):
    pass


_ClientGetCostForecastFilterTagsTypeDef = TypedDict(
    "_ClientGetCostForecastFilterTagsTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientGetCostForecastFilterTagsTypeDef(_ClientGetCostForecastFilterTagsTypeDef):
    pass


_ClientGetCostForecastFilterTypeDef = TypedDict(
    "_ClientGetCostForecastFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetCostForecastFilterDimensionsTypeDef,
        "Tags": ClientGetCostForecastFilterTagsTypeDef,
        "CostCategories": ClientGetCostForecastFilterCostCategoriesTypeDef,
    },
    total=False,
)


class ClientGetCostForecastFilterTypeDef(_ClientGetCostForecastFilterTypeDef):
    """
    The filters that you want to use to filter your forecast. Cost Explorer API supports all of the
    Cost Explorer filters.
    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.
      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:
        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==
            us-west-1``
        . The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION",
        "Values": [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd
        together to retrieve cost or usage data. You can create ``Expression`` and
        ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple
        lines.
        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more
        ``Expression`` objects. This allows you to filter on more advanced options. For example, you
        can filter on ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type ==
             Type1)) AND
        (USAGE_TYPE !=
             DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [
        {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }},
        {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key":
        "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }``
        .. note::

          Because each ``Expression`` can have only one operator, the service returns an error if
          more than one is specified. The following example shows an ``Expression`` object that
          creates an error.
          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``
    """


_ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef(
    _ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef
):
    pass


_ClientGetCostForecastResponseForecastResultsByTimeTypeDef = TypedDict(
    "_ClientGetCostForecastResponseForecastResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetCostForecastResponseForecastResultsByTimeTimePeriodTypeDef,
        "MeanValue": str,
        "PredictionIntervalLowerBound": str,
        "PredictionIntervalUpperBound": str,
    },
    total=False,
)


class ClientGetCostForecastResponseForecastResultsByTimeTypeDef(
    _ClientGetCostForecastResponseForecastResultsByTimeTypeDef
):
    pass


_ClientGetCostForecastResponseTotalTypeDef = TypedDict(
    "_ClientGetCostForecastResponseTotalTypeDef", {"Amount": str, "Unit": str}, total=False
)


class ClientGetCostForecastResponseTotalTypeDef(_ClientGetCostForecastResponseTotalTypeDef):
    """
    - **Total** *(dict) --*

      How much you are forecasted to spend over the forecast period, in ``USD`` .
      - **Amount** *(string) --*

        The actual number that represents the metric.
    """


_ClientGetCostForecastResponseTypeDef = TypedDict(
    "_ClientGetCostForecastResponseTypeDef",
    {
        "Total": ClientGetCostForecastResponseTotalTypeDef,
        "ForecastResultsByTime": List[ClientGetCostForecastResponseForecastResultsByTimeTypeDef],
    },
    total=False,
)


class ClientGetCostForecastResponseTypeDef(_ClientGetCostForecastResponseTypeDef):
    """
    - *(dict) --*

      - **Total** *(dict) --*

        How much you are forecasted to spend over the forecast period, in ``USD`` .
        - **Amount** *(string) --*

          The actual number that represents the metric.
    """


_RequiredClientGetCostForecastTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetCostForecastTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetCostForecastTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetCostForecastTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetCostForecastTimePeriodTypeDef(
    _RequiredClientGetCostForecastTimePeriodTypeDef, _OptionalClientGetCostForecastTimePeriodTypeDef
):
    """
    The period of time that you want the forecast to cover.
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientGetDimensionValuesResponseDimensionValuesTypeDef = TypedDict(
    "_ClientGetDimensionValuesResponseDimensionValuesTypeDef",
    {"Value": str, "Attributes": Dict[str, str]},
    total=False,
)


class ClientGetDimensionValuesResponseDimensionValuesTypeDef(
    _ClientGetDimensionValuesResponseDimensionValuesTypeDef
):
    """
    - *(dict) --*

      The metadata of a specific type that you can use to filter and group your results. You can use
      ``GetDimensionValues`` to find specific values.
      - **Value** *(string) --*

        The value of a dimension with a specific attribute.
    """


_ClientGetDimensionValuesResponseTypeDef = TypedDict(
    "_ClientGetDimensionValuesResponseTypeDef",
    {
        "DimensionValues": List[ClientGetDimensionValuesResponseDimensionValuesTypeDef],
        "ReturnSize": int,
        "TotalSize": int,
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetDimensionValuesResponseTypeDef(_ClientGetDimensionValuesResponseTypeDef):
    """
    - *(dict) --*

      - **DimensionValues** *(list) --*

        The filters that you used to filter your request. Some dimensions are available only for a
        specific context.
        If you set the context to ``COST_AND_USAGE`` , you can use the following dimensions for
        searching:
        * AZ - The Availability Zone. An example is ``us-east-1a`` .
        * DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or
        MySQL.
        * INSTANCE_TYPE - The type of Amazon EC2 instance. An example is ``m4.xlarge`` .
        * LEGAL_ENTITY_NAME - The name of the organization that sells you AWS services, such as
        Amazon Web Services.
        * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the
        member account. The value field contains the AWS ID of the member account.
        * OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.
        * OPERATION - The action performed. Examples include ``RunInstance`` and ``CreateBucket`` .
        * PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
        * PURCHASE_TYPE - The reservation type of the purchase to which this usage is related.
        Examples include On-Demand Instances and Standard Reserved Instances.
        * SERVICE - The AWS service such as Amazon DynamoDB.
        * USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the
        ``GetDimensionValues`` operation includes a unit attribute. Examples include GB and Hrs.
        * USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2:
        CloudWatch – Alarms. The response for this operation includes a unit attribute.
        * RECORD_TYPE - The different types of charges such as RI fees, usage costs, tax refunds,
        and credits.
        * RESOURCE_ID - The unique identifier of the resource. ResourceId is an opt-in feature only
        available for last 14 days for EC2-Compute Service.
        If you set the context to ``RESERVATIONS`` , you can use the following dimensions for
        searching:
        * AZ - The Availability Zone. An example is ``us-east-1a`` .
        * CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.
        * DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid
        values are ``SingleAZ`` and ``MultiAZ`` .
        * INSTANCE_TYPE - The type of Amazon EC2 instance. An example is ``m4.xlarge`` .
        * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the
        member account. The value field contains the AWS ID of the member account.
        * PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.
        * REGION - The AWS Region.
        * SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a
        single Availability Zone.
        * TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).
        * TENANCY - The tenancy of a resource. Examples are shared or dedicated.
        If you set the context to ``SAVINGS_PLANS`` , you can use the following dimensions for
        searching:
        * SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute)
        * PAYMENT_OPTION - Payment option for the given Savings Plans (for example, All Upfront)
        * REGION - The AWS Region.
        * INSTANCE_TYPE_FAMILY - The family of instances (For example, ``m5`` )
        * LINKED_ACCOUNT - The description in the attribute map that includes the full name of the
        member account. The value field contains the AWS ID of the member account.
        * SAVINGS_PLAN_ARN - The unique identifier for your Savings Plan
        - *(dict) --*

          The metadata of a specific type that you can use to filter and group your results. You can
          use ``GetDimensionValues`` to find specific values.
          - **Value** *(string) --*

            The value of a dimension with a specific attribute.
    """


_RequiredClientGetDimensionValuesTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetDimensionValuesTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetDimensionValuesTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetDimensionValuesTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetDimensionValuesTimePeriodTypeDef(
    _RequiredClientGetDimensionValuesTimePeriodTypeDef,
    _OptionalClientGetDimensionValuesTimePeriodTypeDef,
):
    """
    The start and end dates for retrieving the dimension values. The start date is inclusive, but
    the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is
    ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and
    including ``2017-04-30`` but not including ``2017-05-01`` .
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientGetReservationCoverageFilterCostCategoriesTypeDef = TypedDict(
    "_ClientGetReservationCoverageFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetReservationCoverageFilterCostCategoriesTypeDef(
    _ClientGetReservationCoverageFilterCostCategoriesTypeDef
):
    pass


_ClientGetReservationCoverageFilterDimensionsTypeDef = TypedDict(
    "_ClientGetReservationCoverageFilterDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetReservationCoverageFilterDimensionsTypeDef(
    _ClientGetReservationCoverageFilterDimensionsTypeDef
):
    pass


_ClientGetReservationCoverageFilterTagsTypeDef = TypedDict(
    "_ClientGetReservationCoverageFilterTagsTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientGetReservationCoverageFilterTagsTypeDef(_ClientGetReservationCoverageFilterTagsTypeDef):
    pass


_ClientGetReservationCoverageFilterTypeDef = TypedDict(
    "_ClientGetReservationCoverageFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetReservationCoverageFilterDimensionsTypeDef,
        "Tags": ClientGetReservationCoverageFilterTagsTypeDef,
        "CostCategories": ClientGetReservationCoverageFilterCostCategoriesTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageFilterTypeDef(_ClientGetReservationCoverageFilterTypeDef):
    """
    Filters utilization data by dimensions. You can filter by the following dimensions:
    * AZ
    * CACHE_ENGINE
    * DATABASE_ENGINE
    * DEPLOYMENT_OPTION
    * INSTANCE_TYPE
    * LINKED_ACCOUNT
    * OPERATING_SYSTEM
    * PLATFORM
    * REGION
    * SERVICE
    * TAG
    * TENANCY

      ``GetReservationCoverage`` uses the same `Expression
      <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__
      object as the other operations, but only ``AND`` is supported among each dimension. You can
      nest only one level deep. If there are multiple values for a dimension, they are OR'd
      together.
    """


_ClientGetReservationCoverageGroupByTypeDef = TypedDict(
    "_ClientGetReservationCoverageGroupByTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)


class ClientGetReservationCoverageGroupByTypeDef(_ClientGetReservationCoverageGroupByTypeDef):
    """
    - *(dict) --*

      Represents a group when you specify a group by criteria or in the response to a query with a
      specific grouping.
      - **Type** *(string) --*

        The string that represents the type of group.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef",
    {"OnDemandCost": str},
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef
):
    pass


_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef
):
    pass


_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef
):
    pass


_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef",
    {
        "CoverageHours": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageHoursTypeDef,
        "CoverageNormalizedUnits": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageNormalizedUnitsTypeDef,
        "CoverageCost": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageCoverageCostTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef
):
    pass


_ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": ClientGetReservationCoverageResponseCoveragesByTimeGroupsCoverageTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef
):
    pass


_ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef
):
    """
    - **TimePeriod** *(dict) --*

      The period that this coverage was used over.
      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date is
        inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
        starting at ``2017-01-01`` up to the end date.
    """


_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef",
    {"OnDemandCost": str},
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef
):
    pass


_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef
):
    pass


_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef
):
    pass


_ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef",
    {
        "CoverageHours": ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageHoursTypeDef,
        "CoverageNormalizedUnits": ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageNormalizedUnitsTypeDef,
        "CoverageCost": ClientGetReservationCoverageResponseCoveragesByTimeTotalCoverageCostTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef
):
    pass


_ClientGetReservationCoverageResponseCoveragesByTimeTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseCoveragesByTimeTypeDef",
    {
        "TimePeriod": ClientGetReservationCoverageResponseCoveragesByTimeTimePeriodTypeDef,
        "Groups": List[ClientGetReservationCoverageResponseCoveragesByTimeGroupsTypeDef],
        "Total": ClientGetReservationCoverageResponseCoveragesByTimeTotalTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageResponseCoveragesByTimeTypeDef(
    _ClientGetReservationCoverageResponseCoveragesByTimeTypeDef
):
    """
    - *(dict) --*

      Reservation coverage for a specified period, in hours.
      - **TimePeriod** *(dict) --*

        The period that this coverage was used over.
        - **Start** *(string) --*

          The beginning of the time period that you want the usage and costs for. The start date is
          inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
          starting at ``2017-01-01`` up to the end date.
    """


_ClientGetReservationCoverageResponseTotalCoverageCostTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseTotalCoverageCostTypeDef",
    {"OnDemandCost": str},
    total=False,
)


class ClientGetReservationCoverageResponseTotalCoverageCostTypeDef(
    _ClientGetReservationCoverageResponseTotalCoverageCostTypeDef
):
    pass


_ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef(
    _ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef
):
    pass


_ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef(
    _ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef
):
    pass


_ClientGetReservationCoverageResponseTotalTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseTotalTypeDef",
    {
        "CoverageHours": ClientGetReservationCoverageResponseTotalCoverageHoursTypeDef,
        "CoverageNormalizedUnits": ClientGetReservationCoverageResponseTotalCoverageNormalizedUnitsTypeDef,
        "CoverageCost": ClientGetReservationCoverageResponseTotalCoverageCostTypeDef,
    },
    total=False,
)


class ClientGetReservationCoverageResponseTotalTypeDef(
    _ClientGetReservationCoverageResponseTotalTypeDef
):
    pass


_ClientGetReservationCoverageResponseTypeDef = TypedDict(
    "_ClientGetReservationCoverageResponseTypeDef",
    {
        "CoveragesByTime": List[ClientGetReservationCoverageResponseCoveragesByTimeTypeDef],
        "Total": ClientGetReservationCoverageResponseTotalTypeDef,
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetReservationCoverageResponseTypeDef(_ClientGetReservationCoverageResponseTypeDef):
    """
    - *(dict) --*

      - **CoveragesByTime** *(list) --*

        The amount of time that your reservations covered.
        - *(dict) --*

          Reservation coverage for a specified period, in hours.
          - **TimePeriod** *(dict) --*

            The period that this coverage was used over.
            - **Start** *(string) --*

              The beginning of the time period that you want the usage and costs for. The start date
              is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
              usage data starting at ``2017-01-01`` up to the end date.
    """


_RequiredClientGetReservationCoverageTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetReservationCoverageTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetReservationCoverageTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetReservationCoverageTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetReservationCoverageTimePeriodTypeDef(
    _RequiredClientGetReservationCoverageTimePeriodTypeDef,
    _OptionalClientGetReservationCoverageTimePeriodTypeDef,
):
    """
    The start and end dates of the period that you want to retrieve data about reservation coverage
    for. You can retrieve data for a maximum of 13 months: the last 12 months and the current month.
    The start date is inclusive, but the end date is exclusive. For example, if ``start`` is
    ``2017-01-01`` and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from
    ``2017-01-01`` up to and including ``2017-04-30`` but not including ``2017-05-01`` .
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef",
    {"RecommendationId": str, "GenerationTimestamp": str},
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef
):
    """
    - **Metadata** *(dict) --*

      Information about this specific recommendation call, such as the time stamp for when Cost
      Explorer generated this recommendation.
      - **RecommendationId** *(string) --*

        The ID for this specific recommendation.
    """


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "AvailabilityZone": str,
        "Platform": str,
        "Tenancy": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef",
    {
        "InstanceClass": str,
        "InstanceSize": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "ProductDescription": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "DatabaseEngine": str,
        "DatabaseEdition": str,
        "DeploymentOption": str,
        "LicenseModel": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef",
    {
        "EC2InstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsEC2InstanceDetailsTypeDef,
        "RDSInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRDSInstanceDetailsTypeDef,
        "RedshiftInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsRedshiftInstanceDetailsTypeDef,
        "ElastiCacheInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsElastiCacheInstanceDetailsTypeDef,
        "ESInstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsESInstanceDetailsTypeDef,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef",
    {
        "AccountId": str,
        "InstanceDetails": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsInstanceDetailsTypeDef,
        "RecommendedNumberOfInstancesToPurchase": str,
        "RecommendedNormalizedUnitsToPurchase": str,
        "MinimumNumberOfInstancesUsedPerHour": str,
        "MinimumNormalizedUnitsUsedPerHour": str,
        "MaximumNumberOfInstancesUsedPerHour": str,
        "MaximumNormalizedUnitsUsedPerHour": str,
        "AverageNumberOfInstancesUsedPerHour": str,
        "AverageNormalizedUnitsUsedPerHour": str,
        "AverageUtilization": str,
        "EstimatedBreakEvenInMonths": str,
        "CurrencyCode": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedMonthlySavingsPercentage": str,
        "EstimatedMonthlyOnDemandCost": str,
        "EstimatedReservationCostForLookbackPeriod": str,
        "UpfrontCost": str,
        "RecurringStandardMonthlyCost": str,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef",
    {
        "TotalEstimatedMonthlySavingsAmount": str,
        "TotalEstimatedMonthlySavingsPercentage": str,
        "CurrencyCode": str,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef",
    {"OfferingClass": Literal["STANDARD", "CONVERTIBLE"]},
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef",
    {
        "EC2Specification": ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationEC2SpecificationTypeDef
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef",
    {
        "AccountScope": Literal["PAYER", "LINKED"],
        "LookbackPeriodInDays": Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"],
        "TermInYears": Literal["ONE_YEAR", "THREE_YEARS"],
        "PaymentOption": Literal[
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
            "ALL_UPFRONT",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "HEAVY_UTILIZATION",
        ],
        "ServiceSpecification": ClientGetReservationPurchaseRecommendationResponseRecommendationsServiceSpecificationTypeDef,
        "RecommendationDetails": List[
            ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationDetailsTypeDef
        ],
        "RecommendationSummary": ClientGetReservationPurchaseRecommendationResponseRecommendationsRecommendationSummaryTypeDef,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef
):
    pass


_ClientGetReservationPurchaseRecommendationResponseTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": ClientGetReservationPurchaseRecommendationResponseMetadataTypeDef,
        "Recommendations": List[
            ClientGetReservationPurchaseRecommendationResponseRecommendationsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationResponseTypeDef(
    _ClientGetReservationPurchaseRecommendationResponseTypeDef
):
    """
    - *(dict) --*

      - **Metadata** *(dict) --*

        Information about this specific recommendation call, such as the time stamp for when Cost
        Explorer generated this recommendation.
        - **RecommendationId** *(string) --*

          The ID for this specific recommendation.
    """


_ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef",
    {"OfferingClass": Literal["STANDARD", "CONVERTIBLE"]},
    total=False,
)


class ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef(
    _ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef
):
    """
    - **EC2Specification** *(dict) --*

      The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.
      - **OfferingClass** *(string) --*

        Whether you want a recommendation for standard or convertible reservations.
    """


_ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef = TypedDict(
    "_ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef",
    {
        "EC2Specification": ClientGetReservationPurchaseRecommendationServiceSpecificationEC2SpecificationTypeDef
    },
    total=False,
)


class ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef(
    _ClientGetReservationPurchaseRecommendationServiceSpecificationTypeDef
):
    """
    The hardware specifications for the service instances that you want recommendations for, such as
    standard or convertible Amazon EC2 instances.
    - **EC2Specification** *(dict) --*

      The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.
      - **OfferingClass** *(string) --*

        Whether you want a recommendation for standard or convertible reservations.
    """


_ClientGetReservationUtilizationFilterCostCategoriesTypeDef = TypedDict(
    "_ClientGetReservationUtilizationFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetReservationUtilizationFilterCostCategoriesTypeDef(
    _ClientGetReservationUtilizationFilterCostCategoriesTypeDef
):
    pass


_ClientGetReservationUtilizationFilterDimensionsTypeDef = TypedDict(
    "_ClientGetReservationUtilizationFilterDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetReservationUtilizationFilterDimensionsTypeDef(
    _ClientGetReservationUtilizationFilterDimensionsTypeDef
):
    pass


_ClientGetReservationUtilizationFilterTagsTypeDef = TypedDict(
    "_ClientGetReservationUtilizationFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetReservationUtilizationFilterTagsTypeDef(
    _ClientGetReservationUtilizationFilterTagsTypeDef
):
    pass


_ClientGetReservationUtilizationFilterTypeDef = TypedDict(
    "_ClientGetReservationUtilizationFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetReservationUtilizationFilterDimensionsTypeDef,
        "Tags": ClientGetReservationUtilizationFilterTagsTypeDef,
        "CostCategories": ClientGetReservationUtilizationFilterCostCategoriesTypeDef,
    },
    total=False,
)


class ClientGetReservationUtilizationFilterTypeDef(_ClientGetReservationUtilizationFilterTypeDef):
    """
    Filters utilization data by dimensions. You can filter by the following dimensions:
    * AZ
    * CACHE_ENGINE
    * DATABASE_ENGINE
    * DEPLOYMENT_OPTION
    * INSTANCE_TYPE
    * LINKED_ACCOUNT
    * OPERATING_SYSTEM
    * PLATFORM
    * REGION
    * SERVICE
    * SCOPE
    * TENANCY

      ``GetReservationUtilization`` uses the same `Expression
      <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__
      object as the other operations, but only ``AND`` is supported among each dimension, and
      nesting is supported up to only one level deep. If there are multiple values for a dimension,
      they are OR'd together.
    """


_ClientGetReservationUtilizationGroupByTypeDef = TypedDict(
    "_ClientGetReservationUtilizationGroupByTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)


class ClientGetReservationUtilizationGroupByTypeDef(_ClientGetReservationUtilizationGroupByTypeDef):
    """
    - *(dict) --*

      Represents a group when you specify a group by criteria or in the response to a query with a
      specific grouping.
      - **Type** *(string) --*

        The string that represents the type of group.
    """


_ClientGetReservationUtilizationResponseTotalTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseTotalTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseTotalTypeDef(
    _ClientGetReservationUtilizationResponseTotalTypeDef
):
    pass


_ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef(
    _ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef
):
    pass


_ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef",
    {
        "Key": str,
        "Value": str,
        "Attributes": Dict[str, str],
        "Utilization": ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsUtilizationTypeDef,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef(
    _ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef
):
    pass


_ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef(
    _ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef
):
    """
    - **TimePeriod** *(dict) --*

      The period of time that this utilization was used for.
      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date is
        inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
        starting at ``2017-01-01`` up to the end date.
    """


_ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef(
    _ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef
):
    pass


_ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef",
    {
        "TimePeriod": ClientGetReservationUtilizationResponseUtilizationsByTimeTimePeriodTypeDef,
        "Groups": List[ClientGetReservationUtilizationResponseUtilizationsByTimeGroupsTypeDef],
        "Total": ClientGetReservationUtilizationResponseUtilizationsByTimeTotalTypeDef,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef(
    _ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef
):
    """
    - *(dict) --*

      The amount of utilization, in hours.
      - **TimePeriod** *(dict) --*

        The period of time that this utilization was used for.
        - **Start** *(string) --*

          The beginning of the time period that you want the usage and costs for. The start date is
          inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
          starting at ``2017-01-01`` up to the end date.
    """


_ClientGetReservationUtilizationResponseTypeDef = TypedDict(
    "_ClientGetReservationUtilizationResponseTypeDef",
    {
        "UtilizationsByTime": List[
            ClientGetReservationUtilizationResponseUtilizationsByTimeTypeDef
        ],
        "Total": ClientGetReservationUtilizationResponseTotalTypeDef,
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetReservationUtilizationResponseTypeDef(
    _ClientGetReservationUtilizationResponseTypeDef
):
    """
    - *(dict) --*

      - **UtilizationsByTime** *(list) --*

        The amount of time that you used your RIs.
        - *(dict) --*

          The amount of utilization, in hours.
          - **TimePeriod** *(dict) --*

            The period of time that this utilization was used for.
            - **Start** *(string) --*

              The beginning of the time period that you want the usage and costs for. The start date
              is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
              usage data starting at ``2017-01-01`` up to the end date.
    """


_RequiredClientGetReservationUtilizationTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetReservationUtilizationTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetReservationUtilizationTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetReservationUtilizationTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetReservationUtilizationTimePeriodTypeDef(
    _RequiredClientGetReservationUtilizationTimePeriodTypeDef,
    _OptionalClientGetReservationUtilizationTimePeriodTypeDef,
):
    """
    Sets the start and end dates for retrieving RI utilization. The start date is inclusive, but the
    end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is ``2017-05-01``
    , then the cost and usage data is retrieved from ``2017-01-01`` up to and including
    ``2017-04-30`` but not including ``2017-05-01`` .
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientGetRightsizingRecommendationFilterCostCategoriesTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetRightsizingRecommendationFilterCostCategoriesTypeDef(
    _ClientGetRightsizingRecommendationFilterCostCategoriesTypeDef
):
    pass


_ClientGetRightsizingRecommendationFilterDimensionsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationFilterDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetRightsizingRecommendationFilterDimensionsTypeDef(
    _ClientGetRightsizingRecommendationFilterDimensionsTypeDef
):
    pass


_ClientGetRightsizingRecommendationFilterTagsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetRightsizingRecommendationFilterTagsTypeDef(
    _ClientGetRightsizingRecommendationFilterTagsTypeDef
):
    pass


_ClientGetRightsizingRecommendationFilterTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetRightsizingRecommendationFilterDimensionsTypeDef,
        "Tags": ClientGetRightsizingRecommendationFilterTagsTypeDef,
        "CostCategories": ClientGetRightsizingRecommendationFilterCostCategoriesTypeDef,
    },
    total=False,
)


class ClientGetRightsizingRecommendationFilterTypeDef(
    _ClientGetRightsizingRecommendationFilterTypeDef
):
    """
    Use ``Expression`` to filter by cost or by usage. There are two patterns:
    * Simple dimension values - You can set the dimension name and values for the filters that you
    plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==us-west-1`` . The
    ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION", "Values": [
    "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd together to retrieve
    cost or usage data. You can create ``Expression`` and ``DimensionValues`` objects using either
    ``with*`` methods or ``set*`` methods in multiple lines.
    * Compound dimension values with logical operations - You can use multiple ``Expression`` types
    and the logical operators ``AND/OR/NOT`` to create a list of one or more ``Expression`` objects.
    This allows you to filter on more advanced options. For example, you can filter on ``((REGION ==
    us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`` .
    The ``Expression`` for that looks like this:  ``{ "And": [ {"Or": [ {"Dimensions": { "Key":
    "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values":
    ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}}
    ] }``
    .. note::

      Because each ``Expression`` can have only one operator, the service returns an error if more
      than one is specified. The following example shows an ``Expression`` object that creates an
      error.
      ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer"
      ] } }``
    """


_ClientGetRightsizingRecommendationResponseMetadataTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseMetadataTypeDef",
    {
        "RecommendationId": str,
        "GenerationTimestamp": str,
        "LookbackPeriodInDays": Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"],
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseMetadataTypeDef(
    _ClientGetRightsizingRecommendationResponseMetadataTypeDef
):
    """
    - **Metadata** *(dict) --*

      Information regarding this specific recommendation set.
      - **RecommendationId** *(string) --*

        The ID for this specific recommendation.
    """


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": str,
        "InstanceType": str,
        "Platform": str,
        "Region": str,
        "Sku": str,
        "Memory": str,
        "NetworkPerformance": str,
        "Storage": str,
        "Vcpu": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef",
    {
        "EC2ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsEC2ResourceDetailsTypeDef
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": str,
        "MaxMemoryUtilizationPercentage": str,
        "MaxStorageUtilizationPercentage": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef",
    {
        "EC2ResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationEC2ResourceUtilizationTypeDef
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef",
    {
        "ResourceId": str,
        "Tags": List[
            ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTagsTypeDef
        ],
        "ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceDetailsTypeDef,
        "ResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceResourceUtilizationTypeDef,
        "ReservationCoveredHoursInLookbackPeriod": str,
        "SavingsPlansCoveredHoursInLookbackPeriod": str,
        "OnDemandHoursInLookbackPeriod": str,
        "TotalRunningHoursInLookbackPeriod": str,
        "MonthlyCost": str,
        "CurrencyCode": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": str,
        "MaxMemoryUtilizationPercentage": str,
        "MaxStorageUtilizationPercentage": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef",
    {
        "EC2ResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationEC2ResourceUtilizationTypeDef
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": str,
        "InstanceType": str,
        "Platform": str,
        "Region": str,
        "Sku": str,
        "Memory": str,
        "NetworkPerformance": str,
        "Storage": str,
        "Vcpu": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef",
    {
        "EC2ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsEC2ResourceDetailsTypeDef
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef",
    {
        "EstimatedMonthlyCost": str,
        "EstimatedMonthlySavings": str,
        "CurrencyCode": str,
        "DefaultTargetInstance": bool,
        "ResourceDetails": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesResourceDetailsTypeDef,
        "ExpectedResourceUtilization": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesExpectedResourceUtilizationTypeDef,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef",
    {
        "TargetInstances": List[
            ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTargetInstancesTypeDef
        ]
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef",
    {"EstimatedMonthlySavings": str, "CurrencyCode": str},
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef",
    {
        "AccountId": str,
        "CurrentInstance": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsCurrentInstanceTypeDef,
        "RightsizingType": Literal["TERMINATE", "MODIFY"],
        "ModifyRecommendationDetail": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsModifyRecommendationDetailTypeDef,
        "TerminateRecommendationDetail": ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTerminateRecommendationDetailTypeDef,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef(
    _ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseSummaryTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseSummaryTypeDef",
    {
        "TotalRecommendationCount": str,
        "EstimatedTotalMonthlySavingsAmount": str,
        "SavingsCurrencyCode": str,
        "SavingsPercentage": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseSummaryTypeDef(
    _ClientGetRightsizingRecommendationResponseSummaryTypeDef
):
    pass


_ClientGetRightsizingRecommendationResponseTypeDef = TypedDict(
    "_ClientGetRightsizingRecommendationResponseTypeDef",
    {
        "Metadata": ClientGetRightsizingRecommendationResponseMetadataTypeDef,
        "Summary": ClientGetRightsizingRecommendationResponseSummaryTypeDef,
        "RightsizingRecommendations": List[
            ClientGetRightsizingRecommendationResponseRightsizingRecommendationsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetRightsizingRecommendationResponseTypeDef(
    _ClientGetRightsizingRecommendationResponseTypeDef
):
    """
    - *(dict) --*

      - **Metadata** *(dict) --*

        Information regarding this specific recommendation set.
        - **RecommendationId** *(string) --*

          The ID for this specific recommendation.
    """


_ClientGetSavingsPlansCoverageFilterCostCategoriesTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansCoverageFilterCostCategoriesTypeDef(
    _ClientGetSavingsPlansCoverageFilterCostCategoriesTypeDef
):
    pass


_ClientGetSavingsPlansCoverageFilterDimensionsTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageFilterDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetSavingsPlansCoverageFilterDimensionsTypeDef(
    _ClientGetSavingsPlansCoverageFilterDimensionsTypeDef
):
    pass


_ClientGetSavingsPlansCoverageFilterTagsTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansCoverageFilterTagsTypeDef(
    _ClientGetSavingsPlansCoverageFilterTagsTypeDef
):
    pass


_ClientGetSavingsPlansCoverageFilterTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetSavingsPlansCoverageFilterDimensionsTypeDef,
        "Tags": ClientGetSavingsPlansCoverageFilterTagsTypeDef,
        "CostCategories": ClientGetSavingsPlansCoverageFilterCostCategoriesTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansCoverageFilterTypeDef(_ClientGetSavingsPlansCoverageFilterTypeDef):
    """
    Filters Savings Plans coverage data by dimensions. You can filter data for Savings Plans usage
    with the following dimensions:
    * ``LINKED_ACCOUNT``
    * ``REGION``
    * ``SERVICE``
    * ``INSTANCE_FAMILY``

      ``GetSavingsPlansCoverage`` uses the same `Expression
      <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__
      object as the other operations, but only ``AND`` is supported among each dimension. If there
      are multiple values for a dimension, they are OR'd together.
    """


_ClientGetSavingsPlansCoverageGroupByTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageGroupByTypeDef",
    {"Type": Literal["DIMENSION", "TAG", "COST_CATEGORY"], "Key": str},
    total=False,
)


class ClientGetSavingsPlansCoverageGroupByTypeDef(_ClientGetSavingsPlansCoverageGroupByTypeDef):
    """
    - *(dict) --*

      Represents a group when you specify a group by criteria or in the response to a query with a
      specific grouping.
      - **Type** *(string) --*

        The string that represents the type of group.
    """


_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef",
    {
        "SpendCoveredBySavingsPlans": str,
        "OnDemandCost": str,
        "TotalCost": str,
        "CoveragePercentage": str,
    },
    total=False,
)


class ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef(
    _ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef
):
    pass


_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef(
    _ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef
):
    pass


_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesCoverageTypeDef,
        "TimePeriod": ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTimePeriodTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef(
    _ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef
):
    """
    - *(dict) --*

      The amount of Savings Plans eligible usage that is covered by Savings Plans. All calculations
      consider the On-Demand equivalent of your Savings Plans usage.
      - **Attributes** *(dict) --*

        The attribute that applies to a specific ``Dimension`` .
        - *(string) --*

          - *(string) --*
    """


_ClientGetSavingsPlansCoverageResponseTypeDef = TypedDict(
    "_ClientGetSavingsPlansCoverageResponseTypeDef",
    {
        "SavingsPlansCoverages": List[
            ClientGetSavingsPlansCoverageResponseSavingsPlansCoveragesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetSavingsPlansCoverageResponseTypeDef(_ClientGetSavingsPlansCoverageResponseTypeDef):
    """
    - *(dict) --*

      - **SavingsPlansCoverages** *(list) --*

        The amount of spend that your Savings Plans covered.
        - *(dict) --*

          The amount of Savings Plans eligible usage that is covered by Savings Plans. All
          calculations consider the On-Demand equivalent of your Savings Plans usage.
          - **Attributes** *(dict) --*

            The attribute that applies to a specific ``Dimension`` .
            - *(string) --*

              - *(string) --*
    """


_RequiredClientGetSavingsPlansCoverageTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetSavingsPlansCoverageTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetSavingsPlansCoverageTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetSavingsPlansCoverageTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetSavingsPlansCoverageTimePeriodTypeDef(
    _RequiredClientGetSavingsPlansCoverageTimePeriodTypeDef,
    _OptionalClientGetSavingsPlansCoverageTimePeriodTypeDef,
):
    """
    The time period that you want the usage and costs for. The ``Start`` date must be within 13
    months. The ``End`` date must be after the ``Start`` date, and before the current date. Future
    dates can't be used as an ``End`` date.
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef",
    {"RecommendationId": str, "GenerationTimestamp": str},
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef
):
    """
    - **Metadata** *(dict) --*

      Information regarding this specific recommendation set.
      - **RecommendationId** *(string) --*

        The unique identifier for the recommendation set.
    """


_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef",
    {"Region": str, "InstanceFamily": str, "OfferingId": str},
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef
):
    pass


_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef",
    {
        "SavingsPlansDetails": ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsSavingsPlansDetailsTypeDef,
        "AccountId": str,
        "UpfrontCost": str,
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedSPCost": str,
        "EstimatedOnDemandCost": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
        "EstimatedSavingsAmount": str,
        "EstimatedSavingsPercentage": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedAverageUtilization": str,
        "EstimatedMonthlySavingsAmount": str,
        "CurrentMinimumHourlyOnDemandSpend": str,
        "CurrentMaximumHourlyOnDemandSpend": str,
        "CurrentAverageHourlyOnDemandSpend": str,
    },
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef
):
    pass


_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef",
    {
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedTotalCost": str,
        "CurrentOnDemandSpend": str,
        "EstimatedSavingsAmount": str,
        "TotalRecommendationCount": str,
        "DailyCommitmentToPurchase": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedSavingsPercentage": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
    },
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef
):
    pass


_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef",
    {
        "SavingsPlansType": Literal["COMPUTE_SP", "EC2_INSTANCE_SP"],
        "TermInYears": Literal["ONE_YEAR", "THREE_YEARS"],
        "PaymentOption": Literal[
            "NO_UPFRONT",
            "PARTIAL_UPFRONT",
            "ALL_UPFRONT",
            "LIGHT_UTILIZATION",
            "MEDIUM_UTILIZATION",
            "HEAVY_UTILIZATION",
        ],
        "LookbackPeriodInDays": Literal["SEVEN_DAYS", "THIRTY_DAYS", "SIXTY_DAYS"],
        "SavingsPlansPurchaseRecommendationDetails": List[
            ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationDetailsTypeDef
        ],
        "SavingsPlansPurchaseRecommendationSummary": ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationSavingsPlansPurchaseRecommendationSummaryTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef
):
    pass


_ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef = TypedDict(
    "_ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": ClientGetSavingsPlansPurchaseRecommendationResponseMetadataTypeDef,
        "SavingsPlansPurchaseRecommendation": ClientGetSavingsPlansPurchaseRecommendationResponseSavingsPlansPurchaseRecommendationTypeDef,
        "NextPageToken": str,
    },
    total=False,
)


class ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef(
    _ClientGetSavingsPlansPurchaseRecommendationResponseTypeDef
):
    """
    - *(dict) --*

      - **Metadata** *(dict) --*

        Information regarding this specific recommendation set.
        - **RecommendationId** *(string) --*

          The unique identifier for the recommendation set.
    """


_ClientGetSavingsPlansUtilizationDetailsFilterCostCategoriesTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsFilterCostCategoriesTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsFilterCostCategoriesTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsFilterTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetSavingsPlansUtilizationDetailsFilterDimensionsTypeDef,
        "Tags": ClientGetSavingsPlansUtilizationDetailsFilterTagsTypeDef,
        "CostCategories": ClientGetSavingsPlansUtilizationDetailsFilterCostCategoriesTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsFilterTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsFilterTypeDef
):
    """
    Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can
    filter data with the following dimensions:
    * ``LINKED_ACCOUNT``
    * ``SAVINGS_PLAN_ARN``
    * ``REGION``
    * ``PAYMENT_OPTION``
    * ``INSTANCE_TYPE_FAMILY``

      ``GetSavingsPlansUtilizationDetails`` uses the same `Expression
      <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__
      object as the other operations, but only ``AND`` is supported among each dimension.
    """


_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef",
    {
        "SavingsPlanArn": str,
        "Attributes": Dict[str, str],
        "Utilization": ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsAmortizedCommitmentTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef
):
    """
    - *(dict) --*

      A single daily or monthly Savings Plans utilization rate, and details for your account. Master
      accounts in an organization have access to member accounts. You can use ``GetDimensionValues``
      to determine the possible dimension values.
      - **SavingsPlanArn** *(string) --*

        The unique Amazon Resource Name (ARN) for a particular Savings Plan.
    """


_ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef",
    {
        "Utilization": ClientGetSavingsPlansUtilizationDetailsResponseTotalUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationDetailsResponseTotalSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationDetailsResponseTotalAmortizedCommitmentTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationDetailsResponseTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationDetailsResponseTypeDef",
    {
        "SavingsPlansUtilizationDetails": List[
            ClientGetSavingsPlansUtilizationDetailsResponseSavingsPlansUtilizationDetailsTypeDef
        ],
        "Total": ClientGetSavingsPlansUtilizationDetailsResponseTotalTypeDef,
        "TimePeriod": ClientGetSavingsPlansUtilizationDetailsResponseTimePeriodTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationDetailsResponseTypeDef(
    _ClientGetSavingsPlansUtilizationDetailsResponseTypeDef
):
    """
    - *(dict) --*

      - **SavingsPlansUtilizationDetails** *(list) --*

        Retrieves a single daily or monthly Savings Plans utilization rate and details for your
        account.
        - *(dict) --*

          A single daily or monthly Savings Plans utilization rate, and details for your account.
          Master accounts in an organization have access to member accounts. You can use
          ``GetDimensionValues`` to determine the possible dimension values.
          - **SavingsPlanArn** *(string) --*

            The unique Amazon Resource Name (ARN) for a particular Savings Plan.
    """


_RequiredClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef(
    _RequiredClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef,
    _OptionalClientGetSavingsPlansUtilizationDetailsTimePeriodTypeDef,
):
    """
    The time period that you want the usage and costs for. The ``Start`` date must be within 13
    months. The ``End`` date must be after the ``Start`` date, and before the current date. Future
    dates can't be used as an ``End`` date.
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientGetSavingsPlansUtilizationFilterCostCategoriesTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansUtilizationFilterCostCategoriesTypeDef(
    _ClientGetSavingsPlansUtilizationFilterCostCategoriesTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef(
    _ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationFilterTagsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationFilterTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetSavingsPlansUtilizationFilterTagsTypeDef(
    _ClientGetSavingsPlansUtilizationFilterTagsTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationFilterTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetSavingsPlansUtilizationFilterDimensionsTypeDef,
        "Tags": ClientGetSavingsPlansUtilizationFilterTagsTypeDef,
        "CostCategories": ClientGetSavingsPlansUtilizationFilterCostCategoriesTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationFilterTypeDef(_ClientGetSavingsPlansUtilizationFilterTypeDef):
    """
    Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can
    filter data with the following dimensions:
    * ``LINKED_ACCOUNT``
    * ``SAVINGS_PLAN_ARN``
    * ``SAVINGS_PLANS_TYPE``
    * ``REGION``
    * ``PAYMENT_OPTION``
    * ``INSTANCE_TYPE_FAMILY``

      ``GetSavingsPlansUtilization`` uses the same `Expression
      <http://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`__
      object as the other operations, but only ``AND`` is supported among each dimension.
    """


_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef(
    _ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef(
    _ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef(
    _ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef
):
    """
    - **TimePeriod** *(dict) --*

      The time period that you want the usage and costs for.
      - **Start** *(string) --*

        The beginning of the time period that you want the usage and costs for. The start date is
        inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
        starting at ``2017-01-01`` up to the end date.
    """


_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef(
    _ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef",
    {
        "TimePeriod": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTimePeriodTypeDef,
        "Utilization": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeAmortizedCommitmentTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef(
    _ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef
):
    """
    - *(dict) --*

      The amount of Savings Plans utilization, in hours.
      - **TimePeriod** *(dict) --*

        The time period that you want the usage and costs for.
        - **Start** *(string) --*

          The beginning of the time period that you want the usage and costs for. The start date is
          inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
          starting at ``2017-01-01`` up to the end date.
    """


_ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef(
    _ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef",
    {"NetSavings": str, "OnDemandCostEquivalent": str},
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef(
    _ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef(
    _ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationResponseTotalTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseTotalTypeDef",
    {
        "Utilization": ClientGetSavingsPlansUtilizationResponseTotalUtilizationTypeDef,
        "Savings": ClientGetSavingsPlansUtilizationResponseTotalSavingsTypeDef,
        "AmortizedCommitment": ClientGetSavingsPlansUtilizationResponseTotalAmortizedCommitmentTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseTotalTypeDef(
    _ClientGetSavingsPlansUtilizationResponseTotalTypeDef
):
    pass


_ClientGetSavingsPlansUtilizationResponseTypeDef = TypedDict(
    "_ClientGetSavingsPlansUtilizationResponseTypeDef",
    {
        "SavingsPlansUtilizationsByTime": List[
            ClientGetSavingsPlansUtilizationResponseSavingsPlansUtilizationsByTimeTypeDef
        ],
        "Total": ClientGetSavingsPlansUtilizationResponseTotalTypeDef,
    },
    total=False,
)


class ClientGetSavingsPlansUtilizationResponseTypeDef(
    _ClientGetSavingsPlansUtilizationResponseTypeDef
):
    """
    - *(dict) --*

      - **SavingsPlansUtilizationsByTime** *(list) --*

        The amount of cost/commitment you used your Savings Plans. This allows you to specify date
        ranges.
        - *(dict) --*

          The amount of Savings Plans utilization, in hours.
          - **TimePeriod** *(dict) --*

            The time period that you want the usage and costs for.
            - **Start** *(string) --*

              The beginning of the time period that you want the usage and costs for. The start date
              is inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and
              usage data starting at ``2017-01-01`` up to the end date.
    """


_RequiredClientGetSavingsPlansUtilizationTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetSavingsPlansUtilizationTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetSavingsPlansUtilizationTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetSavingsPlansUtilizationTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetSavingsPlansUtilizationTimePeriodTypeDef(
    _RequiredClientGetSavingsPlansUtilizationTimePeriodTypeDef,
    _OptionalClientGetSavingsPlansUtilizationTimePeriodTypeDef,
):
    """
    The time period that you want the usage and costs for. The ``Start`` date must be within 13
    months. The ``End`` date must be after the ``Start`` date, and before the current date. Future
    dates can't be used as an ``End`` date.
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientGetTagsResponseTypeDef = TypedDict(
    "_ClientGetTagsResponseTypeDef",
    {"NextPageToken": str, "Tags": List[str], "ReturnSize": int, "TotalSize": int},
    total=False,
)


class ClientGetTagsResponseTypeDef(_ClientGetTagsResponseTypeDef):
    """
    - *(dict) --*

      - **NextPageToken** *(string) --*

        The token for the next set of retrievable results. AWS provides the token when the response
        from a previous call has more results than the maximum page size.
    """


_RequiredClientGetTagsTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetTagsTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetTagsTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetTagsTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetTagsTimePeriodTypeDef(
    _RequiredClientGetTagsTimePeriodTypeDef, _OptionalClientGetTagsTimePeriodTypeDef
):
    """
    The start and end dates for retrieving the dimension values. The start date is inclusive, but
    the end date is exclusive. For example, if ``start`` is ``2017-01-01`` and ``end`` is
    ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up to and
    including ``2017-04-30`` but not including ``2017-05-01`` .
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientGetUsageForecastFilterCostCategoriesTypeDef = TypedDict(
    "_ClientGetUsageForecastFilterCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientGetUsageForecastFilterCostCategoriesTypeDef(
    _ClientGetUsageForecastFilterCostCategoriesTypeDef
):
    pass


_ClientGetUsageForecastFilterDimensionsTypeDef = TypedDict(
    "_ClientGetUsageForecastFilterDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientGetUsageForecastFilterDimensionsTypeDef(_ClientGetUsageForecastFilterDimensionsTypeDef):
    pass


_ClientGetUsageForecastFilterTagsTypeDef = TypedDict(
    "_ClientGetUsageForecastFilterTagsTypeDef", {"Key": str, "Values": List[str]}, total=False
)


class ClientGetUsageForecastFilterTagsTypeDef(_ClientGetUsageForecastFilterTagsTypeDef):
    pass


_ClientGetUsageForecastFilterTypeDef = TypedDict(
    "_ClientGetUsageForecastFilterTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientGetUsageForecastFilterDimensionsTypeDef,
        "Tags": ClientGetUsageForecastFilterTagsTypeDef,
        "CostCategories": ClientGetUsageForecastFilterCostCategoriesTypeDef,
    },
    total=False,
)


class ClientGetUsageForecastFilterTypeDef(_ClientGetUsageForecastFilterTypeDef):
    """
    The filters that you want to use to filter your forecast. Cost Explorer API supports all of the
    Cost Explorer filters.
    - **Or** *(list) --*

      Return results that match either ``Dimension`` object.
      - *(dict) --*

        Use ``Expression`` to filter by cost or by usage. There are two patterns:
        * Simple dimension values - You can set the dimension name and values for the filters that
        you plan to use. For example, you can filter for ``REGION==us-east-1 OR REGION==
            us-west-1``
        . The ``Expression`` for that looks like this:  ``{ "Dimensions": { "Key": "REGION",
        "Values": [ "us-east-1", “us-west-1” ] } }``   The list of dimension values are OR'd
        together to retrieve cost or usage data. You can create ``Expression`` and
        ``DimensionValues`` objects using either ``with*`` methods or ``set*`` methods in multiple
        lines.
        * Compound dimension values with logical operations - You can use multiple ``Expression``
        types and the logical operators ``AND/OR/NOT`` to create a list of one or more
        ``Expression`` objects. This allows you to filter on more advanced options. For example, you
        can filter on ``((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type ==
             Type1)) AND
        (USAGE_TYPE !=
             DataTransfer)`` . The ``Expression`` for that looks like this:  ``{ "And": [
        {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }},
        {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key":
        "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }``
        .. note::

          Because each ``Expression`` can have only one operator, the service returns an error if
          more than one is specified. The following example shows an ``Expression`` object that
          creates an error.
          ``{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [
          "DataTransfer" ] } }``
    """


_ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef = TypedDict(
    "_ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef",
    {"Start": str, "End": str},
    total=False,
)


class ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef(
    _ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef
):
    pass


_ClientGetUsageForecastResponseForecastResultsByTimeTypeDef = TypedDict(
    "_ClientGetUsageForecastResponseForecastResultsByTimeTypeDef",
    {
        "TimePeriod": ClientGetUsageForecastResponseForecastResultsByTimeTimePeriodTypeDef,
        "MeanValue": str,
        "PredictionIntervalLowerBound": str,
        "PredictionIntervalUpperBound": str,
    },
    total=False,
)


class ClientGetUsageForecastResponseForecastResultsByTimeTypeDef(
    _ClientGetUsageForecastResponseForecastResultsByTimeTypeDef
):
    pass


_ClientGetUsageForecastResponseTotalTypeDef = TypedDict(
    "_ClientGetUsageForecastResponseTotalTypeDef", {"Amount": str, "Unit": str}, total=False
)


class ClientGetUsageForecastResponseTotalTypeDef(_ClientGetUsageForecastResponseTotalTypeDef):
    """
    - **Total** *(dict) --*

      How much you're forecasted to use over the forecast period.
      - **Amount** *(string) --*

        The actual number that represents the metric.
    """


_ClientGetUsageForecastResponseTypeDef = TypedDict(
    "_ClientGetUsageForecastResponseTypeDef",
    {
        "Total": ClientGetUsageForecastResponseTotalTypeDef,
        "ForecastResultsByTime": List[ClientGetUsageForecastResponseForecastResultsByTimeTypeDef],
    },
    total=False,
)


class ClientGetUsageForecastResponseTypeDef(_ClientGetUsageForecastResponseTypeDef):
    """
    - *(dict) --*

      - **Total** *(dict) --*

        How much you're forecasted to use over the forecast period.
        - **Amount** *(string) --*

          The actual number that represents the metric.
    """


_RequiredClientGetUsageForecastTimePeriodTypeDef = TypedDict(
    "_RequiredClientGetUsageForecastTimePeriodTypeDef", {"Start": str}
)
_OptionalClientGetUsageForecastTimePeriodTypeDef = TypedDict(
    "_OptionalClientGetUsageForecastTimePeriodTypeDef", {"End": str}, total=False
)


class ClientGetUsageForecastTimePeriodTypeDef(
    _RequiredClientGetUsageForecastTimePeriodTypeDef,
    _OptionalClientGetUsageForecastTimePeriodTypeDef,
):
    """
    The start and end dates of the period that you want to retrieve usage forecast for. The start
    date is inclusive, but the end date is exclusive. For example, if ``start`` is ``2017-01-01``
    and ``end`` is ``2017-05-01`` , then the cost and usage data is retrieved from ``2017-01-01`` up
    to and including ``2017-04-30`` but not including ``2017-05-01`` .
    - **Start** *(string) --***[REQUIRED]**

      The beginning of the time period that you want the usage and costs for. The start date is
      inclusive. For example, if ``start`` is ``2017-01-01`` , AWS retrieves cost and usage data
      starting at ``2017-01-01`` up to the end date.
    """


_ClientListCostCategoryDefinitionsResponseCostCategoryReferencesTypeDef = TypedDict(
    "_ClientListCostCategoryDefinitionsResponseCostCategoryReferencesTypeDef",
    {"CostCategoryArn": str, "Name": str, "EffectiveStart": str, "EffectiveEnd": str},
    total=False,
)


class ClientListCostCategoryDefinitionsResponseCostCategoryReferencesTypeDef(
    _ClientListCostCategoryDefinitionsResponseCostCategoryReferencesTypeDef
):
    """
    - *(dict) --*

      .. warning::

        * **Cost Category is in preview release for AWS Billing and Cost Management and is subject
        to change. Your use of Cost Categories is subject to the Beta Service Participation terms of
        the `AWS Service Terms <https://aws.amazon.com/service-terms/>`__ (Section 1.10).** *
    """


_ClientListCostCategoryDefinitionsResponseTypeDef = TypedDict(
    "_ClientListCostCategoryDefinitionsResponseTypeDef",
    {
        "CostCategoryReferences": List[
            ClientListCostCategoryDefinitionsResponseCostCategoryReferencesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListCostCategoryDefinitionsResponseTypeDef(
    _ClientListCostCategoryDefinitionsResponseTypeDef
):
    """
    - *(dict) --*

      - **CostCategoryReferences** *(list) --*

        A reference to a Cost Category containing enough information to identify the Cost Category.
        - *(dict) --*

          .. warning::

            * **Cost Category is in preview release for AWS Billing and Cost Management and is
            subject to change. Your use of Cost Categories is subject to the Beta Service
            Participation terms of the `AWS Service Terms <https://aws.amazon.com/service-terms/>`__
            (Section 1.10).** *
    """


_ClientUpdateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "_ClientUpdateCostCategoryDefinitionResponseTypeDef",
    {"CostCategoryArn": str, "EffectiveStart": str},
    total=False,
)


class ClientUpdateCostCategoryDefinitionResponseTypeDef(
    _ClientUpdateCostCategoryDefinitionResponseTypeDef
):
    """
    - *(dict) --*

      - **CostCategoryArn** *(string) --*

        The unique identifier for your Cost Category.
    """


_ClientUpdateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef = TypedDict(
    "_ClientUpdateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientUpdateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef(
    _ClientUpdateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef
):
    pass


_ClientUpdateCostCategoryDefinitionRulesRuleDimensionsTypeDef = TypedDict(
    "_ClientUpdateCostCategoryDefinitionRulesRuleDimensionsTypeDef",
    {
        "Key": Literal[
            "AZ",
            "INSTANCE_TYPE",
            "LINKED_ACCOUNT",
            "OPERATION",
            "PURCHASE_TYPE",
            "REGION",
            "SERVICE",
            "USAGE_TYPE",
            "USAGE_TYPE_GROUP",
            "RECORD_TYPE",
            "OPERATING_SYSTEM",
            "TENANCY",
            "SCOPE",
            "PLATFORM",
            "SUBSCRIPTION_ID",
            "LEGAL_ENTITY_NAME",
            "DEPLOYMENT_OPTION",
            "DATABASE_ENGINE",
            "CACHE_ENGINE",
            "INSTANCE_TYPE_FAMILY",
            "BILLING_ENTITY",
            "RESERVATION_ID",
            "RESOURCE_ID",
            "RIGHTSIZING_TYPE",
            "SAVINGS_PLANS_TYPE",
            "SAVINGS_PLAN_ARN",
            "PAYMENT_OPTION",
        ],
        "Values": List[str],
    },
    total=False,
)


class ClientUpdateCostCategoryDefinitionRulesRuleDimensionsTypeDef(
    _ClientUpdateCostCategoryDefinitionRulesRuleDimensionsTypeDef
):
    pass


_ClientUpdateCostCategoryDefinitionRulesRuleTagsTypeDef = TypedDict(
    "_ClientUpdateCostCategoryDefinitionRulesRuleTagsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientUpdateCostCategoryDefinitionRulesRuleTagsTypeDef(
    _ClientUpdateCostCategoryDefinitionRulesRuleTagsTypeDef
):
    pass


_ClientUpdateCostCategoryDefinitionRulesRuleTypeDef = TypedDict(
    "_ClientUpdateCostCategoryDefinitionRulesRuleTypeDef",
    {
        "Or": List[Any],
        "And": List[Any],
        "Not": Any,
        "Dimensions": ClientUpdateCostCategoryDefinitionRulesRuleDimensionsTypeDef,
        "Tags": ClientUpdateCostCategoryDefinitionRulesRuleTagsTypeDef,
        "CostCategories": ClientUpdateCostCategoryDefinitionRulesRuleCostCategoriesTypeDef,
    },
    total=False,
)


class ClientUpdateCostCategoryDefinitionRulesRuleTypeDef(
    _ClientUpdateCostCategoryDefinitionRulesRuleTypeDef
):
    pass


_ClientUpdateCostCategoryDefinitionRulesTypeDef = TypedDict(
    "_ClientUpdateCostCategoryDefinitionRulesTypeDef",
    {"Value": str, "Rule": ClientUpdateCostCategoryDefinitionRulesRuleTypeDef},
    total=False,
)


class ClientUpdateCostCategoryDefinitionRulesTypeDef(
    _ClientUpdateCostCategoryDefinitionRulesTypeDef
):
    """
    - *(dict) --*

      .. warning::

        * **Cost Category is in preview release for AWS Billing and Cost Management and is subject
        to change. Your use of Cost Categories is subject to the Beta Service Participation terms of
        the `AWS Service Terms <https://aws.amazon.com/service-terms/>`__ (Section 1.10).** *
    """
