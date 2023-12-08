import pprint
import re
from math import lcm

day = "08"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"
# only needed for the different test cases
part = 1

start = "AAA"
end = "ZZZ"
instructions = ""
nodes = {}


with open(file, "r") as f:
    input = f.readlines()
    instructions = input[0].strip()
    for line in input[2:]:
        node = re.findall(r'\w+', line.strip())
        nodes[node[0]] = [node[1], node[2]]

current = start
steps = 0

instructions = instructions.replace("R", "1").replace("L", "0")
i = instructions

# Part 1
if part == 1:
    while current != end:
        if len(i) == 0:
            i += instructions
        current = nodes[current][int(i[0])]
        i = i[1:]
        steps += 1

print(steps)

# Part 2
starts = []
steps = 0

for node in nodes.keys():
    if node[-1] == "A":
        starts.append(node)

paths = {i: { "current": i, "first": 0, "second": 0 } for i in starts}

for path in paths:
    steps = 0
    i = instructions
    while True:
        if len(i) == 0:
                i += instructions

        current = paths[path]["current"]
        paths[path]["current"] =  nodes[current][int(i[0])]
        steps += 1
        i = i[1:]
        if paths[path]["current"][-1] == "Z":
            if paths[path]["first"] == 0:
                paths[path]["first"] = steps
            else:
                paths[path]["second"] = steps
        if paths[path]["second"] != 0:
            break

circles = [int(paths[path]["first"]) for path in paths]
result = lcm(*circles)
print(result)