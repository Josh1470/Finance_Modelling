import unittest
import TestFunctions as tF


class graphTesting(unittest.TestCase):
    def testMean(self):
        self.assertEqual(tF.getMean("AAPL"), 11.67)

    def testMax(self):
        self.assertEqual(tF.getMax("AAPL"), 156.98)

    def testMin(self):
        self.assertEqual(tF.getMin("AAPL"), 0.04)

    def testMedian(self):
        self.assertEqual(tF.getMedian("AAPL"), 0.38)


if __name__ == '__main__':
    unittest.main()
