from kdata import bar
import pandas as pd
import mpl_finance as mpf
import numpy as np
from matplotlib.pylab import date2num
import matplotlib.pyplot as plt
from matplotlib import ticker
import os

def formatdate(date):
    if isinstance(date, int):
        date=str(date)
    if isinstance(date, str):
        date=pd.to_datetime(date)
    return date

def gendateproxy(datetimes):
    datetime_nums = [int(date2num(datetime)) for datetime in datetimes]
    #print('datetime_nums', datetime_nums)
    length=len(datetime_nums)
    proxy = [inum+datetime_nums[0] for inum in np.arange(length)]
    #print(proxy)
    return proxy

def getproxynum(date):
    return gendateproxy([date])[0]

def drawk(stock, sdate, edate, savepath='./'):
    rawdf,stock=bar(stock)
    if rawdf is None:
        print('stock not exist', stock)
        return False
    sdate=formatdate(sdate)
    edate=formatdate(edate)
    sindex=rawdf.loc[ rawdf['datetime'] >= sdate ].index[0]
    eindex=rawdf.loc[ rawdf['datetime'] <= edate ].index[-1]
    append=1
    ssindex=sindex-append
    eeindex=eindex+append
    #print('aa',sindex, ssindex, eindex, eeindex)
    df=rawdf.iloc[ssindex:eeindex]
    fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(15,8))
    proxy=gendateproxy(df['datetime'].values)
    for i in proxy:
        ax1.axvline(i, linewidth=1, color = "r", ls='--')
    proxydate={p:d for p, d in zip(proxy,df['datetime'].values)}
    #print('len',len(df["open"].values))
    mpf.candlestick_ohlc(ax1, 
        zip(proxy, 
        df["open"].values,
        df["high"].values,
        df["low"].values,
        df["close"].values), 
        width=0.75, 
        colorup='r', 
        colordown='g', 
        alpha=0.75)
    title="[{}]-[{}]".format(stock,sdate.strftime("%Y%m%d"))
    ax1.set_title(title, fontsize=12, color='r')

    row=rawdf.iloc[sindex] 
    #print('start',row)
    #print('end', rawdf.iloc[eindex])
    text="ma5:{} ma10:{} ma20:{}".format(row['ma5'], row['ma10'], row['ma20'])
    ax1.text(1,1,text,fontsize=15,verticalalignment="top",horizontalalignment="right")
    ax1.set_ylabel('Price')
    ax1.grid(True)
    ax1.xaxis_date()
    #ax1.autoscale_view()

    ma5s=df['ma5'].tolist()
    ma10s=df['ma10'].tolist()
    ma20s=df['ma20'].tolist()
    ax1.plot(proxy, ma5s, linewidth=0.45, c='k', label='ma5:'+str(round(row['ma5'],3)))
    ax1.plot(proxy, ma10s, linewidth=0.45, c='y', label='ma10:'+str(round(row['ma10'],3)))
    ax1.plot(proxy, ma20s, linewidth=0.45, c='r', label='ma20:'+str(round(row['ma20'],3)))
    ax1.axvline(proxy[append], linewidth=1, color = "k", ls='--')
    ax1.axvline(proxy[-1-append], linewidth=1, color = "k", ls='--')
    fig.autofmt_xdate()
    plt.bar(proxy, df["volume"].values, width= 0.5)
    ax1.legend(loc='best')

    ax2.set_ylabel('Volume')
    ax2.grid(True)
    ax2.axvline(proxy[0], linewidth=1, color = "k", ls='--', label = "dashed")
    ax2.axvline(proxy[-1], linewidth=1, color = "k", ls='--', label = "dashed")
    #if adddate:
    #    ax1.axvline(getproxynum(adddate), linewidth=1, color = "r", ls='--')
    #    ax2.axvline(getproxynum(adddate), linewidth=1, color = "r", ls='--', label = "dashed2")
    def format_date(x, pos=None):
        x=np.clip(x, proxy[0], proxy[-1])
        #print('x',x)
        #return rawdf['datetime'].iat[int(x)]
        #print(proxydate)
        return str(proxydate[int(x)])[:10]
    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    ax2.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    if not savepath is None:
        name="-".join([stock,str(sdate)[:10],str(edate)[:10]])
        print(name)
        plt.savefig(os.path.join(savepath,name+'.png'))
        plt.close()
