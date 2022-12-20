import numpy as np
import matplotlib.pyplot as plt
import sys

day = "18"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

input = np.genfromtxt(file, dtype=int, delimiter=",")

dirs = np.array([[0,0,1], [0, 0,-1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]])

visible = 0

for i in input:
    for d in dirs:
        b = i + d
        if not np.any(np.all(input == b, axis=1)):
            visible += 1

partOne = visible
print(partOne)

max = np.amax(input, axis=0)
min = np.amin(input, axis=0)

x = max[0] + 1
y = max[1] + 1
z = max[2] + 1
map = np.zeros(shape=(x, y, z))

for i in input:
    x = i[0]
    y = i[1]
    z = i[2]
    map[x][y][z] = 1

start = np.array([0,0,0])

def checkNext(point):
    x = point[0]
    y = point[1]
    z = point[2]
    if map[x][y][z] == 1:
        return
    elif map[x][y][z] == 0:
        map[x][y][z] = 2
        for d in dirs:
            try:
                new = point + d
                checkNext(new)
            except:
                pass
        

np.set_printoptions(threshold=sys.maxsize)
checkNext(start)

faces = 0

air = zip(*np.where(map == 0))
for a in (list(a) for a in air):
    x = a[0]
    y = a[1]
    z = a[2]
    point = np.array([x,y,z])
    for d in dirs:
        b = point + d
        if np.any(np.all(input == b, axis=1)):
            faces += 1

partTwo = partOne - faces
print(partTwo)