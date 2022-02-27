import pandas as pd
from pandas import DataFrame
import project
import mplfinance as mpf

"""
Pandas used for dataframes
-------------------------------------------------------------------------------------
project is a module for making polygon API calls
-------------------------------------------------------------------------------------
mplfinance is used to plot the candle-stick graph

"""

def data_Frame(stockTicker,multiplier,indexFormat,_from,_to):
    resp = project.data_main(stockTicker,multiplier,indexFormat,_from,_to)
    """
    stockTicker: the ticker symbol for the company which's prices you want to plot

    indexFormat: what kind of time variation you want eg:- date to date or hour to hour

    multiplier: add on to time variation eg:- if indexFormat is 'hour' and multiplier is 1
    means the next price it will receive will be 1 hour in future from the previous time.

    _from: start date of data you want to receive(str format)

    _to: till which date you want the data to be received(str)
    ----------------------------------------------------------------------------------
    return: this function return a dataframe with a date index and opening, closing,
    highest, lowest price stock reached on the date
    
    """
    x=[]
    O=[]
    C=[]
    H=[]
    L=[] 
    for result in resp.results:
        dt = project.ts_to_datetime(result["t"])
        op = (result["o"])
        cl = (result["c"])
        hi = (result["h"])
        lo = (result["l"])
        x.append(dt)
        O.append(op)
        C.append(cl)
        H.append(hi)
        L.append(lo)
    
    x = pd.to_datetime(x)    
    dict = { 'Open' : O, 'Close' : C, 'High' : H, 'Low' : L} 
    data = DataFrame(dict, index=x)   

    return data
    
a = data_Frame('AAPL', 1, 'hour', '2020-10-11', '2020-10-12')

print(a.Open)

mpf.plot(a,volume=False,style='yahoo',type='candle')
