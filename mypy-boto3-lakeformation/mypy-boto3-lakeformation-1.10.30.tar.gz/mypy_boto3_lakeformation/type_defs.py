"Main interface for lakeformation service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientBatchGrantPermissionsEntriesPrincipalTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTableTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTypeDef",
    "ClientBatchGrantPermissionsEntriesTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresErrorTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresTypeDef",
    "ClientBatchGrantPermissionsResponseTypeDef",
    "ClientBatchRevokePermissionsEntriesPrincipalTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTableTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTypeDef",
    "ClientBatchRevokePermissionsEntriesTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresErrorTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresTypeDef",
    "ClientBatchRevokePermissionsResponseTypeDef",
    "ClientDescribeResourceResponseResourceInfoTypeDef",
    "ClientDescribeResourceResponseTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef",
    "ClientGetDataLakeSettingsResponseTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef",
    "ClientGetEffectivePermissionsForPathResponseTypeDef",
    "ClientGrantPermissionsPrincipalTypeDef",
    "ClientGrantPermissionsResourceDataLocationTypeDef",
    "ClientGrantPermissionsResourceDatabaseTypeDef",
    "ClientGrantPermissionsResourceTableTypeDef",
    "ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientGrantPermissionsResourceTableWithColumnsTypeDef",
    "ClientGrantPermissionsResourceTypeDef",
    "ClientListPermissionsPrincipalTypeDef",
    "ClientListPermissionsResourceDataLocationTypeDef",
    "ClientListPermissionsResourceDatabaseTypeDef",
    "ClientListPermissionsResourceTableTypeDef",
    "ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientListPermissionsResourceTableWithColumnsTypeDef",
    "ClientListPermissionsResourceTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef",
    "ClientListPermissionsResponseTypeDef",
    "ClientListResourcesFilterConditionListTypeDef",
    "ClientListResourcesResponseResourceInfoListTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsTypeDef",
    "ClientRevokePermissionsPrincipalTypeDef",
    "ClientRevokePermissionsResourceDataLocationTypeDef",
    "ClientRevokePermissionsResourceDatabaseTypeDef",
    "ClientRevokePermissionsResourceTableTypeDef",
    "ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientRevokePermissionsResourceTableWithColumnsTypeDef",
    "ClientRevokePermissionsResourceTypeDef",
)


_ClientBatchGrantPermissionsEntriesPrincipalTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientBatchGrantPermissionsEntriesPrincipalTypeDef(
    _ClientBatchGrantPermissionsEntriesPrincipalTypeDef
):
    pass


_ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)


class ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef
):
    pass


_ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef", {"Name": str}, total=False
)


class ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef
):
    pass


_ClientBatchGrantPermissionsEntriesResourceTableTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)


class ClientBatchGrantPermissionsEntriesResourceTableTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceTableTypeDef
):
    pass


_ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef
):
    pass


_ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef
):
    pass


_ClientBatchGrantPermissionsEntriesResourceTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef,
        "Table": ClientBatchGrantPermissionsEntriesResourceTableTypeDef,
        "TableWithColumns": ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientBatchGrantPermissionsEntriesResourceTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceTypeDef
):
    pass


_RequiredClientBatchGrantPermissionsEntriesTypeDef = TypedDict(
    "_RequiredClientBatchGrantPermissionsEntriesTypeDef", {"Id": str}
)
_OptionalClientBatchGrantPermissionsEntriesTypeDef = TypedDict(
    "_OptionalClientBatchGrantPermissionsEntriesTypeDef",
    {
        "Principal": ClientBatchGrantPermissionsEntriesPrincipalTypeDef,
        "Resource": ClientBatchGrantPermissionsEntriesResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientBatchGrantPermissionsEntriesTypeDef(
    _RequiredClientBatchGrantPermissionsEntriesTypeDef,
    _OptionalClientBatchGrantPermissionsEntriesTypeDef,
):
    """
    - *(dict) --*

      A permission to a resource granted by batch operation to the principal.
      - **Id** *(string) --***[REQUIRED]**

        A unique identifier for the batch permissions request entry.
    """


_ClientBatchGrantPermissionsResponseFailuresErrorTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresErrorTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresErrorTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresErrorTypeDef
):
    pass


_ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef
):
    pass


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef
):
    pass


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef
):
    pass


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef
):
    pass


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef
):
    pass


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef
):
    pass


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef,
        "Table": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef,
        "TableWithColumns": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef
):
    pass


_ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef",
    {
        "Id": str,
        "Principal": ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef,
        "Resource": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef
):
    """
    - **RequestEntry** *(dict) --*

      An identifier for an entry of the batch request.
      - **Id** *(string) --*

        A unique identifier for the batch permissions request entry.
    """


_ClientBatchGrantPermissionsResponseFailuresTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresTypeDef",
    {
        "RequestEntry": ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef,
        "Error": ClientBatchGrantPermissionsResponseFailuresErrorTypeDef,
    },
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresTypeDef
):
    """
    - *(dict) --*

      A list of failures when performing a batch grant or batch revoke operation.
      - **RequestEntry** *(dict) --*

        An identifier for an entry of the batch request.
        - **Id** *(string) --*

          A unique identifier for the batch permissions request entry.
    """


_ClientBatchGrantPermissionsResponseTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseTypeDef",
    {"Failures": List[ClientBatchGrantPermissionsResponseFailuresTypeDef]},
    total=False,
)


class ClientBatchGrantPermissionsResponseTypeDef(_ClientBatchGrantPermissionsResponseTypeDef):
    """
    - *(dict) --*

      - **Failures** *(list) --*

        A list of failures to grant permissions to the resources.
        - *(dict) --*

          A list of failures when performing a batch grant or batch revoke operation.
          - **RequestEntry** *(dict) --*

            An identifier for an entry of the batch request.
            - **Id** *(string) --*

              A unique identifier for the batch permissions request entry.
    """


_ClientBatchRevokePermissionsEntriesPrincipalTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientBatchRevokePermissionsEntriesPrincipalTypeDef(
    _ClientBatchRevokePermissionsEntriesPrincipalTypeDef
):
    pass


_ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)


class ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef
):
    pass


_ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef", {"Name": str}, total=False
)


class ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef
):
    pass


_ClientBatchRevokePermissionsEntriesResourceTableTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)


class ClientBatchRevokePermissionsEntriesResourceTableTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceTableTypeDef
):
    pass


_ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef
):
    pass


_ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef
):
    pass


_ClientBatchRevokePermissionsEntriesResourceTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef,
        "Table": ClientBatchRevokePermissionsEntriesResourceTableTypeDef,
        "TableWithColumns": ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientBatchRevokePermissionsEntriesResourceTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceTypeDef
):
    pass


_RequiredClientBatchRevokePermissionsEntriesTypeDef = TypedDict(
    "_RequiredClientBatchRevokePermissionsEntriesTypeDef", {"Id": str}
)
_OptionalClientBatchRevokePermissionsEntriesTypeDef = TypedDict(
    "_OptionalClientBatchRevokePermissionsEntriesTypeDef",
    {
        "Principal": ClientBatchRevokePermissionsEntriesPrincipalTypeDef,
        "Resource": ClientBatchRevokePermissionsEntriesResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientBatchRevokePermissionsEntriesTypeDef(
    _RequiredClientBatchRevokePermissionsEntriesTypeDef,
    _OptionalClientBatchRevokePermissionsEntriesTypeDef,
):
    """
    - *(dict) --*

      A permission to a resource granted by batch operation to the principal.
      - **Id** *(string) --***[REQUIRED]**

        A unique identifier for the batch permissions request entry.
    """


_ClientBatchRevokePermissionsResponseFailuresErrorTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresErrorTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresErrorTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresErrorTypeDef
):
    pass


_ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef
):
    pass


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef
):
    pass


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef
):
    pass


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef
):
    pass


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef
):
    pass


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef
):
    pass


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef,
        "Table": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef,
        "TableWithColumns": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef
):
    pass


_ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef",
    {
        "Id": str,
        "Principal": ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef,
        "Resource": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef
):
    """
    - **RequestEntry** *(dict) --*

      An identifier for an entry of the batch request.
      - **Id** *(string) --*

        A unique identifier for the batch permissions request entry.
    """


_ClientBatchRevokePermissionsResponseFailuresTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresTypeDef",
    {
        "RequestEntry": ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef,
        "Error": ClientBatchRevokePermissionsResponseFailuresErrorTypeDef,
    },
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresTypeDef
):
    """
    - *(dict) --*

      A list of failures when performing a batch grant or batch revoke operation.
      - **RequestEntry** *(dict) --*

        An identifier for an entry of the batch request.
        - **Id** *(string) --*

          A unique identifier for the batch permissions request entry.
    """


_ClientBatchRevokePermissionsResponseTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseTypeDef",
    {"Failures": List[ClientBatchRevokePermissionsResponseFailuresTypeDef]},
    total=False,
)


class ClientBatchRevokePermissionsResponseTypeDef(_ClientBatchRevokePermissionsResponseTypeDef):
    """
    - *(dict) --*

      - **Failures** *(list) --*

        A list of failures to revoke permissions to the resources.
        - *(dict) --*

          A list of failures when performing a batch grant or batch revoke operation.
          - **RequestEntry** *(dict) --*

            An identifier for an entry of the batch request.
            - **Id** *(string) --*

              A unique identifier for the batch permissions request entry.
    """


_ClientDescribeResourceResponseResourceInfoTypeDef = TypedDict(
    "_ClientDescribeResourceResponseResourceInfoTypeDef",
    {"ResourceArn": str, "RoleArn": str, "LastModified": datetime},
    total=False,
)


class ClientDescribeResourceResponseResourceInfoTypeDef(
    _ClientDescribeResourceResponseResourceInfoTypeDef
):
    """
    - **ResourceInfo** *(dict) --*

      A structure containing information about an AWS Lake Formation resource.
      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource.
    """


_ClientDescribeResourceResponseTypeDef = TypedDict(
    "_ClientDescribeResourceResponseTypeDef",
    {"ResourceInfo": ClientDescribeResourceResponseResourceInfoTypeDef},
    total=False,
)


class ClientDescribeResourceResponseTypeDef(_ClientDescribeResourceResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceInfo** *(dict) --*

        A structure containing information about an AWS Lake Formation resource.
        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource.
    """


_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef
):
    pass


_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    {
        "Principal": ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef
):
    pass


_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef
):
    pass


_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef
):
    pass


_ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef
):
    """
    - *(dict) --*

      The AWS Lake Formation principal.
      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.
    """


_ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": List[
            ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef
        ],
        "CreateDatabaseDefaultPermissions": List[
            ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef
        ],
        "CreateTableDefaultPermissions": List[
            ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef
):
    """
    - **DataLakeSettings** *(dict) --*

      A list of AWS Lake Formation principals.
      - **DataLakeAdmins** *(list) --*

        A list of AWS Lake Formation principals.
        - *(dict) --*

          The AWS Lake Formation principal.
          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.
    """


_ClientGetDataLakeSettingsResponseTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseTypeDef",
    {"DataLakeSettings": ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef},
    total=False,
)


class ClientGetDataLakeSettingsResponseTypeDef(_ClientGetDataLakeSettingsResponseTypeDef):
    """
    - *(dict) --*

      - **DataLakeSettings** *(dict) --*

        A list of AWS Lake Formation principals.
        - **DataLakeAdmins** *(list) --*

          A list of AWS Lake Formation principals.
          - *(dict) --*

            The AWS Lake Formation principal.
            - **DataLakePrincipalIdentifier** *(string) --*

              An identifier for the AWS Lake Formation principal.
    """


_ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef
):
    """
    - **Principal** *(dict) --*

      The Data Lake principal to be granted or revoked permissions.
      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.
    """


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef
):
    pass


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef
):
    pass


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef
):
    pass


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef
):
    pass


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef
):
    pass


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef,
        "Table": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef,
        "TableWithColumns": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef
):
    pass


_ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef",
    {
        "Principal": ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef,
        "Resource": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef
):
    """
    - *(dict) --*

      The permissions granted or revoked on a resource.
      - **Principal** *(dict) --*

        The Data Lake principal to be granted or revoked permissions.
        - **DataLakePrincipalIdentifier** *(string) --*

          An identifier for the AWS Lake Formation principal.
    """


_ClientGetEffectivePermissionsForPathResponseTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponseTypeDef",
    {
        "Permissions": List[ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientGetEffectivePermissionsForPathResponseTypeDef(
    _ClientGetEffectivePermissionsForPathResponseTypeDef
):
    """
    - *(dict) --*

      - **Permissions** *(list) --*

        A list of the permissions for the specified table or database resource located at the path
        in Amazon S3.
        - *(dict) --*

          The permissions granted or revoked on a resource.
          - **Principal** *(dict) --*

            The Data Lake principal to be granted or revoked permissions.
            - **DataLakePrincipalIdentifier** *(string) --*

              An identifier for the AWS Lake Formation principal.
    """


_ClientGrantPermissionsPrincipalTypeDef = TypedDict(
    "_ClientGrantPermissionsPrincipalTypeDef", {"DataLakePrincipalIdentifier": str}, total=False
)


class ClientGrantPermissionsPrincipalTypeDef(_ClientGrantPermissionsPrincipalTypeDef):
    """
    The principal to be granted the permissions on the resource. Supported principals are IAM users
    or IAM roles, and they are defined by their principal type and their ARN.
    Note that if you define a resource with a particular ARN, then later delete, and recreate a
    resource with that same ARN, the resource maintains the permissions already granted.
    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientGrantPermissionsResourceDataLocationTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceDataLocationTypeDef", {"ResourceArn": str}, total=False
)


class ClientGrantPermissionsResourceDataLocationTypeDef(
    _ClientGrantPermissionsResourceDataLocationTypeDef
):
    pass


_ClientGrantPermissionsResourceDatabaseTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceDatabaseTypeDef", {"Name": str}, total=False
)


class ClientGrantPermissionsResourceDatabaseTypeDef(_ClientGrantPermissionsResourceDatabaseTypeDef):
    pass


_ClientGrantPermissionsResourceTableTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceTableTypeDef", {"DatabaseName": str, "Name": str}, total=False
)


class ClientGrantPermissionsResourceTableTypeDef(_ClientGrantPermissionsResourceTableTypeDef):
    pass


_ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef
):
    pass


_ClientGrantPermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientGrantPermissionsResourceTableWithColumnsTypeDef(
    _ClientGrantPermissionsResourceTableWithColumnsTypeDef
):
    pass


_ClientGrantPermissionsResourceTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientGrantPermissionsResourceDatabaseTypeDef,
        "Table": ClientGrantPermissionsResourceTableTypeDef,
        "TableWithColumns": ClientGrantPermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientGrantPermissionsResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientGrantPermissionsResourceTypeDef(_ClientGrantPermissionsResourceTypeDef):
    """
    The resource to which permissions are to be granted. Resources in AWS Lake Formation are the
    Data Catalog, databases, and tables.
    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
      persistent metadata store. It contains database definitions, table definitions, and other
      control information to manage your AWS Lake Formation environment.
    """


_ClientListPermissionsPrincipalTypeDef = TypedDict(
    "_ClientListPermissionsPrincipalTypeDef", {"DataLakePrincipalIdentifier": str}, total=False
)


class ClientListPermissionsPrincipalTypeDef(_ClientListPermissionsPrincipalTypeDef):
    """
    Specifies a principal to filter the permissions returned.
    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientListPermissionsResourceDataLocationTypeDef = TypedDict(
    "_ClientListPermissionsResourceDataLocationTypeDef", {"ResourceArn": str}, total=False
)


class ClientListPermissionsResourceDataLocationTypeDef(
    _ClientListPermissionsResourceDataLocationTypeDef
):
    pass


_ClientListPermissionsResourceDatabaseTypeDef = TypedDict(
    "_ClientListPermissionsResourceDatabaseTypeDef", {"Name": str}, total=False
)


class ClientListPermissionsResourceDatabaseTypeDef(_ClientListPermissionsResourceDatabaseTypeDef):
    pass


_ClientListPermissionsResourceTableTypeDef = TypedDict(
    "_ClientListPermissionsResourceTableTypeDef", {"DatabaseName": str, "Name": str}, total=False
)


class ClientListPermissionsResourceTableTypeDef(_ClientListPermissionsResourceTableTypeDef):
    pass


_ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef
):
    pass


_ClientListPermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientListPermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientListPermissionsResourceTableWithColumnsTypeDef(
    _ClientListPermissionsResourceTableWithColumnsTypeDef
):
    pass


_ClientListPermissionsResourceTypeDef = TypedDict(
    "_ClientListPermissionsResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientListPermissionsResourceDatabaseTypeDef,
        "Table": ClientListPermissionsResourceTableTypeDef,
        "TableWithColumns": ClientListPermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientListPermissionsResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientListPermissionsResourceTypeDef(_ClientListPermissionsResourceTypeDef):
    """
    A resource where you will get a list of the principal permissions.
    This operation does not support getting privileges on a table with columns. Instead, call this
    operation on the table, and the operation returns the table and the table w columns.
    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
      persistent metadata store. It contains database definitions, table definitions, and other
      control information to manage your AWS Lake Formation environment.
    """


_ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef
):
    """
    - **Principal** *(dict) --*

      The Data Lake principal to be granted or revoked permissions.
      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.
    """


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef
):
    pass


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef
):
    pass


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef
):
    pass


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef
):
    pass


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef
):
    pass


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef,
        "Table": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef,
        "TableWithColumns": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef
):
    pass


_ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef",
    {
        "Principal": ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef,
        "Resource": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef
):
    """
    - *(dict) --*

      The permissions granted or revoked on a resource.
      - **Principal** *(dict) --*

        The Data Lake principal to be granted or revoked permissions.
        - **DataLakePrincipalIdentifier** *(string) --*

          An identifier for the AWS Lake Formation principal.
    """


_ClientListPermissionsResponseTypeDef = TypedDict(
    "_ClientListPermissionsResponseTypeDef",
    {
        "PrincipalResourcePermissions": List[
            ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPermissionsResponseTypeDef(_ClientListPermissionsResponseTypeDef):
    """
    - *(dict) --*

      - **PrincipalResourcePermissions** *(list) --*

        A list of principals and their permissions on the resource for the specified principal and
        resource types.
        - *(dict) --*

          The permissions granted or revoked on a resource.
          - **Principal** *(dict) --*

            The Data Lake principal to be granted or revoked permissions.
            - **DataLakePrincipalIdentifier** *(string) --*

              An identifier for the AWS Lake Formation principal.
    """


_ClientListResourcesFilterConditionListTypeDef = TypedDict(
    "_ClientListResourcesFilterConditionListTypeDef",
    {
        "Field": Literal["RESOURCE_ARN", "ROLE_ARN", "LAST_MODIFIED"],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "LE",
            "LT",
            "GE",
            "GT",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
            "IN",
            "BETWEEN",
        ],
        "StringValueList": List[str],
    },
    total=False,
)


class ClientListResourcesFilterConditionListTypeDef(_ClientListResourcesFilterConditionListTypeDef):
    """
    - *(dict) --*

      This structure describes the filtering of columns in a table based on a filter condition.
      - **Field** *(string) --*

        The field to filter in the filter condition.
    """


_ClientListResourcesResponseResourceInfoListTypeDef = TypedDict(
    "_ClientListResourcesResponseResourceInfoListTypeDef",
    {"ResourceArn": str, "RoleArn": str, "LastModified": datetime},
    total=False,
)


class ClientListResourcesResponseResourceInfoListTypeDef(
    _ClientListResourcesResponseResourceInfoListTypeDef
):
    """
    - *(dict) --*

      A structure containing information about an AWS Lake Formation resource.
      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource.
    """


_ClientListResourcesResponseTypeDef = TypedDict(
    "_ClientListResourcesResponseTypeDef",
    {
        "ResourceInfoList": List[ClientListResourcesResponseResourceInfoListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourcesResponseTypeDef(_ClientListResourcesResponseTypeDef):
    """
    - *(dict) --*

      - **ResourceInfoList** *(list) --*

        A summary of the data lake resources.
        - *(dict) --*

          A structure containing information about an AWS Lake Formation resource.
          - **ResourceArn** *(string) --*

            The Amazon Resource Name (ARN) of the resource.
    """


_ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef
):
    pass


_ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    {
        "Principal": ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef
):
    pass


_ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef
):
    pass


_ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef
):
    pass


_ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef
):
    """
    - *(dict) --*

      The AWS Lake Formation principal.
      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.
    """


_ClientPutDataLakeSettingsDataLakeSettingsTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": List[ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef],
        "CreateDatabaseDefaultPermissions": List[
            ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef
        ],
        "CreateTableDefaultPermissions": List[
            ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsTypeDef
):
    """
    A list of AWS Lake Formation principals.
    - **DataLakeAdmins** *(list) --*

      A list of AWS Lake Formation principals.
      - *(dict) --*

        The AWS Lake Formation principal.
        - **DataLakePrincipalIdentifier** *(string) --*

          An identifier for the AWS Lake Formation principal.
    """


_ClientRevokePermissionsPrincipalTypeDef = TypedDict(
    "_ClientRevokePermissionsPrincipalTypeDef", {"DataLakePrincipalIdentifier": str}, total=False
)


class ClientRevokePermissionsPrincipalTypeDef(_ClientRevokePermissionsPrincipalTypeDef):
    """
    The principal to be revoked permissions on the resource.
    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientRevokePermissionsResourceDataLocationTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceDataLocationTypeDef", {"ResourceArn": str}, total=False
)


class ClientRevokePermissionsResourceDataLocationTypeDef(
    _ClientRevokePermissionsResourceDataLocationTypeDef
):
    pass


_ClientRevokePermissionsResourceDatabaseTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceDatabaseTypeDef", {"Name": str}, total=False
)


class ClientRevokePermissionsResourceDatabaseTypeDef(
    _ClientRevokePermissionsResourceDatabaseTypeDef
):
    pass


_ClientRevokePermissionsResourceTableTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceTableTypeDef", {"DatabaseName": str, "Name": str}, total=False
)


class ClientRevokePermissionsResourceTableTypeDef(_ClientRevokePermissionsResourceTableTypeDef):
    pass


_ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef
):
    pass


_ClientRevokePermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientRevokePermissionsResourceTableWithColumnsTypeDef(
    _ClientRevokePermissionsResourceTableWithColumnsTypeDef
):
    pass


_ClientRevokePermissionsResourceTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientRevokePermissionsResourceDatabaseTypeDef,
        "Table": ClientRevokePermissionsResourceTableTypeDef,
        "TableWithColumns": ClientRevokePermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientRevokePermissionsResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientRevokePermissionsResourceTypeDef(_ClientRevokePermissionsResourceTypeDef):
    """
    The resource to which permissions are to be revoked.
    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
      persistent metadata store. It contains database definitions, table definitions, and other
      control information to manage your AWS Lake Formation environment.
    """
