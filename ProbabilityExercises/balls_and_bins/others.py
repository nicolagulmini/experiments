'''
Occupancy: balls and bins
'''

import random as rnd
from matplotlib import pyplot as plt

# n is the number of bins, m is the number of balls

def trial(n, m):
    bins = [0 for _ in range(n)]
    for _ in range(m):
        bins[rnd.randint(0, n-1)] += 1
    maxBalls = max(bins)
    numberOfEmptyBins = 0
    for el in bins:
        if el == 0:
            numberOfEmptyBins += 1
    return maxBalls, numberOfEmptyBins

# analysis varying n
max_n = 30
m = 20
trials = 100

maxBallsList, numberOfEmptyBinsList = [], []

for n in range(1, max_n):
    maxBalls, numberOfEmptyBins = 0, 0
    for _ in range(trials):
        tmp_maxBalls, tmp_numberOfEmptyBins = trial(n, m)
        maxBalls += tmp_maxBalls
        numberOfEmptyBins += tmp_numberOfEmptyBins
    maxBallsList.append(maxBalls/trials)
    numberOfEmptyBinsList.append(numberOfEmptyBins/trials)
    

plt.plot(range(1, max_n), maxBallsList, label="Expected max balls in a bin")
plt.plot(range(1, max_n), numberOfEmptyBinsList, label="Expected number of empty bins")
plt.plot(range(1, max_n), [n*((1-1/n)**m) for n in range(1, max_n)], label="Expected value of empty bins")
plt.legend(loc="upper left")
plt.xlabel("n")
plt.show()

# analysis varying m
max_m = 110
n = 30
trials = 100

maxBallsList, numberOfEmptyBinsList = [], []

for m in range(1, max_m):
    maxBalls, numberOfEmptyBins = 0, 0
    for _ in range(trials):
        tmp_maxBalls, tmp_numberOfEmptyBins = trial(n, m)
        maxBalls += tmp_maxBalls
        numberOfEmptyBins += tmp_numberOfEmptyBins
    maxBallsList.append(maxBalls/trials)
    numberOfEmptyBinsList.append(numberOfEmptyBins/trials)


plt.plot(range(1, max_m), maxBallsList, label="Expected max balls in a bin")
plt.plot(range(1, max_m), numberOfEmptyBinsList, label="Expected number of empty bins")
plt.plot(range(1, max_m), [n*((1-1/n)**m) for m in range(1, max_m)], label="Expected value of empty bins")
plt.legend(loc="upper left")
plt.xlabel("m")
plt.show()
