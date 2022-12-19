import numpy as np
import matplotlib.pyplot as plt

day = "18"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

input = np.genfromtxt(file, dtype=int, delimiter=",")

dirs = np.array([[0,0,1], [0, 0,-1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]])

visible = 0

for i in input:
    for d in dirs:
        b = i + d
        if not np.any(np.all(input == b, axis=1)):
            visible += 1

print(visible)

max = np.amax(input, axis=0)

min = np.amin(input, axis=0)

x = max[0] + 1
y = max[1] + 1
z = max[2] + 1

print(x, y, z)

map = np.zeros(shape=(x, y, z))
print(map)

for i in input:
    map[np.array(i)] = 1
