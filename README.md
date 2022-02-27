# Polygon_API
projects using Polygon API

There are three programns in this repo

plot.py and poject.py are inter-connected with each other.
stock_analysis.py is a sperate program
price.xlsx is result i got from running stock_analysis.py and sp_500_stocks.csv is used to produce that result it contains the ticker values of sp 500 companies.

the packages used in plot.py and project.py are:-
pandas:- for making dataframe
mplfinance:- for ploting a candle stick graph
datetime:- taking date time index to make api calls
polygon:- make api calls
project.py is used to make api call from polygon and gives the results in form of a .json format. Which is then used by plot.py to plot a candle stick graph for a company by
the data that was received.

stock_analysis.py 
packages used are:-
time:- use time for making api calls
pandas:- importing csv file, making excel sheets and forming DataFrame for data
requests:- making api calls
this program import the sp_500_stocks.csv file to take the ticker symbols and make the api calls for the selected date of all 500 companies and store the data in an excel file
(price.xlsx)
