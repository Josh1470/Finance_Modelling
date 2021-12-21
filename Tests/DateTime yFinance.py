import yfinance as yf
import pandas as pd
import math

start = '2019-01-01'
end = '2020-01-01'
ticker = 'AAPL'

df = pd.DataFrame(ticker, 'yahoo', start, end)
print(df)