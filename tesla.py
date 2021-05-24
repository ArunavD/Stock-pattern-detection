import yfinance as yf

tesla = yf.Ticker("TSLA")

dataframe = tesla.history(period="1y")

#print(dataframe.to_csv())
dataframe.to_csv("tesla.csv")