""" This module contains the StockServiceHelper class which provides helper methods for the StockService class. """
import math
import time

class StockServiceHelper:
    """ This class provides helper methods for the StockService class. """
    @staticmethod
    def calculate_dividend_yield(stock, market_price):
        """
        Calculate the dividend yield for the stock
        
        Args:
            stock : Stock object
            market_price : Market price
        """
        if market_price <= 0:
            return None
        if stock.stock_type == "Common":
            return stock.last_dividend / market_price
        elif stock.stock_type == "Preferred":
            return (stock.fixed_dividend * stock.par_value) / market_price

    @staticmethod
    def calculate_pe_ratio(stock, market_price):
        """
        Calculate the P/E ratio for the stock
        
        Args:
            stock : Stock object
            market_price : Market price
        """
        dividend = StockServiceHelper.calculate_dividend_yield(stock, market_price)
        if dividend and dividend > 0:
            return market_price / dividend
        return None

    @staticmethod
    def calculate_volume_weighted_stock_price(stock):
        """ 
        Calculate the volume weighted stock price for the stock
        
        Args:
            stock : Stock object
        """
        current_time = time.time()
        valid_trades = [trade for trade in stock.trades if current_time - trade[0] <= 300]
        total_price_quantity = sum(trade[1] * trade[3] for trade in valid_trades)
        total_quantity = sum(trade[1] for trade in valid_trades)
        return total_price_quantity / total_quantity if total_quantity > 0 else None
