import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class stockData:
    def __init__(self,stock):
        self.stock = stock
        ticker = yf.Ticker(self.stock)
        ticker_history = ticker.history(period='max')
        print((ticker_history['Open']))

        sf = ticker_history['Open']
        df = pd.DataFrame({'Date':sf.index, 'Values':sf.values})

        x = df['Date'].tolist()
        y = df['Values'].tolist()

        plt.plot(x,y)
        plt.ylabel('Price($)')
        plt.xlabel('Date', rotation=0)
        plt.show()


y = stockData('AAPL')
print(y)

