import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np


class graphStockData:
    def __init__(self):
        self.time = 0
        self.stockInfo = input('Enter Stock You Would Like to View')
        graphStockData.change_time_series(self)

    def change_time_series(self):
        self.time = input('Enter time series you would like to view: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo or max?')
        graphStockData.graph(self)

    def graph(self):
        self.ticker = yf.Ticker(self.stockInfo)
        self.ticker_history = self.ticker.history(period=self.time)
        print((self.ticker_history['Open']))

        sf = self.ticker_history['Open']
        df = pd.DataFrame({'Date':sf.index, 'Values':sf.values})

        x = df['Date'].tolist()
        y = df['Values'].tolist()

        plt.plot(x,y)
        plt.ylabel('Price($)')
        plt.xlabel('Date', rotation=0)
        plt.show()


class predictFuture(graphStockData):
    def __init__(self):
        super().__init__()
        predictFuture.movingAverage(self)

    def movingAverage(self):
        print(self.ticker)














a = graphStockData()
print(a)
b = predictFuture()
print(b)



