day = "06"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2024/" + day + "/" + source + ".txt"

with open(file, "r") as f:
	data = f.read()

array = [[1 if char == '^' else 3 if char == 'v' 
		  else 4 if char == '<' else 2 if char == '>'
		  else -1 if char == '#' else 0 for char in line] 
		 for line in data.strip().split('\n')]

copy = [row[:] for row in array]

print(array)

solution = 0

current_pos = [0, 0]

found = False
for i in range(len(array)):
	for j in range(len(array[i])):
		if array[i][j] != 0 and array[i][j] != -1:
			current_pos = [i, j]
			parttwo_pos = [i, j]
			found = True
			break
	if found:
		break
	
current_orientation = array[current_pos[0]][current_pos[1]]
parttwo_pos = current_pos[:]

def move(pos, direction, array):
	if direction == 1 and pos[0] == 0:
		return pos, -1
	if direction == 2 and pos[1] == len(array[0]) - 1:
		return pos, -1
	if direction == 3 and pos[0] == len(array) - 1:
		return pos, -1
	if direction == 4 and pos[1] == 0:
		return pos, -1

	if direction == 1:
		return [pos[0] - 1, pos[1]], direction
	if direction == 2:
		return [pos[0], pos[1] + 1], direction
	if direction == 3:
		return [pos[0] + 1, pos[1]], direction
	if direction == 4:
		return [pos[0], pos[1] - 1], direction

	return pos, direction

def turn_right(direction):
	return (direction % 4) + 1

def walk(pos, direction, array, visited_states):
	old_pos = pos[:]
	old_direction = direction
	pos, direction = move(pos, direction, array)
	if direction == -1:
		return old_pos, -1
	cell_value = array[pos[0]][pos[1]]
	if cell_value == 0:
		return pos, direction
	elif cell_value == -1:
		return old_pos, turn_right(old_direction)
	state = (pos[0], pos[1], direction)
	if state in visited_states:
		return pos, -2
	visited_states.add(state)
	return pos, direction

visited_states = set()
for i in range(10000):
	current_pos, current_orientation = walk(current_pos, current_orientation, array, visited_states)
	array[current_pos[0]][current_pos[1]] = current_orientation
	if current_orientation == -1:
		array[current_pos[0]][current_pos[1]] = 1
		break

print(array)
solution = sum(cell != 0 for row in array for cell in row) - sum(cell == -1 for row in array for cell in row)
print(solution)

solution = 0
partone = [row[:] for row in array]
array = [row[:] for row in copy]
for i in range(len(array)):
	for j in range(len(array[i])):
		array = [row[:] for row in copy]
		if array[i][j] == 0:
			if partone[i][j] == 0:
				continue
			array[i][j] = -1
			current_orientation = 1
			current_pos = parttwo_pos[:]
			visited_states = set()
			for x in range(1000000):
				current_pos, current_orientation = walk(current_pos, current_orientation, array, visited_states)
				array[current_pos[0]][current_pos[1]] = current_orientation
				if current_orientation == -1:
					break
				if current_orientation == -2:
					solution += 1
					break

print(solution)