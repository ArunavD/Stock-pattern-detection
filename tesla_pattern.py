import csv


def is_barish_candlestick(candles):
    return candles["Close"] < candles["Open"]


def is_bullish_engulfing(candles,index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_barish_candlestick(previous_day)\
        and current_day["Open"] < previous_day["Close"]\
        and current_day["Close"] > previous_day["Open"]:
        return True
    
    return False




with open("tesla.csv") as f:
    reader = csv.DictReader(f)
    #print(reader)
    candles = list(reader)


for i in range(1, len(candles)):
    
    #print(candles[i])

    if is_bullish_engulfing(candles,i):
        print("{} It is bulish engulfing".format(candles[i]['Date']))




