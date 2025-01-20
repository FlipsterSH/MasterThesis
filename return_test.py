import random
import statistics as st

NUM_TRADES = 210 # number of trades within period
WINR = 66.1 # winrate in percentage
NUM_SIM = 1000
GAIN = 0.5 # gain in percent
LOSS = 0.6


sims = []
for sim in range(NUM_SIM):
    start = 1
    for trade in range(NUM_TRADES):
        win = random.randint(1, 1000) / 10
        if win < WINR:
            start *= 1 + (GAIN / 100)
        else:
            start *= 1 - (LOSS / 100)


    sims.append(start)

print(st.mean(sims))


