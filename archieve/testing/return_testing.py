import random
import statistics

NUM_SIMS = 1000 #Number of simulations
DAYS = 365 #Number of days
NUM_TRADES = 2 #Number of trades
WINRATE = 58 #Winrate in whole percent
FEE = 0.00075 #Fee per buy and sell off 0.075%

WIN = 0.006 #Average gain per win in percent decimals
LOSS = 0.004 #Average loss per loss in percent decimals



values = []

for i in range(NUM_SIMS):
    value = 100
    for i in range(DAYS):
        for i in range(NUM_TRADES):
            r = random.randint(1, 100)
            if r >= WINRATE:
                value *= 1 - (LOSS + (FEE * 2))
            else:
                value *= 1 + (WIN - (FEE * 2))


    values.append(value)    


print("EXPECTED RETURN: ", round(statistics.mean(values), 3))

