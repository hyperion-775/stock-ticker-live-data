import yfinance as yf
from datetime import datetime
import math

#function to format large numbers
def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
     int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

millnames = ['',' Thousand',' Million',' Billion',' Trillion']
date_time = datetime.now()
string_date_time = date_time.strftime("%d/%m/%Y %H:%M:%S")
symbol = input('Enter stock symbol: ')
yfTicker = yf.Ticker(symbol).info
#print report
print("Name: " + yfTicker['longName'])
print("Last Price: $" + str(yfTicker['currentPrice']))
print("Market Time:" , string_date_time)
print("Change: " + str(round(yfTicker['52WeekChange'], 4)))
print("Volume: " + str(millify(yfTicker['averageDailyVolume10Day'])))
print("Market Cap: " + str(millify(yfTicker['marketCap'])))

#stock ticker table attempt using download function
#from_date = input('Enter start date(yyyy-mm-dd): ')
#end_date = input("Enter end date(yyyy-mm-dd): ")
#ticker_info = yf.download(symbol, from_date, end_date)
#print(ticker_info.head())
#print(ticker_info.tail())
