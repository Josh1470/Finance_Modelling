import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from yahoofinancials import YahooFinancials as yF
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import statistics
from GUI_Stuff import TwoStockCode as TSC




def getDataFrame(stock, timeseries):
    ticker = yf.Ticker(stock)
    tickerHistory = ticker.history(period=timeseries)
    sf = tickerHistory['Open']
    df = pd.DataFrame({'Date': sf.index, 'Open': sf.values})
    return df


def getStockDataFrame(stock, timeseries):
    ticker = yf.Ticker(stock)
    tickerHistory = ticker.history(period=timeseries)
    sf = tickerHistory['Open']
    df = pd.DataFrame({'Date': sf.index, 'Open': sf.values})
    return df


# def getStockA(*args):
#     stock = TSC.twoStock.getCurrentStockA()
#     return stock
#
# def getStockB(*args):
#     stock = TSC.twoStock.getCurrentStockB()
#     return stock
#
#
# def getTimeSeries(*args):
#     timeseries = TSC.twoStock.getCurrentTimeSeries()
#     return timeseries
#
#
# x = getDataFrame(getStockA(), getTimeSeries())
# y = getDataFrame(getStockB(), getTimeSeries())
#
# stock = [x, y]

def getMean(df):
    column = df['Open']
    meanUnr = column.mean()
    meanRou = round(meanUnr, 2)
    return meanRou




def getMin(df):
    column = df['Open']
    minUnr = column.min()
    minRou = round(minUnr, 2)
    return minRou




def getMax(df):
    column = df['Open']
    maxUnr = column.max()
    maxRou = round(maxUnr, 2)
    return maxRou



def getMedian(df):
    column = df['Open']
    medUnr = column.median()
    medRou = round(medUnr, 2)
    return medRou


def getRange(df):
    column = df['Open']
    Max = column.max()
    Min = column.min()
    ranUnr = Max - Min
    ranRou = round(ranUnr, 2)
    return ranRou


def perChange(df):
    column = df['Open']
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


