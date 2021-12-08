import unittest
from Tests import TestFunctions as tF


class graphTesting(unittest.TestCase):
    def testMean(self):
        self.assertEqual(tF.getMean("AAPL"), 12.17)

    def testMax(self):
        self.assertEqual(tF.getMax("AAPL"), 156.98)

    def testMin(self):
        self.assertEqual(tF.getMin("AAPL"), 0.04)

    def testMedian(self):
        self.assertEqual(tF.getMedian("AAPL"), 0.38)

    def testPerChange(self):
        self.assertEqual(tF.perChange("AAPL"), 141421.4)

    def testPeRatio(self):
        self.assertEqual(tF.peRatio("AAPL"), 27.96)

    def testMarketCap(self):
        self.assertEqual(tF.marketCap("AAPL"), 2.36)





if __name__ == '__main__':
    unittest.main()
