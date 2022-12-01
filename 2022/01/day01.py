import numpy as np

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/01/" + source + ".txt"
input = np.genfromtxt(file, delimiter = "\n\n", dtype=int, unpack=False)

with open(file, "r") as f:
    data = f.read()
    data = data.split("\n")

first = 0
second = 0
third = 0
current = 0

for i in data:
    
    if i != '':
        current = current + int(i)
    else:
        if current > third:
            third = current
        if current > second:
            third = second
            second = current
        if current > first:
            second = first
            first = current

        current = 0

print("1.: " + str(first))
print("2.: " + str(second))
print("3.: " + str(third))
print("Sum:" + str(first + second +third))