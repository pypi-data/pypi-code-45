"Main interface for greengrass service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_greengrass.type_defs import (
    ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef,
    ListBulkDeploymentDetailedReportsPaginateResponseTypeDef,
    ListBulkDeploymentsPaginatePaginationConfigTypeDef,
    ListBulkDeploymentsPaginateResponseTypeDef,
    ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef,
    ListConnectorDefinitionVersionsPaginateResponseTypeDef,
    ListConnectorDefinitionsPaginatePaginationConfigTypeDef,
    ListConnectorDefinitionsPaginateResponseTypeDef,
    ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef,
    ListCoreDefinitionVersionsPaginateResponseTypeDef,
    ListCoreDefinitionsPaginatePaginationConfigTypeDef,
    ListCoreDefinitionsPaginateResponseTypeDef,
    ListDeploymentsPaginatePaginationConfigTypeDef,
    ListDeploymentsPaginateResponseTypeDef,
    ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef,
    ListDeviceDefinitionVersionsPaginateResponseTypeDef,
    ListDeviceDefinitionsPaginatePaginationConfigTypeDef,
    ListDeviceDefinitionsPaginateResponseTypeDef,
    ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef,
    ListFunctionDefinitionVersionsPaginateResponseTypeDef,
    ListFunctionDefinitionsPaginatePaginationConfigTypeDef,
    ListFunctionDefinitionsPaginateResponseTypeDef,
    ListGroupVersionsPaginatePaginationConfigTypeDef,
    ListGroupVersionsPaginateResponseTypeDef,
    ListGroupsPaginatePaginationConfigTypeDef,
    ListGroupsPaginateResponseTypeDef,
    ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef,
    ListLoggerDefinitionVersionsPaginateResponseTypeDef,
    ListLoggerDefinitionsPaginatePaginationConfigTypeDef,
    ListLoggerDefinitionsPaginateResponseTypeDef,
    ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef,
    ListResourceDefinitionVersionsPaginateResponseTypeDef,
    ListResourceDefinitionsPaginatePaginationConfigTypeDef,
    ListResourceDefinitionsPaginateResponseTypeDef,
    ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef,
    ListSubscriptionDefinitionVersionsPaginateResponseTypeDef,
    ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef,
    ListSubscriptionDefinitionsPaginateResponseTypeDef,
)


__all__ = (
    "ListBulkDeploymentDetailedReportsPaginator",
    "ListBulkDeploymentsPaginator",
    "ListConnectorDefinitionVersionsPaginator",
    "ListConnectorDefinitionsPaginator",
    "ListCoreDefinitionVersionsPaginator",
    "ListCoreDefinitionsPaginator",
    "ListDeploymentsPaginator",
    "ListDeviceDefinitionVersionsPaginator",
    "ListDeviceDefinitionsPaginator",
    "ListFunctionDefinitionVersionsPaginator",
    "ListFunctionDefinitionsPaginator",
    "ListGroupVersionsPaginator",
    "ListGroupsPaginator",
    "ListLoggerDefinitionVersionsPaginator",
    "ListLoggerDefinitionsPaginator",
    "ListResourceDefinitionVersionsPaginator",
    "ListResourceDefinitionsPaginator",
    "ListSubscriptionDefinitionVersionsPaginator",
    "ListSubscriptionDefinitionsPaginator",
)


class ListBulkDeploymentDetailedReportsPaginator(Boto3Paginator):
    """
    Paginator for `list_bulk_deployment_detailed_reports`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BulkDeploymentId: str,
        PaginationConfig: ListBulkDeploymentDetailedReportsPaginatePaginationConfigTypeDef = None,
    ) -> ListBulkDeploymentDetailedReportsPaginateResponseTypeDef:
        """
        [ListBulkDeploymentDetailedReports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports.paginate)
        """


class ListBulkDeploymentsPaginator(Boto3Paginator):
    """
    Paginator for `list_bulk_deployments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListBulkDeploymentsPaginatePaginationConfigTypeDef = None
    ) -> ListBulkDeploymentsPaginateResponseTypeDef:
        """
        [ListBulkDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeployments.paginate)
        """


class ListConnectorDefinitionVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_connector_definition_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ConnectorDefinitionId: str,
        PaginationConfig: ListConnectorDefinitionVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListConnectorDefinitionVersionsPaginateResponseTypeDef:
        """
        [ListConnectorDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitionVersions.paginate)
        """


class ListConnectorDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `list_connector_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListConnectorDefinitionsPaginatePaginationConfigTypeDef = None
    ) -> ListConnectorDefinitionsPaginateResponseTypeDef:
        """
        [ListConnectorDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitions.paginate)
        """


class ListCoreDefinitionVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_core_definition_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CoreDefinitionId: str,
        PaginationConfig: ListCoreDefinitionVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListCoreDefinitionVersionsPaginateResponseTypeDef:
        """
        [ListCoreDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitionVersions.paginate)
        """


class ListCoreDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `list_core_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListCoreDefinitionsPaginatePaginationConfigTypeDef = None
    ) -> ListCoreDefinitionsPaginateResponseTypeDef:
        """
        [ListCoreDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitions.paginate)
        """


class ListDeploymentsPaginator(Boto3Paginator):
    """
    Paginator for `list_deployments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GroupId: str, PaginationConfig: ListDeploymentsPaginatePaginationConfigTypeDef = None
    ) -> ListDeploymentsPaginateResponseTypeDef:
        """
        [ListDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListDeployments.paginate)
        """


class ListDeviceDefinitionVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_device_definition_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DeviceDefinitionId: str,
        PaginationConfig: ListDeviceDefinitionVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeviceDefinitionVersionsPaginateResponseTypeDef:
        """
        [ListDeviceDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitionVersions.paginate)
        """


class ListDeviceDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `list_device_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDeviceDefinitionsPaginatePaginationConfigTypeDef = None
    ) -> ListDeviceDefinitionsPaginateResponseTypeDef:
        """
        [ListDeviceDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitions.paginate)
        """


class ListFunctionDefinitionVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_function_definition_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        FunctionDefinitionId: str,
        PaginationConfig: ListFunctionDefinitionVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListFunctionDefinitionVersionsPaginateResponseTypeDef:
        """
        [ListFunctionDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitionVersions.paginate)
        """


class ListFunctionDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `list_function_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListFunctionDefinitionsPaginatePaginationConfigTypeDef = None
    ) -> ListFunctionDefinitionsPaginateResponseTypeDef:
        """
        [ListFunctionDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitions.paginate)
        """


class ListGroupVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_group_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GroupId: str,
        PaginationConfig: ListGroupVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListGroupVersionsPaginateResponseTypeDef:
        """
        [ListGroupVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListGroupVersions.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListGroupsPaginatePaginationConfigTypeDef = None
    ) -> ListGroupsPaginateResponseTypeDef:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListGroups.paginate)
        """


class ListLoggerDefinitionVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_logger_definition_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        LoggerDefinitionId: str,
        PaginationConfig: ListLoggerDefinitionVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListLoggerDefinitionVersionsPaginateResponseTypeDef:
        """
        [ListLoggerDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitionVersions.paginate)
        """


class ListLoggerDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `list_logger_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListLoggerDefinitionsPaginatePaginationConfigTypeDef = None
    ) -> ListLoggerDefinitionsPaginateResponseTypeDef:
        """
        [ListLoggerDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitions.paginate)
        """


class ListResourceDefinitionVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_resource_definition_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ResourceDefinitionId: str,
        PaginationConfig: ListResourceDefinitionVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListResourceDefinitionVersionsPaginateResponseTypeDef:
        """
        [ListResourceDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitionVersions.paginate)
        """


class ListResourceDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `list_resource_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListResourceDefinitionsPaginatePaginationConfigTypeDef = None
    ) -> ListResourceDefinitionsPaginateResponseTypeDef:
        """
        [ListResourceDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitions.paginate)
        """


class ListSubscriptionDefinitionVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_subscription_definition_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SubscriptionDefinitionId: str,
        PaginationConfig: ListSubscriptionDefinitionVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListSubscriptionDefinitionVersionsPaginateResponseTypeDef:
        """
        [ListSubscriptionDefinitionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions.paginate)
        """


class ListSubscriptionDefinitionsPaginator(Boto3Paginator):
    """
    Paginator for `list_subscription_definitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListSubscriptionDefinitionsPaginatePaginationConfigTypeDef = None
    ) -> ListSubscriptionDefinitionsPaginateResponseTypeDef:
        """
        [ListSubscriptionDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitions.paginate)
        """
