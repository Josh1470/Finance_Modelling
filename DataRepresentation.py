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
        self.stocks = ['AMZN, AAPL, MSFT, GOOGL, FB, TSLA, NVDA']
        print(f'Stocks include {self.stocks}')
        graphStockData.chooseStock(self)

    def chooseStock(self):
        self.stockInfo = input('Enter Stock You Would Like to View')
        graphStockData.changeTimeSeries(self)
        return self.stockInfo


    def changeTimeSeries(self):
        print(f'''Availiable time series include : 
              {self.time_series}''')
        self.time = input('What time series would you like to view?')
        graphStockData.graphDesign(self)

    def graphDesign(self):
        self.colourInitial = ['b', 'g', 'r', 'c', 'm', 'y' ,'k', 'w']
        self.colour = ['blue','green','red','cyan','magenta','yellow','black','white']
        for i in range(len(self.colourInitial)):
            print(f'Input {self.colourInitial[i]} for {self.colour[i]}')
        self.colourChoice = input('What colour would you like?')
        graphStockData.graph(self)



    def graph(self):
        self.ticker = yf.Ticker(self.stockInfo)
        self.ticker_history = self.ticker.history(period=self.time)
        print((self.ticker_history['Open']))

        sf = self.ticker_history['Open']
        self.df = pd.DataFrame({'Date':sf.index, 'Open':sf.values,})

        x = self.df['Date'].tolist()
        y = self.df['Open'].tolist()

        #self.df['SMA_50'] = self.df['Open'].rolling(window=50).mean()
        #self.df['SMA_100'] = self.df['Open'].rolling(window=100).mean()

        #plt.style.use('ggplot')
        #ax = self.df.loc['Adj Close']\
                #.plot(y=['Adj Close', 'SMA_50', 'SMA100'], figsize=(13,10))

        plt.plot(x, y, self.colourChoice)
        plt.ylabel('Price($)')
        plt.xlabel('Date', rotation=0)
        plt.show()
        graphStockData.stats(self)



    def stats(self):
        self.column = self.df['Open']
        max_value = self.column.max()
        max_value = max_value.round(2)
        print(f'The maximum value of this stock in the time frame selected is {max_value}')

        min_value = self.column.min()
        min_value = min_value.round(2)
        print(f'The minimum value of this stock in the time frame selected is {min_value}')

        mean_value = self.column.mean()
        mean_value = mean_value.round(2)
        print(f'The mean value of this stock is {mean_value}')
        graphStockData.calcPercentage(self)

    def calcPercentage(self):
        self.First = self.column[0]
        self.Last = self.column[-1]
        self.change = (self.Last / self.First) * 100
        print(f'The stock {self.stockInfo} has increased by {self.change} in {self.time_series}')



        #self.df['SMA_50'] = self.df['Open'].rolling(window=50).mean()
        #self.df['SMA_100'] = self.df['Open'].rolling(window=100).mean()

        print(self.df)
        graphStockData.plotMA(self)

    def plotMA(self):
        plt.style.use('ggplot')
        ax = self.df.loc['Open'].plot(y=['SMA_50', 'SMA_100'])





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


a = graphStockData()






















