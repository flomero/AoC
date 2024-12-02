day = "02"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2024/" + day + "/" + source + ".txt"

array = []

def is_ascend(arr):
	for i in range(len(arr) - 1):
		if arr[i] > arr[i+1]:
			return False
		elif arr[i] == arr[i+1]:
			return False
		elif arr[i + 1] - arr[i] > 3:
			return False	
	return True

def is_descend(arr):
	for i in range(len(arr) - 1):
		if arr[i] < arr[i+1]:
			return False
		elif arr[i] == arr[i+1]:
			return False
		elif arr[i] - arr[i+1] > 3:
			return False
	return True

with open(file, 'r') as file:
	for line in file:
		row = list(map(int, line.split()))
		array.append(row)

count = 0

for row in array:
	if not is_ascend(row) and not is_descend(row):
		continue
	count += 1

print(count)

def is_safe_with_dampener(arr):
	if is_ascend(arr) or is_descend(arr):
		return True
	for i in range(len(arr)):
		modified_arr = arr[:i] + arr[i+1:]
		if is_ascend(modified_arr) or is_descend(modified_arr):
			return True
	return False

count = 0

for row in array:
	if is_safe_with_dampener(row):
		count += 1

print(count)