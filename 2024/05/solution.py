from functools import cmp_to_key

day = "05"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2024/" + day + "/" + source + ".txt"

with open(file, "r") as f:
	data = f.read()

rules = data.split("\n\n")[0]
updates = data.split("\n\n")[1]
rules = [line.split('|') for line in rules.split("\n")]
updates =  [line.split(',') for line in updates.split("\n")]

def check_rules(row):
	for r,l in rules:
		if r in row and l in row:
			if row.index(r) > row.index(l):
				return False
	return True
	
solution = 0
for line in updates:
	if check_rules(line):
			solution += int(line[len(line)//2])
			# print(line, line[len(line)//2])

print(solution)

solution = 0

def apply_rule(x, y):
	for r,l in rules:
		if x == r and y == l:
			return 1
		if x == l and y == r:
			return -1
	return 0

solution = 0
for line in updates:
	if not check_rules(line):
			line = sorted(line, key=cmp_to_key(apply_rule))
			solution += int(line[len(line)//2])
			# print(line, line[len(line)//2])

print(solution)