""" GBCEStocksController class is used to handle the stocks operations """
import os
import sys

# Import local modules
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from app.utils.stock_service_helper import StockServiceHelper
from app.utils.market_service_helper import MarketServiceHelper
from models.stock import Stock

class GBCEStocksController:
    """ GBCEStocksController class is used to handle the stocks operations """
    def __init__(self):
        """ Initalize the values """
        # Initalize the market service helper class
        self.market_service = MarketServiceHelper()

    def add_stock(self, symbol, stock_type, last_dividend, fixed_dividend, par_value):
        """
        Add the stock to the market

        Args:
            symbol : Stock symbol
            stock_type : Type of stock
            last_dividend : Last dividend
            fixed_dividend : Fixed dividend
            par_value : Par value
        """
        stock_obj = Stock(symbol, stock_type, last_dividend, fixed_dividend, par_value)
        self.market_service.add_stock(stock_obj)

    def record_trade(self, symbol, quantity, buy_sell, price):
        """ 
        Record the trade for the stock

        Args:
            symbol : Stock symbol
            quantity : Quantity of stock
            buy_sell : Buy or Sell
            price : Price of stock
        """
        stock_obj = self.market_service.stocks.get(symbol)
        if stock_obj:
            stock_obj.record_trade(quantity, buy_sell, price)

    def get_dividend_yield(self, symbol, market_price):
        """        
        Get the dividend yield for the stock

        Args:
            symbol : Stock symbol
            market_price : Market price
        """
        stock_obj = self.market_service.stocks.get(symbol)
        return StockServiceHelper.calculate_dividend_yield(stock_obj, market_price) if stock_obj else None

    def get_pe_ratio(self, symbol, market_price):
        """
        Get the P/E ratio for the stock
        
        Args:
            symbol : Stock symbol
            market_price : Market price
        """
        stock_obj = self.market_service.stocks.get(symbol)
        return StockServiceHelper.calculate_pe_ratio(stock_obj, market_price) if stock_obj else None

    def get_volume_weighted_stock_price(self, symbol):
        """
        Get the volume weighted stock price for the stock
        
        Args:
            symbol : Stock symbol
        """
        stock_obj = self.market_service.stocks.get(symbol)
        return StockServiceHelper.calculate_volume_weighted_stock_price(stock_obj) if stock_obj else None

    def get_gbce_all_share_index(self):
        """ Get the GBCE All Share Index """
        return self.market_service.calculate_gbce_all_share_index()
 