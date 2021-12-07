import numpy as np

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/7/" + source + ".txt"
i = np.loadtxt(file, delimiter=",", dtype=int)
j = np.copy(i)

def steps(i, m):
    i[i == m] = -1
    i[i == 0] = m
    i[i == -1] = 0
    i[(i < m) & (i != 0)] = m - i[(i < m) & (i != 0)]
    i[i > m] = i[i > m] - m
    return i

m = np.median(i)
s = np.sum(steps(i, m))
print("First Part: " + str(s))

def g(n): return int((n * (1 + n))/2)

s2 = float("inf")

for p in range(min(j), max(j)):
    ab = [abs(p - n) for n in j]
    all = [g(n) for n in ab]
    s2 = min(s2, sum(all))

print("Second Part: " + str(s2))