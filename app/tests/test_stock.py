import os
import sys
import unittest
import time
# Import local modules
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from app.models.stock import Stock

class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = Stock("POP", "Common", 8, None, 100)

    def test_record_trade(self):
        self.stock.record_trade(100, "buy", 120)
        self.assertEqual(len(self.stock.trades), 1)
        self.assertEqual(self.stock.trades[0][1], 100)  # Quantity
        self.assertEqual(self.stock.trades[0][3], 120)  # Price

if __name__ == "__main__":
    unittest.main()
