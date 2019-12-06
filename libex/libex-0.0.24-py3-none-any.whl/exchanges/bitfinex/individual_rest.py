import logging 
import json
import traceback
import requests  # pip install requests
import hashlib
import hmac
import time #for nonce

from ...fail_exception import FailException 
from ...const import OrderType

from .const import INDIVIDUAL_REST_URL
from .const import SYMBOLS
from .helper import rslv_order_type,rslv_order_status

logger = logging.getLogger(__name__)


class IndividualRest(object):

    def __init__(self, apikey, secrets):

        self._apikey= apikey         # "5qddoZu4E5XYrRlFF8Q3BIlnBtZNxFjRGCBxljJVji1"
        self._keysecret= secrets.get('keysecret')    # "5LQEiMXD44JYMICqs0yYuMapbPM4s91AcWaFHmNZr0a"

        logger.info('apikey:%s, secret:%s' , self._apikey,self._keysecret);

    def _nonce(self):
        """
        Returns a nonce
        Used in authentication
        """
        return str(int(round(time.time() * 1000)))

    def _headers(self, path, nonce, body):

        signature = "/api/" + path + nonce + body
        # print ("Signing: " + signature)
        h = hmac.new(bytes(self._keysecret,'latin-1'),bytes( signature,'latin-1'), hashlib.sha384)
        signature = h.hexdigest()

        return {
            "bfx-nonce": nonce,
            "bfx-apikey": self._apikey,
            "bfx-signature": signature,
            "content-type": "application/json"
        }

    def _post(self,path,body={}):
        nonce = self._nonce()
        
        rawBody = json.dumps(body)

        logger.info('path:%s, body:%s', path,rawBody)

        headers = self._headers(path, nonce, rawBody)

        r = requests.post(INDIVIDUAL_REST_URL + path, headers=headers, data=rawBody, verify=True)

        logger.info('resp: %s', json.dumps(r.json()) )

        if r.status_code == 200:
            return r.json()
        else:
            logger.error('status code:%s' , r.text)
            return None

    def convert_submit_order(self,origin):
    
        order_info = origin[4][0]

        detail = {}

        detail['order_id'] = str(order_info[0])
        detail['coid'] = str(order_info[2])
        detail['size'] = abs(order_info[6])
        detail['side'] = 'buy' if order_info[6]>0 else 'sell'
        detail['type'] = rslv_order_type(order_info[8]).value 
        detail['price'] = order_info[16]
        detail['status'] = rslv_order_status(order_info[13].split(' ')[0]).value
        detail['coin'],detail['currency'] = SYMBOLS[order_info[3]]
        detail['timestamp'] = order_info[4]

        return detail

    def convert_retrieve_order(self,origin):
    
        order_info = origin[0]

        detail = {}

        detail['order_id'] = str(order_info[0])
        detail['coid'] = str(order_info[2])
        detail['size'] = abs(order_info[6])

        detail['side'] = 'buy' if order_info[6]>0 else 'sell'
        detail['type'] = rslv_order_type(order_info[8]).value
        detail['price'] = order_info[16]
        detail['status'] = rslv_order_status(order_info[13]).value
        detail['coin'],detail['currency'] = SYMBOLS[order_info[3]]

        detail['filled_size'] = abs(order_info[7]) - abs(order_info[6])
        detail['filled_notional'] = detail['filled_size'] * order_info[17]

        detail['timestamp'] = order_info[4]

        return detail

    def convert_multi_order(self,origin):

        details = {}

        items = origin[4]

        for item in items:

            order_info = item[4][0]

            detail = {}

            detail['order_id'] = str(order_info[0])
            detail['coid'] = str(order_info[2])
            detail['size'] = abs(order_info[6])

            detail['side'] = 'buy' if order_info[6]>0 else 'sell'
            detail['type'] = rslv_order_type(order_info[8]).value
            detail['price'] = order_info[16]
            detail['status'] = rslv_order_status(order_info[13]).value
            detail['coin'],detail['currency'] = SYMBOLS[order_info[3]]

            detail['filled_size'] = abs(order_info[6]) - abs(order_info[7])
            detail['filled_notional'] = detail['filled_size'] * order_info[17]

            detail['timestamp'] = order_info[4]

            details.setdefault(f"{detail['coin']}_{detail['currency']}",[]).append(detail)

        return details

    def detect(self):

        return True if self._post('v2/auth/r/wallets') else False


    def order_info(self,order_id,coin,currency,must_in_history=False):
        detail = {'id':[ int(order_id)]}

        resp = None

        if not must_in_history:

            resp = self._post(f'v2/auth/r/orders/t{coin.upper()}{currency.upper()}',detail)  
        
        if not resp or len(resp)==0:

            resp = self._post(f'v2/auth/r/orders/t{coin.upper()}{currency.upper()}/hist',detail)  

        if resp and len(resp) > 0:

            rdetail = self.convert_retrieve_order(resp)
            logger.info('order info resp: %s',json.dumps(rdetail))

            return rdetail
        else:
            return None


    def ioc_order(self,price,size,coin,currency,side,coid=None):

        detail = {}

        detail['type'] = 'EXCHANGE IOC'
        detail['price'] = str(price)
        detail['symbol'] = f"t{coin.upper()}{currency.upper()}"
        if coid:
            detail['cid'] = int(coid)

        if 'buy' == side:
            detail['amount'] = str(size)
        elif 'sell' == side:
            detail['amount'] = str(-float(size))


        resp = self._post('v2/auth/w/order/submit',detail)  
        rdetail = self.convert_submit_order(resp)

        logger.info('ioc order resp: %s',json.dumps(rdetail))

        return rdetail['order_id']

    def limit_order(self, price ,size , coin , currency ,side , coid=None ):
        detail = {}

        detail['type'] = 'EXCHANGE LIMIT'
        detail['price'] = str(price)
        detail['symbol'] = f"t{coin.upper()}{currency.upper()}"

        if 'buy' == side:
            detail['amount'] = str(size)
        elif 'sell' == side:
            detail['amount'] = str(-float(size))


        return self._post('v2/auth/w/order/submit',detail)  

    def limit_orders(self, orders ):
        details = {}

        f_orders = []
        for order in orders:

            detail = {}
            detail['type'] = 'EXCHANGE LIMIT'
            detail['price'] = str(order.get('price'))
            detail['symbol'] = f"t{order.get('coin').upper()}{order.get('currency').upper()}"
            if 'buy' == order.get('side'):
                detail['amount'] = str(order.get('size'))
            elif 'sell' == order.get('side'):
                detail['amount'] = str(-float(order.get('size')))

            detail['cid'] = int(order.get('coid'))

            f_order = ['on',detail]

            f_orders.append(f_order)

        details['ops'] = f_orders

        resp = self._post('v2/auth/w/order/multi',details)  

        return self.convert_multi_order(resp) 

    def cancel_orders(self, order_ids , coin,currency):

        logger.info('will cancel orders: %s' , json.dumps(order_ids))

        details = {'ops':[["oc_multi", {'id': list(map(lambda s:int(s) ,order_ids))}]]}

        resp = self._post('v2/auth/w/order/multi',details)  

        j = self.convert_multi_order(resp) 

        logger.info.log('j: %s' , json.dumps(j))

        return j

    def place_order(self,type_,side,price,size,coin,currency):

        detail = {}

        if OrderType.Limit == type_:
            detail['type'] = 'EXCHANGE LIMIT'
        elif OrderType.IOC == type_:
            detail['type'] = 'EXCHANGE IOC'
        else:
            return 

        detail['price'] = price

        if 'buy' == side:
            detail['amount'] = str(size)
        elif 'sell' == side:
            detail['amount'] = str(-float(size))

        detail['symbol'] = f"t{coin.upper()}{currency.upper()}"

        return self._post('v2/auth/w/order/submit',detail)

    def wallets(self):

        return self._post('v2/auth/r/wallets')


    def orders(self,coin,currency):

        return self._post('v2/auth/r/orders/t%s%s' % (coin.upper(),currency.upper()) )

    def order_history(self,coin,currency):

        return self._post('v2/auth/r/orders/t%s%s/hist' % (coin.upper(),currency.upper()))

