from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd
import statistics as st


#test_data_frame = pd.read_csv("MasterThesisMethods/Method1/BTC_close_labeled_dataset_M0.csv", header=0, skiprows=range(1, 30001))
# test_data_frame = pd.read_csv("MasterThesisMethods/Method1/BTC_high_labeled_dataset_M1.csv", header=0, skiprows=range(1, 30001))
#test_data_frame = pd.read_csv("MasterThesisMethods/Method1/SOL_high_labeled_dataset_M1_1.csv", header=0, skiprows=range(1, 30001))
# test_data_frame = pd.read_csv("MasterThesisMethods/Method1/datasets/LTC_high_labeled_dataset_M1.csv", header=0, skiprows=(range(1, 56501)))
# test_data_frame = pd.read_csv("MasterThesisMethods/Method1/testtest.csv", header=0, skiprows=range(1, 25740))
test_data_frame = pd.read_csv("MasterThesisMethods/Method1/datasets/BTC_LTC_high_dataset_M1_combined.csv", header=0, skiprows=100000)


# print(test_data_frame)

test_data_frame2 = test_data_frame.drop(test_data_frame.columns[0], axis=1) # dropping the numerator column
test_data_frame2 = test_data_frame2.drop(test_data_frame2.columns[0], axis=1) #dropping the time column
print(test_data_frame2)

# columns_to_use = ["BTCUSDT:high0", "BTCUSDT:low0", "BTCUSDT:close0", "BTCUSDT:volume0", "Label"]         
# columns_to_use = ["BTCUSDT:high0", "BTCUSDT:low0", "BTCUSDT:close0", "BTCUSDT:volume0", "BTCUSDT:high1", "BTCUSDT:low1", "BTCUSDT:close1", "BTCUSDT:volume1", "BTCUSDT:high2", "BTCUSDT:low2", "BTCUSDT:close2", "BTCUSDT:volume2", "BTCUSDT:high3", "BTCUSDT:low3", "BTCUSDT:close3", "BTCUSDT:volume3", "BTCUSDT:high4", "BTCUSDT:low4", "BTCUSDT:close4", "BTCUSDT:volume4", "Label"]                                                                     
# columns_to_use = ["SOLUSDT:high0", "SOLUSDT:low0", "SOLUSDT:close0", "SOLUSDT:volume0", "SOLUSDT:high1", "SOLUSDT:low1", "SOLUSDT:close1", "SOLUSDT:volume1", "SOLUSDT:high2", "SOLUSDT:low2", "SOLUSDT:close2", "SOLUSDT:volume2", "SOLUSDT:high3", "SOLUSDT:low3", "SOLUSDT:close3", "SOLUSDT:volume3", "SOLUSDT:high4", "SOLUSDT:low4", "SOLUSDT:close4", "SOLUSDT:volume4", "Label"]
columns_to_use = ["LTCUSDT:high0", "LTCUSDT:low0", "LTCUSDT:close0", "LTCUSDT:volume0", "LTCUSDT:high1", "LTCUSDT:low1", "LTCUSDT:close1", "LTCUSDT:volume1", "LTCUSDT:high2", "LTCUSDT:low2", "LTCUSDT:close2", "LTCUSDT:volume2", "LTCUSDT:high3", "LTCUSDT:low3", "LTCUSDT:close3", "LTCUSDT:volume3", "LTCUSDT:high4", "LTCUSDT:low4", "LTCUSDT:close4", "LTCUSDT:volume4", "Label"]

print(test_data_frame2.columns)
test_data_frame2.columns = columns_to_use
print(test_data_frame2)
# test_data_frame2 = test_data_frame2[columns_to_use]

# print(test_data_frame2)
# print(test_data_frame2.shape)

########################################### TRAINING ######################################################
####### Testing data -> TabularDataset
test_tabular_dataset = TabularDataset(test_data_frame2)

# # # ####### Loading predictor
predictor = TabularPredictor.load("AutogluonModels/combined")


######## Making predictions
y_pred = predictor.predict(test_tabular_dataset.drop(columns=["Label"]))
print(y_pred)


# #### Evaluation
# p = predictor.evaluate(test_tabular_dataset, detailed_report=True)
# print(p)

# k = predictor.feature_importance(test_tabular_dataset)
# print(k)


################# Probability analysis ###########################
y_prob = predictor.predict_proba(test_tabular_dataset.drop(columns=["Label"]))
print(y_prob)
print()

counter = 0
correct = 0
predicted_high_list = []
predicted_low_list = []
predicted_close_list = []

balance = 100

hour_count = 0
month_gain = []
month = 100
LEVERAGE = 10

for index, pred in enumerate(y_pred):
    try:
        prob = y_prob[1][index]
        actual = test_data_frame2["Label"][index]

        true_high = test_data_frame2["LTCUSDT:high4"][index + 1]
        true_low = test_data_frame2["LTCUSDT:low4"][index + 1]
        true_close = test_data_frame2["LTCUSDT:close4"][index + 1]
        

        if prob > 0.825:
            counter += 1

            if pred == 1 and actual == 1:
                correct += 1
                predicted_high_list.append(true_high)
                predicted_low_list.append(true_low)
                predicted_close_list.append(true_close)

            ### LOGIC FOR CALCULATING GAIN ###
            if true_high >= 0.5:
                balance *= 1 + (0.005 * LEVERAGE)
                month *= 1 + (0.005 * LEVERAGE)
                print(f"{index}. Gain +5%")
            else:
                balance *= 1 + ((true_close / 100) * LEVERAGE)
                month *= 1 + ((true_close / 100) * LEVERAGE)
                #print(f"{index}. Close + {true_close} ---> High: {true_high}, Low: {true_low}, Close: {true_close}")
                print(f"{index}. Close +{true_close * LEVERAGE}")
    
        hour_count += 1
        if hour_count == 730:
            hour_count = 0
            month_gain.append(round(month - 100, 3))
            month = 100

    except:
        print("Error")


month_gain.append(month - 100)

        

print(f"Correct: {correct}")
print(f"Counter: {counter}")
print(f"Winrate: {correct / counter}")

print(f"AVG High: {st.mean(predicted_high_list)}")
print(f"AVG Low: {st.mean(predicted_low_list)}")
print(f"AVG Close: {st.mean(predicted_close_list)}")
print()
print(f"Balance: {balance}")
print(f"Return: {round(balance - 100, 3)}%")
print()
print(f"Month List: {month_gain}")
print(f"Mean month gain: {st.mean(month_gain)}")





# # # counter = 0
# # # correct = 0
# # # for index, pred in enumerate(y_pred):
# # #     prob = y_prob[1][index]

# # #     if prob < 0.4:
# # #         print(f"Prediction: {pred}, Probability: {prob}")
# # #         if pred == 0 and test_data_frame["Label"][index] == 0:
# # #             correct += 1
# # #         counter += 1

# # # print(f"Correct: {correct}")
# # # print(f"Counter: {counter}")
# # # ########################## END PROB ANALYSIS #####################