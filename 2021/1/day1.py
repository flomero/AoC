file = "C:/Users/flofi/repos/CodeImAdvent/2021/1/" + "test.txt"

with open(file, "r") as f:
    data = f.read()
    data = data.split("\n")

count = 0

for i in range(len(data)-3):
    prev = int(data[i]) + int(data[i+1]) + int(data[i+2])
    nextOne = int(data[i+1]) + int(data[i+2]) + int(data[i+3])
    if nextOne>prev:
        count = count + 1

print(count)