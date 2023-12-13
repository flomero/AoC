import pprint

day = "13"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

with open(file) as f:
    input = f.read()

input = input.split("\n\n")
input = [i.split("\n") for i in input]

pprint.pprint(input)

def getReflection(map):
    matches = []
    for i in range(len(map)):
        for j in range(len(map)):
            if i == j:
                continue
            if map[i] == map[j]:
                matches.append(i)
                matches.append(j)
    return matches

def transpose(map):
    # change rows to columns
    return ["".join([map[i][j] for i in range(len(map))]) for j in range(len(map))]
    

for map in input:
    pprint.pprint(map)
    pprint.pprint(transpose(map))
    vertical = getReflection(map)
    horizontal = getReflection(transpose(map))
    print(horizontal)
    print(vertical)
    if len(map) in horizontal and len(map) - 1 in horizontal:
        print("horizontal")
    elif 0 in vertical and 1 in vertical:
        print("horizontal")
    
    if len(transpose(map)) in vertical and len(transpose(map)) - 1 in vertical:
        print("vertical")
    elif 0 in horizontal and 1 in horizontal:
        print("vertical")