### INF601 - Advanced Programming in Python
### Julia Rogers
### Mini Project 1
import pprint
import yfinance as yf

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

mydata = {}

mytickers.sort()

for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                      'dailyHigh': result.info['dayHigh']
                      }
    #print(f"Ticker: {ticker} \tDaily High: {result.info['dayHigh']}")

pprint.pprint(mydata)



# get historical market data
#hist = msft.history(period="10d")

#pprint.pprint(hist)