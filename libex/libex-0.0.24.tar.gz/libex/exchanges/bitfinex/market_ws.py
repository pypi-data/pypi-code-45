#!/usr/bin/env python3

'''
api doc
https://docs.bitfinex.com/v2/docs/ws-general
https://docs.bitfinex.com/v2/reference#ws-public-trades
'''

import asyncio
import websockets 
import json
import time

import logging

from ...base_market_ws import BaseMarketWs
from ...events import MarketEvent,EventType
from ...const import Channel
from ...common.book import update_book
from ...common.rate import Rate
from .const import MARKET_WS_URL, SYMBOLS

  
# def update_book(depths,size,asks,bids,timestamp):

#     logger.debug(f"update book, asks:{asks} , bids:{bids} , timestamp:{timestamp}\n")

#     curr_asks = depths.setdefault('asks',[])
#     curr_bids = depths.setdefault('bids',[])

#     for item in asks:

#         arr = [n for n in curr_asks if n[0] != item[0]]

#         if item[1] != '0':
#             arr.append(item)

#         curr_asks = arr

        
#     for item in bids: 

#         arr = [n for n in curr_bids if n[0] != item[0]]

#         if item[1] != '0':
#             arr.append(item)

#         curr_bids = arr

#     sorted_asks = sorted(curr_asks, key=lambda a: a[0])[0:size]  # 按每个元素的第一个数据排序
#     depths['asks'] = sorted_asks

#     sorted_bids = sorted(curr_bids, key=lambda a: a[0],reverse=True)[0:size]  # 按每个元素的第一个数据排序
#     depths['bids'] = sorted_bids
  
#     depths['ts'] = timestamp



logger = logging.getLogger(__name__)


class MarketWs(BaseMarketWs):
    """docstring for OkexAdapter"""

    def __init__(self,exchange,symbols,channels,listener,currencies=None,stablecoin=None ):
        super(MarketWs, self).__init__(exchange,symbols,channels,listener)

        self._channelIds = {}
        self._book25 = {}
        self._rate = Rate(exchange,currencies,stablecoin,listener)

    def convert_ticker(self,origin):

        logger.debug('ticker origin: %s' ,origin)

        last = origin[6]
        bid = origin[0]
        ask = origin[2]
        ts  = 0

        return {
            "last":last,
            "bid":bid,
            "ask":ask,
            "ts":ts
        }

    def convert_trade(self,origin):
        price = origin[3]
        size  = abs(origin[2])
        side  = 'sell' if origin[2] > 0 else 'buy'  
        ts    = origin[1]/1000


        # ts = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')
        # ts = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S.%f')
        # ts = datetime.fromtimestamp(ts).astimezone(pytz.timezone("Asia/Shanghai")).isoformat()

        return {
            'price':price,
            'size':size,
            'side':side,
            'ts':ts 
        }


    def convert_book_update(self,msg):

        # print(msg)

        ts = msg[2]/1000
        # ts = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')
        # ts = datetime.fromtimestamp(ts).astimezone(pytz.timezone("Asia/Shanghai")).isoformat()

        # d = 'bid' if float(msg[1][0]) > 0 else 'ask'

        book = msg[1]
        if book[1] >0:
            if book[2] > 0:
                
                return {
                    "bids":[[book[0] , book[2]]],
                    "ts":ts
                }
            else :
                return {
                    "asks":[[book[0] , -book[2]]],
                    "ts":ts
                }
        else:
            if book[2] > 0:
                return{
                    "bids":[[book[0] , 0]],
                    "ts":ts
                    
                }
            else:
                return {
                    "asks":[[book[0] , 0]],
                    "ts":ts
                }   


    def convert_book_snapshot(self,msg):

        asks = []
        bids = []

        data = msg[1]
        for line in data:
            if line[1] > 0:
                if line[2] >0:
                    bids.append([line[0],line[2]])
                else:
                    asks.append([line[0],-line[2]])

        return {
            "asks":asks,
            "bids":bids
            }

    def convert_candle(self, origin):

        logger.debug('origin: %s',origin)

        (ts,o,c,h,l,v) = origin
        ts = ts/1000

        return [ts,o,h,l,c,v]

    def handle_subscribed(self,line):
        
        item_symbol = line.get('symbol')
        item_channel = line.get('channel')
        item_length = line.get('len')
        item_chan_id = line.get('chanId')
        item_key = line.get('key')

        if item_symbol:
            (coin,currency) = SYMBOLS.get(item_symbol)

        channel = None

        if 'book' == item_channel:
            if item_length:
                channel = (Channel.book5,Channel.book10,Channel.book20)
        elif 'candles' == item_channel:
            if item_key:
                (a,b,c) = item_key.split(':')
                print(a,b,c)
                channel = Channel.rslv(f"candle{b}") 
                (coin,currency) = SYMBOLS.get(c)

        elif 'ticker' == item_channel:
            channel = Channel.ticker
        elif 'trades' == item_channel:
            channel = Channel.trade

        self._channelIds[str(item_chan_id)] = {
            'channel': channel ,
            'coin': coin,
            'currency':currency
        }

        logger.info('channels: %s', self._channelIds);

    def handle_ticker(self,line,coin,currency):
        
        type_ = 'snapshot'

        self._listener.on_resolve(coin,currency,'ticker' + '/' + type_ ,None,None,line)

        converted = self.convert_ticker(line[1])

        self._listener.on_market_event(MarketEvent('ticker',converted,'bitfinex',coin,currency))
        self._rate.on_ticker(coin,currency,None, converted)

    def handle_book25(self,line,coin,currency,channels):

        if isinstance(line[1],list):
                
            type_ = 'update'
            if isinstance(line[1][0],list):
                type_ = 'snapshot'


            ts = line[2]/1000

            self._listener.on_resolve(coin,currency,'book25' + '/' + type_ ,None,ts,line)


            typ_enum = None
            if 'snapshot' == type_:
                converted = self.convert_book_snapshot(line)
                typ_enum = EventType.snapshot

                self._book25.setdefault(f"{coin}_{currency}",{'asks':converted.get('asks'),
                    'bids':converted.get('bids')})

            else:
                converted = self.convert_book_update(line)
                typ_enum = EventType.update

                update_book(self._book25.get(f"{coin}_{currency}"),25,converted.get('asks') or [],converted.get('bids') or [],converted.get('ts'))


            if Channel.book5 in self._channels:
                j = {
                    'asks':self._book25.get(f"{coin}_{currency}").get('asks')[0:5],
                    'bids':self._book25.get(f"{coin}_{currency}").get('bids')[0:5],
                    'ts':self._book25.get(f"{coin}_{currency}").get('ts')

                }
                self._listener.on_market_event(MarketEvent('book5',j,'bitfinex',coin,currency))
            if Channel.book10 in self._channels:
                j = {
                    'asks':self._book25.get(f"{coin}_{currency}").get('asks')[0:10],
                    'bids':self._book25.get(f"{coin}_{currency}").get('bids')[0:10],
                    'ts':self._book25.get(f"{coin}_{currency}").get('ts')

                }
                self._listener.on_market_event(MarketEvent('book10',j,'bitfinex',coin,currency))
            if Channel.book20 in self._channels:
                j = {
                    'asks':self._book25.get(f"{coin}_{currency}").get('asks')[0:20],
                    'bids':self._book25.get(f"{coin}_{currency}").get('bids')[0:20],
                    'ts':self._book25.get(f"{coin}_{currency}").get('ts')

                }
                self._listener.on_market_event(MarketEvent('book20',j,'bitfinex',coin,currency))

    def handle_trade(self,line,coin,currency):

        item2 = line[1]

        if isinstance(item2,str):
            
            if 'tu'==item2:

                item = line[2]

                tid = item[0]
                ts = item[1]/1000


                self._listener.on_resolve(coin,currency,'trade',tid,ts,item)


                converted = self.convert_trade(item)
                self._listener.on_market_event(MarketEvent('trade',converted,'bitfinex',coin,currency,EventType.update))


        elif isinstance(item2,list):
            channelMsg = item2

            
            for item in channelMsg:

                tid = item[0]
                ts = item[1]/1000

                self._listener.on_resolve(coin,currency,'trade',tid,ts,item)

                converted = self.convert_trade(item)
                self._listener.on_market_event(MarketEvent('trade',converted,'bitfinex',coin,currency,EventType.update))

    def handle_candle(self,line,coin,currency,channel):
        
        if len(line[1])==0 or isinstance(line[1][0],list):
            candles = []
            for item in line[1]:
                candle = self.convert_candle(item)
                candles.append(candle)

            self._listener.on_market_event(MarketEvent(channel.value,candles,'bitfinex',coin,currency,EventType.snapshot))
        else:
            item = line[1]
            if isinstance(item , list):
                candle = self.convert_candle(item)

                self._listener.on_market_event(MarketEvent(channel.value,candle,'bitfinex',coin,currency,EventType.update))

    async def connect(self ):
 
        logger.info(f"bitfinex,will connect to:{MARKET_WS_URL}")
        
        async with websockets.connect(MARKET_WS_URL) as websocket:
            
            self._listener.on_start()

            try:

                # info message from server
                res = await websocket.recv()
                
                logger.info(f"bitfinex,recv flag:{res}")
                
                self._listener.on_recv(res)


                # TIMESTAMP
                # 32768
                # Timestamp in milliseconds.

                # SEQ_ALL
                # 65536
                # Enable sequencing BETA FEATURE

                # CHECKSUM
                # 131072
                # Enable checksum for every book iteration. Checks the top 25 entries for each side of book. Checksum is a signed int.

                conf = { 
                    "event": "conf", 
                    "flags": 32768
                }

                await websocket.send(json.dumps(conf))
                self._listener.on_sent(json.dumps(conf))
                
                for symbol in self._symbols:

                    s = list(SYMBOLS.keys())[list(SYMBOLS.values()).index(symbol)]


                    if Channel.ticker in self._channels:
                        
                        req = { "event": "subscribe", "channel": "ticker", "symbol": s}
                        await websocket.send(json.dumps(req))
                        self._listener.on_sent(json.dumps(req))

                    if Channel.trade in self._channels:

                        req = { "event": "subscribe", "channel": "trades", "symbol": s}
                        await websocket.send(json.dumps(req))
                        self._listener.on_sent(json.dumps(req))

                    if len([i for i in [Channel.book5,Channel.book10,Channel.book20] if i in self._channels]) > 0:

                        req = { "event": "subscribe", "channel": "book", "symbol": s,"len":25}
                        await websocket.send(json.dumps(req))
                        self._listener.on_sent(json.dumps(req))

                    if  Channel.candle5m in self._channels:

                        req = { "event": "subscribe", "channel": "candles", "key": f"trade:5m:{s}"}
                        await websocket.send(json.dumps(req))
                        self._listener.on_sent(json.dumps(req))
                    if  Channel.candle1h in self._channels:

                        req = { "event": "subscribe", "channel": "candles", "key": f"trade:1h:{s}"}
                        await websocket.send(json.dumps(req))
                        self._listener.on_sent(json.dumps(req))
                
                logger.info('bitfinex,start recv loop.')
                
                while True:

                    res = await websocket.recv()
                    self._listener.on_recv(res)

                    # timer.refresh()

                    line = json.loads(res)

                    if isinstance(line,dict) and line.get('event') == 'pong':
                        logger.info('bitfinex,recv pong ..')

                        continue

                    if isinstance(line,dict) and line.get('event') == 'subscribed':

                        logger.info(f"bitfinex,subscribed:{line}" )
                        
                        self.handle_subscribed(line)
                        
                        logger.info(f"bitfinex,channel ids:{self._channelIds}")
                        
                    elif isinstance(line,list):

                        channelId = line[0]

                        channelObj = self._channelIds.get(str(channelId))
                        coin = channelObj.get('coin')
                        currency = channelObj.get('currency')
                        channel = channelObj.get('channel')

                        if Channel.ticker == channel:
                            if 'hb' != line[1]:
                                self.handle_ticker(line,coin,currency)

                        elif channel == (Channel.book5,Channel.book10,Channel.book20):
                            
                            self.handle_book25(line,coin,currency,channel)

                        elif Channel.trade == channel:

                            self.handle_trade(line,coin,currency)
                            
                        elif channel in [Channel.candle5m,Channel.candle1h]:
                            self.handle_candle(line,coin,currency,channel)


            except websockets.ConnectionClosed as e:

                self._listener.on_end()
                logger.warning(str(e))

                raise
            except Exception as e:

                logger.info(f'time:{time.time()}')
                logger.error(str(e))

                raise

    # unsubscribe channels
    async def unsubscribe_without_login(self,url, channels):
        pass
        # async with websockets.connect(url) as websocket:
        #     sub_param = {"op": "unsubscribe", "args": channels}
        #     sub_str = json.dumps(sub_param)
        #     await  websocket.send(sub_str)
        #     # logger.debug(f"send: {sub_str}")
        #
        #     res = await websocket.recv()
        #     res = inflate(res)
        #     # logger.debug(f"{res}")

if __name__ == '__main__':
 
    pass





