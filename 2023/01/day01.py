import re

day = "01"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2023/" + day + "/" + source + ".txt"

part = 2

input = []

# Part 1
result1 = 0

with open(file, "r") as f:
    for line in f:
        input.append(re.sub(r'^(.).*(.)$', r'\1\2', re.sub(r'\D', '', line)))

for i in input:
    if part == 1:
        if len(i) == 2:
            result1 += int(i)
        else:
            result1 += int(i+i)
    
print(result1)

# Part 2
numbers = []
input2 = []
result2 = 0

with open(file, "r") as f:
    for line in f:
        input2.append(line.strip())



def replaceNumbers(input_string):
    number_dict = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e',
        
    }
    pattern = '|'.join(re.escape(key) for key in number_dict.keys())
    # repeating the replacement until no more matches are found
    while True:
        input_string = re.sub(pattern, lambda x: number_dict[x.group()], input_string)
        if not re.search(pattern, input_string):
            break
    return input_string

x = replaceNumbers("eightwothree")
print(x)

for i in input2:
    numbers.append(re.sub(r'^(.).*(.)$', r'\1\2', re.sub(r'\D', '', replaceNumbers(i))))

print(numbers)

for i in numbers:
    if part == 2:
        if len(i) == 2:
            #print(i)
            result2 += int(i)
        else:
            #print(i+i)
            result2 += int(i+i)

print(result2)


