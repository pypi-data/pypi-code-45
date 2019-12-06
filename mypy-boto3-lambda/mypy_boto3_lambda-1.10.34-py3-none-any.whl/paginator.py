"Main interface for lambda service Paginators"
from __future__ import annotations

import sys
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_lambda.type_defs import (
    ListAliasesPaginatePaginationConfigTypeDef,
    ListAliasesPaginateResponseTypeDef,
    ListEventSourceMappingsPaginatePaginationConfigTypeDef,
    ListEventSourceMappingsPaginateResponseTypeDef,
    ListFunctionEventInvokeConfigsPaginatePaginationConfigTypeDef,
    ListFunctionEventInvokeConfigsPaginateResponseTypeDef,
    ListFunctionsPaginatePaginationConfigTypeDef,
    ListFunctionsPaginateResponseTypeDef,
    ListLayerVersionsPaginatePaginationConfigTypeDef,
    ListLayerVersionsPaginateResponseTypeDef,
    ListLayersPaginatePaginationConfigTypeDef,
    ListLayersPaginateResponseTypeDef,
    ListProvisionedConcurrencyConfigsPaginatePaginationConfigTypeDef,
    ListProvisionedConcurrencyConfigsPaginateResponseTypeDef,
    ListVersionsByFunctionPaginatePaginationConfigTypeDef,
    ListVersionsByFunctionPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAliasesPaginator",
    "ListEventSourceMappingsPaginator",
    "ListFunctionEventInvokeConfigsPaginator",
    "ListFunctionsPaginator",
    "ListLayerVersionsPaginator",
    "ListLayersPaginator",
    "ListProvisionedConcurrencyConfigsPaginator",
    "ListVersionsByFunctionPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    Paginator for `list_aliases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FunctionName: str,
        FunctionVersion: str = None,
        PaginationConfig: ListAliasesPaginatePaginationConfigTypeDef = None,
    ) -> ListAliasesPaginateResponseTypeDef:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListAliases.paginate)
        """


class ListEventSourceMappingsPaginator(Boto3Paginator):
    """
    Paginator for `list_event_source_mappings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EventSourceArn: str = None,
        FunctionName: str = None,
        PaginationConfig: ListEventSourceMappingsPaginatePaginationConfigTypeDef = None,
    ) -> ListEventSourceMappingsPaginateResponseTypeDef:
        """
        [ListEventSourceMappings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListEventSourceMappings.paginate)
        """


class ListFunctionEventInvokeConfigsPaginator(Boto3Paginator):
    """
    Paginator for `list_function_event_invoke_configs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FunctionName: str,
        PaginationConfig: ListFunctionEventInvokeConfigsPaginatePaginationConfigTypeDef = None,
    ) -> ListFunctionEventInvokeConfigsPaginateResponseTypeDef:
        """
        [ListFunctionEventInvokeConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListFunctionEventInvokeConfigs.paginate)
        """


class ListFunctionsPaginator(Boto3Paginator):
    """
    Paginator for `list_functions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        MasterRegion: str = None,
        FunctionVersion: str = None,
        PaginationConfig: ListFunctionsPaginatePaginationConfigTypeDef = None,
    ) -> ListFunctionsPaginateResponseTypeDef:
        """
        [ListFunctions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListFunctions.paginate)
        """


class ListLayerVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_layer_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LayerName: str,
        CompatibleRuntime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ] = None,
        PaginationConfig: ListLayerVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListLayerVersionsPaginateResponseTypeDef:
        """
        [ListLayerVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListLayerVersions.paginate)
        """


class ListLayersPaginator(Boto3Paginator):
    """
    Paginator for `list_layers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CompatibleRuntime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ] = None,
        PaginationConfig: ListLayersPaginatePaginationConfigTypeDef = None,
    ) -> ListLayersPaginateResponseTypeDef:
        """
        [ListLayers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListLayers.paginate)
        """


class ListProvisionedConcurrencyConfigsPaginator(Boto3Paginator):
    """
    Paginator for `list_provisioned_concurrency_configs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FunctionName: str,
        PaginationConfig: ListProvisionedConcurrencyConfigsPaginatePaginationConfigTypeDef = None,
    ) -> ListProvisionedConcurrencyConfigsPaginateResponseTypeDef:
        """
        [ListProvisionedConcurrencyConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListProvisionedConcurrencyConfigs.paginate)
        """


class ListVersionsByFunctionPaginator(Boto3Paginator):
    """
    Paginator for `list_versions_by_function`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FunctionName: str,
        PaginationConfig: ListVersionsByFunctionPaginatePaginationConfigTypeDef = None,
    ) -> ListVersionsByFunctionPaginateResponseTypeDef:
        """
        [ListVersionsByFunction.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/lambda.html#Lambda.Paginator.ListVersionsByFunction.paginate)
        """
