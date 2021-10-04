import tkinter as tk
from tkinter import ttk

class oneStock(tk.Frame):
    def __init__(self):
        super().__init__()

        self.title = tk.Label(text='Graph One Stock', bg='Brown')

        self.boxTitle = ttk.Label(text='Please Select A Stock')
        stocks = 'AMZN AAPL MSFT GOOGL FB TSLA NVDA'
        self.box = ttk.Combobox(root, textvariable=stocks, text='Please Choose A Stock')
        self.box['values'] = stocks
        self.box['state'] = 'readonly'

        self.statistics = tk.Label(bg='blue')


        self.title.grid(row=0, column=0, columnspan=3, sticky='news')
        self.box.grid(row=1, column=0)
        self.statistics.grid(row=2, column=0, rowspan=7, sticky='news')





if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry("500x500")
    oneStock = oneStock()
    #oneStock.pack()
    root.mainloop()