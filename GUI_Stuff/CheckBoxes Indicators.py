import tkinter as tk

class checkIndicators(tk.Frame):
    def __init__(self, master):
        super().__init__()

        self.mean = tk.Checkbutton(text='Tick for mean to be shown as an indicator', onvalue=1, offvalue=0)
        self.median = tk.Checkbutton(text='Tick for median to be shown as an indicator', onvalue=1, offvalue=0)
        self.mode = tk.Checkbutton(text='Tick for mode to be shown as an indicator', onvalue=1, offvalue=0)
        self.max = tk.Checkbutton(text='Tick for max to be shown as an indicator', onvalue=1, offvalue=0)
        self.min = tk.Checkbutton(text='Tick for min to be shown as an indicator', onvalue=1, offvalue=0)
        self.pE = tk.Checkbutton(text='Tick for Price Earnings ratio to be shown as an indicator', onvalue=1, offvalue=0)


        self.mean.grid(row=0, column=0, padx=5, pady=5)
        self.median.grid(row=1, column=0, padx=5, pady=5)
        self.mode.grid(row=0, column=1, padx=5, pady=5)
        self.max.grid(row=1, column=1, padx=5, pady=5)
        self.min.grid(row=0, column=2, padx=5, pady=5)
        self.pE.grid(row=1, column=2, padx=5, pady=5)









if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry("1000x500")
    checkIndicators = checkIndicators(root)
    #checkIndicators.pack()
    root.mainloop()
