import numpy as np

day = "04"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"
input = np.genfromtxt(file, delimiter = ",", dtype=str, unpack=False)

score = 0
score2 = 0

for line in input:
    a, b = map(int, line[0].split("-"))
    x, y = map(int, line[1].split("-"))

    ax = max(a, x)
    by = min(b, y)

    if ax == a and by == b or ax == x and by == y:
        score += 1
    if ax <= by:
        score2 += 1



print(score)
print(score2)


