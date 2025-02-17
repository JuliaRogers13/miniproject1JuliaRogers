### INF601 - Advanced Programming in Python
### Julia Rogers
### Mini Project 1
'''
INF601 - Programming in Python
Assignment #
I, Julia Rogers, affirm that the work submitted for this assignment
is entirely my own. I have not engaged in any form of academic dishonesty,
including but not limited to cheating, plagiarism, or the use of
unauthorized materials. I have neither provided nor received unauthorized
assistance and have accurately cited all sources in adherence to academic
standards. I understand that failing to comply with this integrity
statement may result in consequences, including disciplinary actions as
determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the
principles of academic integrity.
'''

import pprint
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import copy
import os

os.makedirs("charts", exist_ok=True)

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]


mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    hist = result.history(period="10d")
    last10days = []
    for date in hist["Close"][:11]:
        last10days.append(date)
    if len(last10days) == 10:
        maxlist = copy.copy(last10days)
        maxlist.sort()
        max_price = maxlist[-1]+10
        min_price = maxlist[0]-10
        myarray = np.array(last10days)
        plt.plot(myarray)
        plt.xlabel("Days Ago")
        plt.ylabel("Closing Price")
        plt.axis((9, 0, min_price, max_price ))
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.savefig(f"charts/{ticker}.png")
    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days.")