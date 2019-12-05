"Main interface for iot1click-devices service Paginators"
from __future__ import annotations

from datetime import datetime
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iot1click_devices.type_defs import (
    ListDeviceEventsPaginatePaginationConfigTypeDef,
    ListDeviceEventsPaginateResponseTypeDef,
    ListDevicesPaginatePaginationConfigTypeDef,
    ListDevicesPaginateResponseTypeDef,
)


__all__ = ("ListDeviceEventsPaginator", "ListDevicesPaginator")


class ListDeviceEventsPaginator(Boto3Paginator):
    """
    Paginator for `list_device_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        PaginationConfig: ListDeviceEventsPaginatePaginationConfigTypeDef = None,
    ) -> ListDeviceEventsPaginateResponseTypeDef:
        """
        [ListDeviceEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDeviceEvents.paginate)
        """


class ListDevicesPaginator(Boto3Paginator):
    """
    Paginator for `list_devices`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DeviceType: str = None,
        PaginationConfig: ListDevicesPaginatePaginationConfigTypeDef = None,
    ) -> ListDevicesPaginateResponseTypeDef:
        """
        [ListDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDevices.paginate)
        """
