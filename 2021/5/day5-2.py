import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt




source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/5/" + source + ".txt"
input = np.loadtxt(file, delimiter=" -> ", dtype=str)


if source == "test":
    size = 10
else:
    size = 1000

map = np.array([[0] * size]*size)

def csplit(i):
    one = i[0]
    two = i[1]
    one = one.split(",")
    two = two.split(",")
    return [one, two]

def x1(i):
    return int(csplit(i)[0][0])
def y1(i):
    return int(csplit(i)[0][1])
def x2(i):
    return int(csplit(i)[1][0])
def y2(i):
    return int(csplit(i)[1][1])

def start(i, j):
    if i > j:
        return [int(j),int(i)]
    else:
        return [int(i),int(j)]

for i in input:
    if y1(i) == y2(i):
        s = start(x1(i), x2(i))[0]
        e = start(x1(i), x2(i))[1]
        for j in range(s, e + 1):
            map[y1(i), j] = map[y1(i), j] + 1
    elif x1(i) == x2(i):
        s = start(y1(i), y2(i))[0]
        e = start(y1(i), y2(i))[1]
        for j in range(s, e + 1):
            map[j, x1(i)] = map[j, x1(i)] + 1
    else:
        if x1(i) < x2(i):
            length = x2(i) - x1(i) + 1
            count = 0
            if y1(i) < y2(i):
                while count < length:
                    map[y1(i) + count, x1(i) + count] = map[y1(i) + count, x1(i) + count] + 1
                    count += 1
            else:
                while count < length:
                    map[y1(i) - count, x1(i) + count] = map[y1(i) - count, x1(i) + count] + 1
                    count += 1
        else:
            length = x1(i) - x2(i) + 1
            count = 0
            if y1(i) < y2(i):
                while count < length:
                    map[y1(i) + count, x1(i) - count] = map[y1(i) + count, x1(i) - count] + 1
                    count += 1
            else:
                while count < length:
                    map[y1(i) - count, x1(i) - count] = map[y1(i) - count, x1(i) - count] + 1
                    count += 1


print(map) 
print(np.count_nonzero(map > 1))

plt.imshow(map)
plt.colorbar()
plt.axis('off')
plt.show()