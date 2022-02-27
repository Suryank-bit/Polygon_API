import datetime
from polygon import RESTClient


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def data_main(stockTicker,multipliar,indexFormat,_from,_to):
    API_KEY="Your API Token"
    with RESTClient(API_KEY) as client:

        resp = client.stocks_equities_aggregates(stockTicker, multipliar, indexFormat, _from, _to, unadjusted=True)
    return resp   
