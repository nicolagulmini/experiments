import random as rnd
from matplotlib import pyplot as plt

# bingo simulation

class card:
    def __init__(self):
        self.cols = 9
        self.rows = 3
        self.list_of_numbers = [[0 for _ in range(3)] for __ in range(9)]
    def getCard(self):
        return self.list_of_numbers
    def colAndRow(self, n):
        if n in range(1, 91):
            index = int(n/10)
            if n == 90:
                index = 8
            for i in range(3):
                if self.list_of_numbers[index][i] == n:
                    return index, i
        return -1, -1
    def remove(self, n):
        if n in range(1, 91):
            col, row = self.colAndRow(n)
            if not col == -1:
                self.list_of_numbers[col][row] = 0
            return
        print("n out of range. Return")
    def row(self, i):
        if i not in range(3):
            print("Error in row method. Please pass 0 <= i <= 2. Return.")
            return 
        return [self.list_of_numbers[_][i] for _ in range(9)]   
    def col(self, i):
        if i not in range(9):
            print("Error in col method. Please pass 0 <= i <= 8. Return.")
            return 
        return self.list_of_numbers[i]
    def numberOfZeros(self):
        tmp = 0
        for col in self.list_of_numbers:
            for num in col:
                if num == 0:
                    tmp += 1
        return tmp
    def fillCard(self):
        numbers = [i for i in range(1, 91)]
        for col in range(8):
            if col == 0:
                extractedNumber = rnd.randint(1, 9)
            elif col < 8:
                extractedNumber = rnd.randint(col*10, col*10+9)
            else:
                extractedNumber = rnd.randint(col*10, col*10+10)
            numbers.remove(extractedNumber)
            self.list_of_numbers[col][0] = extractedNumber
        while self.numberOfZeros() > 15:
            extractedNumber = numbers[rnd.randint(0, len(numbers)-1)]
            numbers.remove(extractedNumber)
            colIndex = int(extractedNumber/10)
            if extractedNumber == 90:
                colIndex = 8
            if self.list_of_numbers[colIndex][2] == 0:
                rowIndex = 2
                if self.list_of_numbers[colIndex][1] == 0:
                    rowIndex = 1
                self.list_of_numbers[colIndex][rowIndex] = extractedNumber            


def simulation(n):
    players = [card() for _ in range(n)]
    for player in players:
        player.fillCard()
        #print(player.getCard())
        
    def win(players):
        for player in players:
            if player.numberOfZeros() == 27:
                return True
        return False
                
    numbers= [i for i in range(1, 91)]
    callsForWin = 0
    while not win(players):
        extracted = numbers[rnd.randint(0, len(numbers)-1)]
        numbers.remove(extracted)
        #print("Extracted:", extracted)
        for player in players:
            player.remove(extracted)
        callsForWin += 1
    return callsForWin

def estimateExp(n, trials):
    toRet = []
    for i in range(1, 1000):
        exp = 0
        for _ in range(trials):
            exp += simulation(i)/trials
        toRet.append(exp)
    return toRet

plt.plot(range(1, 1000), estimateExp(1000, 10), label="estimated number of extractions to win")
plt.legend(loc="upper right")
plt.xlabel("number of players")
plt.ylabel("expected extractions")
plt.savefig("fig.png")
