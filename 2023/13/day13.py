import pprint

day = "13"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

with open(file) as f:
    input = f.read()

input = input.split("\n\n")
input = [i.split("\n") for i in input]

result = 0

#pprint.pprint(input)

def transpose(arr):
    return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

def findReflection(arr):
    matches = []
    # find matching rows
    for i in range(len(arr)): 
        for j in range(len(arr)): 
            if i < j: 
                if arr[i] == arr[j]: 
                    matches.append((i+1,j+1))
    if len(matches) == 0:
        return 0
    if (len(arr)) not in [i[1] for i in matches] and 1 not in [i[0] for i in matches]:
        return 0
    if len(matches) == 1:
        return matches[0][0] + 1
    # find start
    start = (0,0)
    print(matches)
    for i in matches:
        if i[0] == 1 or i[1] == len(arr):
            start = i
    #print(start)
    #print(matches)
    # check continuity
    g = int((start[1] - start[0] -1) / 2)

    if g == 0:
        return 0
    #print(g)
    for x in range(1,g+1):
        print((start[0] + x, start[1] - x))
        if (start[0] + x, start[1] - x) not in matches:
            return 0
    return start[0] + g

for i in input:
    x = findReflection(i) * 100 + findReflection(transpose(i))
    print(x)
    result += x
    
print("Result: ")
print(result)