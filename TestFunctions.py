import yfinance as yf
import pandas as pd
import OneStockCode as OSC


def getMean(stock):
    ticker = yf.Ticker(stock)
    tickerHistory = ticker.history(period='max')

    sf = tickerHistory['Open']
    df = pd.DataFrame({'Date': sf.index, 'Open': sf.values})
    column = df['Open']
    meanUnr = column.mean()
    meanRou = meanUnr.round(2)
    return meanRou


def getMin(stock):
    ticker = yf.Ticker(stock)
    tickerHistory = ticker.history(period='max')

    sf = tickerHistory['Open']
    df = pd.DataFrame({'Date': sf.index, 'Open': sf.values})
    column = df['Open']
    minUnr = column.min()
    minRou = minUnr.round(2)
    return minRou

 
def getMax(stock):
    ticker = yf.Ticker(stock)
    tickerHistory = ticker.history(period='max')

    sf = tickerHistory['Open']
    df = pd.DataFrame({'Date': sf.index, 'Open': sf.values})
    column = df['Open']
    maxUnr = column.max()
    maxRou = maxUnr.round(2)
    return maxRou


def getMedian(stock):
    ticker = yf.Ticker(stock)
    tickerHistory = ticker.history(period='max')

    sf = tickerHistory['Open']
    df = pd.DataFrame({'Date': sf.index, 'Open': sf.values})
    column = df['Open']
    medUnr = column.median()
    medRou = medUnr.round(2)
    return medRou


def getMode(stock):
    ticker = yf.Ticker(stock)
    tickerHistory = ticker.history(period='max')

    sf = tickerHistory['Open']
    df = pd.DataFrame({'Date': sf.index, 'Open': sf.values})
    column = df['Open']
    modUnr = column.mode()
    modRou = modUnr.round(2)
    return modRou

