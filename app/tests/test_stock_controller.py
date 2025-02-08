import os
import sys
import unittest
# Import local modules
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from app.controllers.gbce_stocks_controller import GBCEStocksController

class TestGBCEStocksController(unittest.TestCase):
    def setUp(self):
        self.controller = GBCEStocksController()
        self.controller.add_stock("POP", "Common", 8, None, 100)

    def test_add_stock(self):
        self.assertIn("POP", self.controller.market_service.stocks)

    def test_record_trade(self):
        self.controller.record_trade("POP", 100, "buy", 120)
        self.assertEqual(len(self.controller.market_service.stocks["POP"].trades), 1)

    def test_get_dividend_yield(self):
        self.assertAlmostEqual(self.controller.get_dividend_yield("POP", 120), 0.0667, places=3)

    def test_get_pe_ratio(self):
        self.assertAlmostEqual(self.controller.get_pe_ratio("POP", 120), 1800)

if __name__ == "__main__":
    unittest.main()
