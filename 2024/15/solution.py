from pprint import pprint
import pyperclip
import matplotlib.pyplot as plt
import math
import numpy as np

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "15"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

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
for move in movements:
	# print(map)
	print(move)
	dr, dc = directions[move]
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