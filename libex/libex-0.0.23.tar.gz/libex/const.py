from enum import Enum


class Channel(Enum):

    ticker  = 'ticker'
    trade   = 'trade'
    book    = 'book'
    book5   = 'book5'
    book10   = 'book10'
    book20   = 'book20'
    candle1h    = 'candle1h'
    candle5m    = 'candle5m'

    @classmethod
    def rslv(cls,value):

        print('value: ' + value)

        if value == Channel.ticker.value:
            return Channel.ticker
        elif value == Channel.trade.value:
            return Channel.trade

        elif value == Channel.book.value:
            return Channel.book
            
        elif value == Channel.book5.value:
            return Channel.book5
        elif value == Channel.book10.value:
            return Channel.book10
        elif value == Channel.book20.value:
            return Channel.book20

        elif value == Channel.candle1h.value:
            return Channel.candle1h
        elif value == Channel.candle5m.value:

            return Channel.candle5m
        else:
            raise ValueError


class OrderType(Enum):
    Limit = 'limit'
    Market = 'market'
    IOC = 'ioc'
    Unknown = 'unknown'
    
class OrderStatus(Enum):

    FAILED      = 'failed'
    CANCELED    = 'canceled'

    UNFILLED    = 'unfilled'
    PARTFILLED  = 'partfilled'
    FULLFILLED  = 'filled'
    PLACING     = 'placing'
    CANCELING   = 'canceling'

    UNKNOWN = 'unknown'
    
    def rslv(value):

        if value == OrderStatus.FAILED.value:
            return OrderStatus.FAILED
        elif value == OrderStatus.CANCELED.value:
            return OrderStatus.CANCELED
        elif value == OrderStatus.UNFILLED.value:
            return OrderStatus.UNFILLED
        elif value == OrderStatus.PARTFILLED.value:
            return OrderStatus.PARTFILLED
        elif value == OrderStatus.FULLFILLED.value:
            return OrderStatus.FULLFILLED
        elif value == OrderStatus.PLACING.value:
            return OrderStatus.PLACING
        elif value == OrderStatus.CANCELING.value:
            return OrderStatus.CANCELING
            
        else:
            return OrderStatus.UNKNOWN

