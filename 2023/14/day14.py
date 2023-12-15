import numpy as np

day = "14"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

result = 0
map = np.genfromtxt(file, dtype=str, delimiter=1, comments=None)
mapTwo = np.genfromtxt(file, dtype=str, delimiter=1, comments=None)
map = map.T 

def rollRocks(arr):
    for line in arr:
        # do until no more changes
        while True:
            changed = False
            for i in range(len(line)):
                if line[i] == 'O' and i > 0:
                    if line[i-1] == '.':
                        line[i-1] = 'O'
                        line[i] = '.'
                        changed = True
            if not changed:
                break

def rollRocksTwo(arr):
    for line in arr:
        # do until no more changes
        while True:
            changed = False
            #from right to left
            for i in range(len(line)-1, -1, -1):
                if line[i] == 'O' and i < len(line)-1:
                    if line[i+1] == '.':
                        line[i+1] = 'O'
                        line[i] = '.'
                        changed = True
            if not changed:
                break

rollRocks(map)

map = np.fliplr(map)

for line in map:
    for i in range(len(line)):
        if line[i] == 'O':
            result += i + 1

print(map)
print(result)

# Part 2

cycles = 1000000000
cycle = 0
result = 0
states = []
start = 0

while cycle < cycles:
    print(cycle)
    for i in range(4):
        mapTwo = np.rot90(mapTwo, -1)
        rollRocksTwo(mapTwo)
    if any((mapTwo == x).all() for x in states):
        print("Found a cycle")
        print(cycle)
        for i, s in enumerate(states):
            if (mapTwo == s).all():
                print("Found the same state")
                print(i)
                start = i
        break
    else:
        states.append(mapTwo.copy())
    cycle += 1

cycleLength = cycle - start
remaining = cycles - cycle - 1
remaining = remaining % cycleLength

for i in range(remaining):
    for i in range(4):
        mapTwo = np.rot90(mapTwo, -1)
        rollRocksTwo(mapTwo)


mapTwo = mapTwo.T
mapTwo = np.fliplr(mapTwo)

for line in mapTwo:
    for i in range(len(line)):
        if line[i] == 'O':
            result += i + 1
    
print(mapTwo)
print(result)

