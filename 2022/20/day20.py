import numpy as np

day = "20"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

input = np.genfromtxt(file, delimiter="\n", dtype=int)
print(input)