from pprint import pprint
import pyperclip
import matplotlib.pyplot as plt
import re

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "17"
source = "data"
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

def combo(op, reg):
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

def runprogram(program, reg, a=None):
	outputs = []
	i = 0
	reg = reg.copy()
	if a is not None:
		reg['A'] = a
	while i < len(program):
		opcode = program[i]
		operand = program[i + 1] if i + 1 < len(program) else 0

		if opcode == 0:
			reg['A'] = reg['A'] // 2 ** combo(operand, reg)
		elif opcode == 1:
			reg['B'] ^= operand
		elif opcode == 2:
			reg['B'] = combo(operand, reg) % 8
		elif opcode == 3:
			if reg['A'] != 0:
				i = operand
				continue
		elif opcode == 4:
			reg['B'] ^= reg['C']
		elif opcode == 5:
			outputs.append(combo(operand, reg) % 8)
		elif opcode == 6:
			reg['B'] = reg['A'] // (2 ** combo(operand, reg))
		elif opcode == 7:
			reg['C'] = reg['A'] // (2 ** combo(operand, reg))

		i += 2
	return outputs

outputs = runprogram(program, reg)

result = ",".join(map(str, outputs))

printc(result)


#part 2
reg = {'A': 0, 'B': regB, 'C': regC}

def recursive(program, output, reg, index, a, off=0):
	if index < 0:
		return a

	print(index)
	output_value = output[index]

	for new in range(8):
		testa = (a << 3) + new
		regs = reg.copy()
		regs['A'] = testa
		
		out = runprogram(program, regs)

		if out == output[index:]:
			print(out, output_value, testa)
			res = recursive(program, output, regs, index - 1, testa, off + 1)
			if res is not None:
				return res
	
	return None

result = recursive(program, program, reg, len(program) - 1, 0)
printc(result)
