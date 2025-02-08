""" The GBCERunStocks class is used to run the stock market without database, 
GUI or I/O operations. The value will be held in memory """
import os
import sys

# Import local modules
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from app.controllers.gbce_stocks_controller import GBCEStocksController

class GBCERunStocks:
    """ 
    The GBCERunStocks class is used to run the stock market without database, 
    GUI or I/O operations. The value will be held in memory.
    """
    def __init__(self, stocks_data=None):
        """
        Initalize the values

        Args:
            stocks_data : List of stocks with the information
        """
        self.stocks_data = stocks_data

        # Initalize the stocks controller
        self.gbce_stocks_controller_obj = GBCEStocksController()         
        
    def run_stocks(self):
        """  Run the stocks with the given data and fetch the metrics """
        for data in self.stocks_data:
            self.gbce_stocks_controller_obj.add_stock(*data)

        # Recording Trades
        self.gbce_stocks_controller_obj.record_trade("POP", 100, "buy", 120)
        self.gbce_stocks_controller_obj.record_trade("POP", 50, "sell", 130)
        self.gbce_stocks_controller_obj.record_trade("POP", 150, "buy", 130)

        # Fetching Metrics
        print("Dividend Yield:", self.gbce_stocks_controller_obj.get_dividend_yield("POP", 120))
        print("P/E Ratio:", self.gbce_stocks_controller_obj.get_pe_ratio("POP", 120))
        print("Volume Weighted Stock Price:", self.gbce_stocks_controller_obj.get_volume_weighted_stock_price("POP"))
        print("GBCE All Share Index:", self.gbce_stocks_controller_obj.get_gbce_all_share_index())

if __name__ == "__main__":
    # Initalizing Stocks
    stocks_data = [
        ("TEA", "Common", 0, None, 100),
        ("POP", "Common", 8, None, 100),
        ("ALE", "Common", 23, None, 60),
        ("GIN", "Preferred", 8, 0.02, 100),
        ("JOE", "Common", 13, None, 250)
    ]
    gbce_run_stocks_obj = GBCERunStocks(stocks_data)
    gbce_run_stocks_obj.run_stocks()

    

    

    