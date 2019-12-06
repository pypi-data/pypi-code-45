"Main interface for sagemaker-runtime service type defs"
from __future__ import annotations

import sys
from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ClientInvokeEndpointResponseTypeDef = TypedDict(
    "ClientInvokeEndpointResponseTypeDef",
    {
        "Body": StreamingBody,
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
    },
    total=False,
)
