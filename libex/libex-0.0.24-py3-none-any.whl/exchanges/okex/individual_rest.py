import logging 
import json
import traceback

from .sdk import spot_api  as spot

from ...fail_exception import FailException 
from .code_converter import rest_code
from .sdk.exceptions import OkexAPIException
from .helper import rslv_order_type,rslv_order_status,rslv_symbol

logger = logging.getLogger(__name__)

class IndividualRest(object):


    """docstring for CommandAdapter"""
    def __init__(self, apikey,secrets):
        super(IndividualRest, self).__init__()
        self.apikey =  apikey
        self.secretkey = secrets.get('keysecret')
        self.passphrase = secrets.get('passphrase')

        self.spotApi = spot.SpotAPI(self.apikey, self.secretkey, self.passphrase, True)

    def convert_order(self,origin):
    
        detail = {}

        detail['order_id'] = str(origin.get('order_id'))
        detail['coid'] = str(origin.get('client_oid'))
        detail['price'] = str(origin.get('price'))
        detail['size'] = str(origin.get('size'))
        detail['side'] = origin.get('side')
        detail['type'] = rslv_order_type(origin.get('type'),origin.get('order_type')).value
        detail['status'] = rslv_order_status(origin.get('state')).value
        detail['coin'],detail['currency'] = rslv_symbol(origin.get('instrument_id'))
        detail['filled_size'] = origin.get('filled_size')
        detail['filled_notional'] = origin.get('filled_notional')
        detail['timestamp'] = origin.get('timestamp')

        return detail


    def detect(self):
        try:
            self.spotApi.get_account_info()
            logger.info('detect success!')
    
            return True
    
        except Exception as e:
            logger.warning('detect failed,%s', str(e) )

            logger.error(traceback.format_exc())

            return False
        
    def order_info(self,orderid,coin,currency,must_in_history=False):

        instrument_id = '%s-%s' % (coin,currency)
        try:
            result = self.spotApi.get_order_info(orderid , instrument_id )

            logger.info('order_detail, resp : %s' , result )

            # ret = {
            #     'order_id':result.get('order_id'),
            #     'filled_amount':result.get('filled_size'),
            #     'filled_volume':result.get('filled_notional'),
            #     'created_at':result.get('created_at'),
            #     'timestamp':result.get('timestamp'),
            #     'status':result.get('status')
            # }


            # if result.get('type') == 'limit' and result.get('side') == 'buy':
            #     ret['type'] = 'limit_buy'
            #     ret['price'] = result.get('price')
            #     ret['amount'] = result.get('size')
            # elif result.get('type') == 'limit' and result.get('side') == 'sell':

            #     ret['type'] = 'limit_sell'
            #     ret['price'] = result.get('price')
            #     ret['amount'] = result.get('size')

            # elif result.get('type') == 'market' and result.get('side') == 'buy':
            #     ret['type'] = 'market_buy'
            #     ret['volume'] = result.get('notional')

            # elif result.get('type') == 'market' and result.get('side') == 'sell':
            #     ret['type'] = 'market_buy'
            #     ret['amount'] = result.get('size')

            detail = self.convert_order( result)

            return detail

        except OkexAPIException as e:

            logger.error('OkexAPIException:%s, %s',e.status_code,e.response.text)

            obj = e.response.json()

            code = rest_code(obj.get('code') , 40500)

            raise FailException(code,obj.get('message'))

    def ioc_order(self, price ,amount , coin , currency ,side , coid=None ):
         
        otype = 'limit'
        side = side
        instrument_id = '%s-%s' % (coin,currency)
        size = '%s' % amount
        price = '%f' % price
        

        logger.debug(f'otype:{otype} , side:{side} , instrument_id:{instrument_id} , price:{price} , size:{size}')

        try:
            result = self.spotApi.take_order(otype,side,instrument_id, size=size ,client_oid=coid ,price=price,order_type='3')
            logger.info('ioc_order, resp : %s' , result )
        
            if result.get('result'):
                return result.get('order_id')

            else :
                raise FailException(rest_code(result.get('error_code')),result.get('error_message'))

        except OkexAPIException as e:
            logger.error('OkexAPIException:%s, %s',e.status_code,e.response.text)

            obj = e.response.json()

            code = rest_code(obj.get('code'))

            raise FailException(code,obj.get('message'))

        

        

    def limit_order(self, price ,amount , coin , currency ,side , coid=None ):
         
        otype = 'limit'
        side = side
        instrument_id = '%s-%s' % (coin,currency)
        size = '%s' % amount  
        price = '%f' % price 
        

        logger.debug(f'otype:{otype} , side:{side} , instrument_id:{instrument_id} , price:{price} , size:{size}')

        try:
            result = self.spotApi.take_order(otype,side,instrument_id, size=size ,client_oid=coid ,price=price)
            logger.info('limit_order, resp : %s' , result )
        
            if result.get('result'):
                return result.get('order_id')

            else :

                raise FailException(rest_code(result.get('error_code')),result.get('error_message'))

        except OkexAPIException as e:
            logger.error('OkexAPIException:%s, %s',e.status_code,e.response.text)

            obj = e.response.json()

            code = rest_code(obj.get('code'))

            raise FailException(code,obj.get('message'))

        

        

    def limit_orders_appender(self ,orders, price ,amount , side , coin , currency):    

        otype = 'limit'
        instrument_id = '%s-%s' % (coin,currency)
        size = '%s' % amount  
        price = '%s' % price 
        
        return self.spotApi.orders_appender(orders, otype,side,instrument_id,size,price=price)


    #[{type,price,size,coin,currency}]
    def limit_orders(self, orders ):
        
        logger.debug('limit_orders, start .. ')

        f_orders = []

        for order in orders:

            detail = {}

            detail['instrument_id'] = f"{order.get('coin')}-{order.get('currency')}"
            detail['client_oid'] = order.get('coid')
            detail['type'] = 'limit'
            detail['side'] = order.get('side')
            detail['price'] = order.get('price')
            detail['size'] = order.get('size')

            f_orders.append(detail)

        remain_orders = f_orders[0:]

        ret = {}

        while len(remain_orders) > 0:
            step_orders = remain_orders[0:10] 
            remain_orders = remain_orders[10:]

            logger.info('limit_orders, req : %s' , step_orders )

            obj = self.spotApi.take_orders(step_orders)

            logger.info('limit_orders, resp : %s' , obj )

            for k,v in obj.items():

                for item in v:
                    ret.setdefault(k,[]).append({
                        'order_id':item.get('order_id'),
                        'coid':item.get('client_oid')
                        })

        return ret

    def market_order(self, size , coin , currency , side ,coid =None):

        otype = 'market'
        side = side
        instrument_id = '%s-%s' % (coin,currency)
        if side == 'buy':
            funds = '%s' % size
        elif side == 'sell':
            size = '%s' % size

        try:
            result = self.spotApi.take_order(otype,side,instrument_id,client_oid=coid,size=size,funds=funds)

            logger.debug('market_buy, resp : %s' , result )

            return result.get('order_id')

        except OkexAPIException as e:
            logger.error('OkexAPIException:%s, %s',e.status_code,e.response.text)

            obj = e.response.json()

            code = rest_code(obj.get('code'))

            raise FailException(code,obj.get('message'))


    def cancel_order(self, orderid, coin,currency ):

        logger.info(f'cancel_order,{orderid},{coin},{currency}')

        instrument_id = '%s-%s' % (coin,currency)
        try:
            result = self.spotApi.revoke_order(orderid , instrument_id )

            logger.debug('cancel order, resp : %s' , result )

            return result

        except OkexAPIException as e:

            logger.error('OkexAPIException:%s, %s',e.status_code,e.response.text)

            obj = e.response.json()

            code = rest_code(obj.get('code'),40600)

            raise FailException(code,obj.get('message'))

    def cancel_orders(self, order_ids , coin,currency):

        instrument_id = '%s-%s' % (coin,currency)
        
        remain_ids = order_ids[0:]

        try:

            ret = {}

            while len(remain_ids) > 0:    
                step_ids = remain_ids[0:10] 
                remain_ids = remain_ids[10:]
                logger.debug('cancel_orders,step_ids: %s', step_ids)
                obj = self.spotApi.revoke_orders(instrument_id , step_ids)

                for k,v in obj.items():
                    ret.setdefault(k,[]).extend(v)

            logger.info('cancel_orders, ret: %s', ret)

            return ret
        except OkexAPIException as e:
            logger.error('OkexAPIException:%s, %s',e.status_code,e.response.text)

            obj = e.response.json()

            code = rest_code(obj.get('code'),40600)

            raise FailException(code,obj.get('message'))


        