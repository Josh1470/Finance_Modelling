import tkinter as tk
from tkinter import Tk, Button
#from Data_Representation import graphStockData


class TitlePage(tk.Frame):
    def __init__(self, master):
        super().__init__()

        self.title = tk.Label(text='Stock Grapher', font=('Arial', 14), bg='red')


        self.oneStock = tk.Button(text='Click here to graph one stock', bg='Blue')


        self.twoStocks = tk.Button(text='Click here to graph two stocks', bg='Pink', command=master.destroy)

        self.oneStock.grid(row=1, column=0, rowspan=5, sticky='s')
        self.title.grid(row=0, column=0, columnspan=3, sticky='news')
        self.twoStocks.grid(row=1, column=2, rowspan=5, sticky='s')

        container = tk.Frame(self)
        self.frames = {}
        pages = (TitlePage, OneStock, TwoStocks)
        for F in pages:
            frame = F
            self.frames[F] = frame

        #self.showFrame(TitlePage)

    #def showFrame(self, current_frame):
            #for frame in self.frames.values():
                #frame.pack_forget()
            #self.frames[current_frame].pack(fill='red')
            #self.frames[current_frame].setUp()

    def setUp(self):
        pass



class OneStock:
    def __init__(self, master):
        super.__init__()

        self.title = tk.Label(text='Graphing One Stock', font=('Arial', 14), bg='red')

        self.title.grid(row=1, column=0, sticky='news')



class TwoStocks:
    pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    # root.geometry("500x500")
    TitlePage = TitlePage(root)
    #TitlePage.pack()
    root.mainloop()