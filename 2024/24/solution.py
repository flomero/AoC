from pprint import pprint
import pyperclip
from collections import defaultdict
from itertools import combinations


def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "24"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	rawdata = f.read().splitlines()

initial = {}
gates = []

def compute_gate(gtype, a, b):
	if gtype == "AND":
		return a & b
	elif gtype == "OR":
		return a | b
	elif gtype == "XOR":
		return a ^ b
	return None

for line in rawdata:
	line = line.strip()
	if not line:
		continue

	if ":" in line:
		wire, value = line.split(": ")
		initial[wire] = int(value)

	else:
		parts = line.split(" ")
		a, gtype, b, _, output = parts
		gates.append((a, gtype, b, output))

wires = initial.copy()

while True:
	progress = False

	for a, gate_type, b, output in gates:
		if output in wires:
			continue

		if a in wires and b in wires:
			x = wires[a]
			y = wires[b]
			wires[output] = compute_gate(gate_type, x, y)
			progress = True

	if not progress:
		break

wires = dict(sorted(wires.items()))

for wire, value in wires.items():
	print(wire, value)

result = ''
for wire, value in wires.items():
	if wire.startswith("z"):
		result += str(value)

print(result)
#reverse string
result = result[::-1]
result = int(result, 2)

printc(result)
