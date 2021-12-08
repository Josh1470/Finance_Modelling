import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Tests import TestFunctions as tf


class twoStock(tk.Frame):
    def __init__(self, master):
        super().__init__()
        stock1 = 'AAPL'
        stock2 = 'MSFT'

        stocks = "AMZN AAPL MSFT GOOGL FB TSLA NVDA"
        timeSeries = '1m 2m 5m 15m 30m 60m 90m 1h 1d 5d 1wk 1mo 3mo max'


        self.stockA = tk.StringVar()
        self.stockAChoice = ttk.Combobox(root, textvariable=self.stockA)
        self.stockAChoice['values'] = stocks
        self.stockAChoice['state'] = 'readonly'
        self.stockAChoice.current(0)
        self.stockAChoice.grid(row=1, column=0, sticky='news', padx=10, pady=10)
        self.stockA.trace_add('write', self.getCurrentStockA())


        self.stockB = tk.StringVar()
        self.stockB.set('Please choose a second stock')
        self.stockB.select = tk.OptionMenu(self, self.stockA, stocks2)

        self.timeDoubleBox = ttk.Combobox(root, textvariable=timeSeries)
        self.timeDoubleBox.set('Please choose a time series for both stocks')
        self.timeDoubleBox['values'] = timeSeries
        self.timeDoubleBox['state'] = 'readonly'



        self.title = tk.Label(text='Graph two stocks simultaneously', bg='blue')

        self.homepage = tk.Button(text='Click here to return to the homepage', command=master.destroy, bg='red')
        self.stock = tk.Label(text='Indicators', bg='lightblue')
        self.oneStock = tk.Label(text=f'Stock A is AAPL', bg='green')
        self.otherStock = tk.Label(text=f'Stock B is MSFT', bg='green')

        self.Mean1 = tk.Label(text=tf.getMean(stock1))
        self.Min1 = tk.Label(text=tf.getMin(stock1))
        self.Max1 = tk.Label(text=tf.getMax(stock1))
        self.Median1 = tk.Label(text=tf.getMedian(stock1))
        self.MarketCap1 = tk.Label(text=tf.marketCap(stock1))

        self.Mean2 = tk.Label(text=tf.getMean(stock2))
        self.Min2 = tk.Label(text=tf.getMin(stock2))
        self.Max2 = tk.Label(text=tf.getMax(stock2))
        self.Median2 = tk.Label(text=tf.getMedian(stock2))
        self.MarketCap2 = tk.Label(text=tf.marketCap(stock2))



        self.Ind1 = tk.Label(text='Mean', bg='lightblue')
        self.Ind2 = tk.Label(text='Min', bg='lightblue')
        self.Ind3 = tk.Label(text='Max', bg='lightblue')
        self.Ind4 = tk.Label(text='Median', bg='lightblue')
        self.Ind5 =  tk.Label(text='Market Cap (Trillions)', bg='lightblue')



        self.title.grid(row=0, column=0, columnspan=3, sticky='news')
        self.stockA.select.grid(row=1, column=0, sticky='news', padx=5, pady=5)
        self.stockB.select.grid(row=3, column=0, rowspan=1, sticky='news', padx=5, pady=5)
        self.timeDoubleBox.grid(row=1, column=1, rowspan=4, sticky='news', padx=5, pady=5)
        self.homepage.grid(row=12, column=0, columnspan=4, sticky='news')
        self.stock.grid(row=5, column=0, sticky='news')
        self.oneStock.grid(row=5, column=1, sticky='news')
        self.otherStock.grid(row=5, column=2, sticky='news')

        self.Mean1.grid(row=6, column=1, sticky='news')
        self.Min1.grid(row=7, column=1, sticky='news')
        self.Max1.grid(row=8, column=1, sticky='news')
        self.Median1.grid(row=9, column=1, sticky='news')
        self.MarketCap1.grid(row=10, column=1, sticky='news')

        self.Mean2.grid(row=6, column=2, sticky='news')
        self.Min2.grid(row=7, column=2, sticky='news')
        self.Max1.grid(row=8, column=2, sticky='news')
        self.Median2.grid(row=9, column=2, sticky='news')
        self.MarketCap2.grid(row=10, column=2, sticky='news')

        self.Ind1.grid(row=6, column=0, sticky='news', pady=10)
        self.Ind2.grid(row=7, column=0, sticky='news', pady=10)
        self.Ind3.grid(row=8, column=0, sticky='news', pady=10)
        self.Ind4.grid(row=9, column=0, sticky='news', pady=10)
        self.Ind5.grid(row=10, column=0, sticky='news', pady=10)


        #self.stockA.bind('<<ComboboxSelected>>', self.stockAChanged)
        #self.stockB.bind('<<ComboboxSelected>>', self.stockBChanged)
        self.timeDoubleBox.bind('<<ComboboxSelected>>', self.timeDoubleBoxChanged)

    def


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry("750x750")
    twoStock = twoStock(root)
    # oneStock.pack()
    root.mainloop()