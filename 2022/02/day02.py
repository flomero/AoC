import numpy as np

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/02/" + source + ".txt"
input = np.genfromtxt(file, delimiter = "", dtype=str, unpack=False)

print(input)

def getPoints(round, index):
    a = index
    if a == 1: b = 0
    if a == 0: b = 1

    roundScore = 0
    if round[a] == "X":
        roundScore += 1
    elif round[a] == "Y":
        roundScore += 2
    elif round[a] == "Z":
        roundScore += 3
    
    if [round[a], round[b]] in [["A", "X"], ["B", "Y"], ["C", "Z"], ["X", "A"], ["Y", "B"], ["Z", "C"]]:
        roundScore += 3
    elif [round[a], round[b]] in [["A", "Z"], ["B", "X"], ["C", "Y"], ["X", "C"], ["Y", "A"], ["Z", "B"]]:
        roundScore += 6
    
    return roundScore

score = 0    

for i in input:
    score += getPoints(i, 1)

print("1: " + str(score))

win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

lose = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

draw = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

score2 = 0

for i in input:
    if i[1] == "X":
        i[1] = lose[i[0]]
    elif i[1] == "Y":
        i[1] = draw[i[0]]
    elif i[1] == "Z":
        i[1] = win[i[0]]
    score2 += getPoints(i, 1)

print("2: " + str(score2))
print(input)
    