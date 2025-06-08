import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dataframe = pd.read_csv("statistical_analysis/binance_dataset/test_dataset.csv")

print(dataframe.head())

def count_classes(classes, numbers):
    """
    Counts the occurrences of each class in the list of numbers.

    Args:
    classes (list): A list of distinct classes to check.
    numbers (list): A list of numbers to count classes in.

    Returns:
    list: A list of counts corresponding to each class in the classes list.
    """
    return [numbers.count(cls) for cls in classes]


# Create the list using list comprehension
numbers = [round(x, 1) for x in range(-1500, 1501)]

# Convert back to floats with the desired step of 0.01
numbers = [x / 100 for x in range(-1500, 1501)]


y1 = [round(num, 1) for num in dataframe["BTCUSDT:high"].to_list()]
y2 = [round(num, 1) for num in sorted(dataframe["BTCUSDT:low"].to_list())]
# y3 = [2.5, 3.5, 4.5, 5.5, 6.5]

# Example datasets
categories = numbers
data1 = count_classes(numbers, y1)
data2 = count_classes(numbers, y2)

# Bar width
bar_width = 0.25

# Positions of the bars on the x-axis
x = np.arange(len(categories))
x1 = x - bar_width  # For data1
x2 = x              # For data2

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(x1, data1, width=bar_width, label='Data 1', edgecolor='black')
plt.bar(x2, data2, width=bar_width, label='Data 2', edgecolor='black')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot of Multiple Datasets')
plt.xticks(x, categories)  # Set category labels on the x-axis
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()