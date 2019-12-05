"Main interface for schemas service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_schemas.type_defs import (
    ListDiscoverersPaginatePaginationConfigTypeDef,
    ListDiscoverersPaginateResponseTypeDef,
    ListRegistriesPaginatePaginationConfigTypeDef,
    ListRegistriesPaginateResponseTypeDef,
    ListSchemaVersionsPaginatePaginationConfigTypeDef,
    ListSchemaVersionsPaginateResponseTypeDef,
    ListSchemasPaginatePaginationConfigTypeDef,
    ListSchemasPaginateResponseTypeDef,
    SearchSchemasPaginatePaginationConfigTypeDef,
    SearchSchemasPaginateResponseTypeDef,
)


__all__ = (
    "ListDiscoverersPaginator",
    "ListRegistriesPaginator",
    "ListSchemaVersionsPaginator",
    "ListSchemasPaginator",
    "SearchSchemasPaginator",
)


class ListDiscoverersPaginator(Boto3Paginator):
    """
    Paginator for `list_discoverers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DiscovererIdPrefix: str = None,
        SourceArnPrefix: str = None,
        PaginationConfig: ListDiscoverersPaginatePaginationConfigTypeDef = None,
    ) -> ListDiscoverersPaginateResponseTypeDef:
        """
        [ListDiscoverers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/schemas.html#Schemas.Paginator.ListDiscoverers.paginate)
        """


class ListRegistriesPaginator(Boto3Paginator):
    """
    Paginator for `list_registries`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RegistryNamePrefix: str = None,
        Scope: str = None,
        PaginationConfig: ListRegistriesPaginatePaginationConfigTypeDef = None,
    ) -> ListRegistriesPaginateResponseTypeDef:
        """
        [ListRegistries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/schemas.html#Schemas.Paginator.ListRegistries.paginate)
        """


class ListSchemaVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_schema_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RegistryName: str,
        SchemaName: str,
        PaginationConfig: ListSchemaVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListSchemaVersionsPaginateResponseTypeDef:
        """
        [ListSchemaVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/schemas.html#Schemas.Paginator.ListSchemaVersions.paginate)
        """


class ListSchemasPaginator(Boto3Paginator):
    """
    Paginator for `list_schemas`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        RegistryName: str,
        SchemaNamePrefix: str = None,
        PaginationConfig: ListSchemasPaginatePaginationConfigTypeDef = None,
    ) -> ListSchemasPaginateResponseTypeDef:
        """
        [ListSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/schemas.html#Schemas.Paginator.ListSchemas.paginate)
        """


class SearchSchemasPaginator(Boto3Paginator):
    """
    Paginator for `search_schemas`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Keywords: str,
        RegistryName: str,
        PaginationConfig: SearchSchemasPaginatePaginationConfigTypeDef = None,
    ) -> SearchSchemasPaginateResponseTypeDef:
        """
        [SearchSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/schemas.html#Schemas.Paginator.SearchSchemas.paginate)
        """
