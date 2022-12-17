import re
import networkx as nx
from itertools import combinations, permutations
import matplotlib.pyplot as plt

day = "16"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

valves = {}

def parseLine(line):
    valve = ((re.search(r' [A-Z]{2} ', line)).group(0)).strip()  # type: ignore
    rate = int((re.search(r'[0-9]+', line)).group(0))  # type: ignore
    tunnels = ((re.search(r'([A-Z]{2})+(?:, [A-Z]{2})*$', line)).group(0)).split(", ")  # type: ignore
    entry = {
        "rate": rate,
        "tunnels": tunnels
    }
    valves[valve] = entry

with open(file, "r") as f:
    for line in f:
        parseLine(line)

visited = set()
G = nx.Graph()
for v in valves:
    G.add_node(v)
for v in valves:
    if v not in visited:
        for t in valves[v]["tunnels"]:
            G.add_edge(v, t)

nx.draw(G, with_labels=True)

print("graph donw")

nonZeroValves = []
for v in valves:
    if valves[v]["rate"] > 0:
        nonZeroValves.append(v)

print("nzv done")

paths = [list(i) for i in combinations(nonZeroValves, 2)]
connections = {}
for p in paths:
    left = p[0]
    right = p[1]
    length = len(nx.shortest_path(G, source=left, target=right))
    connections[str(left + right)] = length
    connections[str(right + left)] = length

ways = []

## def checkSeq(seq: list, count: int):
##     global ways
##     for p in nonZeroValves:
##         if len(seq) == len(nonZeroValves):
##             ways.append(seq)
##             break 
##         if p not in seq:
##             count += connections[str(seq[-1] + p)]
##             if count > 30:
##                 ways.append(seq)
##                 break 
##             seq.append(p)
##             checkSeq(seq, count)

## for p in nonZeroValves:
##    checkSeq([p], 0)



## print(len(ways))
## 
## print("ways done")

def checkWay(w: list):
    mins = len(nx.shortest_path(G, source="AA", target=w[0]))
    openValves = list()
    flow = 0
    for p in range(len(w)):
        mins += 1
        openValves.append(int(valves[w[p]]["rate"]))
        flow = flow + sum(openValves)
        ## print(mins, flow, sum(openValves))
        if mins == 30: break
        if (p+1) <= len(w) - 1:
            way = len(nx.shortest_path(G, source=w[p], target=w[p+1])) - 1
            for _ in range(way):
                mins += 1
                flow = flow + sum(openValves)
                if mins == 30: break
                ## print(mins, flow, sum(openValves))
        if p == len(w)-1:
            while True:
                mins += 1
                flow = flow + sum(openValves)
                ## print(mins, flow, sum(openValves))
                if mins == 30: break 
        if mins == 30: break 
        ## print(sum(openValves))
    return flow
partOne = 0
## for w in ways:
##     score = checkWay(w)
##     if score > partOne:
##         partOne = score
## 
## print(partOne)
## 
## 
## plt.show()
iterator = permutations(nonZeroValves)

test = 0
res = 0

for it in iterator:
    count = 0
    for i in range(1, len(it)):
        count += connections[str(it[i] + it[i-1])]
    if count <= 30:
        way = checkWay(list(it))
        test += 1
        print(test)
        if way > res:
            res = way


print(res)