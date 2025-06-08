import yfinance as yf
import statistics
from supporting_functions import *
import pandas as pd

"""
Analyzing volatility by calculating the standard deviation of a list of percentage differences
The list of percentage differences contains the hourly percent price difference in various cryptocurrencies

SOL has highest volatility
BTC has lowest volatility
"""

coins = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "XRP-USD"]

for coin in coins:
    data_frame = yf.download(tickers=coin, period="2y", interval="1h")
    closing_data = data_frame['Close'].tolist()
    percent_hourly_diff_data = calculate_percent_differences(closing_data)
    abs_percent_hourly_diff_data = abs_calculate_percent_differences(closing_data)


    print("LENGTH: ", len(closing_data))
    print(f"{coin} closing MAX: ", max(percent_hourly_diff_data))
    print(f"{coin} closing MIN: ", min(percent_hourly_diff_data))
    print(f"{coin} closing mean: ", statistics.mean(percent_hourly_diff_data))
    print(f"{coin} closing abs mean: ", statistics.mean(abs_percent_hourly_diff_data))
    print(f"{coin} closing stdev: ", statistics.stdev(percent_hourly_diff_data))
    print(f"{coin} closing abs stdev: ", statistics.stdev(abs_percent_hourly_diff_data))    

    counter = 0 #count number of times there are moves larger than 0.5%
    neg_counter = 0 #count number of times there are moves less than -0.5%
    for d in percent_hourly_diff_data:
        if d >= 0.5:
        #if round(d * 2) // 2 == 1:
            counter += 1
        
        if d <= -0.5:
            neg_counter += 1

    print(f"{coin} closing more than 0.5%: ", counter)
    print(f"{coin} closing less than -0.5%: ", neg_counter)
    print()
    print("--------------------------------")
    print()
