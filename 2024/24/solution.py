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

def rev_gate(gate_type, output, a):
	if gate_type == "AND":
		return output & a
	elif gate_type == "OR":
		return output | a
	elif gate_type == "XOR":
		return output ^ a
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

expectedorder = ["XOR", "AND", "AND", "XOR", "OR"]
indexorder = 0

# sort wires by a
wires = dict(sorted(wires.items()))

while True:
	progress = False

	for a, gate_type, b, output in gates:
		if output in wires:
			continue

		if a in wires and b in wires:
			x = wires[a]
			y = wires[b]
			# check if right gate in order
			# if gate_type != expectedorder[indexorder % len(expectedorder)]:
			# 	print(a, b, output)
			print(a, b,  gate_type, output)
			wires[output] = compute_gate(gate_type, x, y)
			progress = True

	if not progress:
		break

wires = dict(sorted(wires.items()))

# for wire, value in wires.items():
# 	print(wire, value)

result = ''
for wire, value in wires.items():
	if wire.startswith("z"):
		result += str(value)

# print(result)
#reverse string
result = result[::-1]
result = int(result, 2)

printc(result)

# x = ''
# y = ''
# for wire, value in wires.items():
# 	if wire.startswith("x"):
# 		x += str(value)
# 	elif wire.startswith("y"):
# 		y += str(value)

# x = x[::-1]
# y = y[::-1]



# printc(x)
# printc(y)

# def wrong_bits(x, y, z):
# 	excepted = bin(x & y)[2:]
# 	wrong = []
# 	z = bin(z)[2:]
	
# 	z = z.zfill(len(excepted))
# 	print(excepted, int(excepted, 2))
# 	print(z, int(z, 2))
# 	for i in range(len(z)):
# 		if z[i] != excepted[i]:
# 			wrong.append(i)
# 	return wrong

# wrong = wrong_bits(x, y, result)
# printc(wrong)

