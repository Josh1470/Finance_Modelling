import tkinter as tk
from tkinter import Tk, Button
from GUI_Stuff import OneStockCode as OSC
from GUI_Stuff import TwoStockCode as TSC
from GUI_Stuff import MainMenu as MM
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Tests import TestFunctions as tf


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # container = tk.Frame(self)
        # container.grid(row=0, column=0, sticky='news')
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        #self.show_frame('Main Menu')

        self.frames = {'Main Menu': TitlePage(self),
                       'First Page': oneStock(self),
                       'Second Page': TwoStock(self),
                       'Help Page': helpPage(self)}

        self.show_frame('Main Menu')
        # for F in self.frames:
        #     page_name = F.__name__
        #     frame = F(controller=self)
        #     self.frames[page_name] = frame
        #     frame.grid(row=0, column=0, sticky='news')



    def show_frame(self, page_name, *args, **kwargs):
        frame = self.frames[page_name]
        frame.grid(row=0, column=0, sticky='news')
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.grid_forget()
        frame.grid(row=0, column=0, rowspan=1000, columnspan=1000)
        #frame.tkraise(self.show_frame(page_name))





class TitlePage(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        #OSC.oneStock(controller)
        print('Testing if this frame can be seen')
        self.controller = controller
        self.title = tk.Label(self, text='Stock Grapher', font=('Arial', 14), bg='red')

        self.oneStock = tk.Button(self, text='Click here to graph one stock', bg='Blue',
                                  command=lambda: controller.show_frame("First Page"))
        self.twoStocks = tk.Button(self, text='Click here to graph two stocks', bg='Pink',
                                   command=lambda: controller.show_frame("Second Page"))
        self.oneStock.grid(row=1, column=0, rowspan=1000, sticky='s')
        self.title.grid(row=0, column=0, columnspan=1000, sticky='news')
        self.twoStocks.grid(row=1, column=2, rowspan=1000, sticky='s')
        self.columnconfigure(0, weight=10000)
        self.rowconfigure(0, weight=10000)







class oneStock(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        OSC.oneStock(controller)
        #self.controller = controller
        #self.title = tk.Label(self, text='Stock Grapher', font=('Arial', 14), bg='Blue')

        #self.oneStock = tk.Button(self, text='Click here to graph one stock', bg='Red',
                                  #command=lambda: controller.show_frame("First Page"))
        #self.twoStocks = tk.Button(self, text='Click here to graph two stocks', bg='Green',
                                   #command=lambda: controller.show_frame("Second Page"))
        #self.oneStock.grid(row=1, column=0, rowspan=1000, sticky='s')
        #self.title.grid(row=0, column=0, columnspan=1000, sticky='news')
        #self.twoStocks.grid(row=1, column=2, rowspan=1000, sticky='s')


        #print(OSC.oneStock(tk.Frame))

class TwoStock(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        TSC.twoStock(controller)
        #self.controller = controller
        #self.title = tk.Label(self, text='Stock Grapher', font=('Arial', 14), bg='Pink')

        #self.oneStock = tk.Button(self, text='Click here to graph one stock', bg='Orange',
                                #  command=lambda: controller.show_frame("First Page"))
        #self.twoStocks = tk.Button(self, text='Click here to graph two stocks', bg='Blue',
         #                          command=lambda: controller.show_frame("Second Page"))
        #self.Help = tk.Button(self, text='Click here for some help', bg='Brown',
         #                     command=lambda: controller.show_frame("Help Page"))
        #self.oneStock.grid(row=1, column=0, rowspan=1000, sticky='s')
        #self.title.grid(row=0, column=0, columnspan=1000, sticky='news')
        #self.twoStocks.grid(row=1, column=2, rowspan=1000, sticky='s')
        #self.Help.grid(row=2, column=3, columnspan=1000, sticky='news')

class helpPage(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)





if __name__ == "__main__":
    app = App()
    app.geometry("750x750")
    app.mainloop()
