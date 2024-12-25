from pprint import pprint
import pyperclip
import numpy as np
from itertools import product

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "25"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	rawdata = f.read().splitlines()

data = []
for i in range(0, len(rawdata), 8):
	data.append(rawdata[i:i+7])

pprint(data)

def parse(data):
	parsed = []
	for d in data:
		parsed.append(np.array([[1 if c == "#" else 0 for c in line] for line in d]))
	return parsed

data = parse(data)

pprint(data)

def check(data):
	result = 0
	for i in range(len(data)):
		for j in range(i+1, len(data)):
			new = data[i] + data[j]
			if not np.any(new == 2):
				result += 1
	return result

printc(check(data))