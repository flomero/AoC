from pprint import pprint
import numpy as np

day = "10"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"

result = 0

with open(file, "r") as f:
	data = f.read()

map_data = np.array([[int(digit) for digit in line] for line in data.splitlines() if line.strip()])

print(map_data)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid_move(map_data, x, y, height):
	return (
		0 <= x < map_data.shape[0]
		and 0 <= y < map_data.shape[1]
		and map_data[x, y] == height + 1
	)

trailheads = np.argwhere(map_data == 0)
scores = {}

part = 1
for trailhead in trailheads:
	start_x, start_y = trailhead
	visited = set()
	stack = [(start_x, start_y)]
	nines = []

	while stack:
		x, y = stack.pop()
		if part == 1 and (x, y) in visited:
			continue
		visited.add((x, y))
		if map_data[x, y] == 9:
			nines.append((x, y))
			continue
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if is_valid_move(map_data, nx, ny, map_data[x, y]):
				stack.append((nx, ny))

	scores[(start_x, start_y)] = len(nines)

print(scores)
result = sum(scores.values())
print(result)

# Part 2
# def distinct(map, x, y):
# 	if map[x, y] == 9:
# 		return 1
# 	trails = 0
# 	for dx, dy in directions:
# 		nx, ny = x + dx, y + dy
# 		if is_valid_move(map_data, nx, ny, map_data[x, y]):
# 			trails += distinct(map_data, nx, ny)
# 	return trails

# result = 0

# for trailhead in trailheads:
# 	x, y = trailhead
# 	result += distinct(map_data, x, y)

# print(result)