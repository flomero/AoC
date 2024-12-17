from pprint import pprint
import pyperclip
import matplotlib.pyplot as plt
import re

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "17"
source = "test"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	data = f.read().strip().split("\n")

regA = int(data[0].split(" ")[2])
regB = int(data[1].split(" ")[2])
regC = int(data[2].split(" ")[2])

program = data[4].split(" ")[1].split(",")
program = [int(x) for x in program]

pprint(regA)
pprint(regB)
pprint(regC)
pprint(program)

reg = {'A': regA, 'B': regB, 'C': regC}
outputs = []
i = 0

def combo(op):
	if op <= 3:
		return op
	elif op == 4:
		return reg['A']
	elif op == 5:
		return reg['B']
	elif op == 6:
		return reg['C']
	else:
		raise ValueError

while i < len(program):
	opcode = program[i]
	operand = program[i + 1] if i + 1 < len(program) else 0

	if opcode == 0:
		reg['A'] = reg['A'] // 2 ** combo(operand)
	elif opcode == 1:
		reg['B'] ^= operand
	elif opcode == 2:
		reg['B'] = combo(operand) % 8
	elif opcode == 3:
		if reg['A'] != 0:
			i = operand
			continue
	elif opcode == 4:
		reg['B'] ^= reg['C']
	elif opcode == 5:
		outputs.append(combo(operand) % 8)
	elif opcode == 6:
		reg['B'] = reg['A'] // (2 ** combo(operand))
	elif opcode == 7:
		reg['C'] = reg['A'] // (2 ** combo(operand))

	i += 2

result = ",".join(map(str, outputs))

printc(result)