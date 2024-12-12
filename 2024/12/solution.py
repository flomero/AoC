from pprint import pprint
from collections import deque
import pyperclip

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "12"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"

with open(file, "r") as f:
	data = f.read().splitlines()

data = [list(line.strip()) for line in data]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dir_90_clockwise(dx, dy):
	if dx == 0 and dy == 1:
		return 1, 0
	elif dx == 1 and dy == 0:
		return 0, -1
	elif dx == 0 and dy == -1:
		return -1, 0
	elif dx == -1 and dy == 0:
		return 0, 1

def find_region(data, start, visited):
	queue = deque([start])
	visited.add(start)
	region_cells = []
	perimeter = 0
	plant_type = data[start[0]][start[1]]
	sides = set()

	while queue:
		x, y = queue.popleft()
		region_cells.append((x, y))

		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[0]) or data[nx][ny] != plant_type:
				sides.add((x, y, dx, dy))
				perimeter += 1
			elif (nx, ny) not in visited:
				visited.add((nx, ny))
				queue.append((nx, ny))

	side_adj = 0
	for (x, y, dx, dy) in sides:
		dir = dir_90_clockwise(dx, dy)
		nx, ny = x + dir[0], y + dir[1]
		if (nx, ny, dx, dy) in sides:
			side_adj -= 1

	area = len(region_cells)
	edges = len(sides) + side_adj
	return plant_type, area, perimeter, edges

visited = set()
total_price = 0
total_edge_price = 0

for i in range(len(data)):
	for j in range(len(data[0])):
		if (i, j) not in visited:
			plant_type, area, perimeter, edges = find_region(data, (i, j), visited)
			price = area * perimeter
			print(plant_type, area, perimeter, edges, price)
			total_price += price
			total_edge_price += area * edges

printc(total_price)
printc(total_edge_price)