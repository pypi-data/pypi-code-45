"Main interface for meteringmarketplace service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchMeterUsageResponseResultsUsageRecordTypeDef",
    "ClientBatchMeterUsageResponseResultsTypeDef",
    "ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef",
    "ClientBatchMeterUsageResponseTypeDef",
    "ClientBatchMeterUsageUsageRecordsTypeDef",
    "ClientMeterUsageResponseTypeDef",
    "ClientRegisterUsageResponseTypeDef",
    "ClientResolveCustomerResponseTypeDef",
)


_ClientBatchMeterUsageResponseResultsUsageRecordTypeDef = TypedDict(
    "_ClientBatchMeterUsageResponseResultsUsageRecordTypeDef",
    {"Timestamp": datetime, "CustomerIdentifier": str, "Dimension": str, "Quantity": int},
    total=False,
)


class ClientBatchMeterUsageResponseResultsUsageRecordTypeDef(
    _ClientBatchMeterUsageResponseResultsUsageRecordTypeDef
):
    """
    - **UsageRecord** *(dict) --*

      The UsageRecord that was part of the BatchMeterUsage request.
      - **Timestamp** *(datetime) --*

        Timestamp, in UTC, for which the usage is being reported.
        Your application can meter usage for up to one hour in the past. Make sure the timestamp
        value is not before the start of the software usage.
    """


_ClientBatchMeterUsageResponseResultsTypeDef = TypedDict(
    "_ClientBatchMeterUsageResponseResultsTypeDef",
    {
        "UsageRecord": ClientBatchMeterUsageResponseResultsUsageRecordTypeDef,
        "MeteringRecordId": str,
        "Status": Literal["Success", "CustomerNotSubscribed", "DuplicateRecord"],
    },
    total=False,
)


class ClientBatchMeterUsageResponseResultsTypeDef(_ClientBatchMeterUsageResponseResultsTypeDef):
    """
    - *(dict) --*

      A UsageRecordResult indicates the status of a given UsageRecord processed by BatchMeterUsage.
      - **UsageRecord** *(dict) --*

        The UsageRecord that was part of the BatchMeterUsage request.
        - **Timestamp** *(datetime) --*

          Timestamp, in UTC, for which the usage is being reported.
          Your application can meter usage for up to one hour in the past. Make sure the timestamp
          value is not before the start of the software usage.
    """


_ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef = TypedDict(
    "_ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef",
    {"Timestamp": datetime, "CustomerIdentifier": str, "Dimension": str, "Quantity": int},
    total=False,
)


class ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef(
    _ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef
):
    pass


_ClientBatchMeterUsageResponseTypeDef = TypedDict(
    "_ClientBatchMeterUsageResponseTypeDef",
    {
        "Results": List[ClientBatchMeterUsageResponseResultsTypeDef],
        "UnprocessedRecords": List[ClientBatchMeterUsageResponseUnprocessedRecordsTypeDef],
    },
    total=False,
)


class ClientBatchMeterUsageResponseTypeDef(_ClientBatchMeterUsageResponseTypeDef):
    """
    - *(dict) --*

      Contains the UsageRecords processed by BatchMeterUsage and any records that have failed due to
      transient error.
      - **Results** *(list) --*

        Contains all UsageRecords processed by BatchMeterUsage. These records were either honored by
        AWS Marketplace Metering Service or were invalid.
        - *(dict) --*

          A UsageRecordResult indicates the status of a given UsageRecord processed by
          BatchMeterUsage.
          - **UsageRecord** *(dict) --*

            The UsageRecord that was part of the BatchMeterUsage request.
            - **Timestamp** *(datetime) --*

              Timestamp, in UTC, for which the usage is being reported.
              Your application can meter usage for up to one hour in the past. Make sure the
              timestamp value is not before the start of the software usage.
    """


_RequiredClientBatchMeterUsageUsageRecordsTypeDef = TypedDict(
    "_RequiredClientBatchMeterUsageUsageRecordsTypeDef", {"Timestamp": datetime}
)
_OptionalClientBatchMeterUsageUsageRecordsTypeDef = TypedDict(
    "_OptionalClientBatchMeterUsageUsageRecordsTypeDef",
    {"CustomerIdentifier": str, "Dimension": str, "Quantity": int},
    total=False,
)


class ClientBatchMeterUsageUsageRecordsTypeDef(
    _RequiredClientBatchMeterUsageUsageRecordsTypeDef,
    _OptionalClientBatchMeterUsageUsageRecordsTypeDef,
):
    """
    - *(dict) --*

      A UsageRecord indicates a quantity of usage for a given product, customer, dimension and time.
      Multiple requests with the same UsageRecords as input will be deduplicated to prevent double
      charges.
      - **Timestamp** *(datetime) --***[REQUIRED]**

        Timestamp, in UTC, for which the usage is being reported.
        Your application can meter usage for up to one hour in the past. Make sure the timestamp
        value is not before the start of the software usage.
    """


_ClientMeterUsageResponseTypeDef = TypedDict(
    "_ClientMeterUsageResponseTypeDef", {"MeteringRecordId": str}, total=False
)


class ClientMeterUsageResponseTypeDef(_ClientMeterUsageResponseTypeDef):
    """
    - *(dict) --*

      - **MeteringRecordId** *(string) --*

        Metering record id.
    """


_ClientRegisterUsageResponseTypeDef = TypedDict(
    "_ClientRegisterUsageResponseTypeDef",
    {"PublicKeyRotationTimestamp": datetime, "Signature": str},
    total=False,
)


class ClientRegisterUsageResponseTypeDef(_ClientRegisterUsageResponseTypeDef):
    """
    - *(dict) --*

      - **PublicKeyRotationTimestamp** *(datetime) --*

        (Optional) Only included when public key version has expired
    """


_ClientResolveCustomerResponseTypeDef = TypedDict(
    "_ClientResolveCustomerResponseTypeDef",
    {"CustomerIdentifier": str, "ProductCode": str},
    total=False,
)


class ClientResolveCustomerResponseTypeDef(_ClientResolveCustomerResponseTypeDef):
    """
    - *(dict) --*

      The result of the ResolveCustomer operation. Contains the CustomerIdentifier and product code.
      - **CustomerIdentifier** *(string) --*

        The CustomerIdentifier is used to identify an individual customer in your application. Calls
        to BatchMeterUsage require CustomerIdentifiers for each UsageRecord.
    """
