import numpy as np

source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/10/" + source + ".txt"

with open(file, 'r') as f:
  input = f.read().splitlines()

added = []
pairs = {
    ')':'(',
    ']':'[',
    '}':'{',
    '>':'<'
}

inv_pair = {v: k for k, v in pairs.items()}

points = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

results = []

for i in input:
    current = []
    check = False
    for x in i:
        if x in pairs.keys():
            if len(current) == 0:
                check = True                
                break
            last = current.pop()
            if last != pairs[x]:
                check = True
                break
        else:
            current.append(x)
    if check:
        continue
    
    result = 0
    for c in reversed(current):
        result = (result*5) + points[inv_pair[c]]
    results.append(result)
        

print(np.median(results))

