import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf


file = 'tesla.csv'
data = pd.read_csv(file)
#print(data)
#data.info()


data.Date = pd.to_datetime(data.Date)
#data.info()


data = data.set_index('Date')
#print(data)

#Plotting the data
#mpf.plot(data)

#line and vloume type plot
#mpf.plot(data,type = 'line', volume = True)

#candle stick plot
#mpf.plot(data,type ='candle', volume = True)


#candle stick chart of a specific month
#mpf.plot(data['2020-07'],type ='candle', volume = True)


#candle stick chart for a time frame
#mpf.plot(data['2020-07':'2020-08'],type ='candle',volume = True, tight_layout = True)


#Adding title and style
mpf.plot(data['2020-07':'2020-08'],
         type = 'candle',
         title = 'Tesla price 2020\21',
         volume = True, 
         tight_layout = True,
         style = 'yahoo')
