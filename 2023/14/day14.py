import numpy as np

day = "14"
source = "test"
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

rollRocks(map)

map = np.fliplr(map)

for line in map:
    for i in range(len(line)):
        if line[i] == 'O':
            result += i + 1

print(map)
print(result)

# Part 2

cycles = 3
cycle = 0
result = 0


    
