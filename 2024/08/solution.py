from pprint import pprint

day = "08"
source = "test"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"

part = 1

with open(file, "r") as f:
	input_text = f.read()

antennas = {}
lines = input_text.strip().split("\n")
for row, line in enumerate(lines):
	for col, char in enumerate(line):
		if char.isalnum():
			frequency = char
			if frequency not in antennas:
				antennas[frequency] = []
			antennas[frequency].append((row, col))

height = len(lines)
width = len(lines[0])

antinodes = set()

def add_antinodes_for_frequency(positions, frequency):
	n = len(positions)
	for i in range(n):
		for j in range(i + 1, n):
			y1, x1 = positions[i]
			y2, x2 = positions[j]
			
			dy = y2 - y1
			dx = x2 - x1
			
			antinode1 = (y1 - dy, x1 - dx, frequency)
			antinode2 = (y2 + dy, x2 + dx, frequency)
			
			if 0 <= antinode1[0] < height and 0 <= antinode1[1] < width:
				antinodes.add(antinode1)
			if 0 <= antinode2[0] < height and 0 <= antinode2[1] < width:
				antinodes.add(antinode2)

def add_antinodes_for_frequency_parttwo(positions, frequency):	
	n = len(positions)
	for i in range(n):
		for j in range(i + 1, n):
			y1, x1 = positions[i]
			y2, x2 = positions[j]
			
			dy = y2 - y1
			dx = x2 - x1

			while 0 <= y1 < height and 0 <= x1 < width:
				antinode = (y1, x1, frequency)
				antinodes.add(antinode)
				y1 += dy
				x1 += dx
			while 0 <= y2 < height and 0 <= x2 < width:
				antinode = (y2, x2, frequency)
				antinodes.add(antinode)
				y2 -= dy
				x2 -= dx

for freq, positions in antennas.items():
	if part == 1:
		add_antinodes_for_frequency(positions, freq)
	elif part == 2:
		add_antinodes_for_frequency_parttwo(positions, freq)
	if len(positions) > 1:
		for pos in positions:
			antinodes.add((pos[0], pos[1], freq))

output_lines = list(lines)

counter = 0
for y, x, origin_freq in antinodes:
	if output_lines[y][x] == ".":
		output_lines[y] = output_lines[y][:x] + "#" + output_lines[y][x+1:]
		counter += 1
	elif output_lines[y][x].isalnum():
			if part == 2 or output_lines[y][x] != origin_freq:
				output_lines[y] = output_lines[y][:x] + "#" + output_lines[y][x+1:]
				counter += 1

pprint(output_lines)
print("Total antinodes:", counter)
