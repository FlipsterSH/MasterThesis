from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd


#test_data_frame = pd.read_csv("MasterThesisMethods/Method1/BTC_close_labeled_dataset_M0.csv", header=0, skiprows=range(1, 30001))
#test_data_frame = pd.read_csv("MasterThesisMethods/Method1/BTC_high_labeled_dataset_M1.csv", header=0, skiprows=range(1, 30001))
test_data_frame = pd.read_csv("MasterThesisMethods/Method1/SOL_high_labeled_dataset_M1_1.csv", header=0, skiprows=range(1, 30001))


# print(test_data_frame)

test_data_frame2 = test_data_frame.drop(test_data_frame.columns[0], axis=1)

# columns_to_use = ["BTCUSDT:high0", "BTCUSDT:low0", "BTCUSDT:close0", "BTCUSDT:volume0", "Label"]         
# columns_to_use = ["BTCUSDT:high0", "BTCUSDT:low0", "BTCUSDT:close0", "BTCUSDT:volume0", "BTCUSDT:high1", "BTCUSDT:low1", "BTCUSDT:close1", "BTCUSDT:volume1", "BTCUSDT:high2", "BTCUSDT:low2", "BTCUSDT:close2", "BTCUSDT:volume2", "BTCUSDT:high3", "BTCUSDT:low3", "BTCUSDT:close3", "BTCUSDT:volume3", "BTCUSDT:high4", "BTCUSDT:low4", "BTCUSDT:close4", "BTCUSDT:volume4", "Label"]                                                                     
columns_to_use = ["SOLUSDT:high0", "SOLUSDT:low0", "SOLUSDT:close0", "SOLUSDT:volume0", "SOLUSDT:high1", "SOLUSDT:low1", "SOLUSDT:close1", "SOLUSDT:volume1", "SOLUSDT:high2", "SOLUSDT:low2", "SOLUSDT:close2", "SOLUSDT:volume2", "SOLUSDT:high3", "SOLUSDT:low3", "SOLUSDT:close3", "SOLUSDT:volume3", "SOLUSDT:high4", "SOLUSDT:low4", "SOLUSDT:close4", "SOLUSDT:volume4", "Label"]


test_data_frame2 = test_data_frame2[columns_to_use]

# print(test_data_frame2)
# print(test_data_frame2.shape)

########################################### TRAINING ######################################################
####### Testing data -> TabularDataset
test_tabular_dataset = TabularDataset(test_data_frame2)

# # # ####### Loading predictor
predictor = TabularPredictor.load("AutogluonModels/model1_1_2")


######## Making predictions
y_pred = predictor.predict(test_tabular_dataset.drop(columns=["Label"]))
print(y_pred)


print("######################### PROBABILITY")
y_prob = predictor.predict_proba(test_tabular_dataset.drop(columns=["Label"]))
print(y_prob)
print("####################################")
print()


counter = 0
correct = 0
for index, pred in enumerate(y_pred):
    prob = y_prob[1][index]
    actual = test_data_frame["Label"][index]
    

    if prob > 0.6:
        if pred == 1 and actual == 1:
            correct += 1
        counter += 1
        print(f"Prediction: {pred}, Probability: {prob}, Actual: {actual}")

print(f"Correct: {correct}")
print(f"Counter: {counter}")



# counter = 0
# correct = 0
# for index, pred in enumerate(y_pred):
#     prob = y_prob[1][index]

#     if prob < 0.4:
#         print(f"Prediction: {pred}, Probability: {prob}")
#         if pred == 0 and test_data_frame["Label"][index] == 0:
#             correct += 1
#         counter += 1

# print(f"Correct: {correct}")
# print(f"Counter: {counter}")



##### Evaluation
p = predictor.evaluate(test_tabular_dataset, detailed_report=True)
print(p)

k = predictor.feature_importance(test_tabular_dataset)
print(k)
