import os
from rqalpha.environment import Environment
from rqalpha.data.data_proxy import DataProxy
from rqalpha.data.base_data_source import BaseDataSource
import rqalpha.api as api
import datetime
import pandas as pd
from tqsdk import ta

env = Environment({})
env.set_data_source(BaseDataSource('/home/jun/.rqalpha/bundle/'))
env.set_data_proxy(DataProxy(env.data_source, env.price_board))
data_proxy=env.data_proxy
def bar(instrument,bar_count=5000,fields=None,start_dt=21501020):
    if isinstance(start_dt, int):
        start_dt=pd.to_datetime(str(start_dt))
    elif isinstance(start_dt, str):
        start_dt=pd.to_datetime(start_dt)
    if isinstance(start_dt, pd.Timestamp):
        start_dt=datetime.date(start_dt.year,start_dt.month,start_dt.day)
    if len(str(instrument))==6:
        if int(instrument) >= 6000:
            instrument=str(instrument)+'.XSHG'
        else:
            instrument=str(instrument)+'.XSHE'
    dt = data_proxy.get_previous_trading_date(start_dt)
    bardata=data_proxy.history_bars(instrument,bar_count,'1d',fields,dt)
    if not bardata is None:
        bardf=pd.DataFrame(bardata)
        bardf['datetime']=bardf['datetime']/1000000
        bardf['datetime']=bardf['datetime'].astype(int).astype(str)
        bardf['datetime']=pd.to_datetime(bardf['datetime'])
        boll=ta.BOLL(bardf, 20, 2)
        bardf['bollu']=boll['top']
        bardf['bollm']=boll['mid']
        bardf['bolld']=boll['bottom']
        bardf['ma5']=ta.MA(bardf, 5)
        bardf['ma8']=ta.MA(bardf, 8)
        bardf['ma10']=ta.MA(bardf, 10)
        bardf['ma15']=ta.MA(bardf, 15)
        bardf['ma20']=ta.MA(bardf, 20)
        bardf['ma30']=ta.MA(bardf, 30)
        if os.path.exists('./stock') == True:
            bardf.to_csv('./stock/'+instrument+'.csv')
        return (bardf, instrument)
    #s=datetime.date(2019,1,1)
    #start_dt = datetime.datetime.combine(s, datetime.datetime.min.time())
    #dt = env.data_proxy.get_previous_trading_date(start_dt)
    #a=env.data_proxy.history_bars('600519.XSHG',1,'1d',['close','open','datetime'],dt)
__all__ = ['bar']
