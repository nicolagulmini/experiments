'''
Suppose that we toss balls into b bins until some bin contains two balls. Each toss
is independent, and each ball is equally likely to end up in any bin. What is the
expected number of ball tosses?
'''

# A solution: https://sites.math.rutgers.edu/~ajl213/CLRS/Ch5.pdf

import random as rnd
from matplotlib import pyplot as plt
import math

nbins = 200

def thereAreTwoBallsInSomeBin(bins):
    for el in bins:
        if el == 2:
            return True
    return False

def countThrows(b):
    bins = [0 for _ in range(b)]
    count = 0
    while not thereAreTwoBallsInSomeBin(bins):
        bins[rnd.randint(0,b-1)] += 1
        count += 1
    return count

def expectationFormula(b):
    toReturn = 0
    for x in range(2, b+2):
        tmpProd = 1
        for i in range(1, x-1):
            tmpProd *= 1-i/b
        toReturn += x*(x-1)*tmpProd
    return toReturn/b

def BodnarLohr(b):
    toReturn = 0
    for x in range(2, b+2):
        tmpProd = 1
        for i in range(1, x):
            tmpProd *= 1-i/b
        toReturn += x*(x-1)*tmpProd
    return toReturn/b

def bound1(b):
    toReturn = 0
    for x in range(2, b+2):
        e = math.exp(-(x-2)*(x-3)/(2*b))
        toReturn += x*(x-1)*e
    return toReturn/b

def bound2(b):
    toReturn = 0
    for x in range(2, b+2):
        e = math.exp(-(x-2)/b)
        toReturn += x*(x-1)*e
    return toReturn/b
    

episodes, harmonics, expectations, BLexpectations, bound_1, bound_2 = [[0 for _ in range(nbins)] for __ in range(6)]

trials = 100

for b in range(1, nbins):
    expectations[b] = expectationFormula(b)
    harmonics[b] = 1/b+harmonics[b-1] # harmonic number
    BLexpectations[b] = BodnarLohr(b)
    bound_1[b] = bound1(b)
    bound_2[b] = bound2(b)
    for _ in range(trials):
        episodes[b] += countThrows(b)/trials

plt.plot(range(nbins), BLexpectations, label="Bodnar Lohr Expectation")
plt.plot(range(nbins), expectations, label="My solution")
plt.plot(range(nbins), harmonics, label="Harmonic number - for comparison")
plt.plot(range(nbins), episodes, label="Number of throws")
plt.plot(range(nbins), bound_1, label="Bound 1")
plt.plot(range(nbins), bound_2, label="Bound 2")
plt.legend(loc="upper left")
plt.ylim(.0, 31.0)
plt.savefig("fig.png")
