import unittest
from Tests import TestFunctions as tF
import yfinance as yf
import datetime as dt
import pandas as pd


class graphTesting(unittest.TestCase):
    def testMean(self):
        self.assertEqual(tF.getMean("AAPL", 'max', df=tF.getDataFrame('AAPL','max')), 13.22)

    def testMax(self):
        self.assertEqual(tF.getMax("AAPL", 'max', df=tF.getDataFrame('AAPL', 'max')), 182.4)

    def testMin(self):
        self.assertEqual(tF.getMin("AAPL", 'max', df=tF.getDataFrame('AAPL','max')), 0.04)

    def testMedian(self):
        self.assertEqual(tF.getMedian("AAPL",'max', df=tF.getDataFrame('AAPL', 'max')), 0.39)

    def testPerChange(self):
        self.assertEqual(tF.perChange("AAPL", 'max', df=tF.getDataFrame('AAPL', 'max')), 158414)

    def testPeRatio(self):
        self.assertEqual(tF.peRatio("AAPL"), 25.72)

    def testMarketCap(self):
        self.assertEqual(tF.marketCap("AAPL"), 2.53)





if __name__ == '__main__':
    unittest.main()
