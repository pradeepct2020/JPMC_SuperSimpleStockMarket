import os
import sys
import unittest
import time
# Import local modules
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from app.models.stock import Stock
from app.utils.market_service_helper import MarketServiceHelper
from app.utils.stock_service_helper import StockServiceHelper

class TestMarketServiceHelper(unittest.TestCase):
    def setUp(self):
        self.market = MarketServiceHelper()
        self.stock1 = Stock("POP", "Common", 8, None, 100)
        self.stock2 = Stock("ALE", "Common", 23, None, 60)
        self.market.add_stock(self.stock1)
        self.market.add_stock(self.stock2)

    def test_calculate_gbce_all_share_index(self):
        self.stock1.record_trade(100, "buy", 120)
        self.stock2.record_trade(50, "sell", 130)
        price1 = StockServiceHelper.calculate_volume_weighted_stock_price(self.stock1)
        price2 = StockServiceHelper.calculate_volume_weighted_stock_price(self.stock2)
        expected_index = (price1 * price2) ** 0.5  # Geometric mean
        self.assertAlmostEqual(self.market.calculate_gbce_all_share_index(), expected_index)

if __name__ == "__main__":
    unittest.main()
