"Main interface for sagemaker-runtime service type defs"
from __future__ import annotations

from botocore.response import StreamingBody
from mypy_boto3.type_defs import TypedDict


__all__ = ("ClientInvokeEndpointResponseTypeDef",)


_ClientInvokeEndpointResponseTypeDef = TypedDict(
    "_ClientInvokeEndpointResponseTypeDef",
    {
        "Body": StreamingBody,
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
    },
    total=False,
)


class ClientInvokeEndpointResponseTypeDef(_ClientInvokeEndpointResponseTypeDef):
    """
    - *(dict) --*

      - **Body** (:class:`.StreamingBody`) --

        Includes the inference provided by the model.
        For information about the format of the response body, see `Common Data Formats—Inference
        <https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html>`__ .
    """
