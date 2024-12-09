from pprint import pprint

day = "09"
source = "data"
file = f"C:/Users/flofi/repos/CodeImAdvent/2024/{day}/{source}.txt"
part = 1


with open(file, "r") as f:
	data = f.read()

numbers = []
for c in data:
	numbers.append(int(c))

pos = 0
result = 0
i = 0

data = []

for i in range(0, len(numbers)):
	if i % 2 == 0:
		for j in range(numbers[i]):
			data.append(pos)
		pos += 1
	else:
		for j in range(numbers[i]):
			data.append(-1)

# for i in range(0, len(data)):
# 	if data[i] == -1:
# 		for j in range(len(data) - 1, -1, -1):
# 			if data[j] != -1:
# 				data[i] = data[j]
# 				data[j] = -1 
# 				break
# data = [x for x in data if x != -1]

for j in range(len(data) - 1, -1, -1):
	if data[j] != -1:
		block_length = 0
		for k in range(j, -1, -1):
			if data[k] == data[j]:
				block_length += 1
			else:
				break
		for x in range(j + 1, len(data)):
			if data[x] == data[j]:
				block_length += 1
			else:
				break

		for i in range(len(data)):
			if data[i] == -1:
				block_size = 0
				for m in range(i, len(data)):
					if data[m] == -1:
						block_size += 1
					else:
						break
				if block_length <= block_size:
					print(f"Moving File ID {data[j]} of size {block_length} into free block of size {block_size} at {i}")
					start = j - block_length + 1
					if start < i:
						break
					for k in range(block_length):
						data[i + k] = data[start + k]
						data[start + k] = -1
					break

# data = [x for x in data if x != -1]

for i in range(0, len(data)):
	if data[i] == -1:
		continue
	result += data[i] * i
	#print (data[i], i, data[i] * i)

print(data)
print(result)
