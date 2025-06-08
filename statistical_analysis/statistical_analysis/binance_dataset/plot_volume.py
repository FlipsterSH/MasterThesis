import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics

def calculate_means(numbers):
    # Separate positive and negative numbers
    positive_numbers = [num for num in numbers if num > 0]
    negative_numbers = [num for num in numbers if num < 0]

    # Calculate means
    if positive_numbers:
        mean_positive = sum(positive_numbers) / len(positive_numbers)
    else:
        mean_positive = None  # No positive numbers in the list

    if negative_numbers:
        mean_negative = sum(negative_numbers) / len(negative_numbers)
    else:
        mean_negative = None  # No negative numbers in the list

    # Print results
    if mean_positive is not None:
        print(f"Mean of positive numbers: {mean_positive}")
    else:
        print("No positive numbers in the list.")

    if mean_negative is not None:
        print(f"Mean of negative numbers: {mean_negative}")
    else:
        print("No negative numbers in the list.")


dataframe = pd.read_csv("statistical_analysis/binance_dataset/test_dataset.csv")


# Replace this list with your own data
volume = dataframe["BTCUSDT:volume"].to_list()


print(f"MAX Volume: {max(volume)}")
print(f"MIN Volume: {min(volume)}")
print(f"MEAN Volume: {statistics.mean(volume)}")
print(f"SD Volume: {statistics.stdev(volume)}")
calculate_means(volume)



