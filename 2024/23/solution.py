from pprint import pprint
import pyperclip
from collections import defaultdict
from itertools import combinations

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "23"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	rawdata = f.read().splitlines()

connections = defaultdict(set)
for line in rawdata:
	a, b = line.split("-")
	connections[a].add(b)
	connections[b].add(a)

def findtrios(connections):
	trios = set()
	for node in connections:
		neighbors = connections[node]
		for a, b in combinations(neighbors, 2):
			if a in connections[b]:
				trios.add(tuple(sorted([node, a, b])))
	return trios

def filtertrios(trios):
	res = []
	for trio in trios:
		if any(c.startswith('t') for c in trio):
			res.append(trio)
	return res

trios = findtrios(connections)
trios = filtertrios(trios)

result = len(trios)

printc(result)

def isclique(group):
	for a in group:
		for b in group:
			if a != b and b not in connections[a]:
				return False
	return True

def largestclique(connections):
	def expand(potential, candidates, excluded):
		if not candidates and not excluded:
			return potential
		
		largest = potential
		for node in list(candidates):
			np = potential.copy()
			np.add(node)
			nc = candidates.copy()
			nc.intersection_update(connections[node])
			ne = excluded.copy()
			ne.intersection_update(connections[node])
			new = expand(np, nc, ne)
			if len(new) > len(largest):
				largest = new

			candidates.remove(node)
			excluded.add(node)

		return largest

	nodes = set(connections.keys())
	largest = expand(set(), nodes, set())
	return sorted(largest)

password = ",".join(largestclique(connections))
printc(password)
