import os
import sys
import unittest
# Import local modules
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from app.models.stock import Stock
from app.utils.stock_service_helper import StockServiceHelper

class TestStockServiceHelper(unittest.TestCase):
    def setUp(self):
        self.stock_common = Stock("POP", "Common", 8, None, 100)
        self.stock_preferred = Stock("GIN", "Preferred", 8, 0.02, 100)

    def test_dividend_yield_common(self):
        self.assertAlmostEqual(StockServiceHelper.calculate_dividend_yield(self.stock_common, 100), 0.08)

    def test_dividend_yield_preferred(self):
        self.assertAlmostEqual(StockServiceHelper.calculate_dividend_yield(self.stock_preferred, 100), 0.02)

    def test_pe_ratio(self):
        self.assertAlmostEqual(StockServiceHelper.calculate_pe_ratio(self.stock_common, 100), 1250)

if __name__ == "__main__":
    unittest.main()
