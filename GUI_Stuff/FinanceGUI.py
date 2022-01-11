import tkinter as tk
from tkinter import Tk, Button
from GUI_Stuff import OneStockCode as OSC
from GUI_Stuff import TwoStockCode as TSC


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky='news')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (TitlePage, OneStock, TwoStock):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='news')

        self.show_frame("TitlePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()






class TitlePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.title = tk.Label(text='Stock Grapher', font=('Arial', 14), bg='red')


        self.oneStock = tk.Button(text='Click here to graph one stock', bg='Blue',
                                  command=lambda: controller.show_frame("OneStock"))

        self.twoStocks = tk.Button(text='Click here to graph two stocks', bg='Pink',
                                   command=lambda: controller.show_frame("TwoStock"))

        self.oneStock.grid(row=1, column=0, rowspan=5, sticky='s')
        self.title.grid(row=0, column=0, columnspan=3, sticky='news')
        self.twoStocks.grid(row=1, column=2, rowspan=5, sticky='s')



class OneStock(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1")
        label.pack()
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("TitlePage"))
        button.pack()


class TwoStock(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        TwoStock = TSC


if __name__ == "__main__":
    app = App()
    app.mainloop()
