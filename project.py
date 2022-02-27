import datetime
from polygon import RESTClient


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def data_main(stockTicker,multipliar,indexFormat,_from,_to):
    """
    stockTicker: the ticker symbol for the company which's prices you want to plot

    indexFormat: what kind of time variation you want eg:- date to date or hour to hour

    multiplier: add on to time variation eg:- if indexFormat is 'hour' and multiplier is 1
    means the next price it will receive will be 1 hour in future from the previous time.

    _from: start date of data you want to receive(str format)

    _to: till which date you want the data to be received(str)
    ----------------------------------------------------------------------------------
    return: resp a json file having data needed
    
    """
    API_KEY="Your API Token"
    with RESTClient(API_KEY) as client:

        resp = client.stocks_equities_aggregates(stockTicker, multipliar, indexFormat, _from, _to, unadjusted=True)
    return resp   
