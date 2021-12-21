import tkinter as tk
from tkinter import Tk, Button
from GUI_Stuff import OneStockCode as OSC
from GUI_Stuff import TwoStockCode as TSC


class TitlePage(tk.Frame):
    def __init__(self, master, controller):
        super().__init__()

        self.title = tk.Label(text='Stock Grapher', font=('Arial', 14), bg='red')


        self.oneStock = tk.Button(text='Click here to graph one stock', bg='Blue')


        self.twoStocks = tk.Button(text='Click here to graph two stocks', bg='Pink', command=lambda : controller.show_frame(OneStock))

        self.oneStock.grid(row=1, column=0, rowspan=5, sticky='s')
        self.title.grid(row=0, column=0, columnspan=3, sticky='news')
        self.twoStocks.grid(row=1, column=2, rowspan=5, sticky='s')



    def setUp(self):
        pass



class OneStock:
    def __init__(self, master):
        oneStock = OSC
        print(oneStock)



class TwoStocks:
    def __init__(self, master):
        TwoStock = TSC
        print(TwoStock)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry("500x500")
    TitlePage = TitlePage(root)
    #TitlePage.pack()
    root.mainloop()