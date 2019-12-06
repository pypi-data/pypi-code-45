#!/usr/bin/env python3

import asyncio
import websockets
import json
import zlib
import time
import requests
import dateutil.parser as dp
import base64
import hmac
import hashlib
import threading
import re

import logging
                
import traceback

from ...common.timer import Timer

from ...base_individual_ws import BaseIndividualWs

from ...events import IndividualOrderEvent,IndividualBalanceEvent,EventType

from ...thread_pool import executor

from .const import INDIVIDUAL_WS_URL
from .helper import rslv_order_type, rslv_order_status


logger = logging.getLogger(__name__) 


class IndividualWs(BaseIndividualWs):


    def __init__(self,apikey, secrets,symbols , coins ,listener):
        super(IndividualWs, self).__init__('bitfinex',symbols,secrets,listener)

        self._coins = coins

        self.apikey = apikey
        self.keysecret = secrets.get('keysecret')



    def convert_balance_snapshot(self,line):    

        print('balance, line:',line)

        balances = {}

        for item in line[2]:
            if 'exchange' == item[0]:
                    
                currency = item[1].lower()
                balance = float(item[2])
                available = float(item[4] or 0)

                balances[currency] = {
                    "balance":balance,
                    "available":available,
                    "freeze":balance - available
                }

        return balances


    def convert_balance_update(self,line):    

        print('balance, line:',line)
        

        balances = {}

        item = line[2] 

        if 'exchange' == item[0]:

            currency = item[1].lower()
            balance = float(item[2])
            available = float(item[4] or 0)

            balances[currency] = {
                "balance":balance,
                "available":available,
                "freeze":balance - available
            }

        return balances 

    def convert_order_snapshot(self,line):    

        print('order, line:',line)

        orders = {}

        for symbol in self._symbols: 
            coin = symbol[0]
            currency = symbol[1]

            symbol_orders={}

            for item in line[2]:
                if f"t{symbol[0].upper()}{symbol[1].upper()}" == item[3]:
                    
                    type_ = None
                    side = None

                    type_ = rslv_order_type(item[8]).value
                    status = rslv_order_status(item[13]).value

                    if item[6] > 0:
                        side = 'buy'
                    elif item[6] < 0:
                        side = 'sell'

                    if coin and currency and type_ and side:
                        order_id = str(item[0])

                        order = {
                            'order_id':order_id,
                            'coid':str(item[2]),
                            'coin': coin,
                            'currency': currency,
                            'type': type_,
                            'side': side,
                            'price': item[16],
                            'size': abs(item[6]),
                            'status':status,
                            'timestamp':item[4]
                        }


                    symbol_orders[order_id] = order

                orders[(coin,currency)] = symbol_orders

        return orders

    def convert_order_update(self,line):    

        orders = {}

        item = line[2]
        coin = None
        currency = None
        type_ = None
        side = None
        for symbol in self._symbols: 
            if f"t{symbol[0].upper()}{symbol[1].upper()}" == item[3]:
                coin = symbol[0]
                currency = symbol[1]

        type_ = rslv_order_type(item[8]).value
        status = rslv_order_status(item[13]).value

        if item[7] > 0:
            side = 'buy'
        elif item[7] < 0:
            side = 'sell'
        else:
            logger.warning('unknown side: %s',item[7])

        if coin and currency and type_ and side:
            order_id = str(item[0])

            order = {
                'order_id':order_id,
                'coid':str(item[2]),
                'coin': coin,
                'currency': currency,
                'type': type_,
                'side': side,
                'price': item[16],
                'size': abs(item[7]),
                'status':status,
                'timestamp':item[4]
            }


            orders[(coin,currency)] = {order_id:order}

        return orders
 
    async def connect(self):

        logger.info(f"bitfinex,will connect to:{INDIVIDUAL_WS_URL}")
        
        async with websockets.connect(INDIVIDUAL_WS_URL) as websocket:


            self._listener.on_start()

            try:

                authNonce   = str(int(round(time.time() * 1000)))
                authPayload = 'AUTH' + authNonce
                authSig     = hmac.new(bytes(self.keysecret,'latin-1'),bytes( authPayload,'latin-1'), hashlib.sha384).hexdigest()
              
                send_text = json.dumps({
                    'event':'auth',
                    'apiKey':self.apikey,
                    'authSig':authSig,
                    'authPayload':authPayload,
                    'authNonce':authNonce,
                    'calc':1
                    })

                await websocket.send(send_text)

                self._listener.on_sent(send_text)


                while True:


                    res = await websocket.recv()
                    self._listener.on_recv(res)


                    line = json.loads(res)


                    if isinstance(line,dict) and line.get('event') == 'pong':
                        logger.info('bitfinex,recv pong ..')

                        continue

                    elif isinstance(line,dict) and line.get('event') == 'auth':

                        if line.get('status') == 'OK':
                            print('auth success.')

                        else:
                            print('auth failed.')
  

                    elif isinstance(line,list):

                        print('line is list:' , line)

                        if line[0] == 0:
                            
                            if 'ws' == line[1]:

                                balances = self.convert_balance_snapshot(line)

                                event = IndividualBalanceEvent('balance',balances, self._exchange, self.apikey , EventType.snapshot )
                                self._listener.on_individual_event(event)

                            elif 'wu' == line[1]:
                                balances = self.convert_balance_update(line)

                                event = IndividualBalanceEvent('balance',balances, self._exchange, self.apikey , EventType.update )
                                self._listener.on_individual_event(event)


                            elif line[1] == 'os':

                                orders = self.convert_order_snapshot(line)

                                for k,v in orders.items():

                                    event = IndividualOrderEvent('order',v,self._exchange,self.apikey,k[0],k[1],EventType.snapshot)

                                    self._listener.on_individual_event(event)
 

                            elif line[1] in ['on','ou','oc'] :
                                
                                orders = self.convert_order_update(line)

                                logger.info('orders: %s', orders)

                                for k,v in orders.items():
                                    event = IndividualOrderEvent('order',v,self._exchange,self.apikey,k[0],k[1],EventType.update)

                                    self._listener.on_individual_event(event)

                            else:

                                logger.warning('unknown message: %s', line[1])


            except websockets.ConnectionClosed as e:

                logger.warning(str(e))

                raise
            except Exception as e:

                logger.error(str(e))

                raise
            finally:

                self._listener.on_end()


