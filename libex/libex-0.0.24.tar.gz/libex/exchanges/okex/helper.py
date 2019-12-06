from ...const import OrderType, OrderStatus

# ACTIVE, EXECUTED, PARTIALLY FILLED, CANCELED, RSN_DUST (amount is less than 0.00000001), RSN_PAUSE (trading is paused / paused due to AMPL rebase event)
def rslv_order_status(native_status):
    native_status = str(native_status)

    if '-2' == native_status:
        return OrderStatus.FAILED
    elif '-1' == native_status:
        return OrderStatus.CANCELED
    elif '0' == native_status:
        return OrderStatus.UNFILLED
    elif '1' == native_status:
        return OrderStatus.PARTFILLED
    elif '2' == native_status:
        return OrderStatus.FULLFILLED
    elif '3' == native_status:
        return OrderStatus.PLACING
    elif '4' == native_status:
        return OrderStatus.CANCELING
    else:
        return OrderStatus.UNKNOWN


def rslv_order_type(native_type, native_order_type):
    native_order_type = str(native_order_type)
    if 'limit' == native_type:
        if '0' == native_order_type:
            return OrderType.Limit

        elif '1' == native_order_type:
            return OrderType.Unknown
        elif '2' == native_order_type:
            return OrderType.Unknown
        elif '3' == native_order_type:
            return OrderType.IOC
        else:
            return OrderType.Unknown

    elif 'market' == native_type:
        return OrderType.market
    else:
        return OrderType.Unknown

def rslv_symbol(native_symbol):

    symbol = native_symbol.split('-')
    coin = symbol[0].lower()
    currency = symbol[1].lower()

    return (coin,currency)

