from pprint import pprint
import pyperclip
import matplotlib.pyplot as plt

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "16"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	data = f.read().strip().split("\n")
	start, end = None, None
	for y, row in enumerate(data):
		for x, char in enumerate(row):
			if char == 'S':
				start = (x, y)
			elif char == 'E':
				end = (x, y)

print(start, end)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
width = len(data[0])
height = len(data)

def solve(maze, start, end):
	queue = [(0, 0, start[0], start[1], 0)]
	visited = set()

	while queue:
		queue.sort(key=lambda x: x[0])
		total, current, x, y, curdir = queue.pop(0)

		if (x, y, curdir) in visited:
			continue
		visited.add((x, y, curdir))

		if (x, y) == end:
			return total

		for newdir, (dx, dy) in enumerate(directions):
			nx = x + dx
			ny = y + dy

			if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] != '#':
				if newdir != curdir:
					cost = 1000 
				else:
					cost = 0

				queue.append((
					current + 1 + cost,
					current + 1 + cost,
					nx, ny, newdir
				))

printc(solve(data, start, end))


def solve2(maze, start, end):
	queue = [(0, 0, start[0], start[1], 0, [(start[0], start[1])])]
	visited = {}
	paths = []
	score = float('inf')

	while queue:
		queue.sort(key=lambda x: x[0])
		total, current, x, y, curdir, path = queue.pop(0)

		if (x, y, curdir) in visited and visited[(x, y, curdir)] < total:
			continue
		visited[(x, y, curdir)] = total

		if (x, y) == end:
			if total < score:
				score = total
				paths = [path]
			elif total == score:
				paths.append(path)
			continue

		for newdir, (dx, dy) in enumerate(directions):
			nx = x + dx
			ny = y + dy

			if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] != '#':
				if newdir != curdir:
					cost = 1000 
				else:
					cost = 0

				queue.append((
					current + 1 + cost,
					current + 1 + cost,
					nx, ny, newdir,
					path + [(nx, ny)]
				))
	return paths


def mark_path(maze, path):
	for x, y in path:
		maze[y] = maze[y][:x] + 'X' + maze[y][x + 1:]

paths = solve2(data, start, end)

for path in paths:
	mark_path(data, path)

result = 0
for row in data:
	result += row.count('X')


# print(len(paths))
# pprint(data)
printc(result)

# convert to numeric 2d array
maze = []
for row in data:
	maze.append([])
	for char in row:
		if char == '#':
			maze[-1].append(1)
		elif char == 'X':
			maze[-1].append(2)
		else:
			maze[-1].append(0)

# hide all axes
plt.axis('off')
plt.imshow(maze)
plt.savefig(f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/viz.png", bbox_inches='tight', pad_inches=0, dpi=300)