import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Tests import TestFunctions2 as tf2
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class twoStock(tk.Frame):
    def __init__(self, master):
        super().__init__()

        self.mean = 'Mean'
        self.min = 'Minimum'
        self.max = 'Maximum'
        self.median = 'Median'
        self.marketCap = 'Market Cap (T)'
        self.percentageChange = 'Percentage Change (%)'

        self.x = tf2.getDataFrame(self.getCurrentStockA(), self.getCurrentTimeSeries())
        self.y = tf2.getDataFrame(self.getCurrentStockB(), self.getCurrentTimeSeries())

        stocks = "AMZN AAPL MSFT GOOGL FB TSLA NVDA"
        timeSeries = '1m 2m 5m 15m 30m 60m 90m 1h 1d 5d 1wk 1mo 3mo max'

        self.stockA = tk.StringVar()
        self.stockAChoice = ttk.Combobox(textvariable=self.stockA)
        self.stockAChoice['values'] = stocks
        self.stockAChoice['state'] = 'readonly'
        self.stockAChoice.current(0)
        self.stockAChoice.grid(row=1, column=0, rowspan=4, sticky='news', padx=5, pady=5)
        self.stockA.trace_add('write', self.getCurrentStockA())

        self.stockB = tk.StringVar()
        self.stockBChoice = ttk.Combobox(textvariable=self.stockB)
        self.stockBChoice['values'] = stocks
        self.stockBChoice['state'] = 'readonly'
        self.stockBChoice.current(1)
        self.stockBChoice.grid(row=1, column=1, rowspan=4, sticky='news', padx=5, pady=5)
        self.stockB.trace_add('write', self.getCurrentStockB())

        self.timeBox = tk.StringVar()
        self.timeBoxChoice = ttk.Combobox(textvariable=self.timeBox)
        self.timeBoxChoice['values'] = timeSeries
        self.timeBoxChoice['state'] = 'readonly'
        self.timeBoxChoice.current(0)
        self.timeBoxChoice.grid(row=1, column=2, rowspan=4, sticky='news', padx=5, pady=5)
        self.timeBox.trace_add('write', self.getCurrentTimeSeries())

        self.title = tk.Label(text='Graph two stocks simultaneously', bg='blue', fg='white')

        self.homepage = tk.Button(text='Click here to return to the homepage', command=master.destroy, bg='red',
                                  fg='white')
        self.stock = tk.Label(text='Indicators', bg='lightblue')
        self.oneStock = tk.Label(text=f'Stock A is {self.getStockName(self.getCurrentStockA())}', bg='green')
        self.otherStock = tk.Label(text=f'Stock B is {self.getStockName(self.getCurrentStockB())}', bg='green')
        self.indGuide = tk.Label(text='Which Indicators wins?', bg='green')
        self.graph = tk.Label(text=self.graphStocks())

        self.Mean1 = tk.Label(text=tf2.getMean(self.getCurrentStockA(), self.getCurrentStockB(), self.x))
        self.Min1 = tk.Label(text=tf2.getMin(self.getCurrentStockA(), self.getCurrentTimeSeries(), self.x))
        self.Max1 = tk.Label(text=tf2.getMax(self.getCurrentStockA(), self.getCurrentTimeSeries(), self.x))
        self.Median1 = tk.Label(text=tf2.getMedian(self.getCurrentStockA(), self.getCurrentTimeSeries(), self.x))
        self.MarketCap1 = tk.Label(text=tf2.marketCap(self.getCurrentStockA()))
        self.PC1 = tk.Label(text=tf2.perChange(self.getCurrentStockA(), self.getCurrentTimeSeries(), self.x))

        self.Mean2 = tk.Label(text=tf2.getMean(self.getCurrentStockA(), self.getCurrentStockB(), self.y))
        self.Min2 = tk.Label(text=tf2.getMin(self.getCurrentStockB(), self.getCurrentTimeSeries(), self.y))
        self.Max2 = tk.Label(text=tf2.getMax(self.getCurrentStockB(), self.getCurrentTimeSeries(), self.y))
        self.Median2 = tk.Label(text=tf2.getMedian(self.getCurrentStockB(), self.getCurrentTimeSeries(), self.y))
        self.MarketCap2 = tk.Label(text=tf2.marketCap(self.getCurrentStockB()))
        self.PC2 = tk.Label(text=tf2.perChange(self.getCurrentStockB(), self.getCurrentTimeSeries(), self.y))

        self.Ind1 = tk.Label(text='Mean', bg='lightblue')
        self.Ind2 = tk.Label(text='Min', bg='lightblue')
        self.Ind3 = tk.Label(text='Max', bg='lightblue')
        self.Ind4 = tk.Label(text='Median', bg='lightblue')
        self.Ind5 = tk.Label(text='Market Cap (T)', bg='lightblue')
        self.Ind6 = tk.Label(text='Percentage Change (%)', bg='lightblue')

        self.HoL1 = tk.Label(
            text=(self.highLow(tf2.getMean(self.getCurrentStockA(), self.getCurrentTimeSeries(), self.x)
                               , tf2.getMean(self.getCurrentStockB(), self.getCurrentTimeSeries(), self.y), self.mean)),
            bg='orange')

        self.HoL2 = tk.Label(text=(self.highLow(tf2.getMin(self.getCurrentStockA(), self.getCurrentTimeSeries(), self.x)
                                                , tf2.getMin(self.getCurrentStockB(), self.getCurrentTimeSeries(),
                                                             self.y), self.min)), bg='orange')

        self.HoL3 = tk.Label(text=(self.highLow(tf2.getMax(self.getCurrentStockA(), self.getCurrentTimeSeries(), self.x)
                                                , tf2.getMax(self.getCurrentStockB(), self.getCurrentTimeSeries(),
                                                             self.y), self.max)), bg='orange')

        self.HoL4 = tk.Label(
            text=(self.highLow(tf2.getMedian(self.getCurrentStockA(), self.getCurrentTimeSeries(), self.x)
                               , tf2.getMedian(self.getCurrentStockB(), self.getCurrentTimeSeries(), self.y),
                               self.median)), bg='orange')

        self.HoL5 = tk.Label(text=(self.highLow(tf2.marketCap(self.getCurrentStockA())
                                                , tf2.marketCap(self.getCurrentStockB()), self.marketCap)), bg='orange')

        self.HoL6 = tk.Label(
            text=(self.highLow(tf2.perChange(self.getCurrentStockA(), self.getCurrentTimeSeries(), self.x)
                               , tf2.perChange(self.getCurrentStockB(), self.getCurrentTimeSeries(), self.y),
                               self.percentageChange)), bg='orange')

        self.title.grid(row=0, column=0, columnspan=95, sticky='news')

        self.homepage.grid(row=12, column=0, columnspan=4, sticky='news')
        self.stock.grid(row=5, column=0, sticky='news')
        self.oneStock.grid(row=5, column=1, sticky='news')
        self.otherStock.grid(row=5, column=2, sticky='news')
        self.indGuide.grid(row=5, column=3, sticky='news')

        self.Mean1.grid(row=6, column=1, sticky='news')
        self.Min1.grid(row=7, column=1, sticky='news')
        self.Max1.grid(row=8, column=1, sticky='news')
        self.Median1.grid(row=9, column=1, sticky='news')
        self.MarketCap1.grid(row=10, column=1, sticky='news')
        self.PC1.grid(row=11, column=1, sticky='news')

        self.Mean2.grid(row=6, column=2, sticky='news')
        self.Min2.grid(row=7, column=2, sticky='news')
        self.Max2.grid(row=8, column=2, sticky='news')
        self.Median2.grid(row=9, column=2, sticky='news')
        self.MarketCap2.grid(row=10, column=2, sticky='news')
        self.PC2.grid(row=11, column=2, sticky='news')

        self.Ind1.grid(row=6, column=0, sticky='news', pady=10)
        self.Ind2.grid(row=7, column=0, sticky='news', pady=10)
        self.Ind3.grid(row=8, column=0, sticky='news', pady=10)
        self.Ind4.grid(row=9, column=0, sticky='news', pady=10)
        self.Ind5.grid(row=10, column=0, sticky='news', pady=10)
        self.Ind6.grid(row=11, column=0, sticky='news', pady=11)

        self.HoL1.grid(row=6, column=3, sticky='news', pady=10)
        self.HoL2.grid(row=7, column=3, sticky='news', pady=10)
        self.HoL3.grid(row=8, column=3, sticky='news', pady=10)
        self.HoL4.grid(row=9, column=3, sticky='news', pady=10)
        self.HoL5.grid(row=10, column=3, sticky='news', pady=10)
        self.HoL6.grid(row=11, column=3, sticky='news', pady=10)

    def getCurrentStockA(*args):
        return 'AMZN'

    def getCurrentStockB(*args):
        return 'AAPL'

    def getCurrentTimeSeries(self, *args):
        return '1mo'

    def graphStocks(self):
        figure = plt.figure(figsize=(6, 6), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure)
        xlabel = 'Days since opening of time frame'
        ylabel = 'Price($)'
        chart_type.get_tk_widget().grid(row=1, column=4, rowspan=13, columnspan=9, sticky='news', padx=20, pady=20)
        self.stockList = [self.getCurrentStockA(), self.getCurrentStockB()]
        for stock in self.stockList:
            self.df = tf2.getDataFrame(stock, self.getCurrentTimeSeries())
            self.df['log_ret'] = np.log(self.df['Open']) - np.log(self.df['Open'].shift(1))
            self.df['cum_sum'] = self.df['log_ret'].cumsum()
            self.df['ma'] = self.df['cum_sum'].rolling(window=2).mean()
            self.df2 = self.df.set_index('Date')
            self.df2['cum_sum'].plot(kind='line', legend=True, ax=ax,  xlabel=xlabel, ylabel=ylabel,
                                    title=f'Graph of {self.getStockName(self.getCurrentStockA())} and {self.getStockName(self.getCurrentStockB())}')
            self.df2['ma'].plot()

        plt.legend([self.getStockName(self.getCurrentStockA()), f'Moving Average of {self.getStockName(self.getCurrentStockA())}',
        self.getStockName(self.getCurrentStockB()),f'Moving Average of {self.getStockName(self.getCurrentStockB())}'])
        #plt.legend([self.getStockName(self.getCurrentStockA()), self.getStockName(self.getCurrentStockB())])


        plt.gcf().canvas.draw()

    def highLow(self, stock1val, stock2val, indicator):
        self.stock1val = stock1val
        self.stock2val = stock2val
        self.indicator = indicator
        if self.stock1val > self.stock2val:
            return f'{self.getCurrentStockA()} has a higher {self.indicator} than {self.getCurrentStockB()}'
        elif self.stock1val < self.stock2val:
            return f'{self.getCurrentStockB()} has a higher {self.indicator} than {self.getCurrentStockA()}'

    def split(self, word):
        return [char for char in word]

    def getStockName(self, word):
        temp = self.split(word)
        if temp[0] == 'A':
            if temp[1] == 'M':
                return 'Amazon (AMZN)'
            elif temp[1] == 'A':
                return 'Apple (AAPL)'
        elif temp[0] == 'M':
            return 'Microsoft (MSFT)'
        elif temp[0] == 'G':
            return 'Google (GOOGL)'
        elif temp[0] == 'F':
            return 'Facebook (FB)'
        elif temp[0] == 'T':
            return 'Telsa (TSLA)'
        elif temp[0] == 'N':
            return 'Nvidia (NVDA)'



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry("1250x1250")
    twoStock = twoStock(root)
    # oneStock.pack()
    root.mainloop()