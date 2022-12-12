import numpy as np
from queue import PriorityQueue

day = "12"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

input = np.genfromtxt(file, delimiter=1, dtype=str)

start = np.where(input == "S")
end = np.where(input == "E")

characters = 'abcdefghijklmnopqrstuvwxyz'
elevation = {}
for x in range(len(characters)):
    elevation[characters[x]] = x+1
elevation["E"] = 26
elevation["S"] = 1

def findPath(start):
    global elevation
    height = len(input)
    length = len(input[0])
    visited = set(start)
    queue = [(int(start[0]), int(start[1]), int(0))]

    while queue:
        x, y, steps = queue[0]
        if len(queue) > 1:  queue = queue[1:]
        else: queue = []

        if input[x, y] == "E":
            return steps

        for i, j in [(x+1, y), (x-1,y), (x, y+1), (x, y-1)]:
            if 0 <= i < height and 0 <= j < length:
                if (i, j) not in visited and elevation[input[i, j]] - elevation[input[x, y]] <= 1:
                    visited.add((i, j))
                    queue.append((i, j, steps +1)) 

partOne = findPath((start[0][0], start[1][0]))
print(partOne)

pathLengths = np.array([partOne])
startingPoints = np.where(input == "a")
for p in range(len(startingPoints[0])):
    l = findPath((startingPoints[0][p], startingPoints[1][p]))
    if l:
        pathLengths = np.append(pathLengths, l)

partTwo = np.amin(pathLengths)
print(partTwo)
