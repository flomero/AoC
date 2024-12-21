from pprint import pprint
import pyperclip
from collections import deque

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "20"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	rawdata = f.read().splitlines()

grid = {}
for row, line in enumerate(rawdata):
	for col, char in enumerate(line):
		grid[(row, col)] = char
		if char == 'S':
			start = (row, col)
		elif char == 'E':
			end = (row, col)

directions = ((1,0),(-1,0),(0,1),(0,-1))

def bfs(start):
	dist_map = {start: 0}
	queue = deque([start])
	
	while queue:
		r, c = queue.popleft()
		d = dist_map[(r, c)]
		
		for dr, dc in directions:
			nr, nc = r + dr, c + dc
			if (nr, nc) not in dist_map and grid.get((nr, nc)) != '#':
				queue.append((nr, nc))
				dist_map[(nr, nc)] = d + 1
				
	return dist_map
	
lengthmap = bfs(start)
# pprint(lengthmap)

cheats = {}
for (row, col), dist in lengthmap.items():
	for dr, dc in directions:
		nr = row + 2 * dr
		nc = col + 2 * dc
		if (nr, nc) in lengthmap and lengthmap[(nr, nc)] < dist:
			saved = dist - lengthmap[(nr, nc)] - 2
			if saved > 0:
				cheats[((row, col), (nr, nc))] = saved

def getresult(cheats):
	result = 0
	for saved in cheats.values():
		if saved >= 100:
			result += 1
	return result

print(getresult(cheats))

cheats = {}
max_distance = 20
for (row, col), dist in lengthmap.items():
	for dr in range(-max_distance, max_distance + 1):
		for dc in range(-max_distance, max_distance + 1):
			adr = abs(dr)
			adc = abs(dc)
			if adr + adc <= max_distance:
				nr = row + dr
				nc = col + dc
				if (nr, nc) in lengthmap and lengthmap[(nr, nc)] < dist:
					saved = dist - lengthmap[(nr, nc)] - adr - adc
					if saved > 0:
						cheats[((row, col), (nr, nc))] = saved

print(getresult(cheats))

# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# def bfs_from_goal(racetrack, start, end):
# 	distance_grid = [[float('inf')] * cols for _ in range(rows)]
# 	queue = deque([(end, 0)])
# 	distance_grid[end[0]][end[1]] = 0
	
# 	while queue:
# 		(r, c), dist = queue.popleft()
		
# 		for dr, dc in directions:
# 			nr, nc = r + dr, c + dc
			
# 			if 0 <= nr < rows and 0 <= nc < cols:
# 				# If we found a shorter path, update the grid and add to queue
# 				if distance_grid[nr][nc] > dist + 1 and racetrack[nr][nc] != '#':
# 					distance_grid[nr][nc] = dist + 1
# 					queue.append(((nr, nc), dist + 1))
	
# 	return distance_grid

# grid = bfs_from_goal(racetrack, start, end)
# pprint(grid)



# times = []
# for r in range(rows):
# 	for c in range(cols):
# 		copy = [row[:] for row in racetrack]
# 		if racetrack[r][c] == "#":
# 			racetrack[r][c] = "."
# 			if racetrack[r+1][c] == "#":
# 				racetrack[r+1][c] = "."
# 			elif racetrack[r][c+1] == "#":
# 				racetrack[r][c+1] = "."


