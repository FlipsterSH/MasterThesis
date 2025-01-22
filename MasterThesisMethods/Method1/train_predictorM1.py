from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd

# train_data_frame = pd.read_csv("datasets/train_data_frame")
# test_data_frame = pd.read_csv("datasets/test_data_frame")
# train_data_frame = pd.read_csv("MasterThesisMethods/Method1/LTC_high_labeled_dataset_M1_1.csv", nrows=30000)
train_data_frame = pd.read_csv("MasterThesisMethods/Method1/LTC_high_labeled_dataset_M1.csv", nrows=56500)

print(train_data_frame)

train_data_frame2 = train_data_frame.drop(train_data_frame.columns[0], axis=1)

# columns_to_use = ["BTCUSDT:high0", "BTCUSDT:low0", "BTCUSDT:close0", "BTCUSDT:volume0", "Label"]  
# columns_to_use = ["BTCUSDT:high0", "BTCUSDT:low0", "BTCUSDT:close0", "BTCUSDT:volume0", "BTCUSDT:high1", "BTCUSDT:low1", "BTCUSDT:close1", "BTCUSDT:volume1", "BTCUSDT:high2", "BTCUSDT:low2", "BTCUSDT:close2", "BTCUSDT:volume2", "BTCUSDT:high3", "BTCUSDT:low3", "BTCUSDT:close3", "BTCUSDT:volume3", "BTCUSDT:high4", "BTCUSDT:low4", "BTCUSDT:close4", "BTCUSDT:volume4", "Label"]                                                                     
columns_to_use = ["LTCUSDT:high0", "LTCUSDT:low0", "LTCUSDT:close0", "LTCUSDT:volume0", "LTCUSDT:high1", "LTCUSDT:low1", "LTCUSDT:close1", "LTCUSDT:volume1", "LTCUSDT:high2", "LTCUSDT:low2", "LTCUSDT:close2", "LTCUSDT:volume2", "LTCUSDT:high3", "LTCUSDT:low3", "LTCUSDT:close3", "LTCUSDT:volume3", "LTCUSDT:high4", "LTCUSDT:low4", "LTCUSDT:close4", "LTCUSDT:volume4", "Label"]
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