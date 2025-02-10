from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd
import statistics as st

test_data_frame = pd.read_csv("MasterThesisMethods/Method2/LTC_validation.csv", header=0)

test_data_frame2 = test_data_frame.drop(test_data_frame.columns[0], axis=1)

columns_to_use = ["LTCUSDT:high0", "LTCUSDT:low0", "LTCUSDT:close0", "LTCUSDT:volume0", "LTCUSDT:high1", "LTCUSDT:low1", "LTCUSDT:close1", "LTCUSDT:volume1", "LTCUSDT:high2", "LTCUSDT:low2", "LTCUSDT:close2", "LTCUSDT:volume2", "LTCUSDT:high3", "LTCUSDT:low3", "LTCUSDT:close3", "LTCUSDT:volume3", "LTCUSDT:high4", "LTCUSDT:low4", "LTCUSDT:close4", "LTCUSDT:volume4", "Label"]

test_data_frame2 = test_data_frame2[columns_to_use]
print(test_data_frame2.drop(columns=["Label"]))

########################################### TRAINING ######################################################
####### Testing data -> TabularDataset
test_tabular_dataset = TabularDataset(test_data_frame2)

# # # ####### Loading predictor
predictor = TabularPredictor.load("AutogluonModels/model2_combined")


######## Making predictions
y_pred = predictor.predict(test_tabular_dataset.drop(columns=["Label"]))
print(y_pred)


# ##### Evaluation
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

gain = 100

hour_count = 0
month_gain = []
month = 100

for index, pred in enumerate(y_pred):
    try:
        prob = y_prob[1][index]
        actual = test_data_frame["Label"][index]

        true_high = test_data_frame["LTCUSDT:high4"][index + 1]
        true_low = test_data_frame["LTCUSDT:low4"][index + 1]
        true_close = test_data_frame["LTCUSDT:close4"][index + 1]
        

        if prob > 0.65:
            counter += 1

            if pred == 1 and actual == 1:
                correct += 1
                predicted_high_list.append(true_high)
                predicted_low_list.append(true_low)
                predicted_close_list.append(true_close)

            ### LOGIC FOR CALCULATING GAIN ###
            if true_high >= 1:
                gain *= 1 + 0.008
                month *= 1 + 0.008
                print("Gain +0.8%")
            else:
                gain *= 1 + (true_close / 100)
                month *= 1 + (true_close / 100)
                print(f"Close + {true_close} ---> High: {true_high}, Low: {true_low}, Close: {true_close}")

    
        hour_count += 1
        if hour_count == 730:
            hour_count = 0
            month_gain.append(month - 100)
            month = 100

    except:
        print("Error")


        

print(f"Correct: {correct}")
print(f"Counter: {counter}")
print(f"Winrate: {correct / counter}")

print(f"AVG High: {st.mean(predicted_high_list)}")
print(f"AVG Low: {st.mean(predicted_low_list)}")
print(f"AVG Close: {st.mean(predicted_close_list)}")
print()
print(f"Gain: {gain}")
print(f"Return: {round(gain - 100, 3)}%")
print()
print(f"Month List: {month_gain}")
print(f"Mean month gain: {st.mean(month_gain)}")