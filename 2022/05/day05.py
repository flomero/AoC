import numpy as np
import re
import copy

day = "05"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"
input = np.genfromtxt(file, delimiter = ",", dtype=str, unpack=False)

def getLine(word):
    linenumber = 1
    with open(file, 'r') as inputFile:
        for line in inputFile:
            words = line.split()
            if word in words:
                return linenumber
            linenumber += 1

stacks = []

with open(file) as inputFile:
    stacksRaw = inputFile.readlines()[0:(getLine("move")-3)]
    for s in stacksRaw:
        entries = re.findall('....?', s)
        print(entries)
        for index, i in enumerate(entries):
            i = i.strip().replace("[", "").replace("]", "")
            while (index + 1 > len(stacks)):
                stacks.append([])
            if i != "":
                stacks[index].insert(0, i)

second = copy.deepcopy(stacks)

with open(file) as inputFile:
    movesRaw = inputFile.readlines()[(getLine("move"))-1:]
    for line in movesRaw:
        steps = (re.sub(r"[a-z]", "", line)).split("  ")
        for i in range(int(steps[0].strip())):
            stacks[int(steps[2].strip()) -1].append(stacks[int(steps[1].strip()) -1].pop())

ans = ""

print(second)

for i in stacks[:]:
   ans = ans + i.pop()

print(second)

print(ans)

with open(file) as inputFile:
    movesRaw = inputFile.readlines()[(getLine("move"))-1:]
    for line in movesRaw:
        steps = (re.sub(r"[a-z]", "", line)).split("  ")
        start =  int(steps[1].strip()) -1
        target = int(steps[2].strip()) -1
        times = int(steps[0].strip())

        moved = second[start][(len(second[start])-times):].copy()
        second[start] = second[start][:(len(second[start])-times)]
        for i in moved:
            second[target].append(i)
        print(second)
    
ans2 = ""

for i in second[:]:
   ans2 = ans2 + str(i.pop())

print(ans2)



