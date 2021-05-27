import csv

def is_bullish_candlestick(candles):
    return float(candles['Close']) > float(candles['Open'])



def is_bearish_candlestick(candles):
    return float(candles['Close']) < float(candles['Open'])



def is_bullish_engulfing(candles,index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bearish_candlestick(previous_day)\
        and float(current_day['Open']) < float(previous_day['Close'])\
        and float(current_day['Close']) > float(previous_day['Open']):
        return True
    
    return False


def is_bearish_engulfing(candles,index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bullish_candlestick(previous_day)\
        and float(current_day["Open"]) > float(previous_day["Close"])\
        and float(current_day["Close"]) < float(previous_day["Open"]):
        return True
    
    return False



sp500_file = open("sp500_companies.csv")
sp500_companies = csv.reader(sp500_file)

for company in sp500_companies:
    #print(company)

    ticker, company_name = company

    history_file = open("history/{}.csv".format(ticker))


    reader = csv.DictReader(history_file)
    candles = list(reader)

    for i in range(1, len(candles)):
        

        if is_bullish_engulfing(candles,i):
           print("{} - In {}, it is bulish engulfing".format(ticker, candles[i]['Date']))
           break
        

    
        if is_bearish_engulfing(candles,i):
            print("{} - In {}, it is bearish engulfing".format(ticker, candles[i]['Date']))
