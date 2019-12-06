"Main interface for marketplacecommerceanalytics service type defs"
from __future__ import annotations

import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientGenerateDataSetResponseTypeDef = TypedDict(
    "ClientGenerateDataSetResponseTypeDef", {"dataSetRequestId": str}, total=False
)

ClientStartSupportDataExportResponseTypeDef = TypedDict(
    "ClientStartSupportDataExportResponseTypeDef", {"dataSetRequestId": str}, total=False
)
