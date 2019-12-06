import logging
import json
from ..events import EventType,MarketEvent


logger = logging.getLogger(__name__)

class Rate(object):
    """docstring for Rate"""
    def __init__(self,exchange, currencies,stablecoin,listener):
        super(Rate, self).__init__()
        self.exchange = exchange
        self.currencies = currencies
        self.stablecoin = stablecoin
        self.rates = {}
        self.listener = listener


    def on_ticker(self, coin,currency,timestamp,detail):

        
        key = "%s_%s" % (coin,currency)

        logger.info('rate ticker: %s' , key)
        logger.info('currencies: %s, stable: %s' , json.dumps(self.currencies), self.stablecoin)

        if coin in self.currencies and currency == self.stablecoin:
            self.rates[key] = detail.get('last')
            
            self.listener.on_market_event( MarketEvent('rates',self.rates, self.exchange ))

            
