from pprint import pprint
import pyperclip
import matplotlib.pyplot as plt
import re

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "18"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	rawdata = f.read().strip().split("\n")
	data = [list(map(int, line.split(','))) for line in rawdata]

pprint(data)

result = 0
memorysize = 71
steps = 1024

def find_shortest_path(grid):
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	queue = [(0, 0, 0)]
	visited = set([(0, 0)])

	grid = [list(row) for row in grid]
	grid[memorysize-1][memorysize-1] = 'X'


	while queue:
		queue.sort(key=lambda x: x[2])
		x, y, steps = queue.pop(0)
		if grid[y][x] == '#':
			continue
		if grid[y][x] == 'X':
			for p in visited:
				grid[p[1]][p[0]] = 'O'
			return steps
		for dx, dy in directions:
			new_x, new_y = x + dx, y + dy
			if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and (new_x, new_y) not in visited:
				queue.append((new_x, new_y, steps + 1))
				visited.add((new_x, new_y))
	return -1

def run(data, size, steps):
	grid = [['.' for _ in range(size)] for _ in range(size)]
	i = 0
	for x, y in data[:steps]:
		grid[y][x] = '#'
		if i > 1000:
			path = find_shortest_path(grid)
			if path == -1:
				print('Result', x,y)
				return grid
		i += 1
		print(x,y)
	return grid

grid = run(data, memorysize, 3450)
# pprint(grid)

result = find_shortest_path(grid)
printc(result)
