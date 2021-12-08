from DataRepresentation import graphStockData as osInterface

class osTests(osInterface):
    def testChooseStock(self):
        flag = True
        while flag:
            print(self.stocks)
            self.stockInfo = input('Please choose a stock from list above')
            self.stockInfo = self.stockInfo.upper()
            if self.stockInfo in self.stocks:
                print('Input accepted')
                flag = False
            elif self.stockInfo not in self.stocks:
                print('Input Denied')

    def testChooseTimeSeries(self):
        flag = True
        while flag:
            print(self.time_series)
            self.time = input('Please choose a timeseries from the list above')
            if self.time in self.time_series:
                print('Input accepted')
                flag = False
            elif self.time not in self.time_series:
                print('Input denied')

    def testChooseColour(self):
        flag = True
        while flag:
            print(self.colour)
            self.colourChoice = input('Please choose a colour from the list above')
            self.colourChoice = self.colourChoice.lower()
            if self.colourChoice in self.colour:
                print('Input accepted')
                flag = False
            elif self.colourChoice not in self.colour:
                print('Input denied')

x = osTests()
print(x)