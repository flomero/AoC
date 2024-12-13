from pprint import pprint
import pyperclip
import re

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "13"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	rawdata = f.read().splitlines()

data = []
current_entry = []
pattern = re.compile(r"[-+]?\d+")
for line in rawdata:
	line = line.strip()
	if line:
		numbers = [int(num) for num in pattern.findall(line)]
		current_entry.append(numbers)
	else:
		if current_entry:
			data.append(current_entry)
			current_entry = []
if current_entry:
	data.append(current_entry)

def play(A, B, prize):
	ax, ay = A
	bx, by = B
	px, py = prize

	min_cost = float("inf")
	found = False
	for a in range(101):
		for b in range(101):
			current_x = a * ax + b * bx
			current_y = a * ay + b * by
			if current_x == px and current_y == py:
				found = True
				cost = 3 * a + b
				min_cost = min(min_cost, cost)

	return min_cost if found else 0

# Part 2
def play2(A, B, prize):
	ax, ay = A
	bx, by = B
	px, py = prize

	px = px + 10000000000000
	py = py + 10000000000000
	
	a = (px * by - py * bx) // (ax * by - ay * bx)
	b = (px * ay - py * ax) // (bx * ay - by * ax)

	if a * ax + b * bx == px and a * ay + b * by == py:
		return 3 * a + b
	return 0

result = 0
result2 = 0
for entry in data:
	A = tuple(entry[0])
	B = tuple(entry[1])
	prize = tuple(entry[2])
	result += play(A, B, prize)
	this = play2(A, B, prize)
	print(this)
	result2 += this

print('-----------')
printc(result)
printc(result2)