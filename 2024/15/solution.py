from pprint import pprint
import pyperclip
import matplotlib.pyplot as plt
import math
import numpy as np

import sys
sys.setrecursionlimit(10000)

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "15"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 2

with open(file, "r") as f:
	rawdata = f.read().splitlines()

map = []
movements = ''
map_lines = []
move_lines = []
for line in rawdata:
	if line.startswith('#'):
		map_lines.append(line)
	else:
		move_lines.append(line)
map = [list(line) for line in map_lines]

movements = ''.join(move_lines)

pprint(map)
pprint(movements)


directions = {
	'^': (-1, 0),
	'v': (1, 0),
	'<': (0, -1),
	'>': (0, 1)
}

def movebox(map, r, c, dr, dc):
	nextr, nextc = r + dr, c + dc
	if not (0 <= nextr < rows and 0 <= nextc < cols):
		return False
	if map[nextr, nextc] == '.':
		map[nextr, nextc] = 'O'
		map[r, c] = '.'
		return True
	elif map[nextr, nextc] == 'O':
		if movebox(map, nextr, nextc, dr, dc):
			map[nextr, nextc] = 'O'
			map[r, c] = '.'
			return True
	return False

map = np.array(map)
start_pos = np.where(map == '@')
start_pos = (start_pos[0][0], start_pos[1][0])
rows, cols = map.shape
if part == 1:
	for possible in movements:
		# print(map)
		print(possible)
		dr, dc = directions[possible]
		nextr, nextc = start_pos[0] + dr, start_pos[1] + dc
		if not (0 <= nextr < rows and 0 <= nextc < cols):
			continue
		target = map[nextr, nextc]
		if target == '#':
			continue
		elif target == '.':
			map[start_pos] = '.'
			map[nextr, nextc] = '@'
			start_pos = (nextr, nextc)
		elif target == 'O':
			box_nextr, box_nextc = nextr + dr, nextc + dc
			if movebox(map, nextr, nextc, dr, dc):
				map[start_pos] = '.'
				map[nextr, nextc] = '@'
				start_pos = (nextr, nextc)
	result = 0
	for r in range(rows):
		for c in range(cols):
			if map[r,c] == 'O':
				result += 100 * r + c

	pprint(map)
	printc(result)

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation



# Part 2
resized_map = []
for row in map:
	resized_row = []
	for tile in row:
		if tile == '#':
			resized_row.extend(['#', '#'])
		elif tile == '.':
			resized_row.extend(['.', '.'])
		elif tile == 'O':
			resized_row.extend(['[', ']'])
		elif tile == '@':
			resized_row.extend(['@', '.'])
	resized_map.append(resized_row)
resized_map = np.array(resized_map)

viz = 1
if viz:
	frames = []

rows, cols = resized_map.shape
start_pos = np.where(resized_map == '@')
start_pos = (start_pos[0][0], start_pos[1][0])
resized_map[start_pos] = '.'

tile_numeric = {
	'#': 1,  # Wall
	'.': 0,  # Floor
	'O': 3,  # Box
	'@': 4,  # Player
	'[': 3,  # Box part
	']': 3   # Box part
}

i = 1000

def findnew(map, maybe, dr, dc):
	new = set()
	for pr, pc in maybe:
		newpoint = (pr + dr, pc + dc)

		if dr != 0:
			if map[newpoint] == '[':
				new.add(newpoint)
				new.add((newpoint[0], newpoint[1] + 1))
			elif map[newpoint] == ']':
				new.add(newpoint)
				new.add((newpoint[0], newpoint[1] - 1))
		elif map[newpoint] in ['[', ']']:
			new.add(newpoint)
	return new

for moves in movements:
	# print(resized_map)
	maybe = []
	maybe.append(start_pos)
	possible = []

	dr, dc = directions[moves]

	while True:
		if any(resized_map[point[0] + dr, point[1] + dc] == '#' for point in maybe):
			possible = None
			break
		if all(resized_map[point[0] + dr, point[1] + dc] == '.' for point in maybe):
			break

		new = findnew(resized_map, maybe, dr, dc)
		# print(new)
		maybe = new
		for point in new:
			possible.append((point, resized_map[point]))

	if possible is not None:
		# print(possible)
		start_pos = (start_pos[0] + dr, start_pos[1] + dc)
		for point, c in possible:
			resized_map[point] = '.'
		for point, c in possible:
			pr, pc = point
			resized_map[pr + dr, pc + dc] = c
	
	if viz and i > 0:
		numeric_map = np.array([[tile_numeric[tile] for tile in row] for row in resized_map])
		numeric_map[start_pos] = 10
		frames.append(numeric_map)
		i -= 1

def animate(i):
	current_frame = frames[i]
	im.set_data(current_frame)
	return [im]

if viz:
	fig, ax = plt.subplots()
	ax.set_xticks([])
	ax.set_yticks([])
	im = ax.imshow(np.full(resized_map.shape, fill_value=0), cmap='tab20', norm=mcolors.Normalize(vmin=0, vmax=10))
	anim = FuncAnimation(fig, animate, frames=len(frames), interval=50)
	anim.save("C:/Users/flofi/repos/CodeImAdvent/2024/15/animation.gif")

result = 0
for r in range(rows):
	for c in range(cols):
		if resized_map[r,c] == '[':
			result += 100 * r + c

print(resized_map)
printc(result)




















# player = np.where(resized_map == '@')
# left_boxes = np.where(resized_map == '[')
# walls = np.where(resized_map == '#')

# player_pos = (player[0][0], player[1][0])
# boxes = set([(left_boxes[0][i], left_boxes[1][i]) for i in range(len(left_boxes[0]))])
# walls = set([(walls[0][i], walls[1][i]) for i in range(len(walls[0]))])

# def move_box(box, direction, boxes, walls):
# 	dr, dc = directions[direction]
# 	r, c = box
# 	new_box = (r + dr, c + dc)
	
# 	if (new_box[0], new_box[1]) in walls or (new_box[0], new_box[1] + 1) in walls:
# 		return False
		
# 	if any((new_box[0], new_box[1] + i) in boxes for i in [0, 1]):
# 		return False
		
# 	boxes.remove(box)
# 	boxes.add(new_box)
# 	return True

# def move_robot(pos, boxes, walls, direction):
# 	dr, dc = directions[direction]
# 	new_pos = (pos[0] + dr, pos[1] + dc)
	
# 	for box in boxes:
# 		if new_pos == box or new_pos == (box[0], box[1] + 1):
# 			if move_box(box, direction, boxes, walls):
# 				return new_pos, boxes
# 			return pos, boxes
			
# 	if new_pos not in walls:# 		return new_pos, boxes
		
# 	return pos, boxes

# def simulate_movements(pos, boxes, walls, movements):
# 	for move in movements:
# 		pos, boxes = move_robot(pos, boxes, walls, move)
# 	return pos, boxes

# def calculate_gps(boxes):
# 	result = 0
# 	for box in boxes:
# 		top_distance = box[0]
# 		left_distance = box[1]
# 		result += 100 * top_distance + left_distance
# 	return result

# final_pos, final_boxes = simulate_movements(player_pos, boxes, walls, movements)
# result = calculate_gps(final_boxes)
# print(f"Final result: {result}")
