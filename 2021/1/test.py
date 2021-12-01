file = "C:/Users/flofi/repos/CodeImAdvent/2021/1/" + "test.txt"

my_file = open(file, "r")
content = my_file.read()
numbers = content.split("\n")
my_file.close()
count = 0

for i in range(len(numbers)-3):
    prev = int(numbers[i]) + int(numbers[i+1]) + int(numbers[i+2])
    nextOne = int(numbers[i+1]) + int(numbers[i+2]) + int(numbers[i+3])
    if nextOne>prev:
        count = count + 1

print(count)