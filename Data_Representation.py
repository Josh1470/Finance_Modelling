import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import hvplot.pandas
#import numpy as np




class graphStockData:
    def __init__(self):
        self.time_series = ['1m, 2m , 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo and max']
        self.time = 0
        graphStockData.setOutStock(self)

    def setOutStock(self):
        self.stocks = ['AMZN, O, NNN, LYB, EPD, KMI, R, VALE, FCX, CAT, OSK, NEM, NVDA, TSM, NUE']
        print(f'Stocks include {self.stocks}')
        graphStockData.chooseStock(self)

    def chooseStock(self):
        self.stockInfo = input('Enter Stock You Would Like to View')
        graphStockData.change_time_series(self)
        return self.stockInfo


    def change_time_series(self):
        print(f'''Availiable time series include : 
              {self.time_series}''')
        self.time = input('What time series would you like to view?')
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

        print(self.stocks)
        z = input('Would you like to add another stock to compare').lower()
        if z == 'yes':
            pass


class graphManyStocks(graphStockData):
    def __init__(self):
        super().__init__()
        graphManyStocks.chooseStocks(self)


    def chooseStocks(self):
        print(self.stocks)
        self.stockA = input('Choose stock to be displayed')
        self.stockB = input('Choose stock to be displayed')
        graphManyStocks.graphStocks(self)
    #def chooseStockTimeSeries(self):

    def graphStocks(self):


        pass

choice = input('''Would you like to plot:
                1: A graph with one stock
                2: A graph with two stocks''')

if choice == '1':
    a = graphStockData()
    print(a)
elif choice == '2':
    b = graphManyStocks()
    print(b)



















