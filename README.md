![](https://dqvh7oj3vu3ch.cloudfront.net/720x,q85/articles/remote/18743ddf07c1f8574a9ca56f2ece05c0.jpeg)

# Stock-pattern-detection
Detecting candlestick patterns in real time stocks

## Focus
Focusing mainly on finding bullish engulfing and bearish engulfing patters.

## What is bullish engulfing?
![](https://aliceblueonline.com/antiq/wp-content/uploads/2019/05/engulfing.001.png)
A bullish engulfing pattern is a white or green candlestick that closes higher than the previous day's opening after opening lower than the previous day's close.

## What is bearish engulfing?
![](https://best-mt4-indicators.com/wp-content/uploads/2020/06/engulfing-candle-indicator.png)
A bearish engulfing pattern is a technical chart pattern that signals lower prices to come. The pattern consists of an up (white or green) candlestick followed by a large down (black or red) candlestick that eclipses or "engulfs" the smaller up candle.

<!-- Libraries -->
## Libraries
+ [yfinance](https://pypi.org/project/yfinance/) - An easy-to-use Python library for accessing the informations of Stocks.
+ [pandas](https://pypi.org/project/pandas/) - the most powerful and flexible open source data analysis / manipulation tool.
+ [matplotlib](https://pypi.org/project/matplotlib/) - is a comprehensive library for creating static, animated, and interactive visualizations in Python.


<!-- Description -->
## Description of each file
1. [tesla.py](https://github.com/ArunavD/Stock-pattern-detection/blob/master/tesla.py) - Extracting all historical stock information of tesla and saving the output to a csv file.
2. [tesla.csv](https://github.com/ArunavD/Stock-pattern-detection/blob/master/tesla.csv)- Output file of tesla.py
3. [tesla_price_visualisation.py](https://github.com/ArunavD/Stock-pattern-detection/blob/master/tesla_price_visualisation.py) - Visualising the output csv file.
4.  [tesla_pattern.py](https://github.com/ArunavD/Stock-pattern-detection/blob/master/tesla_pattern.py) - Finding bullish engulfing patterns in tesla.csv file.
5.  [sp500_companies.csv](https://github.com/ArunavD/Stock-pattern-detection/blob/master/sp500_companies.csv) - A csv file of S&P 500 companies list and their ticker name.
6.  [download_sp500_history.py](https://github.com/ArunavD/Stock-pattern-detection/blob/master/download_sp500_history.py) - Downloading all historical data of S&P 500 companies and saving them to different csv files.
7.  [history](https://github.com/ArunavD/Stock-pattern-detection/tree/master/history) - Contains all output csv files of S&P 500 companies.
8.  [sp500_pattern.py](https://github.com/ArunavD/Stock-pattern-detection/blob/master/sp500_pattern.py) - Finding bullish engulfing and bearish engulfing patterns in all the S&P 500 companies csv files.
