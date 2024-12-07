from itertools import product
from collections import defaultdict

day = "07"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2024/" + day + "/" + source + ".txt"

data = defaultdict(list)

with open(file, "r") as f:
	for line in f:
		key, values = line.split(":") 
		key = int(key.strip()) 
		values = list(map(int, values.split())) 
		data[key].append(values)

def is_valid(res, numbers):
	count = len(numbers) - 1
	ops = product("+*|", repeat=count)
	for op in ops:
		expr = str(numbers[0])
		result = numbers[0]
		for i in range(count):
			if op[i] == "+":
				result += numbers[i + 1]
			elif op[i] == "*":
				result *= numbers[i + 1]
			else:
				result = int(str(result) + str(numbers[i + 1]))
		if res == result:
			return True
	return False

result = 0
for key, values_list in data.items():
	for values in values_list:
		if is_valid(key, values):
			result += key

print(result)