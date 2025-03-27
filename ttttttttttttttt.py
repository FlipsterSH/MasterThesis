probabilities = [1, 1, 0.5, 0.1, 0.2, 0.7, 0.7, 0.8, 0.8, 0.9, 0.75]
actual = [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
closes = [1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1]


MINIMUM_PROBABILITY = 0.70
LEVERAGE = 1
GAIN = 0.5

CORRECT = 0
NUM_TRADES = 0
BAD_TRADES = []
ALL_TRADES = []
invested = 100
invested_list = []


for index, probbb in enumerate(probabilities):
    predicted = round(probbb)

    # IF THE PREDICTION HAS A SUFFICIENT PROBABILITY
    if probbb >= MINIMUM_PROBABILITY:
        NUM_TRADES += 1

        # IF THE PREDICTION IS CORRECT
        if predicted == actual[index]:
            CORRECT += 1
            ALL_TRADES.append(GAIN * LEVERAGE)
            invested *= 1 + (GAIN / 100 * LEVERAGE)
            copyy = invested
            invested_list.append(copyy)

        # IF THE PREDICTION IS INCORRECT    
        else:
            true_close = closes[index]
            bad_trad = (round(true_close * LEVERAGE, 3), round(probbb, 3))
            BAD_TRADES.append(bad_trad)
            ALL_TRADES.append(true_close * LEVERAGE)
            invested *= 1 + (true_close/ 100 * LEVERAGE)
            copyy = invested
            invested_list.append(copyy)

    else:
        copyy = invested
        invested_list.append(copyy)



print(f"CORRECT: {CORRECT}")
print(f"WRONG: {NUM_TRADES - CORRECT}")
print(f"NUMBER OF TRADES: {NUM_TRADES}")
print(f"WINRATE: {round(CORRECT / NUM_TRADES, 3) * 100}%")
print(f"RETURN: {invested - 100}")
print(f"IVESTMENT VALUE: {invested}")
print("----------------------------------")
for btbb in BAD_TRADES:
    print(btbb)

print(invested_list)