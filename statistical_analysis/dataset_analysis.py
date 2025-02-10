import pandas as pd
from supporting_functions import *
import statistics

high_thresh = 0.5 # threshold for counting high values
low_thresh = -0.5 # threshold for counting low values

dataframe = pd.read_csv("statistical_analysis/4y_hourly_candlestick.csv", index_col=False)

###################### THIS ANALYSIS CHECK FOR NAN VALUES AND ZERO DIVISION ERRORS WITHIN THE DATASET #############################
print("DATASET ERROR ANALYSIS")

for col in dataframe.columns:
    nan_counter = 0
    zero_div_counter = 0
    for d in dataframe[col]:
        if d == 0.00000001:
            zero_div_counter += 1
    
    print(f"ZeroDiv errors : {col} : {zero_div_counter}")
    print(f"Nan values : {col} : {dataframe[col].isna().sum()}")
    print()

print("-----------------------------------------------------------")
print("EXTREME VALUE ANALYSIS")

high_data = {}
low_data = {}
close_data = {}

for col in dataframe.columns:
    if "high" in str(col):
        high_data[col] = dataframe[col].to_list()
    
    if "low" in str(col):
        low_data[col] = dataframe[col].to_list()
    
    if "close" in str(col):
        close_data[col] = dataframe[col].to_list()

diff_type_data = [high_data, low_data, close_data]



for ticker in high_data:
    print(f"Sample size of {ticker[0:6]} dataset: {len(dataframe[ticker].to_list())}")

print()
print(f"Ticker : Occurrences higher than {high_thresh}% : Highest high (in percent%)")
for ticker in high_data:
    # high_data[ticker] = dataframe[ticker].to_list()
    count = len([i for i in high_data[ticker] if i > high_thresh])
    print(f"{ticker} : {count} : {max(high_data[ticker])}")

print()
print(f"Ticker : Occurrences lower than {low_thresh} : Lowest low")
for ticker in low_data:
    # low_data[ticker] = dataframe[ticker].to_list()
    count = len([i for i in low_data[ticker] if i < low_thresh])
    print(f"{ticker} : {count} : {min(low_data[ticker])}")           



################ VOLATILITY ANALYSIS ###########################
print("---------------------------------------")
print("VOLATILITY ANALYSIS")
for data1 in diff_type_data:
    for ticker in data1:
        try:
            print(f"{ticker} MAX: {max(data1[ticker])}")
            print(f"{ticker} MIN: ", min(data1[ticker]))
            print(f"{ticker} mean: ", statistics.mean(data1[ticker]))
            print(f"{ticker} abs mean: ", statistics.mean([abs(x) for x in data1[ticker]]))
            print(f"{ticker} stdev: ", statistics.stdev(data1[ticker]))
            print(f"{ticker} abs stdev: ", statistics.stdev([abs(x) for x in data1[ticker]]))    

            counter = 0 #count number of times there are moves larger than 0.5%
            neg_counter = 0 #count number of times there are moves less than -0.5%
            for d in data1[ticker]:
                if d >= high_thresh:
                #if round(d * 2) // 2 == 1:
                    counter += 1
                
                if d <= low_thresh:
                    neg_counter += 1

            print(f"{ticker} moving more than {high_thresh}%: ", counter)
            print(f"{ticker} moving less than {low_thresh}%: ", neg_counter)
            print()

        except Exception as e:  # Catch general exceptions and assign to variable 'e'
            print(f"The dataset for {ticker} is missing data or incomplete: {e}")