day = "15"
source = "test"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

input = ""
result = 0

with open(file) as f:
    input = f.read()

input = input.split(",")

def hash(str):
    value = 0
    for i in str: 
        value += ord(i)
        value *= 17
        value %= 256
    return value

for i in input: 
    value = hash(i)
    print(value)
    result += value

print(result)

# Part 2

