import json
from functools import cmp_to_key

day = "13"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

with open(file, 'r') as f:
  input = f.read().splitlines()
  input = [i for i in input if i]

def compare(left, right):
    if len(left) == 0 and len(right) != 0:
        return True
    for i in range(len(left)):
        if i > len(right) - 1:
            return False
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] == right[i]:
                continue
            else: 
                return left[i] < right[i]
        elif type(left[i]) == list and type(right[i]) == list:
            check = compare(left[i], right[i])
            if check == None:
                continue
            else:
                return check
        else:
            if type(left[i]) == list:
                r = [right[i]]
                check = compare(left[i], r)
                if check == None:
                    continue
                else:
                    return check
            elif type(right[i]) == list:
                l = [left[i]]
                check = compare(l, right[i])
                if check == None:
                    continue
                else:
                    return check
    if len(left) < len(right):
        return True
    return None

index = 0
indices = []

for i, (a, b) in enumerate(zip(input[::2], input[1::2])):
    a = json.loads(a)
    b = json.loads(b)
    if (compare(a, b)):
        indices.append(i+1)
    
partOne = sum(indices)
print(partOne)

start = "[[2]]"
end = "[[6]]"

input.append(start)
input.append(end)

for index, i in enumerate(input):
    input[index] = json.loads(i)

def sortKey(left, right):
    if compare(left, right):
        return -1
    else:
        return 1

sortedInput = sorted(input, key=cmp_to_key(sortKey))

a = 0
b = 0

for index, i in enumerate(sortedInput, 1):
    if i == json.loads(start):
        a = index
    elif i == json.loads(end):
        b = index

print(a*b)
