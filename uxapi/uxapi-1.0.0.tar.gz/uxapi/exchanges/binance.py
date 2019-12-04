import json
import bisect
from yarl import URL
from uxapi import register
from uxapi import UXSymbol
from uxapi import Message
from uxapi import UXPatch
from uxapi import Session
from uxapi import WSHandler
from uxapi.exchanges.ccxt import binance
from uxapi.helpers import (
    deep_extend,
    all_equal,
    async_call,
    is_sorted,
)


@register
class Binance(UXPatch, binance):
    id = 'binance'

    def __init__(self, market_type, config=None):
        if market_type == 'spot':
            config = deep_extend({
                'urls': {
                    'api': {
                        'public': 'https://api.binance.com/api/v3',
                        'private': 'https://api.binance.com/api/v3',
                    }
                }
            }, config or {})
        elif market_type == 'swap':
            config = deep_extend({
                'urls': {
                    'api': {
                        'public': 'https://fapi.binance.com/fapi/v1',
                        'private': 'https://fapi.binance.com/fapi/v1',
                    }
                },
                'options': {'defaultMarket': 'futures'},
            }, config or {})
        else:
            raise ValueError('invalid market_type')
        return super().__init__(market_type, config)

    def describe(self):
        return self.deep_extend(super().describe(), {
            'urls': {
                'wsapi': {
                    'market': 'wss://stream.binance.com:9443/stream',
                    'private': 'wss://stream.binance.com:9443/ws',
                    'fmarket': 'wss://fstream.binance.com/stream',
                    'fprivate': 'wss://fstream.binance.com/ws',
                }
            },

            'wsapi': {
                'market': {
                    'orderbook': '{symbol}@depth{level}',
                    'kline': '{symbol}@kline_{period}',
                    'trade': '{symbol}@trade',
                    'aggTrade': '{symbol}@aggTrade',
                    'ticker': '{symbol}@ticker',
                    '!ticker': '!ticker@arr',
                    'miniTicker': '{symbol}@miniTicker',
                    '!miniTicker': '!miniTicker@arr',
                    'quote': '{symbol}@bookTicker',
                    '!quote': '!bookTicker', 
                },
                'private': {'private': 'private'},
                'fmarket': {
                    'orderbook': '{symbol}@depth{level}',
                    'kline': '{symbol}@kline_{period}',
                    'aggTrade': '{symbol}@aggTrade',
                    'markPrice': '{symbol}@markPrice',
                    'miniTicker': '{symbol}@miniTicker',
                    'ticker': '{symbol}@ticker',
                    'quote': '{symbol}@bookTicker',
                    '!quote': '!bookTicker',
                },
                'fprivate': {'private': 'private'},
            }
        })

    def _fetch_markets(self, params=None):
        markets = super()._fetch_markets(params)
        for market in markets:
            market['type'] = self.market_type
            if self.market_type == 'swap':
                market['contractValue'] = 1
        return markets

    def order_book_merger(self):
        return BinanceOrderBookMerger(self)

    def wshandler(self, feed):
        wsapi_types = set(self.wsapi_type(topic) for topic in feed.topics)
        if len(wsapi_types) > 1:
            raise ValueError('feed contains incompatible topics')
        wsapi_type = wsapi_types.pop()
        wsurl = self.urls['wsapi'][wsapi_type]
        return BinanceWSHandler(self, wsurl, feed, wsapi_type)
    
    def wsapi_type(self, uxtopic):
        if uxtopic.market_type == 'spot':
            if uxtopic.maintype == 'private':
                return 'private'
            else:
                return 'market'
        elif uxtopic.market_type == 'swap':
            if uxtopic.maintype == 'private':
                return 'fprivate'
            else:
                return 'fmarket'
        else:
            raise ValueError('invalid topic')

    def convert_symbol(self, uxsymbol):
        if uxsymbol.market_type == 'spot':
            return str(uxsymbol)
        elif uxsymbol.market_type == 'swap':
            return f'{uxsymbol.quote}/{uxsymbol.base}'
        else:
            raise ValueError('invalid symbol')

    def convert_topic(self, uxtopic):
        maintype = uxtopic.maintype
        subtype = uxtopic.subtype
        wsapi_type = self.wsapi_type(uxtopic)
        template = self.wsapi[wsapi_type][maintype]

        symbol = None
        if uxtopic.extrainfo:
            uxsymbol = UXSymbol(uxtopic.exchange_id, uxtopic.market_type,
                                uxtopic.extrainfo)
            symbol = self.market_id(uxsymbol).lower()

        if maintype == 'orderbook':
            if subtype is None:
                level = '20@100ms'
            elif subtype == 'full':
                level = ''
            else:
                level = subtype
            return template.format(symbol=symbol, level=level)
        elif maintype == 'kline':
            period = self.timeframes[subtype]
            return template.format(symbol=symbol, period=period)
        else:
            return template.format(symbol=symbol)


class BinanceWSHandler(WSHandler):
    def __init__(self, exchange, wsurl, feed, wsapi_type):
        super().__init__(exchange, wsurl, feed)
        self.wsapi_type = wsapi_type

    async def connect(self):
        if not self.session:
            self.session = Session()
            self.own_session = True

        if self.login_required:
            listen_key = await self.fetch_listen_key()
            wsurl = URL(f'{self.wsurl}/{listen_key}')
        else:
            topics = [self.convert_topic(topic) for topic in self.feed.topics]
            query = {'streams': '/'.join(topics)}
            wsurl = URL(self.wsurl).with_query(query)
        ws = await self.session.ws_connect(str(wsurl))
        return ws

    async def fetch_listen_key(self):
        if self.wsapi_type == 'private':
            url = 'https://api.binance.com/api/v3/userDataStream'
        elif self.wsapi_type == 'fprivate':
            url = 'https://fapi.binance.com/fapi/v1/listenKey'
        else:
            raise RuntimeError('invalid wsapi_type')
        credentials = self.get_credentials()
        headers = {'X-MBX-APIKEY': credentials['apiKey']}
        async with self.session.post(url, headers=headers) as resp:
            result = await resp.json()
        if 'listenKey' not in result:
            raise RuntimeError(result)
        return result['listenKey']

    @property
    def login_required(self):
        return self.wsapi_type in ['private', 'fprivate']

    def create_keepalive_task(self):
        pass

    def create_login_task(self):
        pass

    def create_subscribe_task(self):
        pass 

    def decode(self, data):
        return json.loads(data)


class BinanceOrderBookMerger:
    def __init__(self, exchange):
        self.exchange = exchange
        self.cache = []
        self.task = None
        self.snapshot = None
        self.prices = None

    def __call__(self, ctx, message):
        key, msg = message
        patch = msg['data']
        if self.snapshot:
            self.merge(patch)
            return Message(key, self.snapshot)

        self.cache.append(patch)
        if not self.task:
            self.task = async_call(self.fetch_order_book, patch['s'])
        if not self.task.done():
            return None

        snapshot = self.task.result()
        self.task = None
        self.on_snapshot(snapshot)
        return Message(key, self.snapshot)

    def on_snapshot(self, snapshot):
        self.snapshot = snapshot
        self.prices = {
            'asks': [float(item[0]) for item in snapshot['asks']],
            'bids': [-float(item[0]) for item in snapshot['bids']]
        }
        array = [patch['u'] for patch in self.cache]
        i = bisect.bisect_right(array, snapshot['lastUpdateId'])
        self.snapshot['lastUpdateId'] = None
        for patch in self.cache[i:]:
            self.merge(patch)
        self.cache = None

    def merge(self, patch):
        lastUpdateId = self.snapshot['lastUpdateId']
        if lastUpdateId:
            if 'pu' in patch:   # binance futures
                if patch['pu'] != lastUpdateId:
                    raise ValueError('invalid patch')
            else:   # binance spot
                if patch['U'] != lastUpdateId + 1:
                    raise ValueError('invalid patch')
        self.snapshot['lastUpdateId'] = patch['u']
        self.merge_asks_bids('asks', patch['a'])
        self.merge_asks_bids('bids', patch['b'])

    def merge_asks_bids(self, key, patch):
        for item in patch:
            if key == 'asks':
                price = float(item[0])
            else:
                price = -float(item[0])
            amount = float(item[1])
            array = self.prices[key]
            i = bisect.bisect_left(array, price)
            if i < len(array) and array[i] == price:
                if amount == 0:
                    array.pop(i)
                    self.snapshot[key].pop(i)
                else:
                    self.snapshot[key][i] = item
            else:
                if amount != 0:
                    array.insert(i, price)
                    self.snapshot[key].insert(i, item)

    def fetch_order_book(self, symbol):
        return self.exchange.publicGetDepth(params={
            'symbol': symbol,
            'limit': 1000,
        })