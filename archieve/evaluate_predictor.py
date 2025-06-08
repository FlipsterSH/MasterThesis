from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd


# test_data_frame = pd.read_csv("datasets/test_data_frame", index_col=False)
# test_data_frame = test_data_frame.drop(test_data_frame.columns[0], axis=1)

test_data_frame = pd.read_csv("validation_set.csv", index_col=False)
test_data_frame.drop(["BTCUSDC:time"], axis=1, inplace=True)
test_data_frame = test_data_frame.drop(test_data_frame.columns[0], axis=1)

# # # ####### Loading predictor
# predictor = TabularPredictor.load("AutogluonModels/ag-20240921_151853")
predictor = TabularPredictor.load("AutogluonModels/ag-20241006_155434")


####### Testing data -> TabularDataset
test_tabular_dataset = TabularDataset(test_data_frame)


######## Making predictions
y_pred = predictor.predict(test_tabular_dataset.drop(columns=["Label"]))
print(y_pred)
y_pred.head()


####### Evaluation
p = predictor.evaluate(test_tabular_dataset, detailed_report=True)
#p = predictor.evaluate(test_tabular_dataset)
print(p)

k = predictor.feature_importance(test_tabular_dataset)
print(k)
