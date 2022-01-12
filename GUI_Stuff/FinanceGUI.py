import tkinter as tk
from tkinter import Tk, Button
from GUI_Stuff import OneStockCode as OSC
from GUI_Stuff import TwoStockCode as TSC


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # container = tk.Frame(self)
        # container.grid(row=0, column=0, sticky='news')
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        self.frames = {'Main Menu': TitlePage(self),
                       'First Page': OneStock(self),
                       'Second Page': TwoStock(self)}
        # for F in (TitlePage, OneStock, TwoStock):
        #     # page_name = F.__name__
        #     frame = F(parent=container, controller=self)
        #     self.frames[page_name] = frame
        #     frame.grid(row=0, column=0, sticky='news')

        self.show_frame('Main Menu')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        # frame.grid(row=0, column=0, sticky='news')
        widgets = self.winfo_children()
        for w in widgets:
            if w.winfo_class() == 'Frame':
                w.pack_forget()
        frame.pack(expand=True, fill=tk.BOTH)
        #frame.tkraise(self)






class TitlePage(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)

        self.controller = controller
        self.title = tk.Label(self, text='Stock Grapher', font=('Arial', 14), bg='red')


        self.oneStock = tk.Button(self, text='Click here to graph one stock', bg='Blue',
                                  command=lambda: controller.show_frame("First Page"))

        self.twoStocks = tk.Button(self, text='Click here to graph two stocks', bg='Pink',
                                   command=lambda: controller.show_frame("TwoStock"))

        self.oneStock.grid(row=1, column=0, rowspan=5, sticky='s')
        self.title.grid(row=0, column=0, columnspan=3, sticky='news')
        self.twoStocks.grid(row=1, column=2, rowspan=5, sticky='s')



class OneStock(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller
        label = tk.Label(self, text="This is page 1")
        label.pack()
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame('Main Menu'))
        button.pack()


class TwoStock(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.controller = controller
        TwoStock = TSC


if __name__ == "__main__":
    app = App()
    app.mainloop()
