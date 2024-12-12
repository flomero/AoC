from pprint import pprint
from collections import deque
import pyperclip
from collections import defaultdict

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

def find_region(data, start, visited):
	queue = deque([start])
	visited.add(start)
	region_cells = []
	perimeter = 0
	plant_type = data[start[0]][start[1]]

	while queue:
		x, y = queue.popleft()
		region_cells.append((x, y))
		
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			
			if nx < 0 or ny < 0 or nx >= len(data) or ny >= len(data[0]):
				perimeter += 1
				
			elif (nx, ny) in visited and data[nx][ny] != plant_type:
				perimeter += 1
			elif (nx, ny) not in visited:
				if data[nx][ny] == plant_type:
					visited.add((nx, ny))
					queue.append((nx, ny))
				else:
					perimeter += 1

	area = len(region_cells)
	return plant_type, area, perimeter

visited = set()
total_price = 0

for i in range(len(data)):
	for j in range(len(data[0])):
		if (i, j) not in visited:
			plant_type, area, perimeter = find_region(data, (i, j), visited)
			price = area * perimeter
			print(plant_type, area, perimeter, price)
			total_price += price

printc(total_price)


