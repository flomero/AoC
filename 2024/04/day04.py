day = "04"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2024/" + day + "/" + source + ".txt"

import numpy as np

grid = np.array([list(line.strip()) for line in open(file)])
word = "XMAS"

def countw(line, word):
	count = 0
	start = 0
	while True:
		start = line.find(word, start)
		if start == -1:
			break
		count += 1
		start += 1
	start = 0
	while True:
		start = line[::-1].find(word, start)
		if start == -1:
			break
		count += 1
		start += 1
	return count

def search_word(grid, word):
	count = 0

	for row in grid:
		count += countw("".join(row), word)

	for col in grid.T:
		count += countw("".join(col), word)

	for i in range(-grid.shape[0] + 1, grid.shape[1]):
		diag = grid.diagonal(i)
		count += countw("".join(diag), word)

	flipped_grid = np.fliplr(grid)
	for i in range(-flipped_grid.shape[0] + 1, flipped_grid.shape[1]):
		diag = flipped_grid.diagonal(i)
		count += countw("".join(diag), word)

	return count

total_count = search_word(grid, word)
print(total_count)

def matches_pattern(subgrid, pattern):
	for i in range(pattern.shape[0]):
		for j in range(pattern.shape[1]):
			if pattern[i, j] != '.' and subgrid[i, j] != pattern[i, j]:
				return False
	return True

def search_x_mas(grid, pattern):
	rows, cols = grid.shape
	pattern_size = pattern.shape[0]
	count = 0

	for r in range(rows - pattern_size + 1):
		for c in range(cols - pattern_size + 1):
			subgrid = grid[r:r+pattern_size, c:c+pattern_size]
			if matches_pattern(subgrid, pattern):
				count += 1
	return count

patterns = [
	np.array([
		['M', '.', 'S'],
		['.', 'A', '.'],
		['M', '.', 'S']
	]),
	np.array([
		['M', '.', 'M'],
		['.', 'A', '.'],
		['S', '.', 'S']
	]),
	np.array([
		['S', '.', 'M'],
		['.', 'A', '.'],
		['S', '.', 'M']
	]),
	np.array([
		['S', '.', 'S'],
		['.', 'A', '.'],
		['M', '.', 'M']
	]),
]

total_count = 0
for pattern in patterns:
	count = search_x_mas(grid, pattern)
	total_count += count
	print(f"Pattern\n {pattern} found {count} times")

print(f"Total: {total_count}")