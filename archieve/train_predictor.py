from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd

# train_data_frame = pd.read_csv("datasets/train_data_frame")
# test_data_frame = pd.read_csv("datasets/test_data_frame")
train_data_frame = pd.read_csv("training_set.csv")

train_data_frame.drop(["BTCUSDC:time"], axis=1, inplace=True)
train_data_frame2 = train_data_frame.drop(train_data_frame.columns[0], axis=1)

columns_to_use = ["BTCUSDC:close2", "BTCUSDC:open1", "BTCUSDC:high0", "BTCUSDC:high1", "BTCUSDC:close0", "BTCUSDC:low2", "BNBUSDC:high2", "BNBUSDC:low2", "BNBUSDC:close2", "BNBUSDC:low0", "BNBUSDC:high1", "BNBUSDC:open1", "BNBUSDC:close0", "Label"]                                                                       
train_data_frame2 = train_data_frame2[columns_to_use]

print(train_data_frame2)


# test_data_frame = test_data_frame.drop(test_data_frame.columns[0], axis=1)

print(train_data_frame2.shape)
# print(test_data_frame.shape)

############################################ TRAINING ######################################################
######## Training data -> TabularDataset
train_tabular_dataset = TabularDataset(train_data_frame2)
train_tabular_dataset.head()
label = "Label"
train_tabular_dataset[label].describe()
print(train_tabular_dataset)


# Training model -> TabularPredictor
# predictor = TabularPredictor(label=label, eval_metric="balanced_accuracy", positive_class=1).fit(train_tabular_dataset, num_bag_folds=5, num_bag_sets=5, num_stack_levels=3)
predictor = TabularPredictor(label=label, eval_metric="accuracy").fit(train_tabular_dataset, presets="best_quality")

#predictor = TabularPredictor(label=label).fit(train_tabular_dataset)