'''
Generalized Coupon Collecting:
Suppose that there is a collection of n uniformly distributed cards and for each packet there are m ≤ n (usually m << n) different cards.  
Analyze the number of packets to buy to complete the collection in expectation and also in high probability.
'''

import random as rnd
from matplotlib import pyplot as plt
import numpy

# the cards are 0, 1, ..., n-1

def packet(n, m):
    extracted_cards = []
    while not len(extracted_cards) == m:
        extracted_card = rnd.randint(0, n-1)
        if extracted_card not in extracted_cards:
            extracted_cards.append(extracted_card)
    return extracted_cards

def completedCollection(coll):
    for el in coll:
        if el == 0:
            return False
    return True

def collect(n, m):
    collection = [0 for _ in range(n)]
    count = 0
    duplicates = 0
    while not completedCollection(collection):
        new_cards = packet(n, m)
        count += 1
        for card in new_cards:
            if collection[card] == 0:
                collection[card] = 1
            else:
                duplicates += 1
    return count, duplicates

def estimateExpectation(n, m, trials):
    expCount = 0
    expDup = 0
    for _ in range(trials):
        tmpCount, tmpDup = collect(n, m)
        expCount += tmpCount
        expDup += tmpDup
    return expCount/trials, expDup/trials

def boundExpectation(n, m):
    toReturn = 0
    for j in range(n):
        toReturn += 1/(1-(j/n)**m)
    return toReturn

def harmonic(n):
    toReturn = 0
    for j in range(1, n+1):
        toReturn += 1/j
    return toReturn

def highProbCount(n, m, d):
    return (d-1)*numpy.log(n)/(harmonic(n)-harmonic(n-m))

d = 2 
trials = 100

# analysis of number of packets, increasing n and fixing m = 5
max_n = 100
m = 5
count, expectation, highProb = [], [], []

for n in range(m, max_n):
    count.append(estimateExpectation(n, m, trials)[0])
    expectation.append(boundExpectation(n, m))
    highProb.append(highProbCount(n, m, d))
    
plt.plot(range(m, max_n), count, label="Number of packets")
plt.plot(range(m, max_n), expectation, label="Bound on expectation")
plt.plot(range(m, max_n), highProb, label="High probability number")
plt.legend(loc="upper left")
plt.xlabel("n")
plt.show()

# analysis of number of packets, increasing m and fixing n = 40
n = 40
max_m = 10
count, expectation, highProb = [], [], []
for m in range(1, max_m):
    count.append(estimateExpectation(n, m, trials)[0])
    expectation.append(boundExpectation(n, m))
    highProb.append(highProbCount(n, m, d))
    
plt.plot(range(1, max_m), count, label="Number of packets")
plt.plot(range(1, max_m), expectation, label="Bound on expectation")
plt.plot(range(1, max_m), highProb, label="High probability number")
plt.legend(loc="upper right")
plt.xlabel("m")
plt.show()

# (incomplete) analysis of duplicates
m = 5
max_n = 70
numberOfPacks, numberOfDuplicates = [], []
for n in range(m, max_n):
    tmpPacks, tmpDup = estimateExpectation(n, m, trials)
    numberOfPacks.append(tmpPacks)
    numberOfDuplicates.append(tmpDup)

plt.plot(range(m, max_n), numberOfPacks, label="Number of packets")
plt.plot(range(m, max_n), range(m, max_n), label="Cards to complete the collection")
plt.plot(range(m, max_n), numberOfDuplicates, label="Number of duplicates")
plt.legend(loc="upper left")
plt.show()
