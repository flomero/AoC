from collections import defaultdict as ddict
import pprint

source = "data"
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
            print(path)
            continue
        if next.islower() and next in path and path[0] == "2":
            continue

        queue.append(("2" if next.islower() and next in path else "") + path + "," + next)

print(count)







