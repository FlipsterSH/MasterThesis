import yfinance as yf
# import statistics
from supporting_functions import *
import pandas as pd
# import numpy as np
from sklearn.model_selection import train_test_split
# from autogluon.tabular import TabularDataset, TabularPredictor



#This script creates a train and test dataset and save them as CSVs



################################################### DOWNLOADING AND PREPROCESSING DATA ###########################################

coins = {"BTC-USD": [], "ETH-USD": [], "BNB-USD": [], "SOL-USD": [], "XRP-USD": []}
volumes = {"BTC-USD": [], "ETH-USD": [], "BNB-USD": [], "SOL-USD": [], "XRP-USD": []}

#downloading data and convering into percent differences between each datapoint (price point)
for coin in coins:
    data_frame = yf.download(tickers=coin, period="2y", interval="1h")
    closing_data = data_frame['Close'].tolist()
    volume_data = data_frame['Volume'].tolist()
    percent_hourly_diff_data = calculate_percent_differences(closing_data) #percent hourly diff data for  
    # hourly_volume_quantile = assign_quantiles(volume_data) #hourly volume quantile
    # volumes[coin] = hourly_volume_quantile
    hourly_volume_normalized = normalize_list(volume_data)
    coins[coin] = percent_hourly_diff_data
    volumes[coin] = hourly_volume_normalized

#trimming coin lists to same length
for coin1 in coins:
    for coin2 in coins:
        coin1_list, coin2_list = trim_lists_to_same_length(coins[coin1], coins[coin2])
        coins[coin1] = coin1_list
        coins[coin2] = coin2_list

#trimming volume lists to same length
for coin1 in volumes:
    for coin2 in volumes:
        coin1_list, coin2_list = trim_lists_to_same_length(volumes[coin1], volumes[coin2])
        volumes[coin1] = coin1_list
        volumes[coin2] = coin2_list

#trimmimng volume and coin list to be same length
for coin in coins:
    coin_list, volume_list = trim_lists_to_same_length(coins[coin], volumes[coin])
    coins[coin] = coin_list
    volumes[coin] = volume_list



################################################### CREATING LABELLED DATASETS ###########################################

#creating labelled data with solana price as label, two options 1 or 0 ---> 0: sol will trade less than 0.5% change, 1: = sol will grow by more than 0.5% the next hour
hours = 3
data = []
for i in range(len(coins["BTC-USD"]) - hours):
    data_row = []

    for t in range(hours):
        for coin in coins:
            data_row.append(coins[coin][i + t])
            data_row.append(volumes[coin][i + t])


    if coins["SOL-USD"][i + hours] >= 0.5:
        data_row.append(1)
    else:
        data_row.append(0)

    data.append(data_row)



cols = []
for t in range(hours):
    for coin in coins:
        cols.append(f"{coin}_change{t}")
        cols.append(f"{coin}_vol{t}")
cols.append("Label")

labelled_data_frame = pd.DataFrame(data, columns=cols)





################################################### SAVING DATASET ###########################################

# Splitting dataframes into Train and Test
train_data_frame, test_data_frame = train_test_split(labelled_data_frame, test_size=0.2)
train_data_frame.to_csv("datasets/train_data_frame")
test_data_frame.to_csv("datasets/test_data_frame")







