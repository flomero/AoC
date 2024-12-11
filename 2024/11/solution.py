from pprint import pprint
import numpy as np
from functools import cache

day = "11"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"

part = 2
result = 0

with open(file, "r") as f:
	data = f.read().splitlines()

if part == 1:
	map_data = np.array([int(num) for line in data for num in line.split()], dtype=object)

	pprint(map_data)

	def has_even_len(number):
		return len(str(abs(number))) % 2 == 0

	def iterate(data):
		new_data = []
		for n in data:
			if n == 0:
				new_data.append(1)
			elif has_even_len(n):
				str_n = str(abs(n))
				half = len(str_n) // 2
				left = int(str_n[:half])
				right = int(str_n[half:])
				new_data.append(left)
				new_data.append(right)
			else:
				new_data.append(n * 2024)
		return np.array(new_data, dtype=object)

	blinks = 0
	max_blinks = 75

	while blinks < max_blinks:
		map_data = iterate(map_data)
		blinks += 1

	result = len(map_data)
	print(result)

elif part == 2:
	map_data = [int(num) for line in data for num in line.split()]
	pprint(map_data)

	@cache
	def count(x, i):
		if i == 0:
			return 1

		if x == 0:
			return count(1, i - 1)

		l = len(str(abs(x)))

		if l % 2 == 0:
			half = l // 2
			left = int(str(x)[:half])
			right = int(str(x)[half:])
			return (
				count(left, i - 1) +
				count(right, i - 1)
			)

		return count(x * 2024, i - 1)

	max_blinks = 75
	result = sum(count(x, max_blinks) for x in map_data)
	print(result)
