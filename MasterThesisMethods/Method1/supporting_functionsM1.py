import numpy as np
from datetime import datetime

def percent_difference(before, after):
    """
    Calculate the percent difference between two numbers.
    ONLY WORKS WITH POSITIVE NUMBERS

    Parameters:
    before (float or int): The initial value.
    after (float or int): The final value.

    Returns:
    float: The percent difference between the two numbers.
    """
    try:
        difference = after - before
        percent_diff = (difference / before) * 100
        return percent_diff
    except ZeroDivisionError:
        return 0.00000001



def calculate_percent_differences(prices):
    """
    -Calculate the percent difference between consecutive stock prices.
    -ONLY WORKS WITH POSITIVE NUMBERS
    -ROUNDS OFF TO NEAREST 0.1

    Parameters:
    prices (list of float or int): A list of stock prices.

    Returns:
    list of float: A list of percent differences between consecutive prices.
    """
    if len(prices) == 0 or type(prices) != list:
        return "error with input into calculate_percent_difference()"
    

    percent_differences = []
    try:
        for i in range(1, len(prices)):
            before = prices[i - 1]
            after = prices[i]
            percent_diff = percent_difference(before, after)
            #percent_differences.append(round_to_nearest_point_two(percent_diff))
            percent_differences.append(percent_diff)
        
        return percent_differences
    except:
        return "Error in calculate_percent_differences()"
    

def abs_calculate_percent_differences(prices):
    """
    Calculate the absolute percent difference between consecutive stock prices.
    This means no negative percenage changes
    ONLY WORKS WITH POSITIVE NUMBERS

    Parameters:
    prices (list of float or int): A list of stock prices.

    Returns:
    list of float: A list of percent differences between consecutive prices.
    """
    if len(prices) == 0 or type(prices) != list:
        return "error with input into calculate_percent_difference()"
    

    percent_differences = []
    try:
        for i in range(1, len(prices)):
            before = prices[i - 1]
            after = prices[i]
            percent_diff = percent_difference(before, after)
            percent_differences.append(abs(percent_diff))
        
        return percent_differences
    except:
        return "Error in calculate_percent_differences()"


def trim_lists_to_same_length(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        return "List has no length error in trim_lists_to_same_length()", "List has no length error in trim_lists_to_same_length()"
    # Find the length of the shorter list
    min_length = min(len(list1), len(list2))
    
    # Trim both lists from the start so that the ends are aligned
    trimmed_list1 = list1[-min_length:]
    trimmed_list2 = list2[-min_length:]
    
    return trimmed_list1, trimmed_list2


def round_to_nearest_half(data_list):
    rounded_list = []
    for x in data_list:
        rounded_value = round(x * 2) / 2
        rounded_list.append(rounded_value)
    return rounded_list


def round_to_nearest_point_two(number):
    # Multiply the number by 5, round to the nearest integer, then divide by 5
    rounded_number = round(number * 5) / 5
    return rounded_number


def assign_quantiles(data_list):
    # Calculate the quantiles based on the sorted data
    q1 = np.percentile(data_list, 25)
    q2 = np.percentile(data_list, 50)
    q3 = np.percentile(data_list, 75)
    
    # Create a new list with corresponding quantiles
    quantile_list = []
    for number in data_list:
        if number <= q1:
            quantile_list.append(1)
        elif number <= q2:
            quantile_list.append(2)
        elif number <= q3:
            quantile_list.append(3)
        else:
            quantile_list.append(4)
    
    return quantile_list


def label_terciles(numbers):
    """
    Takes a list of numbers and returns a list of labels (-1, 0, 1),
    based on the 1/3 and 2/3 quantiles.
    """
    # Convert to a NumPy array
    data = np.array(numbers)
    
    # Calculate the 1/3 (33.33%) and 2/3 (66.67%) quantiles
    q1 = np.percentile(data, 100/3)   # ~33.33rd percentile
    q2 = np.percentile(data, 200/3)   # ~66.67th percentile
    
    # Assign labels
    labels = np.where(data < q1, -1, np.where(data < q2, 0, 1))
    
    # Return as a regular Python list (optional: you can also return the NumPy array directly)
    return labels.tolist()


def normalize_list(numbers):
    ##### USES MIN MAX NOMALIZATION
    if not numbers:
        return []

    min_val = min(numbers)
    max_val = max(numbers)
    
    # Avoid division by zero if all numbers are the same
    if min_val == max_val:
        return [0.5] * len(numbers)

    normalized_numbers = [round((x - min_val) / (max_val - min_val), 5) for x in numbers]
    
    return normalized_numbers


# Function to convert Unix timestamp (in seconds or milliseconds) to a readable datetime string using strftime
def unix_to_datetime_string(unix_timestamp, in_milliseconds=True): #Takes in int or string
    if in_milliseconds:
        # Convert milliseconds to seconds
        unix_timestamp = int(unix_timestamp) / 1000
    return datetime.utcfromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %H:%M:%S')


# Function to return the Unix timestamp of the next day
def next_day_unix_timestamp(unix_timestamp, in_milliseconds=False): #Takes in int or string
    if in_milliseconds:
        # Add one day's worth of milliseconds
        next_day_timestamp = int(unix_timestamp) + (86400 * 1000)
    else:
        # Add one day's worth of seconds
        next_day_timestamp = int(unix_timestamp) + 86400
    return next_day_timestamp


# Function to return the Unix timestamp of the next week
def next_week_unix_timestamp(unix_timestamp, in_milliseconds=False):
    # Ensure the timestamp is an integer
    unix_timestamp = int(unix_timestamp)
    
    if in_milliseconds:
        # Number of milliseconds in one week: 7 days * 24 hours * 60 minutes * 60 seconds * 1000 milliseconds
        one_week_ms = 7 * 24 * 60 * 60 * 1000  # 604800000 milliseconds
        next_week_timestamp = unix_timestamp + one_week_ms
    else:
        # Number of seconds in one week: 7 days * 24 hours * 60 minutes * 60 seconds
        one_week_sec = 7 * 24 * 60 * 60  # 604800 seconds
        next_week_timestamp = unix_timestamp + one_week_sec
    
    return next_week_timestamp


def next_30_days_unix_timestamp(unix_timestamp, in_milliseconds=False):
    # Ensure the timestamp is an integer
    try:
        timestamp = int(unix_timestamp)
    except ValueError:
        raise ValueError("The unix_timestamp must be an integer or a string representing an integer.")

    # Number of seconds in one day
    seconds_per_day = 86400
    milliseconds_per_day = seconds_per_day * 1000

    if in_milliseconds:
        # Add 30 days worth of milliseconds
        added_time = milliseconds_per_day * 30
    else:
        # Add 30 days worth of seconds
        added_time = seconds_per_day * 30

    next_timestamp = timestamp + added_time
    return next_timestamp





if __name__ == "__main__":
    #Example usage percent_difference
    # before_value = 115
    # after_value = 110

    # result = percent_difference(before_value, after_value)
    # print(f"The percent difference is {result:.2f}%")



    # Example usage calculate_percent_differences
    stock_prices = [100, 200, 400, 800, 99999999]

    # percent_differences = calculate_percent_differences(stock_prices)
    # print(percent_differences)

    print(normalize_list(stock_prices))