from collections import defaultdict as ddict
import pprint

source = "test1"
file = "C:/Users/flofi/repos/CodeImAdvent/2021/12/" + source + ".txt"

with open(file, 'r') as f:
  input = f.read().splitlines()

caves = ddict(list)
for line in input:
    l = line.split("-")
    if l[1] != "start":
        caves[l[0]].append(l[1])
    if l[0] != "start":
        caves[l[1]].append(l[0])

pprint.pprint(dict(caves))

visited =[]
count = 0
path = "start"
queue = [path]


while queue:
    path = queue.pop(0)
    if path in visited:
        continue
    visited.append(path)
    last = path.split(",")[-1]

    for next in caves[last]:
        if next == "end":
            count = count + 1
            path = path + ",end"
            print(path)
            continue
        if next.islower() and next in path:
            continue
        queue.append(path + "," + next)

print(count)



