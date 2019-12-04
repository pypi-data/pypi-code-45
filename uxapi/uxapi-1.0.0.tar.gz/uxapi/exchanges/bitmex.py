import time
import asyncio
import json
import operator
import collections

import pendulum
import ccxt

from uxapi import register
from uxapi import UXSymbol
from uxapi import Message
from uxapi import UXPatch
from uxapi import WSHandler
from uxapi.helpers import (
    hmac,
    contract_delivery_time
)


@register
class Bitmex(UXPatch, ccxt.bitmex):
    id = 'bitmex'

    def describe(self):
        return self.deep_extend(super().describe(), {
            'deliveryHourUTC': 12,

            'options': {
                'ws-api-expires': 60*60*24*1000,  # 1000 days
            },

            'urls': {
                'wsapi': 'wss://www.bitmex.com/realtime',
                'wsapiTest': 'wss://testnet.bitmex.com/realtime',
            },

            'wsapi': [
                'orderbook',
                'trade',
                'quote',
                'announcement',
                'chat',
                'connected',
                'funding',
                'instrument',
                'insurance',
                'liquidation',
                'publicNotifications',
                'settlement',
                'affiliate',
                'execution',
                'myorder',
                'margin',
                'position',
                'privateNotifications',
                'transact',
                'wallet',
            ],
        })

    @classmethod
    def testnet(cls, market_type, config):
        bitmex = cls(market_type, config)
        bitmex.urls['api'] = bitmex.urls['test']
        bitmex.urls['wsapi'] = bitmex.urls['wsapiTest']
        return bitmex

    def _fetch_markets(self, params):
        markets = super()._fetch_markets(params)
        for market in markets:
            contract_value = self.safe_float(market['info'], 'lotSize')
            if contract_value:
                market['contractValue'] = contract_value
            if market['type'] == 'future':
                market['type'] == 'futures'
                market['deliveryTime'] = market['info']['settle']
        return markets

    def parse_order_book(self, orderbook):
        # [
        #     {
        #         "symbol": "XBTUSD",
        #         "id": 15599187800,
        #         "side": "Sell",
        #         "size": 542,
        #         "price": 8122
        #     },
        #     ...
        # ]
        asks = []
        bids = []
        for item in orderbook:
            price = float(item['price'])
            amount = float(item['size'])
            if item['side'] == 'Sell':
                asks.append([price, amount])
            else:
                bids.append([price, amount])
        asks = sorted(asks, key=operator.itemgetter(0))
        bids = sorted(bids, key=operator.itemgetter(0), reverse=True)
        return {
            'asks': asks,
            'bids': bids,
            'timestamp': None,
            'datetime': None,
            'nonce': None
        }

    def order_book_merger(self):
        return BitmexOrderBookMerger()

    def wshandler(self, feed):
        return BitmexWSHandler(self, self.urls['wsapi'], feed)

    def convert_symbol(self, uxsymbol):
        if uxsymbol.market_type == 'swap':
            return uxsymbol.name
        if uxsymbol.market_type == 'futures':
            delivery_time = contract_delivery_time(
                expiration=uxsymbol.contract_expiration,
                delivery_hour=self.deliveryHourUTC)
            code = self._contract_code(delivery_time)
            if uxsymbol.quote == 'USD':
                if uxsymbol.base == 'BTC':
                    return f'XBT{code}'
            elif uxsymbol.quote in ['ADA', 'BCH', 'EOS', 'ETH', 'LTC', 'TRX', 'XRP']:
                return f'{uxsymbol.quote}{code}'
        raise ValueError('invalid symbol')

    @staticmethod
    def _contract_code(delivery_time):
        month_codes = "FGHJKMNQUVXZ"
        year = delivery_time.year - 2000
        quarter = (delivery_time.month + 2) // 3
        delivery_month = month_codes[quarter * 3 - 1]
        return f'{delivery_month}{year}'

    def convert_topic(self, uxtopic):
        maintype = uxtopic.maintype
        assert maintype in self.wsapi
        subtype = uxtopic.subtype
        topic = None
        if maintype == 'orderbook':
            if subtype == 'full':
                level = 'L2'
            elif subtype == '25':
                level = 'L2_25'
            else:
                level = '10'
            topic = f'orderBook{level}'
        elif maintype == 'quote':
            if subtype:
                topic = f'quoteBin{subtype}'
            else:
                topic = 'quote'
        elif maintype == 'trade':
            if subtype:
                topic = f'tradeBin{subtype}'
            else:
                topic = 'trade'
        elif maintype == 'myorder':
            topic = 'order'
        else:
            topic = maintype

        if uxtopic.extrainfo:
            uxsymbol = UXSymbol(uxtopic.exchange_id, uxtopic.market_type,
                                uxtopic.extrainfo)
            symbol = self.market_id(uxsymbol)
            topic = f'{topic}:{symbol}'

        return topic


class BitmexWSHandler(WSHandler):
    default_api_expires = 60 * 60 * 24 * 1000  # 1000 days

    def on_connected(self):
        self.pre_handlers.append(self.handle_info_message)
        self.pre_handlers.append(self.handle_error_message)

    def handle_info_message(self, ctx, message):
        _, msg = message
        if 'info' in msg:
            self.logger.info(msg)
            return None
        else:
            return message

    def handle_error_message(self, ctx, message):
        _, msg = message
        if 'error' in msg:
            raise RuntimeError(msg)
        else:
            return message

    def create_keepalive_task(self):
        self.last_message_timestamp = time.time()
        return super().create_keepalive_task()

    async def keepalive(self):
        interval = 5
        while True:
            await asyncio.sleep(interval)
            now = time.time()
            if now - self.last_message_timestamp >= interval:
                await self.send('ping')

    def handle_keepalive_message(self, ctx, message):
        self.last_message_timestamp = time.time()
        _, msg = message
        if msg == 'pong':
            return None
        else:
            return message

    @property
    def login_required(self):
        private_types = [
            'myorder', 'margin', 'position', 'affiliate', 'execution',
            'privateNotifications', 'transact', 'wallet',
        ]
        topic_types = [topic.maintype for topic in self.feed.topics]
        for typ in private_types:
            if typ in topic_types:
                return True
        return False

    def login_command(self, credentials):
        if self.exchange:
            expires = self.exchange.options['ws-api-expires']
        else:
            expires = self.default_api_expires
        expires += int(time.time())

        payload = 'GET' + '/realtime' + str(expires)
        signature = hmac(
            bytes(credentials['secret'], 'utf8'),
            bytes(payload, 'utf8'),
            digest='hex'
        )
        return {
            'op': 'authKeyExpires',
            'args': [
                credentials['apiKey'],
                expires,
                signature,
            ]
        }

    def handle_login_message(self, ctx, message):
        _, msg = message
        if ('request' in msg) and (msg['request'].get('op') == 'authKeyExpires'):
            if msg['success']:
                self.logger.info(f'feed {self.feed.id}: logged in')
                self.on_login()
                return None
            raise RuntimeError('login failed')
        else:
            return message

    def subscribe_commands(self, topics):
        command = {
            'op': 'subscribe',
            'args': topics,
        }
        return [command]

    def handle_subscribe_message(self, ctx, message):
        _, msg = message
        if 'subscribe' in msg:
            topic = msg['subscribe']
            self.logger.info(f'feed {self.feed.id}: {topic} subscribed')
            self.on_subscribe(topic)
            return None
        else:
            return message

    def decode(self, data):
        try:
            jsonmsg = json.loads(data)
            return jsonmsg
        except json.JSONDecodeError:
            return data


class BitmexOrderBookMerger:
    def __init__(self):
        self.snapshot = None

    def __call__(self, ctx, message):
        key, msg = message
        self.merge(msg['action'], msg['data'])
        return Message(key, self.snapshot)

    def merge(self, action, patch):
        if action == 'partial':
            self.snapshot = {item['id']: item for item in patch}
        elif action == 'update':
            for item in patch:
                self.snapshot[item['id']]['size'] = item['size']
        elif action == 'delete':
            for item in patch:
                del self.snapshot[item['id']]
        elif action == 'insert':
            self.snapshot.update({item['id']: item for item in patch})
        else:
            raise ValueError('invalid action')
        return self.snapshot.values()