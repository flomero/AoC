from math import sqrt
import sys
import numpy as np

day = "11"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

factor = 1_000_000

input = np.genfromtxt(file, dtype=str, delimiter=1, comments=None)
part2 = input.copy()

def addDots(arr, *args):
    copy = arr.copy()
    x = 0
    for index, row in enumerate(copy):
        if np.all(row == "."):
            arr = np.insert(arr, index + x, ".", axis=0) 
            x += 1
    return arr 

def findDots(arr):
    dots = []
    for index, row in enumerate(arr):
        if np.all(row == "."):
            dots.append(index)
    return dots

input = addDots(input)
input = addDots(input.T).T

galaxys = []

for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        if input[i][j] == "#":
            galaxys.append([i, j])

def findPath(start, end):
    dist = abs(start[0] - end[0]) + abs(start[1] - end[1])
    return dist

result = 0

for i in range(0, len(galaxys)):
    for j in range(0, len(galaxys)):
        if i < j:
            result += findPath(galaxys[i], galaxys[j])

print(result)
print(input)

# Part 2
input = part2
print(input)
colDots = findDots(input.T)
rowDots = findDots(input)

print(colDots)
print(rowDots)

galaxys = []

for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        if input[i][j] == "#":
            galaxys.append([i, j])

def findPath2(start, end):
    dist = abs(start[0] - end[0]) + abs(start[1] - end[1])
    for r in rowDots:
        mi =  min(start[0], end[0])
        ma = max(start[0], end[0])
        if mi < r < ma:
            dist += factor - 1
    for c in colDots:
        mi =  min(start[1], end[1])
        ma = max(start[1], end[1])
        if mi < c < ma:
            dist += factor - 1
    return dist

result = 0

for i in range(0, len(galaxys)):
    for j in range(0, len(galaxys)):
        if i < j:
            result += findPath2(galaxys[i], galaxys[j])

print(result)
