import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Tests import TestFunctions as tf


class twoStock(tk.Frame):
    def __init__(self, master):
        super().__init__()


        stocks = "AMZN AAPL MSFT GOOGL FB TSLA NVDA"
        timeSeries = '1m 2m 5m 15m 30m 60m 90m 1h 1d 5d 1wk 1mo 3mo max'


        self.stockA = tk.StringVar()
        self.stockAChoice = ttk.Combobox(root, textvariable=self.stockA)
        self.stockAChoice['values'] = stocks
        self.stockAChoice['state'] = 'readonly'
        self.stockAChoice.current(0)
        self.stockAChoice.grid(row=1, column=0, sticky='news', padx=5, pady=5)
        self.stockA.trace_add('write', self.getCurrentStockA())


        self.stockB = tk.StringVar()
        self.stockBChoice = ttk.Combobox(root, textvariable=self.stockB)
        self.stockBChoice['values'] = stocks
        self.stockBChoice['state'] = 'readonly'
        self.stockBChoice.current(0)
        self.stockBChoice.grid(row=3, column=0, rowspan=1, sticky='news', padx=5, pady=5)
        self.stockB.trace_add('write', self.getCurrentStockB())


        self.timeBox = tk.StringVar()
        self.timeBoxChoice = ttk.Combobox(root, textvariable=self.timeBox)
        self.timeBoxChoice['values'] = timeSeries
        self.timeBoxChoice['state'] = 'readonly'
        self.timeBoxChoice.current(0)
        self.timeBoxChoice.grid(row=1, column=1, rowspan=4, sticky='news', padx=5, pady=5)
        self.timeBox.trace_add('write', self.getCurrentTimeSeries())


        self.title = tk.Label(text='Graph two stocks simultaneously', bg='blue')

        self.homepage = tk.Button(text='Click here to return to the homepage', command=master.destroy, bg='red')
        self.stock = tk.Label(text='Indicators', bg='lightblue')
        self.oneStock = tk.Label(text=f'Stock A is {self.getCurrentStockA()}', bg='green')
        self.otherStock = tk.Label(text=f'Stock B is {self.getCurrentStockB()}', bg='green')

        self.Mean1 = tk.Label(text=tf.getMean(self.getCurrentStockA(), self.getCurrentTimeSeries()))
        self.Min1 = tk.Label(text=tf.getMin(self.getCurrentStockA(), self.getCurrentTimeSeries()))
        self.Max1 = tk.Label(text=tf.getMax(self.getCurrentStockA(), self.getCurrentTimeSeries()))
        self.Median1 = tk.Label(text=tf.getMedian(self.getCurrentStockA(), self.getCurrentTimeSeries()))
        self.MarketCap1 = tk.Label(text=tf.marketCap(self.getCurrentStockA()))

        self.Mean2 = tk.Label(text=tf.getMean(self.getCurrentStockB(), self.getCurrentTimeSeries()))
        self.Min2 = tk.Label(text=tf.getMin(self.getCurrentStockB(), self.getCurrentTimeSeries()))
        self.Max2 = tk.Label(text=tf.getMax(self.getCurrentStockB(), self.getCurrentTimeSeries()))
        self.Median2 = tk.Label(text=tf.getMedian(self.getCurrentStockB(), self.getCurrentTimeSeries()))
        self.MarketCap2 = tk.Label(text=tf.marketCap(self.getCurrentStockB()))



        self.Ind1 = tk.Label(text='Mean', bg='lightblue')
        self.Ind2 = tk.Label(text='Min', bg='lightblue')
        self.Ind3 = tk.Label(text='Max', bg='lightblue')
        self.Ind4 = tk.Label(text='Median', bg='lightblue')
        self.Ind5 =  tk.Label(text='Market Cap (T)', bg='lightblue')



        self.title.grid(row=0, column=0, columnspan=3, sticky='news')



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


    def getCurrentStockA(self):
        self.normal = root.state()
        if twoStock is not self.normal:
            return 'AAPL'
        elif twoStock is self.normal:
            currentStockA = self.stockA.get()
            return currentStockA

    def getCurrentStockB(self):
        self.normal = root.state()
        if twoStock is not self.normal:
            return 'AMZN'
        elif twoStock is self.normal:
            currentStockB = self.stockB.get()
            return currentStockB

    def getCurrentTimeSeries(self):
        self.normal = root.state()
        if twoStock is not self.normal:
            return '1mo'
        elif twoStock is self.normal:
            currentTimeSeries = self.timeBox.get()
            return currentTimeSeries


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry("750x750")
    twoStock = twoStock(root)
    # oneStock.pack()
    root.mainloop()