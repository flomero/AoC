from pprint import pprint
import pyperclip
from collections import deque
from functools import lru_cache
import itertools

def printc(arg):
	print(arg)
	pyperclip.copy(str(arg))

day = "21"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1

with open(file, "r") as f:
	rawdata = f.read().splitlines()

numeric_keypad = {
	"7": (0, 0), "8": (0, 1), "9": (0, 2),
	"4": (1, 0), "5": (1, 1), "6": (1, 2),
	"1": (2, 0), "2": (2, 1), "3": (2, 2),
	"0": (3, 1), "A": (3, 2)
}

directional_keypad = {
	"^": (0, 1), 'A': (0, 2),
	"<": (1, 0), "v": (1, 1), ">": (1, 2)
}

keypad = {
	"7": (0, 0), "8": (0, 1), "9": (0, 2),
	"4": (1, 0), "5": (1, 1), "6": (1, 2),
	"1": (2, 0), "2": (2, 1), "3": (2, 2),
	"0": (3, 1), "A": (3, 2),
	"^": (0, 1), 'B': (0, 2),
	"<": (1, 0), "v": (1, 1), ">": (1, 2)
}

dirs = {
	"^": (-1, 0), "<": (0, -1), "v": (1, 0), ">": (0, 1)
}

def checkmoves(start, end, illegal):
	dx, dy = (end[0] - start[0], end[1] - start[1])
	allmoves = "^" * -dx
	allmoves += "v" * dx 
	allmoves += "<" * -dy 
	allmoves += ">" * dy

	moves = []
	for p in set(itertools.permutations(allmoves)):
		position = start
		for move in p:
			position = (position[0] + dirs[move][0], position[1] + dirs[move][1])
			if position == illegal:
				break
		else:
			moves.append("".join(p) + "B")

	return moves or ["B"]


@lru_cache
def find(code, maxiterations, depth):
	if depth == 0:
		cur = keypad["A"]
		illegal = (3, 0)
	else:
		cur = keypad["B"]
		illegal = (0, 0)

	length = 0
	for char in code:
		next = keypad[char]
		moves = checkmoves(cur, next, illegal)

		if depth == maxiterations:
			length += len(moves[0])
		else:
			length += min(find(move, maxiterations, depth + 1) for move in moves)

		cur = next

	return length

result = 0
for code in rawdata:
	numeric = int(code[:-1])
	result += find(code, 2, 0) * numeric
printc(result)

result = 0
for code in rawdata:
	numeric = int(code[:-1])
	result += find(code, 25, 0) * numeric
printc(result)

# def find_shortest_path(start, end, keypad):
# 	queue = deque([(start, "")])
# 	visited = set()
	
# 	while queue:
# 		position, path = queue.popleft()

# 		if position in visited:
# 			continue
# 		visited.add(position)
		
# 		if position == end:
# 			return path
		
# 		for direction, (dx, dy) in [("^", (-1, 0)), ("<", (0, -1)), ("v", (1, 0)), (">", (0, 1))]:
# 			new_x, new_y = position[0] + dx, position[1] + dy
# 			new_position = (new_x, new_y)
			
# 			if new_position in keypad.values():
# 				new_path = path + direction
# 				queue.append((new_position, new_path))
# 	return ""

# @lru_cache
# def findarrowbot(start, end):
# 	queue = deque([(start, "")])
# 	visited = set()
	
# 	while queue:
# 		position, path = queue.popleft()

# 		if position in visited:
# 			continue
# 		visited.add(position)
		
# 		if position == end:
# 			return path
		
# 		for direction, (dx, dy) in [("^", (-1, 0)), ("<", (0, -1)), ("v", (1, 0)), (">", (0, 1))]:
# 			new_x, new_y = position[0] + dx, position[1] + dy
# 			new_position = (new_x, new_y)
			
# 			if new_position in directional_keypad.values():
# 				new_path = path + direction
# 				queue.append((new_position, new_path))
# 	return ""


# def arrowrobot(robot_2_start, target_sequence):
# 	robot_2_current = robot_2_start
# 	full_robot_2_sequence = ""
# 	target_sequence = list(target_sequence)
# 	for index, char in enumerate(target_sequence):
# 		target_position = directional_keypad[char]
# 		robot_2_path = findarrowbot(robot_2_current, target_position)
# 		full_robot_2_sequence += robot_2_path + "A"
# 		robot_2_current = target_position
# 	target_sequence = ''.join(target_sequence)
# 	return full_robot_2_sequence


# def sort_path(path, rep=False):
# 	segments = path.split('A')
	
# 	sorted_segments = []
# 	for segment in segments:
# 		vertical = sorted([d for d in segment if d in "^v"])
# 		horizontal = sorted([d for d in segment if d in "<>"])

# 		sorted_segments.append(''.join(vertical + horizontal))
	
# 	result = []
# 	for i, segment in enumerate(sorted_segments):
# 		result.append(segment)
# 		if i < len(segments) - 1:
# 			result.append('A')

# 	path = ''.join(result)
# 	path = path.replace(">^>", ">>^")
# 	path = path.replace("<v<", "v<<")
# 	path = path.replace("^>>", ">^>")
# 	return path


# result = 0
# start_position = numeric_keypad["A"]
# arrow_start_position = directional_keypad["A"]

# for code in rawdata:
# 	current_position = start_position
# 	numeric_part = int(code[:-1])
	
# 	path = []
# 	for digit in code:
# 		target_position = numeric_keypad[digit]
# 		path_segment = find_shortest_path(current_position, target_position, numeric_keypad)
# 		path.append(path_segment + "A")
# 		current_position = target_position

# 	numeric_keypad_sequence = "".join(path)
# 	numeric_keypad_sequence = sort_path(numeric_keypad_sequence)
# 	print(numeric_keypad_sequence)
# 	arrow_sequence = arrowrobot(arrow_start_position, numeric_keypad_sequence)
# 	print(arrow_sequence)
# 	arrow_start_position = directional_keypad["A"]
# 	arrow_sequence = sort_path(arrow_sequence, True)
# 	print(arrow_sequence)
# 	arrow_sequence = arrowrobot(arrow_start_position, arrow_sequence)
# 	print(arrow_sequence)
# 	# arrow_start_position = directional_keypad["A"]
# 	# arrow_sequence = arrowrobot(arrow_start_position, arrow_sequence)

# 	complexity = (len(arrow_sequence)) * numeric_part
# 	result += complexity

# 	print(len(arrow_sequence))
# 	print(f"Code: {code}")
# 	# print(f"Numeric Keypad Path: {numeric_keypad_sequence}")
# 	# print(f"Arrow Keypad Path: {arrow_sequence}")
# 	print(f"Numeric Part: {numeric_part}, Total Complexity: {complexity}")

# printc(result)

# <v<A>^>A<A>A<AAv>A^A<vAAA^>A
# v<<A>>^A<A>AvA<^AA>A<vAAA>^A
# <v<A>A<A>^>AvA^<Av>A^A<v<A>^>AvA^A<v<A>^>AA<vA>A^A<A>A<v<A>A^>AAA<Av>A^A
# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A

# <v<A>^>AvA^A<v<A>^>AA<vA<A>^>AA<Av>AA^A<vA^>AA<A>A<vA<A>^>AAA<Av>A^A
# <v<A>>^AvA^A<v   A<AA>>^AAvA<^A>AAvA ^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A

# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# <vA<AA>^>AvAA^<A>A<v<A>^>AvA^A<v<A>^>AA<vA>A^A<A>A<vA<A>^>AAA<Av>A^A
# v<<A>>^A<A>AvA<^AA>A<vAAA>^A
# v<<A>>^A<A>A<AAv>A^Av<AAA^>A
# <A^A>^^AvvvA
# <A^A^^>AvvvA