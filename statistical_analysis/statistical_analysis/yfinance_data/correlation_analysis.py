import yfinance as yf
import statistics
from supporting_functions import *
import pandas as pd
import numpy as np

"""
Analyzing correlation by calculating the correlation coefficient between the percent change differences at the same timeslots
Highest corrrelation is BNB, lowest correlation is ETH
"""

coins = {"BTC-USD": [], "ETH-USD": [], "BNB-USD": [], "SOL-USD": [], "XRP-USD": []}

#downloading data and convering into percent differences between each datapoint (price point)
for coin in coins:
    data_frame = yf.download(tickers=coin, period="2y", interval="1h")
    closing_data = data_frame['Close'].tolist()
    percent_hourly_diff_data = calculate_percent_differences(closing_data)
    coins[coin] = percent_hourly_diff_data
    # print(coin, percent_hourly_diff_data[0])

#trimming lists to same length
for coin1 in coins:
    for coin2 in coins:
        coin1_list, coin2_list = trim_lists_to_same_length(coins[coin1], coins[coin2])
        coins[coin1] = coin1_list
        coins[coin2] = coin2_list

# for coin in coins:
#     print(coins[coin][0])
#     print(len(coins[coin]))
#     print()

for coin in coins:
    correlation_coefficient = np.corrcoef(coins["BTC-USD"], coins[coin])
    print(f"{coin} - correlation coefficient to BTC-USD: {correlation_coefficient}")
