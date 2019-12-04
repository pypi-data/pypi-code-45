"Main interface for savingsplans service type defs"
from __future__ import annotations

from typing import Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCreateSavingsPlanResponseTypeDef",
    "ClientDescribeSavingsPlanRatesFiltersTypeDef",
    "ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef",
    "ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef",
    "ClientDescribeSavingsPlanRatesResponseTypeDef",
    "ClientDescribeSavingsPlansFiltersTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesFiltersTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef",
    "ClientDescribeSavingsPlansOfferingRatesResponseTypeDef",
    "ClientDescribeSavingsPlansOfferingsFiltersTypeDef",
    "ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef",
    "ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef",
    "ClientDescribeSavingsPlansOfferingsResponseTypeDef",
    "ClientDescribeSavingsPlansResponsesavingsPlansTypeDef",
    "ClientDescribeSavingsPlansResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
)


_ClientCreateSavingsPlanResponseTypeDef = TypedDict(
    "_ClientCreateSavingsPlanResponseTypeDef", {"savingsPlanId": str}, total=False
)


class ClientCreateSavingsPlanResponseTypeDef(_ClientCreateSavingsPlanResponseTypeDef):
    """
    - *(dict) --*

      - **savingsPlanId** *(string) --*

        The ID of the Savings Plan.
    """


_ClientDescribeSavingsPlanRatesFiltersTypeDef = TypedDict(
    "_ClientDescribeSavingsPlanRatesFiltersTypeDef",
    {
        "name": Literal[
            "region",
            "instanceType",
            "productDescription",
            "tenancy",
            "productType",
            "serviceCode",
            "usageType",
            "operation",
        ],
        "values": List[str],
    },
    total=False,
)


class ClientDescribeSavingsPlanRatesFiltersTypeDef(_ClientDescribeSavingsPlanRatesFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The filter name.
    """


_ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef = TypedDict(
    "_ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef",
    {
        "name": Literal[
            "region", "instanceType", "instanceFamily", "productDescription", "tenancy"
        ],
        "value": str,
    },
    total=False,
)


class ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef(
    _ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef
):
    pass


_ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef = TypedDict(
    "_ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef",
    {
        "rate": str,
        "currency": Literal["CNY", "USD"],
        "unit": str,
        "productType": Literal["EC2", "Fargate"],
        "serviceCode": Literal["AmazonEC2", "AmazonECS"],
        "usageType": str,
        "operation": str,
        "properties": List[ClientDescribeSavingsPlanRatesResponsesearchResultspropertiesTypeDef],
    },
    total=False,
)


class ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef(
    _ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef
):
    pass


_ClientDescribeSavingsPlanRatesResponseTypeDef = TypedDict(
    "_ClientDescribeSavingsPlanRatesResponseTypeDef",
    {
        "savingsPlanId": str,
        "searchResults": List[ClientDescribeSavingsPlanRatesResponsesearchResultsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeSavingsPlanRatesResponseTypeDef(_ClientDescribeSavingsPlanRatesResponseTypeDef):
    """
    - *(dict) --*

      - **savingsPlanId** *(string) --*

        The ID of the Savings Plan.
    """


_ClientDescribeSavingsPlansFiltersTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansFiltersTypeDef",
    {
        "name": Literal[
            "region",
            "ec2-instance-family",
            "commitment",
            "upfront",
            "term",
            "savings-plan-type",
            "payment-option",
            "start",
            "end",
        ],
        "values": List[str],
    },
    total=False,
)


class ClientDescribeSavingsPlansFiltersTypeDef(_ClientDescribeSavingsPlansFiltersTypeDef):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The filter name.
    """


_ClientDescribeSavingsPlansOfferingRatesFiltersTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingRatesFiltersTypeDef",
    {
        "name": Literal[
            "region", "instanceFamily", "instanceType", "productDescription", "tenancy", "productId"
        ],
        "values": List[str],
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingRatesFiltersTypeDef(
    _ClientDescribeSavingsPlansOfferingRatesFiltersTypeDef
):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The filter name.
    """


_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef",
    {"name": str, "value": str},
    total=False,
)


class ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef(
    _ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef
):
    pass


_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef",
    {
        "offeringId": str,
        "paymentOption": Literal["All Upfront", "Partial Upfront", "No Upfront"],
        "planType": Literal["Compute", "EC2Instance"],
        "durationSeconds": int,
        "currency": Literal["CNY", "USD"],
        "planDescription": str,
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef(
    _ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef
):
    """
    - **savingsPlanOffering** *(dict) --*

      The Savings Plan offering.
      - **offeringId** *(string) --*

        The ID of the offering.
    """


_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef",
    {
        "savingsPlanOffering": ClientDescribeSavingsPlansOfferingRatesResponsesearchResultssavingsPlanOfferingTypeDef,
        "rate": str,
        "unit": str,
        "productType": Literal["EC2", "Fargate"],
        "serviceCode": Literal["AmazonEC2", "AmazonECS"],
        "usageType": str,
        "operation": str,
        "properties": List[
            ClientDescribeSavingsPlansOfferingRatesResponsesearchResultspropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef(
    _ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef
):
    """
    - *(dict) --*

      Information about a Savings Plan offering rate.
      - **savingsPlanOffering** *(dict) --*

        The Savings Plan offering.
        - **offeringId** *(string) --*

          The ID of the offering.
    """


_ClientDescribeSavingsPlansOfferingRatesResponseTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingRatesResponseTypeDef",
    {
        "searchResults": List[ClientDescribeSavingsPlansOfferingRatesResponsesearchResultsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingRatesResponseTypeDef(
    _ClientDescribeSavingsPlansOfferingRatesResponseTypeDef
):
    """
    - *(dict) --*

      - **searchResults** *(list) --*

        Information about the Savings Plans offering rates.
        - *(dict) --*

          Information about a Savings Plan offering rate.
          - **savingsPlanOffering** *(dict) --*

            The Savings Plan offering.
            - **offeringId** *(string) --*

              The ID of the offering.
    """


_ClientDescribeSavingsPlansOfferingsFiltersTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingsFiltersTypeDef",
    {"name": Literal["region", "instanceFamily"], "values": List[str]},
    total=False,
)


class ClientDescribeSavingsPlansOfferingsFiltersTypeDef(
    _ClientDescribeSavingsPlansOfferingsFiltersTypeDef
):
    """
    - *(dict) --*

      Information about a filter.
      - **name** *(string) --*

        The filter name.
    """


_ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef",
    {"name": Literal["region", "instanceFamily"], "value": str},
    total=False,
)


class ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef(
    _ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef
):
    pass


_ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef",
    {
        "offeringId": str,
        "productTypes": List[Literal["EC2", "Fargate"]],
        "planType": Literal["Compute", "EC2Instance"],
        "description": str,
        "paymentOption": Literal["All Upfront", "Partial Upfront", "No Upfront"],
        "durationSeconds": int,
        "currency": Literal["CNY", "USD"],
        "serviceCode": str,
        "usageType": str,
        "operation": str,
        "properties": List[
            ClientDescribeSavingsPlansOfferingsResponsesearchResultspropertiesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef(
    _ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef
):
    """
    - *(dict) --*

      Information about a Savings Plan offering.
      - **offeringId** *(string) --*

        The ID of the offering.
    """


_ClientDescribeSavingsPlansOfferingsResponseTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansOfferingsResponseTypeDef",
    {
        "searchResults": List[ClientDescribeSavingsPlansOfferingsResponsesearchResultsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeSavingsPlansOfferingsResponseTypeDef(
    _ClientDescribeSavingsPlansOfferingsResponseTypeDef
):
    """
    - *(dict) --*

      - **searchResults** *(list) --*

        Information about the Savings Plans offerings.
        - *(dict) --*

          Information about a Savings Plan offering.
          - **offeringId** *(string) --*

            The ID of the offering.
    """


_ClientDescribeSavingsPlansResponsesavingsPlansTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansResponsesavingsPlansTypeDef",
    {
        "offeringId": str,
        "savingsPlanId": str,
        "savingsPlanArn": str,
        "description": str,
        "start": str,
        "end": str,
        "state": Literal["payment-pending", "payment-failed", "active", "retired"],
        "region": str,
        "ec2InstanceFamily": str,
        "savingsPlanType": Literal["Compute", "EC2Instance"],
        "paymentOption": Literal["All Upfront", "Partial Upfront", "No Upfront"],
        "productTypes": List[Literal["EC2", "Fargate"]],
        "currency": Literal["CNY", "USD"],
        "commitment": str,
        "upfrontPaymentAmount": str,
        "recurringPaymentAmount": str,
        "termDurationInSeconds": int,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeSavingsPlansResponsesavingsPlansTypeDef(
    _ClientDescribeSavingsPlansResponsesavingsPlansTypeDef
):
    """
    - *(dict) --*

      Information about a Savings Plan.
      - **offeringId** *(string) --*

        The ID of the offering.
    """


_ClientDescribeSavingsPlansResponseTypeDef = TypedDict(
    "_ClientDescribeSavingsPlansResponseTypeDef",
    {"savingsPlans": List[ClientDescribeSavingsPlansResponsesavingsPlansTypeDef], "nextToken": str},
    total=False,
)


class ClientDescribeSavingsPlansResponseTypeDef(_ClientDescribeSavingsPlansResponseTypeDef):
    """
    - *(dict) --*

      - **savingsPlans** *(list) --*

        Information about the Savings Plans.
        - *(dict) --*

          Information about a Savings Plan.
          - **offeringId** *(string) --*

            The ID of the offering.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(_ClientListTagsForResourceResponseTypeDef):
    """
    - *(dict) --*

      - **tags** *(dict) --*

        Information about the tags.
        - *(string) --*

          - *(string) --*
    """
