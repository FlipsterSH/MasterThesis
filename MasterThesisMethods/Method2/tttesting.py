import pandas as pd


test_data_frame = pd.read_csv("MasterThesisMethods/Method2/Combined_datasets_2h_7y.csv", header=0)

labels = test_data_frame["Label"].to_list()


zeros = 0
ones = 1

for l in labels:
    if l == 0:
        zeros += 1
    if l == 1:
        ones += 1

print(zeros)
print(ones)