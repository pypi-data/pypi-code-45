from uxapi.__version__ import VERSION, __version__
from uxapi.symbol import UXSymbol
from uxapi.topic import UXTopic
from uxapi.seqiter import seqiter
from uxapi.event import Event
from uxapi.queue import Queue
from uxapi.session import Session
from uxapi.patch import UXPatch
from uxapi.handlerctx import HandlerContext
from uxapi.feed import Feed

import collections
Message = collections.namedtuple('Message', 'key msg')

from uxapi.wshandler import WSHandler
from uxapi.aggregator import Aggregator


def print_message(ctx, message):
    key, msg = message
    print(msg)
    return message


_registry = {}


def register(exchange_cls):
    _registry[exchange_cls.id] = exchange_cls


def new_exchange(exchange_id, market_type, config=None):
    return _registry[exchange_id](market_type, config)


from uxapi.exchanges.okex import Okex
from uxapi.exchanges.huobi import Huobi
from uxapi.exchanges.bitmex import Bitmex
from uxapi.exchanges.binance import Binance