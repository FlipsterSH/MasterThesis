

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
        return 0



def calculate_percent_differences(prices):
    """
    Calculate the percent difference between consecutive stock prices.
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




if __name__ == "__main__":
    #Example usage percent_difference
    # before_value = 115
    # after_value = 110

    # result = percent_difference(before_value, after_value)
    # print(f"The percent difference is {result:.2f}%")



    # Example usage calculate_percent_differences
    stock_prices = [100, 200, 400, 800]

    percent_differences = calculate_percent_differences(stock_prices)
    print(percent_differences)