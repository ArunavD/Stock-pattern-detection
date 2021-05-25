import csv


with open("tesla.csv") as f:
    reader = csv.DictReader(f)
    #print(reader)
    candles = list(reader)


for i in range(1, len(candles)):
    print(candles[i])