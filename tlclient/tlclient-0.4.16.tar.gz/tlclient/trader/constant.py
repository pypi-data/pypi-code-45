# auto generated by update_py.py

from tlclient.linker.constant import ReadableEnum

MODULE_TICKER_LENGTH = 20
MODULE_SOURCE_LENGTH = 20
MODULE_ACCOUNT_LENGTH = 20
MODULE_GATEWAY_LENGTH = 10
MODULE_ORDERREF_LENGTH = 50
MODULE_ERR_MSG_LENGTH = 81
MODULE_TRADEID_LENGTH = 50
MODULE_TRADINGDAY_LENGTH = 9

ORDER_BOOK_SIZE = 10

USER_RSA_KEY_DIR = '/shared/key/'


class MsgType(ReadableEnum):
    # trading msg types
    REQ_ORDER_INSERT = 200
    REQ_ORDER_INSERT_NEED_RM = 201
    REQ_ORDER_INSERT_PASS_RM = 202
    REQ_ORDER_INSERT_FAIL_RM = 203
    REQ_ORDER_INSERT_BASKET = 204
    REQ_ORDER_INSERT_J = 205

    REQ_ORDER_CANCEL = 210
    REQ_ORDER_STATUS = 220
    REQ_POSITION = 230
    REQ_ACCOUNT = 240
    REQ_ORDER_INFO = 250
    REQ_ACTIVE_ORDERS = 260
    REQ_HISTORY_TRADES = 270
    REQ_CANCEL_ACTIVE_ORDERS = 261
    RSP_ORDER_INSERT = 300
    RSP_ORDER_INSERT_BASKET = 303
    RSP_ORDER_CANCEL = 310
    RSP_ORDER_STATUS = 320
    RSP_POSITION = 330
    RSP_ACCOUNT = 340
    RSP_ORDER_INFO = 350
    RSP_ACTIVE_ORDERS = 360
    RSP_CANCEL_ACTIVE_ORDERS = 361
    RSP_HISTORY_TRADES = 370
    RTN_ORDER = 400
    RTN_TRADE = 410

    # market msg types
    MKT_DATA_TYPE = 500
    MKT_SUBSCRIBE = 500
    MKT_SNAP = 510
    MKT_SNAP_PLUS = 511
    MKT_SNAP_FUT = 512
    MKT_SNAP_OPT = 513
    MKT_SNAP_AGG = 519
    MKT_BAR = 520
    MKT_BAR_GEN = 521
    MKT_VOL = 522
    MKT_INDEX = 530
    MKT_ORDER = 540
    MKT_TRADE = 550
    MKT_DATA_END = 599

    # risk manager related
    RMS_STATUS = 800
    RMS_UPDATE_RULE = 801
    RMS_DELETE_RULE = 802
    RMS_APPLY_RULE = 803
    RMS_UNAPPLY_RULE = 804
    RMS_ACTIVATE_RULE = 805
    RMS_DEACTIVATE_RULE = 806
    RMS_RISK_RULE_VIOLATED_WARNING = 810
    RMS_UPDATE_RULE_HELPER = 850

    # system status msg types
    SYSTEM_STATUS_TYPE = 900
    GTW_CONNECTION = 900
    SYSTEM_STATUS_END = 999

    @staticmethod
    def is_market_data_type(msg_type):
        return msg_type >= MsgType.MKT_DATA_TYPE and msg_type <= MsgType.MKT_DATA_END

    @staticmethod
    def is_trading_data_type(msg_type):
        return msg_type >= MsgType.REQ_ORDER_INSERT and msg_type < MsgType.MKT_DATA_TYPE

    @staticmethod
    def is_system_status_data_type(msg_type):
        return msg_type >= MsgType.SYSTEM_STATUS_TYPE and msg_type <= MsgType.SYSTEM_STATUS_END


class ExchangeID(ReadableEnum):
    NOT_AVAILABLE = 0
    SSE = 1
    SZE = 2
    HK = 3
    CFFEX = 4
    DCE = 5
    SHFE = 6
    CZCE = 7

    CRYPTO = 100
    HUOBI = 101
    OKEX = 102
    BINANCE = 103
    BITMEX = 104


class Direction(ReadableEnum):
    NOT_AVAILABLE = 0
    BUY = 1
    SELL = 2


class PosiDirection(ReadableEnum):
    NOT_AVAILABLE = 0
    NET = 1
    LONG = 2
    SHORT = 3


class OrderType(ReadableEnum):
    NOT_AVAILABLE = 0
    PLAIN_ORDER_PREFIX = 1
    BASKET_ORDER_PREFIX = 2
    ALGO_ORDER_PREFIX = 3
    # PLAIN
    PLAIN_ORDER = 10
    LIMIT = 11
    MARKET = 12
    FAK = 13
    FOK = 14
    # BASKET
    BASKET_ORDER = 20
    # ALGO
    ALGO_ORDER = 30
    TWAP = 31


class OffsetFlag(ReadableEnum):
    NOT_AVAILABLE = 0
    OPEN = 1
    CLOSE = 2
    FORCE_CLOSE = 3
    CLOSE_TODAY = 4
    CLOSE_YESTERDAY = 5


class OrderStatus(ReadableEnum):
    NOT_AVAILABLE = 0
    UNKNOWN = 1
    PROPOSED = 10
    RESPONDED = 20
    QUEUEING = 30
    NO_TRADE_QUEUEING = 31
    PART_TRADE_QUEUEING = 32
    PENDING_MAX = 39
    # // if status >= 40, it is not pending
    REJECTED = 40  # // router / gateway / exchange reject
    REJECT_BY_ROUTER = 41
    REJECT_BY_GATEWAY = 42
    REJECT_BY_EXCHANGE = 43
    CANCELED = 50  # // cancelled, no mater all traded or partly traded
    NO_TRADE_CANCELED = 51
    PART_TRADE_CANCELED = 52
    ALL_TRADED = 60
    # // some other middle status...
    TO_CANCEL = 70


class TradingStyle(ReadableEnum):
    NOT_AVAILABLE = 0
    AGGRESSIVE = 1
    NEUTRAL = 2
    CONSERVATIVE = 3


class BarType(ReadableEnum):
    NOT_AVAILABLE = 0
    MIN_1 = 1
    MIN_3 = 2
    MIN_5 = 3
    MIN_15 = 4
    MIN_30 = 5
    HOUR_1 = 10
    HOUR_2 = 11
    HOUR_4 = 12
    HOUR_6 = 13
    HOUR_12 = 14
    DAY_1 = 20
    WEEK_1 = 30
    MONTH_1 = 40
    YEAR_1 = 50

    _type_secs_cache = None

    @classmethod
    def get_seconds(cls, bar_type):
        if cls._type_secs_cache is None:
            cls._type_secs_cache = {
                cls.MIN_1: 1 * 60,
                cls.MIN_3: 3 * 60,
                cls.MIN_5: 5 * 60,
                cls.MIN_15: 15 * 60,
                cls.MIN_30: 30 * 60,
                cls.HOUR_1: 1 * 60 * 60,
                cls.HOUR_2: 2 * 60 * 60,
                cls.HOUR_4: 4 * 60 * 60,
                cls.HOUR_6: 6 * 60 * 60,
                cls.HOUR_12: 12 * 60 * 60,
                cls.DAY_1: 1 * 24 * 60 * 60,
                cls.WEEK_1: 1 * 7 * 24 * 60 * 60,
                cls.MONTH_1: 1 * 30 * 24 * 60 * 60,  # not accurate
                cls.YEAR_1: 1 * 365 * 24 * 60 * 60,  # not accurate
            }
        return cls._type_secs_cache.get(bar_type, -1)


class AssetType(ReadableEnum):
    NOT_AVAILABLE = 0
    #
    TRADITIONAL_ASSET = 10
    STOCK = 11
    FUTURES = 12
    OPTION = 13
    #
    CRYPTO_ASSET = 20
    CRYPTO_SPOT = 21
    CRYPTO_CONTRACT = 22
    CRYPTO_MARGIN = 23
    CRYPTO_FUTURES = 24
    CRYPTO_SWAP = 25


class ExecRole(ReadableEnum):
    NOT_AVAILABLE = 0
    MAKER = 1
    TAKER = 2


class MarginMode(ReadableEnum):
    NOT_AVAILABLE = 0
    CROSSED = 1
    FIXED = 2
