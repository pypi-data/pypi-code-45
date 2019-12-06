import logging 
import importlib


logger = logging.getLogger(__name__)


def load_native_ex(ex):

    mstr = 'libex.exchanges.' + ex + '.native_ex'

    m = importlib.import_module(mstr) 

    return m


def load_individual_rest(ex , apikey, secrets ):
 
    mstr = 'libex.exchanges.' + ex + '.individual_rest'

    logger.debug('load class: ' + mstr)

    m = importlib.import_module(mstr) 

    ex_class = getattr (m, 'IndividualRest')

    ex_rest = ex_class(apikey, secrets)

    return ex_rest

def load_individual_ws(ex ,apikey , secrets ,symbols,coins,listener ):
 
    mstr = 'libex.exchanges.' + ex + '.individual_ws'

    logger.info('load class: ' + mstr)

    m = importlib.import_module(mstr) 

    ex_class = getattr (m, 'IndividualWs')

    ex_ws = ex_class(apikey ,secrets , symbols, coins , listener)

    return ex_ws

def load_market_ws(ex , symbols ,channels , listener ,currencies=None,stablecoin=None):
 
    mstr = 'libex.exchanges.' + ex + '.market_ws'

    logger.debug('load class: ' + mstr)

    m = importlib.import_module(mstr) 

    ex_class = getattr (m, 'MarketWs')

    ex_ws = ex_class(ex , symbols, channels , listener,currencies,stablecoin)

    return ex_ws