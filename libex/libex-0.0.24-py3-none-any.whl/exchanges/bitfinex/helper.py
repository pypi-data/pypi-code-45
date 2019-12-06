import logging

from ...const import OrderType,OrderStatus

logger = logging.getLogger(__name__)

# ACTIVE, EXECUTED, PARTIALLY FILLED, CANCELED, RSN_DUST (amount is less than 0.00000001), RSN_PAUSE (trading is paused / paused due to AMPL rebase event)
def rslv_order_status(native_status):

    if 'ACTIVE' == native_status:
        return OrderStatus.UNFILLED
    elif 'EXECUTED' == native_status:
        return OrderStatus.FULLFILLED
    elif 'PARTIALLY FILLED' == native_status:
        return OrderStatus.PARTFILLED
    elif 'CANCELED' == native_status:
        return OrderStatus.CANCELED
    elif 'IOC CANCELED' == native_status:
        return OrderStatus.CANCELED
    elif native_status.startswith('EXECUTED '):
        return OrderStatus.FULLFILLED

    elif 'RSN_DUST' == native_status:
        return OrderStatus.UNKNOWN
    elif 'RSN_PAUSE' == native_status:
        return OrderStatus.UNKNOWN

    else:
        logger.warning('Unknown Native Status: %s', native_status)
        return OrderStatus.UNKNOWN


def rslv_order_type(native_type):
    if 'EXCHANGE IOC' == native_type:
        return OrderType.IOC
    elif 'EXCHANGE LIMIT' == native_type:
        return OrderType.Limit
    else:
        logger.warning('Unknown Native Type: %s', native_type)
        return OrderType.Unknown
