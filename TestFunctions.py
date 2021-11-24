import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from yahoofinancials import YahooFinancials as yF
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import statistics


def getDataFrame(stock):
    ticker = yf.Ticker(stock)
    tickerHistory = ticker.history(period='3mo')
    sf = tickerHistory['Open']
    df = pd.DataFrame({'Date': sf.index, 'Open': sf.values})
    return df['Open']


def getMean(stock):
    column = getDataFrame(stock)
    meanUnr = column.mean()
    meanRou = round(meanUnr, 2)
    return meanRou


def getMin(stock):
    column = getDataFrame(stock)
    minUnr = column.min()
    minRou = round(minUnr, 2)
    return minRou

 
def getMax(stock):
    column = getDataFrame(stock)
    maxUnr = column.max()
    maxRou = round(maxUnr, 2)
    return maxRou


def getMedian(stock):
    column = getDataFrame(stock)
    medUnr = column.median()
    medRou = round(medUnr, 2)
    return medRou


def getRange(stock):
    column = getDataFrame(stock)
    Max = column.max()
    Min = column.min()
    ranUnr = Max - Min
    ranRou = round(ranUnr, 2)
    return ranRou

def graphStock(stock):
    ticker = yf.Ticker(stock)
    ticker_history = ticker.history(period='max')
    plt.plot(getDataFrame(stock))
    ax = plt.gca
    return plt.gcf().canvas.draw()






def perChange(stock):
    column = getDataFrame(stock)
    First = column.iloc[0]
    Last = column.iloc[-1]
    changeUnr = (Last / First) * 100
    changeRou = changeUnr.round(2)
    return changeRou

def peRatio(stock):
    yahooFinance = yF(stock)
    quoteTable = yF.get_pe_ratio(yahooFinance)
    ratioRou = round(quoteTable, 2)
    return ratioRou

def marketCap(stock):
    yahooFinance = yF(stock)
    mc = yF.get_market_cap(yahooFinance)
    mcRou = round(mc / 1000000000000, 2)
    return mcRou

def getYearlyHigh(stock):
    yahooFinance = yF(stock)
    yH = yF.get_yearly_high(yahooFinance)
    yHRou = round(yH, 2)
    return yHRou

def getYearlyLow(stock):
    yahooFinance = yF(stock)
    yL = yF.get_yearly_low(yahooFinance)
    yLRou = round(yL, 2)
    return yLRou

def getCurrentStock(stock):
    return stock


