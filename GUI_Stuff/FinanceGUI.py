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
                       'Second Page': TwoStock(self)}

        self.show_frame('Main Menu')
        for F in self.frames:
            page_name = F.__name__
            frame = F(controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='news')



    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.grid(row=0, column=0, sticky='news')
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.grid_forget()
        frame.grid(row=0, column=0)
        #frame.tkraise(self.show_frame(page_name))






class TitlePage(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        print('Testing if this frame can be seen')
        print(MM.TitlePage(tk.Frame))







class oneStock(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)

        print(OSC.oneStock(tk.Frame))

class TwoStock(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)

        print(TSC.twoStock(tk.Frame))

if __name__ == "__main__":
    app = App()
    app.geometry("750x750")
    app.mainloop()
