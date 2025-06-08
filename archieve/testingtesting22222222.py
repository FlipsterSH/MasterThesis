import pandas as pd

# train_data_frame = pd.read_csv("datasets/train_data_frame")
# test_data_frame = pd.read_csv("datasets/test_data_frame")
train_data_frame = pd.read_csv("training_set.csv")

train_data_frame.drop(["BTCUSDC:time"], axis=1, inplace=True)
train_data_frame2 = train_data_frame.drop(train_data_frame.columns[0], axis=1)

for l in train_data_frame2["Label"]:
    print(type(l))