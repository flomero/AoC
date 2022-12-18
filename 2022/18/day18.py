import numpy as np

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

print(visible)