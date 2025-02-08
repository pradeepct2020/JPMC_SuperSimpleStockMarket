""" This module contains the MarketServiceHelper class which is responsible for calculating the GBCE All Share Index. """
import math
from app.utils.stock_service_helper import StockServiceHelper

class MarketServiceHelper:
    """ This class is responsible for calculating the GBCE All Share Index. """
    def __init__(self):
        """ Initalize the values """
        self.stocks = {}

    def add_stock(self, stock):
        """ 
        Add the stock to the market 
        
        Args:
            stock : Stock object
        """
        self.stocks[stock.symbol] = stock

    def calculate_gbce_all_share_index(self):
        """ Calculate the GBCE All Share Index """
        prices = [StockServiceHelper.calculate_volume_weighted_stock_price(stock) for stock in self.stocks.values() if StockServiceHelper.calculate_volume_weighted_stock_price(stock) is not None]
        if not prices:
            return None
        return math.exp(sum(math.log(price) for price in prices) / len(prices))
