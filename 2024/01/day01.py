day = "01"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2024/" + day + "/" + source + ".txt"

left_list = []
right_list = []

with open(file, 'r') as file:
	for line in file:
		left, right = map(int, line.split())
		left_list.append(left)
		right_list.append(right)

left_list.sort()
right_list.sort()

x = 0
for i in range(len(left_list)):
	if left_list[i] < right_list[i]:
		x += right_list[i] - left_list[i]
	else:
		x += left_list[i] - right_list[i]

print(x)

# Part 2

x = 0


for i in range(len(left_list)):
	y = 0
	for j in range(len(right_list)):
		if left_list[i] == right_list[j]:
			y += 1
		if right_list[j] > left_list[i]:
			break
	x += left_list[i] * y

print(x)