import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials as yF
from CLInterface import GetStockName as GSC


#import numpy as np



class graphStockData:
    def __init__(self):
        self.time_series = ['1m, 2m , 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo and max']
        self.time = 0                       #Defines key attributes for this class
        self.stocks = ['AMZN, AAPL, MSFT, GOOGL, FB, TSLA, NVDA']
        graphStockData.setOutStock(self)

    def setOutStock(self):
        print(f'Stocks include {self.stocks}') #Prints out the stock list for the user to view
        graphStockData.chooseStock(self)

    def chooseStock(self):
        self.stockInfo = input('Enter Stock You Would Like to View').upper() #Asks the user to input a stock they want to graph, and makes
        #the capiltilises the entire input as required by yFinance
        graphStockData.changeTimeSeries(self)


    def changeTimeSeries(self):
        print(f'''Availiable time series include : 
              {self.time_series}''') #Prints out the time series list for the user to view
        self.time = input('What time series would you like to view?') #Asks the user to input a time series they would like to see used when
        #graphing the stock
        graphStockData.graphDesign(self)

    def graphDesign(self):
        self.colourInitial = ['b', 'g', 'r', 'c', 'm', 'y' ,'k', 'w'] #Outlines the initials of the colour that can be graphed
        self.colour = ['blue','green','red','cyan','magenta','yellow','black','white'] #Outlines the names of the colours that can be graphed
        for i in range(len(self.colourInitial)): #Loops through the colourInitial list
            print(f'Input {self.colourInitial[i]} for {self.colour[i]}')
        self.colourChoice = input('What colour would you like?') #Asks the user to input a colour for the line to have
        graphStockData.graph(self)

    def getName(self):
        temp = self.stockInfo #Makes the temp equal to the stock the user has inputted
        if temp == 'AAPL':
            return 'Apple'
        elif temp == 'AMZN':
            return 'Amazon'
        elif temp == 'MSFT':
            return 'Microsoft'
        elif temp == 'GOOGL':
            return 'Google'
        elif temp == 'FB':
            return 'Facebook'
        elif temp == 'TSLA':
            return 'Telsa'
        elif temp == 'NVDA':
            return 'Nvidia'
        else:
            return temp.upper()



    def graph(self):
        self.ticker = yf.Ticker(self.stockInfo)
        self.ticker_history = self.ticker.history(period=self.time)
        print((self.ticker_history['Open']))

        sf = self.ticker_history['Open']
        self.df = pd.DataFrame({'Date':sf.index, 'Open':sf.values,})

        x = self.df['Date'].tolist()
        y = self.df['Open'].tolist()


        plt.plot(x, y, self.colourChoice)
        plt.ylabel('Price($)')
        plt.xlabel('Date', rotation=0)
        plt.title(f"Graph of {self.getName()}'s stock") #Graphs the stock
        plt.show()
        graphStockData.stats(self)



    def stats(self):
        self.column = self.df['Open']
        max_value = self.column.max()
        max_value = max_value.round(2)
        print(f'The maximum value of this stock in the time frame selected is {max_value}') #Finds the max value of the stock in the time frame

        min_value = self.column.min()
        min_value = min_value.round(2)
        print(f'The minimum value of this stock in the time frame selected is {min_value}') #Finds the min value of the stock in the time frame

        mean_value = self.column.mean()
        mean_value = mean_value.round(2)
        print(f'The mean value of this stock is {mean_value}') #Finds the mean value of the stock in the time frame
        graphStockData.calcPercentage(self)

    def calcPercentage(self):
        self.First = self.df['Open'].iloc[0]
        self.Last = self.df['Open'].iloc[-1]
        self.change = (self.Last / self.First) * 100
        self.change = self.change.round(2)
        print(f'The stock {self.stockInfo} has increased by {self.change}% in {self.time}') #Calculates the percentage change of the stock from
        #first dataframe entry to last dataframe entry
        graphStockData.moreIndicatiors(self)

    def moreIndicatiors(self):
        self.yahooFinance = yF(self.stockInfo)
        self.quoteTable = yF.get_pe_ratio(self.yahooFinance)
        print(f'Price Earnings ratio is {self.quoteTable}') #Returns the P/E ratio of the stock

        self.marketCap = yF.get_market_cap(self.yahooFinance)
        self.mc = self.marketCap/1000000000000
        print(f'Market cap is {self.mc}') #Returns the market cap of the stock



class oneStockTests(graphStockData):
    def __init__(self):
        super().__init__()








        #self.df['SMA_50'] = self.df['Open'].rolling(window=50).mean()
        #self.df['SMA_100'] = self.df['Open'].rolling(window=100).mean()







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






















