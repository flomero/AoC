file = "C:/Users/flofi/repos/CodeImAdvent/2021/1/" + "data.txt"

with open(file, "r") as f:
    data = f.read()
    data = data.split("\n")

count1 = count2 = 0

for i in range(len(data)-1):
    prev = int(data[i])
    next = int(data[i+1])
    if next > prev:
        count1 = count1 + 1

for i in range(len(data)-3):
    prev = int(data[i]) + int(data[i+1]) + int(data[i+2])
    next = int(data[i+1]) + int(data[i+2]) + int(data[i+3])
    if next >prev:
        count2 = count2 + 1

print(count1)
print(count2)