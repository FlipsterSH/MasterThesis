from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd

# train_data_frame = pd.read_csv("datasets/train_data_frame")
# test_data_frame = pd.read_csv("datasets/test_data_frame")
train_data_frame = pd.read_csv("MasterThesisMethods/Method1/SOL_high_labeled_dataset_M1_1.csv", nrows=30000)

print(train_data_frame)

train_data_frame2 = train_data_frame.drop(train_data_frame.columns[0], axis=1)

# columns_to_use = ["BTCUSDT:high0", "BTCUSDT:low0", "BTCUSDT:close0", "BTCUSDT:volume0", "Label"]  
# columns_to_use = ["BTCUSDT:high0", "BTCUSDT:low0", "BTCUSDT:close0", "BTCUSDT:volume0", "BTCUSDT:high1", "BTCUSDT:low1", "BTCUSDT:close1", "BTCUSDT:volume1", "BTCUSDT:high2", "BTCUSDT:low2", "BTCUSDT:close2", "BTCUSDT:volume2", "BTCUSDT:high3", "BTCUSDT:low3", "BTCUSDT:close3", "BTCUSDT:volume3", "BTCUSDT:high4", "BTCUSDT:low4", "BTCUSDT:close4", "BTCUSDT:volume4", "Label"]                                                                     
columns_to_use = ["SOLUSDT:high0", "SOLUSDT:low0", "SOLUSDT:close0", "SOLUSDT:volume0", "SOLUSDT:high1", "SOLUSDT:low1", "SOLUSDT:close1", "SOLUSDT:volume1", "SOLUSDT:high2", "SOLUSDT:low2", "SOLUSDT:close2", "SOLUSDT:volume2", "SOLUSDT:high3", "SOLUSDT:low3", "SOLUSDT:close3", "SOLUSDT:volume3", "SOLUSDT:high4", "SOLUSDT:low4", "SOLUSDT:close4", "SOLUSDT:volume4", "Label"]
train_data_frame2 = train_data_frame2[columns_to_use]

print(train_data_frame2)

# print(train_data_frame2.shape)

############################################ TRAINING ######################################################
######## Training data -> TabularDataset
train_tabular_dataset = TabularDataset(train_data_frame2)
train_tabular_dataset.head()
label = "Label"
train_tabular_dataset[label].describe()
print(train_tabular_dataset)


# Training model -> TabularPredictor
# predictor = TabularPredictor(label=label, eval_metric="balanced_accuracy", positive_class=1).fit(train_tabular_dataset, num_bag_folds=5, num_bag_sets=5, num_stack_levels=3)
# predictor = TabularPredictor(label=label, eval_metric="accuracy").fit(train_tabular_dataset, presets="high_quality")
predictor = TabularPredictor(label=label).fit(train_tabular_dataset)