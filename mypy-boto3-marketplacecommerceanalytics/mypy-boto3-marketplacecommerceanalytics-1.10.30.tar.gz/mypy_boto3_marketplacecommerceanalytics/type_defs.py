"Main interface for marketplacecommerceanalytics service type defs"
from __future__ import annotations

from mypy_boto3.type_defs import TypedDict


__all__ = ("ClientGenerateDataSetResponseTypeDef", "ClientStartSupportDataExportResponseTypeDef")


_ClientGenerateDataSetResponseTypeDef = TypedDict(
    "_ClientGenerateDataSetResponseTypeDef", {"dataSetRequestId": str}, total=False
)


class ClientGenerateDataSetResponseTypeDef(_ClientGenerateDataSetResponseTypeDef):
    """
    - *(dict) --*Container for the result of the GenerateDataSet operation.

      - **dataSetRequestId** *(string) --*A unique identifier representing a specific request to the
      GenerateDataSet operation. This identifier can be used to correlate a request with
      notifications from the SNS topic.
    """


_ClientStartSupportDataExportResponseTypeDef = TypedDict(
    "_ClientStartSupportDataExportResponseTypeDef", {"dataSetRequestId": str}, total=False
)


class ClientStartSupportDataExportResponseTypeDef(_ClientStartSupportDataExportResponseTypeDef):
    """
    - *(dict) --*Container for the result of the StartSupportDataExport operation.

      - **dataSetRequestId** *(string) --*A unique identifier representing a specific request to the
      StartSupportDataExport operation. This identifier can be used to correlate a request with
      notifications from the SNS topic.
    """
