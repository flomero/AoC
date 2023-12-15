import pprint


day = "15"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

input = ""
result = 0

with open(file) as f:
    input = f.read()

input = input.split(",")

def hash(str):
    value = 0
    for i in str: 
        value += ord(i)
        value *= 17
        value %= 256
    return value

for i in input: 
    value = hash(i)
    result += value

print(result)

# Part 2
boxes = {i:[] for i in range(256)}

for i in input: 
    if "=" in i: 
        l,f = i.split("=")
        lens = (l, int(f))
        labels = [x[0] for x in boxes[hash(l)]]
        if l not in labels:
            boxes[hash(l)].append(lens)
        else:
            for x in boxes[hash(l)]: 
                if x[0] == l: 
                    boxes[hash(l)][boxes[hash(l)].index(x)] = lens
    elif "-" in i: 
        l = i.split("-")[0]
        box = hash(l)
        labels = [x[0] for x in boxes[box]]
        if l in labels: 
            for x in boxes[box]: 
                if x[0] == l: 
                    boxes[box].remove(x)

focusPower = 0
for box in boxes: 
    for index, lens in enumerate(boxes[box]): 
        power = (index + 1) * (box + 1) * lens[1]
        focusPower += power

print(focusPower)
        
