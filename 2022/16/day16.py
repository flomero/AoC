import re
import networkx as nx
from itertools import combinations, permutations
import matplotlib.pyplot as plt

day = "16"
source = "test"
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

nonZeroValves = []
for v in valves:
    if valves[v]["rate"] > 0:
        nonZeroValves.append(v)

pairs = list(list(l) for l in combinations(nonZeroValves, 2))
for p in range(len(pairs)):
    l = len(nx.shortest_path(G, source=pairs[p][0], target=pairs[p][1])) - 1
    pairs[p].append(l)

start = "AA"
ways = list(list(i) for i in permutations(nonZeroValves))
for w in ways:
    print(w)

def checkWay(w):
    mins = len(nx.shortest_path(G, source="AA", target=w[0])) - 1
    while mins < 30:
        for p in range(len(w) - 1):
            



## plt.show()