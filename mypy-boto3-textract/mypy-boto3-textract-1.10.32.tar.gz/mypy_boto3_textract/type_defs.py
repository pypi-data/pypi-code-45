"Main interface for textract service type defs"
from __future__ import annotations

from typing import Any, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientAnalyzeDocumentDocumentS3ObjectTypeDef",
    "ClientAnalyzeDocumentDocumentTypeDef",
    "ClientAnalyzeDocumentHumanLoopConfigDataAttributesTypeDef",
    "ClientAnalyzeDocumentHumanLoopConfigTypeDef",
    "ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef",
    "ClientAnalyzeDocumentResponseBlocksGeometryTypeDef",
    "ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef",
    "ClientAnalyzeDocumentResponseBlocksTypeDef",
    "ClientAnalyzeDocumentResponseDocumentMetadataTypeDef",
    "ClientAnalyzeDocumentResponseHumanLoopActivationOutputTypeDef",
    "ClientAnalyzeDocumentResponseTypeDef",
    "ClientDetectDocumentTextDocumentS3ObjectTypeDef",
    "ClientDetectDocumentTextDocumentTypeDef",
    "ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef",
    "ClientDetectDocumentTextResponseBlocksGeometryTypeDef",
    "ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef",
    "ClientDetectDocumentTextResponseBlocksTypeDef",
    "ClientDetectDocumentTextResponseDocumentMetadataTypeDef",
    "ClientDetectDocumentTextResponseTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksTypeDef",
    "ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef",
    "ClientGetDocumentAnalysisResponseWarningsTypeDef",
    "ClientGetDocumentAnalysisResponseTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksTypeDef",
    "ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef",
    "ClientGetDocumentTextDetectionResponseWarningsTypeDef",
    "ClientGetDocumentTextDetectionResponseTypeDef",
    "ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef",
    "ClientStartDocumentAnalysisDocumentLocationTypeDef",
    "ClientStartDocumentAnalysisNotificationChannelTypeDef",
    "ClientStartDocumentAnalysisResponseTypeDef",
    "ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef",
    "ClientStartDocumentTextDetectionDocumentLocationTypeDef",
    "ClientStartDocumentTextDetectionNotificationChannelTypeDef",
    "ClientStartDocumentTextDetectionResponseTypeDef",
)


_ClientAnalyzeDocumentDocumentS3ObjectTypeDef = TypedDict(
    "_ClientAnalyzeDocumentDocumentS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientAnalyzeDocumentDocumentS3ObjectTypeDef(_ClientAnalyzeDocumentDocumentS3ObjectTypeDef):
    pass


_ClientAnalyzeDocumentDocumentTypeDef = TypedDict(
    "_ClientAnalyzeDocumentDocumentTypeDef",
    {"Bytes": bytes, "S3Object": ClientAnalyzeDocumentDocumentS3ObjectTypeDef},
    total=False,
)


class ClientAnalyzeDocumentDocumentTypeDef(_ClientAnalyzeDocumentDocumentTypeDef):
    """
    The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to
    call Amazon Textract operations, you can't pass image bytes. The document must be an image in
    JPEG or PNG format.
    If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image
    bytes that are passed using the ``Bytes`` field.
    - **Bytes** *(bytes) --*

      A blob of base64-encoded document bytes. The maximum size of a document that's provided in a
      blob of bytes is 5 MB. The document bytes must be in PNG or JPEG format.
      If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image
      bytes passed using the ``Bytes`` field.
    """


_ClientAnalyzeDocumentHumanLoopConfigDataAttributesTypeDef = TypedDict(
    "_ClientAnalyzeDocumentHumanLoopConfigDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)


class ClientAnalyzeDocumentHumanLoopConfigDataAttributesTypeDef(
    _ClientAnalyzeDocumentHumanLoopConfigDataAttributesTypeDef
):
    pass


_RequiredClientAnalyzeDocumentHumanLoopConfigTypeDef = TypedDict(
    "_RequiredClientAnalyzeDocumentHumanLoopConfigTypeDef", {"HumanLoopName": str}
)
_OptionalClientAnalyzeDocumentHumanLoopConfigTypeDef = TypedDict(
    "_OptionalClientAnalyzeDocumentHumanLoopConfigTypeDef",
    {
        "FlowDefinitionArn": str,
        "DataAttributes": ClientAnalyzeDocumentHumanLoopConfigDataAttributesTypeDef,
    },
    total=False,
)


class ClientAnalyzeDocumentHumanLoopConfigTypeDef(
    _RequiredClientAnalyzeDocumentHumanLoopConfigTypeDef,
    _OptionalClientAnalyzeDocumentHumanLoopConfigTypeDef,
):
    """
    Sets the configuration for the human in the loop workflow for analyzing documents.
    - **HumanLoopName** *(string) --***[REQUIRED]**

      The name of the human workflow used for this image. This should be kept unique within a
      region.
    """


_ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef(
    _ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef
):
    pass


_ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef", {"X": Any, "Y": Any}, total=False
)


class ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef(
    _ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef
):
    pass


_ClientAnalyzeDocumentResponseBlocksGeometryTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)


class ClientAnalyzeDocumentResponseBlocksGeometryTypeDef(
    _ClientAnalyzeDocumentResponseBlocksGeometryTypeDef
):
    pass


_ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef",
    {"Type": Literal["VALUE", "CHILD"], "Ids": List[str]},
    total=False,
)


class ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef(
    _ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef
):
    pass


_ClientAnalyzeDocumentResponseBlocksTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseBlocksTypeDef",
    {
        "BlockType": Literal[
            "KEY_VALUE_SET", "PAGE", "LINE", "WORD", "TABLE", "CELL", "SELECTION_ELEMENT"
        ],
        "Confidence": Any,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientAnalyzeDocumentResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef],
        "EntityTypes": List[Literal["KEY", "VALUE"]],
        "SelectionStatus": Literal["SELECTED", "NOT_SELECTED"],
        "Page": int,
    },
    total=False,
)


class ClientAnalyzeDocumentResponseBlocksTypeDef(_ClientAnalyzeDocumentResponseBlocksTypeDef):
    pass


_ClientAnalyzeDocumentResponseDocumentMetadataTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseDocumentMetadataTypeDef", {"Pages": int}, total=False
)


class ClientAnalyzeDocumentResponseDocumentMetadataTypeDef(
    _ClientAnalyzeDocumentResponseDocumentMetadataTypeDef
):
    """
    - **DocumentMetadata** *(dict) --*

      Metadata about the analyzed document. An example is the number of pages.
      - **Pages** *(integer) --*

        The number of pages that are detected in the document.
    """


_ClientAnalyzeDocumentResponseHumanLoopActivationOutputTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseHumanLoopActivationOutputTypeDef",
    {
        "HumanLoopArn": str,
        "HumanLoopActivationReasons": List[str],
        "HumanLoopActivationConditionsEvaluationResults": str,
    },
    total=False,
)


class ClientAnalyzeDocumentResponseHumanLoopActivationOutputTypeDef(
    _ClientAnalyzeDocumentResponseHumanLoopActivationOutputTypeDef
):
    pass


_ClientAnalyzeDocumentResponseTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseTypeDef",
    {
        "DocumentMetadata": ClientAnalyzeDocumentResponseDocumentMetadataTypeDef,
        "Blocks": List[ClientAnalyzeDocumentResponseBlocksTypeDef],
        "HumanLoopActivationOutput": ClientAnalyzeDocumentResponseHumanLoopActivationOutputTypeDef,
        "AnalyzeDocumentModelVersion": str,
    },
    total=False,
)


class ClientAnalyzeDocumentResponseTypeDef(_ClientAnalyzeDocumentResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentMetadata** *(dict) --*

        Metadata about the analyzed document. An example is the number of pages.
        - **Pages** *(integer) --*

          The number of pages that are detected in the document.
    """


_ClientDetectDocumentTextDocumentS3ObjectTypeDef = TypedDict(
    "_ClientDetectDocumentTextDocumentS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectDocumentTextDocumentS3ObjectTypeDef(
    _ClientDetectDocumentTextDocumentS3ObjectTypeDef
):
    pass


_ClientDetectDocumentTextDocumentTypeDef = TypedDict(
    "_ClientDetectDocumentTextDocumentTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectDocumentTextDocumentS3ObjectTypeDef},
    total=False,
)


class ClientDetectDocumentTextDocumentTypeDef(_ClientDetectDocumentTextDocumentTypeDef):
    """
    The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to
    call Amazon Textract operations, you can't pass image bytes. The document must be an image in
    JPEG or PNG format.
    If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image
    bytes that are passed using the ``Bytes`` field.
    - **Bytes** *(bytes) --*

      A blob of base64-encoded document bytes. The maximum size of a document that's provided in a
      blob of bytes is 5 MB. The document bytes must be in PNG or JPEG format.
      If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image
      bytes passed using the ``Bytes`` field.
    """


_ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef(
    _ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef
):
    pass


_ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef",
    {"X": Any, "Y": Any},
    total=False,
)


class ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef(
    _ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef
):
    pass


_ClientDetectDocumentTextResponseBlocksGeometryTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)


class ClientDetectDocumentTextResponseBlocksGeometryTypeDef(
    _ClientDetectDocumentTextResponseBlocksGeometryTypeDef
):
    pass


_ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef",
    {"Type": Literal["VALUE", "CHILD"], "Ids": List[str]},
    total=False,
)


class ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef(
    _ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef
):
    pass


_ClientDetectDocumentTextResponseBlocksTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseBlocksTypeDef",
    {
        "BlockType": Literal[
            "KEY_VALUE_SET", "PAGE", "LINE", "WORD", "TABLE", "CELL", "SELECTION_ELEMENT"
        ],
        "Confidence": Any,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientDetectDocumentTextResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef],
        "EntityTypes": List[Literal["KEY", "VALUE"]],
        "SelectionStatus": Literal["SELECTED", "NOT_SELECTED"],
        "Page": int,
    },
    total=False,
)


class ClientDetectDocumentTextResponseBlocksTypeDef(_ClientDetectDocumentTextResponseBlocksTypeDef):
    pass


_ClientDetectDocumentTextResponseDocumentMetadataTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseDocumentMetadataTypeDef", {"Pages": int}, total=False
)


class ClientDetectDocumentTextResponseDocumentMetadataTypeDef(
    _ClientDetectDocumentTextResponseDocumentMetadataTypeDef
):
    """
    - **DocumentMetadata** *(dict) --*

      Metadata about the document. It contains the number of pages that are detected in the
      document.
      - **Pages** *(integer) --*

        The number of pages that are detected in the document.
    """


_ClientDetectDocumentTextResponseTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseTypeDef",
    {
        "DocumentMetadata": ClientDetectDocumentTextResponseDocumentMetadataTypeDef,
        "Blocks": List[ClientDetectDocumentTextResponseBlocksTypeDef],
        "DetectDocumentTextModelVersion": str,
    },
    total=False,
)


class ClientDetectDocumentTextResponseTypeDef(_ClientDetectDocumentTextResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentMetadata** *(dict) --*

        Metadata about the document. It contains the number of pages that are detected in the
        document.
        - **Pages** *(integer) --*

          The number of pages that are detected in the document.
    """


_ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef(
    _ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef
):
    pass


_ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef",
    {"X": Any, "Y": Any},
    total=False,
)


class ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef(
    _ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef
):
    pass


_ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)


class ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef(
    _ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef
):
    pass


_ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef",
    {"Type": Literal["VALUE", "CHILD"], "Ids": List[str]},
    total=False,
)


class ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef(
    _ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef
):
    pass


_ClientGetDocumentAnalysisResponseBlocksTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseBlocksTypeDef",
    {
        "BlockType": Literal[
            "KEY_VALUE_SET", "PAGE", "LINE", "WORD", "TABLE", "CELL", "SELECTION_ELEMENT"
        ],
        "Confidence": Any,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef],
        "EntityTypes": List[Literal["KEY", "VALUE"]],
        "SelectionStatus": Literal["SELECTED", "NOT_SELECTED"],
        "Page": int,
    },
    total=False,
)


class ClientGetDocumentAnalysisResponseBlocksTypeDef(
    _ClientGetDocumentAnalysisResponseBlocksTypeDef
):
    pass


_ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef", {"Pages": int}, total=False
)


class ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef(
    _ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef
):
    """
    - **DocumentMetadata** *(dict) --*

      Information about a document that Amazon Textract processed. ``DocumentMetadata`` is returned
      in every page of paginated responses from an Amazon Textract video operation.
      - **Pages** *(integer) --*

        The number of pages that are detected in the document.
    """


_ClientGetDocumentAnalysisResponseWarningsTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseWarningsTypeDef",
    {"ErrorCode": str, "Pages": List[int]},
    total=False,
)


class ClientGetDocumentAnalysisResponseWarningsTypeDef(
    _ClientGetDocumentAnalysisResponseWarningsTypeDef
):
    pass


_ClientGetDocumentAnalysisResponseTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseTypeDef",
    {
        "DocumentMetadata": ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef,
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED", "PARTIAL_SUCCESS"],
        "NextToken": str,
        "Blocks": List[ClientGetDocumentAnalysisResponseBlocksTypeDef],
        "Warnings": List[ClientGetDocumentAnalysisResponseWarningsTypeDef],
        "StatusMessage": str,
        "AnalyzeDocumentModelVersion": str,
    },
    total=False,
)


class ClientGetDocumentAnalysisResponseTypeDef(_ClientGetDocumentAnalysisResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentMetadata** *(dict) --*

        Information about a document that Amazon Textract processed. ``DocumentMetadata`` is
        returned in every page of paginated responses from an Amazon Textract video operation.
        - **Pages** *(integer) --*

          The number of pages that are detected in the document.
    """


_ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": Any, "Height": Any, "Left": Any, "Top": Any},
    total=False,
)


class ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef(
    _ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef
):
    pass


_ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef",
    {"X": Any, "Y": Any},
    total=False,
)


class ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef(
    _ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef
):
    pass


_ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)


class ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef(
    _ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef
):
    pass


_ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef",
    {"Type": Literal["VALUE", "CHILD"], "Ids": List[str]},
    total=False,
)


class ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef(
    _ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef
):
    pass


_ClientGetDocumentTextDetectionResponseBlocksTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseBlocksTypeDef",
    {
        "BlockType": Literal[
            "KEY_VALUE_SET", "PAGE", "LINE", "WORD", "TABLE", "CELL", "SELECTION_ELEMENT"
        ],
        "Confidence": Any,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef],
        "EntityTypes": List[Literal["KEY", "VALUE"]],
        "SelectionStatus": Literal["SELECTED", "NOT_SELECTED"],
        "Page": int,
    },
    total=False,
)


class ClientGetDocumentTextDetectionResponseBlocksTypeDef(
    _ClientGetDocumentTextDetectionResponseBlocksTypeDef
):
    pass


_ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef", {"Pages": int}, total=False
)


class ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef(
    _ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef
):
    """
    - **DocumentMetadata** *(dict) --*

      Information about a document that Amazon Textract processed. ``DocumentMetadata`` is returned
      in every page of paginated responses from an Amazon Textract video operation.
      - **Pages** *(integer) --*

        The number of pages that are detected in the document.
    """


_ClientGetDocumentTextDetectionResponseWarningsTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseWarningsTypeDef",
    {"ErrorCode": str, "Pages": List[int]},
    total=False,
)


class ClientGetDocumentTextDetectionResponseWarningsTypeDef(
    _ClientGetDocumentTextDetectionResponseWarningsTypeDef
):
    pass


_ClientGetDocumentTextDetectionResponseTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseTypeDef",
    {
        "DocumentMetadata": ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef,
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED", "PARTIAL_SUCCESS"],
        "NextToken": str,
        "Blocks": List[ClientGetDocumentTextDetectionResponseBlocksTypeDef],
        "Warnings": List[ClientGetDocumentTextDetectionResponseWarningsTypeDef],
        "StatusMessage": str,
        "DetectDocumentTextModelVersion": str,
    },
    total=False,
)


class ClientGetDocumentTextDetectionResponseTypeDef(_ClientGetDocumentTextDetectionResponseTypeDef):
    """
    - *(dict) --*

      - **DocumentMetadata** *(dict) --*

        Information about a document that Amazon Textract processed. ``DocumentMetadata`` is
        returned in every page of paginated responses from an Amazon Textract video operation.
        - **Pages** *(integer) --*

          The number of pages that are detected in the document.
    """


_ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef = TypedDict(
    "_ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef(
    _ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef
):
    """
    - **S3Object** *(dict) --*

      The Amazon S3 bucket that contains the input document.
      - **Bucket** *(string) --*

        The name of the S3 bucket.
    """


_ClientStartDocumentAnalysisDocumentLocationTypeDef = TypedDict(
    "_ClientStartDocumentAnalysisDocumentLocationTypeDef",
    {"S3Object": ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef},
    total=False,
)


class ClientStartDocumentAnalysisDocumentLocationTypeDef(
    _ClientStartDocumentAnalysisDocumentLocationTypeDef
):
    """
    The location of the document to be processed.
    - **S3Object** *(dict) --*

      The Amazon S3 bucket that contains the input document.
      - **Bucket** *(string) --*

        The name of the S3 bucket.
    """


_RequiredClientStartDocumentAnalysisNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartDocumentAnalysisNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartDocumentAnalysisNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartDocumentAnalysisNotificationChannelTypeDef", {"RoleArn": str}, total=False
)


class ClientStartDocumentAnalysisNotificationChannelTypeDef(
    _RequiredClientStartDocumentAnalysisNotificationChannelTypeDef,
    _OptionalClientStartDocumentAnalysisNotificationChannelTypeDef,
):
    """
    The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the
    operation to.
    - **SNSTopicArn** *(string) --***[REQUIRED]**

      The Amazon SNS topic that Amazon Textract posts the completion status to.
    """


_ClientStartDocumentAnalysisResponseTypeDef = TypedDict(
    "_ClientStartDocumentAnalysisResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartDocumentAnalysisResponseTypeDef(_ClientStartDocumentAnalysisResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier for the document text detection job. Use ``JobId`` to identify the job in a
        subsequent call to ``GetDocumentAnalysis`` . A ``JobId`` value is only valid for 7 days.
    """


_ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef = TypedDict(
    "_ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef(
    _ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef
):
    """
    - **S3Object** *(dict) --*

      The Amazon S3 bucket that contains the input document.
      - **Bucket** *(string) --*

        The name of the S3 bucket.
    """


_ClientStartDocumentTextDetectionDocumentLocationTypeDef = TypedDict(
    "_ClientStartDocumentTextDetectionDocumentLocationTypeDef",
    {"S3Object": ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef},
    total=False,
)


class ClientStartDocumentTextDetectionDocumentLocationTypeDef(
    _ClientStartDocumentTextDetectionDocumentLocationTypeDef
):
    """
    The location of the document to be processed.
    - **S3Object** *(dict) --*

      The Amazon S3 bucket that contains the input document.
      - **Bucket** *(string) --*

        The name of the S3 bucket.
    """


_RequiredClientStartDocumentTextDetectionNotificationChannelTypeDef = TypedDict(
    "_RequiredClientStartDocumentTextDetectionNotificationChannelTypeDef", {"SNSTopicArn": str}
)
_OptionalClientStartDocumentTextDetectionNotificationChannelTypeDef = TypedDict(
    "_OptionalClientStartDocumentTextDetectionNotificationChannelTypeDef",
    {"RoleArn": str},
    total=False,
)


class ClientStartDocumentTextDetectionNotificationChannelTypeDef(
    _RequiredClientStartDocumentTextDetectionNotificationChannelTypeDef,
    _OptionalClientStartDocumentTextDetectionNotificationChannelTypeDef,
):
    """
    The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the
    operation to.
    - **SNSTopicArn** *(string) --***[REQUIRED]**

      The Amazon SNS topic that Amazon Textract posts the completion status to.
    """


_ClientStartDocumentTextDetectionResponseTypeDef = TypedDict(
    "_ClientStartDocumentTextDetectionResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartDocumentTextDetectionResponseTypeDef(
    _ClientStartDocumentTextDetectionResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier of the text detection job for the document. Use ``JobId`` to identify the job
        in a subsequent call to ``GetDocumentTextDetection`` . A ``JobId`` value is only valid for 7
        days.
    """
