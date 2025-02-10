from binance import Client
from datetime import datetime, timedelta
import pandas as pd
from supporting_functionsM2 import *
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
        # print(klines)

    # Converting data from list to pandas dataframe
    new_data = pd.DataFrame(data=[row[0:6] for row in klines], columns=["time", "open", "high", "low", "close", "volume"])
    data = pd.concat([data, new_data], ignore_index=True)

    for _ in range(periods - 1):
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

    ########################################## PREPROCESSING DATA #################################################################### TODO FUNDAMENTAL FLAW OR SOMETHING WITH THE PREPROCESSING OF THE TWO HOUR INTERVALS
    # New dataobject for storing processed data
    processed_data = {f"{ticker}:time": [], f"{ticker}:open": [], f"{ticker}:high": [], f"{ticker}:low": [], f"{ticker}:close": [], f"{ticker}:volume": []}

    for i, o in enumerate(data["open"]): #o == open, the open price value of the candle stick
        if i <= 2: #Skipping the first three hour to calculate the percent diff using this hour
            continue

        if o == 0: # error handling if there is missing opening price or invalid dataset
            continue
        
        openprice = data["open"][i-1]
        highprice = max([float(data["high"][i-1]), float(data["high"][i])]) # the highest price within the two candlesticks hour 1 and hour 2
        lowprice = min([float(data["low"][i-1]), float(data["low"][i])]) # the lowest price within the two candlesticks hour 1 and hour 2

        processed_data[f"{ticker}:time"].append(data["time"][i]) # the time component is the closing time of the candlestick
        processed_data[f"{ticker}:open"].append(percent_difference(float(openprice), float(o))) # percent difference between the opening price of the prior hour vs. the next hour
        processed_data[f"{ticker}:high"].append(percent_difference(float(openprice), highprice)) # percent diff between open price of hour 1 and highest price within the two candlesticks
        processed_data[f"{ticker}:low"].append(percent_difference(float(openprice), lowprice)) # percent diff between open price of hour 1 and lowest price within the two candlesticks
        processed_data[f"{ticker}:close"].append(percent_difference(float(openprice), float(data["close"][i]))) # percent diff between open price in hour 1 and close price in hour 2
        processed_data[f"{ticker}:volume"].append(percent_difference(float(data["volume"][i-2]), float(data["volume"][i]))) # percent difference between the volume of the prior candlestick vs. open of current candle


    processed_data = pd.DataFrame(data=processed_data, columns=[f"{ticker}:time", f"{ticker}:open", f"{ticker}:high", f"{ticker}:low", f"{ticker}:close", f"{ticker}:volume"])
    return processed_data #returns a dataframe containing processed data



############################# CREATES THE LABELED DATASET ##########################################################################################################
#takes in a large pandas dataframe consisting of all the preprocessed data to create the labelled dataset
#tickers is the list of tickes used in the dataframe
#options is a list of options: "open", "high", "low", "close", "volume" - DO NOT INCLUDE TIME IN OPTIONS - TIME IS HARDCODED WITHIN THE LOOP
#value is the value to focus on, i.e "BTCUSDT:close" or "ETHUSDC:high"
#epochs means the numer of rows in the dataframe to analyse, i.e epochs=3 means using 3 rows (3 hours) of data from the dataframe to use as input data for the label
#threshold is the minimum accepted value for the label to be 1, else the label will be 0, i.e threshold = 0.5 means all data that is larger than 0.5 will be included
def create_labeled_dataset(dataframe, tickers, options, value, epochs, threshold, time):
    # column_labels = ["BTCUSDT:time"] # name of the columns for the return dataframe
    column_labels = ["time"] # name of the columns for the return dataframe

    # filling up the list with labels for the columns
    for round in range(epochs):
        for ticker in tickers:
            for option in options:
                column_labels.append(f"{ticker}:{option}{round}")
    
    column_labels.append("Label")


    # filling up list of data, row by row in the dataset
    data = [] # this list stores all the rows filled with all the data
    for i in range(len(dataframe[time]) - epochs - 1): #looping from the third element to the third last element, with stepsize 1, if epoch=3 # TODO FUNDAMENTAL FLAW IN THE FORLOOP RANGE
        data_row = [] # list stores data for one row

        data_row.append(dataframe[time][i + epochs])

        for t in range(epochs):
            for ticker in tickers:
                for option in options:
                    data_row.append(dataframe[f"{ticker}:{option}"][i + t])

        if dataframe[value][i + epochs + 1] > threshold: # here we use the threshold #TODO FUNDAMENTAL FLAW WITH CHOOSING THE VALIDATION VALUE
            data_row.append(1)
        else:
            data_row.append(0)

        data.append(data_row)


    labelled_data_frame = pd.DataFrame(data, columns=column_labels)
    return labelled_data_frame




if __name__ == "__main__":
    # start = "1514761200" # 01.01.2018
    # periods = 73 # approx 6 years
    # start = "1609455600" # 01.01.2021
    # periods = 36
    start = "1704063600" #01.01.2024
    periods = 12
    tickers = ["LTCUSDT"]


    options = ["high", "low", "close", "volume"] # BASE OPTIONS
    EPOCHS=5
    THRESHOLD=1 # Threshold value for lableling, ie. BTCUSDT:close = 0.5 > 0.0 => label = 1, if BTCUSDT:close = -0.5 < 0.0 => 0
    PREDICTOR="LTCUSDT:high"
    TIME = "LTCUSDT:time"
    data = []

    print("Initiating download sequence...")
    for ticker in tickers:
        dataframe = download_and_preprocess_data(ticker, periods, start)
        data.append(dataframe)
        print(f"{ticker} finished downloading.")

    concatenated_data = pd.concat(data, axis=1)

    # # These two lines are to save and print the dataset without label
    # concatenated_data.to_csv("correxction_dataset.csv")
    # print(concatenated_data)


    ############# THIS IS FOR CREATING LABELED DATASET #####################
    labeled_dataset = create_labeled_dataset(concatenated_data, tickers, options, value=PREDICTOR, epochs=EPOCHS, threshold=THRESHOLD, time=TIME)
    print(labeled_dataset)
    print(len(labeled_dataset.keys()))
    labeled_dataset.to_csv("LTC_validation.csv")



