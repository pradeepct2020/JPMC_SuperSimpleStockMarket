# JPMC_SuperSimpleStockMarket
Assignment – Super Simple Stock Market

Overview
--------
The Super Simple Stock Market is a Python-based application that models a basic stock exchange system for the Global Beverage Corporation Exchange (GBCE). It calculates key financial metrics and processes stock trades.

Features
--------
  1. Calculate Dividend Yield for common and preferred stocks.
  2. Compute the P/E Ratio based on stock price.
  3. Record and store trades in memory.
  4. Calculate Volume Weighted Stock Price based on trades from the last 5 minutes.
  5. Compute the GBCE All Share Index using the geometric mean of all stocks.

Usage
-----
Run the application:

python bin/gbce_run_stocks.py

Results:
--------

Dividend Yield: 0.06666666666666667

P/E Ratio: 1800.0

Volume Weighted Stock Price: 126.66666666666667

GBCE All Share Index: 126.66666666666664


Running Tests
--------------
python -m unittest discover -s app/tests

Results

........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
