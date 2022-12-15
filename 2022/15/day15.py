import re
import numpy as np

day = "15"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

if source == "test":
    target = 10
else:
    target = 2_000_000

input = []

with open(file, "r") as f:
    for line in f:
        input.append(re.sub(" +", " ", (re.sub(r'[^0-9\s]', '', line))).strip().split(" "))

def getDist(line):
    return abs(line[0]-line[2]) + abs(line[1]-line[3])


input = np.array(input)
input = input.astype(np.int_)

matchingTarget = []
beaconsTarget = set()

for line in input:
    sx = line[0]
    sy = line[1]
    bx = line[2]
    by = line[3]
    rad = getDist(line)
    if (sy - rad) <= target <= (sy + rad):
        width = rad - abs(sy - target)
        matchingTarget.append((sx - width, sx + width))
        if by == target:
            beaconsTarget.add((bx, by))

matchingTarget = np.array(matchingTarget)

if (np.min(matchingTarget)) <= 0:
    partOne = abs(np.min(matchingTarget)) + abs(np.max(matchingTarget)) + 1 - len(beaconsTarget)
else:
    partOne = abs(np.min(matchingTarget)) + abs(np.max(matchingTarget)) - len(beaconsTarget)
print(partOne)

search = target * 2

map = np.zeros(shape=(search, search))

def checkLine(i):
    matchingTarget = []
    for line in input:
        sx = line[0]
        sy = line[1]
        rad = getDist(line)
        if (sy - rad) <= i <= (sy + rad):
            width = rad - abs(sy - i)
            matchingTarget.append((sx - width, sx + width))

    matchingTarget = np.array(matchingTarget)
    for k in matchingTarget:
        for j in range(k[0], k[1]):
            if 0 <= j <= (search-1) :
                map[i][j] += 1
                print()
    print(matchingTarget)

for i in range(0, search):
    checkLine(i)

print(map)

for line in input:
    sx = line[0]
    sy = line[1]
    bx = line[2]
    by = line[3]
    if search > sx > 0 and search > sy > 0:
        map[sx][sy] += 5
    if search > bx > 0 and search > by > 0:
        map[bx][by] += 3

print(map)


    

