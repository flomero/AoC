from pprint import pprint
import pyperclip
import re

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "14"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	rawdata = f.read().splitlines()

data = []
for line in rawdata:
	line = line.strip()
	parts = line.split() 
	position_part = parts[0][2:]
	velocity_part = parts[1][2:]
	px, py = map(int, position_part.split(','))
	vx, vy = map(int, velocity_part.split(','))
	data.append(((px, py), (vx, vy)))

pprint(data)

result = 0

maxseconds = 100
width = 101
height = 103

def robotswalk(data, width, height, seconds):
	grid = [[0 for _ in range(width)] for _ in range(height)]

	for ((px, py), (vx, vy)) in data:
		for _ in range(seconds):
			px = (px + vx) % width
			py = (py + vy) % height
		grid[py][px] += 1

	return grid

grid = robotswalk(data, width, height, maxseconds)
# pprint(grid)

def count_quadrants(grid):
	height = len(grid)
	width = len(grid[0])

	midx = width // 2
	midy = height // 2

	quadrants = [0, 0, 0, 0]

	for y in range(height):
		for x in range(width):
			if x == midx or y == midy:
				continue

			if x < midx and y < midy:
				quadrants[0] += grid[y][x]
			elif x >= midx and y < midy:
				quadrants[1] += grid[y][x]
			elif x < midx and y >= midy:
				quadrants[2] += grid[y][x]
			else:
				quadrants[3] += grid[y][x]

	return quadrants

def multiply(quadrants):
	factor = 1
	for count in quadrants:
		factor *= count
	return factor

quadrants = count_quadrants(grid)
pprint(quadrants)
result = multiply(quadrants)
printc(result)