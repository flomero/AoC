from pprint import pprint
import pyperclip
import matplotlib.pyplot as plt
import re

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "19"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	rawdata = f.read().strip().split("\n")

patterns = rawdata[0].split(", ")
designs = rawdata[2:]

print(patterns)
print(designs)

def canmatch(r, memo={}):
		if r in memo:
			return memo[r]
		if not r:
			return True
		for p in patterns:
			if r.startswith(p):
				if canmatch(r[len(p):], memo):
					memo[r] = True
					return True
		memo[r] = False
		return False


result = 0

for design in designs:
	if canmatch(design):
		result += 1

printc(result)

# def findways(r, memo={}):
# 	if r in memo:
# 		return memo[r]
# 	if not r:
# 		return [[]]

# 	ways = []
# 	for p in patterns:
# 		if r.startswith(p):
# 			for way in findways(r[len(p):], memo):
# 				ways.append([p] + way)
# 	memo[r] = ways
# 	return ways

def findways(r, memo={}):
	if r in memo:
		return memo[r]
	if not r:
		return 1
	total = 0
	for p in patterns:
		if r.startswith(p):
			total += findways(r[len(p):], memo)
	memo[r] = total
	return total

result = 0

for design in designs:
	result += findways(design)

printc(result)