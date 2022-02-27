import time
import pandas as pd
from pip import main
import requests


stocks = pd.read_csv('sp_500_stocks.csv')
API_TOKEN = 'WD42r4ATWJNEbbbQv5SBhEbMZRgTOQfD'

my_col = ['Ticker','Open', 'Close', 'High', 'Low', 'Volume']
i=1
f_dataframe = pd.DataFrame(columns=my_col)

for symbol in stocks['Ticker']:
    i+=1 
    api_url = f'https://api.polygon.io/v1/open-close/{symbol}/2021-10-06?adjusted=true&apiKey={API_TOKEN}'
    data = requests.get(api_url).json()
    try:
        f_dataframe = f_dataframe.append(pd.Series([symbol,data['open'],data['close'],data['high'],data['low'],data['volume']], index = my_col),ignore_index = True)
        print(f_dataframe)
        print(i)
        if(i%5==0):
            print("if executed")
            time.sleep(60)
    except KeyError:
        print("can't call")
print(f_dataframe)
filename = pd.ExcelWriter("Price.xlsx", engine='xlsxwriter')
f_dataframe.to_excel(filename, sheet_name='Stock_Analysis', index=False)

background_color = '#0a0a23'
font_color = '#ffffff'

string_format = filename.book.add_format(
        {
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

dollar_format = filename.book.add_format(
        {
            'num_format':'$0.00',
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

integer_format = filename.book.add_format(
        {
            'num_format':'0',
            'font_color': font_color,
            'bg_color': background_color,
            'border': 1
        }
    )

column_format = {'A':['Ticker',string_format],
                 'B':['Open',dollar_format],
                 'C':['Close',dollar_format],
                 'D':['High',dollar_format], 
                 'E':['Low',dollar_format],
                 'F':['Volume',integer_format]
                }

for column in column_format.keys():
    filename.sheets['Stock_Analysis'].set_column(f'{column}:{column}', 20, column_format[column][1])
    filename.sheets['Stock_Analysis'].write(f'{column}1', column_format[column][0], string_format)
    
filename.save()  

if __name__ == '__main__':
    main() 