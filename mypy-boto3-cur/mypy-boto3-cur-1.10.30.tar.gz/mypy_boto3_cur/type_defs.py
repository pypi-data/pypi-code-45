"Main interface for cur service type defs"
from __future__ import annotations

from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDeleteReportDefinitionResponseTypeDef",
    "ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef",
    "ClientDescribeReportDefinitionsResponseTypeDef",
    "ClientModifyReportDefinitionReportDefinitionTypeDef",
    "ClientPutReportDefinitionReportDefinitionTypeDef",
    "DescribeReportDefinitionsPaginatePaginationConfigTypeDef",
    "DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef",
    "DescribeReportDefinitionsPaginateResponseTypeDef",
)


_ClientDeleteReportDefinitionResponseTypeDef = TypedDict(
    "_ClientDeleteReportDefinitionResponseTypeDef", {"ResponseMessage": str}, total=False
)


class ClientDeleteReportDefinitionResponseTypeDef(_ClientDeleteReportDefinitionResponseTypeDef):
    """
    - *(dict) --*

      If the action is successful, the service sends back an HTTP 200 response.
      - **ResponseMessage** *(string) --*

        Whether the deletion was successful or not.
    """


_ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef = TypedDict(
    "_ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef",
    {
        "ReportName": str,
        "TimeUnit": Literal["HOURLY", "DAILY"],
        "Format": Literal["textORcsv", "Parquet"],
        "Compression": Literal["ZIP", "GZIP", "Parquet"],
        "AdditionalSchemaElements": List[str],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": Literal[
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "eu-central-1",
            "eu-west-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "eu-north-1",
            "ap-northeast-3",
            "ap-east-1",
        ],
        "AdditionalArtifacts": List[Literal["REDSHIFT", "QUICKSIGHT", "ATHENA"]],
        "RefreshClosedReports": bool,
        "ReportVersioning": Literal["CREATE_NEW_REPORT", "OVERWRITE_REPORT"],
    },
    total=False,
)


class ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef(
    _ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef
):
    """
    - *(dict) --*

      The definition of AWS Cost and Usage Report. You can specify the report name, time unit,
      report format, compression format, S3 bucket, additional artifacts, and schema elements in the
      definition.
      - **ReportName** *(string) --*

        The name of the report that you want to create. The name must be unique, is case sensitive,
        and can't include spaces.
    """


_ClientDescribeReportDefinitionsResponseTypeDef = TypedDict(
    "_ClientDescribeReportDefinitionsResponseTypeDef",
    {
        "ReportDefinitions": List[ClientDescribeReportDefinitionsResponseReportDefinitionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeReportDefinitionsResponseTypeDef(
    _ClientDescribeReportDefinitionsResponseTypeDef
):
    """
    - *(dict) --*

      If the action is successful, the service sends back an HTTP 200 response.
      - **ReportDefinitions** *(list) --*

        A list of AWS Cost and Usage reports owned by the account.
        - *(dict) --*

          The definition of AWS Cost and Usage Report. You can specify the report name, time unit,
          report format, compression format, S3 bucket, additional artifacts, and schema elements in
          the definition.
          - **ReportName** *(string) --*

            The name of the report that you want to create. The name must be unique, is case
            sensitive, and can't include spaces.
    """


_RequiredClientModifyReportDefinitionReportDefinitionTypeDef = TypedDict(
    "_RequiredClientModifyReportDefinitionReportDefinitionTypeDef", {"ReportName": str}
)
_OptionalClientModifyReportDefinitionReportDefinitionTypeDef = TypedDict(
    "_OptionalClientModifyReportDefinitionReportDefinitionTypeDef",
    {
        "TimeUnit": Literal["HOURLY", "DAILY"],
        "Format": Literal["textORcsv", "Parquet"],
        "Compression": Literal["ZIP", "GZIP", "Parquet"],
        "AdditionalSchemaElements": List[str],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": Literal[
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "eu-central-1",
            "eu-west-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "eu-north-1",
            "ap-northeast-3",
            "ap-east-1",
        ],
        "AdditionalArtifacts": List[Literal["REDSHIFT", "QUICKSIGHT", "ATHENA"]],
        "RefreshClosedReports": bool,
        "ReportVersioning": Literal["CREATE_NEW_REPORT", "OVERWRITE_REPORT"],
    },
    total=False,
)


class ClientModifyReportDefinitionReportDefinitionTypeDef(
    _RequiredClientModifyReportDefinitionReportDefinitionTypeDef,
    _OptionalClientModifyReportDefinitionReportDefinitionTypeDef,
):
    """
    The definition of AWS Cost and Usage Report. You can specify the report name, time unit, report
    format, compression format, S3 bucket, additional artifacts, and schema elements in the
    definition.
    - **ReportName** *(string) --***[REQUIRED]**

      The name of the report that you want to create. The name must be unique, is case sensitive,
      and can't include spaces.
    """


_RequiredClientPutReportDefinitionReportDefinitionTypeDef = TypedDict(
    "_RequiredClientPutReportDefinitionReportDefinitionTypeDef", {"ReportName": str}
)
_OptionalClientPutReportDefinitionReportDefinitionTypeDef = TypedDict(
    "_OptionalClientPutReportDefinitionReportDefinitionTypeDef",
    {
        "TimeUnit": Literal["HOURLY", "DAILY"],
        "Format": Literal["textORcsv", "Parquet"],
        "Compression": Literal["ZIP", "GZIP", "Parquet"],
        "AdditionalSchemaElements": List[str],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": Literal[
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "eu-central-1",
            "eu-west-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "eu-north-1",
            "ap-northeast-3",
            "ap-east-1",
        ],
        "AdditionalArtifacts": List[Literal["REDSHIFT", "QUICKSIGHT", "ATHENA"]],
        "RefreshClosedReports": bool,
        "ReportVersioning": Literal["CREATE_NEW_REPORT", "OVERWRITE_REPORT"],
    },
    total=False,
)


class ClientPutReportDefinitionReportDefinitionTypeDef(
    _RequiredClientPutReportDefinitionReportDefinitionTypeDef,
    _OptionalClientPutReportDefinitionReportDefinitionTypeDef,
):
    """
    Represents the output of the PutReportDefinition operation. The content consists of the detailed
    metadata and data file information.
    - **ReportName** *(string) --***[REQUIRED]**

      The name of the report that you want to create. The name must be unique, is case sensitive,
      and can't include spaces.
    """


_DescribeReportDefinitionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeReportDefinitionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeReportDefinitionsPaginatePaginationConfigTypeDef(
    _DescribeReportDefinitionsPaginatePaginationConfigTypeDef
):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef = TypedDict(
    "_DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef",
    {
        "ReportName": str,
        "TimeUnit": Literal["HOURLY", "DAILY"],
        "Format": Literal["textORcsv", "Parquet"],
        "Compression": Literal["ZIP", "GZIP", "Parquet"],
        "AdditionalSchemaElements": List[str],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": Literal[
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "eu-central-1",
            "eu-west-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "eu-north-1",
            "ap-northeast-3",
            "ap-east-1",
        ],
        "AdditionalArtifacts": List[Literal["REDSHIFT", "QUICKSIGHT", "ATHENA"]],
        "RefreshClosedReports": bool,
        "ReportVersioning": Literal["CREATE_NEW_REPORT", "OVERWRITE_REPORT"],
    },
    total=False,
)


class DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef(
    _DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef
):
    """
    - *(dict) --*

      The definition of AWS Cost and Usage Report. You can specify the report name, time unit,
      report format, compression format, S3 bucket, additional artifacts, and schema elements in the
      definition.
      - **ReportName** *(string) --*

        The name of the report that you want to create. The name must be unique, is case sensitive,
        and can't include spaces.
    """


_DescribeReportDefinitionsPaginateResponseTypeDef = TypedDict(
    "_DescribeReportDefinitionsPaginateResponseTypeDef",
    {"ReportDefinitions": List[DescribeReportDefinitionsPaginateResponseReportDefinitionsTypeDef]},
    total=False,
)


class DescribeReportDefinitionsPaginateResponseTypeDef(
    _DescribeReportDefinitionsPaginateResponseTypeDef
):
    """
    - *(dict) --*

      If the action is successful, the service sends back an HTTP 200 response.
      - **ReportDefinitions** *(list) --*

        A list of AWS Cost and Usage reports owned by the account.
        - *(dict) --*

          The definition of AWS Cost and Usage Report. You can specify the report name, time unit,
          report format, compression format, S3 bucket, additional artifacts, and schema elements in
          the definition.
          - **ReportName** *(string) --*

            The name of the report that you want to create. The name must be unique, is case
            sensitive, and can't include spaces.
    """
