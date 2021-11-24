import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import TestFunctions as tf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class oneStock(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.timeVal = '5d'


        stocks = "AMZN AAPL MSFT GOOGL FB TSLA NVDA"
        self.box = ttk.Combobox(root, textvariable=stocks)
        #self.box.set('aapl')
        self.box['values'] = stocks
        self.box['state'] = 'readonly'





        timeSeries = '1m 2m 5m 15m 30m 60m 90m 1h 1d 5d 1wk 1mo 3mo max'
        self.timeBox = ttk.Combobox(root, textvariable=timeSeries)
        #self.timeBox.set('Please choose a time series')
        self.timeBox['values'] = timeSeries
        self.timeBox['state'] = 'readonly'


        self.title = tk.Label(text='Graph One Stock', bg='Brown')

        self.homePage = tk.Button(text='Click to return to main menu', bg='orange', command=master.destroy)
        self.help = tk.Button(text='Click here for some help', bg='grey', command=master.destroy)
        self.twoStock = tk.Button(text='Click here to go to the two stock page', bg='red', command=master.destroy)
        self.graph = tk.Label(text=tf.graphStock("AAPL"), bg='green')

        self.mean = tk.Label(bg='#5C7AB9', text=f'The mean of the stock in the time frame is ${tf.getMean("AAPL")}')
        self.max = tk.Label(bg='#5C7AB9', text=f'The max of the stock in the time frame is ${tf.getMax("AAPL")}')
        self.min = tk.Label(bg='#5C7AB9', text=f'The min of the stock in the time frame is ${tf.getMin("AAPL")}')
        self.median = tk.Label(bg='#5C7AB9', text=f'The median of the stock in the time frame is ${tf.getMedian("AAPL")}')
        self.mode = tk.Label(bg='#5C7AB9', text=f'The range of this stock in the time frame is ${tf.getRange("AAPL")}')

        self.PC = tk.Label(bg='#5C7AB9', text=f'The Percentage change of this stock in the time frame is {tf.perChange("AAPL")}%')
        self.peRatio = tk.Label(bg='#5C7AB9', text=f'The price to earnings ratio of this stock in the time frame is {tf.peRatio("AAPL")}')
        self.marketCap = tk.Label(bg='#5C7AB9', text=f'The market cap of this stock in the time frame {tf.marketCap("AAPL")}T')
        self.yearlyHigh = tk.Label(bg='#5C7AB9', text=f'The yearly high of this stock is ${tf.getYearlyLow("AAPL")}')
        self.yearlyLow = tk.Label(bg='#5C7AB9', text=f'The yearly low of this stock is ${tf.getYearlyHigh("AAPL")}')


        self.title.grid(row=0, column=0, columnspan=12, sticky='news')
        self.box.grid(row=1, column=0, columnspan=1, sticky='news', padx=10, pady=10)
        self.timeBox.grid(row=2, column=0, columnspan=1, sticky='news', padx=10, pady=10)

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
        self.graph.grid(row=1, column=4, rowspan=13, columnspan=9, sticky='news', padx=5, pady=5)
        self.help.grid(row=15, column=0, columnspan=9, sticky='news')
        self.twoStock.grid(row=14, column=10, rowspan=2, columnspan=2, sticky='news')

        self.box.bind('<<ComboboxSelected>>', self.stocksChanged)
        self.timeBox.bind('<<ComboboxSelected>>', self.timeChanged)

    def stocksChanged(self, event):
        self.boxVal = 'aapl'
        return self.boxVal


    def timeChanged(self, event):
        self.timeVal = self.timeBox.get()
        print(self.timeVal)

        self.timeMsg = f'You selected {self.timeVal}'
        print(self.timeMsg)
        showinfo(title='result', message=self.timeMsg)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry("750x750")
    oneStock = oneStock(root)
    # oneStock.pack()
    root.mainloop()
