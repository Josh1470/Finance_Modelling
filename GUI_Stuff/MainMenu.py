import tkinter as tk

class TitlePage(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title = tk.Label(self, text='Stock Grapher', font=('Arial', 14), bg='red')

        self.oneStock = tk.Button(self, text='Click here to graph one stock', bg='Blue',
                                      command=lambda: controller.show_frame("First Page"))

        self.twoStocks = tk.Button(self, text='Click here to graph two stocks', bg='Pink',
                                       command=lambda: controller.show_frame("Second Page"))

        self.helpPage = tk.Button(self, text='Click here to go to the help page', bg='Orange',
                                        command=lambda: controller.show_frame("Help Page"))

        self.oneStock.grid(row=1, column=0,  sticky='news')
        self.title.grid(row=0, column=0, columnspan=3, sticky='news')
        self.twoStocks.grid(row=1, column=2, sticky='news')
        self.helpPage.grid(row=2, column=0, columnspan=4, sticky='news')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry("750x750")
    TitlePage = TitlePage(root)
    TitlePage.pack()
    root.mainloop()



