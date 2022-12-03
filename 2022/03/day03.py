import numpy as np

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/03/" + source + ".txt"
input = np.genfromtxt(file, delimiter = "", dtype=str, unpack=False)

def getPrio(a: str):
    if a.isupper() == True:
        return (ord(a) - 64 + 26)
    else:
        return (ord(a)- 96)

sumPrios = 0

for line in input:
    firstpart = line[slice(0, len(line)//2)]
    secondpart =  line[slice(len(line)//2, len(line))]
   
    stack = ""
    for char in firstpart:
        if char in secondpart and char not in stack:
            sumPrios = sumPrios + getPrio(char)
            stack = stack + char

print("1: " + str(sumPrios))

sumPrios2 = 0

for a, b, c in zip(*[iter(input)]*3):
    stack = ""
    for char in a:
        if char in b and char in c and char not in stack:
            sumPrios2 = sumPrios2 + getPrio(char)
            stack = stack + char
            print(char + " --- " + str(getPrio(char)))

print("2: " + str(sumPrios2))