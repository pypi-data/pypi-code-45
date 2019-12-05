"Main interface for devicefarm service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_devicefarm.type_defs import (
    GetOfferingStatusPaginatePaginationConfigTypeDef,
    GetOfferingStatusPaginateResponseTypeDef,
    ListArtifactsPaginatePaginationConfigTypeDef,
    ListArtifactsPaginateResponseTypeDef,
    ListDeviceInstancesPaginatePaginationConfigTypeDef,
    ListDeviceInstancesPaginateResponseTypeDef,
    ListDevicePoolsPaginatePaginationConfigTypeDef,
    ListDevicePoolsPaginateResponseTypeDef,
    ListDevicesPaginateFiltersTypeDef,
    ListDevicesPaginatePaginationConfigTypeDef,
    ListDevicesPaginateResponseTypeDef,
    ListInstanceProfilesPaginatePaginationConfigTypeDef,
    ListInstanceProfilesPaginateResponseTypeDef,
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
    ListNetworkProfilesPaginatePaginationConfigTypeDef,
    ListNetworkProfilesPaginateResponseTypeDef,
    ListOfferingPromotionsPaginatePaginationConfigTypeDef,
    ListOfferingPromotionsPaginateResponseTypeDef,
    ListOfferingTransactionsPaginatePaginationConfigTypeDef,
    ListOfferingTransactionsPaginateResponseTypeDef,
    ListOfferingsPaginatePaginationConfigTypeDef,
    ListOfferingsPaginateResponseTypeDef,
    ListProjectsPaginatePaginationConfigTypeDef,
    ListProjectsPaginateResponseTypeDef,
    ListRemoteAccessSessionsPaginatePaginationConfigTypeDef,
    ListRemoteAccessSessionsPaginateResponseTypeDef,
    ListRunsPaginatePaginationConfigTypeDef,
    ListRunsPaginateResponseTypeDef,
    ListSamplesPaginatePaginationConfigTypeDef,
    ListSamplesPaginateResponseTypeDef,
    ListSuitesPaginatePaginationConfigTypeDef,
    ListSuitesPaginateResponseTypeDef,
    ListTestsPaginatePaginationConfigTypeDef,
    ListTestsPaginateResponseTypeDef,
    ListUniqueProblemsPaginatePaginationConfigTypeDef,
    ListUniqueProblemsPaginateResponseTypeDef,
    ListUploadsPaginatePaginationConfigTypeDef,
    ListUploadsPaginateResponseTypeDef,
    ListVPCEConfigurationsPaginatePaginationConfigTypeDef,
    ListVPCEConfigurationsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetOfferingStatusPaginator",
    "ListArtifactsPaginator",
    "ListDeviceInstancesPaginator",
    "ListDevicePoolsPaginator",
    "ListDevicesPaginator",
    "ListInstanceProfilesPaginator",
    "ListJobsPaginator",
    "ListNetworkProfilesPaginator",
    "ListOfferingPromotionsPaginator",
    "ListOfferingTransactionsPaginator",
    "ListOfferingsPaginator",
    "ListProjectsPaginator",
    "ListRemoteAccessSessionsPaginator",
    "ListRunsPaginator",
    "ListSamplesPaginator",
    "ListSuitesPaginator",
    "ListTestsPaginator",
    "ListUniqueProblemsPaginator",
    "ListUploadsPaginator",
    "ListVPCEConfigurationsPaginator",
)


class GetOfferingStatusPaginator(Boto3Paginator):
    """
    Paginator for `get_offering_status`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetOfferingStatusPaginatePaginationConfigTypeDef = None
    ) -> GetOfferingStatusPaginateResponseTypeDef:
        """
        [GetOfferingStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.GetOfferingStatus.paginate)
        """


class ListArtifactsPaginator(Boto3Paginator):
    """
    Paginator for `list_artifacts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str,
        type: Literal["SCREENSHOT", "FILE", "LOG"],
        PaginationConfig: ListArtifactsPaginatePaginationConfigTypeDef = None,
    ) -> ListArtifactsPaginateResponseTypeDef:
        """
        [ListArtifacts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListArtifacts.paginate)
        """


class ListDeviceInstancesPaginator(Boto3Paginator):
    """
    Paginator for `list_device_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListDeviceInstancesPaginatePaginationConfigTypeDef = None
    ) -> ListDeviceInstancesPaginateResponseTypeDef:
        """
        [ListDeviceInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDeviceInstances.paginate)
        """


class ListDevicePoolsPaginator(Boto3Paginator):
    """
    Paginator for `list_device_pools`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str,
        type: Literal["CURATED", "PRIVATE"] = None,
        PaginationConfig: ListDevicePoolsPaginatePaginationConfigTypeDef = None,
    ) -> ListDevicePoolsPaginateResponseTypeDef:
        """
        [ListDevicePools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevicePools.paginate)
        """


class ListDevicesPaginator(Boto3Paginator):
    """
    Paginator for `list_devices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str = None,
        filters: List[ListDevicesPaginateFiltersTypeDef] = None,
        PaginationConfig: ListDevicesPaginatePaginationConfigTypeDef = None,
    ) -> ListDevicesPaginateResponseTypeDef:
        """
        [ListDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevices.paginate)
        """


class ListInstanceProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_instance_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListInstanceProfilesPaginatePaginationConfigTypeDef = None
    ) -> ListInstanceProfilesPaginateResponseTypeDef:
        """
        [ListInstanceProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListInstanceProfiles.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None
    ) -> ListJobsPaginateResponseTypeDef:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListJobs.paginate)
        """


class ListNetworkProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_network_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str,
        type: Literal["CURATED", "PRIVATE"] = None,
        PaginationConfig: ListNetworkProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListNetworkProfilesPaginateResponseTypeDef:
        """
        [ListNetworkProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListNetworkProfiles.paginate)
        """


class ListOfferingPromotionsPaginator(Boto3Paginator):
    """
    Paginator for `list_offering_promotions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListOfferingPromotionsPaginatePaginationConfigTypeDef = None
    ) -> ListOfferingPromotionsPaginateResponseTypeDef:
        """
        [ListOfferingPromotions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingPromotions.paginate)
        """


class ListOfferingTransactionsPaginator(Boto3Paginator):
    """
    Paginator for `list_offering_transactions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListOfferingTransactionsPaginatePaginationConfigTypeDef = None
    ) -> ListOfferingTransactionsPaginateResponseTypeDef:
        """
        [ListOfferingTransactions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingTransactions.paginate)
        """


class ListOfferingsPaginator(Boto3Paginator):
    """
    Paginator for `list_offerings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListOfferingsPaginatePaginationConfigTypeDef = None
    ) -> ListOfferingsPaginateResponseTypeDef:
        """
        [ListOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferings.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    Paginator for `list_projects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str = None, PaginationConfig: ListProjectsPaginatePaginationConfigTypeDef = None
    ) -> ListProjectsPaginateResponseTypeDef:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListProjects.paginate)
        """


class ListRemoteAccessSessionsPaginator(Boto3Paginator):
    """
    Paginator for `list_remote_access_sessions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str,
        PaginationConfig: ListRemoteAccessSessionsPaginatePaginationConfigTypeDef = None,
    ) -> ListRemoteAccessSessionsPaginateResponseTypeDef:
        """
        [ListRemoteAccessSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRemoteAccessSessions.paginate)
        """


class ListRunsPaginator(Boto3Paginator):
    """
    Paginator for `list_runs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: ListRunsPaginatePaginationConfigTypeDef = None
    ) -> ListRunsPaginateResponseTypeDef:
        """
        [ListRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRuns.paginate)
        """


class ListSamplesPaginator(Boto3Paginator):
    """
    Paginator for `list_samples`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: ListSamplesPaginatePaginationConfigTypeDef = None
    ) -> ListSamplesPaginateResponseTypeDef:
        """
        [ListSamples.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSamples.paginate)
        """


class ListSuitesPaginator(Boto3Paginator):
    """
    Paginator for `list_suites`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: ListSuitesPaginatePaginationConfigTypeDef = None
    ) -> ListSuitesPaginateResponseTypeDef:
        """
        [ListSuites.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSuites.paginate)
        """


class ListTestsPaginator(Boto3Paginator):
    """
    Paginator for `list_tests`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: ListTestsPaginatePaginationConfigTypeDef = None
    ) -> ListTestsPaginateResponseTypeDef:
        """
        [ListTests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListTests.paginate)
        """


class ListUniqueProblemsPaginator(Boto3Paginator):
    """
    Paginator for `list_unique_problems`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, arn: str, PaginationConfig: ListUniqueProblemsPaginatePaginationConfigTypeDef = None
    ) -> ListUniqueProblemsPaginateResponseTypeDef:
        """
        [ListUniqueProblems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUniqueProblems.paginate)
        """


class ListUploadsPaginator(Boto3Paginator):
    """
    Paginator for `list_uploads`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        arn: str,
        type: Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ] = None,
        PaginationConfig: ListUploadsPaginatePaginationConfigTypeDef = None,
    ) -> ListUploadsPaginateResponseTypeDef:
        """
        [ListUploads.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUploads.paginate)
        """


class ListVPCEConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `list_vpce_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListVPCEConfigurationsPaginatePaginationConfigTypeDef = None
    ) -> ListVPCEConfigurationsPaginateResponseTypeDef:
        """
        [ListVPCEConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/devicefarm.html#DeviceFarm.Paginator.ListVPCEConfigurations.paginate)
        """
