""" Stock model class """
from collections import deque
import time

class Stock:
    """ Stock model class """
    def __init__(self, symbol, stock_type, last_dividend, fixed_dividend, par_value):
        """ Initalize the values """
        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.trades = deque()

    def record_trade(self, quantity, buy_sell, price):
        """ 
        Record the trade for the stock 
        
        Args:
            quantity : Quantity of stock
            buy_sell : Buy or Sell
            price : Price of stock
        """
        self.trades.append((time.time(), quantity, buy_sell, price))
