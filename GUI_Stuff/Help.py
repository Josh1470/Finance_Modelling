import tkinter as tk
import matplotlib.pyplot as plt

class Help(tk.Frame):
    def __init__(self, controller):
        super().__init__()

        self.title = tk.Label(bg='Pink', text="FAQ's")

        self.FAQ1 = tk.Label(bg='lightblue', text='Would I be able to invest directly through this interface?')
        self.FAQ2 = tk.Label(bg='lightblue', text='How regularly does stock information update?')
        self.FAQ3 = tk.Label(bg='lightblue', text='Is the GUI at all customisable?')
        self.FAQ4 = tk.Label(bg='lightblue', text='Would the system be accessible through the internet or is it a '
                                          'downloadable software')
        self.FAQ5 = tk.Label(bg='lightblue', text='Is there a way to filter stocks shown on the graph')

        self.answer1 = tk.Label(text='No, currently you are unable to invest directly through this '
                                                'interface,however with more time this is '
                                      'something we would love to implement')
        self.answer2 = tk.Label(text='The dashboard gets all its information from the Yahoo Finance API, and it will update as regularly'
                                     ' as the user refreshes the dashboard')
        self.answer3 = tk.Label(text='The GUI is customisable as far as the user is able to change the stock shown and '
                                     'the time series shown on both the OneStock and TwoStock Frames. \n'
                                     'The user can also compare two stocks of their choice in the TwoStock Frame, and the user can '
                                     'choose if they want the moving averages on this graph as well')
        self.answer4 = tk.Label(text='The system is not accessbile through the internet but it is a downloadable software.\n'
                                     'The software can be accessed for free through GitHub and this means the code can'
                                     'can be changed in any way the user wants')
        self.answer5 = tk.Label(text='There is a way to filter the stocks shown on the graph as the user can choose the stock,'
                                     ' they would like to display through the combo boxes. However, the user will need to \n refresh the frame each time a new stock is chosen. '
                                     'This is so the code can output the indicators for the chosen stock ')

        self.title.grid(row=0, column=0, columnspan=100, sticky='news')

        self.FAQ1.grid(row=1, column=1, padx=5, pady=5)
        self.answer1.grid(row=2, column=1)

        self.FAQ2.grid(row=3, column=1, padx=5, pady=5)
        self.answer2.grid(row=4, column=1)

        self.FAQ3.grid(row=5, column=1, padx=5, pady=5)
        self.answer3.grid(row=6, column=1)

        self.FAQ4.grid(row=7, column=1, padx=5, pady=5)
        self.answer4.grid(row=8, column=1)

        self.FAQ5.grid(row=9, column=1, padx=5, pady=5)
        self.answer5.grid(row=10, column=1)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry('750x750')
    Help = Help(root)
    # oneStock.pack()
    root.mainloop()
