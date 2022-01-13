import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Tests import TestFunctions as tf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


class oneStock(tk.Frame):
    def __init__(self, master):
        super().__init__()

        stocks = 'AMZN AAPL MSFT  GOOGL  FB  TSLA NVDA'
        self.box = tk.StringVar()
        self.boxChoice = ttk.Combobox(textvariable=self.box)
        self.boxChoice['values'] = stocks
        self.boxChoice['state'] = 'readonly'
        self.boxChoice.current(0)
        self.boxChoice.grid(row=1, column=0, sticky='news', padx=10, pady=10)
        self.box.trace_add('write', self.getCurrentStock())


        timeSeries = '1m 2m 5m 15m 30m 60m 90m 1h 1d 5d 1wk 1mo 3mo max'
        self.timeBox = tk.StringVar()
        self.timeBox_choice = ttk.Combobox(textvariable=timeSeries)
        self.timeBox_choice['values'] = timeSeries
        self.timeBox_choice['state'] = 'readonly'
        self.timeBox_choice.current(13)
        self.timeBox_choice.grid(row=2, column=0, sticky='news', padx=10, pady=10)
        self.timeBox.trace_add('write', self.getCurrentTimeSeries())


        self.title = tk.Label(text='Graph One Stock', bg='Brown')

        self.homePage = tk.Button(text='Click to return to main menu', bg='orange', command=master.destroy)
        self.help = tk.Button(text='Click here for some help', bg='grey', command=master.destroy)
        self.twoStock = tk.Button(text='Click here to go to the two stock page', bg='red', command=master.destroy)
        self.graph = tk.Label(text=self.graphCurrentStock(self.getCurrentStock()), bg='green')

        self.mean = tk.Label(bg='#5C7AB9', text=f'The mean of the stock in the time frame is ${tf.getMean(self.getCurrentStock(), self.getCurrentTimeSeries())}')
        self.max = tk.Label(bg='#5C7AB9', text=f'The max of the stock in the time frame is ${tf.getMax(self.getCurrentStock(), self.getCurrentTimeSeries())}')
        self.min = tk.Label(bg='#5C7AB9', text=f'The min of the stock in the time frame is ${tf.getMin(self.getCurrentStock(), self.getCurrentTimeSeries())}')
        self.median = tk.Label(bg='#5C7AB9', text=f'The median of the stock in the time frame is ${tf.getMedian(self.getCurrentStock(), self.getCurrentTimeSeries())}')
        self.mode = tk.Label(bg='#5C7AB9', text=f'The range of this stock in the time frame is ${tf.getRange(self.getCurrentStock(), self.getCurrentTimeSeries())}')

        self.PC = tk.Label(bg='#5C7AB9', text=f'The Percentage change of this stock in the time frame is {tf.perChange(self.getCurrentStock(), self.getCurrentTimeSeries())}%')
        self.peRatio = tk.Label(bg='#5C7AB9', text=f'The price to earnings ratio of this stock in the time frame is {tf.peRatio(self.getCurrentStock())}')
        self.marketCap = tk.Label(bg='#5C7AB9', text=f'The market cap of this stock in the time frame {tf.marketCap(self.getCurrentStock())}T')
        self.yearlyHigh = tk.Label(bg='#5C7AB9', text=f'The yearly high of this stock is ${tf.getYearlyHigh(self.getCurrentStock())}')
        self.yearlyLow = tk.Label(bg='#5C7AB9', text=f'The yearly low of this stock is ${tf.getYearlyLow(self.getCurrentStock())}')


        self.title.grid(row=0, column=0, columnspan=12, sticky='news')

        self.mean.grid(row=4, column=0, rowspan=1, sticky='news', pady=5, padx=5)
        self.max.grid(row=5, column=0, rowspan=1, sticky='news', pady=5, padx=5)
        self.min.grid(row=6, column=0, rowspan=1, sticky='news', pady=5, padx=5)
        self.median.grid(row=7, column=0, rowspan=1, sticky='news', pady=5, padx=5)
        self.mode.grid(row=8, column=0, rowspan=1, sticky='news', pady=5, padx=5)
        self.peRatio.grid(row=9, column=0, rowspan=1, sticky='news', pady=5, padx=5)
        self.PC.grid(row=10, column=0, rowspan=1, sticky='news', pady=5, padx=5)
        self.marketCap.grid(row=11, column=0, rowspan=1, sticky='news', pady=5, padx=5)
        self.yearlyHigh.grid(row=12, column=0, rowspan=1, sticky='news', pady=5, padx=5)
        self.yearlyLow.grid(row=13, column=0, rowspan=1, sticky='news', pady=5, padx=5)

        self.homePage.grid(row=14,column=0, columnspan=9, sticky='news')
        self.help.grid(row=15, column=0, columnspan=9, sticky='news')
        self.twoStock.grid(row=14, column=10, rowspan=2, columnspan=2, sticky='news')



    def getCurrentStock(*args):
        # if self.box.get() != 'AMZN':
        #     self.update()
        #     return self.box.get()
        # else:
        #     return 'AMZN'
        return 'AMZN'

    def getCurrentTimeSeries(*args):
        return 'max'

    def getCurrentDataFrame(self, stock, timeseries):
        df = tf.getDataFrame(stock, self.getCurrentTimeSeries())
        return df

    def update(self):
        self.destroy()
        self.__init__(self)


    def graphCurrentStock(self, stock):
        figure = plt.figure(figsize=(4,4), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure)
        xlabel = 'Date of Stocks'
        ylabel = 'Price($)'
        chart_type.get_tk_widget().grid(row=1, column=4, rowspan=13, columnspan=9, sticky='news', padx=20, pady=20)
        df = tf.x
        df.plot(kind='line', legend=True, ax=ax, xlabel=xlabel, ylabel=ylabel, title=f"{self.getCurrentStock().upper()}'s stock history in {self.getCurrentTimeSeries()}")
        plt.gcf().canvas.draw()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry("750x750")
    oneStock = oneStock(root)
    # oneStock.pack()
    root.mainloop()

