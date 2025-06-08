from binance import Client
from datetime import datetime, timedelta
import pandas as pd
from supporting_functions import *
from API_KEYS2 import get_keys


def download_and_preprocess_data(ticker, periods, start):
    ############################################# Setting up client #####################################################################
    KEY, SECRET = get_keys()
    client = Client(KEY, SECRET)


    ############################################# SETTING UP PARAMETRES #################################################################
    periods = periods
    LIMIT = 720 # 720h = 30 days
    START = start
    END = next_30_days_unix_timestamp(START)


    ############################################ DOWNLOADING DATA ###################################################################### 
    data = pd.DataFrame(columns=["time", "open", "high", "low", "close", "volume"])

    # downloading the first set of candlestick lines
    klines = client.get_historical_klines(ticker, client.KLINE_INTERVAL_1HOUR, limit=LIMIT, start_str=unix_to_datetime_string(START, in_milliseconds=False), end_str=unix_to_datetime_string(END, in_milliseconds=False))


    # Converting data from list to pandas dataframe
    new_data = pd.DataFrame(data=[row[0:6] for row in klines], columns=["time", "open", "high", "low", "close", "volume"])
    data = pd.concat([data, new_data], ignore_index=True)

    for i in range(periods - 1):
        # Moving the start and end interval to next day
        START = next_30_days_unix_timestamp(START)
        END = next_30_days_unix_timestamp(START) 

        # downloading candlestick lines
        klines = client.get_historical_klines(ticker, client.KLINE_INTERVAL_1HOUR, limit=LIMIT, start_str=unix_to_datetime_string(START, in_milliseconds=False), end_str=unix_to_datetime_string(END, in_milliseconds=False))
        # print(klines)

        # Converting data from list to pandas dataframe
        new_data = pd.DataFrame(data=[row[0:6] for row in klines], columns=["time", "open", "high", "low", "close", "volume"])

        # concatinating the new data with the existing data
        data = pd.concat([data, new_data], ignore_index=True)

    # converting all time values from unix to readable string, not important, just for visual purposes and fact checking
    data["time"] = data["time"].apply(unix_to_datetime_string) #converting time from 


    ########################################## PREPROCESSING DATA ####################################################################
    # New dataobject for storing post processing data
    processed_data = {f"{ticker}:time": [], f"{ticker}:open": [], f"{ticker}:high": [], f"{ticker}:low": [], f"{ticker}:close": [], f"{ticker}:volume": []}

    for i, o in enumerate(data["open"]): #o == open, the open price value of the candle stick
        if i == 0: #Skipping the first hour to calculate the percent diff using this hour
            continue

        processed_data[f"{ticker}:time"].append(data["time"][i]) #time is the same
        processed_data[f"{ticker}:open"].append(percent_difference(float(data["open"][i-1]), float(o))) # percent difference between the opening price of the prior candlestick vs. open of current candle
        processed_data[f"{ticker}:high"].append(percent_difference(float(o), float(data["high"][i]))) # percent diff between open and high
        processed_data[f"{ticker}:low"].append(percent_difference(float(o), float(data["low"][i]))) # percent diff between open and low
        processed_data[f"{ticker}:close"].append(percent_difference(float(o), float(data["close"][i]))) # percent diff between open and close
        processed_data[f"{ticker}:volume"].append(percent_difference(float(data["volume"][i-1]), float(data["volume"][i]))) # percent difference between the colume of the prior candlestick vs. open of current candle


    processed_data = pd.DataFrame(data=processed_data, columns=[f"{ticker}:time", f"{ticker}:open", f"{ticker}:high", f"{ticker}:low", f"{ticker}:close", f"{ticker}:volume"])
    return processed_data #returns a dataframe containing processed data



############################# CREATES THE LABELED DATASET ##########################################################################################################
#takes in a large pandas dataframe consisting of all the preprocessed data to create the labelled dataset
#tickers is the list of tickes used in the dataframe
#options is a list of options, in this case it will always be: "open", "high", "low", "close", "volume" - DO NOT INCLUDE TIME IN OPTIONS - TIME IS HARDCODED WITHIN THE LOOP
#value is the value to focus on, i.e "BTCUSDC:close" or "ETHUSDC:high"
#epochs means the numer of rows in the dataframe to analyse, i.e epochs=3 means using 3 rows (3 hours) of data from the dataframe to use as input data for the label
#threshold is the minimum accepted value for the label to be 1, else the label will be 0, i.e threshold = 0.5 means all data that is larger than 0.5 will be included
def create_labeled_dataset(dataframe, tickers, options, value, epochs, threshold):
    column_labels = ["BTCUSDC:time"] # name of the columns for the return dataframe

    # filling up the list with labels for the columns
    for round in range(epochs):
        for ticker in tickers:
            for option in options:
                column_labels.append(f"{ticker}:{option}{round}")
    
    column_labels.append("Label")


    # filling up list of data, row by row in the dataset
    data = [] # this list stores all the rows filled with all the data
    for i in range(len(dataframe["BTCUSDC:time"]) - epochs): #looping from the third element to the third last element, with stepsize 1
        data_row = []

        data_row.append(dataframe["BTCUSDC:time"][i + epochs])

        for t in range(epochs):
            for ticker in tickers:
                for option in options:
                    data_row.append(dataframe[f"{ticker}:{option}"][i + t])

        if dataframe[value][i + epochs] > threshold: # here we use the threshold
            data_row.append(1)
        else:
            data_row.append(0)

        data.append(data_row)


    labelled_data_frame = pd.DataFrame(data, columns=column_labels)
    return labelled_data_frame




if __name__ == "__main__":
    start = "1609459200" #01.01.2021
    periods = 42 # number of 30 day periods
    tickers = ["BTCUSDC", "ETHUSDC", "BNBUSDC"]
    options = ["open", "high", "low", "close", "volume"]
    data = []

    print("Initiating download sequence...")
    for ticker in tickers:
        dataframe = download_and_preprocess_data(ticker, periods, start)
        data.append(dataframe)
        print(f"{ticker} finished downloading.")

    concatenated_data = pd.concat(data, axis=1)

    concatenated_data.to_csv("testing_dataset2.csv")
    print(concatenated_data)


    labeled_dataset = create_labeled_dataset(concatenated_data, tickers, options, value="ETHUSDC:high", epochs=3, threshold=0.5)
    print(labeled_dataset)
    print(len(labeled_dataset.keys()))
    labeled_dataset.to_csv("testing_dataset1_labeled.csv")



