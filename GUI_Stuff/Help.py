import tkinter as tk
import matplotlib.pyplot as plt

class Help(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.title = tk.Label(bg='Pink', text="FAQ's")

        self.title.grid(row=0, column=0, columnspan=100, sticky='news')

        questions = ['Would I be able to invest directly through this interface?',
                     'How regularly does stock information update?',
                     'Is the GUI at all customisable?',
                     'Would the system be accessible through the internet or is it a downloadable software',
                     'Is there a way to filter stocks shown on the graph',
                     'What does the Range indicator mean?',
                     'What is a companies Price/Earnings ratio mean?',
                     'What does the market cap indicator indicate?'
                     ]
        answers = ['No, currently you are unable to invest directly through this interface,however with more time this is '
                   'something we would love to implement',
                   'The dashboard gets all its information from the Yahoo Finance API, and it will update as regularly '
                   'as the user refreshes the dashboard',
                   'The GUI is customisable as far as the user is able to change the stock shown and the time series shown on both the OneStock and TwoStock Frames. \n '
                   'The user can also compare two stocks of their choice in the TwoStock Frame, \n '
                   'and the user can choose if they want the moving averages on this graph as well',
                   'The system is not accessbile through the internet but it is a downloadable software. \n'
                   'The software can be accessed for free through GitHub and this means the code can be changed in any way the user wants',
                   'There is a way to filter the stocks shown on the graph as the user can choose the stock, they would like to display through the combo boxes. '
                   'However, \n the user will need to refresh the frame each time a new stock is chosen. '
                   'This is so the code can output the indicators for the chosen stock',
                   'Numerical difference between the stock price on the first day of the time frame selected and \n'
                   'the stock price on the final day of the time frame selected',
                   'It is the stock price divided by the earnings per share of the company. A high P/E ratio tends to suggest a company is overvalued \n'
                   'Whereas a low P/E ratio suggests a company is undervalued',
                   'This is the total value of all the company’s shares of stock.']
        QuestionRow = [1, 3, 5, 7, 9, 11, 13, 15, 17]
        AnswerRow = [2, 4, 6, 8, 10, 12, 14, 16, 18]

        for i in range(len(questions)):
            Question = tk.Label(bg='lightblue', text=questions[i])
            Question.grid(row=QuestionRow[i], column=1, padx=5, pady=5)

        for i in range(len(answers)):
            Answer = tk.Label(text=answers[i])
            Answer.grid(row=AnswerRow[i], column=1)

        self.mainMenu = tk.Button(bg='red', text='Click to return to Main Menu')
        self.oneStock = tk.Button(bg='orange', text='Click to go to the OneStock page')
        self.twoStock = tk.Button(bg='yellow', text='Click to go to the TwoStock page')

        self.mainMenu.grid(row=110, column=1, sticky='news')
        self.oneStock.grid(row=120, column=1, sticky='news')
        self.twoStock.grid(row=130, column=1, sticky='news')


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stock Grapher")
    root.geometry('900x900')
    Help = Help(root)
    # oneStock.pack()
    root.mainloop()


# questions = ['Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5']
# answers = ['Answer 1, Answer 2, Answer 3, Answer 4, Answer 4, Answer 5']
# QuestionRow = [1, 3, 5, 7, 9]
# AnswerRow= [2, 4, 6, 8, 10]
#
# for i in range(len(questions)):
#     Question = tk.Label(bg='lightblue', text=questions[i])
#     Question.grid(row=QuestionRow[i], column=1)
#
# for i in range(len(answers)):
#     Answer = tk.Label(text=answers[i])
#     Answer.grid(row=AnswerRow[i], column=2)
#
